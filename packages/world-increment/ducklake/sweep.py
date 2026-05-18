#!/usr/bin/env python3
"""World-increment sweep + Hamming swarm snapshot."""
import json
import time
import datetime
import hashlib
import os
import requests
import duckdb

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
HEADERS = {"Accept": "application/vnd.github.v3+json", "User-Agent": "world-increment-sweep/1.0"}

GF3_COLORS = {0: ("#d3869b", "ERGODIC"), 1: ("#b8bb26", "PLUS"), 2: ("#cc241d", "MINUS")}
GF3_TRITS  = {0: 0, 1: 1, 2: -1}

def gf3(n):
    mod = n % 3
    color, name = GF3_COLORS[mod]
    return GF3_TRITS[mod], color, name

def snap_hash(*parts):
    return hashlib.sha256("|".join(str(p) for p in parts).encode()).hexdigest()[:16]

# ── DB setup ─────────────────────────────────────────────────────────────────
con = duckdb.connect(DB_PATH)
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
try:
    con.execute("CREATE SEQUENCE IF NOT EXISTS increment_seq START 1")
    con.execute("CREATE SEQUENCE IF NOT EXISTS repo_seq START 1")
except Exception:
    pass

def next_inc():
    return con.execute("SELECT nextval('increment_seq')").fetchone()[0]

def next_repo():
    return con.execute("SELECT nextval('repo_seq')").fetchone()[0]

# ── JOB 1: GitHub sweep ───────────────────────────────────────────────────────
ORGS  = ["plurigrid", "kubeflow", "TeglonLabs"]
USERS = ["bmorphism", "zubyul", "migalkin", "DJedamski", "wasita",
         "kristinezheng", "M1shaaa", "AustinCStone"]

def fetch_repos(kind, name):
    url = f"https://api.github.com/{'orgs' if kind=='org' else 'users'}/{name}/repos?per_page=100&sort=pushed"
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            return r.json()
        print(f"  [{name}] HTTP {r.status_code}")
        return []
    except Exception as e:
        print(f"  [{name}] error: {e}")
        return []

def fetch_events(user):
    url = f"https://api.github.com/users/{user}/events/public?per_page=30"
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        return r.json() if r.status_code == 200 else []
    except Exception:
        return []

total_repos = 0
now_ts = datetime.datetime.utcnow().isoformat()

print("=== JOB 1: GitHub Social Graph Sweep ===")

for org in ORGS:
    print(f"Fetching org: {org}")
    repos = fetch_repos("org", org)
    print(f"  {len(repos)} repos")
    for repo in repos:
        inc_id = next_inc()
        trit, color, gf3name = gf3(inc_id)
        sh = snap_hash(org, repo.get("full_name",""), repo.get("pushed_at",""))
        con.execute("""INSERT INTO world_increments VALUES (?,now(),?,?,?,'org',?,?,?,?,?)""",
            [inc_id, trit, color, gf3name, org, "repo_push",
             repo.get("name",""), org, sh])
        repo_id = next_repo()
        con.execute("""INSERT INTO repo_snapshots VALUES (?,now(),?,?,?,?,?,?,?,?,?,?)""",
            [repo_id, inc_id, org, repo.get("name",""), repo.get("full_name",""),
             repo.get("language"), repo.get("stargazers_count",0),
             repo.get("forks_count",0), repo.get("open_issues_count",0),
             repo.get("pushed_at",""), (repo.get("description") or "")[:200]])
        total_repos += 1
    time.sleep(0.5)

for user in USERS:
    print(f"Fetching user: {user}")
    repos = fetch_repos("user", user)
    print(f"  {len(repos)} repos")
    for repo in repos:
        inc_id = next_inc()
        trit, color, gf3name = gf3(inc_id)
        sh = snap_hash(user, repo.get("full_name",""), repo.get("pushed_at",""))
        con.execute("""INSERT INTO world_increments VALUES (?,now(),?,?,?,'user',?,?,?,?,?)""",
            [inc_id, trit, color, gf3name, user, "repo_push",
             repo.get("name",""), user, sh])
        repo_id = next_repo()
        con.execute("""INSERT INTO repo_snapshots VALUES (?,now(),?,?,?,?,?,?,?,?,?,?)""",
            [repo_id, inc_id, user, repo.get("name",""), repo.get("full_name",""),
             repo.get("language"), repo.get("stargazers_count",0),
             repo.get("forks_count",0), repo.get("open_issues_count",0),
             repo.get("pushed_at",""), (repo.get("description") or "")[:200]])
        total_repos += 1
    time.sleep(0.5)

# Events for bmorphism and zubyul
for user in ["bmorphism", "zubyul"]:
    print(f"Fetching events: {user}")
    events = fetch_events(user)
    print(f"  {len(events)} events")
    for ev in events:
        inc_id = next_inc()
        trit, color, gf3name = gf3(inc_id)
        repo_name = ev.get("repo", {}).get("name", "")
        ev_type = ev.get("type", "")
        actor = ev.get("actor", {}).get("login", user)
        sh = snap_hash(user, ev_type, ev.get("id",""), repo_name)
        con.execute("""INSERT INTO world_increments VALUES (?,now(),?,?,?,'event',?,?,?,?,?)""",
            [inc_id, trit, color, gf3name, user, ev_type, repo_name, actor, sh])
    time.sleep(0.5)

