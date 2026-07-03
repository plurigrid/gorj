#!/usr/bin/env python3
"""Build world-increments DuckDB from sweep data."""
import duckdb
import hashlib
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "world-increments.duckdb")
con = duckdb.connect(DB_PATH)

# ── Schema ──────────────────────────────────────────────────────────────────
con.execute("""
CREATE TABLE IF NOT EXISTS world_increments (
  id INTEGER,
  timestamp TIMESTAMP DEFAULT now(),
  gf3_trit INTEGER,
  gf3_color VARCHAR,
  gf3_name VARCHAR,
  source_type VARCHAR,
  source_name VARCHAR,
  event_type VARCHAR,
  repo_name VARCHAR,
  actor VARCHAR,
  snapshot_hash VARCHAR
)""")

con.execute("""
CREATE TABLE IF NOT EXISTS repo_snapshots (
  id INTEGER,
  timestamp TIMESTAMP DEFAULT now(),
  increment_id INTEGER,
  org_or_user VARCHAR,
  repo_name VARCHAR,
  full_name VARCHAR,
  language VARCHAR,
  stars INTEGER,
  forks INTEGER,
  open_issues INTEGER,
  pushed_at VARCHAR,
  description VARCHAR
)""")

con.execute("""
CREATE TABLE IF NOT EXISTS aptos_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  world VARCHAR,
  address VARCHAR,
  balance_apt DOUBLE
)""")

con.execute("""
CREATE TABLE IF NOT EXISTS multisig_probes (
  timestamp TIMESTAMP DEFAULT now(),
  pair VARCHAR,
  address VARCHAR,
  sigs_required INTEGER,
  healthy BOOLEAN
)""")

con.execute("""
CREATE TABLE IF NOT EXISTS mnx_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  ticker VARCHAR,
  name VARCHAR,
  category VARCHAR,
  price DOUBLE,
  change_pct DOUBLE
)""")

try:
    con.execute("CREATE SEQUENCE IF NOT EXISTS increment_seq START 1")
    con.execute("CREATE SEQUENCE IF NOT EXISTS repo_seq START 1")
except Exception:
    pass

# GF(3) color chain
GF3 = [
    (0, "#d3869b", "ERGODIC"),
    (1, "#b8bb26", "PLUS"),
    (-1, "#cc241d", "MINUS"),
]

def gf3(id_: int):
    return GF3[id_ % 3]

# ── Repo data ─────────────────────────────────────────────────────────────
repos = []

