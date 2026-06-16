#!/usr/bin/env python3
"""World-increment sweep + Hamming swarm snapshot."""
import subprocess, json, time, hashlib, os, sys
from datetime import datetime

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"

def duckdb_exec(sql):
    r = subprocess.run(["duckdb", DB, sql], capture_output=True, text=True)
    if r.returncode != 0 and r.stderr:
        print(f"  DuckDB warn: {r.stderr.strip()[:200]}")
    return r.stdout

def duckdb_exec_script(path):
    r = subprocess.run(["duckdb", DB, f".read {path}"], capture_output=True, text=True)
    if r.returncode != 0 and r.stderr:
        print(f"  DuckDB warn: {r.stderr.strip()[:200]}")
    return r.stdout

# GF(3) color chain
def gf3(idx):
    t = idx % 3
    if t == 0: return (0, "ERGODIC", "#d3869b")
    if t == 1: return (1, "PLUS", "#b8bb26")
    return (-1, "MINUS", "#cc241d")

# ── SCHEMA ──────────────────────────────────────────────────────────────────
SCHEMA = """
CREATE TABLE IF NOT EXISTS world_increments (
  id INTEGER, timestamp TIMESTAMP DEFAULT now(), gf3_trit INTEGER,
  gf3_color VARCHAR, gf3_name VARCHAR, source_type VARCHAR,
  source_name VARCHAR, event_type VARCHAR, repo_name VARCHAR,
  actor VARCHAR, snapshot_hash VARCHAR
);
CREATE TABLE IF NOT EXISTS repo_snapshots (
  id INTEGER, timestamp TIMESTAMP DEFAULT now(), increment_id INTEGER,
  org_or_user VARCHAR, repo_name VARCHAR, full_name VARCHAR,
  language VARCHAR, stars INTEGER, forks INTEGER, open_issues INTEGER,
  pushed_at VARCHAR, description VARCHAR
);
CREATE SEQUENCE IF NOT EXISTS increment_seq START 1;
CREATE SEQUENCE IF NOT EXISTS repo_seq START 1;
CREATE TABLE IF NOT EXISTS aptos_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  world VARCHAR, address VARCHAR, balance_apt DOUBLE
);
CREATE TABLE IF NOT EXISTS multisig_probes (
  timestamp TIMESTAMP DEFAULT now(),
  pair VARCHAR, address VARCHAR, sigs_required INTEGER, healthy BOOLEAN
);
CREATE TABLE IF NOT EXISTS mnx_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  ticker VARCHAR, name VARCHAR, category VARCHAR,
  price DOUBLE, change_pct DOUBLE
);
"""

print("Creating schema...")
for stmt in SCHEMA.strip().split(";"):
    s = stmt.strip()
    if s:
        duckdb_exec(s + ";")

