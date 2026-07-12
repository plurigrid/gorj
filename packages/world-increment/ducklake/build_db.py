#!/usr/bin/env python3
"""Build world-increments.duckdb with GitHub sweep and Hamming swarm snapshot."""
import duckdb
import hashlib
import sys
from datetime import datetime

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
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
    con.execute("CREATE SEQUENCE increment_seq START 1")
except: pass
try:
    con.execute("CREATE SEQUENCE repo_seq START 1")
except: pass

def gf3(id_val):
    trit = id_val % 3
    if trit == 0:
        return (0, "#d3869b", "ERGODIC")
    elif trit == 1:
        return (1, "#b8bb26", "PLUS")
    else:
        return (-1, "#cc241d", "MINUS")

def snap_hash(s):
    return hashlib.sha256(s.encode()).hexdigest()[:16]

# --- GitHub sweep data ---
# Proxy blocks cross-org GitHub API; recording plurigrid/gorj as anchor
github_sources = [
    # (source_type, source_name, event_type, repo_name, actor)
    ("org", "plurigrid", "repo_sweep_blocked", "gorj", "proxy-scope-restricted"),
    ("org", "kubeflow", "repo_sweep_blocked", "", "proxy-scope-restricted"),
    ("org", "TeglonLabs", "repo_sweep_blocked", "", "proxy-scope-restricted"),
    ("user", "bmorphism", "repo_sweep_blocked", "", "proxy-scope-restricted"),
    ("user", "zubyul", "repo_sweep_blocked", "", "proxy-scope-restricted"),
    ("user", "migalkin", "repo_sweep_blocked", "", "proxy-scope-restricted"),
    ("user", "DJedamski", "repo_sweep_blocked", "", "proxy-scope-restricted"),
    ("user", "wasita", "repo_sweep_blocked", "", "proxy-scope-restricted"),
    ("user", "kristinezheng", "repo_sweep_blocked", "", "proxy-scope-restricted"),
    ("user", "M1shaaa", "repo_sweep_blocked", "", "proxy-scope-restricted"),
    ("user", "AustinCStone", "repo_sweep_blocked", "", "proxy-scope-restricted"),
]

for i, (stype, sname, etype, rname, actor) in enumerate(github_sources):
    id_val = con.execute("SELECT nextval('increment_seq')").fetchone()[0]
    trit, color, name = gf3(id_val)
    h = snap_hash(f"{stype}{sname}{etype}")
    con.execute(
        "INSERT INTO world_increments VALUES (?,now(),?,?,?,?,?,?,?,?,?)",
        [id_val, trit, color, name, stype, sname, etype, rname, actor, h]
    )

# --- Aptos balances ---
aptos_data = [
    ("alice", "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b", 0.43643352),
    ("bob",   "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d", 12.657007),
    ("A",     "0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a", 0.051767),
    ("B",     "0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13", 0.036256),
    ("C",     "0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e", 0.010185),
    ("D",     "0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1", 0.011629),
    ("E",     "0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36", 0.009372),
    ("F",     "0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71", 1.960516),
    ("G",     "0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32", 0.000681),
    ("H",     "0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f", 0.001681),
    ("I",     "0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9", 0.000681),
    ("J",     "0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54", 1.895093),
    ("K",     "0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4", 0.161961),
    ("L",     "0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9", 1.927269),
    ("M",     "0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9", 0.112285),
    ("N",     "0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c", 0.106121),
    ("O",     "0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d", 0.210136),
    ("P",     "0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948", 0.140136),
    ("Q",     "0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9", 0.10324),
    ("R",     "0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10", 0.090217),
    ("S",     "0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386", 0.091788),
    ("T",     "0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588", 0.073713),
    ("U",     "0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956", 0.055773),
    ("V",     "0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3", 0.04883299),
    ("W",     "0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0", 0.040705),
    ("X",     "0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d", 0.042577),
    ("Y",     "0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4", 0.044449),
    ("Z",     "0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c", 0.024268),
]

for world, addr, bal in aptos_data:
    con.execute("INSERT INTO aptos_snapshots VALUES (now(),?,?,?)", [world, addr, bal])
    id_val = con.execute("SELECT nextval('increment_seq')").fetchone()[0]
    trit, color, gname = gf3(id_val)
    h = snap_hash(f"aptos{world}{addr}")
    con.execute("INSERT INTO world_increments VALUES (?,now(),?,?,?,?,?,?,?,?,?)",
        [id_val, trit, color, gname, "aptos", world, "balance_snapshot", "", addr, h])

# --- Multisig probes ---
multisig_data = [
    ("A-B", "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2),
    ("A-G", "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2),
    ("Y-Z", "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2),
    ("S-T", "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2),
    ("V-W", "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2),
]

for pair, addr, sigs in multisig_data:
    con.execute("INSERT INTO multisig_probes VALUES (now(),?,?,?,?)", [pair, addr, sigs, True])
    id_val = con.execute("SELECT nextval('increment_seq')").fetchone()[0]
    trit, color, gname = gf3(id_val)
    h = snap_hash(f"multisig{pair}{addr}")
    con.execute("INSERT INTO world_increments VALUES (?,now(),?,?,?,?,?,?,?,?,?)",
        [id_val, trit, color, gname, "multisig", pair, "probe", "", addr, h])

# MNX - unavailable (auth required)
con.execute("INSERT INTO mnx_snapshots VALUES (now(),'N/A','MNX Markets','unavailable',NULL,NULL)")

con.close()
print("DuckDB built OK:", DB_PATH)
