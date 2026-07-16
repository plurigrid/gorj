#!/usr/bin/env python3
"""Build world-increments DuckDB from collected sweep data."""
import duckdb
import json
import hashlib
from datetime import datetime

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"

# GF(3) color chain
def gf3(id_):
    t = id_ % 3
    if t == 0: return (0, "#d3869b", "ERGODIC")
    if t == 1: return (1, "#b8bb26", "PLUS")
    return (-1, "#cc241d", "MINUS")

con = duckdb.connect(DB_PATH)

con.execute("""
CREATE TABLE IF NOT EXISTS world_increments (
  id INTEGER, timestamp TIMESTAMP DEFAULT now(), gf3_trit INTEGER,
  gf3_color VARCHAR, gf3_name VARCHAR, source_type VARCHAR,
  source_name VARCHAR, event_type VARCHAR, repo_name VARCHAR,
  actor VARCHAR, snapshot_hash VARCHAR
)
""")
con.execute("""
CREATE TABLE IF NOT EXISTS repo_snapshots (
  id INTEGER, timestamp TIMESTAMP DEFAULT now(), increment_id INTEGER,
  org_or_user VARCHAR, repo_name VARCHAR, full_name VARCHAR,
  language VARCHAR, stars INTEGER, forks INTEGER, open_issues INTEGER,
  pushed_at VARCHAR, description VARCHAR
)
""")
con.execute("CREATE SEQUENCE IF NOT EXISTS increment_seq START 1")
con.execute("CREATE SEQUENCE IF NOT EXISTS repo_seq START 1")
con.execute("""
CREATE TABLE IF NOT EXISTS aptos_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  world VARCHAR, address VARCHAR, balance_apt DOUBLE
)
""")
con.execute("""
CREATE TABLE IF NOT EXISTS multisig_probes (
  timestamp TIMESTAMP DEFAULT now(),
  pair VARCHAR, address VARCHAR, sigs_required INTEGER, healthy BOOLEAN
)
""")
con.execute("""
CREATE TABLE IF NOT EXISTS mnx_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  ticker VARCHAR, name VARCHAR, category VARCHAR,
  price DOUBLE, change_pct DOUBLE
)
""")

