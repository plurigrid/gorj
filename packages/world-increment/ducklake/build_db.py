#!/usr/bin/env python3
"""Build world-increments DuckDB from sweep data."""
import duckdb
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "world-increments.duckdb")
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

def gf3(id_val):
    m = id_val % 3
    if m == 0: return (0, "#d3869b", "ERGODIC")
    if m == 1: return (1, "#b8bb26", "PLUS")
    return (-1, "#cc241d", "MINUS")

# All repos collected from sweep
REPOS = [
    # plurigrid
    ("plurigrid","plurigrid/gorj","Clojure",1,0,1512,"2026-07-30T13:14:38Z","forj + Rama topology nREPL routing + GF(3) gay trit coloring"),
    ("plurigrid","plurigrid/zig-syrup","Zig",2,2,0,"2026-07-28T13:02:13Z","High-performance Zig implementation of OCapN Syrup with CapTP optimizations"),
    ("plurigrid","plurigrid/asi","HTML",56,13,4,"2026-07-10T09:47:39Z","everything is topological chemputer!"),
    ("plurigrid","plurigrid/shrimp",None,0,0,0,"2026-07-03T01:24:20Z","Jank worked example: shrimp"),
    ("plurigrid","plurigrid/place","TeX",1,2,14,"2026-07-14T09:11:33Z",None),
    ("plurigrid","plurigrid/eirobri","Clojure",0,0,31,"2026-07-21T02:24:02Z","EiRoBri replay world"),
    ("plurigrid","plurigrid/nash-portal","Rust",2,2,1,"2026-05-19T01:49:59Z","NASH token TUI in the browser"),
    ("plurigrid","plurigrid/asi-skills","Julia",3,0,0,"2026-04-26T08:09:26Z","69 skills with Galois Hole Type accessibility"),
    ("plurigrid","plurigrid/bci-blue-share","JavaScript",0,0,0,"2026-04-26T07:08:03Z","BCI signal infrastructure"),
    ("plurigrid","plurigrid/nanoclj-zig","Zig",1,1,20,"2026-04-25T07:29:09Z","NaN-boxed Clojure interpreter in Zig 0.15"),
    ("plurigrid","plurigrid/spi-race","Swift",0,0,0,"2026-04-21T19:31:56Z","Splitmix Parallel Integrity"),
    ("plurigrid","plurigrid/reafference","HTML",0,0,0,"2026-04-16T05:21:49Z","Reafference adaptation workspace"),
    ("plurigrid","plurigrid/web-browser","Rust",0,0,0,"2026-04-10T02:54:47Z","web-browser from prepostweb lineage"),
    ("plurigrid","plurigrid/vivarium","Clojure",1,0,0,"2026-04-08T08:38:37Z",None),
    ("plurigrid","plurigrid/gatomic","Clojure",0,0,0,"2026-03-30T00:54:48Z","Deterministic color identity store with sonification"),
    ("plurigrid","plurigrid/forester","XSLT",0,0,0,"2026-03-30T01:32:26Z","CatColab mathematical documentation forest"),
    ("plurigrid","plurigrid/gay-tofu","HTML",0,0,0,"2026-01-08T15:14:34Z","Low-discrepancy color sequences for visual TOFU authentication"),
    ("plurigrid","plurigrid/lazygay","Go",0,0,0,"2026-01-08T14:19:25Z","lazygit fork with Gay.jl deterministic commit coloring"),
    ("plurigrid","plurigrid/gay-rs","Rust",0,0,0,"2026-01-08T14:19:22Z","Rust crate for Gay.jl deterministic coloring"),
    ("plurigrid","plurigrid/gay-go","Go",0,0,0,"2026-01-08T14:19:23Z","Go implementation of Gay.jl deterministic coloring"),
    ("plurigrid","plurigrid/gay-terminal","Rust",0,0,0,"2026-01-08T14:19:24Z","Terminal ANSI coloring with Gay.jl"),
    ("plurigrid","plurigrid/lazybjj","Rust",0,0,0,"2026-01-08T14:19:19Z","TUI for jj with Gay.jl GF(3) coloring"),
    ("plurigrid","plurigrid/leprechauns","Racket",0,0,0,"2026-01-23T07:46:46Z","Spritely Goblins + Gay.jl semantic colors"),
    ("plurigrid","plurigrid/hoot","Scheme",0,0,1,"2026-01-23T07:47:10Z","Spritely Hoot - Scheme to WebAssembly compiler"),
    ("plurigrid","plurigrid/ontology","JavaScript",8,9,16,"2025-05-27T18:18:34Z","autopoietic ergodicity and embodied gradualism"),
    ("plurigrid","plurigrid/vcg-auction","Rust",7,3,1,"2023-03-16T21:53:08Z","a simple contract that performs a VCG auction"),
    ("plurigrid","plurigrid/agent","Python",5,1,6,"2023-03-31T18:45:23Z","Framework for agency amplification"),
    ("plurigrid","plurigrid/microworlds","Rust",3,5,3,"2023-05-13T03:54:56Z",None),
    ("plurigrid","plurigrid/StochFlow","Python",4,1,0,"2024-03-20T23:34:57Z","stochastic interpolant models and algorithms"),
    ("plurigrid","plurigrid/Plurigraph","JavaScript",3,5,4,"2025-01-05T08:39:09Z","Plurigrid knowledge base for Obsidian.md"),
    # kubeflow top repos
    ("kubeflow","kubeflow/kubeflow",None,15798,2690,0,"2026-07-10T11:31:26Z","Machine Learning Toolkit for Kubernetes"),
    ("kubeflow","kubeflow/pipelines","Python",4171,2071,498,"2026-07-29T20:28:13Z","Machine Learning Pipelines for Kubeflow"),
    ("kubeflow","kubeflow/spark-operator","Python",3142,1510,112,"2026-07-29T18:25:53Z","Kubernetes operator for Apache Spark"),
    ("kubeflow","kubeflow/trainer","Go",2163,1004,125,"2026-07-30T03:08:36Z","Distributed AI Model Training on Kubernetes"),
    ("kubeflow","kubeflow/katib","Python",1694,532,107,"2026-07-26T16:12:12Z","Automated Machine Learning on Kubernetes"),
    ("kubeflow","kubeflow/examples","Jsonnet",1461,755,111,"2025-04-14T01:54:52Z","Extended examples and tutorials"),
    ("kubeflow","kubeflow/community-distribution","YAML",1029,1070,26,"2026-07-29T12:00:24Z","Kubeflow Community Distribution"),
    ("kubeflow","kubeflow/arena","Go",816,196,44,"2026-07-29T06:03:45Z","A CLI for Kubeflow"),
    ("kubeflow","kubeflow/kale","Python",698,158,59,"2026-07-27T11:51:22Z","Kubeflow's superfood for Data Scientists"),
    ("kubeflow","kubeflow/mpi-operator","Go",530,238,102,"2026-07-28T08:49:54Z","Kubernetes Operator for MPI-based applications"),
    ("kubeflow","kubeflow/mcp-server","Python",31,38,34,"2026-07-30T11:34:09Z","MCP Server for AI-Assisted Development with Kubeflow Tools"),
    ("kubeflow","kubeflow/hub","Go",179,189,26,"2026-07-30T12:24:10Z","Model Registry for ML model developers"),
    ("kubeflow","kubeflow/mlflow-integration","Python",7,7,3,"2026-07-30T13:12:51Z",None),
    # TeglonLabs
    ("TeglonLabs","TeglonLabs/jank-crane","C++",0,0,0,"2026-06-08T19:03:03Z","crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps"),
    ("TeglonLabs","TeglonLabs/mathpix-gem","Ruby",2,0,11,"2026-01-01T12:13:13Z","Transform mathematical images to LaTeX"),
    ("TeglonLabs","TeglonLabs/coin-flip-mcp","JavaScript",0,2,1,"2025-09-21T08:57:27Z","MCP server for flipping coins with varying degrees of randomness"),
    ("TeglonLabs","TeglonLabs/monad-mcp-server",None,0,0,0,"2025-05-14T11:36:14Z","Monad MCP Server"),
    ("TeglonLabs","TeglonLabs/topoi","Python",0,0,1,"2025-01-24T04:49:26Z",None),
    # bmorphism top repos
    ("bmorphism","bmorphism/Gay.jl","Julia",2,1,188,"2026-07-30T02:12:32Z","Wide-gamut color sampling with splittable determinism"),
    ("bmorphism","bmorphism/ocaml-mcp-sdk","OCaml",61,2,0,"2026-03-16T05:24:25Z","OCaml SDK for Model Context Protocol"),
    ("bmorphism","bmorphism/risc0-cosmwasm-example","Rust",23,2,1,"2022-10-20T23:50:40Z","CosmWasm + zkVM RISC-V EFI template"),
    ("bmorphism","bmorphism/anti-bullshit-mcp-server","JavaScript",22,7,1,"2026-01-16T08:54:58Z","MCP server for analyzing claims and detecting manipulation"),
    ("bmorphism","bmorphism/say-mcp-server","JavaScript",20,9,3,"2025-01-07T03:15:18Z","MCP server for macOS text-to-speech"),
    ("bmorphism","bmorphism/babashka-mcp-server","JavaScript",19,6,3,"2025-01-05T11:09:42Z","MCP server for Babashka"),
    ("bmorphism","bmorphism/manifold-mcp-server","JavaScript",14,9,5,"2025-01-11T10:36:58Z","MCP server for Manifold Markets prediction markets"),
    ("bmorphism","bmorphism/penrose-mcp","JavaScript",9,4,0,"2025-01-20T21:44:55Z","Penrose server for Infinity-Topos"),
    ("bmorphism","bmorphism/nats-mcp-server",None,7,3,2,"2025-01-06T23:33:41Z","MCP server for NATS messaging system"),
    ("bmorphism","bmorphism/marginalia-mcp-server","JavaScript",8,6,0,"2025-01-06T05:47:24Z","MCP server for managing marginalia and annotations"),
    ("bmorphism","bmorphism/hypernym-mcp-server","JavaScript",6,5,0,"2025-04-02T21:21:08Z",None),
    ("bmorphism","bmorphism/shitcoin","Python",5,0,0,"2026-04-08T08:07:08Z","gets denom for cw20 assets for permissionless degeneracy in IBC"),
    ("bmorphism","bmorphism/penumbra-mcp","JavaScript",5,6,3,"2025-01-07T01:15:23Z","MCP server for Penumbra blockchain"),
    # zubyul notable
    ("zubyul","zubyul/gay-world","Python",1,1,0,"2026-03-26T04:03:39Z","Goblin world builder: Gay.jl + MLX"),
    ("zubyul","zubyul/from-possible-worlds","TeX",0,0,1,"2026-07-18T12:02:57Z",None),
    ("zubyul","zubyul/voice-observatory","Python",0,0,0,"2026-04-24T05:56:17Z","Passive macOS TUI observing voice-download pathways"),
    ("zubyul","zubyul/nash-tui","Rust",0,0,0,"2026-04-13T07:45:16Z","NASH token TUI: real-time candles via GeckoTerminal"),
    ("zubyul","zubyul/jonikas_lab_data_analysis_misc","Jupyter Notebook",2,0,0,"2023-08-16T20:24:40Z","various scripts for large genetic sequence data"),
    ("zubyul","zubyul/WGCNA","HTML",2,0,0,"2023-07-05T18:02:30Z","weighted gene correlation network analysis"),
    # migalkin
    ("migalkin","migalkin/NodePiece","Python",144,21,0,"2026-05-07T05:40:02Z","Compositional Representations for Large Knowledge Graphs (ICLR'22)"),
    ("migalkin","migalkin/StarE","Python",89,16,1,"2026-04-16T14:12:45Z","Message Passing for Hyper-Relational Knowledge Graphs (EMNLP 2020)"),
    ("migalkin","migalkin/kgcourse2021","HTML",24,8,0,"2026-07-10T15:40:00Z","Materials for Knowledge Graphs course"),
    ("migalkin","migalkin/NBFNet_mlx","Python",10,1,1,"2026-03-11T01:31:21Z","Neural Bellman-Ford networks in MLX for Apple Silicon"),
    ("migalkin","migalkin/RWL","Python",8,1,0,"2026-05-28T20:19:20Z","Weisfeiler and Leman Go Relational (LOG 2022)"),
    ("migalkin","migalkin/rambo","Rust",3,0,1,"2023-02-28T16:37:22Z",None),
    # AustinCStone
    ("AustinCStone","AustinCStone/TextGAN","Python",92,30,5,"2025-03-03T13:26:32Z","GAN for text generation in TensorFlow"),
    ("AustinCStone","AustinCStone/byteruckus","HTML",0,0,0,"2026-07-15T05:19:33Z",None),
    ("AustinCStone","AustinCStone/StereoVisionMRF","Python",11,4,0,"2026-04-01T07:39:41Z","Infer depth from stereo images with MRF"),
    ("AustinCStone","AustinCStone/SpectralClustering","Python",3,2,0,"2021-04-16T08:46:36Z","Spectral clustering"),
    ("AustinCStone","AustinCStone/bmfork","Python",0,0,1,"2025-05-09T04:18:54Z",None),
    # DJedamski
    ("DJedamski","DJedamski/kaggle_ncaa18","Jupyter Notebook",0,0,0,"2018-02-26T16:33:24Z","Code for NCAA March Madness competition 2018"),
    ("DJedamski","DJedamski/Kaggle","None",1,0,0,"2023-04-21T01:42:35Z",None),
    ("DJedamski","DJedamski/School","R",1,1,0,"2023-04-21T01:42:33Z","Projects from grad school"),
    # wasita
    ("wasita","wasita/wasita.github.io","Svelte",1,0,8,"2026-07-21T15:55:45Z","personal website"),
    ("wasita","wasita/magic-garden","Python",2,1,1,"2026-04-22T21:16:43Z","bot for magic garden discord game"),
    ("wasita","wasita/wm-cv","Svelte",0,0,0,"2026-07-14T03:53:19Z","Academic CV as web app"),
    ("wasita","wasita/send2kobo","TypeScript",1,0,0,"2026-05-19T02:59:26Z","Website for sending books to kobo e-reader"),
    # kristinezheng
    ("kristinezheng","kristinezheng/kristinezheng.github.io","HTML",0,0,0,"2026-07-01T20:57:48Z",None),
    ("kristinezheng","kristinezheng/lookit-jenga","Jupyter Notebook",0,0,0,"2024-05-16T18:29:05Z","Lookit study for 9.85"),
    ("kristinezheng","kristinezheng/auditory-illusion","CSS",0,0,0,"2022-03-07T02:57:44Z","auditory illusion 9.35 spring 2022"),
    # M1shaaa
    ("M1shaaa","M1shaaa/M1shaaa",None,0,0,0,"2026-02-04T19:32:04Z","Config files for GitHub profile"),
    ("M1shaaa","M1shaaa/lab-bookshelf-","TypeScript",0,0,0,"2024-12-31T05:11:18Z",None),
]

