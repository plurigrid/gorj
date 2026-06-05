#!/usr/bin/env python3
"""Build world-increments DuckDB: GitHub social graph + Aptos hamming swarm snapshot."""
import duckdb, json, hashlib
from datetime import datetime

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
con = duckdb.connect(DB)

for stmt in [
    """CREATE TABLE IF NOT EXISTS world_increments (
      id INTEGER, timestamp TIMESTAMP DEFAULT now(), gf3_trit INTEGER,
      gf3_color VARCHAR, gf3_name VARCHAR, source_type VARCHAR,
      source_name VARCHAR, event_type VARCHAR, repo_name VARCHAR,
      actor VARCHAR, snapshot_hash VARCHAR)""",
    """CREATE TABLE IF NOT EXISTS repo_snapshots (
      id INTEGER, timestamp TIMESTAMP DEFAULT now(), increment_id INTEGER,
      org_or_user VARCHAR, repo_name VARCHAR, full_name VARCHAR,
      language VARCHAR, stars INTEGER, forks INTEGER, open_issues INTEGER,
      pushed_at VARCHAR, description VARCHAR)""",
    """CREATE TABLE IF NOT EXISTS aptos_snapshots (
      timestamp TIMESTAMP DEFAULT now(),
      world VARCHAR, address VARCHAR, balance_apt DOUBLE)""",
    """CREATE TABLE IF NOT EXISTS multisig_probes (
      timestamp TIMESTAMP DEFAULT now(),
      pair VARCHAR, address VARCHAR, sigs_required INTEGER, healthy BOOLEAN)""",
    """CREATE TABLE IF NOT EXISTS mnx_snapshots (
      timestamp TIMESTAMP DEFAULT now(),
      ticker VARCHAR, name VARCHAR, category VARCHAR,
      price DOUBLE, change_pct DOUBLE)""",
]:
    con.execute(stmt)

GF3 = {0: (0, "#d3869b", "ERGODIC"), 1: (1, "#b8bb26", "PLUS"), 2: (-1, "#cc241d", "MINUS")}
def gf3(n): return GF3[n % 3]
def snap_hash(d): return hashlib.sha256(json.dumps(d, sort_keys=True, default=str).encode()).hexdigest()[:16]

ts = datetime.utcnow().isoformat()

