#!/usr/bin/env python3
"""World Increment + Hamming Swarm Sweep Script"""

import json
import subprocess
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
DUCKDB = "/usr/local/bin/duckdb"

def duckdb_exec(sql):
    result = subprocess.run(
        [DUCKDB, DB_PATH, sql],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"DuckDB error: {result.stderr}")
    return result.stdout.strip()

def duckdb_exec_multi(sql_lines):
    combined = "\n".join(sql_lines)
    result = subprocess.run(
        [DUCKDB, DB_PATH, combined],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"DuckDB error: {result.stderr}")
    return result.stdout.strip()

def http_get(url, timeout=15):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print(f"  GET {url} -> error: {e}")
        return None

def http_post(url, data, timeout=15):
    try:
        body = json.dumps(data).encode()
        req = urllib.request.Request(url, data=body, headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        })
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print(f"  POST {url} -> error: {e}")
        return None

def esc(s):
    if s is None:
        return ""
    return str(s).replace("'", "''")

def gf3_info(n):
    r = n % 3
    if r == 0:
        return (0, '#d3869b', 'ERGODIC')
    elif r == 1:
        return (1, '#b8bb26', 'PLUS')
    else:
        return (-1, '#cc241d', 'MINUS')

# ============================================================
# SETUP TABLES
# ============================================================
print("=== Setting up DuckDB tables ===")
setup_sql = """
CREATE TABLE IF NOT EXISTS world_increments (
  id INTEGER, timestamp TIMESTAMP DEFAULT now(), gf3_trit INTEGER,
  gf3_color VARCHAR, gf3_name VARCHAR, source_type VARCHAR,
  source_name VARCHAR, event_type VARCHAR, repo_name VARCHAR,
  actor VARCHAR, snapshot_hash VARCHAR
);
CREATE TABLE IF NOT EXISTS repo_snapshots (
  id INTEGER, timestamp TIMESTAMP DEFAULT now(), increment_id INTEGER,
  org_or_user VARCHAR, repo_name VARCHAR, full_name VARCHAR,
  language VARCHAR, stars INTEGER, forks INTEGER, open_issues INTEGER,
  pushed_at VARCHAR, description VARCHAR
);
CREATE SEQUENCE IF NOT EXISTS increment_seq START 1;
CREATE SEQUENCE IF NOT EXISTS repo_seq START 1;
CREATE TABLE IF NOT EXISTS aptos_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  world VARCHAR, address VARCHAR, balance_apt DOUBLE
);
CREATE TABLE IF NOT EXISTS multisig_probes (
  timestamp TIMESTAMP DEFAULT now(),
  pair VARCHAR, address VARCHAR, sigs_required INTEGER, healthy BOOLEAN
);
CREATE TABLE IF NOT EXISTS mnx_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  ticker VARCHAR, name VARCHAR, category VARCHAR,
  price DOUBLE, change_pct DOUBLE
);
"""
duckdb_exec(setup_sql)
print("Tables created.")

# ============================================================
# JOB 1: GITHUB SOCIAL GRAPH
# ============================================================
print("\n=== JOB 1: GitHub Social Graph Sweep ===")

ORGS = ["plurigrid", "kubeflow", "TeglonLabs"]
USERS = ["bmorphism", "zubyul", "migalkin", "DJedamski", "wasita", "kristinezheng", "M1shaaa", "AustinCStone"]
EVENT_USERS = ["bmorphism", "zubyul"]

all_repos = []  # (source_type, source_name, repo_data)

# Fetch org repos
for org in ORGS:
    print(f"  Fetching org: {org}")
    data = http_get(f"https://api.github.com/orgs/{org}/repos?per_page=100&sort=pushed")
    if data and isinstance(data, list):
        for r in data:
            all_repos.append(("org", org, r))
        print(f"    -> {len(data)} repos")
    time.sleep(0.5)

# Fetch user repos
for user in USERS:
    print(f"  Fetching user: {user}")
    data = http_get(f"https://api.github.com/users/{user}/repos?per_page=100&sort=pushed")
    if data and isinstance(data, list):
        for r in data:
            all_repos.append(("user", user, r))
        print(f"    -> {len(data)} repos")
    time.sleep(0.5)

