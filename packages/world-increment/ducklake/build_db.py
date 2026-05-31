#!/usr/bin/env python3
"""Build world-increments DuckDB from collected GitHub + Aptos data."""
import duckdb
import hashlib
import json
from datetime import datetime

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"

def gf3(n):
    t = n % 3
    if t == 0: return (0, "#d3869b", "ERGODIC")
    if t == 1: return (1, "#b8bb26", "PLUS")
    return (-1, "#cc241d", "MINUS")

def snap_hash(s):
    return hashlib.sha256(s.encode()).hexdigest()[:16]

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

# Truncate for fresh sweep
con.execute("DELETE FROM world_increments")
con.execute("DELETE FROM repo_snapshots")
con.execute("DELETE FROM aptos_snapshots")
con.execute("DELETE FROM multisig_probes")
con.execute("DELETE FROM mnx_snapshots")

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

# ── Repo data ────────────────────────────────────────────────────────────────
repos = [
  # (org_or_user, full_name, language, stars, forks, open_issues, pushed_at, description)
  # plurigrid
  ("plurigrid","plurigrid/place","TeX",1,1,10,"2026-05-21T18:28:09Z",""),
  ("plurigrid","plurigrid/eirobri","Clojure",0,0,28,"2026-05-26T07:23:35Z","EiRoBri replay world"),
  ("plurigrid","plurigrid/nash-portal","Rust",2,3,1,"2026-05-19T01:49:59Z","NASH token TUI in the browser"),
  ("plurigrid","plurigrid/gorj","Clojure",0,0,270,"2026-05-31T01:26:05Z","forj + Rama topology nREPL routing + GF(3) gay trit coloring"),
  ("plurigrid","plurigrid/zig-syrup","Zig",2,2,0,"2026-04-30T03:52:16Z","High-performance Zig OCapN Syrup"),
  ("plurigrid","plurigrid/asi","HTML",23,6,4,"2026-04-26T08:51:41Z","everything is topological chemputer!"),
  ("plurigrid","plurigrid/asi-skills","Julia",3,1,0,"2026-04-26T08:09:26Z","69 skills with Galois Hole Type accessibility"),
  ("plurigrid","plurigrid/bci-blue-share","JavaScript",0,0,0,"2026-04-26T07:08:03Z","BCI signal infrastructure"),
  ("plurigrid","plurigrid/nanoclj-zig","Zig",1,2,20,"2026-04-25T07:29:09Z","NaN-boxed Clojure interpreter in Zig"),
  ("plurigrid","plurigrid/spi-race","Swift",0,0,0,"2026-04-21T19:31:56Z","Splitmix Parallel Integrity"),
  ("plurigrid","plurigrid/reafference","HTML",0,0,0,"2026-04-16T05:21:49Z","Reafference adaptation workspace"),
  ("plurigrid","plurigrid/web-browser","Rust",0,0,0,"2026-04-10T02:54:47Z","web-browser from prepostweb lineage"),
  ("plurigrid","plurigrid/vivarium","Clojure",1,0,0,"2026-04-08T08:38:37Z",""),
  ("plurigrid","plurigrid/flowglad-rs","Rust",0,0,0,"2026-04-08T07:56:15Z",""),
  ("plurigrid","plurigrid/tree-sitter-nanoclj-zig","C",0,0,0,"2026-04-04T07:48:21Z","Tree-sitter grammar for nanoclj-zig"),
  ("plurigrid","plurigrid/forester","XSLT",0,0,0,"2026-03-30T01:32:26Z","CatColab mathematical documentation forest"),
  ("plurigrid","plurigrid/gatomic","Clojure",0,0,0,"2026-03-30T00:54:48Z","Deterministic color identity store"),
  ("plurigrid","plurigrid/gay-tofu","HTML",0,0,0,"2026-01-08T15:14:34Z","Low-discrepancy color sequences for visual TOFU"),
  ("plurigrid","plurigrid/lazygay","Go",0,0,0,"2026-01-08T14:19:25Z","lazygit fork with Gay.jl coloring"),
  ("plurigrid","plurigrid/gay-terminal","Rust",0,0,0,"2026-01-08T14:19:24Z","Terminal ANSI coloring with Gay.jl"),
  ("plurigrid","plurigrid/gay-go","Go",0,0,0,"2026-01-08T14:19:23Z","Go implementation of Gay.jl"),
  ("plurigrid","plurigrid/gay-rs","Rust",0,0,0,"2026-01-08T14:19:22Z","Rust crate for Gay.jl GF(3) trits"),
  ("plurigrid","plurigrid/lazybjj","Rust",0,0,0,"2026-01-08T14:19:19Z","TUI for jj with Gay.jl GF(3) coloring"),
  ("plurigrid","plurigrid/agent-o-rama","Clojure",0,0,0,"2026-01-02T01:09:22Z",""),
  ("plurigrid","plurigrid/aptos-wallet-ruby","Ruby",1,0,0,"2025-09-30T22:47:22Z",""),
  ("plurigrid","plurigrid/duck-kanban","Rust",1,0,0,"2025-09-26T20:18:38Z","Duck intelligence kanban"),
  ("plurigrid","plurigrid/discohy","Hy",0,0,0,"2025-09-10T02:01:31Z",""),
  ("plurigrid","plurigrid/ontology","JavaScript",8,9,16,"2025-05-27T18:18:34Z","autopoietic ergodicity and embodied gradualism"),
  ("plurigrid","plurigrid/Plurigraph","JavaScript",3,5,4,"2025-01-05T08:39:09Z","Plurigrid knowledge base for Obsidian"),
  ("plurigrid","plurigrid/act","Python",3,1,4,"2024-07-26T08:27:08Z","building blocks for cognitive category theory"),
  ("plurigrid","plurigrid/StochFlow","Python",4,1,0,"2024-03-20T23:34:57Z","stochastic interpolant models"),
  ("plurigrid","plurigrid/microworlds","Rust",3,5,3,"2023-05-13T03:54:56Z",""),
  ("plurigrid","plurigrid/agent","Python",5,1,6,"2023-03-31T18:45:23Z","Framework for agency amplification"),
  ("plurigrid","plurigrid/vcg-auction","Rust",7,2,1,"2023-03-16T21:53:08Z","VCG auction contract"),
  ("plurigrid","plurigrid/grid","TypeScript",2,1,1,"2023-01-02T11:55:55Z","Plurigrid Testnet #0"),
  ("plurigrid","plurigrid/org","Jupyter Notebook",2,0,1,"2023-11-07T01:08:05Z","Duck leveraging directed hypergraphs"),
  # kubeflow
  ("kubeflow","kubeflow/pipelines","Python",4149,2002,488,"2026-05-30T08:47:04Z","Machine Learning Pipelines for Kubeflow"),
  ("kubeflow","kubeflow/trainer","Go",2106,963,127,"2026-05-30T03:14:50Z","Distributed AI Model Training on Kubernetes"),
  ("kubeflow","kubeflow/hub","Go",175,181,36,"2026-05-29T21:13:12Z","Model Registry for ML models"),
  ("kubeflow","kubeflow/mcp-apache-spark-history-server","Python",173,61,20,"2026-05-29T19:22:55Z","MCP Server for Spark History Server"),
  ("kubeflow","kubeflow/manifests","YAML",1019,1064,23,"2026-05-29T16:51:52Z","Kubeflow AI Reference Platform Manifests"),
  ("kubeflow","kubeflow/kale","Python",691,155,46,"2026-05-29T17:04:54Z","Kubeflow superfood for Data Scientists"),
  ("kubeflow","kubeflow/mpi-operator","Go",528,235,102,"2026-05-29T15:44:06Z","Kubernetes Operator for MPI"),
  ("kubeflow","kubeflow/website","HTML",184,919,49,"2026-05-28T14:05:25Z","Kubeflow Website"),
  ("kubeflow","kubeflow/sdk","Python",118,181,135,"2026-05-28T07:53:11Z","Universal Python SDK for AI on Kubernetes"),
  ("kubeflow","kubeflow/notebooks","",73,114,195,"2026-05-29T19:48:25Z","Kubeflow Notebooks for AI/ML"),
  ("kubeflow","kubeflow/katib","Python",1685,524,123,"2026-05-29T21:30:47Z","Automated Machine Learning on Kubernetes"),
  ("kubeflow","kubeflow/kubeflow","",15693,2665,3,"2026-05-24T11:31:41Z","Machine Learning Toolkit for Kubernetes"),
  ("kubeflow","kubeflow/dashboard","TypeScript",16,56,81,"2026-05-29T18:55:47Z","Kubeflow Central Dashboard"),
  ("kubeflow","kubeflow/spark-operator","Python",3124,1488,101,"2026-05-29T18:34:23Z","Kubernetes operator for Apache Spark"),
  ("kubeflow","kubeflow/community","Jupyter Notebook",195,257,18,"2026-05-29T16:20:00Z","Kubeflow community information"),
  ("kubeflow","kubeflow/arena","Go",811,191,49,"2026-05-07T06:46:17Z","CLI for Kubeflow"),
  ("kubeflow","kubeflow/examples","Jsonnet",1463,755,111,"2025-04-14T01:54:52Z","Extended examples and tutorials"),
  # TeglonLabs
  ("TeglonLabs","TeglonLabs/mathpix-gem","Ruby",2,0,11,"2026-01-01T12:13:13Z","Transform mathematical images to LaTeX"),
  ("TeglonLabs","TeglonLabs/coin-flip-mcp","JavaScript",0,2,1,"2025-09-21T08:57:27Z","MCP server for flipping coins"),
  ("TeglonLabs","TeglonLabs/monad-mcp-server","",0,0,0,"2025-05-14T11:36:14Z","Monad MCP Server"),
  ("TeglonLabs","TeglonLabs/topoi","Python",0,0,1,"2025-01-24T04:49:26Z",""),
  # bmorphism
  ("bmorphism","bmorphism/Gay.jl","Julia",1,0,189,"2026-05-31T00:39:44Z","Wide-gamut color sampling with splittable determinism"),
  ("bmorphism","bmorphism/oxgame","OCaml",0,0,0,"2026-05-15T09:53:27Z","Stellar resolution and open-game composition for OCaml"),
  ("bmorphism","bmorphism/ocaml-mcp-sdk","OCaml",61,2,0,"2026-03-16T05:24:25Z","OCaml SDK for Model Context Protocol"),
  ("bmorphism","bmorphism/anti-bullshit-mcp-server","JavaScript",23,7,1,"2026-01-16T08:54:58Z","MCP server for analyzing claims"),
  ("bmorphism","bmorphism/vibespace-mcp-go-ternary","HTML",0,1,3,"2026-01-11T12:50:40Z","Go MCP experience with NATS and balanced ternary"),
  ("bmorphism","bmorphism/open-location-code-zig","Zig",3,0,0,"2025-12-30T19:33:45Z","Open Location Code for Zig"),
  ("bmorphism","bmorphism/monero-rental-hash-war","Haskell",1,0,0,"2025-10-05T23:08:54Z","OpenGame analysis of Monero rental hash war"),
  ("bmorphism","bmorphism/risc0-cosmwasm-example","Rust",23,2,1,"2022-10-20T23:40:00Z","CosmWasm + zkVM RISC-V EFI template"),
  ("bmorphism","bmorphism/manifold-mcp-server","JavaScript",14,9,5,"2025-01-11T10:36:58Z","MCP server for Manifold Markets"),
  ("bmorphism","bmorphism/say-mcp-server","JavaScript",20,9,3,"2025-01-07T03:15:18Z","MCP server for macOS TTS"),
  ("bmorphism","bmorphism/penrose-mcp","JavaScript",10,4,0,"2025-01-20T21:44:55Z","Penrose server for Infinity-Topos"),
  ("bmorphism","bmorphism/babashka-mcp-server","JavaScript",18,6,3,"2025-01-05T11:09:42Z","MCP server for Babashka"),
  ("bmorphism","bmorphism/hypernym-mcp-server","JavaScript",6,5,0,"2025-04-02T21:21:08Z",""),
  ("bmorphism","bmorphism/graphistry-mcp","Python",2,0,0,"2025-05-06T17:34:24Z","Graphistry MCP for graph visualization"),
  # zubyul
  ("zubyul","zubyul/voice-observatory","Python",0,0,0,"2026-04-24T05:56:17Z","Passive macOS TUI observing voice-download pathways"),
  ("zubyul","zubyul/ghostel-emacs-worlds","GLSL",0,0,0,"2026-04-24T00:20:56Z","Ghostty config + alice/bob emacs-mods"),
  ("zubyul","zubyul/nash-tui","Rust",0,0,0,"2026-04-13T07:45:16Z","NASH token TUI"),
  ("zubyul","zubyul/gay-world","Python",1,1,0,"2026-03-26T04:03:39Z","Goblin world builder with Gay.jl"),
  ("zubyul","zubyul/Gay.jl","Julia",0,0,0,"2026-03-28T11:30:01Z","Gay.jl fork — wide-gamut color sampling"),
  ("zubyul","zubyul/tilelang-kernels","Python",0,0,0,"2026-03-16T02:31:13Z","TileLang GPU kernels for SplitMix64 color generation"),
  ("zubyul","zubyul/big-bad-plurigrid-quiz","Emacs Lisp",0,0,0,"2026-04-09T18:51:31Z","27 flashcards from plurigrid activity"),
  ("zubyul","zubyul/plurigrid-site","Svelte",0,1,11,"2026-02-04T03:20:08Z","Plurigrid world: site deployment"),
  ("zubyul","zubyul/Gay.jl","Julia",0,0,0,"2026-03-28T11:30:01Z","Wide-gamut color sampling"),
  ("zubyul","zubyul/zubyul.github.io","CSS",1,0,0,"2026-01-27T03:24:34Z",""),
  # Social graph: migalkin
  ("migalkin","migalkin/NodePiece","Python",144,21,0,"2026-05-07T05:40:02Z","Compositional representations for Knowledge Graphs (ICLR22)"),
  ("migalkin","migalkin/StarE","Python",89,16,1,"2026-04-16T14:12:45Z","Message Passing for Hyper-Relational KGs (EMNLP 2020)"),
  ("migalkin","migalkin/kgcourse2021","HTML",25,9,0,"2026-02-16T05:16:08Z","Knowledge Graphs course materials"),
  ("migalkin","migalkin/NBFNet_mlx","Python",10,1,1,"2026-03-11T01:31:21Z","Neural Bellman-Ford networks in MLX"),
  ("migalkin","migalkin/RWL","Python",8,1,0,"2026-05-28T20:19:20Z","Weisfeiler and Leman Go Relational (LOG 2022)"),
  # DJedamski
  ("DJedamski","DJedamski/kaggle_ncaa18","Jupyter Notebook",0,0,0,"2018-02-26T16:33:24Z","NCAA March Madness competition 2018"),
  ("DJedamski","DJedamski/Kaggle","",1,0,0,"2023-04-21T01:42:35Z",""),
  # wasita
  ("wasita","wasita/wasita.github.io","Svelte",1,0,8,"2026-05-20T22:38:02Z","personal website"),
  ("wasita","wasita/wm-cv","Svelte",0,0,0,"2026-05-13T05:29:08Z","Academic CV as single page web app"),
  ("wasita","wasita/vocoder","JavaScript",0,0,0,"2026-05-06T05:14:03Z",""),
  ("wasita","wasita/send2kobo","TypeScript",1,0,0,"2026-05-19T02:59:26Z","Website for sending books to kobo"),
  ("wasita","wasita/magic-garden","Python",2,1,1,"2026-04-22T21:16:43Z","bot for magic garden discord game"),
  # kristinezheng
  ("kristinezheng","kristinezheng/kristinezheng.github.io","HTML",0,0,0,"2026-05-14T22:29:01Z",""),
  ("kristinezheng","kristinezheng/lookit-jenga","Jupyter Notebook",0,0,0,"2024-05-16T18:29:05Z","Lookit study for 9.85"),
  # M1shaaa
  ("M1shaaa","M1shaaa/M1shaaa","",0,0,0,"2026-02-04T19:32:04Z","GitHub profile config"),
  ("M1shaaa","M1shaaa/lab-bookshelf-","TypeScript",0,0,0,"2024-12-31T05:11:18Z",""),
  ("M1shaaa","M1shaaa/rosie-s-study-3-lookit-project","",0,0,0,"2024-11-04T22:15:39Z",""),
  # AustinCStone
  ("AustinCStone","AustinCStone/TextGAN","Python",92,30,5,"2025-03-03T13:26:32Z","GAN for text generation in TensorFlow"),
  ("AustinCStone","AustinCStone/StereoVisionMRF","Python",11,4,0,"2026-04-01T07:39:41Z","Depth from stereo images with MRF"),
  ("AustinCStone","AustinCStone/EpsteinSearch","Python",0,0,0,"2026-02-11T01:10:57Z",""),
  ("AustinCStone","AustinCStone/bmforkupdate","Python",0,0,0,"2025-05-09T04:50:16Z",""),
  ("AustinCStone","AustinCStone/bmfork","Python",0,0,1,"2025-05-09T04:18:54Z",""),
  ("AustinCStone","AustinCStone/SpectralClustering","Python",3,2,0,"2021-04-16T08:46:36Z","Spectral clustering implementation"),
]

