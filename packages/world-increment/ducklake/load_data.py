#!/usr/bin/env python3
"""Load all sweep data into DuckDB."""
import duckdb, hashlib, json

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

def gf3(id_):
    t = id_ % 3
    if t == 0: return (0, "#d3869b", "ERGODIC")
    if t == 1: return (1, "#b8bb26", "PLUS")
    return (-1, "#cc241d", "MINUS")

def snap_hash(name):
    return hashlib.sha256(name.encode()).hexdigest()[:16]

# === WORLD INCREMENTS (one per source) ===
sources = [
    ("org", "plurigrid", "repo_snapshot"),
    ("org", "kubeflow", "repo_snapshot"),
    ("org", "TeglonLabs", "repo_snapshot"),
    ("user", "bmorphism", "repo_snapshot"),
    ("user", "zubyul", "repo_snapshot"),
    ("social_graph", "migalkin+DJedamski+wasita+kristinezheng+M1shaaa+AustinCStone", "repo_snapshot"),
]

for i, (st, sn, et) in enumerate(sources, 1):
    trit, color, name = gf3(i)
    con.execute(
        "INSERT INTO world_increments VALUES (?,now(),?,?,?,?,?,?,?,?,?)",
        [i, trit, color, name, st, sn, et, sn, sn, snap_hash(sn)]
    )