# Fetch events (for world_increments)
all_events = []
for user in EVENT_USERS:
    print(f"  Fetching events: {user}")
    data = http_get(f"https://api.github.com/users/{user}/events/public?per_page=30")
    if data and isinstance(data, list):
        all_events.extend([(user, e) for e in data])
        print(f"    -> {len(data)} events")
    time.sleep(0.5)

print(f"\nTotal repos collected: {len(all_repos)}")
print(f"Total events collected: {len(all_events)}")

# Insert world_increments for each source
print("\n  Inserting world_increments...")
increment_counter = 0

sources = [("org", o) for o in ORGS] + [("user", u) for u in USERS]
for stype, sname in sources:
    increment_counter += 1
    iid = increment_counter
    trit, color, gname = gf3_info(iid)
    sql = f"""
INSERT INTO world_increments (id, gf3_trit, gf3_color, gf3_name, source_type, source_name, event_type, repo_name, actor, snapshot_hash)
VALUES (
  {iid}, {trit}, '{color}', '{gname}', '{stype}', '{esc(sname)}',
  'repo_scan', '', '{esc(sname)}', '{esc(sname + '_' + str(iid))}'
);
"""
    duckdb_exec(sql)

# Insert events as world_increments
for user, evt in all_events[:20]:  # cap at 20 events
    increment_counter += 1
    iid = increment_counter
    trit, color, gname = gf3_info(iid)
    etype = esc(evt.get("type", ""))
    rname = esc((evt.get("repo") or {}).get("name", ""))
    actor = esc((evt.get("actor") or {}).get("login", user))
    sql = f"""
INSERT INTO world_increments (id, gf3_trit, gf3_color, gf3_name, source_type, source_name, event_type, repo_name, actor, snapshot_hash)
VALUES (
  {iid}, {trit}, '{color}', '{gname}', 'event', '{esc(user)}',
  '{etype}', '{rname}', '{actor}', '{esc(user + '_evt_' + str(iid))}'
);
"""
    duckdb_exec(sql)

print(f"  Inserted {increment_counter} world_increments")

# Insert repo_snapshots
print("  Inserting repo_snapshots...")
repo_counter = 0
# Deduplicate by full_name
seen_repos = set()
for stype, sname, r in all_repos:
    fn = r.get("full_name", "")
    if fn in seen_repos:
        continue
    seen_repos.add(fn)
    repo_counter += 1
    rid = repo_counter
    # Find associated increment_id
    inc_id = 1  # default
    for i, (st, sn) in enumerate(sources, 1):
        if st == stype and sn == sname:
            inc_id = i
            break
    lang = esc(r.get("language") or "")
    stars = r.get("stargazers_count", 0) or 0
    forks = r.get("forks_count", 0) or 0
    issues = r.get("open_issues_count", 0) or 0
    pushed = esc(r.get("pushed_at") or "")
    desc = esc((r.get("description") or "")[:200])
    rname = esc(r.get("name", ""))
    full_name = esc(fn)
    ou = esc(sname)
    sql = f"""
INSERT INTO repo_snapshots (id, increment_id, org_or_user, repo_name, full_name, language, stars, forks, open_issues, pushed_at, description)
VALUES (
  {rid}, {inc_id}, '{ou}', '{rname}', '{full_name}',
  '{lang}', {stars}, {forks}, {issues}, '{pushed}', '{desc}'
);
"""
    duckdb_exec(sql)

print(f"  Inserted {repo_counter} repo_snapshots")

# ============================================================
# JOB 2: HAMMING SWARM SNAPSHOT
# ============================================================
print("\n=== JOB 2: Hamming Swarm Snapshot ===")