# ── ALL REPOS ─────────────────────────────────────────────────────────────────
repos = [
# plurigrid
{"org_or_user":"plurigrid","full_name":"plurigrid/gorj","repo_name":"gorj","language":"Clojure","stars":0,"forks":0,"open_issues":376,"pushed_at":"2026-06-05T17:17:13Z","description":"forj + Rama topology nREPL routing + GF(3) gay trit coloring for compositional open game REPL orchestration"},
{"org_or_user":"plurigrid","full_name":"plurigrid/place","repo_name":"place","language":"TeX","stars":1,"forks":2,"open_issues":8,"pushed_at":"2026-06-04T09:51:50Z","description":None},
{"org_or_user":"plurigrid","full_name":"plurigrid/eirobri","repo_name":"eirobri","language":"Clojure","stars":0,"forks":0,"open_issues":29,"pushed_at":"2026-06-03T20:43:46Z","description":"EiRoBri replay world"},
{"org_or_user":"plurigrid","full_name":"plurigrid/nash-portal","repo_name":"nash-portal","language":"Rust","stars":2,"forks":3,"open_issues":1,"pushed_at":"2026-05-19T01:49:59Z","description":"NASH token TUI in the browser — ratzilla WASM + GeckoTerminal OHLCV candlesticks"},
{"org_or_user":"plurigrid","full_name":"plurigrid/zig-syrup","repo_name":"zig-syrup","language":"Zig","stars":2,"forks":2,"open_issues":0,"pushed_at":"2026-04-30T03:52:16Z","description":"High-performance Zig implementation of OCapN Syrup with CapTP optimizations"},
{"org_or_user":"plurigrid","full_name":"plurigrid/asi","repo_name":"asi","language":"HTML","stars":25,"forks":6,"open_issues":4,"pushed_at":"2026-04-26T08:51:41Z","description":"everything is topological chemputer!"},
{"org_or_user":"plurigrid","full_name":"plurigrid/asi-skills","repo_name":"asi-skills","language":"Julia","stars":3,"forks":1,"open_issues":0,"pushed_at":"2026-04-26T08:09:26Z","description":"69 skills with Galois Hole Type accessibility"},
{"org_or_user":"plurigrid","full_name":"plurigrid/nanoclj-zig","repo_name":"nanoclj-zig","language":"Zig","stars":1,"forks":2,"open_issues":20,"pushed_at":"2026-04-25T07:29:09Z","description":"NaN-boxed Clojure interpreter in Zig 0.15"},
{"org_or_user":"plurigrid","full_name":"plurigrid/bci-blue-share","repo_name":"bci-blue-share","language":"JavaScript","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-26T07:08:03Z","description":"BCI signal infrastructure"},
{"org_or_user":"plurigrid","full_name":"plurigrid/spi-race","repo_name":"spi-race","language":"Swift","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-21T19:31:56Z","description":"Splitmix Parallel Integrity — deterministic color generation"},
{"org_or_user":"plurigrid","full_name":"plurigrid/reafference","repo_name":"reafference","language":"HTML","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-16T05:21:49Z","description":"Reafference adaptation workspace"},
{"org_or_user":"plurigrid","full_name":"plurigrid/web-browser","repo_name":"web-browser","language":"Rust","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-10T02:54:47Z","description":"web-browser — from prepostweb lineage"},
{"org_or_user":"plurigrid","full_name":"plurigrid/vivarium","repo_name":"vivarium","language":"Clojure","stars":1,"forks":0,"open_issues":0,"pushed_at":"2026-04-08T08:38:37Z","description":None},
{"org_or_user":"plurigrid","full_name":"plurigrid/flowglad-rs","repo_name":"flowglad-rs","language":"Rust","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-08T07:56:15Z","description":None},
{"org_or_user":"plurigrid","full_name":"plurigrid/tree-sitter-nanoclj-zig","repo_name":"tree-sitter-nanoclj-zig","language":"C","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-04T07:48:21Z","description":"Tree-sitter grammar for nanoclj-zig"},
{"org_or_user":"plurigrid","full_name":"plurigrid/forester","repo_name":"forester","language":"XSLT","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-03-30T01:32:26Z","description":"CatColab mathematical documentation forest"},
{"org_or_user":"plurigrid","full_name":"plurigrid/gatomic","repo_name":"gatomic","language":"Clojure","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-03-30T00:54:48Z","description":"Deterministic color identity store — Gay + Datomic + Atomic"},
{"org_or_user":"plurigrid","full_name":"plurigrid/blue","repo_name":"blue","language":"TeX","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-03-29T23:06:32Z","description":None},
{"org_or_user":"plurigrid","full_name":"plurigrid/nblm-flashcards","repo_name":"nblm-flashcards","language":"Hy","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-03-26T08:23:01Z","description":"NotebookLM Enterprise flashcard pipeline"},
{"org_or_user":"plurigrid","full_name":"plurigrid/graded-optic","repo_name":"graded-optic","language":"Haskell","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-02-08T16:10:16Z","description":"Semiring-graded bidirectional processes"},
{"org_or_user":"plurigrid","full_name":"plurigrid/shepherd","repo_name":"shepherd","language":"Scheme","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-01-23T07:47:28Z","description":"Spritely Shepherd - Service manager"},
{"org_or_user":"plurigrid","full_name":"plurigrid/hoot","repo_name":"hoot","language":"Scheme","stars":0,"forks":0,"open_issues":1,"pushed_at":"2026-01-23T07:47:10Z","description":"Spritely Hoot - Scheme to WebAssembly compiler"},
{"org_or_user":"plurigrid","full_name":"plurigrid/gay-tofu","repo_name":"gay-tofu","language":"HTML","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-01-08T15:14:34Z","description":"Low-discrepancy color sequences for visual TOFU authentication"},
{"org_or_user":"plurigrid","full_name":"plurigrid/lazygay","repo_name":"lazygay","language":"Go","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-01-08T14:19:25Z","description":"lazygit fork with Gay.jl deterministic commit coloring"},
{"org_or_user":"plurigrid","full_name":"plurigrid/gay-rs","repo_name":"gay-rs","language":"Rust","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-01-08T14:19:22Z","description":"Rust crate for Gay.jl deterministic coloring with GF(3) trits"},
{"org_or_user":"plurigrid","full_name":"plurigrid/agent-o-rama","repo_name":"agent-o-rama","language":"Clojure","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-01-02T01:09:22Z","description":None},
{"org_or_user":"plurigrid","full_name":"plurigrid/ontology","repo_name":"ontology","language":"JavaScript","stars":8,"forks":9,"open_issues":16,"pushed_at":"2025-05-27T18:18:34Z","description":"autopoietic ergodicity and embodied gradualism"},
{"org_or_user":"plurigrid","full_name":"plurigrid/Plurigraph","repo_name":"Plurigraph","language":"JavaScript","stars":3,"forks":5,"open_issues":4,"pushed_at":"2025-01-05T08:39:09Z","description":"Plurigrid knowledge base for use with Obsidian.md"},
{"org_or_user":"plurigrid","full_name":"plurigrid/StochFlow","repo_name":"StochFlow","language":"Python","stars":4,"forks":1,"open_issues":0,"pushed_at":"2024-03-20T23:34:57Z","description":"Stochastic interpolant models — diffusive and flow-based processes"},
{"org_or_user":"plurigrid","full_name":"plurigrid/act","repo_name":"act","language":"Python","stars":3,"forks":1,"open_issues":4,"pushed_at":"2024-07-26T08:27:08Z","description":"building blocks for cognitive category theory"},
{"org_or_user":"plurigrid","full_name":"plurigrid/agent","repo_name":"agent","language":"Python","stars":5,"forks":1,"open_issues":6,"pushed_at":"2023-03-31T18:45:23Z","description":"Framework for agency amplification"},
{"org_or_user":"plurigrid","full_name":"plurigrid/vcg-auction","repo_name":"vcg-auction","language":"Rust","stars":7,"forks":2,"open_issues":1,"pushed_at":"2023-03-16T21:53:08Z","description":"a simple contract that performs a VCG auction"},
{"org_or_user":"plurigrid","full_name":"plurigrid/microworlds","repo_name":"microworlds","language":"Rust","stars":3,"forks":5,"open_issues":3,"pushed_at":"2023-05-13T03:54:56Z","description":None},
{"org_or_user":"plurigrid","full_name":"plurigrid/duck-kanban","repo_name":"duck-kanban","language":"Rust","stars":1,"forks":0,"open_issues":0,"pushed_at":"2025-09-26T20:18:38Z","description":"Duck intelligence kanban system"},
{"org_or_user":"plurigrid","full_name":"plurigrid/aptos-wallet-ruby","repo_name":"aptos-wallet-ruby","language":"Ruby","stars":1,"forks":0,"open_issues":0,"pushed_at":"2025-09-30T22:47:22Z","description":None},
# kubeflow
{"org_or_user":"kubeflow","full_name":"kubeflow/kubeflow","repo_name":"kubeflow","language":None,"stars":15706,"forks":2670,"open_issues":3,"pushed_at":"2026-05-24T11:31:41Z","description":"Machine Learning Toolkit for Kubernetes"},
{"org_or_user":"kubeflow","full_name":"kubeflow/pipelines","repo_name":"pipelines","language":"Python","stars":4152,"forks":2007,"open_issues":489,"pushed_at":"2026-06-05T15:11:18Z","description":"Machine Learning Pipelines for Kubeflow"},
{"org_or_user":"kubeflow","full_name":"kubeflow/spark-operator","repo_name":"spark-operator","language":"Python","stars":3125,"forks":1488,"open_issues":99,"pushed_at":"2026-06-04T17:55:40Z","description":"Kubernetes operator for Apache Spark"},
{"org_or_user":"kubeflow","full_name":"kubeflow/trainer","repo_name":"trainer","language":"Go","stars":2111,"forks":964,"open_issues":123,"pushed_at":"2026-06-05T03:17:48Z","description":"Distributed AI Model Training and LLM Fine-Tuning on Kubernetes"},
{"org_or_user":"kubeflow","full_name":"kubeflow/katib","repo_name":"katib","language":"Python","stars":1684,"forks":525,"open_issues":120,"pushed_at":"2026-06-04T01:14:59Z","description":"Automated Machine Learning on Kubernetes"},
{"org_or_user":"kubeflow","full_name":"kubeflow/examples","repo_name":"examples","language":"Jsonnet","stars":1462,"forks":756,"open_issues":111,"pushed_at":"2025-04-14T01:54:52Z","description":"Extended examples and tutorials"},
{"org_or_user":"kubeflow","full_name":"kubeflow/manifests","repo_name":"manifests","language":"YAML","stars":1020,"forks":1065,"open_issues":22,"pushed_at":"2026-06-05T14:42:22Z","description":"Kubeflow Community Distribution"},
{"org_or_user":"kubeflow","full_name":"kubeflow/arena","repo_name":"arena","language":"Go","stars":811,"forks":191,"open_issues":49,"pushed_at":"2026-05-07T06:46:17Z","description":"A CLI for Kubeflow"},
{"org_or_user":"kubeflow","full_name":"kubeflow/kale","repo_name":"kale","language":"Python","stars":690,"forks":155,"open_issues":48,"pushed_at":"2026-06-04T20:31:45Z","description":"Kubeflow's superfood for Data Scientists"},
{"org_or_user":"kubeflow","full_name":"kubeflow/mpi-operator","repo_name":"mpi-operator","language":"Go","stars":528,"forks":235,"open_issues":103,"pushed_at":"2026-06-02T14:30:58Z","description":"Kubernetes operator for MPI-based applications"},
{"org_or_user":"kubeflow","full_name":"kubeflow/fairing","repo_name":"fairing","language":"Jsonnet","stars":337,"forks":143,"open_issues":134,"pushed_at":"2022-04-11T05:28:47Z","description":"Python SDK for building, training, and deploying ML models"},
{"org_or_user":"kubeflow","full_name":"kubeflow/pytorch-operator","repo_name":"pytorch-operator","language":"Jsonnet","stars":310,"forks":143,"open_issues":63,"pushed_at":"2021-12-01T17:44:48Z","description":"PyTorch on Kubernetes"},
{"org_or_user":"kubeflow","full_name":"kubeflow/mcp-apache-spark-history-server","repo_name":"mcp-apache-spark-history-server","language":"Python","stars":174,"forks":62,"open_issues":22,"pushed_at":"2026-06-04T17:24:33Z","description":"MCP Server and CLI for Apache Spark History Server"},
{"org_or_user":"kubeflow","full_name":"kubeflow/kfp-tekton","repo_name":"kfp-tekton","language":"TypeScript","stars":182,"forks":123,"open_issues":79,"pushed_at":"2024-11-19T12:23:51Z","description":"Kubeflow Pipelines on Tekton"},
{"org_or_user":"kubeflow","full_name":"kubeflow/website","repo_name":"website","language":"HTML","stars":184,"forks":921,"open_issues":43,"pushed_at":"2026-06-05T02:01:44Z","description":"Kubeflow Website"},
{"org_or_user":"kubeflow","full_name":"kubeflow/hub","repo_name":"hub","language":"Go","stars":175,"forks":182,"open_issues":41,"pushed_at":"2026-06-05T15:39:48Z","description":"Model Registry for ML model developers"},
{"org_or_user":"kubeflow","full_name":"kubeflow","repo_name":"community","language":"Jupyter Notebook","stars":194,"forks":257,"open_issues":15,"pushed_at":"2026-06-05T17:29:18Z","description":"Kubeflow community proposals and governance"},
{"org_or_user":"kubeflow","full_name":"kubeflow/kfctl","repo_name":"kfctl","language":"Go","stars":182,"forks":134,"open_issues":94,"pushed_at":"2023-08-15T20:19:22Z","description":"kfctl is a CLI for deploying and managing Kubeflow"},
{"org_or_user":"kubeflow","full_name":"kubeflow/sdk","repo_name":"sdk","language":"Python","stars":120,"forks":181,"open_issues":137,"pushed_at":"2026-06-04T03:07:45Z","description":"Universal Python SDK to run AI workloads on Kubernetes"},
{"org_or_user":"kubeflow","full_name":"kubeflow/notebooks","repo_name":"notebooks","language":None,"stars":73,"forks":119,"open_issues":183,"pushed_at":"2026-06-05T15:36:12Z","description":"Kubeflow Notebooks: interactive development environments"},
# TeglonLabs
{"org_or_user":"TeglonLabs","full_name":"TeglonLabs/mathpix-gem","repo_name":"mathpix-gem","language":"Ruby","stars":2,"forks":0,"open_issues":11,"pushed_at":"2026-01-01T12:13:16Z","description":"Transform mathematical images to LaTeX"},
{"org_or_user":"TeglonLabs","full_name":"TeglonLabs/coin-flip-mcp","repo_name":"coin-flip-mcp","language":"JavaScript","stars":0,"forks":2,"open_issues":1,"pushed_at":"2025-03-16T01:31:45Z","description":"MCP server for flipping coins with varying degrees of randomness"},
{"org_or_user":"TeglonLabs","full_name":"TeglonLabs/monad-mcp-server","repo_name":"monad-mcp-server","language":None,"stars":0,"forks":0,"open_issues":0,"pushed_at":"2025-05-14T17:53:01Z","description":"Monad MCP Server"},
{"org_or_user":"TeglonLabs","full_name":"TeglonLabs/topoi","repo_name":"topoi","language":"Python","stars":0,"forks":0,"open_issues":1,"pushed_at":"2025-01-24T06:47:38Z","description":None},
# bmorphism
{"org_or_user":"bmorphism","full_name":"bmorphism/Gay.jl","repo_name":"Gay.jl","language":"Julia","stars":1,"forks":0,"open_issues":189,"pushed_at":"2026-06-05T00:41:24Z","description":"Wide-gamut color sampling with splittable determinism (Pigeons.jl SPI pattern)"},
{"org_or_user":"bmorphism","full_name":"bmorphism/world","repo_name":"world","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-06-02T06:49:02Z","description":"Local worlds launcher for SA3, jank, and world proofs"},
{"org_or_user":"bmorphism","full_name":"bmorphism/ocaml-mcp-sdk","repo_name":"ocaml-mcp-sdk","language":"OCaml","stars":61,"forks":2,"open_issues":0,"pushed_at":"2026-03-16T05:24:25Z","description":"OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect library"},
{"org_or_user":"bmorphism","full_name":"bmorphism/say-mcp-server","repo_name":"say-mcp-server","language":"JavaScript","stars":20,"forks":9,"open_issues":3,"pushed_at":"2025-01-07T03:15:18Z","description":"MCP server for macOS text-to-speech functionality"},
{"org_or_user":"bmorphism","full_name":"bmorphism/babashka-mcp-server","repo_name":"babashka-mcp-server","language":"JavaScript","stars":19,"forks":6,"open_issues":3,"pushed_at":"2025-01-05T11:09:42Z","description":"A Model Context Protocol server for interacting with Babashka"},
{"org_or_user":"bmorphism","full_name":"bmorphism/anti-bullshit-mcp-server","repo_name":"anti-bullshit-mcp-server","language":"JavaScript","stars":23,"forks":7,"open_issues":1,"pushed_at":"2026-01-16T08:54:58Z","description":"MCP server for analyzing claims and detecting manipulation"},
{"org_or_user":"bmorphism","full_name":"bmorphism/manifold-mcp-server","repo_name":"manifold-mcp-server","language":"JavaScript","stars":14,"forks":9,"open_issues":5,"pushed_at":"2025-01-11T10:36:58Z","description":"MCP server for interacting with Manifold Markets prediction markets"},
{"org_or_user":"bmorphism","full_name":"bmorphism/marginalia-mcp-server","repo_name":"marginalia-mcp-server","language":"JavaScript","stars":8,"forks":6,"open_issues":0,"pushed_at":"2025-01-06T05:47:24Z","description":"MCP server for managing marginalia and annotations"},
{"org_or_user":"bmorphism","full_name":"bmorphism/hypernym-mcp-server","repo_name":"hypernym-mcp-server","language":"JavaScript","stars":6,"forks":5,"open_issues":0,"pushed_at":"2025-04-02T21:21:08Z","description":None},
{"org_or_user":"bmorphism","full_name":"bmorphism/penrose-mcp","repo_name":"penrose-mcp","language":"JavaScript","stars":10,"forks":4,"open_issues":0,"pushed_at":"2025-01-20T21:44:55Z","description":"Penrose server for the Infinity-Topos environment"},
{"org_or_user":"bmorphism","full_name":"bmorphism/risc0-cosmwasm-example","repo_name":"risc0-cosmwasm-example","language":"Rust","stars":23,"forks":2,"open_issues":1,"pushed_at":"2022-10-20T23:50:40Z","description":"CosmWasm + zkVM RISC-V EFI template"},
{"org_or_user":"bmorphism","full_name":"bmorphism/nats-mcp-server","repo_name":"nats-mcp-server","language":None,"stars":7,"forks":3,"open_issues":2,"pushed_at":"2025-01-06T23:33:41Z","description":"MCP server for NATS messaging system"},
{"org_or_user":"bmorphism","full_name":"bmorphism/oxgame","repo_name":"oxgame","language":"OCaml","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-05-15T09:53:27Z","description":"Stellar resolution and open-game composition for OCaml"},
{"org_or_user":"bmorphism","full_name":"bmorphism/shitcoin","repo_name":"shitcoin","language":"Python","stars":5,"forks":0,"open_issues":0,"pushed_at":"2026-04-08T08:07:08Z","description":"gets denom for cw20 assets for permissionless degeneracy in IBC"},
{"org_or_user":"bmorphism","full_name":"bmorphism/vibespace-mcp-go-ternary","repo_name":"vibespace-mcp-go-ternary","language":"HTML","stars":0,"forks":1,"open_issues":3,"pushed_at":"2026-01-11T12:50:40Z","description":"MCP experience for vibes and worlds with NATS streaming and balanced ternary"},
{"org_or_user":"bmorphism","full_name":"bmorphism/magic-world-org","repo_name":"magic-world-org","language":"Python","stars":1,"forks":0,"open_issues":0,"pushed_at":"2026-04-05T07:03:50Z","description":"Magic World Org (Local MLX)"},
{"org_or_user":"bmorphism","full_name":"bmorphism/flox-mcp-bb","repo_name":"flox-mcp-bb","language":"Clojure","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-02-12T02:45:43Z","description":"Open-source MCP server for Flox — Babashka/Clojure, 20 tools"},
{"org_or_user":"bmorphism","full_name":"bmorphism/penumbra-mcp","repo_name":"penumbra-mcp","language":"JavaScript","stars":5,"forks":6,"open_issues":3,"pushed_at":"2025-01-07T01:15:23Z","description":"MCP server for Penumbra blockchain"},
{"org_or_user":"bmorphism","full_name":"bmorphism/monero-rental-hash-war","repo_name":"monero-rental-hash-war","language":"Haskell","stars":1,"forks":0,"open_issues":0,"pushed_at":"2025-10-05T23:08:54Z","description":"Compositional OpenGame analysis of Monero rental hash war"},
{"org_or_user":"bmorphism","full_name":"bmorphism/meso","repo_name":"meso","language":"Jupyter Notebook","stars":1,"forks":1,"open_issues":0,"pushed_at":"2023-08-09T06:04:11Z","description":"Scripts simulating approximation of inverse transformations of probabilistic Markov Kernels"},
{"org_or_user":"bmorphism","full_name":"bmorphism/plurigrid-celo","repo_name":"plurigrid-celo","language":"TypeScript","stars":1,"forks":1,"open_issues":0,"pushed_at":"2022-12-09T10:07:25Z","description":"Celo e-app for Albany Plurigrid"},
# zubyul
{"org_or_user":"zubyul","full_name":"zubyul/voice-observatory","repo_name":"voice-observatory","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-24T05:56:20Z","description":"Passive macOS TUI observing voice-download pathways"},
{"org_or_user":"zubyul","full_name":"zubyul/Gay.jl","repo_name":"Gay.jl","language":"Julia","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-03-28T11:30:07Z","description":"Wide-gamut color sampling with splittable determinism"},
{"org_or_user":"zubyul","full_name":"zubyul/gay-world","repo_name":"gay-world","language":"Python","stars":1,"forks":1,"open_issues":0,"pushed_at":"2026-04-05T06:54:03Z","description":"Goblin world builder: each goblin is a world"},
{"org_or_user":"zubyul","full_name":"zubyul/tilelang-kernels","repo_name":"tilelang-kernels","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-03-16T02:31:16Z","description":"TileLang GPU kernels for GF(3) trit classification and Sinkhorn OT"},
{"org_or_user":"zubyul","full_name":"zubyul/kinesis-kb360pro","repo_name":"kinesis-kb360pro","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-03-26T10:29:44Z","description":"Claude Code skill for Kinesis Advantage360 Pro keyboard with GF(3) color analysis"},
{"org_or_user":"zubyul","full_name":"zubyul/big-bad-plurigrid-quiz","repo_name":"big-bad-plurigrid-quiz","language":"Emacs Lisp","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-09T18:51:35Z","description":"27 flashcards from bmorphism/plurigrid/zubyul recent activity"},
{"org_or_user":"zubyul","full_name":"zubyul/plurigrid-site","repo_name":"plurigrid-site","language":"Svelte","stars":0,"forks":1,"open_issues":11,"pushed_at":"2026-03-26T09:06:31Z","description":"Plurigrid world: site deployment"},
{"org_or_user":"zubyul","full_name":"zubyul/WGCNA","repo_name":"WGCNA","language":"HTML","stars":2,"forks":0,"open_issues":0,"pushed_at":"2026-03-26T09:05:26Z","description":"weighted gene correlation network analysis project"},
{"org_or_user":"zubyul","full_name":"zubyul/jonikas_lab_data_analysis_misc","repo_name":"jonikas_lab_data_analysis_misc","language":"Jupyter Notebook","stars":2,"forks":0,"open_issues":0,"pushed_at":"2026-03-26T09:05:21Z","description":"various scripts used to process large genetic sequence data"},
{"org_or_user":"zubyul","full_name":"zubyul/Nikolova_lab_data_analysis","repo_name":"Nikolova_lab_data_analysis","language":"R","stars":2,"forks":0,"open_issues":0,"pushed_at":"2026-03-26T09:05:23Z","description":"undergraduate thesis — cortical thickness to transcription factors for depression"},
# migalkin
{"org_or_user":"migalkin","full_name":"migalkin/NodePiece","repo_name":"NodePiece","language":"Python","stars":144,"forks":21,"open_issues":0,"pushed_at":"2026-05-07T05:40:02Z","description":"Compositional and Parameter-Efficient Representations for Large Knowledge Graphs (ICLR 22)"},
{"org_or_user":"migalkin","full_name":"migalkin/StarE","repo_name":"StarE","language":"Python","stars":89,"forks":16,"open_issues":1,"pushed_at":"2026-04-16T14:12:45Z","description":"EMNLP 2020: Message Passing for Hyper-Relational Knowledge Graphs"},
{"org_or_user":"migalkin","full_name":"migalkin/kgcourse2021","repo_name":"kgcourse2021","language":"HTML","stars":25,"forks":9,"open_issues":0,"pushed_at":"2026-02-16T05:16:08Z","description":"Knowledge Graphs course materials"},
{"org_or_user":"migalkin","full_name":"migalkin/NBFNet_mlx","repo_name":"NBFNet_mlx","language":"Python","stars":10,"forks":1,"open_issues":1,"pushed_at":"2026-03-11T01:31:21Z","description":"Neural Bellman-Ford networks implemented in MLX for Apple Silicon"},
{"org_or_user":"migalkin","full_name":"migalkin/RWL","repo_name":"RWL","language":"Python","stars":8,"forks":1,"open_issues":0,"pushed_at":"2026-05-28T20:19:20Z","description":"Weisfeiler and Leman Go Relational (LOG 2022)"},
{"org_or_user":"migalkin","full_name":"migalkin/rambo","repo_name":"rambo","language":"Rust","stars":3,"forks":0,"open_issues":1,"pushed_at":"2023-02-28T16:37:22Z","description":None},
# wasita
{"org_or_user":"wasita","full_name":"wasita/wasita.github.io","repo_name":"wasita.github.io","language":"Svelte","stars":1,"forks":0,"open_issues":8,"pushed_at":"2026-06-01T04:15:14Z","description":"personal website"},
{"org_or_user":"wasita","full_name":"wasita/vocoder","repo_name":"vocoder","language":"JavaScript","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-05-06T05:14:03Z","description":None},
{"org_or_user":"wasita","full_name":"wasita/magic-garden","repo_name":"magic-garden","language":"Python","stars":2,"forks":1,"open_issues":1,"pushed_at":"2026-04-22T21:16:43Z","description":"bot for magic garden discord auto-purchasing seeds"},
{"org_or_user":"wasita","full_name":"wasita/wm-cv","repo_name":"wm-cv","language":"Svelte","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-05-13T05:29:08Z","description":"Academic CV as single page web app"},
{"org_or_user":"wasita","full_name":"wasita/send2kobo","repo_name":"send2kobo","language":"TypeScript","stars":1,"forks":0,"open_issues":0,"pushed_at":"2026-05-19T02:59:26Z","description":"Website for sending books to your kobo e-reader"},
# kristinezheng
{"org_or_user":"kristinezheng","full_name":"kristinezheng/kristinezheng.github.io","repo_name":"kristinezheng.github.io","language":"HTML","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-05-14T22:29:01Z","description":None},
{"org_or_user":"kristinezheng","full_name":"kristinezheng/lookit-jenga","repo_name":"lookit-jenga","language":"Jupyter Notebook","stars":0,"forks":0,"open_issues":0,"pushed_at":"2024-05-16T18:29:05Z","description":"Lookit study for 9.85"},
# M1shaaa
{"org_or_user":"M1shaaa","full_name":"M1shaaa/lab-bookshelf-","repo_name":"lab-bookshelf-","language":"TypeScript","stars":0,"forks":0,"open_issues":0,"pushed_at":"2024-12-31T05:11:18Z","description":None},
{"org_or_user":"M1shaaa","full_name":"M1shaaa/Python-Lookit-Uploads","repo_name":"Python-Lookit-Uploads","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2024-02-15T22:59:37Z","description":"random projects"},
# AustinCStone
{"org_or_user":"AustinCStone","full_name":"AustinCStone/TextGAN","repo_name":"TextGAN","language":"Python","stars":92,"forks":30,"open_issues":5,"pushed_at":"2025-03-03T13:26:32Z","description":"A generative adversarial network for text generation, written in TensorFlow"},
{"org_or_user":"AustinCStone","full_name":"AustinCStone/StereoVisionMRF","repo_name":"StereoVisionMRF","language":"Python","stars":11,"forks":4,"open_issues":0,"pushed_at":"2026-04-01T07:39:41Z","description":"Infer depth from stereo images using MRF with loopy belief propagation"},
{"org_or_user":"AustinCStone","full_name":"AustinCStone/EpsteinSearch","repo_name":"EpsteinSearch","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-02-11T01:10:57Z","description":None},
{"org_or_user":"AustinCStone","full_name":"AustinCStone/Connectomics","repo_name":"Connectomics","language":"TeX","stars":0,"forks":0,"open_issues":0,"pushed_at":"2014-05-22T19:27:53Z","description":"Kaggle Connectomics Challenge — infer neural connectome from fluorescence data"},
# DJedamski
{"org_or_user":"DJedamski","full_name":"DJedamski/Kaggle","repo_name":"Kaggle","language":None,"stars":1,"forks":0,"open_issues":0,"pushed_at":"2023-04-21T01:42:35Z","description":None},
{"org_or_user":"DJedamski","full_name":"DJedamski/School","repo_name":"School","language":"R","stars":1,"forks":1,"open_issues":0,"pushed_at":"2023-04-21T01:42:33Z","description":"Small projects from grad school"},
{"org_or_user":"DJedamski","full_name":"DJedamski/kaggle_ncaa18","repo_name":"kaggle_ncaa18","language":"Jupyter Notebook","stars":0,"forks":0,"open_issues":0,"pushed_at":"2018-02-26T16:33:24Z","description":"Code for NCAA March Madness competition (2018)"},
]