# --- plurigrid (100 of 103) ---
plurigrid_repos = [
    ("plurigrid","plurigrid/asi","HTML",28,8,4,"2026-06-29T03:15:56Z","everything is topological chemputer!"),
    ("plurigrid","plurigrid/ontology","JavaScript",8,9,16,"2025-05-27T18:18:34Z","autopoietic ergodicity and embodied gradualism"),
    ("plurigrid","plurigrid/vcg-auction","Rust",7,2,1,"2023-03-16T21:53:08Z","a simple contract that performs a VCG auction"),
    ("plurigrid","plurigrid/agent","Python",5,1,6,"2023-03-31T18:45:23Z","Framework for agency amplification"),
    ("plurigrid","plurigrid/StochFlow","Python",4,1,0,"2024-03-20T23:34:57Z","stochastic interpolant models"),
    ("plurigrid","plurigrid/Plurigraph","JavaScript",3,5,4,"2025-01-05T08:39:09Z","Plurigrid knowledge base for Obsidian"),
    ("plurigrid","plurigrid/asi-skills","Julia",3,0,0,"2026-04-26T08:09:26Z","69 skills with Galois Hole Type accessibility"),
    ("plurigrid","plurigrid/microworlds","Rust",3,5,3,"2023-05-13T03:54:56Z",""),
    ("plurigrid","plurigrid/act","Python",3,1,4,"2024-07-26T08:27:08Z","building blocks for cognitive category theory"),
    ("plurigrid","plurigrid/org","Jupyter Notebook",2,0,1,"2023-11-07T01:08:05Z","Dynamically Replicating Duck"),
    ("plurigrid","plurigrid/zig-syrup","Zig",2,2,0,"2026-04-30T03:52:16Z","High-performance Zig OCapN Syrup"),
    ("plurigrid","plurigrid/nash-portal","Rust",2,3,1,"2026-05-19T01:49:59Z","NASH token TUI"),
    ("plurigrid","plurigrid/grid","TypeScript",2,1,1,"2023-01-02T11:55:55Z","Plurigrid Testnet #0"),
    ("plurigrid","plurigrid/nanoclj-zig","Zig",1,1,20,"2026-04-25T07:29:09Z","NaN-boxed Clojure interpreter in Zig"),
    ("plurigrid","plurigrid/place","TeX",1,1,12,"2026-06-29T20:40:59Z",""),
    ("plurigrid","plurigrid/eirobri","Clojure",0,0,30,"2026-06-30T02:23:56Z","EiRoBri replay world"),
    ("plurigrid","plurigrid/gorj","Clojure",0,0,937,"2026-07-03T09:13:18Z","forj + Rama topology nREPL routing + GF(3) gay trit coloring"),
    ("plurigrid","plurigrid/shrimp","",0,0,0,"2026-07-03T01:24:20Z","Jank worked example: shrimp"),
    ("plurigrid","plurigrid/nanoclj-zig","Zig",1,1,20,"2026-04-25T07:29:09Z","NaN-boxed Clojure interpreter in Zig 0.15"),
    ("plurigrid","plurigrid/json-canvas","",0,0,0,"2026-02-06T06:50:57Z","JSON Canvas: Real-time interaction data capture"),
    ("plurigrid","plurigrid/graded-optic","Haskell",0,0,0,"2026-02-08T16:10:16Z","Semiring-graded bidirectional processes"),
    ("plurigrid","plurigrid/shepherd","Scheme",0,0,0,"2026-01-23T07:47:28Z","Spritely Shepherd"),
    ("plurigrid","plurigrid/hoot","Scheme",0,0,1,"2026-01-23T07:47:10Z","Spritely Hoot Scheme to WASM"),
    ("plurigrid","plurigrid/web-browser","Rust",0,0,0,"2026-04-10T02:54:47Z","web-browser from prepostweb lineage"),
    ("plurigrid","plurigrid/spi-race","Swift",0,0,0,"2026-04-21T19:31:56Z","Splitmix Parallel Integrity"),
    ("plurigrid","plurigrid/nblm-flashcards","Hy",0,0,0,"2026-03-26T08:23:01Z","NotebookLM Enterprise flashcard pipeline"),
    ("plurigrid","plurigrid/tree-sitter-nanoclj-zig","C",0,0,0,"2026-04-04T07:48:21Z","Tree-sitter grammar for nanoclj-zig"),
    ("plurigrid","plurigrid/bci-blue-share","JavaScript",0,0,0,"2026-04-26T07:08:03Z","BCI signal infrastructure"),
    ("plurigrid","plurigrid/reafference","HTML",0,0,0,"2026-04-16T05:21:49Z","Reafference adaptation workspace"),
    ("plurigrid","plurigrid/vivarium","Clojure",1,0,0,"2026-04-08T08:38:37Z",""),
    ("plurigrid","plurigrid/flowglad-rs","Rust",0,0,0,"2026-04-08T07:56:15Z",""),
    ("plurigrid","plurigrid/gatomic","Clojure",0,0,0,"2026-03-30T00:54:48Z","Deterministic color identity store"),
    ("plurigrid","plurigrid/agent-o-rama","Clojure",0,0,0,"2026-01-02T01:09:22Z",""),
    ("plurigrid","plurigrid/gay-world","",0,0,0,"",""),
    ("plurigrid","plurigrid/lazybjj","Rust",0,0,0,"2026-01-08T14:19:19Z","TUI for jj with Gay.jl GF(3) coloring"),
    ("plurigrid","plurigrid/gay-go","Go",0,0,0,"2026-01-08T14:19:23Z","Go implementation of Gay.jl"),
    ("plurigrid","plurigrid/gay-rs","Rust",0,0,0,"2026-01-08T14:19:22Z","Rust crate for Gay.jl"),
    ("plurigrid","plurigrid/gay-terminal","Rust",0,0,0,"2026-01-08T14:19:24Z","Terminal ANSI coloring with Gay.jl"),
    ("plurigrid","plurigrid/lazygay","Go",0,0,0,"2026-01-08T14:19:25Z","lazygit fork with Gay.jl"),
    ("plurigrid","plurigrid/spritely-semantic-colors","",0,0,0,"2026-01-23T07:38:32Z","Deterministic color mappings for Spritely"),
    ("plurigrid","plurigrid/gay-tofu","HTML",0,0,0,"2026-01-08T15:14:34Z","Low-discrepancy color sequences for TOFU"),
    ("plurigrid","plurigrid/forester","XSLT",0,0,0,"2026-03-30T01:32:26Z","CatColab mathematical documentation forest"),
    ("plurigrid","plurigrid/blue","TeX",0,0,0,"2026-03-29T23:06:32Z",""),
    ("plurigrid","plurigrid/gemini-agent","Python",0,0,0,"2026-02-19T06:39:16Z",""),
    ("plurigrid","plurigrid/DiffusionVoiceDemo","Clojure",0,0,0,"2024-04-02T18:09:01Z",""),
    ("plurigrid","plurigrid/plurigrid.xyz","TypeScript",0,0,1,"2022-08-31T05:26:14Z",""),
    ("plurigrid","plurigrid/commons-contracts","Rust",0,0,0,"2022-09-09T09:20:11Z","CosmWasm contracts"),
    ("plurigrid","plurigrid/VPP","Julia",0,1,0,"2023-01-11T18:41:07Z","Hyperreal Power Plant"),
    ("plurigrid","plurigrid/duck-kanban","Rust",1,0,0,"2025-09-26T20:18:38Z","Duck intelligence kanban"),
    ("plurigrid","plurigrid/aptos-wallet-ruby","Ruby",1,0,0,"2025-09-30T22:47:22Z",""),
    ("plurigrid","plurigrid/discohy","Hy",0,0,0,"2025-09-10T02:01:31Z",""),
]

