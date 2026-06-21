#!/usr/bin/env python3
"""Build world-increments DuckDB from sweep data."""

import duckdb
import hashlib
import json
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

# GF(3) helpers
def gf3(n):
    t = n % 3
    if t == 0: return (0, "#d3869b", "ERGODIC")
    if t == 1: return (1, "#b8bb26", "PLUS")
    return (-1, "#cc241d", "MINUS")

def snap_hash(s):
    return hashlib.md5(s.encode()).hexdigest()[:12]

# --- REPO DATA ---
# format: (source_type, org_or_user, full_name, language, stars, forks, open_issues, pushed_at, description)
repos = []

# plurigrid (100 repos)
plurigrid_repos = [
    ("plurigrid","plurigrid/asi","HTML",26,8,4,"2026-06-10T12:51:42Z","everything is topological chemputer!"),
    ("plurigrid","plurigrid/place","TeX",1,1,9,"2026-06-20T00:28:26Z",""),
    ("plurigrid","plurigrid/eirobri","Clojure",0,0,29,"2026-06-03T20:43:46Z","EiRoBri replay world"),
    ("plurigrid","plurigrid/nash-portal","Rust",2,3,1,"2026-05-19T01:49:59Z","NASH token TUI in the browser"),
    ("plurigrid","plurigrid/gorj","Clojure",0,0,714,"2026-06-21T07:15:51Z","forj + Rama topology nREPL routing + GF(3) gay trit coloring"),
    ("plurigrid","plurigrid/zig-syrup","Zig",2,2,0,"2026-04-30T03:52:16Z","High-performance Zig OCapN Syrup implementation"),
    ("plurigrid","plurigrid/asi-skills","Julia",3,0,0,"2026-04-26T08:09:26Z","69 skills with Galois Hole Type accessibility"),
    ("plurigrid","plurigrid/bci-blue-share","JavaScript",0,0,0,"2026-04-26T07:08:03Z","BCI signal infrastructure"),
    ("plurigrid","plurigrid/nanoclj-zig","Zig",1,1,20,"2026-04-25T07:29:09Z","NaN-boxed Clojure interpreter in Zig 0.15"),
    ("plurigrid","plurigrid/spi-race","Swift",0,0,0,"2026-04-21T19:31:56Z","Splitmix Parallel Integrity"),
    ("plurigrid","plurigrid/reafference","HTML",0,0,0,"2026-04-16T05:21:49Z","Reafference adaptation workspace"),
    ("plurigrid","plurigrid/web-browser","Rust",0,0,0,"2026-04-10T02:54:47Z","web-browser from prepostweb lineage"),
    ("plurigrid","plurigrid/vivarium","Clojure",1,0,0,"2026-04-08T08:38:37Z",""),
    ("plurigrid","plurigrid/flowglad-rs","Rust",0,0,0,"2026-04-08T07:56:15Z",""),
    ("plurigrid","plurigrid/tree-sitter-nanoclj-zig","C",0,0,0,"2026-04-04T07:48:21Z","Tree-sitter grammar for nanoclj-zig"),
    ("plurigrid","plurigrid/forester","XSLT",0,0,0,"2026-03-30T01:32:26Z","CatColab mathematical documentation forest"),
    ("plurigrid","plurigrid/gatomic","Clojure",0,0,0,"2026-03-30T00:54:48Z","Deterministic color identity store with sonification"),
    ("plurigrid","plurigrid/blue","TeX",0,0,0,"2026-03-29T23:06:32Z",""),
    ("plurigrid","plurigrid/red","",0,0,0,"2026-03-29T22:58:46Z",""),
    ("plurigrid","plurigrid/nblm-flashcards","Hy",0,0,0,"2026-03-26T08:23:01Z","NotebookLM Enterprise flashcard pipeline"),
    ("plurigrid","plurigrid/gemini-agent","Python",0,0,0,"2026-02-19T06:39:16Z",""),
    ("plurigrid","plurigrid/graded-optic","Haskell",0,0,0,"2026-02-08T16:10:16Z","Semiring-graded bidirectional processes"),
    ("plurigrid","plurigrid/json-canvas","",0,0,0,"2026-02-06T06:50:57Z","JSON Canvas: Real-time interaction data capture"),
    ("plurigrid","plurigrid/shepherd","Scheme",0,0,0,"2026-01-23T07:47:28Z","Spritely Shepherd mirror"),
    ("plurigrid","plurigrid/goblinshare","Scheme",0,0,0,"2026-01-23T07:47:12Z","P2P filesharing demo for Goblins"),
    ("plurigrid","plurigrid/magenc","Scheme",0,0,0,"2026-01-23T07:47:11Z","Magenc Magnet URIs"),
    ("plurigrid","plurigrid/hoot","Scheme",0,0,1,"2026-01-23T07:47:10Z","Spritely Hoot Scheme to WebAssembly compiler"),
    ("plurigrid","plurigrid/leprechauns","Racket",0,0,0,"2026-01-23T07:46:46Z","Spritely Goblins + Gay.jl semantic colors"),
    ("plurigrid","plurigrid/spritely-semantic-colors","",0,0,0,"2026-01-23T07:38:32Z","Deterministic color mappings for Spritely/Goblins objects"),
    ("plurigrid","plurigrid/gay-tofu","HTML",0,0,0,"2026-01-08T15:14:34Z","Low-discrepancy color sequences for visual TOFU authentication"),
    ("plurigrid","plurigrid/lazygay","Go",0,0,0,"2026-01-08T14:19:25Z","lazygit fork with Gay.jl deterministic commit coloring"),
    ("plurigrid","plurigrid/gay-terminal","Rust",0,0,0,"2026-01-08T14:19:24Z","Terminal ANSI coloring with Gay.jl"),
    ("plurigrid","plurigrid/gay-go","Go",0,0,0,"2026-01-08T14:19:23Z","Go implementation of Gay.jl"),
    ("plurigrid","plurigrid/gay-rs","Rust",0,0,0,"2026-01-08T14:19:22Z","Rust crate for Gay.jl with GF(3) trits"),
    ("plurigrid","plurigrid/lazybjj","Rust",0,0,0,"2026-01-08T14:19:19Z","TUI for jj with Gay.jl GF(3) coloring"),
    ("plurigrid","plurigrid/agent-o-rama","Clojure",0,0,0,"2026-01-02T01:09:22Z",""),
    ("plurigrid","plurigrid/aptos-wallet-ruby","Ruby",1,0,0,"2025-09-30T22:47:22Z",""),
    ("plurigrid","plurigrid/duck-kanban","Rust",1,0,0,"2025-09-26T20:18:38Z","Duck intelligence kanban system"),
    ("plurigrid","plurigrid/ontology","JavaScript",8,9,16,"2025-05-27T18:18:34Z","autopoietic ergodicity and embodied gradualism"),
    ("plurigrid","plurigrid/Plurigraph","JavaScript",3,5,4,"2025-01-05T08:39:09Z","Plurigrid knowledge base for Obsidian.md"),
    ("plurigrid","plurigrid/act","Python",3,1,4,"2024-07-26T08:27:08Z","building blocks for cognitive category theory"),
    ("plurigrid","plurigrid/StochFlow","Python",4,1,0,"2024-03-20T23:34:57Z","stochastic interpolant models"),
    ("plurigrid","plurigrid/microworlds","Rust",3,5,3,"2023-05-13T03:54:56Z",""),
    ("plurigrid","plurigrid/agent","Python",5,1,6,"2023-03-31T18:45:23Z","Framework for agency amplification"),
    ("plurigrid","plurigrid/vcg-auction","Rust",7,2,1,"2023-03-16T21:53:08Z","VCG auction contract"),
    ("plurigrid","plurigrid/VPP","Julia",0,1,0,"2023-01-11T18:41:07Z","Hyperreal Power Plant"),
    ("plurigrid","plurigrid/grid","TypeScript",2,1,1,"2023-01-02T11:55:55Z","Plurigrid Testnet #0: Edith Clarke"),
]