print(f"Total repos inserted: {total_repos}")

# ── JOB 2: Aptos Hamming Swarm ────────────────────────────────────────────────
print("\n=== JOB 2: Hamming Swarm Snapshot ===")

APTOS_BASE = "https://fullnode.mainnet.aptoslabs.com/v1"

WALLETS = {
    "alice": "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b",
    "bob":   "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d",
    "A":     "0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a",
    "B":     "0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13",
    "C":     "0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e",
    "D":     "0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1",
    "E":     "0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36",
    "F":     "0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71",
    "G":     "0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32",
    "H":     "0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f",
    "I":     "0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9",
    "J":     "0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54",
    "K":     "0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4",
    "L":     "0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9",
    "M":     "0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9",
    "N":     "0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c",
    "O":     "0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d",
    "P":     "0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948",
    "Q":     "0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9",
    "R":     "0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10",
    "S":     "0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386",
    "T":     "0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588",
    "U":     "0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956",
    "V":     "0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3",
    "W":     "0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0",
    "X":     "0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d",
    "Y":     "0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4",
    "Z":     "0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c",
}

aptos_balances = {}
COIN_RESOURCE = "0x1::coin::CoinStore%3C0x1::aptos_coin::AptosCoin%3E"

for world, addr in WALLETS.items():
    url = f"{APTOS_BASE}/accounts/{addr}/resource/{COIN_RESOURCE}"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            val = int(r.json()["data"]["coin"]["value"])
            apt = val / 1e8
        else:
            apt = None
    except Exception:
        apt = None
    aptos_balances[world] = apt
    status = f"{apt:.4f} APT" if apt is not None else "not found"
    print(f"  {world}: {status}")
    con.execute("INSERT INTO aptos_snapshots VALUES (now(),?,?,?)",
                [world, addr, apt])
    time.sleep(1)

# ── Multisig probes ────────────────────────────────────────────────────────────
print("\n=== Multisig Probes ===")
MULTISIGS = {
    "A-B": "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",
    "A-G": "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",
    "Y-Z": "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",
    "S-T": "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",
    "V-W": "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",
}

for pair, addr in MULTISIGS.items():
    payload = {
        "function": "0x1::multisig_account::num_signatures_required",
        "type_arguments": [],
        "arguments": [addr]
    }
    try:
        r = requests.post(f"{APTOS_BASE}/view", json=payload, timeout=10)
        if r.status_code == 200:
            data = r.json()
            sigs = int(data[0]) if data else 0
            healthy = sigs > 0
        else:
            sigs = 0
            healthy = False
        print(f"  {pair}: sigs_required={sigs}, healthy={healthy}")
    except Exception as e:
        sigs = 0
        healthy = False
        print(f"  {pair}: error {e}")
    con.execute("INSERT INTO multisig_probes VALUES (now(),?,?,?,?)",
                [pair, addr, sigs, healthy])
    time.sleep(1)

# ── MNX Markets ───────────────────────────────────────────────────────────────
print("\n=== MNX Markets ===")
mnx_data = []
mnx_paths = [
    "https://testnet.mnx.fi/api/markets",
    "https://testnet.mnx.fi/api/tickers",
    "https://testnet.mnx.fi/api/v1/markets",
    "https://testnet.mnx.fi/api/v1/tickers",
]
for url in mnx_paths:
    try:
        r = requests.get(url, timeout=10, headers={"User-Agent": "world-increment-sweep/1.0"})
        if r.status_code == 200:
            try:
                data = r.json()
                print(f"  Got data from {url}: {str(data)[:200]}")
                if isinstance(data, list):
                    mnx_data = data
                elif isinstance(data, dict):
                    mnx_data = data.get("markets", data.get("tickers", [data]))
                break
            except Exception:
                print(f"  {url}: non-JSON response")
        else:
            print(f"  {url}: HTTP {r.status_code}")
    except Exception as e:
        print(f"  {url}: {e}")
    time.sleep(0.5)

if not mnx_data:
    print("  MNX Markets unavailable — inserting sentinel row")
    con.execute("INSERT INTO mnx_snapshots VALUES (now(),?,?,?,?,?)",
                ["N/A", "unavailable", "N/A", 0.0, 0.0])
else:
    for m in mnx_data:
        if not isinstance(m, dict):
            continue
        ticker = m.get("ticker", m.get("symbol", m.get("id", "?")))
        name = m.get("name", ticker)
        category = m.get("category", m.get("type", "unknown"))
        price = float(m.get("price", m.get("last", 0)) or 0)
        change_pct = float(m.get("change_pct", m.get("change", 0)) or 0)
        con.execute("INSERT INTO mnx_snapshots VALUES (now(),?,?,?,?,?)",
                    [ticker, name, category, price, change_pct])