# --- kubeflow (48) ---
kubeflow_repos = [
    ("kubeflow","kubeflow/kubeflow","",15760,2682,0,"2026-06-18T11:45:16Z","Machine Learning Toolkit for Kubernetes"),
    ("kubeflow","kubeflow/pipelines","Python",4167,2021,412,"2026-07-03T09:34:28Z","Machine Learning Pipelines for Kubeflow"),
    ("kubeflow","kubeflow/spark-operator","Python",3132,1496,103,"2026-07-02T08:52:01Z","Kubernetes operator for Apache Spark"),
    ("kubeflow","kubeflow/trainer","Go",2129,975,145,"2026-07-02T15:21:32Z","Distributed AI Model Training on Kubernetes"),
    ("kubeflow","kubeflow/katib","Python",1688,529,114,"2026-07-01T21:20:57Z","Automated Machine Learning on Kubernetes"),
    ("kubeflow","kubeflow/examples","Jsonnet",1460,756,111,"2025-04-14T01:54:52Z","Extended examples and tutorials"),
    ("kubeflow","kubeflow/community-distribution","YAML",1028,1067,24,"2026-07-03T09:20:06Z","Kubeflow Community Distribution"),
    ("kubeflow","kubeflow/arena","Go",814,194,44,"2026-07-03T01:57:25Z","A CLI for Kubeflow"),
    ("kubeflow","kubeflow/kale","Python",694,156,38,"2026-07-01T12:44:49Z","Kubeflow's superfood for Data Scientists"),
    ("kubeflow","kubeflow/mpi-operator","Go",529,237,102,"2026-07-02T17:21:40Z","Kubernetes Operator for MPI-based applications"),
    ("kubeflow","kubeflow/fairing","Jsonnet",337,143,134,"2022-04-11T05:28:47Z","Python SDK for building, training, deploying ML"),
    ("kubeflow","kubeflow/pytorch-operator","Jsonnet",310,143,63,"2021-12-01T17:44:48Z","PyTorch on Kubernetes"),
    ("kubeflow","kubeflow/community","Jupyter Notebook",194,265,15,"2026-07-01T21:20:20Z","Kubeflow community info"),
    ("kubeflow","kubeflow/website","HTML",184,923,29,"2026-07-02T16:52:48Z","Kubeflow Website"),
    ("kubeflow","kubeflow/kfp-tekton","TypeScript",183,123,79,"2024-11-19T12:23:51Z","Kubeflow Pipelines on Tekton"),
    ("kubeflow","kubeflow/kfctl","Go",182,134,94,"2023-08-15T20:19:22Z","CLI for deploying and managing Kubeflow"),
    ("kubeflow","kubeflow/mcp-apache-spark-history-server","Python",179,66,19,"2026-06-25T20:28:43Z","MCP Server for Apache Spark History Server"),
    ("kubeflow","kubeflow/hub","Go",174,184,35,"2026-07-02T17:16:53Z","Model Registry for ML models"),
    ("kubeflow","kubeflow/sdk","Python",123,188,140,"2026-07-02T19:23:35Z","Universal Python SDK for AI on Kubernetes"),
    ("kubeflow","kubeflow/notebooks","",73,125,180,"2026-07-02T17:54:18Z","Kubeflow Notebooks"),
    ("kubeflow","kubeflow/mcp-server","Python",19,25,32,"2026-06-29T14:46:23Z","MCP Server for Kubeflow Tools"),
    ("kubeflow","kubeflow/dashboard","TypeScript",16,59,86,"2026-07-03T08:11:17Z","Kubeflow Central Dashboard"),
    ("kubeflow","kubeflow/pipelines-components","Python",11,47,36,"2026-07-02T16:09:54Z","Kubeflow Pipelines components"),
    ("kubeflow","kubeflow/docs-agent","Python",39,95,152,"2026-06-25T05:33:14Z","Kubeflow Documentation AI Agent"),
    ("kubeflow","kubeflow/mlflow-integration","Python",6,5,5,"2026-07-01T19:01:56Z",""),
    ("kubeflow","kubeflow/internal-acls","Go",19,390,2,"2026-07-02T03:35:54Z","Group ACLs for Kubeflow developers"),
]

