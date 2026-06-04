#!/usr/bin/env python3
"""Build world-increment DuckDB from collected GitHub + Aptos snapshots."""

import duckdb
import json
import os
import hashlib
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
CREATE SEQUENCE IF NOT EXISTS increment_seq START 1
""")
con.execute("""
CREATE SEQUENCE IF NOT EXISTS repo_seq START 1
""")
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

def gf3(idx):
    t = idx % 3
    if t == 0:
        return (0, "#d3869b", "ERGODIC")
    elif t == 1:
        return (1, "#b8bb26", "PLUS")
    else:
        return (-1, "#cc241d", "MINUS")

def snap_hash(data):
    return hashlib.sha256(str(data).encode()).hexdigest()[:16]

# --- Repo data ---
# plurigrid repos extracted (30 from search)
plurigrid_repos = [
    ("plurigrid", "zig-syrup", "plurigrid/zig-syrup", "Zig", 2, 2, 0, "2026-04-30T03:52:16Z", "High-performance Zig implementation of OCapN Syrup with CapTP"),
    ("plurigrid", "asi", "plurigrid/asi", "HTML", 18, 5, 4, "2026-04-26T08:51:41Z", "everything is topological chemputer!"),
    ("plurigrid", "nash-portal", "plurigrid/nash-portal", "Rust", 1, 2, 0, "2026-04-26T08:50:56Z", "NASH token TUI in the browser"),
    ("plurigrid", "horse", "plurigrid/horse", "TeX", 1, 1, 8, "2026-04-29T20:35:13Z", ""),
    ("plurigrid", "asi-skills", "plurigrid/asi-skills", "Julia", 3, 1, 0, "2026-04-26T08:09:26Z", "69 skills with Galois Hole Type accessibility"),
    ("plurigrid", "bci-blue-share", "plurigrid/bci-blue-share", "JavaScript", 0, 0, 0, "2026-04-26T07:08:03Z", "BCI signal infrastructure"),
    ("plurigrid", "nanoclj-zig", "plurigrid/nanoclj-zig", "Zig", 1, 1, 20, "2026-04-25T07:29:09Z", "NaN-boxed Clojure interpreter in Zig 0.15"),
    ("plurigrid", "spi-race", "plurigrid/spi-race", "Swift", 0, 0, 0, "2026-04-21T19:31:56Z", "Splitmix Parallel Integrity"),
    ("plurigrid", "reafference", "plurigrid/reafference", "HTML", 0, 0, 0, "2026-04-16T05:21:49Z", "Reafference adaptation workspace"),
    ("plurigrid", "gorj", "plurigrid/gorj", "Clojure", 0, 0, 68, "2026-05-05T10:16:13Z", "forj + Rama topology nREPL routing + GF(3) gay trit coloring"),
    ("plurigrid", "web-browser", "plurigrid/web-browser", "Rust", 0, 0, 0, "2026-04-10T02:54:47Z", "web-browser from prepostweb lineage"),
    ("plurigrid", "vivarium", "plurigrid/vivarium", "Clojure", 1, 0, 0, "2026-04-08T08:38:37Z", ""),
    ("plurigrid", "flowglad-rs", "plurigrid/flowglad-rs", "Rust", 0, 0, 0, "2026-04-08T07:56:15Z", ""),
    ("plurigrid", "tree-sitter-nanoclj-zig", "plurigrid/tree-sitter-nanoclj-zig", "C", 0, 0, 0, "2026-04-04T07:48:21Z", "Tree-sitter grammar for nanoclj-zig"),
    ("plurigrid", "forester", "plurigrid/forester", "XSLT", 0, 0, 0, "2026-03-30T01:32:26Z", "CatColab mathematical documentation forest"),
    ("plurigrid", "gatomic", "plurigrid/gatomic", "Clojure", 0, 0, 0, "2026-03-30T00:54:48Z", "Deterministic color identity store with sonification"),
    ("plurigrid", "blue", "plurigrid/blue", "TeX", 0, 0, 0, "2026-03-29T23:06:32Z", ""),
    ("plurigrid", "red", "plurigrid/red", "", 0, 0, 0, "2026-03-29T22:58:46Z", ""),
    ("plurigrid", "nblm-flashcards", "plurigrid/nblm-flashcards", "Hy", 0, 0, 0, "2026-03-26T08:23:01Z", "NotebookLM Enterprise flashcard pipeline"),
    ("plurigrid", "gemini-agent", "plurigrid/gemini-agent", "Python", 0, 0, 0, "2026-02-19T06:39:16Z", ""),
    ("plurigrid", "graded-optic", "plurigrid/graded-optic", "Haskell", 0, 0, 0, "2026-02-08T16:10:16Z", "Semiring-graded bidirectional processes"),
    ("plurigrid", "json-canvas", "plurigrid/json-canvas", "", 0, 0, 0, "2026-02-06T06:50:57Z", "JSON Canvas"),
    ("plurigrid", "shepherd", "plurigrid/shepherd", "Scheme", 0, 0, 0, "2026-01-23T07:47:28Z", "Spritely Shepherd"),
    ("plurigrid", "goblinshare", "plurigrid/goblinshare", "Scheme", 0, 0, 0, "2026-01-23T07:47:12Z", "P2P filesharing demo for Goblins"),
    ("plurigrid", "magenc", "plurigrid/magenc", "Scheme", 0, 0, 0, "2026-01-23T07:47:11Z", "Magenc Magnet URIs"),
    ("plurigrid", "hoot", "plurigrid/hoot", "Scheme", 0, 0, 0, "2026-01-23T07:47:10Z", "Spritely Hoot - Scheme to WebAssembly compiler"),
    ("plurigrid", "leprechauns", "plurigrid/leprechauns", "Racket", 0, 0, 0, "2026-01-23T07:46:46Z", "Spritely Goblins + Gay.jl semantic colors"),
    ("plurigrid", "spritely-semantic-colors", "plurigrid/spritely-semantic-colors", "", 0, 0, 0, "2026-01-23T07:38:32Z", "Deterministic color mappings"),
    ("plurigrid", "gay-tofu", "plurigrid/gay-tofu", "HTML", 0, 0, 0, "2026-01-08T15:14:34Z", "Low-discrepancy color sequences for visual TOFU"),
    ("plurigrid", "lazygay", "plurigrid/lazygay", "Go", 0, 0, 0, "2026-01-08T14:19:25Z", "lazygit fork with Gay.jl deterministic commit coloring"),
]

# kubeflow repos
kubeflow_repos = [
    ("kubeflow", "trainer", "kubeflow/trainer", "Go", 2096, 948, 126, "2026-05-05T10:43:07Z", "Distributed AI Model Training and LLM Fine-Tuning on Kubernetes"),
    ("kubeflow", "hub", "kubeflow/hub", "Go", 175, 178, 48, "2026-05-05T09:41:03Z", "Model Registry provides a single pane of glass for ML models"),
    ("kubeflow", "mpi-operator", "kubeflow/mpi-operator", "Go", 524, 235, 100, "2026-05-05T05:00:55Z", "Kubernetes Operator for MPI-based applications"),
    ("kubeflow", "pipelines", "kubeflow/pipelines", "Python", 4132, 1986, 489, "2026-05-04T23:46:27Z", "Machine Learning Pipelines for Kubeflow"),
    ("kubeflow", "kale", "kubeflow/kale", "Python", 684, 156, 52, "2026-05-04T12:38:49Z", "Kubeflow's superfood for Data Scientists"),
    ("kubeflow", "notebooks", "kubeflow/notebooks", "", 71, 106, 197, "2026-05-04T20:12:34Z", "Kubeflow Notebooks runs interactive development environments"),
    ("kubeflow", "community", "kubeflow/community", "Jsonnet", 196, 256, 13, "2026-05-01T13:13:03Z", "Information about the Kubeflow community"),
    ("kubeflow", "dashboard", "kubeflow/dashboard", "TypeScript", 17, 55, 71, "2026-05-04T19:43:03Z", "Kubeflow Central Dashboard"),
    ("kubeflow", "manifests", "kubeflow/manifests", "YAML", 1015, 1065, 30, "2026-04-30T08:53:03Z", "Kubeflow AI Reference Platform Deployment Manifests"),
    ("kubeflow", "sdk", "kubeflow/sdk", "Python", 111, 174, 125, "2026-04-29T20:43:32Z", "Universal Python SDK to run AI workloads on Kubernetes"),
    ("kubeflow", "kubeflow", "kubeflow/kubeflow", "", 15621, 2647, 0, "2026-04-29T13:58:28Z", "Machine Learning Toolkit for Kubernetes"),
    ("kubeflow", "website", "kubeflow/website", "HTML", 184, 919, 50, "2026-04-28T20:25:01Z", "Kubeflow Website"),
    ("kubeflow", "spark-operator", "kubeflow/spark-operator", "Python", 3123, 1482, 90, "2026-04-28T17:44:00Z", "Kubernetes operator for managing the lifecycle of Apache Spark"),
    ("kubeflow", "arena", "kubeflow/arena", "Go", 810, 191, 63, "2026-04-28T11:45:01Z", "A CLI for Kubeflow"),
    ("kubeflow", "mcp-apache-spark-history-server", "kubeflow/mcp-apache-spark-history-server", "Python", 164, 55, 22, "2026-04-28T04:41:59Z", "MCP Server and CLI for Apache Spark History Server"),
    ("kubeflow", "katib", "kubeflow/katib", "Python", 1682, 522, 122, "2026-04-14T01:21:37Z", "Automated Machine Learning on Kubernetes"),
    ("kubeflow", "examples", "kubeflow/examples", "Jsonnet", 1460, 756, 111, "2025-04-14T01:54:52Z", "A repository to host extended examples and tutorials"),
]

# TeglonLabs repos (inline)
teglon_repos = [
    ("TeglonLabs", "mathpix-gem", "TeglonLabs/mathpix-gem", "Ruby", 2, 0, 11, "2026-01-01T12:13:13Z", "Transform mathematical images to LaTeX"),
    ("TeglonLabs", "monad-mcp-server", "TeglonLabs/monad-mcp-server", "JavaScript", 0, 0, 0, "2025-05-14T11:36:14Z", "Monad MCP Server"),
    ("TeglonLabs", "topoi", "TeglonLabs/topoi", "Python", 0, 0, 1, "2025-01-24T04:49:26Z", ""),
    ("TeglonLabs", "coin-flip-mcp", "TeglonLabs/coin-flip-mcp", "JavaScript", 0, 2, 1, "2025-09-21T08:57:27Z", "MCP server for flipping coins"),
]

# bmorphism repos (40 entries)
bmorphism_repos = [
    ("bmorphism", "boxxy", "bmorphism/boxxy", "Move", 0, 1, 0, "2026-04-30T03:35:47Z", ""),
    ("bmorphism", "nanoclj-zig", "bmorphism/nanoclj-zig", "Zig", 0, 0, 0, "2026-04-25T07:29:15Z", ""),
    ("bmorphism", "Gay.jl", "bmorphism/Gay.jl", "Julia", 1, 0, 187, "2026-05-05T00:31:58Z", "Wide-gamut color sampling with splittable determinism"),
    ("bmorphism", "postweb", "bmorphism/postweb", "Go", 0, 0, 0, "2026-04-09T10:51:57Z", "postweb - evolved from prepostweb"),
    ("bmorphism", "shitcoin", "bmorphism/shitcoin", "Python", 5, 0, 0, "2026-04-08T08:07:08Z", "gets denom for cw20 assets"),
    ("bmorphism", "magic-world-org", "bmorphism/magic-world-org", "Python", 1, 0, 0, "2026-04-05T07:03:50Z", "Magic World Org (Local MLX)"),
    ("bmorphism", "zig-syrup", "bmorphism/zig-syrup", "Zig", 0, 0, 0, "2026-03-28T21:42:32Z", "Embeddable OCapN Syrup encoder/decoder in Zig"),
    ("bmorphism", "ocaml-mcp-sdk", "bmorphism/ocaml-mcp-sdk", "OCaml", 60, 2, 0, "2026-03-16T05:24:25Z", "OCaml SDK for Model Context Protocol"),
    ("bmorphism", "flox-mcp-bb", "bmorphism/flox-mcp-bb", "Clojure", 0, 0, 0, "2026-02-12T02:45:43Z", "Open-source MCP server for Flox"),
    ("bmorphism", "vibesnipe-market", "bmorphism/vibesnipe-market", "Move", 0, 0, 9, "2026-02-05T10:23:25Z", ""),
    ("bmorphism", "tapes", "bmorphism/tapes", "", 0, 0, 0, "2026-02-04T02:23:37Z", "VHS tapes for terminal recordings"),
    ("bmorphism", "duck-rio-heateq", "bmorphism/duck-rio-heateq", "Rust", 0, 0, 0, "2026-02-02T23:33:32Z", ""),
    ("bmorphism", "aella", "bmorphism/aella", "Rascal", 1, 0, 0, "2026-02-01T02:44:30Z", ""),
    ("bmorphism", "hymlx", "bmorphism/hymlx", "Python", 1, 0, 0, "2026-01-22T12:20:32Z", ""),
    ("bmorphism", "GeoACSets.jl", "bmorphism/GeoACSets.jl", "Julia", 0, 1, 1, "2026-01-19T13:57:13Z", "Categorical data structures (ACSets) with geospatial capabilities"),
    ("bmorphism", "anti-bullshit-mcp-server", "bmorphism/anti-bullshit-mcp-server", "JavaScript", 23, 7, 1, "2026-01-16T08:54:58Z", "MCP server for analyzing claims"),
    ("bmorphism", "open-location-code-zig", "bmorphism/open-location-code-zig", "Zig", 3, 0, 0, "2025-12-30T19:33:45Z", "Open Location Code (Plus Codes) for Zig"),
    ("bmorphism", "signal-mcp", "bmorphism/signal-mcp", "Rust", 0, 0, 0, "2025-12-11T07:20:08Z", "O(n)->O(1) chromatic mode collapse via Galois connection"),
    ("bmorphism", "bafishka", "bmorphism/bafishka", "Clojure", 1, 0, 0, "2025-12-19T09:38:00Z", "Rust-native Fish shell-friendly file operations"),
    ("bmorphism", "monero-rental-hash-war", "bmorphism/monero-rental-hash-war", "Haskell", 1, 0, 0, "2025-10-05T23:08:54Z", "Compositional OpenGame analysis of Monero rental hash war"),
    ("bmorphism", "schoenfinkel", "bmorphism/schoenfinkel", "Python", 1, 0, 0, "2025-10-04T23:31:11Z", "Post-quantum categorical gravity framework"),
    ("bmorphism", "vibespace-mcp-go-ternary", "bmorphism/vibespace-mcp-go-ternary", "HTML", 0, 1, 3, "2026-01-11T12:50:40Z", "Go implementation of a MCP experience for vibes and worlds"),
]

# zubyul repos
zubyul_repos = [
    ("zubyul", "voice-observatory", "zubyul/voice-observatory", "Python", 0, 0, 0, "2026-04-24T05:56:17Z", "Passive macOS TUI observing voice-download pathways"),
    ("zubyul", "ghostel-emacs-worlds", "zubyul/ghostel-emacs-worlds", "GLSL", 0, 0, 0, "2026-04-24T00:20:56Z", "Ghostty config + ghostel family"),
    ("zubyul", "nash-web", "zubyul/nash-web", "Rust", 0, 0, 0, "2026-04-13T07:08:58Z", "NASH token browser TUI via ratzilla WASM"),
    ("zubyul", "nash-tui", "zubyul/nash-tui", "Rust", 0, 0, 0, "2026-04-13T07:45:16Z", "NASH token TUI: real-time candles"),
    ("zubyul", "big-bad-plurigrid-quiz", "zubyul/big-bad-plurigrid-quiz", "Emacs Lisp", 0, 0, 0, "2026-04-09T18:51:31Z", "27 flashcards from bmorphism/plurigrid/zubyul"),
    ("zubyul", "Gay.jl", "zubyul/Gay.jl", "Julia", 0, 0, 0, "2026-03-28T11:30:01Z", "Wide-gamut color sampling with splittable determinism"),
    ("zubyul", "kinesis-kb360pro", "zubyul/kinesis-kb360pro", "Python", 0, 0, 0, "2026-03-26T10:29:40Z", "Claude Code skill for Kinesis Advantage360 Pro keyboard"),
    ("zubyul", "gay-world", "zubyul/gay-world", "Python", 1, 1, 0, "2026-03-26T04:03:39Z", "Goblin world builder"),
    ("zubyul", "from-possible-worlds", "zubyul/from-possible-worlds", "TeX", 0, 0, 0, "2026-03-16T03:14:55Z", ""),
    ("zubyul", "tilelang-kernels", "zubyul/tilelang-kernels", "Python", 0, 0, 0, "2026-03-16T02:31:13Z", "TileLang GPU kernels for SplitMix64 color generation"),
    ("zubyul", "fleet-bootstrap", "zubyul/fleet-bootstrap", "Shell", 0, 0, 0, "2026-02-23T08:19:58Z", ""),
    ("zubyul", "gay-terminal-colors", "zubyul/gay-terminal-colors", "Clojure", 0, 0, 0, "2026-02-21T07:38:14Z", "Gay.jl world_terminal_fingerprint"),
    ("zubyul", "basin", "zubyul/basin", "Rust", 0, 0, 0, "2026-02-13T10:31:47Z", ""),
    ("zubyul", "openbci-visualizer", "zubyul/openbci-visualizer", "Zig", 0, 0, 0, "2026-02-04T11:17:41Z", ""),
    ("zubyul", "plurigrid-site", "zubyul/plurigrid-site", "Svelte", 0, 1, 11, "2026-02-04T03:20:08Z", "Plurigrid world: site deployment"),
    ("zubyul", "vibesnipe", "zubyul/vibesnipe", "Move", 0, 0, 1, "2026-01-30T22:36:03Z", ""),
    ("zubyul", "zubyul.github.io", "zubyul/zubyul.github.io", "CSS", 1, 0, 0, "2026-01-27T03:24:34Z", ""),
    ("zubyul", "toad-warpify-extension", "zubyul/toad-warpify-extension", "Python", 0, 0, 0, "2026-01-17T07:48:40Z", "Warpify extension for Toad"),
    ("zubyul", "thread-site", "zubyul/thread-site", "Haskell", 0, 0, 0, "2025-12-23T23:53:27Z", ""),
    ("zubyul", "GayMove", "zubyul/GayMove", "Move", 0, 0, 0, "2025-12-18T09:40:08Z", ""),
]

# Social graph repos (migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone)
social_repos = [
    ("migalkin", "kgcourse2021", "migalkin/kgcourse2021", "HTML", 25, 9, 0, "2026-02-16T05:16:08Z", "Materials for Knowledge Graphs course"),
    ("migalkin", "NBFNet_mlx", "migalkin/NBFNet_mlx", "Python", 10, 1, 1, "2026-03-11T01:31:21Z", "Neural Bellman-Ford networks in MLX"),
    ("migalkin", "StarE", "migalkin/StarE", "Python", 89, 16, 1, "2026-04-16T14:12:45Z", "EMNLP 2020: Message Passing for Hyper-Relational Knowledge Graphs"),
    ("migalkin", "NodePiece", "migalkin/NodePiece", "Python", 143, 21, 0, "2026-03-02T09:39:45Z", "Compositional Knowledge Graph Representations (ICLR'22)"),
    ("DJedamski", "kaggle_ncaa18", "DJedamski/kaggle_ncaa18", "Jupyter Notebook", 0, 0, 0, "2018-02-26T16:33:24Z", "Code for NCAA March Madness competition"),
    ("wasita", "wasita.github.io", "wasita/wasita.github.io", "Svelte", 1, 0, 8, "2026-04-28T05:26:08Z", "personal website"),
    ("wasita", "magic-garden", "wasita/magic-garden", "Python", 2, 1, 1, "2026-04-22T21:16:43Z", "bot for magic garden discord activity game"),
    ("kristinezheng", "kristinezheng.github.io", "kristinezheng/kristinezheng.github.io", "HTML", 0, 0, 0, "2026-04-09T17:09:47Z", ""),
    ("M1shaaa", "M1shaaa", "M1shaaa/M1shaaa", "", 0, 0, 0, "2026-02-04T19:32:04Z", "Config files for GitHub profile"),
    ("M1shaaa", "lab-bookshelf-", "M1shaaa/lab-bookshelf-", "TypeScript", 0, 0, 0, "2024-12-31T05:11:18Z", ""),
    ("AustinCStone", "EpsteinSearch", "AustinCStone/EpsteinSearch", "Python", 0, 0, 0, "2026-02-11T01:10:57Z", ""),
    ("AustinCStone", "TextGAN", "AustinCStone/TextGAN", "Python", 92, 30, 5, "2025-03-03T13:26:32Z", "A generative adversarial network for text generation"),
    ("AustinCStone", "StereoVisionMRF", "AustinCStone/StereoVisionMRF", "Python", 11, 4, 0, "2026-04-01T07:39:41Z", "Recover 3D geometry from stereo images"),
]

all_repos = (
    [(r, "org", "plurigrid") for r in plurigrid_repos] +
    [(r, "org", "kubeflow") for r in kubeflow_repos] +
    [(r, "org", "TeglonLabs") for r in teglon_repos] +
    [(r, "user", "bmorphism") for r in bmorphism_repos] +
    [(r, "user", "zubyul") for r in zubyul_repos] +
    [(r, "user_social", s[0]) for r, s in [(r, (r[0],)) for r in social_repos]]
)

# Re-flatten for social repos
all_repos_flat = []
for r in plurigrid_repos:
    all_repos_flat.append(("org", "plurigrid") + r)
for r in kubeflow_repos:
    all_repos_flat.append(("org", "kubeflow") + r)
for r in teglon_repos:
    all_repos_flat.append(("org", "TeglonLabs") + r)
for r in bmorphism_repos:
    all_repos_flat.append(("user", "bmorphism") + r)
for r in zubyul_repos:
    all_repos_flat.append(("user", "zubyul") + r)
for r in social_repos:
    all_repos_flat.append(("user_social", r[0]) + r)

# Insert world_increments and repo_snapshots
inc_id = 1
repo_id = 1
for src_type, src_name, org_or_user, repo_name, full_name, lang, stars, forks, issues, pushed_at, desc in all_repos_flat:
    trit, color, gname = gf3(inc_id)
    h = snap_hash((full_name, pushed_at, stars))
    con.execute("""
        INSERT INTO world_increments VALUES (?, now(), ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [inc_id, trit, color, gname, src_type, src_name, "repo_snapshot", full_name, "github-api", h])
    con.execute("""
        INSERT INTO repo_snapshots VALUES (?, now(), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [repo_id, inc_id, org_or_user, repo_name, full_name, lang, stars, forks, issues, pushed_at, desc])
    inc_id += 1
    repo_id += 1

# --- Aptos snapshots ---
aptos_data = [
    ("alice", "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b", 0.0),
    ("bob", "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d", 0.0),
    ("A", "0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a", 0.0),
    ("B", "0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13", 0.0),
    ("C", "0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e", 0.0),
    ("D", "0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1", 0.0),
    ("E", "0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36", 0.0),
    ("F", "0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71", 0.0),
    ("G", "0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32", 0.0),
    ("H", "0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f", 0.0),
    ("I", "0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9", 0.0),
    ("J", "0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54", 0.0),
    ("K", "0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4", 0.0),
    ("L", "0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9", 0.0),
    ("M", "0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9", 0.0),
    ("N", "0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c", 0.0),
    ("O", "0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d", 0.0),
    ("P", "0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948", 0.0),
    ("Q", "0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9", 0.0),
    ("R", "0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10", 0.0),
    ("S", "0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386", 0.0),
    ("T", "0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588", 0.0),
    ("U", "0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956", 0.0),
    ("V", "0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3", 0.0),
    ("W", "0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0", 0.0),
    ("X", "0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d", 0.0),
    ("Y", "0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4", 0.0),
    ("Z", "0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c", 0.0),
]

for world, address, balance_apt in aptos_data:
    con.execute("INSERT INTO aptos_snapshots VALUES (now(), ?, ?, ?)", [world, address, balance_apt])

# --- Multisig probes ---
multisig_data = [
    ("A-B", "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2, True),
    ("A-G", "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2, True),
    ("Y-Z", "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2, True),
    ("S-T", "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2, True),
    ("V-W", "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2, True),
]

for pair, address, sigs_required, healthy in multisig_data:
    con.execute("INSERT INTO multisig_probes VALUES (now(), ?, ?, ?, ?)", [pair, address, sigs_required, healthy])

# --- MNX snapshots: unavailable ---
# SPA returns HTML for all API paths, no market data available

# Verify
print("=== world_increments ===")
print(con.execute("SELECT COUNT(*) FROM world_increments").fetchone())
print("=== repo_snapshots ===")
print(con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone())
print("=== aptos_snapshots ===")
print(con.execute("SELECT COUNT(*) FROM aptos_snapshots").fetchone())
print("=== multisig_probes ===")
print(con.execute("SELECT COUNT(*) FROM multisig_probes").fetchall())

# Sample
print("\nSample world_increments:")
for row in con.execute("SELECT id, gf3_trit, gf3_color, gf3_name, source_name, repo_name FROM world_increments LIMIT 5").fetchall():
    print(row)

print("\nSample aptos_snapshots:")
for row in con.execute("SELECT world, address, balance_apt FROM aptos_snapshots LIMIT 5").fetchall():
    print(row)

print("\nAll multisig probes:")
for row in con.execute("SELECT pair, address, sigs_required, healthy FROM multisig_probes").fetchall():
    print(row)

con.close()
print("\nDone.")
