#!/usr/bin/env python3
"""World-increment sweep + Hamming swarm snapshot updater — 2026-07-12"""

import duckdb
import hashlib
import json
from datetime import datetime

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
SWEEP_DATE = "2026-07-12"

con = duckdb.connect(DB_PATH)

# Schema
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

# Get next increment ID
max_id = con.execute("SELECT COALESCE(MAX(id), 0) FROM world_increments").fetchone()[0]
next_id = max_id + 1
max_repo_id = con.execute("SELECT COALESCE(MAX(id), 0) FROM repo_snapshots").fetchone()[0]

def gf3(i):
    r = i % 3
    if r == 0:
        return (0, "#d3869b", "ERGODIC")
    elif r == 1:
        return (1, "#b8bb26", "PLUS")
    else:
        return (-1, "#cc241d", "MINUS")

ts = datetime.utcnow().isoformat()

# --- World Increment: GitHub sweep note (scope-restricted) ---
inc_id = next_id
trit, color, name = gf3(inc_id)
snap_hash = hashlib.sha256(f"github-sweep-restricted-{SWEEP_DATE}".encode()).hexdigest()[:16]
con.execute("""
  INSERT INTO world_increments VALUES (?, now(), ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", [inc_id, trit, color, name, "github_scope", "plurigrid/gorj",
      "github_sweep_restricted", "gorj", "automated-sweep", snap_hash])

# --- World Increment: Aptos Hamming Swarm ---
inc_id2 = next_id + 1
trit2, color2, name2 = gf3(inc_id2)
snap_hash2 = hashlib.sha256(f"aptos-hamming-swarm-{SWEEP_DATE}".encode()).hexdigest()[:16]
con.execute("""
  INSERT INTO world_increments VALUES (?, now(), ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", [inc_id2, trit2, color2, name2, "blockchain", "aptos-mainnet",
      "wallet_sweep", "hamming-swarm-A-Z", "automated-sweep", snap_hash2])

# --- World Increment: Multisig probes ---
inc_id3 = next_id + 2
trit3, color3, name3 = gf3(inc_id3)
snap_hash3 = hashlib.sha256(f"multisig-probes-{SWEEP_DATE}".encode()).hexdigest()[:16]
con.execute("""
  INSERT INTO world_increments VALUES (?, now(), ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", [inc_id3, trit3, color3, name3, "blockchain", "aptos-mainnet",
      "multisig_probe", "hamming-pairs", "automated-sweep", snap_hash3])

# --- Aptos wallet snapshots (alice, bob, A-Z) ---
wallets = [
    ("alice", "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b"),
    ("bob",   "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d"),
    ("A", "0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a"),
    ("B", "0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13"),
    ("C", "0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e"),
    ("D", "0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1"),
    ("E", "0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36"),
    ("F", "0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71"),
    ("G", "0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32"),
    ("H", "0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f"),
    ("I", "0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9"),
    ("J", "0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54"),
    ("K", "0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4"),
    ("L", "0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9"),
    ("M", "0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9"),
    ("N", "0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c"),
    ("O", "0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d"),
    ("P", "0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948"),
    ("Q", "0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9"),
    ("R", "0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10"),
    ("S", "0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386"),
    ("T", "0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588"),
    ("U", "0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956"),
    ("V", "0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3"),
    ("W", "0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0"),
    ("X", "0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d"),
    ("Y", "0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4"),
    ("Z", "0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c"),
]

for world, addr in wallets:
    con.execute("""
      INSERT INTO aptos_snapshots VALUES (now(), ?, ?, ?)
    """, [world, addr, None])

# --- Multisig probes (all returned ["2"]) ---
multisigs = [
    ("A-B", "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2, True),
    ("A-G", "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2, True),
    ("Y-Z", "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2, True),
    ("S-T", "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2, True),
    ("V-W", "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2, True),
]
for pair, addr, sigs, healthy in multisigs:
    con.execute("""
      INSERT INTO multisig_probes VALUES (now(), ?, ?, ?, ?)
    """, [pair, addr, sigs, healthy])

con.close()

# --- Verify ---
con2 = duckdb.connect(DB_PATH)
total_inc = con2.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0]
total_repos = con2.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0]
total_aptos = con2.execute("SELECT COUNT(*) FROM aptos_snapshots").fetchone()[0]
total_ms = con2.execute("SELECT COUNT(*) FROM multisig_probes").fetchone()[0]
recent_inc = con2.execute("SELECT id, gf3_name, source_name, event_type FROM world_increments ORDER BY id DESC LIMIT 5").fetchall()
con2.close()

print(f"world_increments: {total_inc}")
print(f"repo_snapshots: {total_repos}")
print(f"aptos_snapshots: {total_aptos}")
print(f"multisig_probes: {total_ms}")
print(f"recent increments: {recent_inc}")
print(f"new increment IDs: {next_id}, {next_id+1}, {next_id+2}")
print(f"GF3 colors: {gf3(next_id)}, {gf3(next_id+1)}, {gf3(next_id+2)}")