# --- TeglonLabs (5) ---
teglon_repos = [
    ("TeglonLabs","TeglonLabs/mathpix-gem","Ruby",2,0,11,"2026-01-01T12:13:13Z","Transform mathematical images to LaTeX"),
    ("TeglonLabs","TeglonLabs/topoi","Python",0,0,1,"2025-01-24T04:49:26Z",""),
    ("TeglonLabs","TeglonLabs/jank-crane","C++",0,0,0,"2026-06-08T19:03:03Z","crane-jank converged-IR hub"),
    ("TeglonLabs","TeglonLabs/monad-mcp-server","",0,0,0,"2025-05-14T11:36:14Z","Monad MCP Server"),
    ("TeglonLabs","TeglonLabs/coin-flip-mcp","JavaScript",0,2,1,"2025-09-21T08:57:27Z","MCP server for flipping coins"),
]

# --- bmorphism (100 of 105) ---
bmorphism_repos = [
    ("bmorphism","bmorphism/ocaml-mcp-sdk","OCaml",61,2,0,"2026-03-16T05:24:25Z","OCaml SDK for Model Context Protocol"),
    ("bmorphism","bmorphism/anti-bullshit-mcp-server","JavaScript",23,7,1,"2026-01-16T08:54:58Z","MCP server for analyzing claims"),
    ("bmorphism","bmorphism/risc0-cosmwasm-example","Rust",23,2,1,"2022-10-20T23:50:40Z","CosmWasm + zkVM RISC-V EFI template"),
    ("bmorphism","bmorphism/say-mcp-server","JavaScript",20,9,3,"2025-01-07T03:15:18Z","MCP server for macOS text-to-speech"),
    ("bmorphism","bmorphism/babashka-mcp-server","JavaScript",19,6,3,"2025-01-05T11:09:42Z","MCP server for Babashka"),
    ("bmorphism","bmorphism/manifold-mcp-server","JavaScript",14,9,5,"2025-01-11T10:36:58Z","MCP server for Manifold Markets"),
    ("bmorphism","bmorphism/penrose-mcp","JavaScript",9,4,0,"2025-01-20T21:44:55Z","Penrose server for Infinity-Topos"),
    ("bmorphism","bmorphism/marginalia-mcp-server","JavaScript",8,6,0,"2025-01-06T05:47:24Z","MCP server for marginalia"),
    ("bmorphism","bmorphism/nats-mcp-server","",7,3,2,"2025-01-06T23:33:41Z","MCP server for NATS messaging"),
    ("bmorphism","bmorphism/hypernym-mcp-server","JavaScript",6,5,0,"2025-04-02T21:21:08Z",""),
    ("bmorphism","bmorphism/penumbra-mcp","JavaScript",5,6,3,"2025-01-07T01:15:23Z","MCP server for Penumbra blockchain"),
    ("bmorphism","bmorphism/Gay.jl","Julia",2,1,187,"2026-07-03T00:34:16Z","Wide-gamut color sampling with splittable determinism"),
    ("bmorphism","bmorphism/open-location-code-zig","Zig",3,0,0,"2025-12-30T19:33:45Z","Open Location Code for Zig"),
    ("bmorphism","bmorphism/slowtime-mcp-server","TypeScript",3,5,6,"2025-01-02T01:23:33Z","MCP server for secure time-based operations"),
    ("bmorphism","bmorphism/graphistry-mcp","Python",2,0,0,"2025-05-06T17:34:24Z","Graphistry MCP integration"),
    ("bmorphism","bmorphism/whale","MATLAB",2,0,0,"2025-09-04T06:55:21Z","omniglot + sperm whale codas"),
    ("bmorphism","bmorphism/rama-event-processor","Java",1,0,0,"2025-07-02T07:01:44Z","Event processing with Rama"),
    ("bmorphism","bmorphism/zeldar","Python",1,0,1,"2025-08-26T15:16:21Z","Burning Man Art Robot"),
    ("bmorphism","bmorphism/monero-rental-hash-war","Haskell",1,0,0,"2025-10-05T23:08:54Z","Monero rental hash war analysis"),
    ("bmorphism","bmorphism/krep-mcp-server","JavaScript",1,1,1,"2025-03-19T20:22:46Z","High-performance string search MCP"),
    ("bmorphism","bmorphism/vibespace-mcp-go-ternary","HTML",0,1,3,"2026-01-11T12:50:40Z","Go MCP with balanced ternary support"),
    ("bmorphism","bmorphism/world","Python",0,0,0,"2026-06-02T06:49:02Z","Local worlds launcher"),
    ("bmorphism","bmorphism/GeoACSets.jl","Julia",0,1,1,"2026-01-19T13:57:13Z","Categorical data structures with geospatial"),
    ("bmorphism","bmorphism/oxgame","OCaml",0,0,0,"2026-05-15T09:53:27Z","Stellar resolution and open-game composition"),
    ("bmorphism","bmorphism/flox-mcp-bb","Clojure",0,0,0,"2026-02-12T02:45:43Z","Open-source MCP server for Flox"),
    ("bmorphism","bmorphism/postweb","Go",0,0,0,"2026-04-09T10:51:57Z","postweb evolved from prepostweb"),
    ("bmorphism","bmorphism/satreadout","HTML",0,0,0,"2026-06-20T13:05:41Z","Machine-checked saturating non-Riemannian readout"),
    ("bmorphism","bmorphism/oxcaml-sci-canonical","OCaml",1,0,0,"2025-06-20T06:37:12Z","Canonical OxCaml-SCI implementation"),
    ("bmorphism","bmorphism/magic-world-org","Python",1,0,0,"2026-04-05T07:03:50Z","Magic World Org (Local MLX)"),
    ("bmorphism","bmorphism/bci-preview","HTML",0,0,0,"2026-06-20T00:20:44Z","Stable redirect for bci.place"),
    ("bmorphism","bmorphism/apple-container-framework","Clojure",0,0,0,"2025-07-13T12:12:10Z","Apple Container Framework Babashka"),
    ("bmorphism","bmorphism/nanoclj-zig","Zig",1,0,0,"2026-05-07T20:12:15Z",""),
    ("bmorphism","bmorphism/bafishka","Clojure",1,0,0,"2025-12-19T09:38:00Z","Rust-native Fish shell file operations"),
    ("bmorphism","bmorphism/lumon-tui","Python",1,0,0,"2025-02-02T11:24:21Z","Terminal parallel worlds"),
    ("bmorphism","bmorphism/ezkl-ethglobal2025","Python",1,0,0,"2025-07-07T01:16:01Z",""),
    ("bmorphism","bmorphism/zk-haiku-nanogpt","Solidity",1,0,0,"2025-07-06T03:08:24Z","ZK-Haiku-NanoGPT verifiable multi-agent"),
    ("bmorphism","bmorphism/vibespace-mcp-go","",0,0,0,"2025-03-19T20:30:02Z","Go MCP for vibes with NATS streaming"),
]

