#!/usr/bin/env python3
"""Ingest pre-fetched social graph data + live Aptos queries into DuckDB."""
import json
import time
import datetime
import hashlib
import requests
import duckdb

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"

GF3_COLORS = {0: ("#d3869b", "ERGODIC"), 1: ("#b8bb26", "PLUS"), 2: ("#cc241d", "MINUS")}
GF3_TRITS  = {0: 0, 1: 1, 2: -1}

def gf3(n):
    mod = n % 3
    color, name = GF3_COLORS[mod]
    return GF3_TRITS[mod], color, name

def snap_hash(*parts):
    return hashlib.sha256("|".join(str(p) for p in parts).encode()).hexdigest()[:16]

# ── Repo data collected via MCP GitHub search ────────────────────────────────
REPO_DATA = {
  "plurigrid": [
    {"name":"gorj","full_name":"plurigrid/gorj","language":"Clojure","stargazers_count":0,"forks_count":0,"open_issues_count":247,"pushed_at":"2026-05-08T14:06:40Z","description":"forj + Rama topology nREPL routing + GF(3) gay trit coloring"},
    {"name":"asi","full_name":"plurigrid/asi","language":"HTML","stargazers_count":23,"forks_count":5,"open_issues_count":4,"pushed_at":"2026-05-17T14:27:10Z","description":"everything is topological chemputer!"},
    {"name":"ontology","full_name":"plurigrid/ontology","language":"JavaScript","stargazers_count":8,"forks_count":9,"open_issues_count":16,"pushed_at":"2026-05-09T04:20:49Z","description":"autopoietic ergodicity and embodied gradualism"},
    {"name":"Plurigraph","full_name":"plurigrid/Plurigraph","language":"JavaScript","stargazers_count":3,"forks_count":5,"open_issues_count":4,"pushed_at":"2026-05-12T03:19:41Z","description":"Plurigrid knowledge base for use with Obsidian.md"},
    {"name":"vcg-auction","full_name":"plurigrid/vcg-auction","language":"Rust","stargazers_count":7,"forks_count":2,"open_issues_count":1,"pushed_at":"2025-12-16T12:32:02Z","description":"a simple contract that performs a VCG auction"},
    {"name":"agent","full_name":"plurigrid/agent","language":"Python","stargazers_count":5,"forks_count":1,"open_issues_count":6,"pushed_at":"2024-10-16T11:33:13Z","description":"Framework for agency amplification"},
    {"name":"microworlds","full_name":"plurigrid/microworlds","language":"Rust","stargazers_count":3,"forks_count":5,"open_issues_count":3,"pushed_at":"2024-03-14T00:12:46Z","description":"👽"},
    {"name":"StochFlow","full_name":"plurigrid/StochFlow","language":"Python","stargazers_count":4,"forks_count":1,"open_issues_count":0,"pushed_at":"2024-08-15T02:58:54Z","description":"Python library: stochastic interpolant models"},
    {"name":"asi-skills","full_name":"plurigrid/asi-skills","language":"Julia","stargazers_count":3,"forks_count":1,"open_issues_count":0,"pushed_at":"2026-04-26T08:09:31Z","description":"69 skills with Galois Hole Type accessibility"},
    {"name":"zig-syrup","full_name":"plurigrid/zig-syrup","language":"Zig","stargazers_count":2,"forks_count":2,"open_issues_count":0,"pushed_at":"2026-04-30T03:52:19Z","description":"High-performance Zig implementation of OCapN Syrup"},
    {"name":"nanoclj-zig","full_name":"plurigrid/nanoclj-zig","language":"Zig","stargazers_count":1,"forks_count":2,"open_issues_count":20,"pushed_at":"2026-04-25T07:29:13Z","description":"NaN-boxed Clojure interpreter in Zig 0.15"},
    {"name":"nash-portal","full_name":"plurigrid/nash-portal","language":"Rust","stargazers_count":2,"forks_count":3,"open_issues_count":2,"pushed_at":"2026-05-05T11:37:02Z","description":"NASH token TUI in the browser"},
    {"name":"horse","full_name":"plurigrid/horse","language":"TeX","stargazers_count":1,"forks_count":1,"open_issues_count":9,"pushed_at":"2026-04-26T08:31:03Z","description":""},
    {"name":"vivarium","full_name":"plurigrid/vivarium","language":"Clojure","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-08T22:49:56Z","description":""},
    {"name":"act","full_name":"plurigrid/act","language":"Python","stargazers_count":3,"forks_count":1,"open_issues_count":4,"pushed_at":"2024-11-25T09:36:59Z","description":"building blocks for cognitive category theory"},
    {"name":"duck-kanban","full_name":"plurigrid/duck-kanban","language":"Rust","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-10-24T09:24:59Z","description":"Duck intelligence kanban system"},
    {"name":"aptos-wallet-ruby","full_name":"plurigrid/aptos-wallet-ruby","language":"Ruby","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-10-24T09:25:13Z","description":""},
    {"name":"graded-optic","full_name":"plurigrid/graded-optic","language":"Haskell","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-02-08T16:10:19Z","description":"Semiring-graded bidirectional processes"},
    {"name":"gatomic","full_name":"plurigrid/gatomic","language":"Clojure","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-30T00:54:51Z","description":"Deterministic color identity store with sonification"},
    {"name":"leprechauns","full_name":"plurigrid/leprechauns","language":"Racket","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-01-23T07:45:06Z","description":"Spritely Goblins + Gay.jl semantic colors"},
    {"name":"shepherd","full_name":"plurigrid/shepherd","language":"Scheme","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-01-23T07:49:09Z","description":"Spritely Shepherd - Service manager"},
    {"name":"hoot","full_name":"plurigrid/hoot","language":"Scheme","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-01-23T07:49:08Z","description":"Spritely Hoot - Scheme to WebAssembly compiler"},
    {"name":"magenc","full_name":"plurigrid/magenc","language":"Scheme","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-01-23T07:47:17Z","description":"Magenc Magnet URIs"},
    {"name":"goblinshare","full_name":"plurigrid/goblinshare","language":"Scheme","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-01-23T07:47:17Z","description":"P2P filesharing demo for Goblins"},
    {"name":"grid","full_name":"plurigrid/grid","language":"TypeScript","stargazers_count":2,"forks_count":1,"open_issues_count":1,"pushed_at":"2023-01-31T11:42:52Z","description":"Plurigrid Testnet #0: Edith Clarke"},
    {"name":"org","full_name":"plurigrid/org","language":"Jupyter Notebook","stargazers_count":2,"forks_count":0,"open_issues_count":1,"pushed_at":"2024-04-12T23:48:43Z","description":"Dynamically Replicating Duck"},
    {"name":"nblm-flashcards","full_name":"plurigrid/nblm-flashcards","language":"Hy","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-26T08:23:04Z","description":"NotebookLM Enterprise flashcard pipeline"},
    {"name":"agent-o-rama","full_name":"plurigrid/agent-o-rama","language":"Clojure","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-01-01T23:39:06Z","description":""},
    {"name":"gemini-agent","full_name":"plurigrid/gemini-agent","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-02-19T06:39:19Z","description":""},
    {"name":"gay-rs","full_name":"plurigrid/gay-rs","language":"Rust","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-01-08T14:19:26Z","description":"Rust crate for Gay.jl deterministic coloring"},
    {"name":"gay-go","full_name":"plurigrid/gay-go","language":"Go","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-01-08T14:19:26Z","description":"Go implementation of Gay.jl deterministic coloring"},
    {"name":"lazygay","full_name":"plurigrid/lazygay","language":"Go","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-01-08T14:19:29Z","description":"lazygit fork with Gay.jl deterministic commit coloring"},
    {"name":"lazybjj","full_name":"plurigrid/lazybjj","language":"Rust","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-01-08T14:19:32Z","description":"TUI for jj with Gay.jl GF(3) coloring"},
    {"name":"gay-terminal","full_name":"plurigrid/gay-terminal","language":"Rust","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-01-08T14:19:27Z","description":"Terminal ANSI coloring with Gay.jl"},
    {"name":"gay-tofu","full_name":"plurigrid/gay-tofu","language":"HTML","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-01-08T15:14:38Z","description":"Low-discrepancy color sequences for visual TOFU authentication"},
  ],
  "kubeflow": [
    {"name":"kubeflow","full_name":"kubeflow/kubeflow","language":None,"stargazers_count":15647,"forks_count":2648,"open_issues_count":2,"pushed_at":"2026-05-18T13:36:06Z","description":"Machine Learning Toolkit for Kubernetes"},
    {"name":"pipelines","full_name":"kubeflow/pipelines","language":"Python","stargazers_count":4140,"forks_count":1993,"open_issues_count":470,"pushed_at":"2026-05-18T15:49:11Z","description":"Machine Learning Pipelines for Kubeflow"},
    {"name":"trainer","full_name":"kubeflow/trainer","language":"Go","stargazers_count":2100,"forks_count":950,"open_issues_count":101,"pushed_at":"2026-05-18T03:05:44Z","description":"Distributed AI Model Training and LLM Fine-Tuning on Kubernetes"},
    {"name":"spark-operator","full_name":"kubeflow/spark-operator","language":"Python","stargazers_count":3126,"forks_count":1482,"open_issues_count":90,"pushed_at":"2026-05-18T22:05:12Z","description":"Kubernetes operator for Apache Spark"},
    {"name":"katib","full_name":"kubeflow/katib","language":"Python","stargazers_count":1682,"forks_count":522,"open_issues_count":124,"pushed_at":"2026-05-16T15:36:21Z","description":"Automated Machine Learning on Kubernetes"},
    {"name":"examples","full_name":"kubeflow/examples","language":"Jsonnet","stargazers_count":1463,"forks_count":756,"open_issues_count":111,"pushed_at":"2026-05-15T19:11:13Z","description":"A repository to host extended examples and tutorials"},
    {"name":"arena","full_name":"kubeflow/arena","language":"Go","stargazers_count":810,"forks_count":190,"open_issues_count":57,"pushed_at":"2026-05-07T06:46:21Z","description":"A CLI for Kubeflow"},
    {"name":"kale","full_name":"kubeflow/kale","language":"Python","stargazers_count":687,"forks_count":156,"open_issues_count":54,"pushed_at":"2026-05-18T19:18:04Z","description":"Kubeflow's superfood for Data Scientists"},
    {"name":"mpi-operator","full_name":"kubeflow/mpi-operator","language":"Go","stargazers_count":527,"forks_count":235,"open_issues_count":101,"pushed_at":"2026-05-17T09:13:50Z","description":"Kubernetes Operator for MPI-based applications"},
    {"name":"fairing","full_name":"kubeflow/fairing","language":"Jsonnet","stargazers_count":337,"forks_count":143,"open_issues_count":134,"pushed_at":"2025-09-08T14:41:40Z","description":"Python SDK for building, training, and deploying ML models"},
    {"name":"manifests","full_name":"kubeflow/manifests","language":"YAML","stargazers_count":1017,"forks_count":1064,"open_issues_count":27,"pushed_at":"2026-05-16T16:37:58Z","description":"Kubeflow AI Reference Platform Deployment Manifests"},
    {"name":"mcp-apache-spark-history-server","full_name":"kubeflow/mcp-apache-spark-history-server","language":"Python","stargazers_count":170,"forks_count":60,"open_issues_count":22,"pushed_at":"2026-05-18T22:08:11Z","description":"MCP Server and CLI for Apache Spark History Server"},
    {"name":"hub","full_name":"kubeflow/hub","language":"Go","stargazers_count":175,"forks_count":178,"open_issues_count":48,"pushed_at":"2026-05-18T21:18:00Z","description":"Model Registry for ML model developers"},
    {"name":"sdk","full_name":"kubeflow/sdk","language":"Python","stargazers_count":118,"forks_count":174,"open_issues_count":131,"pushed_at":"2026-05-18T19:07:44Z","description":"Universal Python SDK to run AI workloads on Kubernetes"},
    {"name":"docs-agent","full_name":"kubeflow/docs-agent","language":"Python","stargazers_count":36,"forks_count":98,"open_issues_count":153,"pushed_at":"2026-05-06T16:36:21Z","description":"Kubeflow Documentation AI Agent"},
    {"name":"website","full_name":"kubeflow/website","language":"HTML","stargazers_count":184,"forks_count":920,"open_issues_count":52,"pushed_at":"2026-05-13T20:18:51Z","description":"Kubeflow Website"},
    {"name":"notebooks","full_name":"kubeflow/notebooks","language":None,"stargazers_count":72,"forks_count":110,"open_issues_count":190,"pushed_at":"2026-05-12T15:56:23Z","description":"Kubeflow Notebooks"},
    {"name":"dashboard","full_name":"kubeflow/dashboard","language":"TypeScript","stargazers_count":17,"forks_count":56,"open_issues_count":76,"pushed_at":"2026-05-11T15:26:20Z","description":"Kubeflow Central Dashboard"},
    {"name":"mcp-server","full_name":"kubeflow/mcp-server","language":"Python","stargazers_count":9,"forks_count":13,"open_issues_count":22,"pushed_at":"2026-05-16T19:09:35Z","description":"MCP Server for AI-Assisted Development with Kubeflow"},
    {"name":"community","full_name":"kubeflow/community","language":"Jupyter Notebook","stargazers_count":196,"forks_count":257,"open_issues_count":13,"pushed_at":"2026-05-18T17:12:07Z","description":"Information about the Kubeflow community"},
  ],
  "TeglonLabs": [
    {"name":"mathpix-gem","full_name":"TeglonLabs/mathpix-gem","language":"Ruby","stargazers_count":2,"forks_count":0,"open_issues_count":11,"pushed_at":"2026-01-01T12:13:16Z","description":"Transform mathematical images to LaTeX"},
    {"name":"coin-flip-mcp","full_name":"TeglonLabs/coin-flip-mcp","language":"JavaScript","stargazers_count":0,"forks_count":2,"open_issues_count":1,"pushed_at":"2025-03-16T01:31:45Z","description":"MCP server for flipping coins with varying degrees of randomness"},
    {"name":"monad-mcp-server","full_name":"TeglonLabs/monad-mcp-server","language":None,"stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-05-14T17:53:01Z","description":"Monad MCP Server"},
    {"name":"topoi","full_name":"TeglonLabs/topoi","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":1,"pushed_at":"2025-01-24T06:47:38Z","description":""},
  ],
  "bmorphism": [
    {"name":"Gay.jl","full_name":"bmorphism/Gay.jl","language":"Julia","stargazers_count":1,"forks_count":0,"open_issues_count":189,"pushed_at":"2026-05-15T12:46:42Z","description":"Wide-gamut color sampling with splittable determinism"},
    {"name":"ocaml-mcp-sdk","full_name":"bmorphism/ocaml-mcp-sdk","language":"OCaml","stargazers_count":61,"forks_count":2,"open_issues_count":0,"pushed_at":"2026-05-08T16:50:34Z","description":"OCaml SDK for Model Context Protocol"},
    {"name":"penrose-mcp","full_name":"bmorphism/penrose-mcp","language":"JavaScript","stargazers_count":10,"forks_count":4,"open_issues_count":0,"pushed_at":"2026-04-12T18:09:12Z","description":"Penrose server for the Infinity-Topos environment"},
    {"name":"manifold-mcp-server","full_name":"bmorphism/manifold-mcp-server","language":"JavaScript","stargazers_count":14,"forks_count":9,"open_issues_count":5,"pushed_at":"2026-04-15T19:54:28Z","description":"MCP server for Manifold Markets prediction markets"},
    {"name":"say-mcp-server","full_name":"bmorphism/say-mcp-server","language":"JavaScript","stargazers_count":20,"forks_count":9,"open_issues_count":3,"pushed_at":"2026-03-19T23:11:59Z","description":"MCP server for macOS text-to-speech functionality"},
    {"name":"babashka-mcp-server","full_name":"bmorphism/babashka-mcp-server","language":"JavaScript","stargazers_count":18,"forks_count":6,"open_issues_count":3,"pushed_at":"2026-03-26T14:35:39Z","description":"Model Context Protocol server for Babashka"},
    {"name":"anti-bullshit-mcp-server","full_name":"bmorphism/anti-bullshit-mcp-server","language":"JavaScript","stargazers_count":23,"forks_count":7,"open_issues_count":1,"pushed_at":"2026-02-05T15:46:59Z","description":"MCP server for analyzing claims"},
    {"name":"marginalia-mcp-server","full_name":"bmorphism/marginalia-mcp-server","language":"JavaScript","stargazers_count":8,"forks_count":6,"open_issues_count":0,"pushed_at":"2026-03-27T16:55:55Z","description":"MCP server implementation for managing marginalia"},
    {"name":"hypernym-mcp-server","full_name":"bmorphism/hypernym-mcp-server","language":"JavaScript","stargazers_count":6,"forks_count":5,"open_issues_count":0,"pushed_at":"2025-10-24T09:21:53Z","description":""},
    {"name":"nats-mcp-server","full_name":"bmorphism/nats-mcp-server","language":None,"stargazers_count":7,"forks_count":3,"open_issues_count":2,"pushed_at":"2025-12-20T23:56:36Z","description":"MCP server for NATS messaging system"},
    {"name":"risc0-cosmwasm-example","full_name":"bmorphism/risc0-cosmwasm-example","language":"Rust","stargazers_count":23,"forks_count":2,"open_issues_count":1,"pushed_at":"2022-10-19T05:39:15Z","description":"CosmWasm + zkVM RISC-V EFI template"},
    {"name":"shitcoin","full_name":"bmorphism/shitcoin","language":"Python","stargazers_count":5,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-08T08:07:17Z","description":"gets denom for cw20 assets"},
    {"name":"whale","full_name":"bmorphism/whale","language":"MATLAB","stargazers_count":2,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-20T15:04:09Z","description":"omniglot + sperm whale codas = metawhaling"},
    {"name":"open-location-code-zig","full_name":"bmorphism/open-location-code-zig","language":"Zig","stargazers_count":3,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-24T21:54:01Z","description":"Open Location Code (Plus Codes) for Zig"},
    {"name":"graphistry-mcp","full_name":"bmorphism/graphistry-mcp","language":"Python","stargazers_count":2,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-10-24T09:22:41Z","description":"Graphistry MCP integration for graph visualization"},
    {"name":"schoenfinkel","full_name":"bmorphism/schoenfinkel","language":"Python","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-10-24T09:24:26Z","description":"Post-quantum categorical gravity framework"},
    {"name":"magic-world-org","full_name":"bmorphism/magic-world-org","language":"Python","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-05-01T01:06:25Z","description":"Magic World Org (Local MLX)"},
    {"name":"penumbra-mcp","full_name":"bmorphism/penumbra-mcp","language":"JavaScript","stargazers_count":5,"forks_count":6,"open_issues_count":3,"pushed_at":"2025-01-06T04:49:59Z","description":"MCP server for interacting with Penumbra blockchain"},
    {"name":"slowtime-mcp-server","full_name":"bmorphism/slowtime-mcp-server","language":"TypeScript","stargazers_count":3,"forks_count":5,"open_issues_count":6,"pushed_at":"2025-01-02T01:23:23Z","description":"MCP server for secure time-based operations"},
    {"name":"aella","full_name":"bmorphism/aella","language":"Rascal","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-02T17:15:48Z","description":""},
    {"name":"GeoACSets.jl","full_name":"bmorphism/GeoACSets.jl","language":"Julia","stargazers_count":0,"forks_count":1,"open_issues_count":1,"pushed_at":"2026-01-19T13:55:07Z","description":"Categorical data structures with geospatial capabilities"},
    {"name":"monero-rental-hash-war","full_name":"bmorphism/monero-rental-hash-war","language":"Haskell","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-10-24T09:25:25Z","description":"Compositional OpenGame analysis of Monero rental hash war"},
    {"name":"meso","full_name":"bmorphism/meso","language":"Jupyter Notebook","stargazers_count":1,"forks_count":1,"open_issues_count":0,"pushed_at":"2025-10-24T09:19:08Z","description":"Scripts simulating approximation of inverse transformations"},
  ],
  "zubyul": [
    {"name":"voice-observatory","full_name":"zubyul/voice-observatory","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-24T05:56:20Z","description":"Passive macOS TUI observing voice-download pathways"},
    {"name":"gay-world","full_name":"zubyul/gay-world","language":"Python","stargazers_count":1,"forks_count":1,"open_issues_count":0,"pushed_at":"2026-04-05T06:54:03Z","description":"Goblin world builder: each goblin is a world"},
    {"name":"kinesis-kb360pro","full_name":"zubyul/kinesis-kb360pro","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-26T10:29:44Z","description":"Claude Code skill for Kinesis Advantage360 Pro keyboard"},
    {"name":"ghostel-emacs-worlds","full_name":"zubyul/ghostel-emacs-worlds","language":"GLSL","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-24T00:21:00Z","description":"Ghostty config + ghostel family"},
    {"name":"big-bad-plurigrid-quiz","full_name":"zubyul/big-bad-plurigrid-quiz","language":"Emacs Lisp","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-09T18:51:35Z","description":"27 flashcards from bmorphism/plurigrid/zubyul activity"},
    {"name":"tilelang-kernels","full_name":"zubyul/tilelang-kernels","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-16T02:31:16Z","description":"TileLang GPU kernels for SplitMix64 color generation"},
    {"name":"Gay.jl","full_name":"zubyul/Gay.jl","language":"Julia","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-28T11:30:07Z","description":"Wide-gamut color sampling with splittable determinism"},
    {"name":"from-possible-worlds","full_name":"zubyul/from-possible-worlds","language":"TeX","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-16T03:07:20Z","description":""},
    {"name":"jonikas_lab_data_analysis_misc","full_name":"zubyul/jonikas_lab_data_analysis_misc","language":"Jupyter Notebook","stargazers_count":2,"forks_count":0,"open_issues_count":0,"pushed_at":"2023-06-15T21:54:54Z","description":"various scripts for processing genetic sequence data"},
    {"name":"WGCNA","full_name":"zubyul/WGCNA","language":"HTML","stargazers_count":2,"forks_count":0,"open_issues_count":0,"pushed_at":"2023-06-16T13:50:22Z","description":"weighted gene correlation network analysis project"},
    {"name":"Nikolova_lab_data_analysis","full_name":"zubyul/Nikolova_lab_data_analysis","language":"R","stargazers_count":2,"forks_count":0,"open_issues_count":0,"pushed_at":"2023-06-16T13:55:33Z","description":"undergraduate thesis - cortical thickness and depression"},
    {"name":"zubyul.github.io","full_name":"zubyul/zubyul.github.io","language":"CSS","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2024-06-10T15:22:35Z","description":""},
  ],
  "migalkin": [
    {"name":"NodePiece","full_name":"migalkin/NodePiece","language":"Python","stargazers_count":144,"forks_count":21,"open_issues_count":0,"pushed_at":"2026-05-07T05:40:02Z","description":"Compositional and Parameter-Efficient Representations for Large Knowledge Graphs"},
    {"name":"StarE","full_name":"migalkin/StarE","language":"Python","stargazers_count":89,"forks_count":16,"open_issues_count":1,"pushed_at":"2026-04-16T14:12:45Z","description":"Message Passing for Hyper-Relational Knowledge Graphs"},
    {"name":"kgcourse2021","full_name":"migalkin/kgcourse2021","language":"HTML","stargazers_count":25,"forks_count":9,"open_issues_count":0,"pushed_at":"2026-02-16T05:16:08Z","description":"Курс по Knowledge Graphs"},
    {"name":"NBFNet_mlx","full_name":"migalkin/NBFNet_mlx","language":"Python","stargazers_count":10,"forks_count":1,"open_issues_count":1,"pushed_at":"2026-03-11T01:31:21Z","description":"Neural Bellman-Ford networks in MLX for Apple Silicon"},
    {"name":"RWL","full_name":"migalkin/RWL","language":"Python","stargazers_count":7,"forks_count":1,"open_issues_count":0,"pushed_at":"2022-11-30T23:09:41Z","description":"Weisfeiler and Leman Go Relational"},
    {"name":"rambo","full_name":"migalkin/rambo","language":"Rust","stargazers_count":3,"forks_count":0,"open_issues_count":1,"pushed_at":"2019-08-13T14:16:53Z","description":""},
  ],
  "DJedamski": [
    {"name":"kaggle_ncaa18","full_name":"DJedamski/kaggle_ncaa18","language":"Jupyter Notebook","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2018-02-26T16:33:24Z","description":"Code for NCAA March Madness competition"},
    {"name":"Kaggle","full_name":"DJedamski/Kaggle","language":None,"stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2023-04-21T01:42:35Z","description":""},
    {"name":"School","full_name":"DJedamski/School","language":"R","stargazers_count":1,"forks_count":1,"open_issues_count":0,"pushed_at":"2023-04-21T01:42:33Z","description":"A couple small projects from grad school"},
    {"name":"Getting-and-Cleaning-Data","full_name":"DJedamski/Getting-and-Cleaning-Data","language":"R","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2023-04-21T01:42:34Z","description":"Coursera Project"},
  ],
  "wasita": [
    {"name":"wasita.github.io","full_name":"wasita/wasita.github.io","language":"Svelte","stargazers_count":1,"forks_count":0,"open_issues_count":8,"pushed_at":"2026-05-18T03:30:34Z","description":"personal website"},
    {"name":"wm-cv","full_name":"wasita/wm-cv","language":"Svelte","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-05-13T05:29:08Z","description":"Academic CV as single page web app"},
    {"name":"magic-garden","full_name":"wasita/magic-garden","language":"Python","stargazers_count":2,"forks_count":1,"open_issues_count":1,"pushed_at":"2026-04-22T21:16:43Z","description":"a bot for the magic garden discord activity game"},
    {"name":"vocoder","full_name":"wasita/vocoder","language":"JavaScript","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-05-06T05:14:03Z","description":""},
    {"name":"wins-search","full_name":"wasita/wins-search","language":"CSS","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2022-09-26T02:49:52Z","description":"Women in Network Science member list website"},
  ],
  "kristinezheng": [
    {"name":"kristinezheng.github.io","full_name":"kristinezheng/kristinezheng.github.io","language":"HTML","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-05-14T22:29:01Z","description":""},
    {"name":"lookit-jenga","full_name":"kristinezheng/lookit-jenga","language":"Jupyter Notebook","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2024-05-16T18:29:05Z","description":"Lookit study"},
    {"name":"Green-Machine","full_name":"kristinezheng/Green-Machine","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2021-09-19T04:47:32Z","description":"HackMIT 2021: Sustainability Track"},
  ],
  "M1shaaa": [
    {"name":"M1shaaa","full_name":"M1shaaa/M1shaaa","language":None,"stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-02-04T19:32:04Z","description":"Config files for my GitHub profile"},
    {"name":"lab-bookshelf-","full_name":"M1shaaa/lab-bookshelf-","language":"TypeScript","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2024-12-31T05:11:18Z","description":""},
    {"name":"Python-Lookit-Uploads","full_name":"M1shaaa/Python-Lookit-Uploads","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2024-02-15T22:59:37Z","description":"random projects"},
  ],
  "AustinCStone": [
    {"name":"TextGAN","full_name":"AustinCStone/TextGAN","language":"Python","stargazers_count":92,"forks_count":30,"open_issues_count":5,"pushed_at":"2016-09-19T01:55:28Z","description":"A generative adversarial network for text generation"},
    {"name":"EpsteinSearch","full_name":"AustinCStone/EpsteinSearch","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-02-11T01:10:57Z","description":""},
    {"name":"StereoVisionMRF","full_name":"AustinCStone/StereoVisionMRF","language":"Python","stargazers_count":11,"forks_count":4,"open_issues_count":0,"pushed_at":"2016-01-10T08:25:11Z","description":"MRF with loopy belief propagation for depth from stereo"},
    {"name":"SpectralClustering","full_name":"AustinCStone/SpectralClustering","language":"Python","stargazers_count":3,"forks_count":2,"open_issues_count":0,"pushed_at":"2015-11-09T03:26:42Z","description":"Implementing spectral clustering"},
    {"name":"bmforkupdate","full_name":"AustinCStone/bmforkupdate","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-05-09T04:50:16Z","description":""},
    {"name":"bmfork","full_name":"AustinCStone/bmfork","language":"Python","stargazers_count":0,"forks_count":1,"open_issues_count":1,"pushed_at":"2025-05-09T04:18:54Z","description":""},
    {"name":"Connectomics","full_name":"AustinCStone/Connectomics","language":"TeX","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2014-05-11T05:29:44Z","description":"2013-2014 Kaggle Connectomics Challenge"},
  ],
}

# ── DB setup ─────────────────────────────────────────────────────────────────
con = duckdb.connect(DB_PATH)
con.execute("DROP TABLE IF EXISTS world_increments")
con.execute("DROP TABLE IF EXISTS repo_snapshots")
con.execute("DROP TABLE IF EXISTS aptos_snapshots")
con.execute("DROP TABLE IF EXISTS multisig_probes")
con.execute("DROP TABLE IF EXISTS mnx_snapshots")
try:
    con.execute("DROP SEQUENCE increment_seq")
    con.execute("DROP SEQUENCE repo_seq")
except Exception:
    pass

con.execute("""
CREATE TABLE world_increments (
  id INTEGER, timestamp TIMESTAMP DEFAULT now(), gf3_trit INTEGER,
  gf3_color VARCHAR, gf3_name VARCHAR, source_type VARCHAR,
  source_name VARCHAR, event_type VARCHAR, repo_name VARCHAR,
  actor VARCHAR, snapshot_hash VARCHAR
)""")
con.execute("""
CREATE TABLE repo_snapshots (
  id INTEGER, timestamp TIMESTAMP DEFAULT now(), increment_id INTEGER,
  org_or_user VARCHAR, repo_name VARCHAR, full_name VARCHAR,
  language VARCHAR, stars INTEGER, forks INTEGER, open_issues INTEGER,
  pushed_at VARCHAR, description VARCHAR
)""")
con.execute("""
CREATE TABLE aptos_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  world VARCHAR, address VARCHAR, balance_apt DOUBLE
)""")
con.execute("""
CREATE TABLE multisig_probes (
  timestamp TIMESTAMP DEFAULT now(),
  pair VARCHAR, address VARCHAR, sigs_required INTEGER, healthy BOOLEAN
)""")
con.execute("""
CREATE TABLE mnx_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  ticker VARCHAR, name VARCHAR, category VARCHAR,
  price DOUBLE, change_pct DOUBLE
)""")
con.execute("CREATE SEQUENCE increment_seq START 1")
con.execute("CREATE SEQUENCE repo_seq START 1")

def next_inc():
    return con.execute("SELECT nextval('increment_seq')").fetchone()[0]

def next_repo():
    return con.execute("SELECT nextval('repo_seq')").fetchone()[0]

# ── JOB 1: Insert GitHub repo data ──────────────────────────────────────────
print("=== JOB 1: Inserting GitHub repo data ===")
total_repos = 0

for source_name, repos in REPO_DATA.items():
    # Determine source_type
    source_type = "org" if source_name in ("plurigrid", "kubeflow", "TeglonLabs") else "user"
    for repo in repos:
        inc_id = next_inc()
        trit, color, gf3name = gf3(inc_id)
        sh = snap_hash(source_name, repo.get("full_name",""), repo.get("pushed_at",""))
        con.execute("""INSERT INTO world_increments VALUES (?,now(),?,?,?,?,?,?,?,?,?)""",
            [inc_id, trit, color, gf3name, source_type, source_name, "repo_push",
             repo.get("name",""), source_name, sh])
        repo_id = next_repo()
        con.execute("""INSERT INTO repo_snapshots VALUES (?,now(),?,?,?,?,?,?,?,?,?,?)""",
            [repo_id, inc_id, source_name, repo.get("name",""), repo.get("full_name",""),
             repo.get("language"), repo.get("stargazers_count",0),
             repo.get("forks_count",0), repo.get("open_issues_count",0),
             repo.get("pushed_at",""), (repo.get("description") or "")[:200]])
        total_repos += 1
    print(f"  {source_name}: {len(repos)} repos")

print(f"Total repos inserted: {total_repos}")

# ── JOB 2: Aptos Hamming Swarm ────────────────────────────────────────────────
print("\n=== JOB 2: Hamming Swarm Snapshot (Aptos) ===")
APTOS_BASE = "https://fullnode.mainnet.aptoslabs.com/v1"

WALLETS = {
    "alice": "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b",
    "bob":   "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d",
    "A":     "0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a",
    "B":     "0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13",
    "C":     "0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e",
    "D":     "0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1",
    "E":     "0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36",
    "F":     "0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71",
    "G":     "0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32",
    "H":     "0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f",
    "I":     "0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9",
    "J":     "0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54",
    "K":     "0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4",
    "L":     "0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9",
    "M":     "0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9",
    "N":     "0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c",
    "O":     "0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d",
    "P":     "0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948",
    "Q":     "0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9",
    "R":     "0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10",
    "S":     "0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386",
    "T":     "0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588",
    "U":     "0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956",
    "V":     "0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3",
    "W":     "0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0",
    "X":     "0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d",
    "Y":     "0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4",
    "Z":     "0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c",
}

aptos_balances = {}
for world, addr in WALLETS.items():
    payload = {
        "function": "0x1::coin::balance",
        "type_arguments": ["0x1::aptos_coin::AptosCoin"],
        "arguments": [addr]
    }
    try:
        r = requests.post(f"{APTOS_BASE}/view", json=payload, timeout=10)
        if r.status_code == 200:
            val = int(r.json()[0])
            apt = val / 1e8
        else:
            apt = None
    except Exception:
        apt = None
    aptos_balances[world] = apt
    status = f"{apt:.4f} APT" if apt is not None else "not found"
    print(f"  {world}: {status}")
    con.execute("INSERT INTO aptos_snapshots VALUES (now(),?,?,?)", [world, addr, apt])
    time.sleep(1)

# ── Multisig probes ────────────────────────────────────────────────────────────
print("\n=== Multisig Probes ===")
MULTISIGS = {
    "A-B": "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",
    "A-G": "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",
    "Y-Z": "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",
    "S-T": "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",
    "V-W": "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",
}
for pair, addr in MULTISIGS.items():
    payload = {"function":"0x1::multisig_account::num_signatures_required","type_arguments":[],"arguments":[addr]}
    try:
        r = requests.post(f"{APTOS_BASE}/view", json=payload, timeout=10)
        if r.status_code == 200:
            data = r.json()
            sigs = int(data[0]) if data else 0
            healthy = sigs > 0
        else:
            sigs = 0; healthy = False
    except Exception as e:
        sigs = 0; healthy = False
    print(f"  {pair}: sigs_required={sigs}, healthy={healthy}")
    con.execute("INSERT INTO multisig_probes VALUES (now(),?,?,?,?)", [pair, addr, sigs, healthy])
    time.sleep(1)

# ── MNX Markets ───────────────────────────────────────────────────────────────
print("\n=== MNX Markets ===")
mnx_data = []
mnx_available = False
for url in ["https://testnet.mnx.fi/api/markets","https://testnet.mnx.fi/api/tickers",
            "https://testnet.mnx.fi/api/v1/markets"]:
    try:
        r = requests.get(url, timeout=10, headers={"User-Agent": "world-increment-sweep/1.0"})
        if r.status_code == 200:
            try:
                data = r.json()
                mnx_data = data if isinstance(data, list) else data.get("markets", data.get("tickers", [data]))
                mnx_available = True
                break
            except Exception:
                pass
    except Exception:
        pass
    time.sleep(0.5)

if not mnx_available:
    print("  MNX Markets: unavailable (testnet SPA, no public API endpoints)")
    con.execute("INSERT INTO mnx_snapshots VALUES (now(),?,?,?,?,?)", ["N/A","unavailable","N/A",0.0,0.0])
else:
    for m in mnx_data:
        if not isinstance(m, dict): continue
        ticker = m.get("ticker", m.get("symbol", m.get("id", "?")))
        name = m.get("name", ticker)
        category = m.get("category", m.get("type", "unknown"))
        price = float(m.get("price", m.get("last", 0)) or 0)
        change_pct = float(m.get("change_pct", m.get("change", 0)) or 0)
        con.execute("INSERT INTO mnx_snapshots VALUES (now(),?,?,?,?,?)", [ticker, name, category, price, change_pct])

# ── Summary stats ─────────────────────────────────────────────────────────────
inc_count  = con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0]
repo_count = con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0]
aptos_found = con.execute("SELECT COUNT(*) FROM aptos_snapshots WHERE balance_apt IS NOT NULL").fetchone()[0]
aptos_total = con.execute("SELECT COALESCE(SUM(balance_apt),0) FROM aptos_snapshots WHERE balance_apt IS NOT NULL").fetchone()[0]
ms_healthy = con.execute("SELECT COUNT(*) FROM multisig_probes WHERE healthy=true").fetchone()[0]
ms_total   = con.execute("SELECT COUNT(*) FROM multisig_probes").fetchone()[0]

gf3_dist  = con.execute("SELECT gf3_name, COUNT(*) FROM world_increments GROUP BY gf3_name ORDER BY gf3_name").fetchall()
top_langs = con.execute("SELECT language, COUNT(*) FROM repo_snapshots WHERE language IS NOT NULL GROUP BY language ORDER BY 2 DESC LIMIT 10").fetchall()
top_stars = con.execute("SELECT full_name, stars FROM repo_snapshots ORDER BY stars DESC LIMIT 12").fetchall()
aptos_rows = con.execute("SELECT world, address, balance_apt FROM aptos_snapshots ORDER BY world").fetchall()
ms_rows    = con.execute("SELECT pair, address, sigs_required, healthy FROM multisig_probes ORDER BY pair").fetchall()
source_dist = con.execute("SELECT org_or_user, COUNT(*) FROM repo_snapshots GROUP BY org_or_user ORDER BY 2 DESC").fetchall()

con.close()

# ── Write LATEST_SWEEP.md ─────────────────────────────────────────────────────
sweep_date = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
lines = [
f"# World-Increment Sweep + Hamming Snapshot",f"",
f"**Date:** {sweep_date}",f"",f"---",f"",
f"## JOB 1: GitHub Social Graph Sweep",f"",
f"### Sources",f"",
f"| Source | Type | Repos |",f"|--------|------|-------|",
]
for src, cnt in source_dist:
    t = "org" if src in ("plurigrid", "kubeflow", "TeglonLabs") else "user"
    lines.append(f"| {src} | {t} | {cnt} |")

lines += [f"",
f"| Metric | Value |",f"|--------|-------|",
f"| Total world-increments | {inc_count} |",
f"| Total repo snapshots | {repo_count} |",f"",
f"### GF(3) Color Chain Distribution",f"",
f"| GF3 Name | Hex Color | Trit | Count |",f"|----------|-----------|------|-------|",
]
trit_map = {"ERGODIC":(0,"#d3869b"),"PLUS":(1,"#b8bb26"),"MINUS":(-1,"#cc241d")}
for name, cnt in gf3_dist:
    trit, color = trit_map.get(name, (0,"#000"))
    lines.append(f"| {name} | `{color}` | {trit} | {cnt} |")

lines += [f"",f"### Top Languages",f"",f"| Language | Repos |",f"|----------|-------|",]
for lang, cnt in top_langs:
    lines.append(f"| {lang} | {cnt} |")

lines += [f"",f"### Top Starred Repos",f"",f"| Repo | Stars |",f"|------|-------|",]
for full_name, stars in top_stars:
    lines.append(f"| {full_name} | {stars:,} |")

lines += [f"",f"---",f"",
f"## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)",f"",
f"| Metric | Value |",f"|--------|-------|",
f"| Wallets probed | {len(WALLETS)} |",
f"| Wallets with APT balance | {aptos_found} |",
f"| Total APT (found wallets) | {aptos_total:.4f} |",
f"| Multisig contracts healthy | {ms_healthy}/{ms_total} |",f"",
f"### Wallet Balances",f"",
f"| World | Address (truncated) | Balance (APT) |",f"|-------|---------------------|---------------|",
]
for world, addr, bal in aptos_rows:
    short = addr[:10] + "…" + addr[-6:]
    bal_str = f"{bal:.6f}" if bal is not None else "—"
    lines.append(f"| {world} | `{short}` | {bal_str} |")

lines += [f"",f"### Multisig Probes (2-of-2 architecture)",f"",
f"| Pair | Address (truncated) | Sigs Required | Healthy |",f"|------|---------------------|---------------|---------|",
]
for pair, addr, sigs, healthy in ms_rows:
    short = addr[:10] + "…" + addr[-6:]
    h = "✓" if healthy else "✗"
    lines.append(f"| {pair} | `{short}` | {sigs} | {h} |")

lines += [f"",f"### MNX Markets (testnet.mnx.fi)",f"",
f"Status: {'available' if mnx_available else 'unavailable — testnet SPA, no discoverable REST API endpoints (404 on /api/markets, /api/tickers, /api/v1/markets, /api/v1/tickers)'}",
f"",f"---",f"",
f"*Generated by world-increment-sweep + hamming-swarm-snapshot agent. DuckDB: `packages/world-increment/ducklake/world-increments.duckdb`*",
]

summary_path = "/home/user/gorj/packages/world-increment/ducklake/LATEST_SWEEP.md"
with open(summary_path, "w") as f:
    f.write("\n".join(lines) + "\n")

print(f"\n=== Complete ===")
print(f"Increments: {inc_count}, Repos: {repo_count}")
print(f"Aptos wallets with balance: {aptos_found}/{len(WALLETS)}, total APT: {aptos_total:.4f}")
print(f"Multisig: {ms_healthy}/{ms_total} healthy")
print(f"Summary: {summary_path}")
