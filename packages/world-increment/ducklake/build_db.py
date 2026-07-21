#!/usr/bin/env python3
"""Build world-increments DuckDB from sweep data."""

import duckdb
import hashlib
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "world-increments.duckdb")

PLURIGRID_REPOS = [{"full_name": "plurigrid/asi", "name": "asi", "language": "HTML", "stargazers_count": 31, "forks_count": 10, "open_issues_count": 4, "pushed_at": "2026-07-10T09:47:39Z", "description": "everything is topological chemputer!"}, {"full_name": "plurigrid/gorj", "name": "gorj", "language": "Clojure", "stargazers_count": 1, "forks_count": 0, "open_issues_count": 1286, "pushed_at": "2026-07-21T01:12:44Z", "description": "forj + Rama topology nREPL routing + GF(3) gay trit coloring for compositional open game REPL orchestration"}, {"full_name": "plurigrid/shrimp", "name": "shrimp", "language": None, "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2026-07-03T01:24:20Z", "description": "Jank worked example: shrimp"}, {"full_name": "plurigrid/place", "name": "place", "language": "TeX", "stargazers_count": 1, "forks_count": 2, "open_issues_count": 14, "pushed_at": "2026-07-14T09:11:33Z", "description": None}, {"full_name": "plurigrid/eirobri", "name": "eirobri", "language": "Clojure", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 30, "pushed_at": "2026-07-14T02:23:51Z", "description": "EiRoBri replay world"}, {"full_name": "plurigrid/nash-portal", "name": "nash-portal", "language": "Rust", "stargazers_count": 2, "forks_count": 2, "open_issues_count": 1, "pushed_at": "2026-05-19T01:49:59Z", "description": "NASH token TUI in the browser"}, {"full_name": "plurigrid/zig-syrup", "name": "zig-syrup", "language": "Zig", "stargazers_count": 2, "forks_count": 2, "open_issues_count": 0, "pushed_at": "2026-04-30T03:52:16Z", "description": "High-performance Zig implementation of OCapN Syrup with CapTP optimizations"}, {"full_name": "plurigrid/asi-skills", "name": "asi-skills", "language": "Julia", "stargazers_count": 3, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2026-04-26T08:09:26Z", "description": "69 skills with Galois Hole Type accessibility"}, {"full_name": "plurigrid/bci-blue-share", "name": "bci-blue-share", "language": "JavaScript", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2026-04-26T07:08:03Z", "description": "BCI signal infrastructure"}, {"full_name": "plurigrid/nanoclj-zig", "name": "nanoclj-zig", "language": "Zig", "stargazers_count": 1, "forks_count": 1, "open_issues_count": 20, "pushed_at": "2026-04-25T07:29:09Z", "description": "NaN-boxed Clojure interpreter in Zig"}, {"full_name": "plurigrid/spi-race", "name": "spi-race", "language": "Swift", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2026-04-21T19:31:56Z", "description": "Splitmix Parallel Integrity"}, {"full_name": "plurigrid/reafference", "name": "reafference", "language": "HTML", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2026-04-16T05:21:49Z", "description": "Reafference adaptation workspace"}, {"full_name": "plurigrid/web-browser", "name": "web-browser", "language": "Rust", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2026-04-10T02:54:47Z", "description": None}, {"full_name": "plurigrid/vivarium", "name": "vivarium", "language": "Clojure", "stargazers_count": 1, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2026-04-08T08:38:37Z", "description": None}, {"full_name": "plurigrid/flowglad-rs", "name": "flowglad-rs", "language": "Rust", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2026-04-08T07:56:15Z", "description": None}, {"full_name": "plurigrid/tree-sitter-nanoclj-zig", "name": "tree-sitter-nanoclj-zig", "language": "C", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2026-04-04T07:48:21Z", "description": "Tree-sitter grammar for nanoclj-zig"}, {"full_name": "plurigrid/forester", "name": "forester", "language": "XSLT", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2026-03-30T01:32:26Z", "description": None}, {"full_name": "plurigrid/gatomic", "name": "gatomic", "language": "Clojure", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2026-03-30T00:54:48Z", "description": "Deterministic color identity store"}, {"full_name": "plurigrid/nblm-flashcards", "name": "nblm-flashcards", "language": "Hy", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2026-03-26T08:23:01Z", "description": "NotebookLM Enterprise flashcard pipeline"}, {"full_name": "plurigrid/graded-optic", "name": "graded-optic", "language": "Haskell", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2026-02-08T16:10:16Z", "description": "Semiring-graded bidirectional processes"}, {"full_name": "plurigrid/agent-o-rama", "name": "agent-o-rama", "language": "Clojure", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2026-01-02T01:09:22Z", "description": None}, {"full_name": "plurigrid/aptos-wallet-ruby", "name": "aptos-wallet-ruby", "language": "Ruby", "stargazers_count": 1, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2025-09-30T22:47:22Z", "description": None}, {"full_name": "plurigrid/duck-kanban", "name": "duck-kanban", "language": "Rust", "stargazers_count": 1, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2025-09-26T20:18:38Z", "description": "Duck intelligence kanban system"}, {"full_name": "plurigrid/ontology", "name": "ontology", "language": "JavaScript", "stargazers_count": 8, "forks_count": 9, "open_issues_count": 16, "pushed_at": "2025-05-27T18:18:34Z", "description": "autopoietic ergodicity and embodied gradualism"}, {"full_name": "plurigrid/Plurigraph", "name": "Plurigraph", "language": "JavaScript", "stargazers_count": 3, "forks_count": 5, "open_issues_count": 4, "pushed_at": "2025-01-05T08:39:09Z", "description": "Plurigrid knowledge base"}, {"full_name": "plurigrid/act", "name": "act", "language": "Python", "stargazers_count": 3, "forks_count": 1, "open_issues_count": 4, "pushed_at": "2024-07-26T08:27:08Z", "description": "building blocks for cognitive category theory"}, {"full_name": "plurigrid/StochFlow", "name": "StochFlow", "language": "Python", "stargazers_count": 4, "forks_count": 1, "open_issues_count": 0, "pushed_at": "2024-03-20T23:34:57Z", "description": "stochastic interpolant models"}, {"full_name": "plurigrid/agent", "name": "agent", "language": "Python", "stargazers_count": 5, "forks_count": 1, "open_issues_count": 6, "pushed_at": "2023-03-31T18:45:23Z", "description": "Framework for agency amplification"}, {"full_name": "plurigrid/vcg-auction", "name": "vcg-auction", "language": "Rust", "stargazers_count": 7, "forks_count": 3, "open_issues_count": 1, "pushed_at": "2023-03-16T21:53:08Z", "description": "a simple contract that performs a VCG auction"}, {"full_name": "plurigrid/microworlds", "name": "microworlds", "language": "Rust", "stargazers_count": 3, "forks_count": 5, "open_issues_count": 3, "pushed_at": "2023-05-13T03:54:56Z", "description": None}]

KUBEFLOW_REPOS = [{"full_name": "kubeflow/kubeflow", "name": "kubeflow", "language": None, "stargazers_count": 15786, "forks_count": 2687, "open_issues_count": 0, "pushed_at": "2026-07-20T22:08:12Z", "description": "Machine Learning Toolkit for Kubernetes"}, {"full_name": "kubeflow/katib", "name": "katib", "language": "Python", "stargazers_count": 1692, "forks_count": 533, "open_issues_count": 103, "pushed_at": "2026-07-20T22:47:05Z", "description": "Automated Machine Learning on Kubernetes"}, {"full_name": "kubeflow/pipelines", "name": "pipelines", "language": "Python", "stargazers_count": 4169, "forks_count": 2047, "open_issues_count": 436, "pushed_at": "2026-07-20T20:10:20Z", "description": "Machine Learning Pipelines for Kubeflow"}, {"full_name": "kubeflow/trainer", "name": "trainer", "language": "Go", "stargazers_count": 2152, "forks_count": 991, "open_issues_count": 117, "pushed_at": "2026-07-20T16:55:19Z", "description": "Distributed AI Model Training and LLM Fine-Tuning on Kubernetes"}, {"full_name": "kubeflow/spark-operator", "name": "spark-operator", "language": "Python", "stargazers_count": 3140, "forks_count": 1501, "open_issues_count": 108, "pushed_at": "2026-07-20T02:27:27Z", "description": "Kubernetes operator for Apache Spark"}, {"full_name": "kubeflow/community-distribution", "name": "community-distribution", "language": "YAML", "stargazers_count": 1029, "forks_count": 1072, "open_issues_count": 25, "pushed_at": "2026-07-20T14:36:19Z", "description": "Kubeflow Community Distribution"}, {"full_name": "kubeflow/hub", "name": "hub", "language": "Go", "stargazers_count": 178, "forks_count": 188, "open_issues_count": 37, "pushed_at": "2026-07-20T19:15:08Z", "description": "Model Registry"}, {"full_name": "kubeflow/sdk", "name": "sdk", "language": "Python", "stargazers_count": 126, "forks_count": 204, "open_issues_count": 175, "pushed_at": "2026-07-20T15:39:38Z", "description": "Universal Python SDK for AI workloads on Kubernetes"}, {"full_name": "kubeflow/notebooks", "name": "notebooks", "language": None, "stargazers_count": 74, "forks_count": 131, "open_issues_count": 172, "pushed_at": "2026-07-20T14:49:30Z", "description": "Kubeflow Notebooks"}, {"full_name": "kubeflow/mcp-server", "name": "mcp-server", "language": "Python", "stargazers_count": 28, "forks_count": 35, "open_issues_count": 38, "pushed_at": "2026-07-19T16:08:53Z", "description": "MCP Server for AI-Assisted Development with Kubeflow Tools"}, {"full_name": "kubeflow/mcp-apache-spark-history-server", "name": "mcp-apache-spark-history-server", "language": "Python", "stargazers_count": 183, "forks_count": 65, "open_issues_count": 20, "pushed_at": "2026-07-16T20:05:30Z", "description": "MCP Server and CLI for Apache Spark History Server"}, {"full_name": "kubeflow/examples", "name": "examples", "language": "Jsonnet", "stargazers_count": 1460, "forks_count": 756, "open_issues_count": 111, "pushed_at": "2026-06-16T17:59:01Z", "description": "Extended examples and tutorials"}, {"full_name": "kubeflow/arena", "name": "arena", "language": "Go", "stargazers_count": 815, "forks_count": 196, "open_issues_count": 58, "pushed_at": "2026-07-16T11:51:25Z", "description": "A CLI for Kubeflow"}]

TEGLON_REPOS = [{"full_name": "TeglonLabs/jank-crane", "name": "jank-crane", "language": "C++", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2026-06-08T19:03:37Z", "description": "crane-jank converged-IR hub"}, {"full_name": "TeglonLabs/mathpix-gem", "name": "mathpix-gem", "language": "Ruby", "stargazers_count": 2, "forks_count": 0, "open_issues_count": 11, "pushed_at": "2026-01-01T12:13:16Z", "description": "Transform mathematical images to LaTeX"}, {"full_name": "TeglonLabs/coin-flip-mcp", "name": "coin-flip-mcp", "language": "JavaScript", "stargazers_count": 0, "forks_count": 2, "open_issues_count": 1, "pushed_at": "2025-03-16T01:31:45Z", "description": "MCP server for flipping coins"}, {"full_name": "TeglonLabs/monad-mcp-server", "name": "monad-mcp-server", "language": None, "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2025-05-14T17:53:01Z", "description": "Monad MCP Server"}, {"full_name": "TeglonLabs/topoi", "name": "topoi", "language": "Python", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 1, "pushed_at": "2025-01-24T06:47:38Z", "description": None}]

BMORPHISM_REPOS = [{"full_name": "bmorphism/Gay.jl", "name": "Gay.jl", "language": "Julia", "stargazers_count": 2, "forks_count": 1, "open_issues_count": 187, "pushed_at": "2026-07-20T09:41:37Z", "description": "Wide-gamut color sampling with splittable determinism"}, {"full_name": "bmorphism/anti-bullshit-mcp-server", "name": "anti-bullshit-mcp-server", "language": "JavaScript", "stargazers_count": 22, "forks_count": 7, "open_issues_count": 1, "pushed_at": "2026-07-12T19:31:54Z", "description": "MCP server for analyzing claims"}, {"full_name": "bmorphism/gay-chat", "name": "gay-chat", "language": "Scheme", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2026-07-14T21:00:00Z", "description": "gay://chat operationalization"}, {"full_name": "bmorphism/penrose-mcp", "name": "penrose-mcp", "language": "JavaScript", "stargazers_count": 9, "forks_count": 4, "open_issues_count": 0, "pushed_at": "2026-06-24T15:36:16Z", "description": "Penrose server for the Infinity-Topos environment"}, {"full_name": "bmorphism/ocaml-mcp-sdk", "name": "ocaml-mcp-sdk", "language": "OCaml", "stargazers_count": 61, "forks_count": 2, "open_issues_count": 0, "pushed_at": "2026-05-08T16:50:34Z", "description": "OCaml SDK for Model Context Protocol"}, {"full_name": "bmorphism/babashka-mcp-server", "name": "babashka-mcp-server", "language": "JavaScript", "stargazers_count": 19, "forks_count": 6, "open_issues_count": 3, "pushed_at": "2026-06-05T13:16:11Z", "description": "MCP server for Babashka"}, {"full_name": "bmorphism/say-mcp-server", "name": "say-mcp-server", "language": "JavaScript", "stargazers_count": 20, "forks_count": 9, "open_issues_count": 3, "pushed_at": "2026-03-19T23:11:59Z", "description": "MCP server for macOS text-to-speech"}, {"full_name": "bmorphism/manifold-mcp-server", "name": "manifold-mcp-server", "language": "JavaScript", "stargazers_count": 14, "forks_count": 9, "open_issues_count": 5, "pushed_at": "2026-04-15T19:54:28Z", "description": "MCP server for Manifold Markets"}, {"full_name": "bmorphism/risc0-cosmwasm-example", "name": "risc0-cosmwasm-example", "language": "Rust", "stargazers_count": 23, "forks_count": 2, "open_issues_count": 1, "pushed_at": "2025-05-21T13:35:37Z", "description": "CosmWasm + zkVM RISC-V EFI template"}, {"full_name": "bmorphism/whale", "name": "whale", "language": "MATLAB", "stargazers_count": 2, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2026-04-20T15:04:09Z", "description": "omniglot + sperm whale codas"}]

ZUBYUL_REPOS = [{"full_name": "zubyul/voice-observatory", "name": "voice-observatory", "language": "Python", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2026-04-24T05:56:20Z", "description": "Passive macOS TUI observing voice-download pathways"}, {"full_name": "zubyul/ghostel-emacs-worlds", "name": "ghostel-emacs-worlds", "language": "GLSL", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2026-04-24T00:21:00Z", "description": "Ghostty config + ghostel family"}, {"full_name": "zubyul/big-bad-plurigrid-quiz", "name": "big-bad-plurigrid-quiz", "language": "Emacs Lisp", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2026-04-09T18:51:35Z", "description": "27 flashcards from bmorphism/plurigrid/zubyul activity"}, {"full_name": "zubyul/Gay.jl", "name": "Gay.jl", "language": "Julia", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2026-03-28T11:30:07Z", "description": "Wide-gamut color sampling with splittable determinism"}, {"full_name": "zubyul/gay-world", "name": "gay-world", "language": "Python", "stargazers_count": 1, "forks_count": 1, "open_issues_count": 0, "pushed_at": "2026-04-05T06:54:03Z", "description": "Goblin world builder"}, {"full_name": "zubyul/jonikas_lab_data_analysis_misc", "name": "jonikas_lab_data_analysis_misc", "language": "Jupyter Notebook", "stargazers_count": 2, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2026-03-26T09:05:21Z", "description": "various scripts for large genetic sequence data"}]

SOCIAL_REPOS = [
    {"full_name": "migalkin/NodePiece", "name": "NodePiece", "language": "Python", "stargazers_count": 144, "forks_count": 21, "open_issues_count": 0, "pushed_at": "2026-05-07T05:40:02Z", "description": "Compositional and Parameter-Efficient Representations for Large Knowledge Graphs (ICLR 22)"},
    {"full_name": "migalkin/StarE", "name": "StarE", "language": "Python", "stargazers_count": 89, "forks_count": 16, "open_issues_count": 1, "pushed_at": "2026-04-16T14:12:45Z", "description": "EMNLP 2020: Message Passing for Hyper-Relational Knowledge Graphs"},
    {"full_name": "migalkin/NBFNet_mlx", "name": "NBFNet_mlx", "language": "Python", "stargazers_count": 10, "forks_count": 1, "open_issues_count": 1, "pushed_at": "2026-03-11T01:31:21Z", "description": "Neural Bellman-Ford networks in MLX"},
    {"full_name": "migalkin/kgcourse2021", "name": "kgcourse2021", "language": "HTML", "stargazers_count": 24, "forks_count": 8, "open_issues_count": 0, "pushed_at": "2026-07-10T15:40:00Z", "description": "Knowledge Graphs course materials"},
    {"full_name": "wasita/wasita.github.io", "name": "wasita.github.io", "language": "Svelte", "stargazers_count": 1, "forks_count": 0, "open_issues_count": 8, "pushed_at": "2026-07-20T18:18:51Z", "description": "personal website"},
    {"full_name": "wasita/magic-garden", "name": "magic-garden", "language": "Python", "stargazers_count": 2, "forks_count": 1, "open_issues_count": 1, "pushed_at": "2026-04-22T21:16:43Z", "description": "bot for magic garden discord"},
    {"full_name": "AustinCStone/TextGAN", "name": "TextGAN", "language": "Python", "stargazers_count": 92, "forks_count": 30, "open_issues_count": 5, "pushed_at": "2025-03-03T13:26:32Z", "description": "A generative adversarial network for text generation"},
    {"full_name": "AustinCStone/byteruckus", "name": "byteruckus", "language": "HTML", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2026-07-15T05:19:33Z", "description": None},
    {"full_name": "kristinezheng/kristinezheng.github.io", "name": "kristinezheng.github.io", "language": "HTML", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2026-07-01T20:57:48Z", "description": None},
    {"full_name": "DJedamski/kaggle_ncaa18", "name": "kaggle_ncaa18", "language": "Jupyter Notebook", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2018-02-26T16:33:24Z", "description": "Code for NCAA March Madness competition"},
    {"full_name": "M1shaaa/lab-bookshelf-", "name": "lab-bookshelf-", "language": "TypeScript", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2024-12-31T05:11:18Z", "description": None},
]

APTOS_WALLETS = [
    ("alice", "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b"),
    ("bob", "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d"),
    ("A", "0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a"),
    ("B", "0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13"),
    ("C", "0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e"),
    ("D", "0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1"),
    ("E", "0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36"),
    ("F", "0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71"),
    ("G", "0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32"),
    ("H", "0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f"),
    ("I", "0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9"),
    ("J", "0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54"),
    ("K", "0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4"),
    ("L", "0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9"),
    ("M", "0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9"),
    ("N", "0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c"),
    ("O", "0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d"),
    ("P", "0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948"),
    ("Q", "0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9"),
    ("R", "0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10"),
    ("S", "0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386"),
    ("T", "0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588"),
    ("U", "0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956"),
    ("V", "0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3"),
    ("W", "0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0"),
    ("X", "0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d"),
    ("Y", "0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4"),
    ("Z", "0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c"),
]

MULTISIG_PROBES = [
    ("A-B", "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2, True),
    ("A-G", "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2, True),
    ("Y-Z", "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2, True),
    ("S-T", "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2, True),
    ("V-W", "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2, True),
]

GF3_COLORS = [
    (0, "#d3869b", "ERGODIC"),
    (1, "#b8bb26", "PLUS"),
    (2, "#cc241d", "MINUS"),
]


def gf3(id_):
    t = id_ % 3
    trit, color, name = GF3_COLORS[t]
    return trit, color, name


def snap_hash(source_name, repo_name, pushed_at):
    raw = f"{source_name}:{repo_name}:{pushed_at}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def build_db():
    con = duckdb.connect(DB_PATH)

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
        )
    """)
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
        )
    """)
    con.execute("""
        CREATE TABLE IF NOT EXISTS aptos_snapshots (
            timestamp TIMESTAMP DEFAULT now(),
            world VARCHAR,
            address VARCHAR,
            balance_apt DOUBLE
        )
    """)
    con.execute("""
        CREATE TABLE IF NOT EXISTS multisig_probes (
            timestamp TIMESTAMP DEFAULT now(),
            pair VARCHAR,
            address VARCHAR,
            sigs_required INTEGER,
            healthy BOOLEAN
        )
    """)
    con.execute("""
        CREATE TABLE IF NOT EXISTS mnx_snapshots (
            timestamp TIMESTAMP DEFAULT now(),
            ticker VARCHAR,
            name VARCHAR,
            category VARCHAR,
            price DOUBLE,
            change_pct DOUBLE
        )
    """)

    con.execute("CREATE SEQUENCE IF NOT EXISTS increment_seq START 1")
    con.execute("CREATE SEQUENCE IF NOT EXISTS repo_seq START 1")

    all_sources = [
        ("org", "plurigrid", PLURIGRID_REPOS),
        ("org", "kubeflow", KUBEFLOW_REPOS),
        ("org", "TeglonLabs", TEGLON_REPOS),
        ("user", "bmorphism", BMORPHISM_REPOS),
        ("user", "zubyul", ZUBYUL_REPOS),
        ("social_graph", "migalkin+DJedamski+wasita+kristinezheng+M1shaaa+AustinCStone", SOCIAL_REPOS),
    ]

    increment_id = 1
    repo_id = 1

    for source_type, source_name, repos in all_sources:
        for repo in repos:
            trit, color, gf3name = gf3(increment_id)
            shash = snap_hash(source_name, repo["full_name"], repo.get("pushed_at", ""))
            con.execute("""
                INSERT INTO world_increments VALUES (?, now(), ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, [increment_id, trit, color, gf3name, source_type, source_name,
                  "repo_push", repo["full_name"], None, shash])

            org_or_user = source_name if "+" not in source_name else repo["full_name"].split("/")[0]
            con.execute("""
                INSERT INTO repo_snapshots VALUES (?, now(), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, [repo_id, increment_id, org_or_user, repo["name"], repo["full_name"],
                  repo.get("language"), repo.get("stargazers_count", 0),
                  repo.get("forks_count", 0), repo.get("open_issues_count", 0),
                  repo.get("pushed_at"), repo.get("description")])
            increment_id += 1
            repo_id += 1

    for world, address in APTOS_WALLETS:
        con.execute("""
            INSERT INTO aptos_snapshots VALUES (now(), ?, ?, ?)
        """, [world, address, None])

    for pair, address, sigs, healthy in MULTISIG_PROBES:
        con.execute("""
            INSERT INTO multisig_probes VALUES (now(), ?, ?, ?, ?)
        """, [pair, address, sigs, healthy])

    con.execute("INSERT INTO mnx_snapshots VALUES (now(), 'N/A', 'MNX Testnet', 'testnet', NULL, NULL)")

    stats = {}
    stats["total_increments"] = con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0]
    stats["total_repos"] = con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0]
    stats["multisig_healthy"] = con.execute("SELECT COUNT(*) FROM multisig_probes WHERE healthy=true").fetchone()[0]
    stats["aptos_wallets"] = con.execute("SELECT COUNT(*) FROM aptos_snapshots").fetchone()[0]

    top_stars = con.execute("""
        SELECT full_name, stars, language FROM repo_snapshots ORDER BY stars DESC LIMIT 10
    """).fetchall()
    stats["top_stars"] = top_stars

    gf3_dist = con.execute("""
        SELECT gf3_name, gf3_color, COUNT(*) as cnt FROM world_increments GROUP BY gf3_name, gf3_color ORDER BY cnt DESC
    """).fetchall()
    stats["gf3_dist"] = gf3_dist

    per_source = con.execute("""
        SELECT source_name, COUNT(*) as cnt FROM world_increments GROUP BY source_name ORDER BY cnt DESC
    """).fetchall()
    stats["per_source"] = per_source

    con.close()
    return stats


if __name__ == "__main__":
    stats = build_db()
    print(f"Total world increments: {stats['total_increments']}")
    print(f"Total repos: {stats['total_repos']}")
    print(f"Multisig healthy: {stats['multisig_healthy']}/5")
    print(f"Aptos wallets snapshotted: {stats['aptos_wallets']}")
    print("\nTop repos by stars:")
    for r in stats["top_stars"]:
        print(f"  {r[0]} ({r[2]}): ⭐{r[1]}")
    print("\nGF(3) distribution:")
    for g in stats["gf3_dist"]:
        print(f"  {g[0]} {g[1]}: {g[2]} increments")
    print("\nPer source:")
    for s in stats["per_source"]:
        print(f"  {s[0]}: {s[1]}")
    print("\nDone! Saved to", DB_PATH)