# ── GITHUB DATA ─────────────────────────────────────────────────────────────
# Collected repo data: (org_or_user, source_type, repos)
# Each repo: full_name|language|stars|forks|issues|pushed_at|description
GITHUB_DATA = {
    "plurigrid": ("org", [
        "plurigrid/asi|HTML|26|8|4|2026-06-10T12:51:42Z|everything is topological chemputer!",
        "plurigrid/place|TeX|1|2|8|2026-06-15T23:04:11Z|",
        "plurigrid/eirobri|Clojure|0|0|29|2026-06-03T20:43:46Z|EiRoBri replay world",
        "plurigrid/nash-portal|Rust|2|3|1|2026-05-19T01:49:59Z|NASH token TUI in the browser",
        "plurigrid/gorj|Clojure|0|0|610|2026-06-16T04:18:07Z|forj + Rama topology nREPL routing + GF(3) gay trit coloring",
        "plurigrid/zig-syrup|Zig|2|2|0|2026-04-30T03:52:16Z|High-performance Zig implementation of OCapN Syrup",
        "plurigrid/asi-skills|Julia|3|1|0|2026-04-26T08:09:26Z|69 skills with Galois Hole Type accessibility",
        "plurigrid/bci-blue-share|JavaScript|0|0|0|2026-04-26T07:08:03Z|BCI signal infrastructure",
        "plurigrid/nanoclj-zig|Zig|1|2|20|2026-04-25T07:29:09Z|NaN-boxed Clojure interpreter in Zig 0.15",
        "plurigrid/spi-race|Swift|0|0|0|2026-04-21T19:31:56Z|Splitmix Parallel Integrity",
        "plurigrid/reafference|HTML|0|0|0|2026-04-16T05:21:49Z|Reafference adaptation workspace",
        "plurigrid/web-browser|Rust|0|0|0|2026-04-10T02:54:47Z|web-browser — from prepostweb lineage",
        "plurigrid/vivarium|Clojure|1|0|0|2026-04-08T08:38:37Z|",
        "plurigrid/flowglad-rs|Rust|0|0|0|2026-04-08T07:56:15Z|",
        "plurigrid/tree-sitter-nanoclj-zig|C|0|0|0|2026-04-04T07:48:21Z|Tree-sitter grammar for nanoclj-zig",
        "plurigrid/forester|XSLT|0|0|0|2026-03-30T01:32:26Z|CatColab mathematical documentation forest",
        "plurigrid/gatomic|Clojure|0|0|0|2026-03-30T00:54:48Z|Deterministic color identity store with sonification",
        "plurigrid/blue|TeX|0|0|0|2026-03-29T23:06:32Z|",
        "plurigrid/red||0|0|0|2026-03-29T22:58:46Z|",
        "plurigrid/nblm-flashcards|Hy|0|0|0|2026-03-26T08:23:01Z|NotebookLM Enterprise flashcard pipeline",
        "plurigrid/gemini-agent|Python|0|0|0|2026-02-19T06:39:16Z|",
        "plurigrid/graded-optic|Haskell|0|0|0|2026-02-08T16:10:16Z|Semiring-graded bidirectional processes",
        "plurigrid/json-canvas||0|0|0|2026-02-06T06:50:57Z|JSON Canvas: Real-time interaction data capture",
        "plurigrid/shepherd|Scheme|0|0|0|2026-01-23T07:47:28Z|Spritely Shepherd - Service manager",
        "plurigrid/goblinshare|Scheme|0|0|0|2026-01-23T07:47:12Z|P2P filesharing demo for Goblins",
        "plurigrid/magenc|Scheme|0|0|0|2026-01-23T07:47:11Z|Magenc Magnet URIs - Secure Object Permanence",
        "plurigrid/hoot|Scheme|0|0|1|2026-01-23T07:47:10Z|Spritely Hoot - Scheme to WebAssembly compiler",
        "plurigrid/leprechauns|Racket|0|0|0|2026-01-23T07:46:46Z|Spritely Goblins + Gay.jl semantic colors",
        "plurigrid/spritely-semantic-colors||0|0|0|2026-01-23T07:38:32Z|Deterministic color mappings for Spritely/Goblins",
        "plurigrid/gay-tofu|HTML|0|0|0|2026-01-08T15:14:34Z|Low-discrepancy color sequences for visual TOFU authentication",
        "plurigrid/lazygay|Go|0|0|0|2026-01-08T14:19:25Z|lazygit fork with Gay.jl deterministic commit coloring",
        "plurigrid/gay-terminal|Rust|0|0|0|2026-01-08T14:19:24Z|Terminal ANSI coloring with Gay.jl low-discrepancy sequences",
        "plurigrid/gay-go|Go|0|0|0|2026-01-08T14:19:23Z|Go implementation of Gay.jl deterministic coloring",
        "plurigrid/gay-rs|Rust|0|0|0|2026-01-08T14:19:22Z|Rust crate for Gay.jl deterministic coloring",
        "plurigrid/lazybjj|Rust|0|0|0|2026-01-08T14:19:19Z|TUI for jj with Gay.jl GF(3) coloring",
        "plurigrid/agent-o-rama|Clojure|0|0|0|2026-01-02T01:09:22Z|",
        "plurigrid/aptos-wallet-ruby|Ruby|1|0|0|2025-09-30T22:47:22Z|",
        "plurigrid/duck-kanban|Rust|1|0|0|2025-09-26T20:18:38Z|Duck intelligence kanban system",
        "plurigrid/discohy|Hy|0|0|0|2025-09-10T02:01:31Z|",
        "plurigrid/ontology|JavaScript|8|9|16|2025-05-27T18:18:34Z|autopoietic ergodicity and embodied gradualism",
        "plurigrid/Plurigraph|JavaScript|3|5|4|2025-01-05T08:39:09Z|Plurigrid knowledge base for use with Obsidian.md",
        "plurigrid/signe|Python|0|0|0|2024-08-15T20:52:03Z|Signal messages data traversal",
        "plurigrid/act|Python|3|1|4|2024-07-26T08:27:08Z|building blocks for cognitive category theory",
        "plurigrid/StochFlow|Python|4|1|0|2024-03-20T23:34:57Z|Python library for stochastic interpolant models",
        "plurigrid/novella|TypeScript|1|0|0|2024-01-27T08:12:55Z|",
        "plurigrid/microworlds|Rust|3|5|3|2023-05-13T03:54:56Z|",
        "plurigrid/agent|Python|5|1|6|2023-03-31T18:45:23Z|Framework for agency amplification",
        "plurigrid/vcg-auction|Rust|7|2|1|2023-03-16T21:53:08Z|a simple contract that performs a VCG auction",
        "plurigrid/grid|TypeScript|2|1|1|2023-01-02T11:55:55Z|Plurigrid Testnet #0: Edith Clarke",
        "plurigrid/org|Jupyter Notebook|2|0|1|2023-11-07T01:08:05Z|Dynamically Replicating Duck",
        "plurigrid/VPP|Julia|0|1|0|2023-01-11T18:41:07Z|Hyperreal Power Plant",
    ]),
    "kubeflow": ("org", [
        "kubeflow/trainer|Go|2115|969|125|2026-06-16T04:39:35Z|Distributed AI Model Training and LLM Fine-Tuning on Kubernetes",
        "kubeflow/hub|Go|173|183|52|2026-06-15T19:56:13Z|Model Registry provides a single pane of glass for ML model developers",
        "kubeflow/pipelines|Python|4154|2008|476|2026-06-15T19:49:07Z|Machine Learning Pipelines for Kubeflow",
        "kubeflow/community|Jupyter Notebook|194|261|26|2026-06-15T17:07:10Z|Information about the Kubeflow community",
        "kubeflow/community-distribution|YAML|1024|1065|23|2026-06-15T16:47:58Z|Kubeflow Community Distribution",
        "kubeflow/website|HTML|184|924|50|2026-06-15T14:46:37Z|Kubeflow Website",
        "kubeflow/notebooks||73|120|171|2026-06-13T00:38:04Z|Kubeflow Notebooks runs interactive development environments",
        "kubeflow/katib|Python|1683|527|118|2026-06-15T20:07:37Z|Automated Machine Learning on Kubernetes",
        "kubeflow/mlflow-integration|Python|6|4|2|2026-06-12T19:04:52Z|",
        "kubeflow/spark-operator|Python|3127|1490|101|2026-06-15T16:37:34Z|Kubernetes operator for managing the lifecycle of Apache Spark",
        "kubeflow/mpi-operator|Go|528|236|106|2026-06-15T13:03:34Z|Kubernetes Operator for MPI-based applications",
        "kubeflow/sdk|Python|121|180|133|2026-06-16T03:07:23Z|Universal Python SDK to run AI workloads on Kubernetes",
        "kubeflow/docs-agent|Python|39|95|151|2026-06-11T18:43:15Z|Kubeflow Documentation AI Agent",
        "kubeflow/internal-acls|Go|19|389|1|2026-06-11T18:23:36Z|Repository used to main group ACLs",
        "kubeflow/kubeflow||15726|2674|3|2026-06-11T16:32:05Z|Machine Learning Toolkit for Kubernetes",
        "kubeflow/blog|Jupyter Notebook|32|62|26|2026-06-11T16:32:01Z|Kubeflow blog based on fastpages",
        "kubeflow/mcp-apache-spark-history-server|Python|177|64|22|2026-06-16T03:07:21Z|MCP Server for Apache Spark History Server",
        "kubeflow/kale|Python|694|155|49|2026-06-12T22:05:05Z|Kubeflows superfood for Data Scientists",
        "kubeflow/dashboard|TypeScript|16|59|75|2026-06-11T17:07:50Z|Kubeflow Central Dashboard",
        "kubeflow/pipelines-components|Python|11|43|34|2026-06-16T03:40:41Z|Kubeflow Pipelines",
        "kubeflow/mcp-server|Python|11|20|25|2026-05-12T10:14:24Z|MCP Server for AI-Assisted Development with Kubeflow Tools",
        "kubeflow/arena|Go|812|190|44|2026-05-07T06:46:17Z|A CLI for Kubeflow",
        "kubeflow/examples|Jsonnet|1461|756|111|2025-04-14T01:54:52Z|A repository to host extended examples and tutorials",
        "kubeflow/testing|Python|60|86|33|2025-02-14T18:33:13Z|Test infrastructure and tooling for Kubeflow",
        "kubeflow/kfp-tekton|TypeScript|182|123|79|2024-11-19T12:23:51Z|Kubeflow Pipelines on Tekton",
        "kubeflow/fairing|Jsonnet|337|143|134|2022-04-11T05:28:47Z|Python SDK for building training and deploying ML models",
        "kubeflow/xgboost-operator|Python|77|53|22|2021-12-01T18:00:10Z|Incubating project for xgboost operator",
        "kubeflow/pytorch-operator|Jsonnet|310|143|63|2021-12-01T17:44:48Z|PyTorch on Kubernetes",
    ]),
    "TeglonLabs": ("org", [
        "TeglonLabs/jank-crane|C++|0|0|0|2026-06-08T19:03:03Z|crane-jank converged-IR hub: loopify pass spec GF3 convergence maps",
        "TeglonLabs/mathpix-gem|Ruby|2|0|11|2026-01-01T12:13:13Z|Transform mathematical images to LaTeX chemistry structures to SMILES",
        "TeglonLabs/coin-flip-mcp|JavaScript|0|2|1|2025-09-21T08:57:27Z|MCP server for flipping coins with varying degrees of randomness",
        "TeglonLabs/monad-mcp-server||0|0|0|2025-05-14T11:36:14Z|Monad MCP Server",
        "TeglonLabs/topoi|Python|0|0|1|2025-01-24T04:49:26Z|",
    ]),
    "bmorphism": ("user", [
        "bmorphism/satreadout|Lean|0|0|0|2026-06-15T21:20:06Z|Machine-checked saturating non-Riemannian perceptual readout",
        "bmorphism/Gay.jl|Julia|1|1|187|2026-06-16T00:49:54Z|Wide-gamut color sampling with splittable determinism",
        "bmorphism/world|Python|0|0|0|2026-06-02T06:49:02Z|Local worlds launcher for SA3 jank and world proofs",
        "bmorphism/oxgame|OCaml|0|0|0|2026-05-15T09:53:27Z|Stellar resolution and open-game composition for OCaml",
        "bmorphism/nanoclj-zig|Zig|1|0|0|2026-05-07T20:12:15Z|",
        "bmorphism/zig-syrup|Zig|0|0|0|2026-05-07T19:49:05Z|Embeddable OCapN Syrup encoder/decoder in Zig",
        "bmorphism/boxxy|Move|0|1|0|2026-04-30T03:35:47Z|",
        "bmorphism/postweb|Go|0|0|0|2026-04-09T10:51:57Z|postweb — evolved from prepostweb",
        "bmorphism/shitcoin|Python|5|0|0|2026-04-08T08:07:08Z|gets denom for cw20 assets for permissionless degeneracy in IBC",
        "bmorphism/magic-world-org|Python|1|0|0|2026-04-05T07:03:50Z|Magic World Org (Local MLX)",
        "bmorphism/ocaml-mcp-sdk|OCaml|61|2|0|2026-03-16T05:24:25Z|OCaml SDK for Model Context Protocol",
        "bmorphism/flox-mcp-bb|Clojure|0|0|0|2026-02-12T02:45:43Z|Open-source MCP server for Flox",
        "bmorphism/vibesnipe-market|Move|0|0|9|2026-02-05T10:23:25Z|",
        "bmorphism/anti-bullshit-mcp-server|JavaScript|23|7|1|2026-01-16T08:54:58Z|MCP server for analyzing claims validating sources",
        "bmorphism/vibespace-mcp-go-ternary|HTML|0|1|3|2026-01-11T12:50:40Z|Go implementation of a MCP experience for vibes and worlds",
        "bmorphism/open-location-code-zig|Zig|3|0|0|2025-12-30T19:33:45Z|Open Location Code (Plus Codes) for Zig",
        "bmorphism/bafishka|Clojure|1|0|0|2025-12-19T09:38:00Z|Rust-native Fish shell-friendly file operations",
        "bmorphism/hypernym-mcp-server|JavaScript|6|5|0|2025-04-02T21:21:08Z|",
        "bmorphism/manifold-mcp-server|JavaScript|14|9|5|2025-01-11T10:36:58Z|MCP server for interacting with Manifold Markets",
        "bmorphism/say-mcp-server|JavaScript|20|9|3|2025-01-07T03:15:18Z|MCP server for macOS text-to-speech",
        "bmorphism/penumbra-mcp|JavaScript|5|6|3|2025-01-07T01:15:23Z|MCP server for interacting with Penumbra blockchain",
        "bmorphism/nats-mcp-server||7|3|2|2025-01-06T23:33:41Z|MCP server for NATS messaging system",
        "bmorphism/marginalia-mcp-server|JavaScript|8|6|0|2025-01-06T05:47:24Z|An MCP server implementation for managing marginalia",
        "bmorphism/babashka-mcp-server|JavaScript|19|6|3|2025-01-05T11:09:42Z|A Model Context Protocol server for Babashka",
        "bmorphism/penrose-mcp|JavaScript|10|4|0|2025-01-20T21:44:55Z|Penrose server for the Infinity-Topos environment",
        "bmorphism/risc0-cosmwasm-example|Rust|23|2|1|2022-10-20T23:50:40Z|CosmWasm + zkVM RISC-V EFI template",
        "bmorphism/graphistry-mcp|Python|2|0|0|2025-05-06T17:34:24Z|Graphistry MCP integration for graph visualization",
        "bmorphism/whale|MATLAB|2|0|0|2025-09-04T06:55:21Z|omniglot + sperm whale codas = metawhaling",
        "bmorphism/monero-rental-hash-war|Haskell|1|0|0|2025-10-05T23:08:54Z|Compositional OpenGame analysis of Monero rental hash war",
        "bmorphism/elevenlabs-mcp-enhanced|Python|1|0|0|2025-08-29T04:41:58Z|Enhanced ElevenLabs MCP server",
        "bmorphism/rama-event-processor|Java|1|0|0|2025-07-02T07:01:44Z|A repository for processing events with Rama",
        "bmorphism/slowtime-mcp-server|TypeScript|3|5|6|2025-01-02T01:23:33Z|A Model Context Protocol server for secure time-based operations",
        "bmorphism/krep-mcp-server|JavaScript|1|1|1|2025-03-19T20:22:46Z|High-performance string search MCP server",
        "bmorphism/kfsummit19|Python|0|0|0|2019-10-28T16:40:46Z|Example of running kubeflow pipelines on Anthos",
    ]),
    "zubyul": ("user", [
        "zubyul/voice-observatory|Python|0|0|0|2026-04-24T05:56:17Z|Passive macOS TUI observing voice-download pathways",
        "zubyul/ghostel-emacs-worlds|GLSL|0|0|0|2026-04-24T00:20:56Z|Ghostty config + ghostel family + alice/bob emacs-mods",
        "zubyul/nash-tui|Rust|0|0|0|2026-04-13T07:45:16Z|NASH token TUI: real-time candles ticker buy pressure gauge",
        "zubyul/nash-web|Rust|0|0|0|2026-04-13T07:08:58Z|NASH token browser TUI via ratzilla WASM + GeckoTerminal OHLCV",
        "zubyul/big-bad-plurigrid-quiz|Emacs Lisp|0|0|0|2026-04-09T18:51:31Z|27 flashcards from bmorphism/plurigrid/zubyul activity",
        "zubyul/Gay.jl|Julia|0|0|0|2026-03-28T11:30:01Z|Wide-gamut color sampling with splittable determinism",
        "zubyul/kinesis-kb360pro|Python|0|0|0|2026-03-26T10:29:40Z|Claude Code skill for Kinesis Advantage360 Pro keyboard",
        "zubyul/gay-world|Python|1|1|0|2026-03-26T04:03:39Z|Goblin world builder",
        "zubyul/from-possible-worlds|TeX|0|0|0|2026-03-16T03:14:55Z|",
        "zubyul/tilelang-kernels|Python|0|0|0|2026-03-16T02:31:13Z|TileLang GPU kernels for SplitMix64 color generation",
        "zubyul/fleet-bootstrap|Shell|0|0|0|2026-02-23T08:19:58Z|",
        "zubyul/gay-terminal-colors|Clojure|0|0|0|2026-02-21T07:38:14Z|Gay.jl world_terminal_fingerprint",
        "zubyul/basin|Rust|0|0|0|2026-02-13T10:31:47Z|",
        "zubyul/openbci-visualizer|Zig|0|0|0|2026-02-04T11:17:41Z|",
        "zubyul/plurigrid-site|Svelte|0|1|11|2026-02-04T03:20:08Z|Plurigrid world: site deployment",
        "zubyul/repl|Python|0|0|0|2026-02-04T01:08:15Z|",
        "zubyul/zubyul.github.io|CSS|1|0|0|2026-01-27T03:24:34Z|",
        "zubyul/gay-brain-world|Python|0|0|0|2025-12-16T01:19:28Z|Gay.jl SPI colors for Moduleur Brain",
        "zubyul/cat-world|TypeScript|0|0|0|2025-12-12T08:47:14Z|Cat gaze tracker",
        "zubyul/hue-world|JavaScript|0|0|0|2025-12-12T08:32:59Z|Terminal Vibe Snipe puzzle game",
        "zubyul/cascade-world|Python|1|0|0|2025-09-19T18:25:12Z|Cascade development environment",
        "zubyul/defcon|JavaScript|1|0|0|2025-09-17T02:07:00Z|",
        "zubyul/ghostty-modifications|JavaScript|1|0|0|2025-09-15T02:45:21Z|Ghostty terminal modifications and MCP servers",
        "zubyul/jonikas_lab_data_analysis_misc|Jupyter Notebook|2|0|0|2023-08-16T20:24:40Z|various scripts to process genetic sequence data",
        "zubyul/WGCNA|HTML|2|0|0|2023-07-05T18:02:30Z|weighted gene correlation network analysis project",
        "zubyul/Nikolova_lab_data_analysis|R|2|0|0|2023-06-16T13:56:58Z|undergraduate thesis - Human Connectome Project data",
    ]),
    "migalkin": ("user", [
        "migalkin/NodePiece|Python|144|21|0|2026-05-07T05:40:02Z|Compositional and Parameter-Efficient Representations for Large KGs",
        "migalkin/StarE|Python|89|16|1|2026-04-16T14:12:45Z|EMNLP 2020: Message Passing for Hyper-Relational Knowledge Graphs",
        "migalkin/kgcourse2021|HTML|25|9|0|2026-02-16T05:16:08Z|Materials for Knowledge Graphs course",
        "migalkin/NBFNet_mlx|Python|10|1|1|2026-03-11T01:31:21Z|Neural Bellman-Ford networks in MLX for Apple Silicon",
        "migalkin/RWL|Python|8|1|0|2026-05-28T20:19:20Z|Weisfeiler and Leman Go Relational (LOG 2022)",
        "migalkin/rambo|Rust|3|0|1|2023-02-28T16:37:22Z|",
    ]),
    "DJedamski": ("user", [
        "DJedamski/kaggle_ncaa18|Jupyter Notebook|0|0|0|2018-02-26T16:33:24Z|Code for NCAA March Madness competition 2018",
        "DJedamski/School|R|1|1|0|2023-04-21T01:42:33Z|A couple small projects from grad school",
        "DJedamski/Getting-and-Cleaning-Data|R|1|0|0|2023-04-21T01:42:34Z|Coursera Project",
        "DJedamski/Kaggle|R|1|0|0|2023-04-21T01:42:35Z|",
        "DJedamski/EDA|R|0|0|0|2014-11-09T17:00:39Z|Coursera Project",
    ]),
    "wasita": ("user", [
        "wasita/wasita.github.io|Svelte|1|0|8|2026-06-15T20:14:23Z|personal website",
        "wasita/wm-cv|Svelte|0|0|0|2026-05-13T05:29:08Z|Academic CV written as a single page web app",
        "wasita/vocoder|JavaScript|0|0|0|2026-05-06T05:14:03Z|",
        "wasita/ch3-lib|Typst|0|0|0|2026-04-12T04:03:22Z|",
        "wasita/magic-garden|Python|2|1|1|2026-04-22T21:16:43Z|a bot for the magic garden discord activity game",
        "wasita/send2kobo|TypeScript|1|0|0|2026-05-19T02:59:26Z|Website for sending books to your kobo e-reader",
        "wasita/wins-search|CSS|1|0|0|2023-06-03T19:01:11Z|Women in Network Science member list website",
    ]),
    "kristinezheng": ("user", [
        "kristinezheng/kristinezheng.github.io|HTML|0|0|0|2026-06-07T22:53:10Z|",
        "kristinezheng/lookit-jenga|Jupyter Notebook|0|0|0|2024-05-16T18:29:05Z|Lookit study for 9.85",
        "kristinezheng/auditory-illusion|CSS|0|0|0|2022-03-07T02:57:44Z|9.35 spring 2022 auditory illusion",
        "kristinezheng/graph_example|Python|0|0|0|2021-10-08T07:29:53Z|",
        "kristinezheng/Green-Machine|Python|0|0|0|2021-09-19T05:33:04Z|HackMIT 2021: Sustainability Track",
    ]),
    "M1shaaa": ("user", [
        "M1shaaa/M1shaaa||0|0|0|2026-02-04T19:32:04Z|Config files for my GitHub profile",
        "M1shaaa/lab-bookshelf-|TypeScript|0|0|0|2024-12-31T05:11:18Z|",
        "M1shaaa/rosie-s-study-3-lookit-project||0|0|0|2024-11-04T22:15:39Z|",
        "M1shaaa/Python-Lookit-Uploads|Python|0|0|0|2024-02-15T22:59:37Z|random projects",
        "M1shaaa/Classes||0|0|0|2023-12-06T18:20:27Z|",
        "M1shaaa/Yale-Work|HTML|0|0|0|2023-12-06T18:33:14Z|",
        "M1shaaa/MNIST-Classifier||0|0|0|2023-11-28T06:10:47Z|",
        "M1shaaa/Lookit-Demo||0|0|0|2023-04-10T02:44:01Z|",
    ]),
    "AustinCStone": ("user", [
        "AustinCStone/TextGAN|Python|92|30|5|2025-03-03T13:26:32Z|A generative adversarial network for text generation",
        "AustinCStone/StereoVisionMRF|Python|11|4|0|2026-04-01T07:39:41Z|Recover 3D geometry from stereo images",
        "AustinCStone/EpsteinSearch|Python|0|0|0|2026-02-11T01:10:57Z|",
        "AustinCStone/bmforkupdate|Python|0|0|0|2025-05-09T04:50:16Z|",
        "AustinCStone/bmfork|Python|0|0|1|2025-05-09T04:18:54Z|",
        "AustinCStone/SpectralClustering|Python|3|2|0|2021-04-16T08:46:36Z|Implementing spectral clustering",
        "AustinCStone/StructureFromMotion|Python|1|0|0|2019-04-26T19:43:12Z|Recover 3D geometry from videos",
        "AustinCStone/logisticRegressionHaskell|Haskell|1|0|0|2018-02-02T13:34:28Z|Logistic regression done in Haskell",
    ]),
}