print(f"Total repos to insert: {len(repos)}")
inc_id = 1
repo_id = 1
for r in repos:
    trit, color, name = gf3(inc_id)
    h = snap_hash(r)
    con.execute(
        "INSERT INTO world_increments VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        [inc_id, ts, trit, color, name, "github_repo",
         r["org_or_user"], "repo_snapshot", r["repo_name"],
         r["org_or_user"], h])
    con.execute(
        "INSERT INTO repo_snapshots VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
        [repo_id, ts, inc_id, r["org_or_user"], r["repo_name"], r["full_name"],
         r.get("language"), r.get("stars", 0), r.get("forks", 0),
         r.get("open_issues", 0), r.get("pushed_at"), r.get("description")])
    inc_id += 1
    repo_id += 1

# ── APTOS SNAPSHOTS ───────────────────────────────────────────────────────────
aptos = [
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
for world, addr, bal in aptos:
    con.execute("INSERT INTO aptos_snapshots VALUES (?,?,?,?)", [ts, world, addr, bal])

# ── MULTISIG PROBES ───────────────────────────────────────────────────────────
for pair, addr, sigs, healthy in [
    ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2,True),
    ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2,True),
    ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2,True),
    ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2,True),
    ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2,True),
]:
    con.execute("INSERT INTO multisig_probes VALUES (?,?,?,?,?)", [ts, pair, addr, sigs, healthy])