# --- Repo snapshots data ---
ALL_REPOS = [
  # (org_or_user, repo_name, full_name, language, stars, forks, open_issues, pushed_at, description)
  # plurigrid
  ("plurigrid","asi","plurigrid/asi","HTML",30,10,4,"2026-07-10T09:47:39Z","everything is topological chemputer!"),
  ("plurigrid","gorj","plurigrid/gorj","Clojure",1,0,1204,"2026-07-16T16:15:00Z","forj + Rama topology nREPL routing + GF(3) gay trit coloring"),
  ("plurigrid","place","plurigrid/place","TeX",1,1,13,"2026-07-14T09:11:33Z",""),
  ("plurigrid","eirobri","plurigrid/eirobri","Clojure",0,0,30,"2026-07-14T02:23:51Z","EiRoBri replay world"),
  ("plurigrid","nash-portal","plurigrid/nash-portal","Rust",2,3,1,"2026-05-19T01:49:59Z","NASH token TUI in the browser — ratzilla WASM + GeckoTerminal OHLCV candlesticks"),
  ("plurigrid","zig-syrup","plurigrid/zig-syrup","Zig",2,2,0,"2026-04-30T03:52:16Z","High-performance Zig implementation of OCapN Syrup with CapTP optimizations"),
  ("plurigrid","asi-skills","plurigrid/asi-skills","Julia",3,0,0,"2026-04-26T08:09:26Z","69 skills with Galois Hole Type accessibility"),
  ("plurigrid","nanoclj-zig","plurigrid/nanoclj-zig","Zig",1,1,20,"2026-04-25T07:29:09Z","NaN-boxed Clojure interpreter in Zig 0.15"),
  ("plurigrid","ontology","plurigrid/ontology","JavaScript",8,9,16,"2025-05-27T18:18:34Z","autopoietic ergodicity and embodied gradualism"),
  ("plurigrid","Plurigraph","plurigrid/Plurigraph","JavaScript",3,5,4,"2025-01-05T08:39:09Z","Plurigrid knowledge base for use with Obsidian.md"),
  ("plurigrid","act","plurigrid/act","Python",3,1,4,"2024-07-26T08:27:08Z","building blocks for cognitive category theory"),
  # kubeflow top repos
  ("kubeflow","kubeflow","kubeflow/kubeflow","",15779,2685,0,"2026-07-16T09:38:14Z","Machine Learning Toolkit for Kubernetes"),
  ("kubeflow","pipelines","kubeflow/pipelines","Python",4167,2035,427,"2026-07-16T04:03:32Z","Machine Learning Pipelines for Kubeflow"),
  ("kubeflow","trainer","kubeflow/trainer","Go",2150,988,133,"2026-07-15T23:41:08Z","Distributed AI Model Training and LLM Fine-Tuning on Kubernetes"),
  ("kubeflow","spark-operator","kubeflow/spark-operator","Python",3137,1500,106,"2026-07-16T16:01:22Z","Kubernetes operator for managing the lifecycle of Apache Spark applications"),
  ("kubeflow","katib","kubeflow/katib","Python",1690,533,103,"2026-07-16T14:39:00Z","Automated Machine Learning on Kubernetes"),
  ("kubeflow","sdk","kubeflow/sdk","Python",125,196,161,"2026-07-16T14:52:34Z","Universal Python SDK to run AI workloads on Kubernetes"),
  ("kubeflow","hub","kubeflow/hub","Go",177,188,26,"2026-07-16T15:23:53Z","Model Registry for ML model developers"),
  ("kubeflow","mcp-apache-spark-history-server","kubeflow/mcp-apache-spark-history-server","Python",183,65,18,"2026-07-16T14:15:54Z","MCP Server and CLI for Apache Spark History Server"),
  ("kubeflow","mcp-server","kubeflow/mcp-server","Python",26,31,50,"2026-07-16T15:22:42Z","MCP Server for AI-Assisted Development with Kubeflow Tools"),
  # TeglonLabs
  ("TeglonLabs","jank-crane","TeglonLabs/jank-crane","C++",0,0,0,"2026-06-08T19:03:37Z","crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps"),
  ("TeglonLabs","mathpix-gem","TeglonLabs/mathpix-gem","Ruby",2,0,11,"2026-01-01T12:13:16Z","Transform mathematical images to LaTeX with security-first design"),
  ("TeglonLabs","coin-flip-mcp","TeglonLabs/coin-flip-mcp","JavaScript",0,2,1,"2025-03-16T01:31:45Z","MCP server for flipping coins with varying degrees of randomness"),
  ("TeglonLabs","topoi","TeglonLabs/topoi","Python",0,0,1,"2025-01-24T06:47:38Z",""),
  # bmorphism top repos
  ("bmorphism","Gay.jl","bmorphism/Gay.jl","Julia",2,1,187,"2026-07-14T08:57:38Z","Wide-gamut color sampling with splittable determinism"),
  ("bmorphism","gay-chat","bmorphism/gay-chat","Scheme",0,0,0,"2026-07-14T21:00:00Z","gay://chat operationalization over Spritely Brassica Chat"),
  ("bmorphism","anti-bullshit-mcp-server","bmorphism/anti-bullshit-mcp-server","JavaScript",22,7,1,"2026-07-12T19:31:54Z","MCP server for analyzing claims and detecting manipulation"),
  ("bmorphism","ocaml-mcp-sdk","bmorphism/ocaml-mcp-sdk","OCaml",61,2,0,"2026-05-08T16:50:34Z","OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect library"),
  ("bmorphism","whale","bmorphism/whale","MATLAB",2,0,0,"2026-04-20T15:04:09Z","omniglot + sperm whale codas = metawhaling"),
  # zubyul top repos
  ("zubyul","voice-observatory","zubyul/voice-observatory","Python",0,0,0,"2026-04-24T05:56:20Z","Passive macOS TUI observing voice-download pathways"),
  ("zubyul","Gay.jl","zubyul/Gay.jl","Julia",0,0,0,"2026-03-28T11:30:07Z","Wide-gamut color sampling with splittable determinism"),
  ("zubyul","gay-world","zubyul/gay-world","Python",1,1,0,"2026-04-05T06:54:03Z","Goblin world builder: each goblin is a world"),
  # social graph
  ("migalkin","NodePiece","migalkin/NodePiece","Python",144,21,0,"2026-05-07T05:40:02Z","Compositional and Parameter-Efficient Representations for Large Knowledge Graphs"),
  ("migalkin","StarE","migalkin/StarE","Python",89,16,1,"2026-04-16T14:12:45Z","EMNLP 2020: Message Passing for Hyper-Relational Knowledge Graphs"),
  ("migalkin","kgcourse2021","migalkin/kgcourse2021","HTML",24,8,0,"2026-07-10T15:40:00Z","Материалы к курсу по Knowledge Graphs"),
  ("DJedamski","kaggle_ncaa18","DJedamski/kaggle_ncaa18","Jupyter Notebook",0,0,0,"2018-02-26T16:33:24Z","Code for NCAA March Madness competition (2018)"),
  ("wasita","wasita.github.io","wasita/wasita.github.io","Svelte",1,0,8,"2026-07-14T17:55:08Z","personal website"),
  ("wasita","magic-garden","wasita/magic-garden","Python",2,1,1,"2026-04-22T21:16:43Z","bot for magic garden discord activity game"),
  ("kristinezheng","kristinezheng.github.io","kristinezheng/kristinezheng.github.io","HTML",0,0,0,"2026-07-01T20:57:48Z",""),
  ("M1shaaa","lab-bookshelf-","M1shaaa/lab-bookshelf-","TypeScript",0,0,0,"2024-12-31T05:11:18Z",""),
  ("AustinCStone","byteruckus","AustinCStone/byteruckus","HTML",0,0,0,"2026-07-15T05:19:33Z",""),
  ("AustinCStone","TextGAN","AustinCStone/TextGAN","Python",92,30,5,"2025-03-03T13:26:32Z","A generative adversarial network for text generation in TensorFlow"),
]