# --- zubyul (49) ---
zubyul_repos = [
    ("zubyul","zubyul/WGCNA","HTML",2,0,0,"2023-07-05T18:02:30Z","weighted gene correlation network analysis"),
    ("zubyul","zubyul/jonikas_lab_data_analysis_misc","Jupyter Notebook",2,0,0,"2023-08-16T20:24:40Z","scripts for genetic sequence data"),
    ("zubyul","zubyul/Nikolova_lab_data_analysis","R",2,0,0,"2023-06-16T13:56:58Z","undergraduate thesis cortical thickness"),
    ("zubyul","zubyul/gay-world","Python",1,1,0,"2026-03-26T04:03:39Z","Goblin world builder MLX task decomposition"),
    ("zubyul","zubyul/ghostty-modifications","JavaScript",1,0,0,"2025-09-15T02:45:21Z","Ghostty terminal modifications and MCP servers"),
    ("zubyul","zubyul/zubyul.github.io","CSS",1,0,0,"2026-01-27T03:24:34Z",""),
    ("zubyul","zubyul/defcon","JavaScript",1,0,0,"2025-09-17T02:07:00Z",""),
    ("zubyul","zubyul/GoofyLifeChoices","Python",1,0,0,"2025-07-30T18:48:13Z",""),
    ("zubyul","zubyul/cascade-world","Python",1,0,0,"2025-09-19T18:25:12Z","Cascade development environment"),
    ("zubyul","zubyul/send2kobo","TypeScript",1,0,0,"2026-05-19T02:59:26Z","Send books to Kobo e-reader"),
    ("zubyul","zubyul/big-bad-plurigrid-quiz","Emacs Lisp",0,0,0,"2026-04-09T18:51:31Z","27 flashcards from bmorphism/plurigrid activity"),
    ("zubyul","zubyul/nash-tui","Rust",0,0,0,"2026-04-13T07:45:16Z","NASH token TUI real-time candles"),
    ("zubyul","zubyul/nash-web","Rust",0,0,0,"2026-04-13T07:08:58Z","NASH token browser TUI ratzilla WASM"),
    ("zubyul","zubyul/openbci-visualizer","Zig",0,0,0,"2026-02-04T11:17:41Z",""),
    ("zubyul","zubyul/tilelang-kernels","Python",0,0,0,"2026-03-16T02:31:13Z","TileLang GPU kernels for SplitMix64 color"),
    ("zubyul","zubyul/voice-observatory","Python",0,0,0,"2026-04-24T05:56:17Z","Passive macOS TUI observing voice paths"),
    ("zubyul","zubyul/ghostel-emacs-worlds","GLSL",0,0,0,"2026-04-24T00:20:56Z","Ghostty config alice/bob emacs-mods"),
    ("zubyul","zubyul/plurigrid-site","Svelte",0,1,11,"2026-02-04T03:20:08Z","Plurigrid world site deployment"),
    ("zubyul","zubyul/gay-terminal-colors","Clojure",0,0,0,"2026-02-21T07:38:14Z","Gay.jl world terminal fingerprint"),
    ("zubyul","zubyul/Gay.jl","Julia",0,0,0,"2026-03-28T11:30:01Z","Wide-gamut color sampling fork"),
    ("zubyul","zubyul/kinesis-kb360pro","Python",0,0,0,"2026-03-26T10:29:40Z","Claude Code skill for Kinesis keyboard"),
    ("zubyul","zubyul/repl","Python",0,0,0,"2026-02-04T01:08:15Z",""),
    ("zubyul","zubyul/from-possible-worlds","TeX",0,0,0,"2026-03-16T03:14:55Z",""),
    ("zubyul","zubyul/toad-warpify-extension","Python",0,0,0,"2026-01-17T07:48:40Z","Warpify extension for Toad"),
    ("zubyul","zubyul/thread-site","Haskell",0,0,0,"2025-12-23T23:53:27Z",""),
    ("zubyul","zubyul/c-elegans-connectome","JavaScript",0,0,0,"2025-11-22T15:45:00Z",""),
    ("zubyul","zubyul/chromatic-vrf","Kotlin",0,0,0,"2025-12-12T03:26:22Z","Chromatic VRF Gay.jl MCMC EG-Walker CRDT"),
]

