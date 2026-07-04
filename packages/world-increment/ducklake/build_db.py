#!/usr/bin/env python3
"""Build world-increments DuckDB from collected GitHub + Aptos data."""
import duckdb
import json
import hashlib
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
)
""")
con.execute("""
CREATE TABLE IF NOT EXISTS repo_snapshots (
  id INTEGER, timestamp TIMESTAMP DEFAULT now(), increment_id INTEGER,
  org_or_user VARCHAR, repo_name VARCHAR, full_name VARCHAR,
  language VARCHAR, stars INTEGER, forks INTEGER, open_issues INTEGER,
  pushed_at VARCHAR, description VARCHAR
)
""")
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
)
""")
con.execute("""
CREATE TABLE IF NOT EXISTS multisig_probes (
  timestamp TIMESTAMP DEFAULT now(),
  pair VARCHAR, address VARCHAR, sigs_required INTEGER, healthy BOOLEAN
)
""")
con.execute("""
CREATE TABLE IF NOT EXISTS mnx_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  ticker VARCHAR, name VARCHAR, category VARCHAR,
  price DOUBLE, change_pct DOUBLE
)
""")

def gf3(id_val):
    t = id_val % 3
    if t == 0:
        return (0, '#d3869b', 'ERGODIC')
    elif t == 1:
        return (1, '#b8bb26', 'PLUS')
    else:
        return (-1, '#cc241d', 'MINUS')

def snap_hash(full_name, pushed_at):
    return hashlib.sha256(f"{full_name}:{pushed_at}".encode()).hexdigest()[:16]

