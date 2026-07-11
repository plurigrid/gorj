#!/usr/bin/env python3
"""Build world-increments DuckDB from collected sweep data."""
import duckdb, json, hashlib

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
con = duckdb.connect(DB)

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

def gf3(n):
    t = n % 3
    if t == 0: return (0, '#d3869b', 'ERGODIC')
    if t == 1: return (1, '#b8bb26', 'PLUS')
    return (-1, '#cc241d', 'MINUS')

def snap_hash(s): return hashlib.md5(s.encode()).hexdigest()[:12]

# GitHub repo data (collected via MCP)
repos = [
  # (org_or_user, repo_name, full_name, language, stars, forks, open_issues, pushed_at, description)
  # plurigrid
  ('plurigrid','asi','plurigrid/asi','HTML',30,9,4,'2026-07-10','everything is topological chemputer!'),
  ('plurigrid','gorj','plurigrid/gorj','Clojure',1,0,1124,'2026-07-11','forj + Rama topology nREPL routing + GF(3) gay trit coloring'),
  ('plurigrid','shrimp','plurigrid/shrimp',None,0,0,0,'2026-07-03','Jank worked example: shrimp'),
  ('plurigrid','place','plurigrid/place','TeX',1,1,12,'2026-07-07',None),
  ('plurigrid','eirobri','plurigrid/eirobri','Clojure',0,0,30,'2026-06-30','EiRoBri replay world'),
  ('plurigrid','nash-portal','plurigrid/nash-portal','Rust',2,3,1,'2026-05-19','NASH token TUI in the browser'),
  ('plurigrid','zig-syrup','plurigrid/zig-syrup','Zig',2,2,0,'2026-04-30','High-performance Zig OCapN Syrup'),
  ('plurigrid','asi-skills','plurigrid/asi-skills','Julia',3,0,0,'2026-04-26','69 skills with Galois Hole Type accessibility'),
  ('plurigrid','ontology','plurigrid/ontology','JavaScript',8,9,16,'2025-05-27','autopoietic ergodicity and embodied gradualism'),
  ('plurigrid','StochFlow','plurigrid/StochFlow','Python',4,1,0,'2024-03-20','stochastic interpolant models'),
  ('plurigrid','act','plurigrid/act','Python',3,1,4,'2024-07-26','building blocks for cognitive category theory'),
  ('plurigrid','Plurigraph','plurigrid/Plurigraph','JavaScript',3,5,4,'2025-01-05','Plurigrid knowledge base for Obsidian'),
  # TeglonLabs
  ('TeglonLabs','jank-crane','TeglonLabs/jank-crane','C++',0,0,0,'2026-06-08','crane-jank converged-IR hub'),
  ('TeglonLabs','mathpix-gem','TeglonLabs/mathpix-gem','Ruby',2,0,11,'2026-01-01','Mathematical OCR in Ruby'),
  ('TeglonLabs','coin-flip-mcp','TeglonLabs/coin-flip-mcp','JavaScript',0,2,1,'2025-09-21','MCP server for flipping coins'),
  ('TeglonLabs','monad-mcp-server','TeglonLabs/monad-mcp-server',None,0,0,0,'2025-05-14','Monad MCP Server'),
  ('TeglonLabs','topoi','TeglonLabs/topoi','Python',0,0,1,'2025-01-24',None),
  # bmorphism highlights
  ('bmorphism','Gay.jl','bmorphism/Gay.jl','Julia',2,1,187,'2026-06-20','Wide-gamut color sampling with splittable determinism'),
  ('bmorphism','ocaml-mcp-sdk','bmorphism/ocaml-mcp-sdk','OCaml',61,2,0,'2026-05-08','OCaml SDK for Model Context Protocol'),
  ('bmorphism','anti-bullshit-mcp-server','bmorphism/anti-bullshit-mcp-server','JavaScript',23,7,1,'2026-02-05','MCP server for claim analysis'),
  ('bmorphism','say-mcp-server','bmorphism/say-mcp-server','JavaScript',20,9,3,'2026-03-19','MCP server for macOS TTS'),
  ('bmorphism','babashka-mcp-server','bmorphism/babashka-mcp-server','JavaScript',19,6,3,'2026-06-05','MCP server for Babashka/Clojure'),
  ('bmorphism','penrose-mcp','bmorphism/penrose-mcp','JavaScript',9,4,0,'2026-06-24','Penrose server for Infinity-Topos'),
  ('bmorphism','satreadout','bmorphism/satreadout','HTML',0,0,0,'2026-06-20','Machine-checked saturating perceptual readout'),
  ('bmorphism','risc0-cosmwasm-example','bmorphism/risc0-cosmwasm-example','Rust',23,2,1,'2025-05-21','CosmWasm + zkVM RISC-V EFI template'),
  # zubyul
  ('zubyul','voice-observatory','zubyul/voice-observatory','Python',0,0,0,'2026-04-24','Passive macOS TUI observing voice-download pathways'),
  ('zubyul','kinesis-kb360pro','zubyul/kinesis-kb360pro','Python',0,0,0,'2026-03-26','Claude Code skill for Kinesis Advantage360 Pro'),
  ('zubyul','gay-world','zubyul/gay-world','Python',1,1,0,'2026-04-05','Goblin world builder with MLX'),
  # kubeflow highlights
  ('kubeflow','kubeflow','kubeflow/kubeflow',None,15770,2685,0,'2026-07-11','Machine Learning Toolkit for Kubernetes'),
  ('kubeflow','pipelines','kubeflow/pipelines','Python',4169,2030,419,'2026-07-11','Machine Learning Pipelines for Kubeflow'),
  ('kubeflow','trainer','kubeflow/trainer','Go',2136,983,144,'2026-07-11','Distributed AI Model Training'),
  ('kubeflow','spark-operator','kubeflow/spark-operator','Python',3137,1500,110,'2026-07-11','Kubernetes operator for Apache Spark'),
  ('kubeflow','mcp-server','kubeflow/mcp-server','Python',20,28,25,'2026-07-10','MCP Server for AI-Assisted Kubeflow Dev'),
  ('kubeflow','mcp-apache-spark-history-server','kubeflow/mcp-apache-spark-history-server','Python',182,65,19,'2026-07-07','MCP Server for Apache Spark History Server'),
  # migalkin
  ('migalkin','NodePiece','migalkin/NodePiece','Python',144,21,0,'2026-05-07','Compositional KG Representations (ICLR22)'),
  ('migalkin','StarE','migalkin/StarE','Python',89,16,1,'2026-04-16','Message Passing for Hyper-Relational KGs (EMNLP20)'),
  ('migalkin','NBFNet_mlx','migalkin/NBFNet_mlx','Python',10,1,1,'2026-03-11','Neural Bellman-Ford networks in MLX'),
  # DJedamski
  ('DJedamski','Getting-and-Cleaning-Data','DJedamski/Getting-and-Cleaning-Data','R',1,0,0,'2023-04-21','Coursera Project'),
  # wasita
  ('wasita','wasita.github.io','wasita/wasita.github.io','Svelte',1,0,8,'2026-07-06','personal website'),
  ('wasita','magic-garden','wasita/magic-garden','Python',2,1,1,'2026-04-22','Discord magic garden bot'),
  # kristinezheng
  ('kristinezheng','kristinezheng.github.io','kristinezheng/kristinezheng.github.io','HTML',0,0,0,'2026-07-01','personal site'),
  # M1shaaa
  ('M1shaaa','lab-bookshelf-','M1shaaa/lab-bookshelf-','TypeScript',0,0,0,'2024-12-31',None),
  # AustinCStone
  ('AustinCStone','TextGAN','AustinCStone/TextGAN','Python',92,30,5,'2025-03-03','GAN for text generation in TensorFlow'),
  ('AustinCStone','StereoVisionMRF','AustinCStone/StereoVisionMRF','Python',11,4,0,'2026-04-01','MRF for depth from stereo images'),
]