# --- social graph users ---
migalkin_repos = [
    ("migalkin","migalkin/NodePiece","Python",144,21,0,"2026-05-07T05:40:02Z","Compositional Representations for Knowledge Graphs"),
    ("migalkin","migalkin/StarE","Python",89,16,1,"2026-04-16T14:12:45Z","Hyper-Relational Knowledge Graphs EMNLP 2020"),
    ("migalkin","migalkin/kgcourse2021","HTML",25,9,0,"2026-02-16T05:16:08Z","Knowledge Graphs course materials"),
    ("migalkin","migalkin/NBFNet_mlx","Python",10,1,1,"2026-03-11T01:31:21Z","Neural Bellman-Ford networks in MLX"),
    ("migalkin","migalkin/RWL","Python",8,1,0,"2026-05-28T20:19:20Z","Weisfeiler and Leman Go Relational"),
    ("migalkin","migalkin/rambo","Rust",3,0,1,"2023-02-28T16:37:22Z",""),
]
djedamski_repos = [
    ("DJedamski","DJedamski/Getting-and-Cleaning-Data","R",1,0,0,"2023-04-21T01:42:34Z","Coursera Project"),
    ("DJedamski","DJedamski/Kaggle","",1,0,0,"2023-04-21T01:42:35Z",""),
    ("DJedamski","DJedamski/School","R",1,1,0,"2023-04-21T01:42:33Z","Projects from grad school"),
]
wasita_repos = [
    ("wasita","wasita/magic-garden","Python",2,1,1,"2026-04-22T21:16:43Z","Bot for magic garden discord game"),
    ("wasita","wasita/wasita.github.io","Svelte",1,0,8,"2026-07-02T01:40:18Z","personal website"),
    ("wasita","wasita/wins-search","CSS",1,0,0,"2023-06-03T19:01:11Z","Women in Network Science member list"),
    ("wasita","wasita/send2kobo","TypeScript",1,0,0,"2026-05-19T02:59:26Z","Website for sending books to Kobo"),
    ("wasita","wasita/wm-cv","Svelte",0,0,0,"2026-05-13T05:29:08Z","Academic CV as single page web app"),
]
kristinezheng_repos = [
    ("kristinezheng","kristinezheng/Green-Machine","Python",0,0,0,"2021-09-19T05:33:04Z","HackMIT 2021 Sustainability Track"),
    ("kristinezheng","kristinezheng/lookit-jenga","Jupyter Notebook",0,0,0,"2024-05-16T18:29:05Z","Lookit study for 9.85"),
    ("kristinezheng","kristinezheng/kristinezheng.github.io","HTML",0,0,0,"2026-07-01T20:57:48Z",""),
]
m1shaaa_repos = [
    ("M1shaaa","M1shaaa/lab-bookshelf-","TypeScript",0,0,0,"2024-12-31T05:11:18Z",""),
    ("M1shaaa","M1shaaa/Python-Lookit-Uploads","Python",0,0,0,"2024-02-15T22:59:37Z","random projects"),
]
austincstone_repos = [
    ("AustinCStone","AustinCStone/TextGAN","Python",92,30,5,"2025-03-03T13:26:32Z","GAN for text generation in TensorFlow"),
    ("AustinCStone","AustinCStone/StereoVisionMRF","Python",11,4,0,"2026-04-01T07:39:41Z","Depth from stereo images MRF"),
    ("AustinCStone","AustinCStone/SpectralClustering","Python",3,2,0,"2021-04-16T08:46:36Z","Spectral clustering homework"),
    ("AustinCStone","AustinCStone/bmfork","Python",0,0,1,"2025-05-09T04:18:54Z",""),
    ("AustinCStone","AustinCStone/EpsteinSearch","Python",0,0,0,"2026-02-11T01:10:57Z",""),
]