# Aptos wallet addresses
WALLETS = {
    "alice": "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b",
    "bob":   "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d",
    "A": "0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a",
    "B": "0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13",
    "C": "0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e",
    "D": "0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1",
    "E": "0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36",
    "F": "0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71",
    "G": "0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32",
    "H": "0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f",
    "I": "0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9",
    "J": "0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54",
    "K": "0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4",
    "L": "0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9",
    "M": "0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9",
    "N": "0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c",
    "O": "0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d",
    "P": "0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948",
    "Q": "0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9",
    "R": "0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10",
    "S": "0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386",
    "T": "0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588",
    "U": "0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956",
    "V": "0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3",
    "W": "0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0",
    "X": "0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d",
    "Y": "0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4",
    "Z": "0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c",
}

print("  Fetching Aptos balances...")
aptos_data = []
for world_label, addr in WALLETS.items():
    url = f"https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore%3C0x1::aptos_coin::AptosCoin%3E"
    data = http_get(url, timeout=10)
    balance = 0.0
    if data and isinstance(data, dict):
        try:
            raw = data.get("data", {}).get("coin", {}).get("value", "0")
            balance = int(raw) / 100_000_000
        except Exception:
            balance = 0.0
    aptos_data.append((world_label, addr, balance))
    print(f"    {world_label}: {balance:.4f} APT")
    time.sleep(1)

print("  Inserting Aptos snapshots...")
for world_label, addr, balance in aptos_data:
    sql = f"""
INSERT INTO aptos_snapshots (world, address, balance_apt)
VALUES ('{esc(world_label)}', '{esc(addr)}', {balance});
"""
    duckdb_exec(sql)

# Multisig probes
MULTISIG_PAIRS = {
    "A-B": "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",
    "A-G": "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",
    "Y-Z": "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",
    "S-T": "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",
    "V-W": "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",
}

print("\n  Probing multisig contracts...")
multisig_data = []
for pair, addr in MULTISIG_PAIRS.items():
    resp = http_post(
        "https://fullnode.mainnet.aptoslabs.com/v1/view",
        {"function": "0x1::multisig_account::num_signatures_required",
         "type_arguments": [], "arguments": [addr]},
        timeout=10
    )
    sigs = 0
    healthy = False
    if resp and isinstance(resp, list) and len(resp) > 0:
        try:
            sigs = int(resp[0])
            healthy = sigs >= 1
        except Exception:
            pass
    print(f"    {pair} ({addr[:10]}...): sigs_required={sigs}, healthy={healthy}")
    multisig_data.append((pair, addr, sigs, healthy))
    time.sleep(0.5)

print("  Inserting multisig probes...")
for pair, addr, sigs, healthy in multisig_data:
    sql = f"""
INSERT INTO multisig_probes (pair, address, sigs_required, healthy)
VALUES ('{esc(pair)}', '{esc(addr)}', {sigs}, {'true' if healthy else 'false'});
"""
    duckdb_exec(sql)

# MNX Markets
print("\n  Probing MNX markets...")
mnx_endpoints = [
    "https://testnet.mnx.fi/api/markets",
    "https://testnet.mnx.fi/api/v1/markets",
    "https://testnet.mnx.fi/api/tickers",
]
mnx_available = False
mnx_data = []
for ep in mnx_endpoints:
    data = http_get(ep, timeout=10)
    if data:
        print(f"    MNX endpoint {ep} -> got data")
        mnx_available = True
        # Try to parse market data
        items = data if isinstance(data, list) else data.get("markets", data.get("data", []))
        if isinstance(items, list):
            for item in items[:20]:
                ticker = esc(item.get("ticker") or item.get("symbol") or item.get("id") or "")
                name = esc(item.get("name") or "")
                cat = esc(item.get("category") or item.get("type") or "")
                try:
                    price = float(item.get("price") or item.get("last") or 0)
                except:
                    price = 0.0
                try:
                    chg = float(item.get("change_pct") or item.get("change") or item.get("changePercent") or 0)
                except:
                    chg = 0.0
                mnx_data.append((ticker, name, cat, price, chg))
        break
    time.sleep(0.5)

if not mnx_available:
    print("    MNX markets: unavailable")

