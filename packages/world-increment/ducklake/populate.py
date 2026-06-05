#!/usr/bin/env python3
"""Populate world-increments DuckDB with GitHub + Aptos snapshot data."""
import duckdb, json, hashlib, sys
from datetime import datetime

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
con = duckdb.connect(DB)

con.execute("""
CREATE TABLE IF NOT EXISTS world_increments (
  id INTEGER, timestamp TIMESTAMP DEFAULT now(), gf3_trit INTEGER,
  gf3_color VARCHAR, gf3_name VARCHAR, source_type VARCHAR,
  source_name VARCHAR, event_type VARCHAR, repo_name VARCHAR,
  actor VARCHAR, snapshot_hash VARCHAR
)""")
con.execute("""
CREATE TABLE IF NOT EXISTS repo_snapshots (
  id INTEGER, timestamp TIMESTAMP DEFAULT now(), increment_id INTEGER,
  org_or_user VARCHAR, repo_name VARCHAR, full_name VARCHAR,
  language VARCHAR, stars INTEGER, forks INTEGER, open_issues INTEGER,
  pushed_at VARCHAR, description VARCHAR
)""")
con.execute("""
CREATE TABLE IF NOT EXISTS aptos_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  world VARCHAR, address VARCHAR, balance_apt DOUBLE
)""")
con.execute("""
CREATE TABLE IF NOT EXISTS multisig_probes (
  timestamp TIMESTAMP DEFAULT now(),
  pair VARCHAR, address VARCHAR, sigs_required INTEGER, healthy BOOLEAN
)""")
con.execute("""
CREATE TABLE IF NOT EXISTS mnx_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  ticker VARCHAR, name VARCHAR, category VARCHAR,
  price DOUBLE, change_pct DOUBLE
)""")

try: con.execute("CREATE SEQUENCE IF NOT EXISTS increment_seq START 1")
except: pass
try: con.execute("CREATE SEQUENCE IF NOT EXISTS repo_seq START 1")
except: pass

GF3 = {0: (0, "#d3869b", "ERGODIC"), 1: (1, "#b8bb26", "PLUS"), 2: (-1, "#cc241d", "MINUS")}

def gf3(n):
    t = n % 3
    trit, color, name = GF3[t]
    return trit, color, name

def snap_hash(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()[:16]

# ── REPO DATA ─────────────────────────────────────────────────────────────────
repos = json.loads(sys.argv[1])
ts = datetime.utcnow().isoformat()

inc_id = 1
repo_id = 1
for r in repos:
    trit, color, name = gf3(inc_id)
    h = snap_hash(r)
    con.execute("""INSERT INTO world_increments VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
        [inc_id, ts, trit, color, name, "github_repo", r["org_or_user"],
         "repo_snapshot", r["repo_name"], r["org_or_user"], h])
    con.execute("""INSERT INTO repo_snapshots VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
        [repo_id, ts, inc_id, r["org_or_user"], r["repo_name"], r["full_name"],
         r.get("language"), r.get("stars", 0), r.get("forks", 0),
         r.get("open_issues", 0), r.get("pushed_at"), r.get("description")])
    inc_id += 1
    repo_id += 1

# ── APTOS SNAPSHOTS ───────────────────────────────────────────────────────────
aptos = json.loads(sys.argv[2])
for a in aptos:
    con.execute("INSERT INTO aptos_snapshots VALUES (?,?,?,?)",
        [ts, a["world"], a["address"], float(a["balance"])])

# ── MULTISIG PROBES ───────────────────────────────────────────────────────────
multisig = json.loads(sys.argv[3])
for m in multisig:
    con.execute("INSERT INTO multisig_probes VALUES (?,?,?,?,?)",
        [ts, m["pair"], m["address"], int(m["sigs"]), m["healthy"] == "true"])

con.commit()

# ── SUMMARY STATS ─────────────────────────────────────────────────────────────
total_repos = con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0]
total_inc = con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0]
total_aptos = con.execute("SELECT COUNT(*) FROM aptos_snapshots").fetchone()[0]
top_stars = con.execute("""
  SELECT full_name, stars FROM repo_snapshots ORDER BY stars DESC LIMIT 5
""").fetchall()
by_lang = con.execute("""
  SELECT language, COUNT(*) as cnt FROM repo_snapshots
  WHERE language IS NOT NULL GROUP BY language ORDER BY cnt DESC LIMIT 8
""").fetchall()
multisig_health = con.execute("""
  SELECT pair, sigs_required, healthy FROM multisig_probes ORDER BY pair
""").fetchall()
gf3_dist = con.execute("""
  SELECT gf3_name, gf3_color, COUNT(*) FROM world_increments GROUP BY gf3_name, gf3_color ORDER BY gf3_name
""").fetchall()

con.close()
print(json.dumps({
    "total_repos": total_repos,
    "total_increments": total_inc,
    "total_aptos": total_aptos,
    "top_stars": [{"repo": r[0], "stars": r[1]} for r in top_stars],
    "by_language": [{"lang": l[0], "count": l[1]} for l in by_lang],
    "multisig": [{"pair": m[0], "sigs": m[1], "healthy": m[2]} for m in multisig_health],
    "gf3_distribution": [{"name": g[0], "color": g[1], "count": g[2]} for g in gf3_dist],
}))
