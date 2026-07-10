#!/usr/bin/env python3
"""Build world-increment DuckDB from collected data."""
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

# GF3 color chain
def gf3(id_val):
    t = id_val % 3
    if t == 0: return (0, "#d3869b", "ERGODIC")
    if t == 1: return (1, "#b8bb26", "PLUS")
    return (-1, "#cc241d", "MINUS")

# ===================== GITHUB REPO SNAPSHOTS =====================
repos = [
  # plurigrid org (pages 1-4, 103 total)
  {"org": "plurigrid", "full_name": "plurigrid/asi", "language": "HTML", "stars": 30, "forks": 9, "open_issues": 4, "pushed_at": "2026-07-10T09:47:39Z", "description": "everything is topological chemputer!"},
  {"org": "plurigrid", "full_name": "plurigrid/gorj", "language": "Clojure", "stars": 1, "forks": 0, "open_issues": 1099, "pushed_at": "2026-07-10T12:33:49Z", "description": "forj + Rama topology nREPL routing + GF(3) gay trit coloring for compositional open game REPL orchestration"},
  {"org": "plurigrid", "full_name": "plurigrid/shrimp", "language": None, "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-07-03T01:24:20Z", "description": "Jank worked example: shrimp"},
  {"org": "plurigrid", "full_name": "plurigrid/place", "language": "TeX", "stars": 1, "forks": 1, "open_issues": 12, "pushed_at": "2026-07-07T03:10:28Z", "description": None},
  {"org": "plurigrid", "full_name": "plurigrid/eirobri", "language": "Clojure", "stars": 0, "forks": 0, "open_issues": 30, "pushed_at": "2026-06-30T02:23:56Z", "description": "EiRoBri replay world"},
  {"org": "plurigrid", "full_name": "plurigrid/nash-portal", "language": "Rust", "stars": 2, "forks": 3, "open_issues": 1, "pushed_at": "2026-05-19T01:49:59Z", "description": "NASH token TUI in the browser"},
  {"org": "plurigrid", "full_name": "plurigrid/zig-syrup", "language": "Zig", "stars": 2, "forks": 2, "open_issues": 0, "pushed_at": "2026-04-30T03:52:16Z", "description": "High-performance Zig implementation of OCapN Syrup"},
  {"org": "plurigrid", "full_name": "plurigrid/asi-skills", "language": "Julia", "stars": 3, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-26T08:09:26Z", "description": "69 skills with Galois Hole Type accessibility"},
  {"org": "plurigrid", "full_name": "plurigrid/bci-blue-share", "language": "JavaScript", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-26T07:08:03Z", "description": "BCI signal infrastructure"},
  {"org": "plurigrid", "full_name": "plurigrid/nanoclj-zig", "language": "Zig", "stars": 1, "forks": 1, "open_issues": 20, "pushed_at": "2026-04-25T07:29:09Z", "description": "NaN-boxed Clojure interpreter in Zig 0.15"},
  {"org": "plurigrid", "full_name": "plurigrid/spi-race", "language": "Swift", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-21T19:31:56Z", "description": "Splitmix Parallel Integrity"},
  {"org": "plurigrid", "full_name": "plurigrid/reafference", "language": "HTML", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-16T05:21:49Z", "description": "Reafference adaptation workspace"},
  {"org": "plurigrid", "full_name": "plurigrid/web-browser", "language": "Rust", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-10T02:54:47Z", "description": "web-browser"},
  {"org": "plurigrid", "full_name": "plurigrid/vivarium", "language": "Clojure", "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-08T08:38:37Z", "description": None},
  {"org": "plurigrid", "full_name": "plurigrid/flowglad-rs", "language": "Rust", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-08T07:56:15Z", "description": None},
  {"org": "plurigrid", "full_name": "plurigrid/tree-sitter-nanoclj-zig", "language": "C", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-04T07:48:21Z", "description": "Tree-sitter grammar for nanoclj-zig"},
  {"org": "plurigrid", "full_name": "plurigrid/forester", "language": "XSLT", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-03-30T01:32:26Z", "description": "CatColab mathematical documentation forest"},
  {"org": "plurigrid", "full_name": "plurigrid/gatomic", "language": "Clojure", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-03-30T00:54:48Z", "description": "Deterministic color identity store"},
  {"org": "plurigrid", "full_name": "plurigrid/blue", "language": "TeX", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-03-29T23:06:32Z", "description": None},
  {"org": "plurigrid", "full_name": "plurigrid/red", "language": None, "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-03-29T22:58:46Z", "description": None},
  {"org": "plurigrid", "full_name": "plurigrid/nblm-flashcards", "language": "Hy", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-03-26T08:23:01Z", "description": "NotebookLM Enterprise flashcard pipeline"},
  {"org": "plurigrid", "full_name": "plurigrid/gemini-agent", "language": "Python", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-02-19T06:39:16Z", "description": None},
  {"org": "plurigrid", "full_name": "plurigrid/graded-optic", "language": "Haskell", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-02-08T16:10:16Z", "description": "Semiring-graded bidirectional processes"},
  {"org": "plurigrid", "full_name": "plurigrid/json-canvas", "language": None, "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-02-06T06:50:57Z", "description": "JSON Canvas: Real-time interaction data capture"},
  {"org": "plurigrid", "full_name": "plurigrid/shepherd", "language": "Scheme", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-01-23T07:47:28Z", "description": "Spritely Shepherd"},
  {"org": "plurigrid", "full_name": "plurigrid/goblinshare", "language": "Scheme", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-01-23T07:47:12Z", "description": "P2P filesharing demo for Goblins"},
  {"org": "plurigrid", "full_name": "plurigrid/magenc", "language": "Scheme", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-01-23T07:47:11Z", "description": "Magenc Magnet URIs"},
  {"org": "plurigrid", "full_name": "plurigrid/hoot", "language": "Scheme", "stars": 0, "forks": 0, "open_issues": 1, "pushed_at": "2026-01-23T07:47:10Z", "description": "Spritely Hoot - Scheme to WebAssembly compiler"},
  {"org": "plurigrid", "full_name": "plurigrid/leprechauns", "language": "Racket", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-01-23T07:46:46Z", "description": "Spritely Goblins + Gay.jl semantic colors"},
  {"org": "plurigrid", "full_name": "plurigrid/spritely-semantic-colors", "language": None, "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-01-23T07:38:32Z", "description": "Deterministic color mappings for Spritely/Goblins"},
  # page 2
  {"org": "plurigrid", "full_name": "plurigrid/gay-tofu", "language": "HTML", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-01-08T15:14:38Z", "description": "Low-discrepancy color sequences for visual TOFU authentication"},
  {"org": "plurigrid", "full_name": "plurigrid/lazygay", "language": "Go", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-01-08T14:19:29Z", "description": "lazygit fork with Gay.jl deterministic commit coloring"},
  {"org": "plurigrid", "full_name": "plurigrid/gay-terminal", "language": "Rust", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-01-08T14:19:27Z", "description": "Terminal ANSI coloring with Gay.jl"},
  {"org": "plurigrid", "full_name": "plurigrid/gay-go", "language": "Go", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-01-08T14:19:26Z", "description": "Go implementation of Gay.jl deterministic coloring"},
  {"org": "plurigrid", "full_name": "plurigrid/gay-rs", "language": "Rust", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-01-08T14:19:26Z", "description": "Rust crate for Gay.jl deterministic coloring"},
  {"org": "plurigrid", "full_name": "plurigrid/lazybjj", "language": "Rust", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-01-08T14:19:32Z", "description": "TUI for jj with Gay.jl GF(3) coloring"},
  {"org": "plurigrid", "full_name": "plurigrid/agent-o-rama", "language": "Clojure", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-01-01T23:39:06Z", "description": None},
  {"org": "plurigrid", "full_name": "plurigrid/aptos-wallet-ruby", "language": "Ruby", "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2025-10-24T09:25:13Z", "description": None},
  {"org": "plurigrid", "full_name": "plurigrid/duck-kanban", "language": "Rust", "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2025-10-24T09:24:59Z", "description": "Duck intelligence kanban system"},
  {"org": "plurigrid", "full_name": "plurigrid/ontology", "language": "JavaScript", "stars": 8, "forks": 9, "open_issues": 16, "pushed_at": "2026-05-09T04:20:49Z", "description": "autopoietic ergodicity and embodied gradualism"},
  {"org": "plurigrid", "full_name": "plurigrid/Plurigraph", "language": "JavaScript", "stars": 3, "forks": 5, "open_issues": 4, "pushed_at": "2026-05-12T03:19:41Z", "description": "Plurigrid knowledge base for use with Obsidian.md"},
  {"org": "plurigrid", "full_name": "plurigrid/act", "language": "Python", "stars": 3, "forks": 1, "open_issues": 4, "pushed_at": "2024-11-25T09:36:59Z", "description": "building blocks for cognitive category theory"},
  {"org": "plurigrid", "full_name": "plurigrid/StochFlow", "language": "Python", "stars": 4, "forks": 1, "open_issues": 0, "pushed_at": "2024-08-15T02:58:54Z", "description": "Python library for stochastic interpolant models"},
  {"org": "plurigrid", "full_name": "plurigrid/microworlds", "language": "Rust", "stars": 3, "forks": 5, "open_issues": 3, "pushed_at": "2024-03-14T00:12:46Z", "description": "👽"},
  {"org": "plurigrid", "full_name": "plurigrid/vcg-auction", "language": "Rust", "stars": 7, "forks": 3, "open_issues": 1, "pushed_at": "2025-12-16T12:32:02Z", "description": "a simple contract that performs a VCG auction"},
  {"org": "plurigrid", "full_name": "plurigrid/agent", "language": "Python", "stars": 5, "forks": 1, "open_issues": 6, "pushed_at": "2024-10-16T11:33:13Z", "description": "Framework for agency amplification"},
  {"org": "plurigrid", "full_name": "plurigrid/birbs", "language": "C++", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2024-11-20T09:51:35Z", "description": "Build native CosmWasm apps w/ Dart and Flutter"},
  {"org": "plurigrid", "full_name": "plurigrid/grid", "language": "TypeScript", "stars": 2, "forks": 1, "open_issues": 1, "pushed_at": "2023-01-31T11:42:52Z", "description": "Plurigrid Testnet #0: Edith Clarke"},
  # kubeflow org (top 20)
  {"org": "kubeflow", "full_name": "kubeflow/kubeflow", "language": None, "stars": 15771, "forks": 2685, "open_issues": 0, "pushed_at": "2026-07-10T11:32:17Z", "description": "Machine Learning Toolkit for Kubernetes"},
  {"org": "kubeflow", "full_name": "kubeflow/trainer", "language": "Go", "stars": 2134, "forks": 983, "open_issues": 144, "pushed_at": "2026-07-10T12:20:17Z", "description": "Distributed AI Model Training and LLM Fine-Tuning on Kubernetes"},
  {"org": "kubeflow", "full_name": "kubeflow/pipelines", "language": "Python", "stars": 4169, "forks": 2031, "open_issues": 422, "pushed_at": "2026-07-09T18:36:07Z", "description": "Machine Learning Pipelines for Kubeflow"},
  {"org": "kubeflow", "full_name": "kubeflow/spark-operator", "language": "Python", "stars": 3136, "forks": 1500, "open_issues": 108, "pushed_at": "2026-07-09T08:56:50Z", "description": "Kubernetes operator for managing Apache Spark"},
  {"org": "kubeflow", "full_name": "kubeflow/katib", "language": "Python", "stars": 1689, "forks": 532, "open_issues": 111, "pushed_at": "2026-07-09T13:35:36Z", "description": "Automated Machine Learning on Kubernetes"},
  {"org": "kubeflow", "full_name": "kubeflow/arena", "language": "Go", "stars": 815, "forks": 195, "open_issues": 49, "pushed_at": "2026-07-08T08:12:14Z", "description": "A CLI for Kubeflow"},
  {"org": "kubeflow", "full_name": "kubeflow/kale", "language": "Python", "stars": 695, "forks": 157, "open_issues": 45, "pushed_at": "2026-07-10T12:56:54Z", "description": "Kubeflow's superfood for Data Scientists"},
  {"org": "kubeflow", "full_name": "kubeflow/mcp-apache-spark-history-server", "language": "Python", "stars": 182, "forks": 65, "open_issues": 19, "pushed_at": "2026-07-07T06:27:43Z", "description": "MCP Server for Apache Spark History Server"},
  {"org": "kubeflow", "full_name": "kubeflow/hub", "language": "Go", "stars": 177, "forks": 187, "open_issues": 33, "pushed_at": "2026-07-10T13:28:51Z", "description": "Model Registry for ML models"},
  {"org": "kubeflow", "full_name": "kubeflow/sdk", "language": "Python", "stars": 123, "forks": 192, "open_issues": 149, "pushed_at": "2026-07-10T11:34:13Z", "description": "Universal Python SDK to run AI workloads on Kubernetes"},
  # TeglonLabs
  {"org": "TeglonLabs", "full_name": "TeglonLabs/jank-crane", "language": "C++", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-06-08T19:03:37Z", "description": "crane-jank converged-IR hub"},
  {"org": "TeglonLabs", "full_name": "TeglonLabs/mathpix-gem", "language": "Ruby", "stars": 2, "forks": 0, "open_issues": 11, "pushed_at": "2026-01-01T12:13:16Z", "description": "Transform mathematical images to LaTeX"},
  {"org": "TeglonLabs", "full_name": "TeglonLabs/coin-flip-mcp", "language": "JavaScript", "stars": 0, "forks": 2, "open_issues": 1, "pushed_at": "2025-03-16T01:31:45Z", "description": "MCP server for flipping coins"},
  {"org": "TeglonLabs", "full_name": "TeglonLabs/monad-mcp-server", "language": None, "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2025-05-14T17:53:01Z", "description": "Monad MCP Server"},
  {"org": "TeglonLabs", "full_name": "TeglonLabs/topoi", "language": "Python", "stars": 0, "forks": 0, "open_issues": 1, "pushed_at": "2025-01-24T06:47:38Z", "description": None},
  # bmorphism user (top repos)
  {"org": "bmorphism", "full_name": "bmorphism/satreadout", "language": "HTML", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-06-20T13:05:44Z", "description": "Machine-checked saturating non-Riemannian perceptual readout"},
  {"org": "bmorphism", "full_name": "bmorphism/Gay.jl", "language": "Julia", "stars": 2, "forks": 1, "open_issues": 187, "pushed_at": "2026-06-20T14:21:55Z", "description": "Wide-gamut color sampling with splittable determinism"},
  {"org": "bmorphism", "full_name": "bmorphism/ocaml-mcp-sdk", "language": "OCaml", "stars": 61, "forks": 2, "open_issues": 0, "pushed_at": "2026-05-08T16:50:34Z", "description": "OCaml SDK for Model Context Protocol"},
  {"org": "bmorphism", "full_name": "bmorphism/anti-bullshit-mcp-server", "language": "JavaScript", "stars": 23, "forks": 7, "open_issues": 1, "pushed_at": "2026-02-05T15:46:59Z", "description": "MCP server for analyzing claims"},
  {"org": "bmorphism", "full_name": "bmorphism/shitcoin", "language": "Python", "stars": 5, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-08T08:07:17Z", "description": "gets denom for cw20 assets"},
  {"org": "bmorphism", "full_name": "bmorphism/open-location-code-zig", "language": "Zig", "stars": 3, "forks": 0, "open_issues": 0, "pushed_at": "2026-03-24T21:54:01Z", "description": "Open Location Code for Zig"},
  {"org": "bmorphism", "full_name": "bmorphism/flox-mcp-bb", "language": "Clojure", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-06-05T17:53:47Z", "description": "Open-source MCP server for Flox"},
  # zubyul user
  {"org": "zubyul", "full_name": "zubyul/voice-observatory", "language": "Python", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-24T05:56:20Z", "description": "Passive macOS TUI observing voice-download pathways"},
  {"org": "zubyul", "full_name": "zubyul/ghostel-emacs-worlds", "language": "GLSL", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-24T00:21:00Z", "description": "Ghostty config + ghostel family + emacs-mods"},
  {"org": "zubyul", "full_name": "zubyul/big-bad-plurigrid-quiz", "language": "Emacs Lisp", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-09T18:51:35Z", "description": "27 flashcards from bmorphism/plurigrid/zubyul activity"},
  {"org": "zubyul", "full_name": "zubyul/gay-world", "language": "Python", "stars": 1, "forks": 1, "open_issues": 0, "pushed_at": "2026-04-05T06:54:03Z", "description": "Goblin world builder"},
  {"org": "zubyul", "full_name": "zubyul/Gay.jl", "language": "Julia", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-03-28T11:30:07Z", "description": "Wide-gamut color sampling with splittable determinism"},
  {"org": "zubyul", "full_name": "zubyul/kinesis-kb360pro", "language": "Python", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-03-26T10:29:44Z", "description": "Claude Code skill for Kinesis Advantage360 Pro keyboard"},
  # migalkin social graph
  {"org": "migalkin", "full_name": "migalkin/NodePiece", "language": "Python", "stars": 144, "forks": 21, "open_issues": 0, "pushed_at": "2026-05-07T05:40:02Z", "description": "Compositional and Parameter-Efficient Representations for Large Knowledge Graphs"},
  {"org": "migalkin", "full_name": "migalkin/StarE", "language": "Python", "stars": 89, "forks": 16, "open_issues": 1, "pushed_at": "2026-04-16T14:12:45Z", "description": "Message Passing for Hyper-Relational Knowledge Graphs"},
  {"org": "migalkin", "full_name": "migalkin/NBFNet_mlx", "language": "Python", "stars": 10, "forks": 1, "open_issues": 1, "pushed_at": "2026-03-11T01:31:21Z", "description": "Neural Bellman-Ford networks in MLX"},
  {"org": "migalkin", "full_name": "migalkin/kgcourse2021", "language": "HTML", "stars": 25, "forks": 9, "open_issues": 0, "pushed_at": "2026-02-16T05:16:08Z", "description": "Knowledge Graphs course materials"},
  # DJedamski social graph
  {"org": "DJedamski", "full_name": "DJedamski/kaggle_ncaa18", "language": "Jupyter Notebook", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2018-02-26T16:33:24Z", "description": "Code for NCAA March Madness competition (2018)"},
  {"org": "DJedamski", "full_name": "DJedamski/Kaggle", "language": None, "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2023-04-21T01:42:35Z", "description": None},
  # wasita social graph
  {"org": "wasita", "full_name": "wasita/wasita.github.io", "language": "Svelte", "stars": 1, "forks": 0, "open_issues": 8, "pushed_at": "2026-07-06T23:51:09Z", "description": "personal website"},
  {"org": "wasita", "full_name": "wasita/magic-garden", "language": "Python", "stars": 2, "forks": 1, "open_issues": 1, "pushed_at": "2026-04-22T21:16:43Z", "description": "bot for magic garden discord"},
  {"org": "wasita", "full_name": "wasita/send2kobo", "language": "TypeScript", "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2026-05-19T02:59:26Z", "description": "Website for sending books to kobo e-reader"},
  # kristinezheng
  {"org": "kristinezheng", "full_name": "kristinezheng/kristinezheng.github.io", "language": "HTML", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-07-01T20:57:48Z", "description": None},
  # M1shaaa
  {"org": "M1shaaa", "full_name": "M1shaaa/M1shaaa", "language": None, "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-02-04T19:32:04Z", "description": "Config files for my GitHub profile"},
  {"org": "M1shaaa", "full_name": "M1shaaa/lab-bookshelf-", "language": "TypeScript", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2024-12-31T05:11:18Z", "description": None},
  # AustinCStone
  {"org": "AustinCStone", "full_name": "AustinCStone/EpsteinSearch", "language": "Python", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-02-11T01:10:57Z", "description": None},
  {"org": "AustinCStone", "full_name": "AustinCStone/TextGAN", "language": "Python", "stars": 92, "forks": 30, "open_issues": 5, "pushed_at": "2025-03-03T13:26:32Z", "description": "A generative adversarial network for text generation"},
  {"org": "AustinCStone", "full_name": "AustinCStone/StereoVisionMRF", "language": "Python", "stars": 11, "forks": 4, "open_issues": 0, "pushed_at": "2026-04-01T07:39:41Z", "description": "Recover 3D geometry from stereo images"},
]

# Insert world_increments and repo_snapshots
for i, repo in enumerate(repos):
    inc_id = i + 1
    trit, color, name = gf3(inc_id)
    org = repo["org"]
    full_name = repo["full_name"]
    repo_name = full_name.split("/")[1]
    snap_hash = hex(hash(full_name) & 0xFFFFFFFF)[2:]

    con.execute("""
        INSERT INTO world_increments (id, gf3_trit, gf3_color, gf3_name, source_type, source_name, event_type, repo_name, actor, snapshot_hash)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [inc_id, trit, color, name, "github_repo", org, "repo_snapshot", repo_name, org, snap_hash])

    con.execute("""
        INSERT INTO repo_snapshots (id, increment_id, org_or_user, repo_name, full_name, language, stars, forks, open_issues, pushed_at, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [inc_id, inc_id, org, repo_name, full_name,
          repo.get("language"), repo.get("stars", 0), repo.get("forks", 0),
          repo.get("open_issues", 0), repo.get("pushed_at"), repo.get("description")])

print(f"Inserted {len(repos)} repo snapshots")

# ===================== APTOS SNAPSHOTS =====================
aptos_worlds = [
    ("alice", "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b", 0.0),
    ("bob",   "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d", 0.0),
    ("A",     "0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a", 0.0),
    ("B",     "0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13", 0.0),
    ("C",     "0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e", 0.0),
    ("D",     "0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1", 0.0),
    ("E",     "0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36", 0.0),
    ("F",     "0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71", 0.0),
    ("G",     "0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32", 0.0),
    ("H",     "0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f", 0.0),
    ("I",     "0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9", 0.0),
    ("J",     "0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54", 0.0),
    ("K",     "0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4", 0.0),
    ("L",     "0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9", 0.0),
    ("M",     "0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9", 0.0),
    ("N",     "0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c", 0.0),
    ("O",     "0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d", 0.0),
    ("P",     "0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948", 0.0),
    ("Q",     "0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9", 0.0),
    ("R",     "0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10", 0.0),
    ("S",     "0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386", 0.0),
    ("T",     "0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588", 0.0),
    ("U",     "0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956", 0.0),
    ("V",     "0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3", 0.0),
    ("W",     "0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0", 0.0),
    ("X",     "0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d", 0.0),
    ("Y",     "0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4", 0.0),
    ("Z",     "0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c", 0.0),
]
for world, addr, bal in aptos_worlds:
    con.execute("INSERT INTO aptos_snapshots (world, address, balance_apt) VALUES (?, ?, ?)",
                [world, addr, bal])
print(f"Inserted {len(aptos_worlds)} Aptos snapshots")

# ===================== MULTISIG PROBES =====================
multisigs = [
    ("A-B",  "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2, True),
    ("A-G",  "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2, True),
    ("Y-Z",  "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2, True),
    ("S-T",  "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2, True),
    ("V-W",  "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2, True),
]
for pair, addr, sigs, healthy in multisigs:
    con.execute("INSERT INTO multisig_probes (pair, address, sigs_required, healthy) VALUES (?, ?, ?, ?)",
                [pair, addr, sigs, healthy])
print("Inserted 5 multisig probes")

# ===================== MNX SNAPSHOTS =====================
# MNX testnet unavailable (requires Vercel authentication) - no rows inserted
print("MNX: unavailable (Vercel auth required)")

# Verify counts
print("\n=== Table counts ===")
for tbl in ["world_increments", "repo_snapshots", "aptos_snapshots", "multisig_probes", "mnx_snapshots"]:
    n = con.execute(f"SELECT COUNT(*) FROM {tbl}").fetchone()[0]
    print(f"  {tbl}: {n}")

# Top repos by stars
print("\n=== Top 10 repos by stars ===")
rows = con.execute("""
    SELECT full_name, org_or_user, stars, language, pushed_at
    FROM repo_snapshots ORDER BY stars DESC LIMIT 10
""").fetchall()
for r in rows:
    print(f"  {r[0]} ({r[1]}) ⭐{r[2]} [{r[3]}] pushed:{r[4][:10] if r[4] else 'N/A'}")

# GF3 distribution
print("\n=== GF(3) trit distribution ===")
rows = con.execute("""
    SELECT gf3_trit, gf3_color, gf3_name, COUNT(*) as cnt
    FROM world_increments GROUP BY gf3_trit, gf3_color, gf3_name ORDER BY gf3_trit
""").fetchall()
for r in rows:
    print(f"  trit={r[0]} {r[1]} {r[2]}: {r[3]} increments")

con.close()
print("\nDone. DB written to:", DB_PATH)
