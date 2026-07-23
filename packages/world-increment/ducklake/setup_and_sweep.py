#!/usr/bin/env python3
"""World-increment sweep + Hamming swarm snapshot."""
import duckdb, subprocess, json, time, sys, hashlib
from datetime import datetime

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
con = duckdb.connect(DB_PATH)

# ── Schema ──────────────────────────────────────────────────────────────────
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
CREATE SEQUENCE IF NOT EXISTS increment_seq START 1
""")
con.execute("""
CREATE SEQUENCE IF NOT EXISTS repo_seq START 1
""")
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

print("Schema ready.")

# ── GF(3) helper ────────────────────────────────────────────────────────────
def gf3(n):
    r = n % 3
    if r == 0: return (0, "#d3869b", "ERGODIC")
    if r == 1: return (1, "#b8bb26", "PLUS")
    return (-1, "#cc241d", "MINUS")

def next_id():
    return con.execute("SELECT nextval('increment_seq')").fetchone()[0]

def next_repo_id():
    return con.execute("SELECT nextval('repo_seq')").fetchone()[0]

# ── Step 2: GitHub repo snapshots ───────────────────────────────────────────
# Note: GH MCP access is scoped to plurigrid/gorj only.
# We record what we know statically about the sweep targets and mark as
# scope-limited. Actual live data will be added where curl succeeds.
SWEEP_TARGETS = [
    ("org", "plurigrid"),
    ("org", "kubeflow"),
    ("org", "TeglonLabs"),
    ("user", "bmorphism"),
    ("user", "zubyul"),
    ("user", "migalkin"),
    ("user", "DJedamski"),
    ("user", "wasita"),
    ("user", "kristinezheng"),
    ("user", "M1shaaa"),
    ("user", "AustinCStone"),
]

gh_increment_id = next_id()
trit, color, name = gf3(gh_increment_id)
snap_hash = hashlib.sha256(f"github-sweep-{datetime.utcnow().isoformat()}".encode()).hexdigest()[:16]
con.execute("""
  INSERT INTO world_increments
    (id, gf3_trit, gf3_color, gf3_name, source_type, source_name,
     event_type, repo_name, actor, snapshot_hash)
  VALUES (?,?,?,?,?,?,?,?,?,?)
""", [gh_increment_id, trit, color, name, "github", "social-graph-sweep",
      "sweep", "N/A", "scheduler", snap_hash])

# Record scope targets as repo_snapshots with "scope-limited" note
for src_type, src_name in SWEEP_TARGETS:
    rid = next_repo_id()
    con.execute("""
      INSERT INTO repo_snapshots
        (id, increment_id, org_or_user, repo_name, full_name,
         language, stars, forks, open_issues, pushed_at, description)
      VALUES (?,?,?,?,?,?,?,?,?,?,?)
    """, [rid, gh_increment_id, src_name, "scope-limited",
          f"{src_name}/*", None, -1, -1, -1,
          datetime.utcnow().isoformat(),
          f"GH MCP scoped to plurigrid/gorj; {src_type} {src_name} not directly queryable"])

print(f"GitHub sweep recorded (scope-limited) — increment_id={gh_increment_id}, GF3={name}")

# ── Step 4: Aptos wallet balances ───────────────────────────────────────────
APTOS_ADDRS = {
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

APTOS_BASE = "https://fullnode.mainnet.aptoslabs.com/v1"
COIN_PATH = "/accounts/{addr}/resource/0x1::coin::CoinStore%3C0x1::aptos_coin::AptosCoin%3E"

aptos_results = {}
print(f"\nQuerying {len(APTOS_ADDRS)} Aptos addresses...")
for world, addr in APTOS_ADDRS.items():
    url = f"{APTOS_BASE}{COIN_PATH.format(addr=addr)}"
    try:
        r = subprocess.run(
            ["curl", "-s", "--max-time", "10", url],
            capture_output=True, text=True
        )
        data = json.loads(r.stdout)
        raw = data.get("data", {}).get("coin", {}).get("value", None)
        if raw is None:
            # might be error response
            apt = None
            status = f"no_coin_store: {data.get('error_code','?')}"
        else:
            apt = int(raw) / 1e8
            status = f"{apt:.4f} APT"
        aptos_results[world] = apt
        print(f"  {world} ({addr[:8]}...): {status}")
    except Exception as e:
        aptos_results[world] = None
        print(f"  {world}: ERROR {e}")
    time.sleep(1)

# Insert aptos snapshots
for world, bal in aptos_results.items():
    if bal is not None:
        con.execute(
            "INSERT INTO aptos_snapshots (world, address, balance_apt) VALUES (?,?,?)",
            [world, APTOS_ADDRS[world], bal]
        )
print(f"Aptos: {sum(1 for v in aptos_results.values() if v is not None)} balances stored.")

# ── Step 5: Multisig probes ──────────────────────────────────────────────────
MULTISIG_ADDRS = {
    "A-B": "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",
    "A-G": "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",
    "Y-Z": "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",
    "S-T": "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",
    "V-W": "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",
}

print(f"\nProbing {len(MULTISIG_ADDRS)} multisig contracts...")
multisig_results = {}
for pair, addr in MULTISIG_ADDRS.items():
    payload = json.dumps({
        "function": "0x1::multisig_account::num_signatures_required",
        "type_arguments": [],
        "arguments": [addr]
    })
    try:
        r = subprocess.run(
            ["curl", "-s", "--max-time", "10", "-X", "POST",
             "-H", "Content-Type: application/json",
             "-d", payload,
             f"{APTOS_BASE}/view"],
            capture_output=True, text=True
        )
        data = json.loads(r.stdout)
        if isinstance(data, list) and len(data) > 0:
            sigs = int(data[0])
            healthy = sigs > 0
            multisig_results[pair] = (sigs, healthy)
            print(f"  {pair}: {sigs} sigs required, healthy={healthy}")
        else:
            multisig_results[pair] = (None, False)
            print(f"  {pair}: no data — {data}")
    except Exception as e:
        multisig_results[pair] = (None, False)
        print(f"  {pair}: ERROR {e}")
    time.sleep(1)

for pair, (sigs, healthy) in multisig_results.items():
    con.execute(
        "INSERT INTO multisig_probes (pair, address, sigs_required, healthy) VALUES (?,?,?,?)",
        [pair, MULTISIG_ADDRS[pair], sigs, healthy]
    )
print(f"Multisig: {len(multisig_results)} probes stored.")

# ── Step 6: MNX Markets ─────────────────────────────────────────────────────
print("\nFetching MNX Markets...")
mnx_data = []
MNX_URLS = [
    "https://testnet.mnx.fi/api/markets",
    "https://testnet.mnx.fi/api/v1/markets",
    "https://testnet.mnx.fi/api/tickers",
    "https://testnet.mnx.fi/api/v1/tickers",
]
for url in MNX_URLS:
    try:
        r = subprocess.run(
            ["curl", "-s", "--max-time", "10", "-L", url],
            capture_output=True, text=True
        )
        if r.stdout and len(r.stdout) > 20:
            try:
                d = json.loads(r.stdout)
                print(f"  MNX {url}: got JSON data")
                mnx_data = d if isinstance(d, list) else [d]
                break
            except:
                print(f"  MNX {url}: non-JSON response ({len(r.stdout)} chars)")
        else:
            print(f"  MNX {url}: empty/short response")
    except Exception as e:
        print(f"  MNX {url}: ERROR {e}")

if not mnx_data:
    print("  MNX: all endpoints returned no parseable data — noting as unavailable")
    con.execute(
        "INSERT INTO mnx_snapshots (ticker, name, category, price, change_pct) VALUES (?,?,?,?,?)",
        ["N/A", "MNX testnet unavailable", "status", 0.0, 0.0]
    )
else:
    for item in mnx_data[:50]:
        if isinstance(item, dict):
            con.execute(
                "INSERT INTO mnx_snapshots (ticker, name, category, price, change_pct) VALUES (?,?,?,?,?)",
                [
                    item.get("ticker", item.get("symbol", "?")),
                    item.get("name", "?"),
                    item.get("category", item.get("type", "?")),
                    float(item.get("price", item.get("last", 0)) or 0),
                    float(item.get("change_pct", item.get("change", 0)) or 0),
                ]
            )
    print(f"  MNX: {len(mnx_data)} markets stored.")

# ── Step 7: World increment for Aptos ───────────────────────────────────────
aptos_inc_id = next_id()
trit, color, name = gf3(aptos_inc_id)
apt_hash = hashlib.sha256(str(aptos_results).encode()).hexdigest()[:16]
con.execute("""
  INSERT INTO world_increments
    (id, gf3_trit, gf3_color, gf3_name, source_type, source_name,
     event_type, repo_name, actor, snapshot_hash)
  VALUES (?,?,?,?,?,?,?,?,?,?)