# ── Summary stats ─────────────────────────────────────────────────────────────
inc_count = con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0]
repo_count = con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0]
aptos_count = con.execute("SELECT COUNT(*) FROM aptos_snapshots WHERE balance_apt IS NOT NULL").fetchone()[0]
aptos_total = con.execute("SELECT COALESCE(SUM(balance_apt),0) FROM aptos_snapshots").fetchone()[0]
ms_healthy = con.execute("SELECT COUNT(*) FROM multisig_probes WHERE healthy=true").fetchone()[0]
ms_total = con.execute("SELECT COUNT(*) FROM multisig_probes").fetchone()[0]

gf3_dist = con.execute("""
  SELECT gf3_name, COUNT(*) as cnt FROM world_increments GROUP BY gf3_name ORDER BY gf3_name
""").fetchall()

top_langs = con.execute("""
  SELECT language, COUNT(*) as cnt FROM repo_snapshots
  WHERE language IS NOT NULL GROUP BY language ORDER BY cnt DESC LIMIT 8
""").fetchall()

top_stars = con.execute("""
  SELECT full_name, stars FROM repo_snapshots ORDER BY stars DESC LIMIT 10
""").fetchall()

aptos_rows = con.execute("""
  SELECT world, address, balance_apt FROM aptos_snapshots ORDER BY world
""").fetchall()

ms_rows = con.execute("""
  SELECT pair, address, sigs_required, healthy FROM multisig_probes ORDER BY pair
""").fetchall()

con.close()

# ── Write LATEST_SWEEP.md ─────────────────────────────────────────────────────
sweep_date = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

md_lines = [
f"# World-Increment Sweep + Hamming Snapshot",
f"",
f"**Date:** {sweep_date}",
f"",
f"---",
f"",
f"## JOB 1: GitHub Social Graph Sweep",
f"",
f"| Metric | Value |",
f"|--------|-------|",
f"| World increments | {inc_count} |",
f"| Repo snapshots | {repo_count} |",
f"",
f"### GF(3) Color Chain Distribution",
f"",
f"| GF3 Name | Color | Count |",
f"|----------|-------|-------|",
]
for name, cnt in gf3_dist:
    if name == "ERGODIC":
        color = "#d3869b"
    elif name == "PLUS":
        color = "#b8bb26"
    else:
        color = "#cc241d"
    md_lines.append(f"| {name} | `{color}` | {cnt} |")

md_lines += [
f"",
f"### Top Languages",
f"",
f"| Language | Repos |",
f"|----------|-------|",
]
for lang, cnt in top_langs:
    md_lines.append(f"| {lang} | {cnt} |")

md_lines += [
f"",
f"### Top Starred Repos",
f"",
f"| Repo | Stars |",
f"|------|-------|",
]
for full_name, stars in top_stars:
    md_lines.append(f"| {full_name} | {stars} |")

md_lines += [
f"",
f"---",
f"",
f"## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)",
f"",
f"| Metric | Value |",
f"|--------|-------|",
f"| Wallets probed | {len(WALLETS)} |",
f"| Wallets found | {aptos_count} |",
f"| Total APT (visible) | {aptos_total:.4f} |",
f"| Multisig healthy | {ms_healthy}/{ms_total} |",
f"",
f"### Wallet Balances",
f"",
f"| World | Address (truncated) | Balance (APT) |",
f"|-------|---------------------|---------------|",
]
for world, addr, bal in aptos_rows:
    short = addr[:10] + "..." + addr[-6:]
    bal_str = f"{bal:.4f}" if bal is not None else "not found"
    md_lines.append(f"| {world} | `{short}` | {bal_str} |")

md_lines += [
f"",
f"### Multisig Probes",
f"",
f"| Pair | Address (truncated) | Sigs Required | Healthy |",
f"|------|---------------------|---------------|---------|",
]
for pair, addr, sigs, healthy in ms_rows:
    short = addr[:10] + "..." + addr[-6:]
    h_str = "✓" if healthy else "✗"
    md_lines.append(f"| {pair} | `{short}` | {sigs} | {h_str} |")

md_lines += [
f"",
f"### MNX Markets",
f"",
f"Data availability: {'available' if mnx_data else 'unavailable (testnet SPA, no public API endpoints found)'}",
f"",
f"---",
f"",
f"*Generated by world-increment-sweep + hamming-swarm-snapshot agent.*",
]

summary_path = "/home/user/gorj/packages/world-increment/ducklake/LATEST_SWEEP.md"
with open(summary_path, "w") as f:
    f.write("\n".join(md_lines) + "\n")

print(f"\n=== Summary written to {summary_path} ===")
print(f"Increments: {inc_count}, Repos: {repo_count}, Aptos wallets found: {aptos_count}, Multisig healthy: {ms_healthy}/{ms_total}")
