#!/usr/bin/env python3
"""Build world-increment ducklake from sweep data."""
import duckdb
import json
from datetime import datetime

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
con = duckdb.connect(DB_PATH)

# Create tables
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
except:
    pass

def gf3(i):
    t = i % 3
    if t == 0: return (0, "#d3869b", "ERGODIC")
    if t == 1: return (1, "#b8bb26", "PLUS")
    return (-1, "#cc241d", "MINUS")

# All repo data
repos_data = [
    # (org_or_user, full_name, language, stars, forks, open_issues, pushed_at, description)
    # plurigrid (sample of 100)
    ("plurigrid","plurigrid/asi","HTML",31,10,4,"2026-07-10T09:47:39Z","everything is topological chemputer!"),
    ("plurigrid","plurigrid/gorj","Clojure",1,0,1228,"2026-07-18T00:12:59Z","forj + Rama topology nREPL routing + GF(3) gay trit coloring"),
    ("plurigrid","plurigrid/shrimp","",0,0,0,"2026-07-03T01:24:20Z","Jank worked example: shrimp"),
    ("plurigrid","plurigrid/place","TeX",1,1,13,"2026-07-14T09:11:33Z",""),
    ("plurigrid","plurigrid/eirobri","Clojure",0,0,30,"2026-07-14T02:23:51Z","EiRoBri replay world"),
    ("plurigrid","plurigrid/nash-portal","Rust",2,3,1,"2026-05-19T01:49:59Z","NASH token TUI in the browser"),
    ("plurigrid","plurigrid/zig-syrup","Zig",2,2,0,"2026-04-30T03:52:16Z","High-performance Zig implementation of OCapN Syrup"),
    ("plurigrid","plurigrid/asi-skills","Julia",3,0,0,"2026-04-26T08:09:26Z","69 skills with Galois Hole Type accessibility"),
    ("plurigrid","plurigrid/nanoclj-zig","Zig",1,1,20,"2026-04-25T07:29:09Z","NaN-boxed Clojure interpreter in Zig 0.15"),
    ("plurigrid","plurigrid/ontology","JavaScript",8,9,16,"2025-05-27T18:18:34Z","autopoietic ergodicity and embodied gradualism"),
    # kubeflow
    ("kubeflow","kubeflow/trainer","Go",2151,989,122,"2026-07-18T00:32:37Z","Distributed AI Model Training and LLM Fine-Tuning on Kubernetes"),
    ("kubeflow","kubeflow/hub","Go",177,188,24,"2026-07-17T19:01:24Z","Model Registry"),
    ("kubeflow","kubeflow/sdk","Python",125,199,165,"2026-07-17T18:42:09Z","Universal Python SDK"),
    ("kubeflow","kubeflow/pipelines","Python",4168,2043,429,"2026-07-17T14:46:42Z","Machine Learning Pipelines for Kubeflow"),
    ("kubeflow","kubeflow/kubeflow","",15779,2686,0,"2026-07-16T09:38:14Z","Machine Learning Toolkit for Kubernetes"),
    ("kubeflow","kubeflow/katib","Python",1690,533,105,"2026-07-16T14:39:00Z","Automated Machine Learning on Kubernetes"),
    ("kubeflow","kubeflow/spark-operator","Python",3138,1501,106,"2026-07-17T13:37:26Z","Kubernetes operator for Apache Spark"),
    ("kubeflow","kubeflow/mcp-apache-spark-history-server","Python",183,65,20,"2026-07-16T20:05:30Z","MCP Server for Apache Spark History Server"),
    ("kubeflow","kubeflow/arena","Go",815,195,56,"2026-07-16T11:51:25Z","A CLI for Kubeflow"),
    ("kubeflow","kubeflow/community-distribution","YAML",1029,1072,27,"2026-07-17T14:40:31Z","Kubeflow Community Distribution"),
    # TeglonLabs
    ("TeglonLabs","TeglonLabs/jank-crane","C++",0,0,0,"2026-06-08T19:03:37Z","crane-jank converged-IR hub"),
    ("TeglonLabs","TeglonLabs/mathpix-gem","Ruby",2,0,11,"2026-01-01T12:13:16Z","Transform mathematical images to LaTeX"),
    ("TeglonLabs","TeglonLabs/coin-flip-mcp","JavaScript",0,2,1,"2025-03-16T01:31:45Z","MCP server for flipping coins"),
    ("TeglonLabs","TeglonLabs/topoi","Python",0,0,1,"2025-01-24T06:47:38Z",""),
    # bmorphism
    ("bmorphism","bmorphism/gay-chat","Scheme",0,0,0,"2026-07-14T21:00:00Z","gay://chat operationalization over Spritely Brassica Chat"),
    ("bmorphism","bmorphism/Gay.jl","Julia",2,1,187,"2026-07-14T08:57:38Z","Wide-gamut color sampling with splittable determinism"),
    ("bmorphism","bmorphism/anti-bullshit-mcp-server","JavaScript",22,7,1,"2026-07-12T19:31:54Z","MCP server for analyzing claims"),
    ("bmorphism","bmorphism/ocaml-mcp-sdk","OCaml",61,2,0,"2026-05-08T16:50:34Z","OCaml SDK for Model Context Protocol"),
    ("bmorphism","bmorphism/whale","MATLAB",2,0,0,"2026-04-20T15:04:09Z","omniglot + sperm whale codas = metawhaling"),
    ("bmorphism","bmorphism/say-mcp-server","JavaScript",20,9,3,"2026-03-19T23:11:59Z","MCP server for macOS text-to-speech"),
    ("bmorphism","bmorphism/babashka-mcp-server","JavaScript",19,6,3,"2026-06-05T13:16:11Z","MCP server for Babashka"),
    ("bmorphism","bmorphism/penrose-mcp","JavaScript",9,4,0,"2026-06-24T15:36:16Z","Penrose server for Infinity-Topos"),
    ("bmorphism","bmorphism/manifold-mcp-server","JavaScript",14,9,5,"2026-04-15T19:54:28Z","MCP server for Manifold Markets"),
    ("bmorphism","bmorphism/risc0-cosmwasm-example","Rust",23,2,1,"2025-05-21T13:35:37Z","CosmWasm + zkVM RISC-V EFI template"),
    # zubyul
    ("zubyul","zubyul/voice-observatory","Python",0,0,0,"2026-04-24T05:56:20Z","Passive macOS TUI observing voice-download pathways"),
    ("zubyul","zubyul/ghostel-emacs-worlds","GLSL",0,0,0,"2026-04-24T00:21:00Z","Ghostty config + ghostel family"),
    ("zubyul","zubyul/big-bad-plurigrid-quiz","Emacs Lisp",0,0,0,"2026-04-09T18:51:35Z","27 flashcards from bmorphism/plurigrid/zubyul activity"),
    ("zubyul","zubyul/Gay.jl","Julia",0,0,0,"2026-03-28T11:30:07Z","Wide-gamut color sampling fork"),
    ("zubyul","zubyul/gay-world","Python",1,1,0,"2026-04-05T06:54:03Z","Goblin world builder"),
    ("zubyul","zubyul/tilelang-kernels","Python",0,0,0,"2026-03-16T02:31:16Z","TileLang GPU kernels for SplitMix64 color generation"),
    # migalkin
    ("migalkin","migalkin/kgcourse2021","HTML",24,8,0,"2026-07-10T15:40:00Z","Knowledge Graphs course materials"),
    ("migalkin","migalkin/NodePiece","Python",144,21,0,"2026-05-07T05:40:02Z","Compositional KG representations (ICLR22)"),
    ("migalkin","migalkin/StarE","Python",89,16,1,"2026-04-16T14:12:45Z","EMNLP 2020: Hyper-Relational KGs"),
    ("migalkin","migalkin/NBFNet_mlx","Python",10,1,1,"2026-03-11T01:31:21Z","Neural Bellman-Ford networks in MLX"),
    # DJedamski
    ("DJedamski","DJedamski/kaggle_ncaa18","Jupyter Notebook",0,0,0,"2018-02-26T16:33:24Z","NCAA March Madness competition code"),
    ("DJedamski","DJedamski/Kaggle","",1,0,0,"2023-04-21T01:42:35Z",""),
    # wasita
    ("wasita","wasita/wasita.github.io","Svelte",1,0,8,"2026-07-16T19:56:24Z","personal website"),
    ("wasita","wasita/pnas-typst-template","",0,0,0,"2026-07-16T19:36:20Z",""),
    ("wasita","wasita/wm-cv","Svelte",0,0,0,"2026-07-14T03:53:19Z","Academic CV web app"),
    ("wasita","wasita/magic-garden","Python",2,1,1,"2026-04-22T21:16:43Z","Discord magic garden bot"),
    # kristinezheng
    ("kristinezheng","kristinezheng/kristinezheng.github.io","HTML",0,0,0,"2026-07-01T20:57:48Z",""),
    ("kristinezheng","kristinezheng/lookit-jenga","Jupyter Notebook",0,0,0,"2024-05-16T18:29:05Z","Lookit study"),
    # M1shaaa
    ("M1shaaa","M1shaaa/M1shaaa","",0,0,0,"2026-02-04T19:32:04Z","Config files for GitHub profile"),
    ("M1shaaa","M1shaaa/lab-bookshelf-","TypeScript",0,0,0,"2024-12-31T05:11:18Z",""),
    ("M1shaaa","M1shaaa/Python-Lookit-Uploads","Python",0,0,0,"2024-02-15T22:59:37Z","random projects"),
    # AustinCStone
    ("AustinCStone","AustinCStone/byteruckus","HTML",0,0,0,"2026-07-15T05:19:33Z",""),
    ("AustinCStone","AustinCStone/TextGAN","Python",92,30,5,"2025-03-03T13:26:32Z","Generative adversarial network for text"),
    ("AustinCStone","AustinCStone/StereoVisionMRF","Python",11,4,0,"2026-04-01T07:39:41Z","MRF for depth from stereo images"),
    ("AustinCStone","AustinCStone/StructureFromMotion","Python",1,0,0,"2019-04-26T19:43:12Z","Recover 3D geometry from videos"),
]

