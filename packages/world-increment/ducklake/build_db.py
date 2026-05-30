#!/usr/bin/env python3
"""Build world-increments DuckDB from collected social graph + Aptos data."""
import duckdb, json, hashlib
from datetime import datetime

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"

def gf3(id_):
    t = id_ % 3
    if t == 0: return 0, "ERGODIC", "#d3869b"
    if t == 1: return 1, "PLUS", "#b8bb26"
    return -1, "MINUS", "#cc241d"

def snap_hash(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()[:16]

con = duckdb.connect(DB_PATH)

# ── Schema ──────────────────────────────────────────────────────────────────
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
con.execute("CREATE SEQUENCE IF NOT EXISTS increment_seq START 1")
con.execute("CREATE SEQUENCE IF NOT EXISTS repo_seq START 1")

# ── Repo data ────────────────────────────────────────────────────────────────
# All orgs/users → (source, repos_list)
SOURCES = {
    "plurigrid": "org",
    "kubeflow": "org",
    "TeglonLabs": "org",
    "bmorphism": "user",
    "zubyul": "user",
    "migalkin": "user",
    "DJedamski": "user",
    "wasita": "user",
    "kristinezheng": "user",
    "M1shaaa": "user",
    "AustinCStone": "user",
}

# Inline all collected repo data
REPOS = [
# plurigrid
{"org":"plurigrid","name":"place","full_name":"plurigrid/place","language":"TeX","stars":1,"forks":1,"open_issues":10,"pushed_at":"2026-05-21T18:08:38Z","description":""},
{"org":"plurigrid","name":"eirobri","full_name":"plurigrid/eirobri","language":"Clojure","stars":0,"forks":0,"open_issues":28,"pushed_at":"2026-05-19T06:43:05Z","description":"EiRoBri replay world"},
{"org":"plurigrid","name":"nash-portal","full_name":"plurigrid/nash-portal","language":"Rust","stars":2,"forks":3,"open_issues":1,"pushed_at":"2026-05-19T01:50:03Z","description":"NASH token TUI in the browser"},
{"org":"plurigrid","name":"gorj","full_name":"plurigrid/gorj","language":"Clojure","stars":0,"forks":0,"open_issues":257,"pushed_at":"2026-05-08T14:06:40Z","description":"forj + Rama topology nREPL routing + GF(3) gay trit coloring"},
{"org":"plurigrid","name":"zig-syrup","full_name":"plurigrid/zig-syrup","language":"Zig","stars":2,"forks":2,"open_issues":0,"pushed_at":"2026-04-30T03:52:19Z","description":"High-performance Zig implementation of OCapN Syrup"},
{"org":"plurigrid","name":"asi","full_name":"plurigrid/asi","language":"HTML","stars":23,"forks":6,"open_issues":4,"pushed_at":"2026-05-17T14:27:10Z","description":"everything is topological chemputer!"},
{"org":"plurigrid","name":"asi-skills","full_name":"plurigrid/asi-skills","language":"Julia","stars":3,"forks":1,"open_issues":0,"pushed_at":"2026-04-26T08:09:31Z","description":"69 skills with Galois Hole Type accessibility"},
{"org":"plurigrid","name":"bci-blue-share","full_name":"plurigrid/bci-blue-share","language":"JavaScript","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-26T07:08:06Z","description":"BCI signal infrastructure"},
{"org":"plurigrid","name":"nanoclj-zig","full_name":"plurigrid/nanoclj-zig","language":"Zig","stars":1,"forks":2,"open_issues":20,"pushed_at":"2026-04-25T07:29:13Z","description":"NaN-boxed Clojure interpreter in Zig 0.15"},
{"org":"plurigrid","name":"spi-race","full_name":"plurigrid/spi-race","language":"Swift","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-21T19:32:01Z","description":"Splitmix Parallel Integrity — deterministic color generation"},
{"org":"plurigrid","name":"reafference","full_name":"plurigrid/reafference","language":"HTML","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-16T05:21:32Z","description":"Reafference adaptation workspace"},
{"org":"plurigrid","name":"web-browser","full_name":"plurigrid/web-browser","language":"Rust","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-10T02:54:51Z","description":"web-browser from prepostweb lineage"},
{"org":"plurigrid","name":"vivarium","full_name":"plurigrid/vivarium","language":"Clojure","stars":1,"forks":0,"open_issues":0,"pushed_at":"2026-04-08T22:49:56Z","description":""},
{"org":"plurigrid","name":"flowglad-rs","full_name":"plurigrid/flowglad-rs","language":"Rust","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-08T07:56:19Z","description":""},
{"org":"plurigrid","name":"tree-sitter-nanoclj-zig","full_name":"plurigrid/tree-sitter-nanoclj-zig","language":"C","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-04T07:48:25Z","description":"Tree-sitter grammar for nanoclj-zig"},
{"org":"plurigrid","name":"forester","full_name":"plurigrid/forester","language":"XSLT","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-03-30T01:32:30Z","description":"CatColab mathematical documentation forest"},
{"org":"plurigrid","name":"gatomic","full_name":"plurigrid/gatomic","language":"Clojure","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-03-30T00:54:51Z","description":"Deterministic color identity store with sonification"},
{"org":"plurigrid","name":"blue","full_name":"plurigrid/blue","language":"TeX","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-03-29T23:06:37Z","description":""},
{"org":"plurigrid","name":"red","full_name":"plurigrid/red","language":None,"stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-03-29T22:58:46Z","description":""},
{"org":"plurigrid","name":"nblm-flashcards","full_name":"plurigrid/nblm-flashcards","language":"Hy","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-03-26T08:23:04Z","description":"NotebookLM Enterprise flashcard pipeline"},
{"org":"plurigrid","name":"gemini-agent","full_name":"plurigrid/gemini-agent","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-02-19T06:39:19Z","description":""},
{"org":"plurigrid","name":"graded-optic","full_name":"plurigrid/graded-optic","language":"Haskell","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-02-08T16:10:19Z","description":"Semiring-graded bidirectional processes"},
{"org":"plurigrid","name":"json-canvas","full_name":"plurigrid/json-canvas","language":None,"stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-02-06T06:51:00Z","description":"JSON Canvas: Real-time interaction data capture"},
{"org":"plurigrid","name":"shepherd","full_name":"plurigrid/shepherd","language":"Scheme","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-01-23T07:49:09Z","description":"Spritely Shepherd - Service manager"},
{"org":"plurigrid","name":"goblinshare","full_name":"plurigrid/goblinshare","language":"Scheme","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-01-23T07:47:17Z","description":"P2P filesharing demo for Goblins"},
{"org":"plurigrid","name":"magenc","full_name":"plurigrid/magenc","language":"Scheme","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-01-23T07:47:17Z","description":"Magenc Magnet URIs - Secure Object Permanence"},
{"org":"plurigrid","name":"hoot","full_name":"plurigrid/hoot","language":"Scheme","stars":0,"forks":0,"open_issues":1,"pushed_at":"2026-01-23T07:49:08Z","description":"Spritely Hoot - Scheme to WebAssembly compiler"},
{"org":"plurigrid","name":"leprechauns","full_name":"plurigrid/leprechauns","language":"Racket","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-01-23T07:45:06Z","description":"Spritely Goblins + Gay.jl semantic colors"},
{"org":"plurigrid","name":"spritely-semantic-colors","full_name":"plurigrid/spritely-semantic-colors","language":None,"stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-01-23T07:38:36Z","description":"Deterministic color mappings for Spritely/Goblins"},
{"org":"plurigrid","name":"gay-tofu","full_name":"plurigrid/gay-tofu","language":"HTML","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-01-08T15:14:38Z","description":"Low-discrepancy color sequences for visual TOFU"},
{"org":"plurigrid","name":"lazygay","full_name":"plurigrid/lazygay","language":"Go","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-01-08T14:19:29Z","description":"lazygit fork with Gay.jl deterministic commit coloring"},
{"org":"plurigrid","name":"gay-terminal","full_name":"plurigrid/gay-terminal","language":"Rust","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-01-08T14:19:27Z","description":"Terminal ANSI coloring with Gay.jl"},
{"org":"plurigrid","name":"gay-go","full_name":"plurigrid/gay-go","language":"Go","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-01-08T14:19:26Z","description":"Go implementation of Gay.jl deterministic coloring"},
{"org":"plurigrid","name":"gay-rs","full_name":"plurigrid/gay-rs","language":"Rust","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-01-08T14:19:26Z","description":"Rust crate for Gay.jl deterministic coloring"},
{"org":"plurigrid","name":"lazybjj","full_name":"plurigrid/lazybjj","language":"Rust","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-01-08T14:19:32Z","description":"TUI for jj with Gay.jl GF(3) coloring"},
{"org":"plurigrid","name":"agent-o-rama","full_name":"plurigrid/agent-o-rama","language":"Clojure","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-01-01T23:39:06Z","description":""},
{"org":"plurigrid","name":"aptos-wallet-ruby","full_name":"plurigrid/aptos-wallet-ruby","language":"Ruby","stars":1,"forks":0,"open_issues":0,"pushed_at":"2025-10-24T09:25:13Z","description":""},
{"org":"plurigrid","name":"duck-kanban","full_name":"plurigrid/duck-kanban","language":"Rust","stars":1,"forks":0,"open_issues":0,"pushed_at":"2025-10-24T09:24:59Z","description":"Duck intelligence kanban system"},
{"org":"plurigrid","name":"ontology","full_name":"plurigrid/ontology","language":"JavaScript","stars":8,"forks":9,"open_issues":16,"pushed_at":"2026-05-09T04:20:49Z","description":"autopoietic ergodicity and embodied gradualism"},
{"org":"plurigrid","name":"Plurigraph","full_name":"plurigrid/Plurigraph","language":"JavaScript","stars":3,"forks":5,"open_issues":4,"pushed_at":"2026-05-12T03:19:41Z","description":"Plurigrid knowledge base for use with Obsidian.md"},
{"org":"plurigrid","name":"microworlds","full_name":"plurigrid/microworlds","language":"Rust","stars":3,"forks":5,"open_issues":3,"pushed_at":"2024-03-14T00:12:46Z","description":""},
{"org":"plurigrid","name":"vcg-auction","full_name":"plurigrid/vcg-auction","language":"Rust","stars":7,"forks":2,"open_issues":1,"pushed_at":"2025-12-16T12:32:02Z","description":"a simple contract that performs a VCG auction"},
{"org":"plurigrid","name":"agent","full_name":"plurigrid/agent","language":"Python","stars":5,"forks":1,"open_issues":6,"pushed_at":"2024-10-16T11:33:13Z","description":"Framework for agency amplification"},
{"org":"plurigrid","name":"StochFlow","full_name":"plurigrid/StochFlow","language":"Python","stars":4,"forks":1,"open_issues":0,"pushed_at":"2024-08-15T02:58:54Z","description":"stochastic interpolant models"},
{"org":"plurigrid","name":"act","full_name":"plurigrid/act","language":"Python","stars":3,"forks":1,"open_issues":4,"pushed_at":"2024-11-25T09:36:59Z","description":"building blocks for cognitive category theory"},
# kubeflow
{"org":"kubeflow","name":"pipelines","full_name":"kubeflow/pipelines","language":"Python","stars":4150,"forks":2003,"open_issues":483,"pushed_at":"2026-05-29T21:13:22Z","description":"Machine Learning Pipelines for Kubeflow"},
{"org":"kubeflow","name":"hub","full_name":"kubeflow/hub","language":"Go","stars":175,"forks":180,"open_issues":36,"pushed_at":"2026-05-29T21:13:19Z","description":"Model Registry for ML model developers"},
{"org":"kubeflow","name":"mcp-apache-spark-history-server","full_name":"kubeflow/mcp-apache-spark-history-server","language":"Python","stars":173,"forks":61,"open_issues":20,"pushed_at":"2026-05-29T18:32:23Z","description":"MCP Server and CLI for Apache Spark History Server"},
{"org":"kubeflow","name":"manifests","full_name":"kubeflow/manifests","language":"YAML","stars":1019,"forks":1065,"open_issues":23,"pushed_at":"2026-05-29T16:51:56Z","description":"Kubeflow AI Reference Platform Deployment Manifests"},
{"org":"kubeflow","name":"kale","full_name":"kubeflow/kale","language":"Python","stars":691,"forks":155,"open_issues":46,"pushed_at":"2026-05-29T16:27:46Z","description":"Kubeflow's superfood for Data Scientists"},
{"org":"kubeflow","name":"mpi-operator","full_name":"kubeflow/mpi-operator","language":"Go","stars":527,"forks":235,"open_issues":101,"pushed_at":"2026-05-29T15:41:59Z","description":"Kubernetes Operator for MPI-based applications"},
{"org":"kubeflow","name":"trainer","full_name":"kubeflow/trainer","language":"Go","stars":2107,"forks":963,"open_issues":127,"pushed_at":"2026-05-29T10:51:02Z","description":"Distributed AI Model Training and LLM Fine-Tuning"},
{"org":"kubeflow","name":"kubeflow","full_name":"kubeflow/kubeflow","language":None,"stars":15686,"forks":2662,"open_issues":3,"pushed_at":"2026-05-30T01:32:46Z","description":"Machine Learning Toolkit for Kubernetes"},
{"org":"kubeflow","name":"katib","full_name":"kubeflow/katib","language":"Python","stars":1685,"forks":525,"open_issues":123,"pushed_at":"2026-05-28T12:12:22Z","description":"Automated Machine Learning on Kubernetes"},
{"org":"kubeflow","name":"spark-operator","full_name":"kubeflow/spark-operator","language":"Python","stars":3124,"forks":1487,"open_issues":101,"pushed_at":"2026-05-25T04:50:23Z","description":"Kubernetes operator for Apache Spark"},
{"org":"kubeflow","name":"sdk","full_name":"kubeflow/sdk","language":"Python","stars":118,"forks":181,"open_issues":134,"pushed_at":"2026-05-28T07:53:16Z","description":"Universal Python SDK to run AI workloads on Kubernetes"},
{"org":"kubeflow","name":"notebooks","full_name":"kubeflow/notebooks","language":None,"stars":73,"forks":115,"open_issues":195,"pushed_at":"2026-05-27T18:38:21Z","description":"Kubeflow Notebooks"},
{"org":"kubeflow","name":"examples","full_name":"kubeflow/examples","language":"Jsonnet","stars":1463,"forks":755,"open_issues":111,"pushed_at":"2026-05-15T19:11:13Z","description":"A repository to host extended examples and tutorials"},
{"org":"kubeflow","name":"arena","full_name":"kubeflow/arena","language":"Go","stars":811,"forks":191,"open_issues":56,"pushed_at":"2026-05-27T10:10:48Z","description":"A CLI for Kubeflow"},
{"org":"kubeflow","name":"website","full_name":"kubeflow/website","language":"HTML","stars":184,"forks":920,"open_issues":50,"pushed_at":"2026-05-28T14:07:40Z","description":"Kubeflow Website"},
{"org":"kubeflow","name":"dashboard","full_name":"kubeflow/dashboard","language":"TypeScript","stars":16,"forks":57,"open_issues":82,"pushed_at":"2026-05-25T04:50:23Z","description":"Kubeflow Central Dashboard"},
{"org":"kubeflow","name":"docs-agent","full_name":"kubeflow/docs-agent","language":"Python","stars":37,"forks":97,"open_issues":153,"pushed_at":"2026-05-19T06:07:18Z","description":"Kubeflow Documentation AI Agent"},
{"org":"kubeflow","name":"community","full_name":"kubeflow/community","language":"Jupyter Notebook","stars":195,"forks":257,"open_issues":18,"pushed_at":"2026-05-21T23:12:12Z","description":"Kubeflow community information"},
{"org":"kubeflow","name":"mcp-server","full_name":"kubeflow/mcp-server","language":"Python","stars":10,"forks":17,"open_issues":22,"pushed_at":"2026-05-21T13:09:35Z","description":"MCP Server for AI-Assisted Development with Kubeflow Tools"},
# TeglonLabs
{"org":"TeglonLabs","name":"mathpix-gem","full_name":"TeglonLabs/mathpix-gem","language":"Ruby","stars":2,"forks":0,"open_issues":11,"pushed_at":"2026-01-01T12:13:16Z","description":"Transform mathematical images to LaTeX"},
{"org":"TeglonLabs","name":"coin-flip-mcp","full_name":"TeglonLabs/coin-flip-mcp","language":"JavaScript","stars":0,"forks":2,"open_issues":1,"pushed_at":"2025-03-16T01:31:45Z","description":"MCP server for flipping coins with varying degrees of randomness"},
{"org":"TeglonLabs","name":"monad-mcp-server","full_name":"TeglonLabs/monad-mcp-server","language":None,"stars":0,"forks":0,"open_issues":0,"pushed_at":"2025-05-14T17:53:01Z","description":"Monad MCP Server"},
{"org":"TeglonLabs","name":"topoi","full_name":"TeglonLabs/topoi","language":"Python","stars":0,"forks":0,"open_issues":1,"pushed_at":"2025-01-24T06:47:38Z","description":""},
# zubyul
{"org":"zubyul","name":"voice-observatory","full_name":"zubyul/voice-observatory","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-24T05:56:20Z","description":"Passive macOS TUI observing voice-download pathways"},
{"org":"zubyul","name":"ghostel-emacs-worlds","full_name":"zubyul/ghostel-emacs-worlds","language":"GLSL","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-24T00:21:00Z","description":"Ghostty config + ghostel family + alice/bob emacs-mods"},
{"org":"zubyul","name":"big-bad-plurigrid-quiz","full_name":"zubyul/big-bad-plurigrid-quiz","language":"Emacs Lisp","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-09T18:51:35Z","description":"27 flashcards from bmorphism/plurigrid/zubyul activity"},
{"org":"zubyul","name":"Gay.jl","full_name":"zubyul/Gay.jl","language":"Julia","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-03-28T11:30:07Z","description":"Wide-gamut color sampling with splittable determinism"},
{"org":"zubyul","name":"kinesis-kb360pro","full_name":"zubyul/kinesis-kb360pro","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-03-26T10:29:44Z","description":"Claude Code skill for Kinesis Advantage360 Pro keyboard"},
{"org":"zubyul","name":"gay-world","full_name":"zubyul/gay-world","language":"Python","stars":1,"forks":1,"open_issues":0,"pushed_at":"2026-04-05T06:54:03Z","description":"Goblin world builder: each goblin is a world"},
{"org":"zubyul","name":"from-possible-worlds","full_name":"zubyul/from-possible-worlds","language":"TeX","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-03-16T03:07:20Z","description":""},
{"org":"zubyul","name":"tilelang-kernels","full_name":"zubyul/tilelang-kernels","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-03-16T02:31:16Z","description":"TileLang GPU kernels for SplitMix64 color generation"},
{"org":"zubyul","name":"plurigrid-site","full_name":"zubyul/plurigrid-site","language":"Svelte","stars":0,"forks":1,"open_issues":11,"pushed_at":"2026-03-26T09:06:31Z","description":"Plurigrid world: site deployment"},
{"org":"zubyul","name":"hue-world","full_name":"zubyul/hue-world","language":"JavaScript","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-03-26T09:05:56Z","description":"Terminal Vibe Snipe puzzle game"},
{"org":"zubyul","name":"multiplayer-emacs","full_name":"zubyul/multiplayer-emacs","language":"HTML","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-03-26T09:06:00Z","description":"Multiplayer world: Emacs split-pane Vibe Snipe"},
{"org":"zubyul","name":"zubyul.github.io","full_name":"zubyul/zubyul.github.io","language":"CSS","stars":1,"forks":0,"open_issues":0,"pushed_at":"2026-03-26T09:05:35Z","description":""},
{"org":"zubyul","name":"jonikas_lab_data_analysis_misc","full_name":"zubyul/jonikas_lab_data_analysis_misc","language":"Jupyter Notebook","stars":2,"forks":0,"open_issues":0,"pushed_at":"2026-03-26T09:05:21Z","description":"various scripts for genetic sequence data"},
{"org":"zubyul","name":"WGCNA","full_name":"zubyul/WGCNA","language":"HTML","stars":2,"forks":0,"open_issues":0,"pushed_at":"2026-03-26T09:05:26Z","description":"weighted gene correlation network analysis"},
{"org":"zubyul","name":"Nikolova_lab_data_analysis","full_name":"zubyul/Nikolova_lab_data_analysis","language":"R","stars":2,"forks":0,"open_issues":0,"pushed_at":"2026-03-26T09:05:23Z","description":"undergraduate thesis - cortical thickness to transcription factors"},
# Social graph: migalkin
{"org":"migalkin","name":"kgcourse2021","full_name":"migalkin/kgcourse2021","language":"HTML","stars":25,"forks":9,"open_issues":0,"pushed_at":"2026-02-16T05:16:08Z","description":"Course materials on Knowledge Graphs"},
{"org":"migalkin","name":"NodePiece","full_name":"migalkin/NodePiece","language":"Python","stars":144,"forks":21,"open_issues":0,"pushed_at":"2026-05-07T05:40:02Z","description":"Compositional and Parameter-Efficient Representations for Large KGs"},
{"org":"migalkin","name":"StarE","full_name":"migalkin/StarE","language":"Python","stars":89,"forks":16,"open_issues":1,"pushed_at":"2026-04-16T14:12:45Z","description":"Message Passing for Hyper-Relational Knowledge Graphs"},
{"org":"migalkin","name":"RWL","full_name":"migalkin/RWL","language":"Python","stars":8,"forks":1,"open_issues":0,"pushed_at":"2026-05-28T20:19:20Z","description":"Weisfeiler and Leman Go Relational"},
{"org":"migalkin","name":"NBFNet_mlx","full_name":"migalkin/NBFNet_mlx","language":"Python","stars":10,"forks":1,"open_issues":1,"pushed_at":"2026-03-11T01:31:21Z","description":"Neural Bellman-Ford networks in MLX for Apple Silicon"},
{"org":"migalkin","name":"migalkin.github.io","full_name":"migalkin/migalkin.github.io","language":"JavaScript","stars":0,"forks":0,"open_issues":0,"pushed_at":"2025-05-20T23:58:08Z","description":"Academic personal website"},
# Social graph: wasita
{"org":"wasita","name":"wasita.github.io","full_name":"wasita/wasita.github.io","language":"Svelte","stars":1,"forks":0,"open_issues":8,"pushed_at":"2026-05-20T22:38:02Z","description":"personal website"},
{"org":"wasita","name":"wm-cv","full_name":"wasita/wm-cv","language":"Svelte","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-05-13T05:29:08Z","description":"Academic CV written as a single page web app"},
{"org":"wasita","name":"send2kobo","full_name":"wasita/send2kobo","language":"TypeScript","stars":1,"forks":0,"open_issues":0,"pushed_at":"2026-05-19T02:59:26Z","description":"Website for sending books to your kobo e-reader"},
{"org":"wasita","name":"vocoder","full_name":"wasita/vocoder","language":"JavaScript","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-05-06T05:14:03Z","description":""},
{"org":"wasita","name":"magic-garden","full_name":"wasita/magic-garden","language":"Python","stars":2,"forks":1,"open_issues":1,"pushed_at":"2026-04-22T21:16:43Z","description":"bot for magic garden discord game"},
{"org":"wasita","name":"ch3-lib","full_name":"wasita/ch3-lib","language":"Typst","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-12T04:03:22Z","description":""},
# Social graph: kristinezheng
{"org":"kristinezheng","name":"kristinezheng.github.io","full_name":"kristinezheng/kristinezheng.github.io","language":"HTML","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-05-14T22:29:01Z","description":""},
{"org":"kristinezheng","name":"lookit-jenga","full_name":"kristinezheng/lookit-jenga","language":"Jupyter Notebook","stars":0,"forks":0,"open_issues":0,"pushed_at":"2024-05-16T18:29:05Z","description":"Lookit study"},
# Social graph: M1shaaa
{"org":"M1shaaa","name":"M1shaaa","full_name":"M1shaaa/M1shaaa","language":None,"stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-02-04T19:32:04Z","description":"Config files for GitHub profile"},
{"org":"M1shaaa","name":"lab-bookshelf-","full_name":"M1shaaa/lab-bookshelf-","language":"TypeScript","stars":0,"forks":0,"open_issues":0,"pushed_at":"2024-12-31T05:11:18Z","description":""},
# Social graph: AustinCStone
{"org":"AustinCStone","name":"EpsteinSearch","full_name":"AustinCStone/EpsteinSearch","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-02-11T01:10:57Z","description":""},
{"org":"AustinCStone","name":"bmforkupdate","full_name":"AustinCStone/bmforkupdate","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2025-05-09T04:50:16Z","description":""},
{"org":"AustinCStone","name":"TextGAN","full_name":"AustinCStone/TextGAN","language":"Python","stars":92,"forks":30,"open_issues":5,"pushed_at":"2025-03-03T13:26:32Z","description":"A generative adversarial network for text generation"},
{"org":"AustinCStone","name":"StereoVisionMRF","full_name":"AustinCStone/StereoVisionMRF","language":"Python","stars":11,"forks":4,"open_issues":0,"pushed_at":"2026-04-01T07:39:41Z","description":"Using a MRF with loopy belief propagation for stereo vision"},
{"org":"AustinCStone","name":"stonks","full_name":"AustinCStone/stonks","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2020-09-04T22:54:35Z","description":"Playing around with some option calculations"},
# Social graph: DJedamski
{"org":"DJedamski","name":"kaggle_ncaa18","full_name":"DJedamski/kaggle_ncaa18","language":"Jupyter Notebook","stars":0,"forks":0,"open_issues":0,"pushed_at":"2018-02-26T16:33:24Z","description":"NCAA March Madness competition (2018)"},
{"org":"DJedamski","name":"Kaggle","full_name":"DJedamski/Kaggle","language":None,"stars":1,"forks":0,"open_issues":0,"pushed_at":"2023-04-21T01:42:35Z","description":""},
{"org":"DJedamski","name":"School","full_name":"DJedamski/School","language":"R","stars":1,"forks":1,"open_issues":0,"pushed_at":"2023-04-21T01:42:33Z","description":"A couple small projects from grad school"},
# bmorphism
{"org":"bmorphism","name":"Gay.jl","full_name":"bmorphism/Gay.jl","language":"Julia","stars":1,"forks":0,"open_issues":189,"pushed_at":"2026-05-30T00:37:13Z","description":"Wide-gamut color sampling with splittable determinism"},
{"org":"bmorphism","name":"oxgame","full_name":"bmorphism/oxgame","language":"OCaml","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-05-15T09:53:27Z","description":"Stellar resolution and open-game composition for OCaml"},
{"org":"bmorphism","name":"ocaml-mcp-sdk","full_name":"bmorphism/ocaml-mcp-sdk","language":"OCaml","stars":61,"forks":2,"open_issues":0,"pushed_at":"2026-03-16T05:24:25Z","description":"OCaml SDK for Model Context Protocol"},
{"org":"bmorphism","name":"anti-bullshit-mcp-server","full_name":"bmorphism/anti-bullshit-mcp-server","language":"JavaScript","stars":23,"forks":7,"open_issues":1,"pushed_at":"2026-01-16T08:54:58Z","description":"MCP server for analyzing claims and detecting manipulation"},
{"org":"bmorphism","name":"say-mcp-server","full_name":"bmorphism/say-mcp-server","language":"JavaScript","stars":20,"forks":9,"open_issues":3,"pushed_at":"2025-01-07T03:15:18Z","description":"MCP server for macOS text-to-speech functionality"},
{"org":"bmorphism","name":"babashka-mcp-server","full_name":"bmorphism/babashka-mcp-server","language":"JavaScript","stars":18,"forks":6,"open_issues":3,"pushed_at":"2025-01-05T11:09:42Z","description":"MCP server for interacting with Babashka"},
{"org":"bmorphism","name":"manifold-mcp-server","full_name":"bmorphism/manifold-mcp-server","language":"JavaScript","stars":14,"forks":9,"open_issues":5,"pushed_at":"2025-01-11T10:36:58Z","description":"MCP server for Manifold Markets prediction markets"},
{"org":"bmorphism","name":"penrose-mcp","full_name":"bmorphism/penrose-mcp","language":"JavaScript","stars":10,"forks":4,"open_issues":0,"pushed_at":"2025-01-20T21:44:55Z","description":"Penrose server for the Infinity-Topos environment"},
{"org":"bmorphism","name":"marginalia-mcp-server","full_name":"bmorphism/marginalia-mcp-server","language":"JavaScript","stars":8,"forks":6,"open_issues":0,"pushed_at":"2025-01-06T05:47:24Z","description":"MCP server for managing marginalia and annotations"},
{"org":"bmorphism","name":"nats-mcp-server","full_name":"bmorphism/nats-mcp-server","language":None,"stars":7,"forks":3,"open_issues":2,"pushed_at":"2025-01-06T23:33:41Z","description":"MCP server for NATS messaging system"},
{"org":"bmorphism","name":"penumbra-mcp","full_name":"bmorphism/penumbra-mcp","language":"JavaScript","stars":5,"forks":6,"open_issues":3,"pushed_at":"2025-01-07T01:15:23Z","description":"MCP server for Penumbra blockchain"},
{"org":"bmorphism","name":"shitcoin","full_name":"bmorphism/shitcoin","language":"Python","stars":5,"forks":0,"open_issues":0,"pushed_at":"2026-04-08T08:07:08Z","description":"gets denom for cw20 assets for permissionless degeneracy in IBC"},
{"org":"bmorphism","name":"hypernym-mcp-server","full_name":"bmorphism/hypernym-mcp-server","language":"JavaScript","stars":6,"forks":5,"open_issues":0,"pushed_at":"2025-04-02T21:21:08Z","description":""},
{"org":"bmorphism","name":"risc0-cosmwasm-example","full_name":"bmorphism/risc0-cosmwasm-example","language":"Rust","stars":23,"forks":2,"open_issues":1,"pushed_at":"2022-10-20T23:50:40Z","description":"CosmWasm + zkVM RISC-V EFI template"},
{"org":"bmorphism","name":"whale","full_name":"bmorphism/whale","language":"MATLAB","stars":2,"forks":0,"open_issues":0,"pushed_at":"2025-09-04T06:55:21Z","description":"omniglot + sperm whale codas = metawhaling"},
{"org":"bmorphism","name":"vibespace-mcp-go-ternary","full_name":"bmorphism/vibespace-mcp-go-ternary","language":"HTML","stars":0,"forks":1,"open_issues":3,"pushed_at":"2026-01-11T12:50:40Z","description":"Go MCP experience for vibes and worlds with NATS"},
{"org":"bmorphism","name":"open-location-code-zig","full_name":"bmorphism/open-location-code-zig","language":"Zig","stars":3,"forks":0,"open_issues":0,"pushed_at":"2025-12-30T19:33:45Z","description":"Open Location Code for Zig"},
{"org":"bmorphism","name":"zig-syrup","full_name":"bmorphism/zig-syrup","language":"Zig","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-05-07T19:49:05Z","description":"Embeddable OCapN Syrup encoder/decoder in Zig"},
{"org":"bmorphism","name":"monero-rental-hash-war","full_name":"bmorphism/monero-rental-hash-war","language":"Haskell","stars":1,"forks":0,"open_issues":0,"pushed_at":"2025-10-05T23:08:54Z","description":"Compositional OpenGame analysis of Monero rental hash war"},
{"org":"bmorphism","name":"slowtime-mcp-server","full_name":"bmorphism/slowtime-mcp-server","language":"TypeScript","stars":3,"forks":5,"open_issues":6,"pushed_at":"2025-01-02T01:23:33Z","description":"MCP server for secure time-based operations"},
]

# ── Insert repos ─────────────────────────────────────────────────────────────
inc_id = 0
repo_id = 0
for r in REPOS:
    inc_id += 1
    repo_id += 1
    trit, color, name = gf3(inc_id)
    h = snap_hash(r)
    con.execute("""
        INSERT INTO world_increments VALUES (?, now(), ?, ?, ?, 'repo_snapshot', ?, 'push', ?, ?, ?)
    """, [inc_id, trit, color, name, r["org"], r["name"], r["org"], h])
    con.execute("""
        INSERT INTO repo_snapshots VALUES (?, now(), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [repo_id, inc_id, r["org"], r["name"], r["full_name"],
          r.get("language",""), r["stars"], r["forks"], r["open_issues"],
          r["pushed_at"], (r.get("description","") or "")[:100]])

# ── Aptos snapshots ───────────────────────────────────────────────────────────
APTOS_DATA = [
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
for world, addr, bal in APTOS_DATA:
    con.execute("INSERT INTO aptos_snapshots VALUES (now(), ?, ?, ?)", [world, addr, bal])

# ── Multisig probes ───────────────────────────────────────────────────────────
MULTISIG_DATA = [
    ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2,True),
    ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2,True),
    ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2,True),
    ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2,True),
    ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2,True),
]
for pair, addr, sigs, healthy in MULTISIG_DATA:
    con.execute("INSERT INTO multisig_probes VALUES (now(), ?, ?, ?, ?)", [pair, addr, sigs, healthy])

# ── MNX snapshots ─────────────────────────────────────────────────────────────
MNX_DATA = [
    ("OAI26","OpenAI Final 2026 Valuation","event_contract",531000000000.0,-0.38),
    ("ANT26","Anthropic Final 2026 Valuation","event_contract",417000000000.0,-0.71),
    ("NVDA","NVIDIA","stock",213.01,-0.69),
    ("MSFT","Microsoft","stock",448.55,5.16),
    ("INTC","Intel","stock",115.79,-4.43),
    ("TSM","Taiwan Semiconductor","stock",419.30,-1.46),
    ("MU","Micron Technology","stock",961.36,2.91),
    ("TSLA","Tesla Inc","stock",435.09,-1.42),
    ("META","Meta (Facebook)","stock",632.30,-0.20),
    ("AMZN","Amazon","stock",270.25,-0.88),
    ("AAPL","Apple","stock",310.82,-0.19),
    ("GOOGL","Alphabet (Google)","stock",380.32,-2.31),
    ("SPX","S&P 500 Index","index",7575.0,0.28),
    ("GOLD","Gold Spot","commodity",4500.0,1.02),
    ("SILVER","Silver Spot","commodity",75.38,-0.49),
    ("USO","Oil Fund","commodity",129.00,-0.79),
    ("VIX","Volatility Index","index",15.32,-2.85),
    ("DPREZ","Democrat 2028 President","event",0.50,0.80),
    ("INVADE27","Taiwan invasion before 2027","event",0.17,6.29),
]
for ticker, name, cat, price, chg in MNX_DATA:
    con.execute("INSERT INTO mnx_snapshots VALUES (now(), ?, ?, ?, ?, ?)", [ticker, name, cat, price, chg])

con.commit()

# ── Summary stats ─────────────────────────────────────────────────────────────
total_inc = con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0]
total_repos = con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0]
total_aptos = con.execute("SELECT COUNT(*) FROM aptos_snapshots").fetchone()[0]
total_msig = con.execute("SELECT COUNT(*) FROM multisig_probes").fetchone()[0]
total_mnx = con.execute("SELECT COUNT(*) FROM mnx_snapshots").fetchone()[0]

top_orgs = con.execute("""
    SELECT org_or_user, COUNT(*) as cnt, SUM(stars) as total_stars
    FROM repo_snapshots GROUP BY org_or_user ORDER BY cnt DESC
""").fetchall()

print(f"world_increments: {total_inc}")
print(f"repo_snapshots:   {total_repos}")
print(f"aptos_snapshots:  {total_aptos}")
print(f"multisig_probes:  {total_msig}")
print(f"mnx_snapshots:    {total_mnx}")
print("\nOrg/User breakdown:")
for row in top_orgs:
    print(f"  {row[0]}: {row[1]} repos, {row[2] or 0} stars")

con.close()
print("\nDone.")
