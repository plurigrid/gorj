#!/usr/bin/env python3
"""Build world-increment DuckDB from GitHub + Aptos snapshot data."""

import json, duckdb, hashlib, datetime

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

# GF3 color chain
def gf3(id_):
    t = id_ % 3
    if t == 0: return (0, "#d3869b", "ERGODIC")
    if t == 1: return (1, "#b8bb26", "PLUS")
    return (-1, "#cc241d", "MINUS")

def snap_hash(name):
    return hashlib.sha256(name.encode()).hexdigest()[:16]

# ---- Load large JSON files ----
def load_repos_file(path, org_or_user):
    try:
        with open(path) as f:
            data = json.load(f)
        return [(r["full_name"], r.get("language") or "", r.get("stargazers_count",0),
                 r.get("forks_count",0), r.get("open_issues_count",0),
                 (r.get("pushed_at") or "")[:10],
                 (r.get("description") or "")[:200], org_or_user)
                for r in data.get("items", [])]
    except Exception as e:
        print(f"  warn: {path}: {e}")
        return []

BASE = "/root/.claude/projects/-home-user-gorj/a9eb29cf-1613-4429-8907-f6b4d1518af6/tool-results"
plurigrid_repos = load_repos_file(f"{BASE}/mcp-github-search_repositories-1780596497147.txt", "plurigrid")
kubeflow_repos  = load_repos_file(f"{BASE}/mcp-github-search_repositories-1780596496087.txt", "kubeflow")
bmorphism_repos = load_repos_file(f"{BASE}/mcp-github-search_repositories-1780596499242.txt", "bmorphism")
zubyul_repos    = load_repos_file(f"{BASE}/mcp-github-search_repositories-1780596498449.txt", "zubyul")

# TeglonLabs (direct from result)
teglon_repos = [
    ("TeglonLabs/mathpix-gem","Ruby",2,0,11,"2026-01-01","Transform mathematical images to LaTeX","TeglonLabs"),
    ("TeglonLabs/coin-flip-mcp","JavaScript",0,2,1,"2025-09-21","MCP server for flipping coins with varying degrees of randomness","TeglonLabs"),
    ("TeglonLabs/monad-mcp-server","",0,0,0,"2025-05-14","Monad MCP Server","TeglonLabs"),
    ("TeglonLabs/topoi","Python",0,0,1,"2025-01-24","","TeglonLabs"),
]

# Social graph
social_repos = [
    # migalkin
    ("migalkin/NodePiece","Python",144,21,0,"2026-05-07","Compositional and Parameter-Efficient Representations for Large Knowledge Graphs","migalkin"),
    ("migalkin/StarE","Python",89,16,1,"2026-04-16","EMNLP 2020: Message Passing for Hyper-Relational Knowledge Graphs","migalkin"),
    ("migalkin/NBFNet_mlx","Python",10,1,1,"2026-03-11","Neural Bellman-Ford networks implemented in MLX for Apple Silicon","migalkin"),
    ("migalkin/kgcourse2021","HTML",25,9,0,"2026-02-16","Материалы к курсу по Knowledge Graphs","migalkin"),
    ("migalkin/RWL","Python",8,1,0,"2026-05-28","Weisfeiler and Leman Go Relational","migalkin"),
    ("migalkin/rambo","Rust",3,0,1,"2023-02-28","","migalkin"),
    ("migalkin/SMJoin-experiments","R",1,0,0,"2020-03-04","ISWC 2017 SMJoin results","migalkin"),
    # wasita
    ("wasita/wasita.github.io","Svelte",1,0,8,"2026-06-01","personal website","wasita"),
    ("wasita/magic-garden","Python",2,1,1,"2026-04-22","discord bot for magic garden game","wasita"),
    ("wasita/send2kobo","TypeScript",1,0,0,"2026-05-19","Website for sending books to kobo e-reader","wasita"),
    ("wasita/vocoder","JavaScript",0,0,0,"2026-05-06","","wasita"),
    ("wasita/wm-cv","Svelte",0,0,0,"2026-05-13","Academic CV","wasita"),
    # kristinezheng
    ("kristinezheng/kristinezheng.github.io","HTML",0,0,0,"2026-05-14","","kristinezheng"),
    ("kristinezheng/lookit-jenga","Jupyter Notebook",0,0,0,"2024-05-16","Lookit study","kristinezheng"),
    # M1shaaa
    ("M1shaaa/M1shaaa","",0,0,0,"2026-02-04","Config files for GitHub profile","M1shaaa"),
    ("M1shaaa/lab-bookshelf-","TypeScript",0,0,0,"2024-12-31","","M1shaaa"),
    # AustinCStone
    ("AustinCStone/TextGAN","Python",92,30,5,"2025-03-03","A generative adversarial network for text generation","AustinCStone"),
    ("AustinCStone/StereoVisionMRF","Python",11,4,0,"2026-04-01","MRF with loopy belief propagation for depth from stereo","AustinCStone"),
    ("AustinCStone/EpsteinSearch","Python",0,0,0,"2026-02-11","","AustinCStone"),
    ("AustinCStone/SpectralClustering","Python",3,2,0,"2021-04-16","Spectral clustering","AustinCStone"),
    # DJedamski
    ("DJedamski/kaggle_ncaa18","Jupyter Notebook",0,0,0,"2018-02-26","NCAA March Madness competition 2018","DJedamski"),
    ("DJedamski/School","R",1,1,0,"2023-04-21","Small projects from grad school","DJedamski"),
]