# Insert repo_snapshots and world_increments
con.execute("DELETE FROM repo_snapshots")
con.execute("DELETE FROM world_increments")
for i, r in enumerate(repos, 1):
    trit, color, name = gf3(i)
    org, rname, full, lang, stars, forks, issues, pushed, desc = r
    h = snap_hash(full)
    con.execute("""INSERT INTO world_increments VALUES (?,now(),?,?,?,'github_repo',?,?,?,?,?)""",
        [i, trit, color, name, org, 'repo_snapshot', rname, org, h])
    con.execute("""INSERT INTO repo_snapshots VALUES (?,now(),?,?,?,?,?,?,?,?,?,?)""",
        [i, i, org, rname, full, lang, stars, forks, issues, pushed, desc])

# Aptos snapshots
con.execute("DELETE FROM aptos_snapshots")
aptos = [
  ('alice','0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b',0.0),
  ('bob','0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d',0.0),
  ('A','0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a',0.0),
  ('B','0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13',0.0),
  ('C','0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e',0.0),
  ('D','0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1',0.0),
  ('E','0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36',0.0),
  ('F','0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71',0.0),
  ('G','0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32',0.0),
  ('H','0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f',0.0),
  ('I','0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9',0.0),
  ('J','0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54',0.0),
  ('K','0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4',0.0),
  ('L','0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9',0.0),
  ('M','0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9',0.0),
  ('N','0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c',0.0),
  ('O','0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d',0.0),
  ('P','0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948',0.0),
  ('Q','0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9',0.0),
  ('R','0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10',0.0),
  ('S','0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386',0.0),
  ('T','0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588',0.0),
  ('U','0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956',0.0),
  ('V','0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3',0.0),
  ('W','0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0',0.0),
  ('X','0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d',0.0),
  ('Y','0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4',0.0),
  ('Z','0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c',0.0),
]
for w, a, b in aptos:
    con.execute("INSERT INTO aptos_snapshots VALUES (now(),?,?,?)", [w, a, b])

# Multisig probes
con.execute("DELETE FROM multisig_probes")
multisig = [
  ('A-B','0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003',2,True),
  ('A-G','0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096',2,True),
  ('Y-Z','0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883',2,True),
  ('S-T','0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883',2,True),
  ('V-W','0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d',2,True),
]
for pair, addr, sigs, healthy in multisig:
    con.execute("INSERT INTO multisig_probes VALUES (now(),?,?,?,?)", [pair, addr, sigs, healthy])

con.close()
print("DB built successfully")
print(f"Tables: world_increments, repo_snapshots, aptos_snapshots, multisig_probes, mnx_snapshots")

# Verify
con2 = duckdb.connect(DB)
for tbl in ['world_increments','repo_snapshots','aptos_snapshots','multisig_probes']:
    n = con2.execute(f"SELECT count(*) FROM {tbl}").fetchone()[0]
    print(f"  {tbl}: {n} rows")
con2.close()