# All repo data grouped by source
sources = {
    "plurigrid": ("org", [
        {"full_name":"plurigrid/shrimp","language":None,"stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-07-03T01:24:20Z","description":"Jank worked example: shrimp"},
        {"full_name":"plurigrid/asi","language":"HTML","stargazers_count":28,"forks_count":8,"open_issues_count":4,"pushed_at":"2026-06-29T03:15:56Z","description":"everything is topological chemputer!"},
        {"full_name":"plurigrid/place","language":"TeX","stargazers_count":1,"forks_count":1,"open_issues_count":12,"pushed_at":"2026-06-29T20:40:59Z","description":None},
        {"full_name":"plurigrid/eirobri","language":"Clojure","stargazers_count":0,"forks_count":0,"open_issues_count":30,"pushed_at":"2026-06-30T02:23:56Z","description":"EiRoBri replay world"},
        {"full_name":"plurigrid/gorj","language":"Clojure","stargazers_count":0,"forks_count":0,"open_issues_count":963,"pushed_at":"2026-07-04T12:15:15Z","description":"forj + Rama topology nREPL routing + GF(3) gay trit coloring for compositional open game REPL orchestration"},
        {"full_name":"plurigrid/nash-portal","language":"Rust","stargazers_count":2,"forks_count":3,"open_issues_count":1,"pushed_at":"2026-05-19T01:49:59Z","description":"NASH token TUI in the browser"},
        {"full_name":"plurigrid/zig-syrup","language":"Zig","stargazers_count":2,"forks_count":2,"open_issues_count":0,"pushed_at":"2026-04-30T03:52:16Z","description":"High-performance Zig implementation of OCapN Syrup with CapTP optimizations"},
        {"full_name":"plurigrid/asi-skills","language":"Julia","stargazers_count":3,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-26T08:09:26Z","description":"69 skills with Galois Hole Type accessibility"},
        {"full_name":"plurigrid/nanoclj-zig","language":"Zig","stargazers_count":1,"forks_count":1,"open_issues_count":20,"pushed_at":"2026-04-25T07:29:09Z","description":"NaN-boxed Clojure interpreter in Zig 0.15"},
        {"full_name":"plurigrid/spi-race","language":"Swift","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-21T19:31:56Z","description":"Splitmix Parallel Integrity"},
        {"full_name":"plurigrid/reafference","language":"HTML","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-16T05:21:49Z","description":"Reafference adaptation workspace"},
        {"full_name":"plurigrid/web-browser","language":"Rust","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-10T02:54:47Z","description":"web-browser from prepostweb lineage"},
        {"full_name":"plurigrid/vivarium","language":"Clojure","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-08T08:38:37Z","description":None},
        {"full_name":"plurigrid/forester","language":"XSLT","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-30T01:32:26Z","description":"CatColab mathematical documentation forest"},
        {"full_name":"plurigrid/gatomic","language":"Clojure","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-30T00:54:48Z","description":"Deterministic color identity store with sonification"},
        {"full_name":"plurigrid/nblm-flashcards","language":"Hy","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-26T08:23:01Z","description":"NotebookLM Enterprise flashcard pipeline"},
        {"full_name":"plurigrid/gemini-agent","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-02-19T06:39:16Z","description":None},
        {"full_name":"plurigrid/graded-optic","language":"Haskell","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-02-08T16:10:16Z","description":"Semiring-graded bidirectional processes"},
        {"full_name":"plurigrid/shepherd","language":"Scheme","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-01-23T07:47:28Z","description":"Spritely Shepherd"},
        {"full_name":"plurigrid/gay-tofu","language":"HTML","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-01-08T15:14:34Z","description":"Low-discrepancy color sequences for visual TOFU authentication"},
        {"full_name":"plurigrid/lazygay","language":"Go","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-01-08T14:19:25Z","description":"lazygit fork with Gay.jl deterministic commit coloring"},
        {"full_name":"plurigrid/gay-rs","language":"Rust","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-01-08T14:19:22Z","description":"Rust crate for Gay.jl deterministic coloring with GF(3) trits"},
        {"full_name":"plurigrid/agent-o-rama","language":"Clojure","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-01-02T01:09:22Z","description":None},
        {"full_name":"plurigrid/aptos-wallet-ruby","language":"Ruby","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-09-30T22:47:22Z","description":None},
        {"full_name":"plurigrid/duck-kanban","language":"Rust","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-09-26T20:18:38Z","description":"Duck intelligence kanban system"},
        {"full_name":"plurigrid/ontology","language":"JavaScript","stargazers_count":8,"forks_count":9,"open_issues_count":16,"pushed_at":"2025-05-27T18:18:34Z","description":"autopoietic ergodicity and embodied gradualism"},
        {"full_name":"plurigrid/Plurigraph","language":"JavaScript","stargazers_count":3,"forks_count":5,"open_issues_count":4,"pushed_at":"2025-01-05T08:39:09Z","description":"Plurigrid knowledge base for use with Obsidian.md"},
        {"full_name":"plurigrid/act","language":"Python","stargazers_count":3,"forks_count":1,"open_issues_count":4,"pushed_at":"2024-07-26T08:27:08Z","description":"building blocks for cognitive category theory"},
        {"full_name":"plurigrid/StochFlow","language":"Python","stargazers_count":4,"forks_count":1,"open_issues_count":0,"pushed_at":"2024-03-20T23:34:57Z","description":"stochastic interpolant models"},
        {"full_name":"plurigrid/microworlds","language":"Rust","stargazers_count":3,"forks_count":5,"open_issues_count":3,"pushed_at":"2023-05-13T03:54:56Z","description":"👽"},
        {"full_name":"plurigrid/agent","language":"Python","stargazers_count":5,"forks_count":1,"open_issues_count":6,"pushed_at":"2023-03-31T18:45:23Z","description":"Framework for agency amplification"},
        {"full_name":"plurigrid/vcg-auction","language":"Rust","stargazers_count":7,"forks_count":2,"open_issues_count":1,"pushed_at":"2023-03-16T21:53:08Z","description":"VCG auction contract"},
    ]),
    "kubeflow": ("org", [
        {"full_name":"kubeflow/kubeflow","language":None,"stargazers_count":15761,"forks_count":2683,"open_issues_count":0,"pushed_at":"2026-06-18T11:45:16Z","description":"Machine Learning Toolkit for Kubernetes"},
        {"full_name":"kubeflow/pipelines","language":"Python","stargazers_count":4169,"forks_count":2023,"open_issues_count":416,"pushed_at":"2026-07-03T13:38:00Z","description":"Machine Learning Pipelines for Kubeflow"},
        {"full_name":"kubeflow/spark-operator","language":"Python","stargazers_count":3132,"forks_count":1496,"open_issues_count":103,"pushed_at":"2026-07-02T08:52:01Z","description":"Kubernetes operator for Apache Spark"},
        {"full_name":"kubeflow/trainer","language":"Go","stargazers_count":2129,"forks_count":978,"open_issues_count":148,"pushed_at":"2026-07-03T13:41:32Z","description":"Distributed AI Model Training and LLM Fine-Tuning on Kubernetes"},
        {"full_name":"kubeflow/katib","language":"Python","stargazers_count":1689,"forks_count":530,"open_issues_count":114,"pushed_at":"2026-07-01T21:20:57Z","description":"Automated Machine Learning on Kubernetes"},
        {"full_name":"kubeflow/arena","language":"Go","stargazers_count":814,"forks_count":194,"open_issues_count":45,"pushed_at":"2026-07-03T12:22:43Z","description":"A CLI for Kubeflow"},
        {"full_name":"kubeflow/kale","language":"Python","stargazers_count":695,"forks_count":156,"open_issues_count":38,"pushed_at":"2026-07-01T12:44:49Z","description":"Kubeflow's superfood for Data Scientists"},
        {"full_name":"kubeflow/community-distribution","language":"YAML","stargazers_count":1028,"forks_count":1067,"open_issues_count":25,"pushed_at":"2026-07-03T09:20:06Z","description":"Kubeflow Community Distribution"},
        {"full_name":"kubeflow/website","language":"HTML","stargazers_count":184,"forks_count":924,"open_issues_count":29,"pushed_at":"2026-07-03T20:27:09Z","description":"Kubeflow Website"},
        {"full_name":"kubeflow/hub","language":"Go","stargazers_count":174,"forks_count":186,"open_issues_count":33,"pushed_at":"2026-07-04T05:35:35Z","description":"Model Registry"},
        {"full_name":"kubeflow/mcp-apache-spark-history-server","language":"Python","stargazers_count":180,"forks_count":66,"open_issues_count":19,"pushed_at":"2026-06-25T20:28:43Z","description":"MCP Server and CLI for Apache Spark History Server"},
        {"full_name":"kubeflow/sdk","language":"Python","stargazers_count":123,"forks_count":188,"open_issues_count":140,"pushed_at":"2026-07-02T19:23:35Z","description":"Universal Python SDK to run AI workloads on Kubernetes"},
        {"full_name":"kubeflow/examples","language":"Jsonnet","stargazers_count":1460,"forks_count":756,"open_issues_count":111,"pushed_at":"2025-04-14T01:54:52Z","description":"Extended examples and tutorials"},
        {"full_name":"kubeflow/kfp-tekton","language":"TypeScript","stargazers_count":183,"forks_count":123,"open_issues_count":79,"pushed_at":"2024-11-19T12:23:51Z","description":"Kubeflow Pipelines on Tekton"},
        {"full_name":"kubeflow/mcp-server","language":"Python","stargazers_count":19,"forks_count":25,"open_issues_count":32,"pushed_at":"2026-06-29T14:46:23Z","description":"MCP Server for AI-Assisted Development with Kubeflow Tools"},
        {"full_name":"kubeflow/notebooks","language":None,"stargazers_count":73,"forks_count":126,"open_issues_count":180,"pushed_at":"2026-07-03T15:34:14Z","description":"Kubeflow Notebooks"},
        {"full_name":"kubeflow/fairing","language":"Jsonnet","stargazers_count":337,"forks_count":143,"open_issues_count":134,"pushed_at":"2022-04-11T05:28:47Z","description":"Python SDK for building, training, and deploying ML models"},
        {"full_name":"kubeflow/community","language":"Jupyter Notebook","stargazers_count":194,"forks_count":265,"open_issues_count":15,"pushed_at":"2026-07-01T21:20:20Z","description":"Kubeflow community"},
        {"full_name":"kubeflow/pytorch-operator","language":"Jsonnet","stargazers_count":310,"forks_count":143,"open_issues_count":63,"pushed_at":"2021-12-01T17:44:48Z","description":"PyTorch on Kubernetes"},
        {"full_name":"kubeflow/kfctl","language":"Go","stargazers_count":182,"forks_count":134,"open_issues_count":94,"pushed_at":"2023-08-15T20:19:22Z","description":"CLI for deploying and managing Kubeflow"},
    ]),
    "TeglonLabs": ("org", [
        {"full_name":"TeglonLabs/jank-crane","language":"C++","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-06-08T19:03:03Z","description":"crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow"},
        {"full_name":"TeglonLabs/mathpix-gem","language":"Ruby","stargazers_count":2,"forks_count":0,"open_issues_count":11,"pushed_at":"2026-01-01T12:13:13Z","description":"Transform mathematical images to LaTeX"},
        {"full_name":"TeglonLabs/coin-flip-mcp","language":"JavaScript","stargazers_count":0,"forks_count":2,"open_issues_count":1,"pushed_at":"2025-09-21T08:57:27Z","description":"MCP server for flipping coins with varying degrees of randomness"},
        {"full_name":"TeglonLabs/monad-mcp-server","language":None,"stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-05-14T11:36:14Z","description":"Monad MCP Server"},
        {"full_name":"TeglonLabs/topoi","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":1,"pushed_at":"2025-01-24T04:49:26Z","description":None},
    ]),
    "bmorphism": ("user", [
        {"full_name":"bmorphism/Gay.jl","language":"Julia","stargazers_count":2,"forks_count":1,"open_issues_count":187,"pushed_at":"2026-07-04T00:33:17Z","description":"Wide-gamut color sampling with splittable determinism"},
        {"full_name":"bmorphism/satreadout","language":"HTML","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-06-20T13:05:41Z","description":"Machine-checked saturating non-Riemannian perceptual readout"},
        {"full_name":"bmorphism/ocaml-mcp-sdk","language":"OCaml","stargazers_count":61,"forks_count":2,"open_issues_count":0,"pushed_at":"2026-03-16T05:24:25Z","description":"OCaml SDK for Model Context Protocol"},
        {"full_name":"bmorphism/anti-bullshit-mcp-server","language":"JavaScript","stargazers_count":23,"forks_count":7,"open_issues_count":1,"pushed_at":"2026-01-16T08:54:58Z","description":"MCP server for analyzing claims and detecting manipulation"},
        {"full_name":"bmorphism/say-mcp-server","language":"JavaScript","stargazers_count":20,"forks_count":9,"open_issues_count":3,"pushed_at":"2025-01-07T03:15:18Z","description":"MCP server for macOS text-to-speech functionality"},
        {"full_name":"bmorphism/babashka-mcp-server","language":"JavaScript","stargazers_count":19,"forks_count":6,"open_issues_count":3,"pushed_at":"2025-01-05T11:09:42Z","description":"MCP server for Babashka"},
        {"full_name":"bmorphism/manifold-mcp-server","language":"JavaScript","stargazers_count":14,"forks_count":9,"open_issues_count":5,"pushed_at":"2025-01-11T10:36:58Z","description":"MCP server for Manifold Markets"},
        {"full_name":"bmorphism/risc0-cosmwasm-example","language":"Rust","stargazers_count":23,"forks_count":2,"open_issues_count":1,"pushed_at":"2022-10-20T23:50:40Z","description":"CosmWasm + zkVM RISC-V EFI template"},
        {"full_name":"bmorphism/penrose-mcp","language":"JavaScript","stargazers_count":9,"forks_count":4,"open_issues_count":0,"pushed_at":"2025-01-20T21:44:55Z","description":"Penrose server for Infinity-Topos"},
        {"full_name":"bmorphism/magic-world-org","language":"Python","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-05T07:03:50Z","description":"Magic World Org (Local MLX)"},
        {"full_name":"bmorphism/world","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-06-02T06:49:02Z","description":"Local worlds launcher for SA3, jank, and world proofs"},
        {"full_name":"bmorphism/hypernym-mcp-server","language":"JavaScript","stargazers_count":6,"forks_count":5,"open_issues_count":0,"pushed_at":"2025-04-02T21:21:08Z","description":None},
        {"full_name":"bmorphism/nats-mcp-server","language":None,"stargazers_count":7,"forks_count":3,"open_issues_count":2,"pushed_at":"2025-01-06T23:33:41Z","description":"MCP server for NATS messaging system"},
        {"full_name":"bmorphism/marginalia-mcp-server","language":"JavaScript","stargazers_count":8,"forks_count":6,"open_issues_count":0,"pushed_at":"2025-01-06T05:47:24Z","description":"MCP server for managing marginalia and annotations"},
        {"full_name":"bmorphism/vibespace-mcp-go-ternary","language":"HTML","stargazers_count":0,"forks_count":1,"open_issues_count":3,"pushed_at":"2026-01-11T12:50:40Z","description":"Go MCP experience with NATS streaming and balanced ternary"},
        {"full_name":"bmorphism/shitcoin","language":"Python","stargazers_count":5,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-08T08:07:08Z","description":"gets denom for cw20 assets"},
        {"full_name":"bmorphism/open-location-code-zig","language":"Zig","stargazers_count":3,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-12-30T19:33:45Z","description":"Open Location Code for Zig"},
        {"full_name":"bmorphism/monero-rental-hash-war","language":"Haskell","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-10-05T23:08:54Z","description":"Compositional OpenGame analysis of Monero rental hash war"},
        {"full_name":"bmorphism/oxgame","language":"OCaml","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-05-15T09:53:27Z","description":"Stellar resolution and open-game composition for OCaml"},
    ]),
    "zubyul": ("user", [
        {"full_name":"zubyul/voice-observatory","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-24T05:56:17Z","description":"Passive macOS TUI observing voice-download pathways"},
        {"full_name":"zubyul/ghostel-emacs-worlds","language":"GLSL","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-24T00:20:56Z","description":"Ghostty config + ghostel family + alice/bob emacs-mods"},
        {"full_name":"zubyul/nash-tui","language":"Rust","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-13T07:45:16Z","description":"NASH token TUI: real-time candles"},
        {"full_name":"zubyul/big-bad-plurigrid-quiz","language":"Emacs Lisp","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-09T18:51:31Z","description":"27 flashcards from bmorphism/plurigrid/zubyul recent activity"},
        {"full_name":"zubyul/Gay.jl","language":"Julia","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-28T11:30:01Z","description":"Wide-gamut color sampling with splittable determinism"},
        {"full_name":"zubyul/kinesis-kb360pro","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-26T10:29:40Z","description":"Claude Code skill for Kinesis Advantage360 Pro"},
        {"full_name":"zubyul/gay-world","language":"Python","stargazers_count":1,"forks_count":1,"open_issues_count":0,"pushed_at":"2026-03-26T04:03:39Z","description":"Goblin world builder: each goblin is a world"},
        {"full_name":"zubyul/tilelang-kernels","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-16T02:31:13Z","description":"TileLang GPU kernels for SplitMix64 color generation, GF(3) trit classification"},
        {"full_name":"zubyul/gay-terminal-colors","language":"Clojure","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-02-21T07:38:14Z","description":"Gay.jl world_terminal_fingerprint"},
        {"full_name":"zubyul/plurigrid-site","language":"Svelte","stargazers_count":0,"forks_count":1,"open_issues_count":11,"pushed_at":"2026-02-04T03:20:08Z","description":"Plurigrid world: site deployment"},
        {"full_name":"zubyul/vibesnipe","language":"Move","stargazers_count":0,"forks_count":0,"open_issues_count":1,"pushed_at":"2026-01-30T22:36:03Z","description":None},
        {"full_name":"zubyul/jonikas_lab_data_analysis_misc","language":"Jupyter Notebook","stargazers_count":2,"forks_count":0,"open_issues_count":0,"pushed_at":"2023-08-16T20:24:40Z","description":"various scripts used to process large genetic sequence data"},
        {"full_name":"zubyul/WGCNA","language":"HTML","stargazers_count":2,"forks_count":0,"open_issues_count":0,"pushed_at":"2023-07-05T18:02:30Z","description":"weighted gene correlation network analysis project"},
    ]),
    "migalkin": ("user", [
        {"full_name":"migalkin/NodePiece","language":"Python","stargazers_count":144,"forks_count":21,"open_issues_count":0,"pushed_at":"2026-05-07T05:40:02Z","description":"Compositional and Parameter-Efficient Representations for Large Knowledge Graphs"},
        {"full_name":"migalkin/StarE","language":"Python","stargazers_count":89,"forks_count":16,"open_issues_count":1,"pushed_at":"2026-04-16T14:12:45Z","description":"EMNLP 2020: Message Passing for Hyper-Relational Knowledge Graphs"},
        {"full_name":"migalkin/RWL","language":"Python","stargazers_count":8,"forks_count":1,"open_issues_count":0,"pushed_at":"2026-05-28T20:19:20Z","description":"Weisfeiler and Leman Go Relational"},
        {"full_name":"migalkin/NBFNet_mlx","language":"Python","stargazers_count":10,"forks_count":1,"open_issues_count":1,"pushed_at":"2026-03-11T01:31:21Z","description":"Neural Bellman-Ford networks in MLX for Apple Silicon"},
        {"full_name":"migalkin/kgcourse2021","language":"HTML","stargazers_count":25,"forks_count":9,"open_issues_count":0,"pushed_at":"2026-02-16T05:16:08Z","description":"Knowledge Graphs course materials"},
        {"full_name":"migalkin/rambo","language":"Rust","stargazers_count":3,"forks_count":0,"open_issues_count":1,"pushed_at":"2023-02-28T16:37:22Z","description":None},
    ]),
    "DJedamski": ("user", [
        {"full_name":"DJedamski/kaggle_ncaa18","language":"Jupyter Notebook","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2018-02-26T16:33:24Z","description":"Code for NCAA March Madness competition"},
        {"full_name":"DJedamski/Kaggle","language":None,"stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2023-04-21T01:42:35Z","description":None},
        {"full_name":"DJedamski/Getting-and-Cleaning-Data","language":"R","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2023-04-21T01:42:34Z","description":"Coursera Project"},
        {"full_name":"DJedamski/School","language":"R","stargazers_count":1,"forks_count":1,"open_issues_count":0,"pushed_at":"2023-04-21T01:42:33Z","description":"Projects from grad school"},
    ]),
    "wasita": ("user", [
        {"full_name":"wasita/wasita.github.io","language":"Svelte","stargazers_count":1,"forks_count":0,"open_issues_count":8,"pushed_at":"2026-07-02T01:40:18Z","description":"personal website"},
        {"full_name":"wasita/proj-template","language":None,"stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-06-19T21:22:21Z","description":None},
        {"full_name":"wasita/magic-garden","language":"Python","stargazers_count":2,"forks_count":1,"open_issues_count":1,"pushed_at":"2026-04-22T21:16:43Z","description":"bot for magic garden discord activity game"},
        {"full_name":"wasita/send2kobo","language":"TypeScript","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-05-19T02:59:26Z","description":"Website for sending books to your kobo e-reader"},
        {"full_name":"wasita/vocoder","language":"JavaScript","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-05-06T05:14:03Z","description":None},
    ]),
    "kristinezheng": ("user", [
        {"full_name":"kristinezheng/kristinezheng.github.io","language":"HTML","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-07-01T20:57:48Z","description":None},
        {"full_name":"kristinezheng/lookit-jenga","language":"Jupyter Notebook","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2024-05-16T18:29:05Z","description":"Lookit study for 9.85"},
        {"full_name":"kristinezheng/Green-Machine","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2021-09-19T05:33:04Z","description":"HackMIT 2021: Sustainability Track"},
    ]),
    "M1shaaa": ("user", [
        {"full_name":"M1shaaa/lab-bookshelf-","language":"TypeScript","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2024-12-31T05:11:18Z","description":None},
        {"full_name":"M1shaaa/Python-Lookit-Uploads","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2024-02-15T22:59:37Z","description":"random projects"},
    ]),
    "AustinCStone": ("user", [
        {"full_name":"AustinCStone/EpsteinSearch","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-02-11T01:10:57Z","description":None},
        {"full_name":"AustinCStone/TextGAN","language":"Python","stargazers_count":92,"forks_count":30,"open_issues_count":5,"pushed_at":"2025-03-03T13:26:32Z","description":"A generative adversarial network for text generation"},
        {"full_name":"AustinCStone/StereoVisionMRF","language":"Python","stargazers_count":11,"forks_count":4,"open_issues_count":0,"pushed_at":"2026-04-01T07:39:41Z","description":"Recover 3D geometry from videos with unknown camera calibration"},
        {"full_name":"AustinCStone/SpectralClustering","language":"Python","stargazers_count":3,"forks_count":2,"open_issues_count":0,"pushed_at":"2021-04-16T08:46:36Z","description":"Spectral clustering"},
        {"full_name":"AustinCStone/RealTimeRayTracingFractalWorld","language":"C++","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2015-05-11T01:58:57Z","description":"Real time ray tracing of a fractal world"},
    ]),
}

# Insert repo_snapshots and world_increments
increment_id = 0
repo_id = 0

for source_name, (source_type, repos) in sources.items():
    for repo in repos:
        increment_id += 1
        repo_id += 1
        trit, color, name = gf3(increment_id)
        h = snap_hash(repo["full_name"], repo.get("pushed_at", ""))

        con.execute("""
            INSERT INTO world_increments VALUES (?, now(), ?, ?, ?, ?, ?, 'repo_push', ?, ?, ?)
        """, [increment_id, trit, color, name, source_type, source_name,
              repo["full_name"], source_name, h])

        parts = repo["full_name"].split("/", 1)
        repo_name = parts[1] if len(parts) == 2 else repo["full_name"]

        con.execute("""
            INSERT INTO repo_snapshots VALUES (?, now(), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, [repo_id, increment_id, source_name, repo_name, repo["full_name"],
              repo.get("language"), repo.get("stargazers_count", 0),
              repo.get("forks_count", 0), repo.get("open_issues_count", 0),
              repo.get("pushed_at"), repo.get("description")])

print(f"Inserted {increment_id} increments, {repo_id} repo snapshots")

# Insert Aptos balances
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
    con.execute("INSERT INTO aptos_snapshots VALUES (now(), ?, ?, ?)", [world, addr, bal])
print(f"Inserted {len(aptos_data)} Aptos snapshots (all 0 — APT CoinStore not registered)")

# Insert multisig probes
multisig_data = [
    ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2,True),
    ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2,True),
    ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2,True),
    ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2,True),
    ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2,True),
]
for pair, addr, sigs, healthy in multisig_data:
    con.execute("INSERT INTO multisig_probes VALUES (now(), ?, ?, ?, ?)", [pair, addr, sigs, healthy])
print(f"Inserted {len(multisig_data)} multisig probes (all healthy, sigs_required=2)")

# MNX: unavailable (Vercel auth required)
# No rows inserted; note in summary

# Final counts
counts = con.execute("""
SELECT
  (SELECT COUNT(*) FROM world_increments) as increments,
  (SELECT COUNT(*) FROM repo_snapshots) as repos,
  (SELECT COUNT(*) FROM aptos_snapshots) as aptos,
  (SELECT COUNT(*) FROM multisig_probes) as multisigs
""").fetchone()
print(f"DB totals: increments={counts[0]}, repos={counts[1]}, aptos={counts[2]}, multisigs={counts[3]}")

# Sample GF3 distribution
gf3_dist = con.execute("""
SELECT gf3_name, gf3_color, COUNT(*) as cnt
FROM world_increments
GROUP BY gf3_name, gf3_color
ORDER BY gf3_name
""").fetchall()
for row in gf3_dist:
    print(f"  GF3 {row[0]} {row[1]}: {row[2]}")

con.close()
print("Database built successfully:", DB_PATH)
