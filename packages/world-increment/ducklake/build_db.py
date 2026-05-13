#!/usr/bin/env python3
"""Build world-increments DuckDB from sweep data."""
import duckdb, json, hashlib, os, sys

DB = os.path.join(os.path.dirname(__file__), "world-increments.duckdb")
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
con.execute("CREATE SEQUENCE IF NOT EXISTS increment_seq START 1")
con.execute("CREATE SEQUENCE IF NOT EXISTS repo_seq START 1")
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

GF3 = {0: (0, "#d3869b", "ERGODIC"), 1: (1, "#b8bb26", "PLUS"), 2: (-1, "#cc241d", "MINUS")}

def gf3(n):
    t, c, nm = GF3[n % 3]
    return t, c, nm

def snap_hash(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()[:16]

# ── repo data ──────────────────────────────────────────────────────────────
REPOS = []

# data passed in as JSON argument or loaded from extra_repos.json
extra_file = os.path.join(os.path.dirname(__file__), "extra_repos.json")
if os.path.exists(extra_file):
    with open(extra_file) as f:
        REPOS.extend(json.load(f))

# Inline small sources
INLINE = json.loads(sys.argv[1]) if len(sys.argv) > 1 else []
REPOS.extend(INLINE)

print(f"Inserting {len(REPOS)} repos...")

# Clear old data (idempotent re-run)
con.execute("DELETE FROM repo_snapshots")
con.execute("DELETE FROM world_increments")
con.execute("DELETE FROM aptos_snapshots")
con.execute("DELETE FROM multisig_probes")
con.execute("DELETE FROM mnx_snapshots")

for i, r in enumerate(REPOS, 1):
    trit, color, name = gf3(i)
    h = snap_hash(r)
    con.execute(
        "INSERT INTO world_increments VALUES (nextval('increment_seq'), now(), ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        [trit, color, name, "github_repo", r["ou"], "push", r["name"], r.get("ou",""), h]
    )
    inc_id = con.execute("SELECT currval('increment_seq')").fetchone()[0]
    con.execute(
        "INSERT INTO repo_snapshots VALUES (nextval('repo_seq'), now(), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        [inc_id, r["ou"], r["name"], r["full_name"],
         r.get("lang") or "", r.get("stars",0), r.get("forks",0),
         r.get("issues",0), r.get("pushed_at",""), (r.get("desc") or "")[:255]]
    )

# ── Aptos snapshots ────────────────────────────────────────────────────────
APTOS = json.loads(open(os.path.join(os.path.dirname(__file__), "aptos_data.json")).read())
for row in APTOS["balances"]:
    con.execute("INSERT INTO aptos_snapshots(world, address, balance_apt) VALUES (?, ?, ?)",
                [row["world"], row["address"], row["balance_apt"]])

for row in APTOS["multisigs"]:
    con.execute("INSERT INTO multisig_probes(pair, address, sigs_required, healthy) VALUES (?, ?, ?, ?)",
                [row["pair"], row["address"], row["sigs_required"], row["healthy"]])

# ── MNX (SPA, no data) ────────────────────────────────────────────────────
# No market data available from Next.js SPA

# ── Summary query ─────────────────────────────────────────────────────────
total_repos = con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0]
total_inc   = con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0]
total_aptos = con.execute("SELECT COUNT(*) FROM aptos_snapshots").fetchone()[0]
total_ms    = con.execute("SELECT COUNT(*) FROM multisig_probes").fetchone()[0]
top = con.execute(
    "SELECT org_or_user, COUNT(*) c FROM repo_snapshots GROUP BY org_or_user ORDER BY c DESC"
).fetchall()

print(f"DB: {total_inc} increments, {total_repos} repos, {total_aptos} aptos rows, {total_ms} multisig probes")
print("By source:", top)
con.close()
print("Done.")