# ── INSERT GITHUB DATA ───────────────────────────────────────────────────────
print("Inserting GitHub repo snapshots...")
inc_id = 1
repo_id = 1

for org_user, (src_type, repos) in GITHUB_DATA.items():
    trit, color, name = gf3(inc_id)
    snap_hash = hashlib.md5(f"{org_user}{datetime.utcnow().isoformat()}".encode()).hexdigest()[:12]
    event = "org_snapshot" if src_type == "org" else "user_snapshot"

    sql = f"""INSERT INTO world_increments VALUES (
      {inc_id}, now(), {trit}, '{color}', '{name}', '{src_type}',
      '{org_user}', '{event}', '', '{org_user}', '{snap_hash}'
    );"""
    duckdb_exec(sql)

    for repo_line in repos:
        parts = repo_line.split("|")
        if len(parts) < 7:
            continue
        full_name = parts[0].replace("'", "''")
        language = parts[1].replace("'", "''")
        stars = int(parts[2]) if parts[2].isdigit() else 0
        forks = int(parts[3]) if parts[3].isdigit() else 0
        issues = int(parts[4]) if parts[4].isdigit() else 0
        pushed = parts[5]
        desc = parts[6].replace("'", "''")[:200] if len(parts) > 6 else ""
        repo_name = full_name.split("/")[1] if "/" in full_name else full_name

        sql = f"""INSERT INTO repo_snapshots VALUES (
          {repo_id}, now(), {inc_id}, '{org_user}', '{repo_name}', '{full_name}',
          '{language}', {stars}, {forks}, {issues}, '{pushed}', '{desc}'
        );"""
        duckdb_exec(sql)
        repo_id += 1

    inc_id += 1