# Insert world_increments + repo_snapshots
print("Inserting repo data...")
for i, (ou, rn, fn, lang, stars, forks, issues, pushed, desc) in enumerate(ALL_REPOS, 1):
    trit, color, name = gf3(i)
    snap_hash = hashlib.sha256(fn.encode()).hexdigest()[:16]
    con.execute("""
        INSERT INTO world_increments (id, gf3_trit, gf3_color, gf3_name, source_type, source_name,
            event_type, repo_name, actor, snapshot_hash)
        VALUES (?, ?, ?, ?, 'repo_snapshot', ?, 'push', ?, ?, ?)
    """, [i, trit, color, name, ou, rn, ou, snap_hash])
    con.execute("""
        INSERT INTO repo_snapshots (id, increment_id, org_or_user, repo_name, full_name,
            language, stars, forks, open_issues, pushed_at, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [i, i, ou, rn, fn, lang, stars, forks, issues, pushed, desc[:100]])

# Aptos balances
print("Inserting Aptos snapshots...")
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
    con.execute("INSERT INTO aptos_snapshots (world, address, balance_apt) VALUES (?, ?, ?)",
                [world, addr, bal])

# Multisig probes
print("Inserting multisig probes...")
multisig_data = [
  ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2,True),
  ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2,True),
  ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2,True),
  ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2,True),
  ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2,True),
]
for pair, addr, sigs, healthy in multisig_data:
    con.execute("INSERT INTO multisig_probes (pair, address, sigs_required, healthy) VALUES (?, ?, ?, ?)",
                [pair, addr, sigs, healthy])

con.commit()

# Verify counts
counts = {
    'world_increments': con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0],
    'repo_snapshots': con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0],
    'aptos_snapshots': con.execute("SELECT COUNT(*) FROM aptos_snapshots").fetchone()[0],
    'multisig_probes': con.execute("SELECT COUNT(*) FROM multisig_probes").fetchone()[0],
    'mnx_snapshots': con.execute("SELECT COUNT(*) FROM mnx_snapshots").fetchone()[0],
}
print("Table counts:", json.dumps(counts, indent=2))

# GF3 distribution
gf3_dist = con.execute("""
    SELECT gf3_name, gf3_color, COUNT(*) as cnt
    FROM world_increments GROUP BY gf3_name, gf3_color ORDER BY gf3_name
""").fetchall()
print("GF(3) distribution:", gf3_dist)

# Top repos by stars
top_repos = con.execute("""
    SELECT org_or_user, repo_name, stars FROM repo_snapshots
    ORDER BY stars DESC LIMIT 10
""").fetchall()
print("Top 10 repos by stars:", top_repos)

con.close()
print("DuckDB built successfully.")