# === REPO SNAPSHOTS ===
repos = [
    # (increment_id, org_or_user, repo_name, full_name, language, stars, forks, open_issues, pushed_at, description)
    # plurigrid (increment 1)
    (1,"plurigrid","asi","plurigrid/asi","HTML",26,8,4,"2026-06-12","everything is topological chemputer!"),
    (1,"plurigrid","ontology","plurigrid/ontology","JavaScript",8,9,16,"2026-05-09","autopoietic ergodicity and embodied gradualism"),
    (1,"plurigrid","gorj","plurigrid/gorj","Clojure",0,0,738,"2026-05-08","forj + Rama topology nREPL routing + GF(3)"),
    (1,"plurigrid","nanoclj-zig","plurigrid/nanoclj-zig","Zig",1,1,20,"2026-04-25","NaN-boxed Clojure interpreter in Zig 0.15"),
    (1,"plurigrid","zig-syrup","plurigrid/zig-syrup","Zig",2,2,0,"2026-04-30","High-performance OCapN Syrup with CapTP"),
    (1,"plurigrid","nash-portal","plurigrid/nash-portal","Rust",2,3,1,"2026-05-19","NASH token TUI in the browser"),
    (1,"plurigrid","place","plurigrid/place","TeX",1,1,9,"2026-06-04","place"),
    (1,"plurigrid","eirobri","plurigrid/eirobri","Clojure",0,0,29,"2026-05-19","EiRoBri replay world"),
    (1,"plurigrid","asi-skills","plurigrid/asi-skills","Julia",3,0,0,"2026-04-26","69 skills with Galois Hole Type"),
    (1,"plurigrid","Plurigraph","plurigrid/Plurigraph","JavaScript",3,5,4,"2026-05-12","Plurigrid knowledge base for Obsidian"),
    (1,"plurigrid","microworlds","plurigrid/microworlds","Rust",3,5,3,"2024-03-14","microworlds"),
    (1,"plurigrid","vcg-auction","plurigrid/vcg-auction","Rust",7,2,1,"2025-12-16","a simple VCG auction contract"),
    (1,"plurigrid","agent","plurigrid/agent","Python",5,1,6,"2024-10-16","Framework for agency amplification"),
    (1,"plurigrid","StochFlow","plurigrid/StochFlow","Python",4,1,0,"2024-08-15","Stochastic interpolant models"),
    (1,"plurigrid","act","plurigrid/act","Python",3,1,4,"2024-11-25","building blocks for cognitive category theory"),
    # kubeflow (increment 2)
    (2,"kubeflow","kubeflow","kubeflow/kubeflow","None",15739,2680,0,"2026-06-21","Machine Learning Toolkit for Kubernetes"),
    (2,"kubeflow","pipelines","kubeflow/pipelines","Python",4157,2009,449,"2026-06-22","Machine Learning Pipelines for Kubeflow"),
    (2,"kubeflow","spark-operator","kubeflow/spark-operator","Python",3128,1490,104,"2026-06-22","Kubernetes operator for Apache Spark"),
    (2,"kubeflow","trainer","kubeflow/trainer","Go",2118,971,120,"2026-06-20","Distributed AI Model Training"),
    (2,"kubeflow","katib","kubeflow/katib","Python",1685,528,116,"2026-06-22","Automated Machine Learning on Kubernetes"),
    (2,"kubeflow","examples","kubeflow/examples","Jsonnet",1460,756,111,"2026-06-16","Examples and tutorials"),
    (2,"kubeflow","community-distribution","kubeflow/community-distribution","YAML",1027,1065,21,"2026-06-22","Kubeflow Community Distribution"),
    (2,"kubeflow","mcp-apache-spark-history-server","kubeflow/mcp-apache-spark-history-server","Python",177,65,21,"2026-06-19","MCP Server for Apache Spark History Server"),
    (2,"kubeflow","notebooks","kubeflow/notebooks",None,73,125,184,"2026-06-22","Kubeflow Notebooks"),
    (2,"kubeflow","sdk","kubeflow/sdk","Python",120,180,133,"2026-06-19","Universal Python SDK for AI workloads"),
    # TeglonLabs (increment 3)
    (3,"TeglonLabs","mathpix-gem","TeglonLabs/mathpix-gem","Ruby",2,0,11,"2026-01-01","Transform math images to LaTeX"),
    (3,"TeglonLabs","topoi","TeglonLabs/topoi","Python",0,0,1,"2025-01-24","topoi"),
    (3,"TeglonLabs","jank-crane","TeglonLabs/jank-crane","C++",0,0,0,"2026-06-08","crane-jank converged-IR hub"),
    (3,"TeglonLabs","monad-mcp-server","TeglonLabs/monad-mcp-server",None,0,0,0,"2025-05-14","Monad MCP Server"),
    (3,"TeglonLabs","coin-flip-mcp","TeglonLabs/coin-flip-mcp","JavaScript",0,2,1,"2025-03-16","MCP server for flipping coins"),
    # bmorphism (increment 4)
    (4,"bmorphism","ocaml-mcp-sdk","bmorphism/ocaml-mcp-sdk","OCaml",61,2,0,"2026-05-08","OCaml SDK for Model Context Protocol"),
    (4,"bmorphism","anti-bullshit-mcp-server","bmorphism/anti-bullshit-mcp-server","JavaScript",23,7,1,"2026-02-05","MCP server for analyzing claims"),
    (4,"bmorphism","say-mcp-server","bmorphism/say-mcp-server","JavaScript",20,9,3,"2026-03-19","MCP server for macOS TTS"),
    (4,"bmorphism","babashka-mcp-server","bmorphism/babashka-mcp-server","JavaScript",19,6,3,"2026-06-05","MCP server for Babashka"),
    (4,"bmorphism","manifold-mcp-server","bmorphism/manifold-mcp-server","JavaScript",14,9,5,"2026-04-15","MCP for Manifold Markets"),
    (4,"bmorphism","Gay.jl","bmorphism/Gay.jl","Julia",2,1,187,"2026-06-20","Wide-gamut color sampling with SPI"),
    (4,"bmorphism","penrose-mcp","bmorphism/penrose-mcp","JavaScript",10,4,0,"2026-04-12","Penrose server for Infinity-Topos"),
    (4,"bmorphism","risc0-cosmwasm-example","bmorphism/risc0-cosmwasm-example","Rust",23,2,1,"2025-05-21","CosmWasm + zkVM RISC-V EFI template"),
    (4,"bmorphism","world","bmorphism/world","Python",0,0,0,"2026-06-02","Local worlds launcher for SA3, jank"),
    (4,"bmorphism","satreadout","bmorphism/satreadout","HTML",0,0,0,"2026-06-20","Machine-checked saturating readout Lean 4"),
    # zubyul (increment 5)
    (5,"zubyul","gay-world","zubyul/gay-world","Python",1,1,0,"2026-04-05","Goblin world builder with MLX"),
    (5,"zubyul","WGCNA","zubyul/WGCNA","HTML",2,0,0,"2026-03-26","weighted gene correlation network analysis"),
    (5,"zubyul","jonikas_lab_data_analysis_misc","zubyul/jonikas_lab_data_analysis_misc","Jupyter Notebook",2,0,0,"2026-03-26","genetic sequence data analysis"),
    (5,"zubyul","Nikolova_lab_data_analysis","zubyul/Nikolova_lab_data_analysis","R",2,0,0,"2026-03-26","undergraduate thesis - cortical thickness"),
    (5,"zubyul","ghostel-emacs-worlds","zubyul/ghostel-emacs-worlds","GLSL",0,0,0,"2026-04-24","Ghostty config + ghostel family"),
    (5,"zubyul","tilelang-kernels","zubyul/tilelang-kernels","Python",0,0,0,"2026-03-16","TileLang GPU kernels for SplitMix64"),
    (5,"zubyul","big-bad-plurigrid-quiz","zubyul/big-bad-plurigrid-quiz","Emacs Lisp",0,0,0,"2026-04-09","27 flashcards from plurigrid activity"),
    (5,"zubyul","voice-observatory","zubyul/voice-observatory","Python",0,0,0,"2026-04-24","Passive macOS TUI for voice-download"),
    (5,"zubyul","kinesis-kb360pro","zubyul/kinesis-kb360pro","Python",0,0,0,"2026-03-26","Kinesis Advantage360 Pro keyboard skill"),
    # social graph (increment 6)
    (6,"migalkin","NodePiece","migalkin/NodePiece","Python",144,21,0,"2026-05-07","Compositional KG representations (ICLR'22)"),
    (6,"migalkin","StarE","migalkin/StarE","Python",89,16,1,"2026-04-16","Hyper-Relational KG message passing"),
    (6,"migalkin","kgcourse2021","migalkin/kgcourse2021","HTML",25,9,0,"2026-02-16","Knowledge Graphs course materials"),
    (6,"migalkin","NBFNet_mlx","migalkin/NBFNet_mlx","Python",10,1,1,"2026-03-11","Neural Bellman-Ford networks in MLX"),
    (6,"AustinCStone","TextGAN","AustinCStone/TextGAN","Python",92,30,5,"2025-03-03","GAN for text generation in TensorFlow"),
    (6,"wasita","wasita.github.io","wasita/wasita.github.io","Svelte",1,0,8,"2026-06-15","personal website"),
    (6,"wasita","magic-garden","wasita/magic-garden","Python",2,1,1,"2026-04-22","magic garden discord bot"),
    (6,"kristinezheng","Green-Machine","kristinezheng/Green-Machine","Python",0,0,0,"2021-09-19","HackMIT 2021 Sustainability"),
    (6,"M1shaaa","lab-bookshelf-","M1shaaa/lab-bookshelf-","TypeScript",0,0,0,"2024-12-31","lab-bookshelf"),
    (6,"DJedamski","Getting-and-Cleaning-Data","DJedamski/Getting-and-Cleaning-Data","R",1,0,0,"2023-04-21","Coursera Project"),
]