all_repo_groups = (
    plurigrid_repos + kubeflow_repos + teglon_repos + bmorphism_repos +
    zubyul_repos + migalkin_repos + djedamski_repos + wasita_repos +
    kristinezheng_repos + m1shaaa_repos + austincstone_repos
)

# Insert repos
increment_id = 1
repo_id = 1

for (org_user, full_name, lang, stars, forks, issues, pushed_at, desc) in all_repo_groups:
    trit, color, name = gf3(increment_id)
    snap_hash = hashlib.md5(f"{full_name}{pushed_at}".encode()).hexdigest()[:12]
    repo_short = full_name.split("/")[-1] if "/" in full_name else full_name

    con.execute("""
        INSERT INTO world_increments
        (id, gf3_trit, gf3_color, gf3_name, source_type, source_name, event_type, repo_name, actor, snapshot_hash)
        VALUES (?, ?, ?, ?, 'repo', ?, 'push', ?, ?, ?)
    """, [increment_id, trit, color, name, org_user, repo_short, org_user, snap_hash])

    con.execute("""
        INSERT INTO repo_snapshots
        (id, increment_id, org_or_user, repo_name, full_name, language, stars, forks, open_issues, pushed_at, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [repo_id, increment_id, org_user, repo_short, full_name, lang, stars, forks, issues, pushed_at, desc])

    increment_id += 1
    repo_id += 1

print(f"Inserted {repo_id-1} repos as world increments")

# ── Aptos snapshots ──────────────────────────────────────────────────────
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
    con.execute("""
        INSERT INTO aptos_snapshots (world, address, balance_apt)
        VALUES (?, ?, ?)
    """, [world, addr, bal])

print(f"Inserted {len(aptos_data)} Aptos snapshots")

# ── Multisig probes ──────────────────────────────────────────────────────
multisig_data = [
    ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2,True),
    ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2,True),
    ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2,True),
    ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2,True),
    ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2,True),
]

for pair, addr, sigs, healthy in multisig_data:
    con.execute("""
        INSERT INTO multisig_probes (pair, address, sigs_required, healthy)
        VALUES (?, ?, ?, ?)
    """, [pair, addr, sigs, healthy])

print("Inserted 5 multisig probes")

# MNX: unavailable (Vercel auth gated)
con.execute("""
    INSERT INTO mnx_snapshots (ticker, name, category, price, change_pct)
    VALUES ('N/A', 'MNX testnet unavailable (Vercel auth required)', 'N/A', 0.0, 0.0)
""")

# ── Summary query ─────────────────────────────────────────────────────────
total_repos = con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0]
total_increments = con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0]
total_aptos = con.execute("SELECT COUNT(*) FROM aptos_snapshots").fetchone()[0]
top_stars = con.execute("""
    SELECT full_name, stars, language FROM repo_snapshots
    ORDER BY stars DESC LIMIT 10
""").fetchall()

print(f"\nDB summary:")
print(f"  world_increments: {total_increments}")
print(f"  repo_snapshots:   {total_repos}")
print(f"  aptos_snapshots:  {total_aptos}")
print(f"\nTop repos by stars:")
for row in top_stars:
    print(f"  {row[0]:50s} ★{row[1]} ({row[2]})")

con.close()
print("\nDone. DB written to:", DB_PATH)