# TeglonLabs (5 repos)
teglon_repos = [
    ("TeglonLabs","TeglonLabs/jank-crane","C++",0,0,0,"2026-06-08T19:03:03Z","crane-jank converged-IR hub GF3 convergence maps"),
    ("TeglonLabs","TeglonLabs/mathpix-gem","Ruby",2,0,11,"2026-01-01T12:13:13Z","Transform mathematical images to LaTeX"),
    ("TeglonLabs","TeglonLabs/coin-flip-mcp","JavaScript",0,2,1,"2025-09-21T08:57:27Z","MCP server for flipping coins"),
    ("TeglonLabs","TeglonLabs/monad-mcp-server","",0,0,0,"2025-05-14T11:36:14Z","Monad MCP Server"),
    ("TeglonLabs","TeglonLabs/topoi","Python",0,0,1,"2025-01-24T04:49:26Z",""),
]

# kubeflow (top repos)
kubeflow_repos = [
    ("kubeflow","kubeflow/kubeflow","",15738,2680,0,"2026-06-18T11:45:16Z","Machine Learning Toolkit for Kubernetes"),
    ("kubeflow","kubeflow/pipelines","Python",4155,2009,449,"2026-06-20T19:12:02Z","Machine Learning Pipelines for Kubeflow"),
    ("kubeflow","kubeflow/spark-operator","Python",3127,1490,102,"2026-06-18T15:39:22Z","Kubernetes operator for Apache Spark"),
    ("kubeflow","kubeflow/trainer","Go",2118,970,118,"2026-06-19T15:46:05Z","Distributed AI Model Training on Kubernetes"),
    ("kubeflow","kubeflow/community-distribution","YAML",1025,1065,20,"2026-06-18T19:10:25Z","Kubeflow Community Distribution"),
    ("kubeflow","kubeflow/examples","Jsonnet",1460,756,111,"2025-04-14T01:54:52Z","Extended examples and tutorials"),
    ("kubeflow","kubeflow/katib","Python",1683,528,116,"2026-06-20T23:29:45Z","Automated Machine Learning on Kubernetes"),
    ("kubeflow","kubeflow/arena","Go",813,190,43,"2026-05-07T06:46:17Z","A CLI for Kubeflow"),
    ("kubeflow","kubeflow/kale","Python",694,155,55,"2026-06-20T11:20:36Z","Kubeflow superfood for Data Scientists"),
    ("kubeflow","kubeflow/mpi-operator","Go",528,236,106,"2026-06-15T13:03:34Z","Kubernetes Operator for MPI-based applications"),
    ("kubeflow","kubeflow/mcp-apache-spark-history-server","Python",177,65,21,"2026-06-19T21:20:08Z","MCP Server for Apache Spark History Server"),
    ("kubeflow","kubeflow/community","Jupyter Notebook",194,264,15,"2026-06-19T16:50:40Z","Kubeflow community information"),
    ("kubeflow","kubeflow/website","HTML",184,923,40,"2026-06-19T15:39:26Z","Kubeflow Website"),
    ("kubeflow","kubeflow/hub","Go",173,183,39,"2026-06-20T15:40:26Z","Model Registry for ML models"),
    ("kubeflow","kubeflow/sdk","Python",120,180,133,"2026-06-20T03:05:26Z","Universal Python SDK for AI on Kubernetes"),
    ("kubeflow","kubeflow/dashboard","TypeScript",16,59,80,"2026-06-21T00:56:24Z","Kubeflow Central Dashboard"),
    ("kubeflow","kubeflow/mcp-server","Python",16,22,25,"2026-05-12T10:14:24Z","MCP Server for Kubeflow Tools"),
]