repo_id = 1
for r in repos:
    inc_id, org, rname, full, lang, stars, forks, issues, pushed, desc = r
    con.execute(
        "INSERT INTO repo_snapshots VALUES (?,now(),?,?,?,?,?,?,?,?,?,?)",
        [repo_id, inc_id, org, rname, full, lang or "", stars, forks, issues, pushed, desc or ""]
    )
    repo_id += 1

# === APTOS SNAPSHOTS ===
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
    con.execute("INSERT INTO aptos_snapshots VALUES (now(),?,?,?)", [world, addr, bal])

# === MULTISIG PROBES ===
multisig_data = [
    ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2,True),
    ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2,True),
    ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2,True),
    ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2,True),
    ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2,True),
]

for pair, addr, sigs, healthy in multisig_data:
    con.execute("INSERT INTO multisig_probes VALUES (now(),?,?,?,?)", [pair, addr, sigs, healthy])

# MNX: unavailable (Vercel auth protected)
# Insert placeholder noting unavailability
con.execute("INSERT INTO mnx_snapshots VALUES (now(),'N/A','MNX_UNAVAILABLE','vercel_auth_protected',0.0,0.0)")

con.commit()

# Print summary
print("=== DuckDB Summary ===")
print(f"world_increments: {con.execute('SELECT COUNT(*) FROM world_increments').fetchone()[0]}")
print(f"repo_snapshots: {con.execute('SELECT COUNT(*) FROM repo_snapshots').fetchone()[0]}")
print(f"aptos_snapshots: {con.execute('SELECT COUNT(*) FROM aptos_snapshots').fetchone()[0]}")
print(f"multisig_probes: {con.execute('SELECT COUNT(*) FROM multisig_probes').fetchone()[0]}")
print(f"mnx_snapshots: {con.execute('SELECT COUNT(*) FROM mnx_snapshots').fetchone()[0]}")
print()
print("GF3 color chain for increments:")
for row in con.execute("SELECT id, gf3_trit, gf3_color, gf3_name, source_type, source_name FROM world_increments ORDER BY id").fetchall():
    print(f"  [{row[0]}] trit={row[1]} {row[2]} {row[3]} | {row[4]}:{row[5]}")
print()
print("Multisig probes (all 2-of-2):")
for row in con.execute("SELECT pair, sigs_required, healthy FROM multisig_probes").fetchall():
    print(f"  {row[0]}: {row[1]} sigs required, healthy={row[2]}")
print()
print("Aptos balances (all 0 APT - no CoinStore resources found):")
for row in con.execute("SELECT world, balance_apt FROM aptos_snapshots ORDER BY world").fetchall():
    print(f"  {row[0]}: {row[1]} APT")

con.close()
print("\nDone.")
