#!/usr/bin/env python3
"""
world-increment-sweep + hamming-swarm-snapshot ingest script
Queries GitHub, Aptos, and MNX; stores in DuckDB.
"""
import json, subprocess, time, hashlib, sys, os
import urllib.request, urllib.error

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"

# ── helpers ──────────────────────────────────────────────────────────────────

def http_get(url, headers=None, timeout=12):
    req = urllib.request.Request(url, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read())
    except Exception as e:
        return None

def http_post(url, payload, timeout=12):
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data,
                                  headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read())
    except Exception as e:
        return None

GH = "https://api.github.com"
GH_HDR = {"Accept": "application/vnd.github.v3+json",
           "User-Agent": "world-increment-sweep/1.0"}

APTOS = "https://fullnode.mainnet.aptoslabs.com/v1"
COIN  = "0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>"
COIN_ENC = "0x1::coin::CoinStore%3C0x1::aptos_coin::AptosCoin%3E"

# ── GF(3) ────────────────────────────────────────────────────────────────────

def gf3(n):
    m = n % 3
    if m == 0: return (0, "#d3869b", "ERGODIC")
    if m == 1: return (1, "#b8bb26", "PLUS")
    return (-1, "#cc241d", "MINUS")

def snap_hash(s):
    return hashlib.sha1(s.encode()).hexdigest()[:12]

# ── fetch GitHub repos ───────────────────────────────────────────────────────

def gh_repos(kind, name):
    """Returns list of repo dicts. kind='orgs'|'users'"""
    url = f"{GH}/{kind}/{name}/repos?per_page=100&sort=pushed"
    data = http_get(url, GH_HDR)
    if not data or not isinstance(data, list):
        return []
    return data

# ── fetch Aptos balance ──────────────────────────────────────────────────────

def aptos_balance(addr):
    url = f"{APTOS}/accounts/{addr}/resource/{COIN_ENC}"
    d = http_get(url)
    if d and "data" in d:
        return int(d["data"]["coin"]["value"]) / 1e8
    return 0.0

# ── multisig probe ───────────────────────────────────────────────────────────

def multisig_sigs(addr):
    url = f"{APTOS}/view"
    result = http_post(url, {
        "function": "0x1::multisig_account::num_signatures_required",
        "type_arguments": [],
        "arguments": [addr]
    })
    if result and len(result) > 0:
        return int(result[0])
    return None

# ── DuckDB via CLI ───────────────────────────────────────────────────────────

def duckdb_exec(sql):
    r = subprocess.run(["duckdb", DB], input=sql, capture_output=True, text=True)
    if r.returncode != 0 and r.stderr:
        print(f"  DUCKDB ERR: {r.stderr[:200]}", file=sys.stderr)
    return r.stdout.strip()

def duckdb_batch(statements):
    sql = ";\n".join(statements) + ";"
    return duckdb_exec(sql)

# ── get current max IDs ───────────────────────────────────────────────────────

def get_next_id(table, col="id"):
    r = duckdb_exec(f"SELECT COALESCE(MAX({col}),0)+1 FROM {table};")
    lines = [l.strip() for l in r.splitlines() if l.strip() and l.strip() not in ["│", "┌","┐","└","┘","├","┤","─"]]
    for l in lines:
        # strip table borders
        val = l.replace("│","").strip()
        try:
            return int(val)
        except:
            pass
    return 1

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

print("=== world-increment-sweep + hamming-swarm ingest ===")
print(f"DB: {DB}")