print(f"  Inserted {inc_id-1} increments, {repo_id-1} repo snapshots")

# ── APTOS WALLET BALANCES ────────────────────────────────────────────────────
print("\nQuerying Aptos wallet balances...")

APTOS_ADDRS = {
    "alice": "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b",
    "bob":   "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d",
    "A": "0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a",
    "B": "0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13",
    "C": "0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e",
    "D": "0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1",
    "E": "0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36",
    "F": "0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71",
    "G": "0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32",
    "H": "0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f",
    "I": "0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9",
    "J": "0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54",
    "K": "0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4",
    "L": "0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9",
    "M": "0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9",
    "N": "0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c",
    "O": "0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d",
    "P": "0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948",
    "Q": "0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9",
    "R": "0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10",
    "S": "0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386",
    "T": "0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588",
    "U": "0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956",
    "V": "0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3",
    "W": "0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0",
    "X": "0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d",
    "Y": "0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4",
    "Z": "0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c",
}

APTOS_URL = "https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore%3C0x1::aptos_coin::AptosCoin%3E"

aptos_results = {}
for world, addr in APTOS_ADDRS.items():
    try:
        r = subprocess.run(
            ["curl", "-s", "--max-time", "10", APTOS_URL.format(addr=addr)],
            capture_output=True, text=True, timeout=15
        )
        data = json.loads(r.stdout)
        val = int(data.get("data", {}).get("coin", {}).get("value", 0))
        apt = val / 1e8
        aptos_results[world] = (addr, apt)
        print(f"  {world}: {apt:.6f} APT")
    except Exception as e:
        aptos_results[world] = (addr, -1.0)
        print(f"  {world}: ERROR ({type(e).__name__})")
    time.sleep(1)