""", [aptos_inc_id, trit, color, name, "aptos", "hamming-swarm",
      "balance-snapshot", "N/A", "scheduler", apt_hash])

# ── Step 8: Summary stats for report ────────────────────────────────────────
total_apt = sum(v for v in aptos_results.values() if v is not None)
wallets_found = sum(1 for v in aptos_results.values() if v is not None)
wallets_empty = sum(1 for v in aptos_results.values() if v == 0.0)
wallets_missing = sum(1 for v in aptos_results.values() if v is None)
healthy_multisigs = sum(1 for (_,h) in multisig_results.values() if h)

# Top wallets by balance
top_wallets = sorted(
    [(w, b) for w, b in aptos_results.items() if b and b > 0],
    key=lambda x: x[1], reverse=True
)[:5]

report = {
    "timestamp": datetime.utcnow().isoformat() + "Z",
    "github": {
        "targets_recorded": len(SWEEP_TARGETS),
        "note": "GH MCP scoped to plurigrid/gorj; social graph targets recorded as metadata only",
    },
    "aptos": {
        "total_wallets": len(APTOS_ADDRS),
        "wallets_found": wallets_found,
        "wallets_empty_or_zero": wallets_empty,
        "wallets_missing": wallets_missing,
        "total_apt_observed": round(total_apt, 4),
        "top5": [{"world": w, "apt": round(b, 4)} for w, b in top_wallets],
        "balances": {w: round(b, 8) if b is not None else None for w, b in aptos_results.items()},
    },
    "multisig": {
        "total_probed": len(MULTISIG_ADDRS),
        "healthy": healthy_multisigs,
        "results": {
            p: {"sigs_required": s, "healthy": h, "address": MULTISIG_ADDRS[p]}
            for p, (s, h) in multisig_results.items()
        },
    },
    "mnx": {
        "markets_found": len(mnx_data),
        "status": "unavailable" if not mnx_data or (len(mnx_data)==1 and mnx_data[0].get("name","") == "MNX testnet unavailable") else "ok",
    },
    "increments": {
        "github_sweep": {"id": gh_increment_id, "gf3": gf3(gh_increment_id)},
        "aptos_snapshot": {"id": aptos_inc_id, "gf3": gf3(aptos_inc_id)},
    }
}

with open("/home/user/gorj/packages/world-increment/ducklake/sweep_report.json", "w") as f:
    json.dump(report, f, indent=2)

print("\nReport saved to sweep_report.json")
print(json.dumps({k: v for k, v in report.items() if k != "aptos"}, indent=2))
print(f"\nAptos top 5: {top_wallets}")
con.close()
print("\nDone.")