# --- ensure schema exists ---
SCHEMA_SQL = """
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
duckdb_exec(SCHEMA_SQL)
print("Schema ensured.")

# get starting IDs
inc_id = get_next_id("world_increments")
repo_id = get_next_id("repo_snapshots")
print(f"Starting increment ID: {inc_id}, repo ID: {repo_id}")

# ─── GITHUB SWEEP ──────────────────────────────────────────────────────────────

sources = [
    ("orgs", "plurigrid"),
    ("orgs", "kubeflow"),
    ("orgs", "TeglonLabs"),
    ("users", "bmorphism"),
    ("users", "zubyul"),
    ("users", "migalkin"),
    ("users", "DJedamski"),
    ("users", "wasita"),
    ("users", "kristinezheng"),
    ("users", "M1shaaa"),
    ("users", "AustinCStone"),
]

inc_inserts = []
repo_inserts = []

for (kind, name) in sources:
    print(f"  Fetching {kind}/{name} ...", end=" ", flush=True)
    repos = gh_repos(kind, name)
    print(f"{len(repos)} repos")

    source_type = "org" if kind == "orgs" else "user"
    trit, color, gf3name = gf3(inc_id)
    h = snap_hash(f"{name}:{inc_id}")
    inc_inserts.append(
        f"INSERT INTO world_increments VALUES ({inc_id}, now(), {trit}, "
        f"'{color}', '{gf3name}', '{source_type}', '{name}', "
        f"'RepoSweep', NULL, '{name}', '{h}')"
    )
    this_inc_id = inc_id
    inc_id += 1

    for repo in repos:
        lang = (repo.get("language") or "").replace("'","''")[:40]
        desc = (repo.get("description") or "").replace("'","''")[:120].replace("\n"," ")
        full_name = repo.get("full_name","").replace("'","''")
        repo_name = repo.get("name","").replace("'","''")
        pushed = (repo.get("pushed_at") or "")[:10]
        repo_inserts.append(
            f"INSERT INTO repo_snapshots VALUES ({repo_id}, now(), {this_inc_id}, "
            f"'{name}', '{repo_name}', '{full_name}', '{lang}', "
            f"{repo.get('stargazers_count',0)}, {repo.get('forks_count',0)}, "
            f"{repo.get('open_issues_count',0)}, '{pushed}', '{desc}')"
        )
        repo_id += 1

    time.sleep(0.3)

print(f"Inserting {len(inc_inserts)} increments, {len(repo_inserts)} repos ...")

# batch insert increments
CHUNK = 50
for i in range(0, len(inc_inserts), CHUNK):
    duckdb_batch(inc_inserts[i:i+CHUNK])
for i in range(0, len(repo_inserts), CHUNK):
    duckdb_batch(repo_inserts[i:i+CHUNK])
print("GitHub data inserted.")

# ─── APTOS WALLETS ─────────────────────────────────────────────────────────────

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

aptos_inserts = []
print("Querying Aptos balances ...")
for world, addr in WALLETS.items():
    bal = aptos_balance(addr)
    print(f"  {world:6s}: {bal:.8f} APT")
    aptos_inserts.append(
        f"INSERT INTO aptos_snapshots VALUES (now(), '{world}', '{addr}', {bal})"
    )
    time.sleep(1)

duckdb_batch(aptos_inserts)
print("Aptos balances inserted.")

# ─── MULTISIG PROBES ───────────────────────────────────────────────────────────

MULTISIGS = {
    "A-B": "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",
    "A-G": "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",
    "Y-Z": "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",
    "S-T": "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",
    "V-W": "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",
}

ms_inserts = []
print("Probing multisig contracts ...")
for pair, addr in MULTISIGS.items():
    sigs = multisig_sigs(addr)
    healthy = sigs is not None and sigs > 0
    sigs_val = sigs if sigs is not None else 0
    print(f"  {pair}: sigs_required={sigs_val}, healthy={healthy}")
    ms_inserts.append(
        f"INSERT INTO multisig_probes VALUES (now(), '{pair}', '{addr}', "
        f"{sigs_val}, {'true' if healthy else 'false'})"
    )
    time.sleep(1)

duckdb_batch(ms_inserts)
print("Multisig probes inserted.")

# ─── MNX MARKETS ───────────────────────────────────────────────────────────────

print("Probing MNX testnet ...")
MNX_PATHS = [
    "https://testnet.mnx.fi/api/markets",
    "https://testnet.mnx.fi/api/v1/markets",
    "https://testnet.mnx.fi/markets",
    "https://testnet.mnx.fi/api/tickers",
]
mnx_data = None
for url in MNX_PATHS:
    d = http_get(url, timeout=8)
    if d:
        mnx_data = d
        print(f"  MNX data from {url}")
        break

if mnx_data:
    markets = mnx_data if isinstance(mnx_data, list) else mnx_data.get("markets", [])
    mnx_inserts = []
    for m in markets[:50]:
        ticker   = str(m.get("ticker", m.get("symbol",""))).replace("'","''")
        name     = str(m.get("name","")).replace("'","''")
        category = str(m.get("category","")).replace("'","''")
        price    = float(m.get("price", m.get("last", 0)) or 0)
        change   = float(m.get("change_pct", m.get("change24h", 0)) or 0)
        mnx_inserts.append(
            f"INSERT INTO mnx_snapshots VALUES (now(), '{ticker}', '{name}', "
            f"'{category}', {price}, {change})"
        )
    if mnx_inserts:
        duckdb_batch(mnx_inserts)
        print(f"  {len(mnx_inserts)} MNX markets inserted.")
    else:
        print("  MNX: no market rows extracted.")
else:
    print("  MNX testnet: unavailable (SPA or offline)")
    duckdb_exec("INSERT INTO mnx_snapshots VALUES (now(), 'N/A', 'MNX Testnet', 'unavailable', 0.0, 0.0)")

# ─── FINAL COUNTS ──────────────────────────────────────────────────────────────

counts = duckdb_exec("""
SELECT 'world_increments' as t, COUNT(*) as n FROM world_increments
UNION ALL SELECT 'repo_snapshots', COUNT(*) FROM repo_snapshots
UNION ALL SELECT 'aptos_snapshots', COUNT(*) FROM aptos_snapshots
UNION ALL SELECT 'multisig_probes', COUNT(*) FROM multisig_probes
UNION ALL SELECT 'mnx_snapshots', COUNT(*) FROM mnx_snapshots;
""")
print("\n=== Final DB counts ===")
print(counts)

# ─── EXPORT SUMMARY DATA ────────────────────────────────────────────────────────

# Get last sweep increments
last_inc = duckdb_exec(f"""
SELECT id, source_type, source_name, gf3_trit, gf3_color, gf3_name
FROM world_increments
WHERE id >= {inc_id - len(inc_inserts)}
ORDER BY id;
""")

# Get top repos this sweep
top_repos = duckdb_exec(f"""
SELECT org_or_user, repo_name, language, stars, pushed_at
FROM repo_snapshots
WHERE increment_id >= {inc_id - len(inc_inserts)}
ORDER BY stars DESC
LIMIT 20;
""")

# Get aptos latest
aptos_latest = duckdb_exec("""
SELECT world, address, balance_apt
FROM aptos_snapshots
WHERE timestamp = (SELECT MAX(timestamp) FROM aptos_snapshots)
   OR timestamp >= now() - INTERVAL '1 minute'
ORDER BY world;
""")

# Get multisig latest
ms_latest = duckdb_exec("""
SELECT pair, address, sigs_required, healthy
FROM multisig_probes
WHERE timestamp >= now() - INTERVAL '1 minute'
ORDER BY pair;
""")

print("\n=== Increments this sweep ===")
print(last_inc)
print("\n=== Top repos this sweep (by stars) ===")
print(top_repos)
print("\n=== Aptos snapshots ===")
print(aptos_latest)
print("\n=== Multisig probes ===")
print(ms_latest)

print("\nDone. Data stored in:", DB)