# Insert Aptos data
print("Inserting Aptos snapshots...")
for world, (addr, bal) in aptos_results.items():
    sql = f"INSERT INTO aptos_snapshots VALUES (now(), '{world}', '{addr}', {bal});"
    duckdb_exec(sql)

# ── MULTISIG PROBES ──────────────────────────────────────────────────────────
print("\nProbing multisig contracts...")

MULTISIG = {
    "A-B": "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",
    "A-G": "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",
    "Y-Z": "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",
    "S-T": "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",
    "V-W": "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",
}

MULTISIG_URL = "https://fullnode.mainnet.aptoslabs.com/v1/view"

for pair, addr in MULTISIG.items():
    try:
        payload = json.dumps({
            "function": "0x1::multisig_account::num_signatures_required",
            "type_arguments": [],
            "arguments": [addr]
        })
        r = subprocess.run(
            ["curl", "-s", "--max-time", "10", "-X", "POST",
             "-H", "Content-Type: application/json",
             "-d", payload, MULTISIG_URL],
            capture_output=True, text=True, timeout=15
        )
        data = json.loads(r.stdout)
        if isinstance(data, list) and len(data) > 0:
            sigs = int(data[0])
            healthy = sigs > 0
            print(f"  {pair} ({addr[:10]}...): {sigs} sigs required, healthy={healthy}")
            sql = f"INSERT INTO multisig_probes VALUES (now(), '{pair}', '{addr}', {sigs}, {str(healthy).upper()});"
        else:
            print(f"  {pair}: unexpected response: {str(data)[:100]}")
            sql = f"INSERT INTO multisig_probes VALUES (now(), '{pair}', '{addr}', -1, FALSE);"
        duckdb_exec(sql)
    except Exception as e:
        print(f"  {pair}: ERROR ({e})")
        sql = f"INSERT INTO multisig_probes VALUES (now(), '{pair}', '{addr}', -1, FALSE);"
        duckdb_exec(sql)
    time.sleep(1)