if mnx_data:
    print("  Inserting MNX snapshots...")
    for ticker, name, cat, price, chg in mnx_data:
        sql = f"""
INSERT INTO mnx_snapshots (ticker, name, category, price, change_pct)
VALUES ('{ticker}', '{name}', '{cat}', {price}, {chg});
"""
        duckdb_exec(sql)

# ============================================================
# STEP 8: WRITE LATEST_SWEEP.md
# ============================================================
print("\n=== Writing LATEST_SWEEP.md ===")

ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

# Get top 10 repos by stars
top_repos_out = duckdb_exec(
    "SELECT org_or_user, full_name, language, stars, forks, open_issues, pushed_at FROM repo_snapshots ORDER BY stars DESC LIMIT 10;"
)

# Get all aptos
aptos_out = duckdb_exec(
    "SELECT world, address, balance_apt FROM aptos_snapshots ORDER BY world;"
)

# Get multisig
multi_out = duckdb_exec(
    "SELECT pair, address, sigs_required, healthy FROM multisig_probes;"
)

# Build markdown
md_lines = [
    f"# Latest Sweep Report",
    f"",
    f"**Sweep Timestamp:** {ts}",
    f"",
    f"---",
    f"",
    f"## GitHub Social Graph",
    f"",
    f"**Sources Scanned:**",
    f"- Orgs: {', '.join(ORGS)}",
    f"- Users: {', '.join(USERS)}",
    f"",
    f"**Total Repos:** {repo_counter}",
    f"**Total World Increments:** {increment_counter}",
    f"",
    f"### Top 10 Repos by Stars",
    f"",
    f"| org/user | full_name | language | stars | forks | open_issues | pushed_at |",
    f"|----------|-----------|----------|-------|-------|-------------|-----------|",
]

for line in top_repos_out.split("\n"):
    if line.strip() and not line.startswith("org_or_user"):
        parts = line.split("\t")
        if len(parts) >= 7:
            md_lines.append(f"| {' | '.join(p.strip() for p in parts[:7])} |")

md_lines += [
    f"",
    f"---",
    f"",
    f"## Aptos Wallet Balances",
    f"",
    f"| World | Address (truncated) | Balance (APT) |",
    f"|-------|---------------------|---------------|",
]

for world_label, addr, balance in aptos_data:
    trunc = addr[:10] + "..." + addr[-6:]
    md_lines.append(f"| {world_label} | {trunc} | {balance:.4f} |")

md_lines += [
    f"",
    f"---",
    f"",
    f"## Multisig Contract Probes",
    f"",
    f"| Pair | Address (truncated) | Sigs Required | Healthy |",
    f"|------|---------------------|---------------|---------|",
]

for pair, addr, sigs, healthy in multisig_data:
    trunc = addr[:10] + "..." + addr[-6:]
    md_lines.append(f"| {pair} | {trunc} | {sigs} | {'yes' if healthy else 'no'} |")

md_lines += [
    f"",
    f"---",
    f"",
    f"## MNX Markets",
    f"",
]

if mnx_available and mnx_data:
    md_lines += [
        f"**Status:** Available",
        f"",
        f"| Ticker | Name | Category | Price | Change % |",
        f"|--------|------|----------|-------|----------|",
    ]
    for ticker, name, cat, price, chg in mnx_data:
        md_lines.append(f"| {ticker} | {name} | {cat} | {price} | {chg} |")
else:
    md_lines += [
        f"**Status:** Unavailable (all endpoints timed out or returned errors)",
    ]

md_lines += [
    f"",
    f"---",
    f"",
    f"*Generated by world-increment sweep + hamming snapshot [GF3 color chain]*",
]

md_content = "\n".join(md_lines)
with open("/home/user/gorj/packages/world-increment/ducklake/LATEST_SWEEP.md", "w") as f:
    f.write(md_content)

print("LATEST_SWEEP.md written.")

# Final summary
print("\n=== SWEEP COMPLETE ===")
print(f"Timestamp: {ts}")
print(f"Repos collected: {repo_counter}")
print(f"World increments: {increment_counter}")
print(f"Aptos wallets: {len(aptos_data)}")
print(f"Multisig probes: {len(multisig_data)}")
print(f"MNX available: {mnx_available}")