# bmorphism (top repos)
bmorphism_repos = [
    ("bmorphism","bmorphism/Gay.jl","Julia",2,1,187,"2026-06-21T00:43:51Z","Wide-gamut color sampling with splittable determinism"),
    ("bmorphism","bmorphism/ocaml-mcp-sdk","OCaml",61,2,0,"2026-03-16T05:24:25Z","OCaml SDK for Model Context Protocol"),
    ("bmorphism","bmorphism/anti-bullshit-mcp-server","JavaScript",23,7,1,"2026-01-16T08:54:58Z","MCP server for claim analysis"),
    ("bmorphism","bmorphism/risc0-cosmwasm-example","Rust",23,2,1,"2022-10-20T23:50:40Z","CosmWasm + zkVM RISC-V EFI template"),
    ("bmorphism","bmorphism/say-mcp-server","JavaScript",20,9,3,"2025-01-07T03:15:18Z","MCP server for macOS text-to-speech"),
    ("bmorphism","bmorphism/babashka-mcp-server","JavaScript",19,6,3,"2025-01-05T11:09:42Z","MCP server for Babashka"),
    ("bmorphism","bmorphism/manifold-mcp-server","JavaScript",14,9,5,"2025-01-11T10:36:58Z","MCP server for Manifold Markets"),
    ("bmorphism","bmorphism/penrose-mcp","JavaScript",10,4,0,"2025-01-20T21:44:55Z","Penrose server for Infinity-Topos"),
    ("bmorphism","bmorphism/marginalia-mcp-server","JavaScript",8,6,0,"2025-01-06T05:47:24Z","MCP server for annotations"),
    ("bmorphism","bmorphism/hypernym-mcp-server","JavaScript",6,5,0,"2025-04-02T21:21:08Z",""),
    ("bmorphism","bmorphism/nats-mcp-server","",7,3,2,"2025-01-06T23:33:41Z","MCP server for NATS messaging"),
    ("bmorphism","bmorphism/shitcoin","Python",5,0,0,"2026-04-08T08:07:08Z","IBC cw20 asset denom getter"),
    ("bmorphism","bmorphism/satreadout","HTML",0,0,0,"2026-06-20T13:05:41Z","Machine-checked saturating non-Riemannian perceptual readout"),
    ("bmorphism","bmorphism/world","Python",0,0,0,"2026-06-02T06:49:02Z","Local worlds launcher"),
    ("bmorphism","bmorphism/oxgame","OCaml",0,0,0,"2026-05-15T09:53:27Z","Stellar resolution and open-game composition"),
    ("bmorphism","bmorphism/graphistry-mcp","Python",2,0,0,"2025-05-06T17:34:24Z","Graphistry MCP integration for graph visualization"),
    ("bmorphism","bmorphism/monero-rental-hash-war","Haskell",1,0,0,"2025-10-05T23:08:54Z","OpenGame analysis of Monero rental hash war"),
]