# ── MNX MARKETS ─────────────────────────────────────────────────────────────
print("\nProbing MNX markets...")

MNX_ENDPOINTS = [
    "https://testnet.mnx.fi/api/markets",
    "https://testnet.mnx.fi/api/v1/markets",
    "https://testnet.mnx.fi/api/tickers",
    "https://testnet.mnx.fi/markets",
]

mnx_data = None
for url in MNX_ENDPOINTS:
    try:
        r = subprocess.run(
            ["curl", "-s", "--max-time", "10", url],
            capture_output=True, text=True, timeout=15
        )
        if r.stdout.strip() and r.stdout.strip().startswith(("{", "[")):
            mnx_data = json.loads(r.stdout)
            print(f"  Got MNX data from {url}")
            break
        else:
            print(f"  {url}: no JSON (got {len(r.stdout)} chars)")
    except Exception as e:
        print(f"  {url}: ERROR ({e})")

if mnx_data:
    items = mnx_data if isinstance(mnx_data, list) else mnx_data.get("markets", mnx_data.get("data", []))
    for item in items[:20]:
        ticker = str(item.get("ticker", item.get("symbol", "?"))).replace("'", "''")
        name = str(item.get("name", "?")).replace("'", "''")
        category = str(item.get("category", "?")).replace("'", "''")
        price = float(item.get("price", item.get("last", 0)) or 0)
        change_pct = float(item.get("change_pct", item.get("change_24h", 0)) or 0)
        sql = f"INSERT INTO mnx_snapshots VALUES (now(), '{ticker}', '{name}', '{category}', {price}, {change_pct});"
        duckdb_exec(sql)
        print(f"  MNX: {ticker} ${price:.4f} ({change_pct:+.2f}%)")
else:
    print("  MNX testnet unavailable — SPA or no public API endpoint")
    # Insert a placeholder
    duckdb_exec("INSERT INTO mnx_snapshots VALUES (now(), 'N/A', 'MNX testnet unavailable', 'error', 0, 0);")

# ── SUMMARY ──────────────────────────────────────────────────────────────────
print("\nGenerating summary stats...")
total_repos = duckdb_exec("SELECT COUNT(*) FROM repo_snapshots;").strip()
total_stars = duckdb_exec("SELECT SUM(stars) FROM repo_snapshots;").strip()
aptos_rows = duckdb_exec("SELECT world, balance_apt FROM aptos_snapshots ORDER BY world;").strip()
multisig_rows = duckdb_exec("SELECT pair, sigs_required, healthy FROM multisig_probes ORDER BY pair;").strip()

print(f"  Repos: {total_repos}")
print(f"  Total stars: {total_stars}")

print("\nDone! DuckDB populated.")