# Insert repos into world_increments and repo_snapshots
for i, (org, full, lang, stars, forks, issues, pushed, desc) in enumerate(repos):
    inc_id = i + 1
    t = gf3(inc_id)
    repo_name = full.split("/")[1]
    h = snap_hash(full + pushed)
    con.execute("""
    INSERT INTO world_increments VALUES (?, now(), ?, ?, ?, 'github_repo', ?, 'repo_snapshot', ?, ?, ?)
    """, [inc_id, t[0], t[1], t[2], org, repo_name, org, h])
    con.execute("""
    INSERT INTO repo_snapshots VALUES (?, now(), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [i+1, inc_id, org, repo_name, full, lang, stars, forks, issues, pushed, desc])

# ── Aptos snapshots ──────────────────────────────────────────────────────────
aptos = [
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
for world, addr, bal in aptos:
    con.execute("INSERT INTO aptos_snapshots VALUES (now(), ?, ?, ?)", [world, addr, bal])

# ── Multisig probes ──────────────────────────────────────────────────────────
multisigs = [
  ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2,True),
  ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2,True),
  ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2,True),
  ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2,True),
  ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2,True),
]
for pair, addr, sigs, healthy in multisigs:
    con.execute("INSERT INTO multisig_probes VALUES (now(), ?, ?, ?, ?)", [pair, addr, sigs, healthy])

# ── Summary queries ──────────────────────────────────────────────────────────
print("=== world_increments count:", con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0])
print("=== repo_snapshots count:", con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0])
print("=== GF3 distribution:")
for row in con.execute("SELECT gf3_name, gf3_color, COUNT(*) FROM world_increments GROUP BY 1,2").fetchall():
    print(f"  {row}")
print("=== Top orgs by repo count:")
for row in con.execute("SELECT org_or_user, COUNT(*) as n FROM repo_snapshots GROUP BY 1 ORDER BY 2 DESC").fetchall():
    print(f"  {row}")
print("=== aptos_snapshots count:", con.execute("SELECT COUNT(*) FROM aptos_snapshots").fetchone()[0])
print("=== multisig_probes:")
for row in con.execute("SELECT pair, sigs_required, healthy FROM multisig_probes").fetchall():
    print(f"  {row}")

con.close()
print("DB built successfully at", DB_PATH)