# zubyul (top repos)
zubyul_repos = [
    ("zubyul","zubyul/voice-observatory","Python",0,0,0,"2026-04-24T05:56:17Z","Passive macOS TUI observing voice-download pathways"),
    ("zubyul","zubyul/ghostel-emacs-worlds","GLSL",0,0,0,"2026-04-24T00:20:56Z","Ghostty config and emacs-mods"),
    ("zubyul","zubyul/nash-tui","Rust",0,0,0,"2026-04-13T07:45:16Z","NASH token TUI real-time candles"),
    ("zubyul","zubyul/gay-world","Python",1,1,0,"2026-03-26T04:03:39Z","Goblin world builder with MLX task decomposition"),
    ("zubyul","zubyul/Gay.jl","Julia",0,0,0,"2026-03-28T11:30:01Z","Wide-gamut color sampling fork"),
    ("zubyul","zubyul/tilelang-kernels","Python",0,0,0,"2026-03-16T02:31:13Z","TileLang GPU kernels for GF(3) trit classification"),
    ("zubyul","zubyul/plurigrid-site","Svelte",0,1,11,"2026-02-04T03:20:08Z","Plurigrid world site deployment"),
    ("zubyul","zubyul/jonikas_lab_data_analysis_misc","Jupyter Notebook",2,0,0,"2023-08-16T20:24:40Z","genetic sequence data processing"),
    ("zubyul","zubyul/WGCNA","HTML",2,0,0,"2023-07-05T18:02:30Z","weighted gene correlation network analysis"),
]

# migalkin
migalkin_repos = [
    ("migalkin","migalkin/NodePiece","Python",144,21,0,"2026-05-07T05:40:02Z","Compositional KG Representations (ICLR22)"),
    ("migalkin","migalkin/StarE","Python",89,16,1,"2026-04-16T14:12:45Z","EMNLP 2020: Message Passing for Hyper-Relational KGs"),
    ("migalkin","migalkin/kgcourse2021","HTML",25,9,0,"2026-02-16T05:16:08Z","Knowledge Graphs course materials"),
    ("migalkin","migalkin/NBFNet_mlx","Python",10,1,1,"2026-03-11T01:31:21Z","Neural Bellman-Ford networks in MLX"),
    ("migalkin","migalkin/RWL","Python",8,1,0,"2026-05-28T20:19:20Z","Weisfeiler and Leman Go Relational (LOG 2022)"),
    ("migalkin","migalkin/rambo","Rust",3,0,1,"2023-02-28T16:37:22Z",""),
]

# wasita
wasita_repos = [
    ("wasita","wasita/wasita.github.io","Svelte",1,0,8,"2026-06-15T20:14:23Z","personal website"),
    ("wasita","wasita/magic-garden","Python",2,1,1,"2026-04-22T21:16:43Z","Bot for magic garden discord game"),
    ("wasita","wasita/send2kobo","TypeScript",1,0,0,"2026-05-19T02:59:26Z","Website for sending books to kobo e-reader"),
    ("wasita","wasita/proj-template","",0,0,0,"2026-06-19T21:22:21Z",""),
]

