#!/usr/bin/env python3
"""Supplement sweep: fetch repos for sources that returned 0 via urllib.
Uses subprocess curl (which correctly picks up the proxy)."""
import json, subprocess, time, hashlib, sys

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
GH_HDR = ["Accept: application/vnd.github.v3+json", "User-Agent: world-increment-sweep/1.0"]

def curl_get(url, extra_headers=None):
    headers = GH_HDR + (extra_headers or [])
    args = ["curl", "-sf", url]
    for h in headers:
        args += ["-H", h]
    r = subprocess.run(args, capture_output=True, text=True, timeout=20)
    if r.returncode != 0 or not r.stdout.strip():
        return None
    try:
        return json.loads(r.stdout)
    except:
        return None

def duckdb_exec(sql):
    r = subprocess.run(["duckdb", DB], input=sql, capture_output=True, text=True)
    if r.returncode != 0 and r.stderr:
        print(f"  DDB ERR: {r.stderr[:200]}", file=sys.stderr)
    return r.stdout.strip()

def duckdb_batch(statements):
    if not statements:
        return
    sql = ";\n".join(statements) + ";"
    return duckdb_exec(sql)

def snap_hash(s):
    return hashlib.sha1(s.encode()).hexdigest()[:12]

def gf3(n):
    m = n % 3
    if m == 0: return (0, "#d3869b", "ERGODIC")
    if m == 1: return (1, "#b8bb26", "PLUS")
    return (-1, "#cc241d", "MINUS")

# Check which sources already have repos
existing = duckdb_exec("""
SELECT wi.id, wi.source_name, COUNT(rs.id) as repo_count
FROM world_increments wi
LEFT JOIN repo_snapshots rs ON rs.increment_id = wi.id
WHERE wi.id >= 470
GROUP BY wi.id, wi.source_name
ORDER BY wi.id;
""")
print("Current state of sweep increments:")
print(existing)

# Get the increment IDs and source names for sources with 0 repos
rows_raw = duckdb_exec("""
SELECT wi.id, wi.source_name, wi.source_type
FROM world_increments wi
LEFT JOIN repo_snapshots rs ON rs.increment_id = wi.id
WHERE wi.id >= 470
GROUP BY wi.id, wi.source_name, wi.source_type
HAVING COUNT(rs.id) = 0
ORDER BY wi.id;
""")
print("\nSources with 0 repos (to supplement):")
print(rows_raw)

# Parse the DuckDB table output
import re
sources_to_fix = []
for line in rows_raw.splitlines():
    line = line.strip()
    # match lines like: │ 471 │ kubeflow  │ org   │
    m = re.match(r'│\s*(\d+)\s*│\s*(\S+)\s*│\s*(\S+)\s*│', line)
    if m:
        inc_id = int(m.group(1))
        src_name = m.group(2)
        src_type = m.group(3)
        sources_to_fix.append((inc_id, src_name, src_type))

print(f"\nWill supplement {len(sources_to_fix)} sources: {[s[1] for s in sources_to_fix]}")

# Get next repo_id
r = duckdb_exec("SELECT COALESCE(MAX(id),0)+1 FROM repo_snapshots;")
lines = [l.strip() for l in r.splitlines() if l.strip()]
repo_id = 1
for l in lines:
    val = l.replace("│","").strip()
    try:
        repo_id = int(val); break
    except: pass

print(f"Next repo_id: {repo_id}")

total_repos = 0
for (inc_id, src_name, src_type) in sources_to_fix:
    kind = "orgs" if src_type == "org" else "users"
    url = f"https://api.github.com/{kind}/{src_name}/repos?per_page=100&sort=pushed"
    print(f"  Fetching {kind}/{src_name} ...", end=" ", flush=True)
    repos = curl_get(url) or []
    if not isinstance(repos, list):
        repos = []
    print(f"{len(repos)} repos")

    inserts = []
    for repo in repos:
        lang = (repo.get("language") or "").replace("'","''")[:40]
        desc = (repo.get("description") or "").replace("'","''")[:120].replace("\n"," ")
        full_name = repo.get("full_name","").replace("'","''")
        repo_name = repo.get("name","").replace("'","''")
        pushed = (repo.get("pushed_at") or "")[:10]
        inserts.append(
            f"INSERT INTO repo_snapshots VALUES ({repo_id}, now(), {inc_id}, "
            f"'{src_name}', '{repo_name}', '{full_name}', '{lang}', "
            f"{repo.get('stargazers_count',0)}, {repo.get('forks_count',0)}, "
            f"{repo.get('open_issues_count',0)}, '{pushed}', '{desc}')"
        )
        repo_id += 1

    if inserts:
        CHUNK = 50
        for i in range(0, len(inserts), CHUNK):
            duckdb_batch(inserts[i:i+CHUNK])
        total_repos += len(inserts)
    time.sleep(0.5)

print(f"\nSupplemented {total_repos} additional repos.")

# Final counts
counts = duckdb_exec("""
SELECT 'world_increments' as t, COUNT(*) as n FROM world_increments
UNION ALL SELECT 'repo_snapshots', COUNT(*) FROM repo_snapshots;
""")
print("\nFinal counts:")
print(counts)

# Show breakdown by source for this sweep
breakdown = duckdb_exec("""
SELECT wi.source_name, COUNT(rs.id) as repos, wi.gf3_name, wi.gf3_color
FROM world_increments wi
LEFT JOIN repo_snapshots rs ON rs.increment_id = wi.id
WHERE wi.id >= 470
GROUP BY wi.id, wi.source_name, wi.gf3_name, wi.gf3_color
ORDER BY wi.id;
""")
print("\nSweep breakdown:")
print(breakdown)
