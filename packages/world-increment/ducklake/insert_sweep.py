#!/usr/bin/env python3
"""World-increment sweep + Hamming swarm snapshot DB insertion."""
import duckdb
import hashlib
import json
from datetime import datetime

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
NOW = datetime.utcnow().isoformat()

def gf3(id_):
    t = id_ % 3
    if t == 0:
        return (0, "#d3869b", "ERGODIC")
    elif t == 1:
        return (1, "#b8bb26", "PLUS")
    else:
        return (-1, "#cc241d", "MINUS")

def snap_hash(full_name, pushed_at):
    return hashlib.sha256(f"{full_name}:{pushed_at}".encode()).hexdigest()[:16]

con = duckdb.connect(DB_PATH)

# ── Repo data ──────────────────────────────────────────────────────────────────
REPOS = {
    "plurigrid": [
    {"full_name": "plurigrid/place", "language": "TeX", "stars": 1, "forks": 2, "issues": 8, "pushed_at": "2026-06-04T09:51:50Z", "description": ""},
    {"full_name": "plurigrid/eirobri", "language": "Clojure", "stars": 0, "forks": 0, "issues": 29, "pushed_at": "2026-06-03T20:43:46Z", "description": "EiRoBri replay world"},
    {"full_name": "plurigrid/nash-portal", "language": "Rust", "stars": 2, "forks": 3, "issues": 1, "pushed_at": "2026-05-19T01:49:59Z", "description": "NASH token TUI in the browser — ratzilla WASM + GeckoTerminal OHLCV candlesticks"},
    {"full_name": "plurigrid/gorj", "language": "Clojure", "stars": 0, "forks": 0, "issues": 459, "pushed_at": "2026-06-09T13:19:28Z", "description": "forj + Rama topology nREPL routing + GF(3) gay trit coloring"},
    {"full_name": "plurigrid/zig-syrup", "language": "Zig", "stars": 2, "forks": 2, "issues": 0, "pushed_at": "2026-04-30T03:52:16Z", "description": "High-performance Zig implementation of OCapN Syrup with CapTP optimizations"},
    {"full_name": "plurigrid/asi", "language": "HTML", "stars": 25, "forks": 7, "issues": 4, "pushed_at": "2026-04-26T08:51:41Z", "description": "everything is topological chemputer!"},
    {"full_name": "plurigrid/asi-skills", "language": "Julia", "stars": 3, "forks": 1, "issues": 0, "pushed_at": "2026-04-26T08:09:26Z", "description": "69 skills with Galois Hole Type accessibility"},
    {"full_name": "plurigrid/bci-blue-share", "language": "JavaScript", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-04-26T07:08:03Z", "description": "BCI signal infrastructure"},
    {"full_name": "plurigrid/nanoclj-zig", "language": "Zig", "stars": 1, "forks": 2, "issues": 20, "pushed_at": "2026-04-25T07:29:09Z", "description": "NaN-boxed Clojure interpreter in Zig 0.15"},
    {"full_name": "plurigrid/spi-race", "language": "Swift", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-04-21T19:31:56Z", "description": "Splitmix Parallel Integrity"},
    {"full_name": "plurigrid/reafference", "language": "HTML", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-04-16T05:21:49Z", "description": "Reafference adaptation workspace"},
    {"full_name": "plurigrid/web-browser", "language": "Rust", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-04-10T02:54:47Z", "description": "web-browser from prepostweb lineage"},
    {"full_name": "plurigrid/vivarium", "language": "Clojure", "stars": 1, "forks": 0, "issues": 0, "pushed_at": "2026-04-08T08:38:37Z", "description": ""},
    {"full_name": "plurigrid/flowglad-rs", "language": "Rust", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-04-08T07:56:15Z", "description": ""},
    {"full_name": "plurigrid/tree-sitter-nanoclj-zig", "language": "C", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-04-04T07:48:21Z", "description": "Tree-sitter grammar for nanoclj-zig"},
    {"full_name": "plurigrid/forester", "language": "XSLT", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-03-30T01:32:26Z", "description": "CatColab mathematical documentation forest"},
    {"full_name": "plurigrid/gatomic", "language": "Clojure", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-03-30T00:54:48Z", "description": "Deterministic color identity store — Gay + Datomic + Atomic"},
    {"full_name": "plurigrid/blue", "language": "TeX", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-03-29T23:06:32Z", "description": ""},
    {"full_name": "plurigrid/red", "language": None, "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-03-29T22:58:46Z", "description": ""},
    {"full_name": "plurigrid/nblm-flashcards", "language": "Hy", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-03-26T08:23:01Z", "description": "NotebookLM Enterprise flashcard pipeline"},
    {"full_name": "plurigrid/gemini-agent", "language": "Python", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-02-19T06:39:16Z", "description": ""},
    {"full_name": "plurigrid/graded-optic", "language": "Haskell", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-02-08T16:10:16Z", "description": "Semiring-graded bidirectional processes"},
    {"full_name": "plurigrid/json-canvas", "language": None, "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-02-06T06:50:57Z", "description": "JSON Canvas: Real-time interaction data capture"},
    {"full_name": "plurigrid/shepherd", "language": "Scheme", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-01-23T07:47:28Z", "description": "Spritely Shepherd - Service manager"},
    {"full_name": "plurigrid/goblinshare", "language": "Scheme", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-01-23T07:47:12Z", "description": "P2P filesharing demo for Goblins"},
    {"full_name": "plurigrid/magenc", "language": "Scheme", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-01-23T07:47:11Z", "description": "Magenc Magnet URIs"},
    {"full_name": "plurigrid/hoot", "language": "Scheme", "stars": 0, "forks": 0, "issues": 1, "pushed_at": "2026-01-23T07:47:10Z", "description": "Spritely Hoot - Scheme to WebAssembly compiler"},
    {"full_name": "plurigrid/leprechauns", "language": "Racket", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-01-23T07:46:46Z", "description": "Spritely Goblins + Gay.jl semantic colors"},
    {"full_name": "plurigrid/spritely-semantic-colors", "language": None, "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-01-23T07:38:32Z", "description": "Deterministic color mappings for Spritely/Goblins"},
    {"full_name": "plurigrid/gay-tofu", "language": "HTML", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-01-08T15:14:34Z", "description": "Low-discrepancy color sequences for visual TOFU authentication"},
    {"full_name": "plurigrid/lazygay", "language": "Go", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-01-08T14:19:25Z", "description": "lazygit fork with Gay.jl deterministic commit coloring"},
    {"full_name": "plurigrid/gay-terminal", "language": "Rust", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-01-08T14:19:24Z", "description": "Terminal ANSI coloring with Gay.jl"},
    {"full_name": "plurigrid/gay-go", "language": "Go", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-01-08T14:19:23Z", "description": "Go implementation of Gay.jl deterministic coloring"},
    {"full_name": "plurigrid/gay-rs", "language": "Rust", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-01-08T14:19:22Z", "description": "Rust crate for Gay.jl deterministic coloring with GF(3) trits"},
    {"full_name": "plurigrid/lazybjj", "language": "Rust", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-01-08T14:19:19Z", "description": "TUI for jj with Gay.jl GF(3) coloring"},
    {"full_name": "plurigrid/agent-o-rama", "language": "Clojure", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-01-02T01:09:22Z", "description": ""},
    {"full_name": "plurigrid/aptos-wallet-ruby", "language": "Ruby", "stars": 1, "forks": 0, "issues": 0, "pushed_at": "2025-09-30T22:47:22Z", "description": ""},
    {"full_name": "plurigrid/duck-kanban", "language": "Rust", "stars": 1, "forks": 0, "issues": 0, "pushed_at": "2025-09-26T20:18:38Z", "description": "Duck intelligence kanban system"},
    {"full_name": "plurigrid/shiteshiteshite", "language": None, "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2025-09-26T03:07:20Z", "description": ""},
    {"full_name": "plurigrid/discohy", "language": "Hy", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2025-09-10T02:01:31Z", "description": ""},
    {"full_name": "plurigrid/telemind", "language": None, "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2025-06-12T05:54:59Z", "description": ""},
    {"full_name": "plurigrid/ontology", "language": "JavaScript", "stars": 8, "forks": 9, "issues": 16, "pushed_at": "2025-05-27T18:18:34Z", "description": "autopoietic ergodicity and embodied gradualism"},
    {"full_name": "plurigrid/Plurigraph", "language": "JavaScript", "stars": 3, "forks": 5, "issues": 4, "pushed_at": "2025-01-05T08:39:09Z", "description": "Plurigrid knowledge base for Obsidian.md"},
    {"full_name": "plurigrid/signe", "language": "Python", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2024-08-15T20:52:03Z", "description": "Signal messages data traversal"},
    {"full_name": "plurigrid/act", "language": "Python", "stars": 3, "forks": 1, "issues": 4, "pushed_at": "2024-07-26T08:27:08Z", "description": "building blocks for cognitive category theory"},
    {"full_name": "plurigrid/StochFlow", "language": "Python", "stars": 4, "forks": 1, "issues": 0, "pushed_at": "2024-03-20T23:34:57Z", "description": "stochastic interpolant models"},
    {"full_name": "plurigrid/novella", "language": "TypeScript", "stars": 1, "forks": 0, "issues": 0, "pushed_at": "2024-01-27T08:12:55Z", "description": ""},
    {"full_name": "plurigrid/ACT.jl", "language": "Julia", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2024-01-21T00:02:25Z", "description": "applied categorical duck cybernetics"},
    {"full_name": "plurigrid/ducklings", "language": "TypeScript", "stars": 0, "forks": 0, "issues": 15, "pushed_at": "2023-12-25T07:34:27Z", "description": ""},
    {"full_name": "plurigrid/paretae", "language": "TypeScript", "stars": 0, "forks": 0, "issues": 14, "pushed_at": "2023-11-20T05:14:42Z", "description": ""},
    {"full_name": "plurigrid/org", "language": "Jupyter Notebook", "stars": 2, "forks": 0, "issues": 1, "pushed_at": "2023-11-07T01:08:05Z", "description": "Dynamically Replicating Duck"},
    {"full_name": "plurigrid/omega", "language": "Clojure", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2023-11-07T21:08:46Z", "description": ""},
    {"full_name": "plurigrid/microworlds", "language": "Rust", "stars": 3, "forks": 5, "issues": 3, "pushed_at": "2023-05-13T03:54:56Z", "description": ""},
    {"full_name": "plurigrid/agent", "language": "Python", "stars": 5, "forks": 1, "issues": 6, "pushed_at": "2023-03-31T18:45:23Z", "description": "Framework for agency amplification"},
    {"full_name": "plurigrid/vcg-auction", "language": "Rust", "stars": 7, "forks": 2, "issues": 1, "pushed_at": "2023-03-16T21:53:08Z", "description": "a simple contract that performs a VCG auction"},
    {"full_name": "plurigrid/bidder", "language": "Dart", "stars": 0, "forks": 0, "issues": 1, "pushed_at": "2023-03-15T15:23:22Z", "description": "simple flutter app for vcg auction bidding"},
    {"full_name": "plurigrid/plurigrid.github.io", "language": "HTML", "stars": 1, "forks": 2, "issues": 2, "pushed_at": "2023-01-20T03:27:34Z", "description": ""},
    {"full_name": "plurigrid/VPP", "language": "Julia", "stars": 0, "forks": 1, "issues": 0, "pushed_at": "2023-01-11T18:41:07Z", "description": "Hyperreal Power Plant"},
    {"full_name": "plurigrid/grid", "language": "TypeScript", "stars": 2, "forks": 1, "issues": 1, "pushed_at": "2023-01-02T11:55:55Z", "description": "Plurigrid Testnet #0: Edith Clarke"},
    {"full_name": "plurigrid/commons-contracts", "language": "Rust", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2022-09-09T09:20:11Z", "description": "CosmWasm contracts to implement Commons Stack"},
    ],
    "kubeflow": [
    {"full_name": "kubeflow/manifests", "language": "YAML", "stars": 1022, "forks": 1065, "issues": 22, "pushed_at": "2026-06-09T13:01:47Z", "description": "Kubeflow Community Distribution"},
    {"full_name": "kubeflow/trainer", "language": "Go", "stars": 2112, "forks": 963, "issues": 130, "pushed_at": "2026-06-09T12:52:00Z", "description": "Distributed AI Model Training and LLM Fine-Tuning on Kubernetes"},
    {"full_name": "kubeflow/mcp-apache-spark-history-server", "language": "Python", "stars": 174, "forks": 63, "issues": 21, "pushed_at": "2026-06-08T23:08:55Z", "description": "MCP Server and CLI for Apache Spark History Server"},
    {"full_name": "kubeflow/spark-operator", "language": "Python", "stars": 3126, "forks": 1488, "issues": 98, "pushed_at": "2026-06-08T21:15:28Z", "description": "Kubernetes operator for managing the lifecycle of Apache Spark applications"},
    {"full_name": "kubeflow/hub", "language": "Go", "stars": 175, "forks": 181, "issues": 43, "pushed_at": "2026-06-08T20:51:06Z", "description": "Model Registry for ML model metadata"},
    {"full_name": "kubeflow/pipelines", "language": "Python", "stars": 4153, "forks": 2004, "issues": 495, "pushed_at": "2026-06-09T13:22:42Z", "description": "Machine Learning Pipelines for Kubeflow"},
    {"full_name": "kubeflow/internal-acls", "language": "Go", "stars": 19, "forks": 389, "issues": 2, "pushed_at": "2026-06-08T16:06:10Z", "description": "Repository for group ACLs"},
    {"full_name": "kubeflow/notebooks", "language": None, "stars": 73, "forks": 118, "issues": 183, "pushed_at": "2026-06-06T01:03:23Z", "description": "Kubeflow Notebooks"},
    {"full_name": "kubeflow/kale", "language": "Python", "stars": 692, "forks": 155, "issues": 48, "pushed_at": "2026-06-05T21:02:41Z", "description": "Kubeflow's superfood for Data Scientists"},
    {"full_name": "kubeflow/community", "language": "Jupyter Notebook", "stars": 194, "forks": 258, "issues": 15, "pushed_at": "2026-06-05T17:29:18Z", "description": "Information about the Kubeflow community"},
    {"full_name": "kubeflow/website", "language": "HTML", "stars": 184, "forks": 922, "issues": 48, "pushed_at": "2026-06-05T02:01:44Z", "description": "Kubeflow Website"},
    {"full_name": "kubeflow/dashboard", "language": "TypeScript", "stars": 16, "forks": 57, "issues": 72, "pushed_at": "2026-06-09T01:51:08Z", "description": "Kubeflow Central Dashboard"},
    {"full_name": "kubeflow/katib", "language": "Python", "stars": 1685, "forks": 525, "issues": 119, "pushed_at": "2026-06-05T23:23:35Z", "description": "Automated Machine Learning on Kubernetes"},
    {"full_name": "kubeflow/sdk", "language": "Python", "stars": 120, "forks": 181, "issues": 137, "pushed_at": "2026-06-08T03:07:18Z", "description": "Universal Python SDK to run AI workloads on Kubernetes"},
    {"full_name": "kubeflow/mpi-operator", "language": "Go", "stars": 528, "forks": 235, "issues": 103, "pushed_at": "2026-06-02T14:30:58Z", "description": "Kubernetes Operator for MPI-based applications"},
    {"full_name": "kubeflow/pipelines-components", "language": "Python", "stars": 11, "forks": 43, "issues": 33, "pushed_at": "2026-06-04T17:39:10Z", "description": "Kubeflow Pipelines"},
    {"full_name": "kubeflow/mlflow-integration", "language": "Python", "stars": 6, "forks": 4, "issues": 3, "pushed_at": "2026-05-27T15:42:37Z", "description": None},
    {"full_name": "kubeflow/blog", "language": "Jupyter Notebook", "stars": 32, "forks": 62, "issues": 26, "pushed_at": "2026-05-25T13:02:24Z", "description": "Kubeflow blog"},
    {"full_name": "kubeflow/kubeflow", "language": None, "stars": 15713, "forks": 2672, "issues": 3, "pushed_at": "2026-05-24T11:31:41Z", "description": "Machine Learning Toolkit for Kubernetes"},
    {"full_name": "kubeflow/mcp-server", "language": "Python", "stars": 11, "forks": 20, "issues": 25, "pushed_at": "2026-05-12T10:14:24Z", "description": "MCP Server for AI-Assisted Development with Kubeflow Tools"},
    {"full_name": "kubeflow/arena", "language": "Go", "stars": 812, "forks": 190, "issues": 46, "pushed_at": "2026-05-07T06:46:17Z", "description": "A CLI for Kubeflow."},
    {"full_name": "kubeflow/docs-agent", "language": "Python", "stars": 37, "forks": 94, "issues": 151, "pushed_at": "2026-04-14T03:33:15Z", "description": "Kubeflow Documentation AI Agent"},
    {"full_name": "kubeflow/examples", "language": "Jsonnet", "stars": 1462, "forks": 756, "issues": 111, "pushed_at": "2025-04-14T01:54:52Z", "description": "A repository to host extended examples and tutorials"},
    {"full_name": "kubeflow/testing", "language": "Python", "stars": 60, "forks": 86, "issues": 33, "pushed_at": "2025-02-14T18:33:13Z", "description": "Test infrastructure and tooling for Kubeflow."},
    {"full_name": "kubeflow/kfp-tekton", "language": "TypeScript", "stars": 182, "forks": 123, "issues": 79, "pushed_at": "2024-11-19T12:23:51Z", "description": "Kubeflow Pipelines on Tekton"},
    {"full_name": "kubeflow/kubeflow", "language": None, "stars": 15713, "forks": 2672, "issues": 3, "pushed_at": "2026-05-24T11:31:41Z", "description": "Machine Learning Toolkit for Kubernetes"},
    {"full_name": "kubeflow/kfctl", "language": "Go", "stars": 182, "forks": 134, "issues": 94, "pushed_at": "2023-08-15T20:19:22Z", "description": "kfctl is a CLI for deploying and managing Kubeflow"},
    {"full_name": "kubeflow/common", "language": "Go", "stars": 53, "forks": 70, "issues": 40, "pushed_at": "2023-05-28T13:16:00Z", "description": "Common APIs and libraries for Kubeflow operators"},
    {"full_name": "kubeflow/fairing", "language": "Jsonnet", "stars": 337, "forks": 143, "issues": 134, "pushed_at": "2022-04-11T05:28:47Z", "description": "Python SDK for building, training, and deploying ML models"},
    {"full_name": "kubeflow/xgboost-operator", "language": "Python", "stars": 77, "forks": 53, "issues": 22, "pushed_at": "2021-12-01T18:00:10Z", "description": "Incubating project for xgboost operator"},
    {"full_name": "kubeflow/pytorch-operator", "language": "Jsonnet", "stars": 310, "forks": 143, "issues": 63, "pushed_at": "2021-12-01T17:44:48Z", "description": "PyTorch on Kubernetes"},
    {"full_name": "kubeflow/metadata", "language": "TypeScript", "stars": 123, "forks": 63, "issues": 38, "pushed_at": "2021-12-01T17:35:27Z", "description": "Repository for assets related to Metadata."},
    {"full_name": "kubeflow/code-intelligence", "language": "Jupyter Notebook", "stars": 56, "forks": 20, "issues": 64, "pushed_at": "2021-12-01T01:52:58Z", "description": "ML-Powered Developer Tools, using Kubeflow"},
    ],
    "TeglonLabs": [
    {"full_name": "TeglonLabs/jank-crane", "language": "C++", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-06-08T19:03:03Z", "description": "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps"},
    {"full_name": "TeglonLabs/mathpix-gem", "language": "Ruby", "stars": 2, "forks": 0, "issues": 11, "pushed_at": "2026-01-01T12:13:13Z", "description": "Transform mathematical images to LaTeX with security-first design"},
    {"full_name": "TeglonLabs/coin-flip-mcp", "language": "JavaScript", "stars": 0, "forks": 2, "issues": 1, "pushed_at": "2025-09-21T08:57:27Z", "description": "MCP server for flipping coins with varying degrees of randomness"},
    {"full_name": "TeglonLabs/monad-mcp-server", "language": None, "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2025-05-14T11:36:14Z", "description": "Monad MCP Server"},
    {"full_name": "TeglonLabs/topoi", "language": "Python", "stars": 0, "forks": 0, "issues": 1, "pushed_at": "2025-01-24T04:49:26Z", "description": None},
    ],
    "zubyul": [
    {"full_name": "zubyul/voice-observatory", "language": "Python", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-04-24T05:56:17Z", "description": "Passive macOS TUI observing voice-download pathways"},
    {"full_name": "zubyul/ghostel-emacs-worlds", "language": "GLSL", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-04-24T00:20:56Z", "description": "Ghostty config + ghostel family + alice/bob emacs-mods"},
    {"full_name": "zubyul/nash-tui", "language": "Rust", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-04-13T07:45:16Z", "description": "NASH token TUI: real-time candles via GeckoTerminal OHLCV"},
    {"full_name": "zubyul/nash-web", "language": "Rust", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-04-13T07:08:58Z", "description": "NASH token browser TUI via ratzilla WASM"},
    {"full_name": "zubyul/big-bad-plurigrid-quiz", "language": "Emacs Lisp", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-04-09T18:51:31Z", "description": "27 flashcards from recent activity + Emacs drill"},
    {"full_name": "zubyul/Gay.jl", "language": "Julia", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-03-28T11:30:01Z", "description": "Wide-gamut color sampling with splittable determinism"},
    {"full_name": "zubyul/kinesis-kb360pro", "language": "Python", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-03-26T10:29:40Z", "description": "Claude Code skill for Kinesis Advantage360 Pro keyboard"},
    {"full_name": "zubyul/gay-world", "language": "Python", "stars": 1, "forks": 1, "issues": 0, "pushed_at": "2026-03-26T04:03:39Z", "description": "Goblin world builder: each goblin is a world"},
    {"full_name": "zubyul/from-possible-worlds", "language": "TeX", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-03-16T03:14:55Z", "description": ""},
    {"full_name": "zubyul/tilelang-kernels", "language": "Python", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-03-16T02:31:13Z", "description": "TileLang GPU kernels for SplitMix64 color generation, GF(3) trit classification"},
    {"full_name": "zubyul/fleet-bootstrap", "language": "Shell", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-02-23T08:19:58Z", "description": ""},
    {"full_name": "zubyul/gay-terminal-colors", "language": "Clojure", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-02-21T07:38:14Z", "description": "Gay.jl world_terminal_fingerprint: SplitMix64 per-terminal color identity"},
    {"full_name": "zubyul/basin", "language": "Rust", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-02-13T10:31:47Z", "description": ""},
    {"full_name": "zubyul/openbci-visualizer", "language": "Zig", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-02-04T11:17:41Z", "description": ""},
    {"full_name": "zubyul/plurigrid-site", "language": "Svelte", "stars": 0, "forks": 1, "issues": 11, "pushed_at": "2026-02-04T03:20:08Z", "description": "Plurigrid world: site deployment"},
    {"full_name": "zubyul/repl", "language": "Python", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-02-04T01:08:15Z", "description": ""},
    {"full_name": "zubyul/vibesnipe", "language": "Move", "stars": 0, "forks": 0, "issues": 1, "pushed_at": "2026-01-30T22:36:03Z", "description": ""},
    {"full_name": "zubyul/zubyul.github.io", "language": "CSS", "stars": 1, "forks": 0, "issues": 0, "pushed_at": "2026-01-27T03:24:34Z", "description": ""},
    {"full_name": "zubyul/toad-warpify-extension", "language": "Python", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-01-17T07:48:40Z", "description": "Warpify extension for Toad - enables ACP agents to control terminal PTY"},
    {"full_name": "zubyul/thread-site", "language": "Haskell", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2025-12-23T23:53:27Z", "description": ""},
    {"full_name": "zubyul/GayMove", "language": "Move", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2025-12-18T09:40:08Z", "description": ""},
    {"full_name": "zubyul/gay-brain-world", "language": "Python", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2025-12-16T01:19:28Z", "description": "Gay.jl SPI colors for Moduleur Brain (Pico) + OpenBCI EEG"},
    {"full_name": "zubyul/cat-world", "language": "TypeScript", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2025-12-12T08:47:14Z", "description": "Cat gaze tracker - bird videos + eye detection"},
    {"full_name": "zubyul/hue-world", "language": "JavaScript", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2025-12-12T08:32:59Z", "description": "Terminal Vibe Snipe puzzle game with ANSI true color"},
    {"full_name": "zubyul/cascade-world", "language": "Python", "stars": 1, "forks": 0, "issues": 0, "pushed_at": "2025-09-19T18:25:12Z", "description": "Cascade development environment"},
    {"full_name": "zubyul/jonikas_lab_data_analysis_misc", "language": "Jupyter Notebook", "stars": 2, "forks": 0, "issues": 0, "pushed_at": "2023-08-16T20:24:40Z", "description": "various scripts used to process large genetic sequence data"},
    {"full_name": "zubyul/WGCNA", "language": "HTML", "stars": 2, "forks": 0, "issues": 0, "pushed_at": "2023-07-05T18:02:30Z", "description": "weighted gene correlation network analysis project"},
    {"full_name": "zubyul/Nikolova_lab_data_analysis", "language": "R", "stars": 2, "forks": 0, "issues": 0, "pushed_at": "2023-06-16T13:56:58Z", "description": "undergraduate thesis on cortical thickness and depression"},
    ],
    "migalkin": [
    {"full_name": "migalkin/NodePiece", "language": "Python", "stars": 144, "forks": 21, "issues": 0, "pushed_at": "2026-05-07T05:40:02Z", "description": "Compositional and Parameter-Efficient Representations for Large Knowledge Graphs (ICLR'22)"},
    {"full_name": "migalkin/StarE", "language": "Python", "stars": 89, "forks": 16, "issues": 1, "pushed_at": "2026-04-16T14:12:45Z", "description": "EMNLP 2020: Message Passing for Hyper-Relational Knowledge Graphs"},
    {"full_name": "migalkin/RWL", "language": "Python", "stars": 8, "forks": 1, "issues": 0, "pushed_at": "2026-05-28T20:19:20Z", "description": "Weisfeiler and Leman Go Relational (LOG 2022)"},
    {"full_name": "migalkin/NBFNet_mlx", "language": "Python", "stars": 10, "forks": 1, "issues": 1, "pushed_at": "2026-03-11T01:31:21Z", "description": "Neural Bellman-Ford networks implemented in MLX for Apple Silicon"},
    {"full_name": "migalkin/kgcourse2021", "language": "HTML", "stars": 25, "forks": 9, "issues": 0, "pushed_at": "2026-02-16T05:16:08Z", "description": "Materials for Knowledge Graphs course"},
    {"full_name": "migalkin/rambo", "language": "Rust", "stars": 3, "forks": 0, "issues": 1, "pushed_at": "2023-02-28T16:37:22Z", "description": None},
    ],
    "DJedamski": [
    {"full_name": "DJedamski/kaggle_ncaa18", "language": "Jupyter Notebook", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2018-02-26T16:33:24Z", "description": "Code for NCAA March Madness competition (2018)"},
    {"full_name": "DJedamski/Kaggle", "language": None, "stars": 1, "forks": 0, "issues": 0, "pushed_at": "2023-04-21T01:42:35Z", "description": None},
    {"full_name": "DJedamski/EDA", "language": "R", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2014-11-09T17:00:39Z", "description": "Coursera Project"},
    {"full_name": "DJedamski/School", "language": "R", "stars": 1, "forks": 1, "issues": 0, "pushed_at": "2023-04-21T01:42:33Z", "description": "A couple small projects from grad school"},
    ],
    "wasita": [
    {"full_name": "wasita/wasita.github.io", "language": "Svelte", "stars": 1, "forks": 0, "issues": 8, "pushed_at": "2026-06-01T04:15:14Z", "description": "personal website"},
    {"full_name": "wasita/wm-cv", "language": "Svelte", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-05-13T05:29:08Z", "description": "Academic CV as a single page web app"},
    {"full_name": "wasita/vocoder", "language": "JavaScript", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-05-06T05:14:03Z", "description": None},
    {"full_name": "wasita/magic-garden", "language": "Python", "stars": 2, "forks": 1, "issues": 1, "pushed_at": "2026-04-22T21:16:43Z", "description": "a bot for the magic garden discord activity game"},
    {"full_name": "wasita/send2kobo", "language": "TypeScript", "stars": 1, "forks": 0, "issues": 0, "pushed_at": "2026-05-19T02:59:26Z", "description": "Website for sending books to your kobo e-reader"},
    {"full_name": "wasita/wins-search", "language": "CSS", "stars": 1, "forks": 0, "issues": 0, "pushed_at": "2023-06-03T19:01:11Z", "description": "Women in Network Science (WiNS) member list website"},
    ],
    "kristinezheng": [
    {"full_name": "kristinezheng/kristinezheng.github.io", "language": "HTML", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-06-07T22:53:10Z", "description": None},
    {"full_name": "kristinezheng/lookit-jenga", "language": "Jupyter Notebook", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2024-05-16T18:29:05Z", "description": "Lookit study for 9.85"},
    {"full_name": "kristinezheng/Green-Machine", "language": "Python", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2021-09-19T05:33:04Z", "description": "HackMIT 2021: Sustainability Track"},
    ],
    "M1shaaa": [
    {"full_name": "M1shaaa/M1shaaa", "language": None, "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-02-04T19:32:04Z", "description": "Config files for my GitHub profile."},
    {"full_name": "M1shaaa/lab-bookshelf-", "language": "TypeScript", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2024-12-31T05:11:18Z", "description": None},
    {"full_name": "M1shaaa/Python-Lookit-Uploads", "language": "Python", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2024-02-15T22:59:37Z", "description": "random projects"},
    ],
    "bmorphism": [
    {"full_name": "bmorphism/Gay.jl", "language": "Julia", "stars": 1, "forks": 0, "issues": 189, "pushed_at": "2026-06-09T00:36:44Z", "description": "Wide-gamut color sampling with splittable determinism (Pigeons.jl SPI pattern) + LispSyntax"},
    {"full_name": "bmorphism/world", "language": "Python", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-06-02T06:49:02Z", "description": "Local worlds launcher for SA3, jank, and world proofs."},
    {"full_name": "bmorphism/oxgame", "language": "OCaml", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-05-15T09:53:27Z", "description": "Stellar resolution and open-game composition for OCaml"},
    {"full_name": "bmorphism/nanoclj-zig", "language": "Zig", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-05-07T20:12:15Z", "description": None},
    {"full_name": "bmorphism/zig-syrup", "language": "Zig", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-05-07T19:49:05Z", "description": "Embeddable OCapN Syrup encoder/decoder in Zig"},
    {"full_name": "bmorphism/boxxy", "language": "Move", "stars": 0, "forks": 1, "issues": 0, "pushed_at": "2026-04-30T03:35:47Z", "description": None},
    {"full_name": "bmorphism/postweb", "language": "Go", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-04-09T10:51:57Z", "description": "postweb — evolved from prepostweb"},
    {"full_name": "bmorphism/shitcoin", "language": "Python", "stars": 5, "forks": 0, "issues": 0, "pushed_at": "2026-04-08T08:07:08Z", "description": "gets denom for cw20 assets for permissionless degeneracy in IBC"},
    {"full_name": "bmorphism/magic-world-org", "language": "Python", "stars": 1, "forks": 0, "issues": 0, "pushed_at": "2026-04-05T07:03:50Z", "description": "Magic World Org (Local MLX)"},
    {"full_name": "bmorphism/ocaml-mcp-sdk", "language": "OCaml", "stars": 61, "forks": 2, "issues": 0, "pushed_at": "2026-03-16T05:24:25Z", "description": "OCaml SDK for Model Context Protocol"},
    {"full_name": "bmorphism/flox-mcp-bb", "language": "Clojure", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-02-12T02:45:43Z", "description": "Open-source MCP server for Flox — Babashka/Clojure"},
    {"full_name": "bmorphism/vibesnipe-market", "language": "Move", "stars": 0, "forks": 0, "issues": 9, "pushed_at": "2026-02-05T10:23:25Z", "description": None},
    {"full_name": "bmorphism/anti-bullshit-mcp-server", "language": "JavaScript", "stars": 23, "forks": 7, "issues": 1, "pushed_at": "2026-01-16T08:54:58Z", "description": "MCP server for analyzing claims and detecting manipulation"},
    {"full_name": "bmorphism/vibespace-mcp-go-ternary", "language": "HTML", "stars": 0, "forks": 1, "issues": 3, "pushed_at": "2026-01-11T12:50:40Z", "description": "MCP experience for vibes and worlds with NATS streaming and balanced ternary"},
    {"full_name": "bmorphism/open-location-code-zig", "language": "Zig", "stars": 3, "forks": 0, "issues": 0, "pushed_at": "2025-12-30T19:33:45Z", "description": "Open Location Code (Plus Codes) for Zig"},
    {"full_name": "bmorphism/bafishka", "language": "Clojure", "stars": 1, "forks": 0, "issues": 0, "pushed_at": "2025-12-19T09:38:00Z", "description": "Rust-native Fish shell-friendly file operations with Steel-backed SCI Clojure evaluation"},
    {"full_name": "bmorphism/multiverse-color-game", "language": "Julia", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2025-12-12T05:28:11Z", "description": "2+1D Holographic Color Matching Game — Hamkins multiverse + Gay.jl chromatic identity"},
    {"full_name": "bmorphism/say-mcp-server", "language": "JavaScript", "stars": 20, "forks": 9, "issues": 3, "pushed_at": "2025-01-07T03:15:18Z", "description": "MCP server for macOS text-to-speech functionality"},
    {"full_name": "bmorphism/manifold-mcp-server", "language": "JavaScript", "stars": 14, "forks": 9, "issues": 5, "pushed_at": "2025-01-11T10:36:58Z", "description": "MCP server for interacting with Manifold Markets prediction markets"},
    {"full_name": "bmorphism/babashka-mcp-server", "language": "JavaScript", "stars": 19, "forks": 6, "issues": 3, "pushed_at": "2025-01-05T11:09:42Z", "description": "A Model Context Protocol server for Babashka Clojure"},
    {"full_name": "bmorphism/penrose-mcp", "language": "JavaScript", "stars": 10, "forks": 4, "issues": 0, "pushed_at": "2025-01-20T21:44:55Z", "description": "Penrose server for the Infinity-Topos environment"},
    {"full_name": "bmorphism/nats-mcp-server", "language": None, "stars": 7, "forks": 3, "issues": 2, "pushed_at": "2025-01-06T23:33:41Z", "description": "MCP server for NATS messaging system"},
    {"full_name": "bmorphism/marginalia-mcp-server", "language": "JavaScript", "stars": 8, "forks": 6, "issues": 0, "pushed_at": "2025-01-06T05:47:24Z", "description": "MCP server for managing marginalia and annotations"},
    {"full_name": "bmorphism/hypernym-mcp-server", "language": "JavaScript", "stars": 6, "forks": 5, "issues": 0, "pushed_at": "2025-04-02T21:21:08Z", "description": None},
    {"full_name": "bmorphism/risc0-cosmwasm-example", "language": "Rust", "stars": 23, "forks": 2, "issues": 1, "pushed_at": "2022-10-20T23:50:40Z", "description": "CosmWasm + zkVM RISC-V EFI template"},
    {"full_name": "bmorphism/penumbra-mcp", "language": "JavaScript", "stars": 5, "forks": 6, "issues": 3, "pushed_at": "2025-01-07T01:15:23Z", "description": "MCP server for interacting with Penumbra blockchain"},
    {"full_name": "bmorphism/slowtime-mcp-server", "language": "TypeScript", "stars": 3, "forks": 5, "issues": 6, "pushed_at": "2025-01-02T01:23:33Z", "description": "MCP server for secure time-based operations with timing attack protection"},
    {"full_name": "bmorphism/GeoACSets.jl", "language": "Julia", "stars": 0, "forks": 1, "issues": 1, "pushed_at": "2026-01-19T13:57:13Z", "description": "Categorical data structures with geospatial capabilities"},
    {"full_name": "bmorphism/monero-rental-hash-war", "language": "Haskell", "stars": 1, "forks": 0, "issues": 0, "pushed_at": "2025-10-05T23:08:54Z", "description": "Compositional OpenGame analysis of Monero rental hash war"},
    {"full_name": "bmorphism/graphistry-mcp", "language": "Python", "stars": 2, "forks": 0, "issues": 0, "pushed_at": "2025-05-06T17:34:24Z", "description": "Graphistry MCP integration for graph visualization"},
    {"full_name": "bmorphism/zeldar", "language": "Python", "stars": 1, "forks": 0, "issues": 1, "pushed_at": "2025-08-26T15:16:21Z", "description": "Burning Man Art Robot"},
    {"full_name": "bmorphism/whale", "language": "MATLAB", "stars": 2, "forks": 0, "issues": 0, "pushed_at": "2025-09-04T06:55:21Z", "description": "omniglot + sperm whale codas = metawhaling"},
    ],
    "AustinCStone": [
    {"full_name": "AustinCStone/EpsteinSearch", "language": "Python", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2026-02-11T01:10:57Z", "description": None},
    {"full_name": "AustinCStone/bmforkupdate", "language": "Python", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2025-05-09T04:50:16Z", "description": None},
    {"full_name": "AustinCStone/bmfork", "language": "Python", "stars": 0, "forks": 0, "issues": 1, "pushed_at": "2025-05-09T04:18:54Z", "description": None},
    {"full_name": "AustinCStone/TextGAN", "language": "Python", "stars": 92, "forks": 30, "issues": 5, "pushed_at": "2025-03-03T13:26:32Z", "description": "A generative adversarial network for text generation, written in TensorFlow."},
    {"full_name": "AustinCStone/StereoVisionMRF", "language": "Python", "stars": 11, "forks": 4, "issues": 0, "pushed_at": "2026-04-01T07:39:41Z", "description": "Recover 3D geometry from stereo images with MRF"},
    {"full_name": "AustinCStone/TFBirds", "language": "Python", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2019-01-30T08:07:22Z", "description": "Bird flocking simulator in TensorFlow."},
    {"full_name": "AustinCStone/Z-order-curve", "language": "Python", "stars": 0, "forks": 0, "issues": 0, "pushed_at": "2019-06-09T02:53:43Z", "description": "Demo implementation of things related to space filling z-order curve"},
    {"full_name": "AustinCStone/SpectralClustering", "language": "Python", "stars": 3, "forks": 2, "issues": 0, "pushed_at": "2021-04-16T08:46:36Z", "description": "Implementing spectral clustering"},
    {"full_name": "AustinCStone/StructureFromMotion", "language": "Python", "stars": 1, "forks": 0, "issues": 0, "pushed_at": "2019-04-26T19:43:12Z", "description": "Recover 3D geometry from videos"},
    {"full_name": "AustinCStone/logisticRegressionHaskell", "language": "Haskell", "stars": 1, "forks": 0, "issues": 0, "pushed_at": "2018-02-02T13:34:28Z", "description": "Logistic regression in Haskell"},
    ],
}

# ── Insert world_increments + repo_snapshots ───────────────────────────────────
increment_id = 1
repo_id = 1

for org_user, repos in REPOS.items():
    for repo in repos:
        trit, color, name = gf3(increment_id)
        h = snap_hash(repo["full_name"], repo["pushed_at"])
        con.execute("""
            INSERT INTO world_increments VALUES (?,NOW(),?,?,?,'repo_snapshot',?,?,?,?,?)
        """, [increment_id, trit, color, name, org_user, "push",
              repo["full_name"], org_user, h])
        parts = repo["full_name"].split("/", 1)
        con.execute("""
            INSERT INTO repo_snapshots VALUES (?,NOW(),?,?,?,?,?,?,?,?,?,?)
        """, [repo_id, increment_id, org_user,
              parts[1] if len(parts) > 1 else repo["full_name"],
              repo["full_name"], repo.get("language"), repo.get("stars", 0),
              repo.get("forks", 0), repo.get("issues", 0),
              repo.get("pushed_at"), repo.get("description")])
        increment_id += 1
        repo_id += 1

print(f"Inserted {increment_id-1} increments, {repo_id-1} repo snapshots")

# ── Aptos snapshots ────────────────────────────────────────────────────────────
APTOS_BALANCES = {
    "alice": ("0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b", 0.0),
    "bob":   ("0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d", 0.0),
    "A": ("0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a", 0.0),
    "B": ("0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13", 0.0),
    "C": ("0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e", 0.0),
    "D": ("0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1", 0.0),
    "E": ("0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36", 0.0),
    "F": ("0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71", 0.0),
    "G": ("0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32", 0.0),
    "H": ("0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f", 0.0),
    "I": ("0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9", 0.0),
    "J": ("0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54", 0.0),
    "K": ("0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4", 0.0),
    "L": ("0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9", 0.0),
    "M": ("0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9", 0.0),
    "N": ("0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c", 0.0),
    "O": ("0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d", 0.0),
    "P": ("0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948", 0.0),
    "Q": ("0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9", 0.0),
    "R": ("0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10", 0.0),
    "S": ("0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386", 0.0),
    "T": ("0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588", 0.0),
    "U": ("0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956", 0.0),
    "V": ("0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3", 0.0),
    "W": ("0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0", 0.0),
    "X": ("0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d", 0.0),
    "Y": ("0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4", 0.0),
    "Z": ("0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c", 0.0),
}

for world, (addr, bal) in APTOS_BALANCES.items():
    con.execute("INSERT INTO aptos_snapshots VALUES (NOW(),?,?,?)", [world, addr, bal])
print(f"Inserted {len(APTOS_BALANCES)} Aptos balance records")

# ── Multisig probes ────────────────────────────────────────────────────────────
MULTISIG = [
    ("A-B", "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2, True),
    ("A-G", "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2, True),
    ("Y-Z", "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2, True),
    ("S-T", "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2, True),
    ("V-W", "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2, True),
]
for pair, addr, sigs, healthy in MULTISIG:
    con.execute("INSERT INTO multisig_probes VALUES (NOW(),?,?,?,?)", [pair, addr, sigs, healthy])
print("Inserted 5 multisig probe records")

# ── MNX (unavailable) ─────────────────────────────────────────────────────────
con.execute("INSERT INTO mnx_snapshots VALUES (NOW(),'UNAVAILABLE','MNX_TESTNET_VERCEL_AUTH','unavailable',NULL,NULL)")
print("Inserted MNX unavailable marker")

con.close()
print("All data committed to DuckDB.")