repo_id = 0
incr_id = 0
for (source, full_name, lang, stars, forks, issues, pushed_at, desc) in REPOS:
    incr_id += 1
    trit, color_hex, color_name = gf3(incr_id)
    repo_name = full_name.split("/", 1)[1] if "/" in full_name else full_name
    con.execute("""
        INSERT INTO world_increments VALUES (?, now(), ?, ?, ?, 'github', ?, 'repo_snapshot', ?, ?, ?)
    """, [incr_id, trit, color_hex, color_name, source, repo_name, source,
          str(hash(full_name))[:16]])
    repo_id += 1
    con.execute("""
        INSERT INTO repo_snapshots VALUES (?, now(), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [repo_id, incr_id, source, repo_name, full_name,
          lang, stars, forks, issues, pushed_at, desc])

print(f"Inserted {incr_id} world_increments, {repo_id} repo_snapshots")

# Aptos snapshots - all 28 addresses
APTOS = [
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
for world, addr, bal in APTOS:
    con.execute("INSERT INTO aptos_snapshots VALUES (now(), ?, ?, ?)", [world, addr, bal])
print(f"Inserted {len(APTOS)} aptos_snapshots")

# Multisig probes
MULTISIG = [
    ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2,True),
    ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2,True),
    ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2,True),
    ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2,True),
    ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2,True),
]
for pair, addr, sigs, healthy in MULTISIG:
    con.execute("INSERT INTO multisig_probes VALUES (now(), ?, ?, ?, ?)", [pair, addr, sigs, healthy])
print(f"Inserted {len(MULTISIG)} multisig_probes")

# MNX: SPA, no data
print("MNX testnet.mnx.fi: Next.js SPA - no JSON API endpoints reachable (all paths return HTML shell)")

# Summary stats
r = con.execute("SELECT COUNT(*) FROM world_increments").fetchone()
print(f"\nDB summary: {r[0]} world_increments")
r = con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()
print(f"  {r[0]} repo_snapshots")
r = con.execute("SELECT SUM(stars) FROM repo_snapshots").fetchone()
print(f"  {r[0]} total stars")
r = con.execute("SELECT org_or_user, COUNT(*) c FROM repo_snapshots GROUP BY org_or_user ORDER BY c DESC").fetchall()
for row in r:
    print(f"  {row[0]}: {row[1]} repos")

con.close()
print("Done.")