# Insert repo snapshots with GF3 coloring
ts = datetime.now().isoformat()
for i, (org, full_name, lang, stars, forks, issues, pushed, desc) in enumerate(repos_data):
    trit, color, name = gf3(i)
    repo_name = full_name.split("/")[-1]
    # Insert increment
    con.execute("""
        INSERT INTO world_increments (id, timestamp, gf3_trit, gf3_color, gf3_name, source_type, source_name, event_type, repo_name, actor, snapshot_hash)
        VALUES (?, ?, ?, ?, ?, 'repo', ?, 'push', ?, ?, ?)
    """, [i+1, ts, trit, color, name, org, repo_name, org, f"snap_{i:04d}"])
    # Insert repo snapshot
    con.execute("""
        INSERT INTO repo_snapshots (id, timestamp, increment_id, org_or_user, repo_name, full_name, language, stars, forks, open_issues, pushed_at, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [i+1, ts, i+1, org, repo_name, full_name, lang, stars, forks, issues, pushed, desc])

# Aptos balances - all 28 addresses
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
    con.execute("INSERT INTO aptos_snapshots (timestamp, world, address, balance_apt) VALUES (?, ?, ?, ?)",
                [ts, world, addr, bal])

# Multisig probes - all returned 2 sigs (healthy)
multisig_data = [
    ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2,True),
    ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2,True),
    ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2,True),
    ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2,True),
    ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2,True),
]
for pair, addr, sigs, healthy in multisig_data:
    con.execute("INSERT INTO multisig_probes (timestamp, pair, address, sigs_required, healthy) VALUES (?, ?, ?, ?, ?)",
                [ts, pair, addr, sigs, healthy])

# MNX: SPA only - no data
# (no rows inserted into mnx_snapshots)

# Verify
r = con.execute("SELECT count(*) FROM world_increments").fetchone()[0]
rs = con.execute("SELECT count(*) FROM repo_snapshots").fetchone()[0]
ap = con.execute("SELECT count(*) FROM aptos_snapshots").fetchone()[0]
ms = con.execute("SELECT count(*) FROM multisig_probes").fetchone()[0]

print(f"world_increments: {r}")
print(f"repo_snapshots: {rs}")
print(f"aptos_snapshots: {ap}")
print(f"multisig_probes: {ms}")

# GF3 distribution
g = con.execute("SELECT gf3_name, count(*) FROM world_increments GROUP BY gf3_name").fetchall()
print("GF3 distribution:", g)

con.close()
print("DuckDB built OK.")