con.commit()

# ── SUMMARY STATS ─────────────────────────────────────────────────────────────
total_repos   = con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0]
total_inc     = con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0]
top_stars     = con.execute("SELECT full_name, stars FROM repo_snapshots ORDER BY stars DESC LIMIT 10").fetchall()
by_lang       = con.execute("SELECT language, COUNT(*) FROM repo_snapshots WHERE language IS NOT NULL GROUP BY language ORDER BY 2 DESC LIMIT 10").fetchall()
by_org        = con.execute("SELECT org_or_user, COUNT(*) FROM repo_snapshots GROUP BY org_or_user ORDER BY 2 DESC").fetchall()
gf3_dist      = con.execute("SELECT gf3_name, gf3_color, COUNT(*) FROM world_increments GROUP BY gf3_name, gf3_color ORDER BY gf3_name").fetchall()
msig_rows     = con.execute("SELECT pair, sigs_required, healthy FROM multisig_probes ORDER BY pair").fetchall()
aptos_rows    = con.execute("SELECT world, address, balance_apt FROM aptos_snapshots ORDER BY world").fetchall()

con.close()

print("=== DATABASE BUILT SUCCESSFULLY ===")
print(f"Total repo_snapshots: {total_repos}")
print(f"Total world_increments: {total_inc}")
print(f"\nTop 10 by stars:")
for fn, s in top_stars:
    print(f"  {fn}: ★{s}")
print(f"\nTop languages:")
for lang, cnt in by_lang:
    print(f"  {lang}: {cnt}")
print(f"\nRepos by org/user:")
for org, cnt in by_org:
    print(f"  {org}: {cnt}")
print(f"\nGF(3) color distribution:")
for name, color, cnt in gf3_dist:
    print(f"  {name} {color}: {cnt}")
print(f"\nMultisig probes:")
for pair, sigs, healthy in msig_rows:
    print(f"  {pair}: sigs={sigs} healthy={healthy}")
print(f"\nAptos swarm: {len(aptos_rows)} wallets, all balance=0.0 APT (CoinStore not found / unfunded)")
