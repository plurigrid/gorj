#!/usr/bin/env python3
"""Build world-increments DuckDB from sweep data."""
import subprocess, json, hashlib, sys

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"

DDL = """
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
CREATE SEQUENCE IF NOT EXISTS increment_seq START 1;
CREATE SEQUENCE IF NOT EXISTS repo_seq START 1;
"""

def gf3(id_val):
    t = id_val % 3
    if t == 0: return (0, "#d3869b", "ERGODIC")
    if t == 1: return (1, "#b8bb26", "PLUS")
    return (-1, "#cc241d", "MINUS")

def snap_hash(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()[:16]

# All repos collected from sweep
REPOS = {
    "plurigrid": [
{"full_name": "plurigrid/asi", "language": "HTML", "stars": 26, "forks": 8, "open_issues": 4, "pushed_at": "2026-06-10T12:51:42Z", "description": "everything is topological chemputer!"},
{"full_name": "plurigrid/place", "language": "TeX", "stars": 1, "forks": 2, "open_issues": 8, "pushed_at": "2026-06-15T23:04:11Z", "description": ""},
{"full_name": "plurigrid/eirobri", "language": "Clojure", "stars": 0, "forks": 0, "open_issues": 29, "pushed_at": "2026-06-03T20:43:46Z", "description": "EiRoBri replay world"},
{"full_name": "plurigrid/nash-portal", "language": "Rust", "stars": 2, "forks": 3, "open_issues": 1, "pushed_at": "2026-05-19T01:49:59Z", "description": "NASH token TUI"},
{"full_name": "plurigrid/gorj", "language": "Clojure", "stars": 0, "forks": 0, "open_issues": 678, "pushed_at": "2026-06-19T18:14:40Z", "description": "forj + Rama topology nREPL routing + GF(3) gay trit coloring"},
{"full_name": "plurigrid/zig-syrup", "language": "Zig", "stars": 2, "forks": 2, "open_issues": 0, "pushed_at": "2026-04-30T03:52:16Z", "description": "High-performance Zig OCapN Syrup"},
{"full_name": "plurigrid/asi-skills", "language": "Julia", "stars": 3, "forks": 1, "open_issues": 0, "pushed_at": "2026-04-26T08:09:26Z", "description": "69 skills with Galois Hole Type"},
{"full_name": "plurigrid/nanoclj-zig", "language": "Zig", "stars": 1, "forks": 2, "open_issues": 20, "pushed_at": "2026-04-25T07:29:09Z", "description": "NaN-boxed Clojure interpreter in Zig"},
{"full_name": "plurigrid/ontology", "language": "JavaScript", "stars": 8, "forks": 9, "open_issues": 16, "pushed_at": "2025-05-27T18:18:34Z", "description": "autopoietic ergodicity"},
{"full_name": "plurigrid/agent", "language": "Python", "stars": 5, "forks": 1, "open_issues": 6, "pushed_at": "2023-03-31T18:45:23Z", "description": "Framework for agency amplification"},
{"full_name": "plurigrid/vcg-auction", "language": "Rust", "stars": 7, "forks": 2, "open_issues": 1, "pushed_at": "2023-03-16T21:53:08Z", "description": "VCG auction contract"},
{"full_name": "plurigrid/microworlds", "language": "Rust", "stars": 3, "forks": 5, "open_issues": 3, "pushed_at": "2023-05-13T03:54:56Z", "description": ""},
{"full_name": "plurigrid/StochFlow", "language": "Python", "stars": 4, "forks": 1, "open_issues": 0, "pushed_at": "2024-03-20T23:34:57Z", "description": "Stochastic interpolant models"},
{"full_name": "plurigrid/Plurigraph", "language": "JavaScript", "stars": 3, "forks": 5, "open_issues": 4, "pushed_at": "2025-01-05T08:39:09Z", "description": "Plurigrid knowledge base"},
{"full_name": "plurigrid/vivarium", "language": "Clojure", "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-08T08:38:37Z", "description": ""},
{"full_name": "plurigrid/gatomic", "language": "Clojure", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-03-30T00:54:48Z", "description": "Deterministic color identity store"},
{"full_name": "plurigrid/graded-optic", "language": "Haskell", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-02-08T16:10:16Z", "description": "Semiring-graded bidirectional processes"},
{"full_name": "plurigrid/lazygay", "language": "Go", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-01-08T14:19:25Z", "description": "lazygit fork with Gay.jl coloring"},
{"full_name": "plurigrid/gay-rs", "language": "Rust", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-01-08T14:19:22Z", "description": "Rust crate for Gay.jl GF(3) trits"},
{"full_name": "plurigrid/aptos-wallet-ruby", "language": "Ruby", "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2025-09-30T22:47:22Z", "description": ""},
    ],
    "kubeflow": [
{"full_name": "kubeflow/kubeflow", "language": "", "stars": 15736, "forks": 2680, "open_issues": 0, "pushed_at": "2026-06-18T11:45:16Z", "description": "Machine Learning Toolkit for Kubernetes"},
{"full_name": "kubeflow/pipelines", "language": "Python", "stars": 4154, "forks": 2009, "open_issues": 452, "pushed_at": "2026-06-19T18:21:35Z", "description": "Machine Learning Pipelines for Kubeflow"},
{"full_name": "kubeflow/spark-operator", "language": "Python", "stars": 3127, "forks": 1490, "open_issues": 100, "pushed_at": "2026-06-18T15:39:22Z", "description": "Kubernetes operator for Apache Spark"},
{"full_name": "kubeflow/trainer", "language": "Go", "stars": 2117, "forks": 970, "open_issues": 118, "pushed_at": "2026-06-19T15:46:05Z", "description": "Distributed AI Model Training on Kubernetes"},
{"full_name": "kubeflow/katib", "language": "Python", "stars": 1683, "forks": 528, "open_issues": 116, "pushed_at": "2026-06-15T20:07:37Z", "description": "Automated Machine Learning on Kubernetes"},
{"full_name": "kubeflow/examples", "language": "Jsonnet", "stars": 1460, "forks": 756, "open_issues": 111, "pushed_at": "2025-04-14T01:54:52Z", "description": "Examples and tutorials"},
{"full_name": "kubeflow/community-distribution", "language": "YAML", "stars": 1025, "forks": 1065, "open_issues": 21, "pushed_at": "2026-06-18T19:10:25Z", "description": "Kubeflow Community Distribution"},
{"full_name": "kubeflow/arena", "language": "Go", "stars": 813, "forks": 190, "open_issues": 44, "pushed_at": "2026-05-07T06:46:17Z", "description": "A CLI for Kubeflow"},
{"full_name": "kubeflow/kale", "language": "Python", "stars": 694, "forks": 155, "open_issues": 54, "pushed_at": "2026-06-17T21:23:08Z", "description": "Kubeflow's superfood for Data Scientists"},
{"full_name": "kubeflow/mpi-operator", "language": "Go", "stars": 528, "forks": 236, "open_issues": 106, "pushed_at": "2026-06-15T13:03:34Z", "description": "MPI operator for distributed training"},
{"full_name": "kubeflow/fairing", "language": "Jsonnet", "stars": 337, "forks": 143, "open_issues": 134, "pushed_at": "2022-04-11T05:28:47Z", "description": "Python SDK for ML models"},
{"full_name": "kubeflow/mcp-apache-spark-history-server", "language": "Python", "stars": 177, "forks": 65, "open_issues": 20, "pushed_at": "2026-06-19T18:33:43Z", "description": "MCP Server for Apache Spark History Server"},
{"full_name": "kubeflow/community", "language": "Jupyter Notebook", "stars": 194, "forks": 264, "open_issues": 14, "pushed_at": "2026-06-19T16:50:40Z", "description": "Kubeflow community information"},
{"full_name": "kubeflow/website", "language": "HTML", "stars": 184, "forks": 923, "open_issues": 40, "pushed_at": "2026-06-19T15:39:26Z", "description": "Kubeflow Website"},
{"full_name": "kubeflow/hub", "language": "Go", "stars": 173, "forks": 183, "open_issues": 38, "pushed_at": "2026-06-19T11:04:41Z", "description": "Model Registry for MLOps"},
{"full_name": "kubeflow/sdk", "language": "Python", "stars": 120, "forks": 180, "open_issues": 133, "pushed_at": "2026-06-19T14:27:44Z", "description": "Universal Python SDK for Kubernetes AI"},
{"full_name": "kubeflow/notebooks", "language": "", "stars": 73, "forks": 124, "open_issues": 177, "pushed_at": "2026-06-19T16:02:08Z", "description": "Kubeflow Notebooks"},
{"full_name": "kubeflow/docs-agent", "language": "Python", "stars": 39, "forks": 95, "open_issues": 152, "pushed_at": "2026-06-11T18:43:15Z", "description": "Kubeflow Documentation AI Agent"},
{"full_name": "kubeflow/dashboard", "language": "TypeScript", "stars": 16, "forks": 59, "open_issues": 76, "pushed_at": "2026-06-17T05:08:17Z", "description": "Kubeflow Central Dashboard"},
{"full_name": "kubeflow/mcp-server", "language": "Python", "stars": 16, "forks": 22, "open_issues": 25, "pushed_at": "2026-05-12T10:14:24Z", "description": "MCP Server for Kubeflow Tools"},
    ],
    "TeglonLabs": [
{"full_name": "TeglonLabs/jank-crane", "language": "C++", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-06-08T19:03:03Z", "description": "crane-jank converged-IR hub: GF3 convergence maps"},
{"full_name": "TeglonLabs/mathpix-gem", "language": "Ruby", "stars": 2, "forks": 0, "open_issues": 11, "pushed_at": "2026-01-01T12:13:13Z", "description": "Mathematical images to LaTeX Ruby gem"},
{"full_name": "TeglonLabs/coin-flip-mcp", "language": "JavaScript", "stars": 0, "forks": 2, "open_issues": 1, "pushed_at": "2025-09-21T08:57:27Z", "description": "MCP server for flipping coins"},
{"full_name": "TeglonLabs/monad-mcp-server", "language": "", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2025-05-14T11:36:14Z", "description": "Monad MCP Server"},
{"full_name": "TeglonLabs/topoi", "language": "Python", "stars": 0, "forks": 0, "open_issues": 1, "pushed_at": "2025-01-24T04:49:26Z", "description": ""},
    ],
    "bmorphism": [
{"full_name": "bmorphism/ocaml-mcp-sdk", "language": "OCaml", "stars": 61, "forks": 2, "open_issues": 0, "pushed_at": "2026-03-16T05:24:25Z", "description": "OCaml SDK for Model Context Protocol"},
{"full_name": "bmorphism/anti-bullshit-mcp-server", "language": "JavaScript", "stars": 23, "forks": 7, "open_issues": 1, "pushed_at": "2026-01-16T08:54:58Z", "description": "MCP server for claim analysis"},
{"full_name": "bmorphism/risc0-cosmwasm-example", "language": "Rust", "stars": 23, "forks": 2, "open_issues": 1, "pushed_at": "2022-10-20T23:50:40Z", "description": "CosmWasm + zkVM RISC-V EFI template"},
{"full_name": "bmorphism/say-mcp-server", "language": "JavaScript", "stars": 20, "forks": 9, "open_issues": 3, "pushed_at": "2025-01-07T03:15:18Z", "description": "MCP server for macOS TTS"},
{"full_name": "bmorphism/babashka-mcp-server", "language": "JavaScript", "stars": 19, "forks": 6, "open_issues": 3, "pushed_at": "2025-01-05T11:09:42Z", "description": "MCP server for Babashka"},
{"full_name": "bmorphism/manifold-mcp-server", "language": "JavaScript", "stars": 14, "forks": 9, "open_issues": 5, "pushed_at": "2025-01-11T10:36:58Z", "description": "MCP server for Manifold Markets"},
{"full_name": "bmorphism/penrose-mcp", "language": "JavaScript", "stars": 10, "forks": 4, "open_issues": 0, "pushed_at": "2025-01-20T21:44:55Z", "description": "Penrose server for Infinity-Topos"},
{"full_name": "bmorphism/Gay.jl", "language": "Julia", "stars": 1, "forks": 1, "open_issues": 187, "pushed_at": "2026-06-19T00:48:59Z", "description": "Wide-gamut color sampling with GF(3)"},
{"full_name": "bmorphism/satreadout", "language": "Lean", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-06-15T21:20:06Z", "description": "Lean 4 saturating non-Riemannian perceptual readout"},
{"full_name": "bmorphism/vibespace-mcp-go-ternary", "language": "HTML", "stars": 0, "forks": 1, "open_issues": 3, "pushed_at": "2026-01-11T12:50:40Z", "description": "Go MCP vibes with balanced ternary"},
{"full_name": "bmorphism/oxgame", "language": "OCaml", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-05-15T09:53:27Z", "description": "Stellar resolution and open-game composition"},
{"full_name": "bmorphism/marginalia-mcp-server", "language": "JavaScript", "stars": 8, "forks": 6, "open_issues": 0, "pushed_at": "2025-01-06T05:47:24Z", "description": "MCP server for marginalia"},
{"full_name": "bmorphism/nats-mcp-server", "language": "", "stars": 7, "forks": 3, "open_issues": 2, "pushed_at": "2025-01-06T23:33:41Z", "description": "MCP server for NATS messaging"},
{"full_name": "bmorphism/hypernym-mcp-server", "language": "JavaScript", "stars": 6, "forks": 5, "open_issues": 0, "pushed_at": "2025-04-02T21:21:08Z", "description": ""},
{"full_name": "bmorphism/penumbra-mcp", "language": "JavaScript", "stars": 5, "forks": 6, "open_issues": 3, "pushed_at": "2025-01-07T01:15:23Z", "description": "MCP server for Penumbra blockchain"},
{"full_name": "bmorphism/shitcoin", "language": "Python", "stars": 5, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-08T08:07:08Z", "description": "denom for cw20 IBC assets"},
{"full_name": "bmorphism/flox-mcp-bb", "language": "Clojure", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-02-12T02:45:43Z", "description": "MCP server for Flox - Babashka"},
{"full_name": "bmorphism/open-location-code-zig", "language": "Zig", "stars": 3, "forks": 0, "open_issues": 0, "pushed_at": "2025-12-30T19:33:45Z", "description": "Open Location Code for Zig"},
{"full_name": "bmorphism/bafishka", "language": "Clojure", "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2025-12-19T09:38:00Z", "description": "Rust-native Fish shell Clojure eval"},
{"full_name": "bmorphism/world", "language": "Python", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-06-02T06:49:02Z", "description": "Local worlds launcher for SA3, jank, world proofs"},
    ],
    "zubyul": [
{"full_name": "zubyul/voice-observatory", "language": "Python", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-24T05:56:17Z", "description": "Passive macOS TUI observing voice-download pathways"},
{"full_name": "zubyul/nash-tui", "language": "Rust", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-13T07:45:16Z", "description": "NASH token TUI with GeckoTerminal OHLCV"},
{"full_name": "zubyul/gay-world", "language": "Python", "stars": 1, "forks": 1, "open_issues": 0, "pushed_at": "2026-03-26T04:03:39Z", "description": "Goblin world builder with MLX"},
{"full_name": "zubyul/tilelang-kernels", "language": "Python", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-03-16T02:31:13Z", "description": "TileLang GPU kernels for GF(3) trit classification"},
{"full_name": "zubyul/gay-terminal-colors", "language": "Clojure", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-02-21T07:38:14Z", "description": "Gay.jl SplitMix64 per-terminal color identity"},
{"full_name": "zubyul/plurigrid-site", "language": "Svelte", "stars": 0, "forks": 1, "open_issues": 11, "pushed_at": "2026-02-04T03:20:08Z", "description": "Plurigrid world: site deployment"},
{"full_name": "zubyul/kinesis-kb360pro", "language": "Python", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-03-26T10:29:40Z", "description": "Kinesis Advantage360 KMonad + Gay.jl GF(3)"},
{"full_name": "zubyul/big-bad-plurigrid-quiz", "language": "Emacs Lisp", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-09T18:51:31Z", "description": "27 flashcards from bmorphism/plurigrid/zubyul activity"},
{"full_name": "zubyul/ghostel-emacs-worlds", "language": "GLSL", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-24T00:20:56Z", "description": "Ghostty config + alice/bob emacs-mods"},
{"full_name": "zubyul/Gay.jl", "language": "Julia", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-03-28T11:30:01Z", "description": "Wide-gamut color sampling with GF(3)"},
{"full_name": "zubyul/WGCNA", "language": "HTML", "stars": 2, "forks": 0, "open_issues": 0, "pushed_at": "2023-07-05T18:02:30Z", "description": "weighted gene correlation network analysis"},
{"full_name": "zubyul/Nikolova_lab_data_analysis", "language": "R", "stars": 2, "forks": 0, "open_issues": 0, "pushed_at": "2023-06-16T13:56:58Z", "description": "cortical thickness vs transcription factors for depression"},
    ],
    "migalkin": [
{"full_name": "migalkin/NodePiece", "language": "Python", "stars": 144, "forks": 21, "open_issues": 0, "pushed_at": "2026-05-07T05:40:02Z", "description": "Representations for Large Knowledge Graphs (ICLR'22)"},
{"full_name": "migalkin/StarE", "language": "Python", "stars": 89, "forks": 16, "open_issues": 1, "pushed_at": "2026-04-16T14:12:45Z", "description": "EMNLP 2020: Hyper-Relational Knowledge Graphs"},
{"full_name": "migalkin/kgcourse2021", "language": "HTML", "stars": 25, "forks": 9, "open_issues": 0, "pushed_at": "2026-02-16T05:16:08Z", "description": "Knowledge Graphs course materials"},
{"full_name": "migalkin/NBFNet_mlx", "language": "Python", "stars": 10, "forks": 1, "open_issues": 1, "pushed_at": "2026-03-11T01:31:21Z", "description": "Neural Bellman-Ford networks in MLX"},
{"full_name": "migalkin/RWL", "language": "Python", "stars": 8, "forks": 1, "open_issues": 0, "pushed_at": "2026-05-28T20:19:20Z", "description": "Weisfeiler and Leman Go Relational (LOG 2022)"},
{"full_name": "migalkin/rambo", "language": "Rust", "stars": 3, "forks": 0, "open_issues": 1, "pushed_at": "2023-02-28T16:37:22Z", "description": ""},
    ],
    "wasita": [
{"full_name": "wasita/wasita.github.io", "language": "Svelte", "stars": 1, "forks": 0, "open_issues": 8, "pushed_at": "2026-06-15T20:14:23Z", "description": "personal website"},
{"full_name": "wasita/magic-garden", "language": "Python", "stars": 2, "forks": 1, "open_issues": 1, "pushed_at": "2026-04-22T21:16:43Z", "description": "Discord bot for magic garden game"},
{"full_name": "wasita/send2kobo", "language": "TypeScript", "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2026-05-19T02:59:26Z", "description": "Website for sending books to kobo"},
{"full_name": "wasita/wins-search", "language": "CSS", "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2023-06-03T19:01:11Z", "description": "Women in Network Science member list"},
{"full_name": "wasita/wm-cv", "language": "Svelte", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-05-13T05:29:08Z", "description": "Academic CV as single page web app"},
    ],
    "AustinCStone": [
{"full_name": "AustinCStone/TextGAN", "language": "Python", "stars": 92, "forks": 30, "open_issues": 5, "pushed_at": "2025-03-03T13:26:32Z", "description": "GAN for text generation in TensorFlow"},
{"full_name": "AustinCStone/StereoVisionMRF", "language": "Python", "stars": 11, "forks": 4, "open_issues": 0, "pushed_at": "2026-04-01T07:39:41Z", "description": "Depth from stereo images via MRF"},
{"full_name": "AustinCStone/SpectralClustering", "language": "Python", "stars": 3, "forks": 2, "open_issues": 0, "pushed_at": "2021-04-16T08:46:36Z", "description": "Spectral clustering implementation"},
{"full_name": "AustinCStone/StructureFromMotion", "language": "Python", "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2019-04-26T19:43:12Z", "description": "3D geometry from videos"},
{"full_name": "AustinCStone/EpsteinSearch", "language": "Python", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-02-11T01:10:57Z", "description": ""},
{"full_name": "AustinCStone/bmforkupdate", "language": "Python", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2025-05-09T04:50:16Z", "description": ""},
    ],
    "kristinezheng": [
{"full_name": "kristinezheng/kristinezheng.github.io", "language": "HTML", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-06-07T22:53:10Z", "description": "personal site"},
{"full_name": "kristinezheng/lookit-jenga", "language": "Jupyter Notebook", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2024-05-16T18:29:05Z", "description": "Lookit study for 9.85"},
{"full_name": "kristinezheng/Green-Machine", "language": "Python", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2021-09-19T05:33:04Z", "description": "HackMIT 2021 Sustainability"},
    ],
    "M1shaaa": [
{"full_name": "M1shaaa/M1shaaa", "language": "", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-02-04T19:32:04Z", "description": "GitHub profile config"},
{"full_name": "M1shaaa/lab-bookshelf-", "language": "TypeScript", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2024-12-31T05:11:18Z", "description": ""},
{"full_name": "M1shaaa/MNIST-Classifier", "language": "", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2023-11-28T06:10:47Z", "description": ""},
    ],
    "DJedamski": [
{"full_name": "DJedamski/kaggle_ncaa18", "language": "Jupyter Notebook", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2018-02-26T16:33:24Z", "description": "NCAA March Madness 2018"},
{"full_name": "DJedamski/Kaggle", "language": "", "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2023-04-21T01:42:35Z", "description": ""},
{"full_name": "DJedamski/School", "language": "R", "stars": 1, "forks": 1, "open_issues": 0, "pushed_at": "2023-04-21T01:42:33Z", "description": "Projects from grad school"},
    ],
}

APTOS_BALANCES = [
    ("alice", "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b", 0.43643352),
    ("bob",   "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d", 12.657007),
    ("A",     "0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a", 0.051767),
    ("B",     "0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13", 0.036256),
    ("C",     "0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e", 0.010185),
    ("D",     "0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1", 0.011629),
    ("E",     "0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36", 0.009372),
    ("F",     "0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71", 1.960516),
    ("G",     "0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32", 0.000681),
    ("H",     "0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f", 0.001681),
    ("I",     "0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9", 0.000681),
    ("J",     "0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54", 1.895093),
    ("K",     "0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4", 0.161961),
    ("L",     "0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9", 1.927269),
    ("M",     "0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9", 0.112285),
    ("N",     "0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c", 0.106121),
    ("O",     "0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d", 0.210136),
    ("P",     "0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948", 0.140136),
    ("Q",     "0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9", 0.10324),
    ("R",     "0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10", 0.090217),
    ("S",     "0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386", 0.091788),
    ("T",     "0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588", 0.073713),
    ("U",     "0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956", 0.055773),
    ("V",     "0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3", 0.04883299),
    ("W",     "0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0", 0.040705),
    ("X",     "0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d", 0.042577),
    ("Y",     "0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4", 0.044449),
    ("Z",     "0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c", 0.024268),
]

MULTISIG = [
    ("A-B", "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2, True),
    ("A-G", "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2, True),
    ("Y-Z", "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2, True),
    ("S-T", "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2, True),
    ("V-W", "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2, True),
]

# Build SQL script
lines = [DDL]

# Insert world_increments and repo_snapshots
inc_id = 1
repo_id = 1
for org_user, repos in REPOS.items():
    trit, color, name = gf3(inc_id)
    h = snap_hash({"org": org_user, "repos": len(repos)})
    lines.append(f"""INSERT INTO world_increments VALUES (
  {inc_id}, now(), {trit}, '{color}', '{name}', 'github_sweep',
  '{org_user}', 'repo_snapshot', '', '', '{h}'
);""")
    for r in repos:
        lang = (r.get("language") or "").replace("'", "''")
        desc = (r.get("description") or "").replace("'", "''")[:200]
        full = r["full_name"].replace("'", "''")
        lines.append(f"""INSERT INTO repo_snapshots VALUES (
  {repo_id}, now(), {inc_id}, '{org_user}', '{full.split('/',1)[1] if '/' in full else full}',
  '{full}', '{lang}', {r.get('stars',0)}, {r.get('forks',0)},
  {r.get('open_issues',0)}, '{r.get('pushed_at','')}', '{desc}'
);""")
        repo_id += 1
    inc_id += 1

# Insert aptos snapshots
for world, addr, bal in APTOS_BALANCES:
    lines.append(f"INSERT INTO aptos_snapshots VALUES (now(), '{world}', '{addr}', {bal});")

# Insert multisig probes
for pair, addr, sigs, healthy in MULTISIG:
    lines.append(f"INSERT INTO multisig_probes VALUES (now(), '{pair}', '{addr}', {sigs}, {'true' if healthy else 'false'});")

# Summary query
lines.append("""
SELECT 'world_increments' as tbl, count(*) as n FROM world_increments
UNION ALL SELECT 'repo_snapshots', count(*) FROM repo_snapshots
UNION ALL SELECT 'aptos_snapshots', count(*) FROM aptos_snapshots
UNION ALL SELECT 'multisig_probes', count(*) FROM multisig_probes
UNION ALL SELECT 'mnx_snapshots', count(*) FROM mnx_snapshots;
""")

sql = "\n".join(lines)
with open("/tmp/build_db.sql", "w") as f:
    f.write(sql)
print(f"SQL written: {len(sql)} chars, {len(lines)} statements")
print(f"world_increments: {inc_id-1}, repo_snapshots: {repo_id-1}")