# AustinCStone (top)
austin_repos = [
    ("AustinCStone","AustinCStone/TextGAN","Python",92,30,5,"2025-03-03T13:26:32Z","GAN for text generation in TensorFlow"),
    ("AustinCStone","AustinCStone/StereoVisionMRF","Python",11,4,0,"2026-04-01T07:39:41Z","MRF with loopy belief propagation for stereo depth"),
    ("AustinCStone","AustinCStone/SpectralClustering","Python",3,2,0,"2021-04-16T08:46:36Z","Spectral clustering implementation"),
    ("AustinCStone","AustinCStone/StructureFromMotion","Python",1,0,0,"2019-04-26T19:43:12Z","3D geometry recovery from videos"),
]

# DJedamski
djedamski_repos = [
    ("DJedamski","DJedamski/kaggle_ncaa18","Jupyter Notebook",0,0,0,"2018-02-26T16:33:24Z","NCAA March Madness competition code"),
    ("DJedamski","DJedamski/Kaggle","",1,0,0,"2023-04-21T01:42:35Z",""),
    ("DJedamski","DJedamski/Getting-and-Cleaning-Data","R",1,0,0,"2023-04-21T01:42:34Z","Coursera Project"),
    ("DJedamski","DJedamski/School","R",1,1,0,"2023-04-21T01:42:33Z","Small projects from grad school"),
]

# kristinezheng
kristine_repos = [
    ("kristinezheng","kristinezheng/kristinezheng.github.io","HTML",0,0,0,"2026-06-07T22:53:10Z",""),
    ("kristinezheng","kristinezheng/lookit-jenga","Jupyter Notebook",0,0,0,"2024-05-16T18:29:05Z","Lookit study for 9.85"),
]

# M1shaaa
m1shaa_repos = [
    ("M1shaaa","M1shaaa/M1shaaa","",0,0,0,"2026-02-04T19:32:04Z","GitHub profile config"),
    ("M1shaaa","M1shaaa/lab-bookshelf-","TypeScript",0,0,0,"2024-12-31T05:11:18Z",""),
    ("M1shaaa","M1shaaa/Python-Lookit-Uploads","Python",0,0,0,"2024-02-15T22:59:37Z","random projects"),
]

all_sources = [
    ("org", "plurigrid", plurigrid_repos),
    ("org", "TeglonLabs", teglon_repos),
    ("org", "kubeflow", kubeflow_repos),
    ("user", "bmorphism", bmorphism_repos),
    ("user", "zubyul", zubyul_repos),
    ("user", "migalkin", migalkin_repos),
    ("user", "wasita", wasita_repos),
    ("user", "AustinCStone", austin_repos),
    ("user", "DJedamski", djedamski_repos),
    ("user", "kristinezheng", kristine_repos),
    ("user", "M1shaaa", m1shaa_repos),
]

incr_id = 1
repo_id = 1
ts = "2026-06-21 07:30:00"

for src_type, src_name, repo_list in all_sources:
    trit, color, gf3_name = gf3(incr_id)
    h = snap_hash(f"{src_name}:{ts}")
    con.execute("""
        INSERT INTO world_increments VALUES (?,?,?,?,?,?,?,?,?,?,?)
    """, [incr_id, ts, trit, color, gf3_name, src_type, src_name, "repo_snapshot", None, src_name, h])

    for r in repo_list:
        org_or_user, full_name, lang, stars, forks, issues, pushed, desc = r
        con.execute("""
            INSERT INTO repo_snapshots VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
        """, [repo_id, ts, incr_id, org_or_user, full_name.split("/")[1], full_name,
              lang or None, stars, forks, issues, pushed, desc or None])
        repo_id += 1

    incr_id += 1

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
    con.execute("INSERT INTO aptos_snapshots VALUES (?,?,?,?)", [ts, world, addr, bal])

# Multisig probes
multisig_data = [
    ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2,True),
    ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2,True),
    ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2,True),
    ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2,True),
    ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2,True),
]

for pair, addr, sigs, healthy in multisig_data:
    con.execute("INSERT INTO multisig_probes VALUES (?,?,?,?,?)", [ts, pair, addr, sigs, healthy])

# Verify counts
print("world_increments:", con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0])
print("repo_snapshots:", con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0])
print("aptos_snapshots:", con.execute("SELECT COUNT(*) FROM aptos_snapshots").fetchone()[0])
print("multisig_probes:", con.execute("SELECT COUNT(*) FROM multisig_probes").fetchone()[0])

# GF3 color chain summary
print("\nGF3 color chain:")
for row in con.execute("SELECT id, gf3_trit, gf3_color, gf3_name, source_name FROM world_increments ORDER BY id").fetchall():
    print(f"  [{row[0]}] trit={row[1]} {row[2]} ({row[3]}) → {row[4]}")

con.close()
print("\nDone.")