all_repos = plurigrid_repos + kubeflow_repos + bmorphism_repos + zubyul_repos + teglon_repos + social_repos

print(f"Total repos to insert: {len(all_repos)}")

# Insert world_increments + repo_snapshots
now = datetime.datetime.utcnow()
inc_id = 1
repo_id = 1

for repo in all_repos:
    full_name, lang, stars, forks, issues, pushed, desc, source = repo
    trit, color, gf3name = gf3(inc_id)
    h = snap_hash(full_name)
    con.execute("""
        INSERT INTO world_increments VALUES (?,?,?,?,?,'repo',?,?,?,?,?)
    """, [inc_id, now, trit, color, gf3name, source, "repo_snapshot", full_name, source, h])
    con.execute("""
        INSERT INTO repo_snapshots VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
    """, [repo_id, now, inc_id, source, full_name.split("/")[-1], full_name,
          lang, stars, forks, issues, pushed, desc[:200]])
    inc_id += 1
    repo_id += 1

# Aptos snapshots
aptos_data = [
    ("alice","0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b",0.0),
    ("bob","0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d",0.0),
    ("A","0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a",0.0),
    ("B","0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13",0.0),
    ("C","0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e",0.0),
    ("D","0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1",0.0),
    ("E","0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36",0.0),
    ("F","0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71",0.0),
    ("G","0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32",0.0),
    ("H","0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f",0.0),
    ("I","0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9",0.0),
    ("J","0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54",0.0),
    ("K","0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4",0.0),
    ("L","0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9",0.0),
    ("M","0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9",0.0),
    ("N","0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c",0.0),
    ("O","0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d",0.0),
    ("P","0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948",0.0),
    ("Q","0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9",0.0),
    ("R","0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10",0.0),
    ("S","0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386",0.0),
    ("T","0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588",0.0),
    ("U","0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956",0.0),
    ("V","0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3",0.0),
    ("W","0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0",0.0),
    ("X","0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d",0.0),
    ("Y","0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4",0.0),
    ("Z","0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c",0.0),
]
for world, addr, bal in aptos_data:
    con.execute("INSERT INTO aptos_snapshots VALUES (?,?,?,?)", [now, world, addr, bal])

# Multisig probes (all returned sigs_required=2)
multisig_data = [
    ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2,True),
    ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2,True),
    ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2,True),
    ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2,True),
    ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2,True),
]
for pair, addr, sigs, healthy in multisig_data:
    con.execute("INSERT INTO multisig_probes VALUES (?,?,?,?,?)", [now, pair, addr, sigs, healthy])

# MNX - SPA, no API data
con.execute("INSERT INTO mnx_snapshots VALUES (?,?,?,?,?,?)",
            [now, "N/A", "MNX testnet (SPA, no API data)", "unavailable", 0.0, 0.0])

con.commit()

# Verify
print("\n=== DB Summary ===")
print("world_increments:", con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0])
print("repo_snapshots:  ", con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0])
print("aptos_snapshots: ", con.execute("SELECT COUNT(*) FROM aptos_snapshots").fetchone()[0])
print("multisig_probes: ", con.execute("SELECT COUNT(*) FROM multisig_probes").fetchone()[0])
print("mnx_snapshots:   ", con.execute("SELECT COUNT(*) FROM mnx_snapshots").fetchone()[0])

print("\n=== GF3 distribution ===")
for row in con.execute("SELECT gf3_name, gf3_color, COUNT(*) FROM world_increments GROUP BY 1,2 ORDER BY 1").fetchall():
    print(f"  {row[2]:4d} {row[0]} {row[1]}")

print("\n=== Top repos by stars ===")
for row in con.execute("SELECT full_name, stars, language FROM repo_snapshots ORDER BY stars DESC LIMIT 10").fetchall():
    print(f"  {row[1]:5d}* {row[0]} ({row[2]})")

print("\n=== Sources ===")
for row in con.execute("SELECT org_or_user, COUNT(*) FROM repo_snapshots GROUP BY 1 ORDER BY 2 DESC").fetchall():
    print(f"  {row[1]:4d}  {row[0]}")

con.close()
print("\nDone.")
