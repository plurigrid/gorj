#!/usr/bin/env python3
"""Build world-increment DuckDB ducklake from gathered sweep data."""
import duckdb
import json
from datetime import datetime

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"

# GF(3) color chain
def gf3(id_val):
    t = id_val % 3
    if t == 0:
        return (0, "#d3869b", "ERGODIC")
    elif t == 1:
        return (1, "#b8bb26", "PLUS")
    else:
        return (-1, "#cc241d", "MINUS")

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

con.execute("CREATE SEQUENCE IF NOT EXISTS increment_seq START 1")
con.execute("CREATE SEQUENCE IF NOT EXISTS repo_seq START 1")

# All repo snapshot data
SOURCES = [
    ("org", "plurigrid", [
        {"name":"asi","full_name":"plurigrid/asi","language":"HTML","stars":30,"forks":10,"open_issues":4,"pushed_at":"2026-07-10T09:48:02Z","description":"everything is topological chemputer!"},
        {"name":"gorj","full_name":"plurigrid/gorj","language":"Clojure","stars":1,"forks":0,"open_issues":1172,"pushed_at":"2026-07-07T19:20:50Z","description":"forj + Rama topology nREPL routing + GF(3) gay trit coloring"},
        {"name":"shrimp","full_name":"plurigrid/shrimp","language":None,"stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-07-03T01:24:20Z","description":"Jank worked example: shrimp"},
        {"name":"place","full_name":"plurigrid/place","language":"TeX","stars":1,"forks":1,"open_issues":13,"pushed_at":"2026-06-27T22:03:34Z","description":None},
        {"name":"nash-portal","full_name":"plurigrid/nash-portal","language":"Rust","stars":2,"forks":3,"open_issues":1,"pushed_at":"2026-05-19T01:50:03Z","description":"NASH token TUI in the browser"},
        {"name":"zig-syrup","full_name":"plurigrid/zig-syrup","language":"Zig","stars":2,"forks":2,"open_issues":0,"pushed_at":"2026-04-30T03:52:19Z","description":"High-performance Zig OCapN Syrup"},
        {"name":"asi-skills","full_name":"plurigrid/asi-skills","language":"Julia","stars":3,"forks":0,"open_issues":0,"pushed_at":"2026-04-26T08:09:31Z","description":"69 skills with Galois Hole Type accessibility"},
        {"name":"nanoclj-zig","full_name":"plurigrid/nanoclj-zig","language":"Zig","stars":1,"forks":1,"open_issues":20,"pushed_at":"2026-04-25T07:29:13Z","description":"NaN-boxed Clojure interpreter in Zig 0.15"},
        {"name":"ontology","full_name":"plurigrid/ontology","language":"JavaScript","stars":8,"forks":9,"open_issues":16,"pushed_at":"2026-05-09T04:20:49Z","description":"autopoietic ergodicity and embodied gradualism"},
        {"name":"Plurigraph","full_name":"plurigrid/Plurigraph","language":"JavaScript","stars":3,"forks":5,"open_issues":4,"pushed_at":"2026-05-12T03:19:41Z","description":"Plurigrid knowledge base for use with Obsidian.md"},
        {"name":"vcg-auction","full_name":"plurigrid/vcg-auction","language":"Rust","stars":7,"forks":3,"open_issues":1,"pushed_at":"2025-12-16T12:32:02Z","description":"a simple contract that performs a VCG auction"},
        {"name":"agent","full_name":"plurigrid/agent","language":"Python","stars":5,"forks":1,"open_issues":6,"pushed_at":"2024-10-16T11:33:13Z","description":"Framework for agency amplification"},
        {"name":"microworlds","full_name":"plurigrid/microworlds","language":"Rust","stars":3,"forks":5,"open_issues":3,"pushed_at":"2024-03-14T00:12:46Z","description":None},
        {"name":"StochFlow","full_name":"plurigrid/StochFlow","language":"Python","stars":4,"forks":1,"open_issues":0,"pushed_at":"2024-08-15T02:58:54Z","description":"Python stochastic interpolant models"},
        {"name":"act","full_name":"plurigrid/act","language":"Python","stars":3,"forks":1,"open_issues":4,"pushed_at":"2024-11-25T09:36:59Z","description":"building blocks for cognitive category theory"},
    ]),
    ("org", "kubeflow", [
        {"name":"kubeflow","full_name":"kubeflow/kubeflow","language":None,"stars":15777,"forks":2685,"open_issues":0,"pushed_at":"2026-07-14T00:51:22Z","description":"Machine Learning Toolkit for Kubernetes"},
        {"name":"pipelines","full_name":"kubeflow/pipelines","language":"Python","stars":4166,"forks":2032,"open_issues":429,"pushed_at":"2026-07-14T16:40:51Z","description":"Machine Learning Pipelines for Kubeflow"},
        {"name":"trainer","full_name":"kubeflow/trainer","language":"Go","stars":2142,"forks":987,"open_issues":128,"pushed_at":"2026-07-14T21:48:09Z","description":"Distributed AI Model Training and LLM Fine-Tuning"},
        {"name":"spark-operator","full_name":"kubeflow/spark-operator","language":"Python","stars":3136,"forks":1500,"open_issues":109,"pushed_at":"2026-07-14T11:57:56Z","description":"Kubernetes operator for Apache Spark"},
        {"name":"katib","full_name":"kubeflow/katib","language":"Python","stars":1690,"forks":533,"open_issues":106,"pushed_at":"2026-07-11T16:05:34Z","description":"Automated Machine Learning on Kubernetes"},
        {"name":"arena","full_name":"kubeflow/arena","language":"Go","stars":815,"forks":195,"open_issues":56,"pushed_at":"2026-07-14T11:33:40Z","description":"A CLI for Kubeflow"},
        {"name":"kale","full_name":"kubeflow/kale","language":"Python","stars":695,"forks":157,"open_issues":43,"pushed_at":"2026-07-13T15:58:26Z","description":"Kubeflow's superfood for Data Scientists"},
        {"name":"hub","full_name":"kubeflow/hub","language":"Go","stars":177,"forks":188,"open_issues":28,"pushed_at":"2026-07-14T19:44:48Z","description":"Model Registry"},
        {"name":"sdk","full_name":"kubeflow/sdk","language":"Python","stars":124,"forks":196,"open_issues":155,"pushed_at":"2026-07-14T10:02:42Z","description":"Universal Python SDK to run AI workloads on Kubernetes"},
        {"name":"mcp-server","full_name":"kubeflow/mcp-server","language":"Python","stars":26,"forks":31,"open_issues":47,"pushed_at":"2026-07-13T15:45:00Z","description":"MCP Server for AI-Assisted Development with Kubeflow Tools"},
        {"name":"mcp-apache-spark-history-server","full_name":"kubeflow/mcp-apache-spark-history-server","language":"Python","stars":182,"forks":65,"open_issues":19,"pushed_at":"2026-07-07T06:27:43Z","description":"MCP Server and CLI for Apache Spark History Server"},
        {"name":"docs-agent","full_name":"kubeflow/docs-agent","language":"Python","stars":39,"forks":98,"open_issues":158,"pushed_at":"2026-07-11T16:56:53Z","description":"Kubeflow Documentation AI Agent"},
        {"name":"notebooks","full_name":"kubeflow/notebooks","language":None,"stars":73,"forks":129,"open_issues":176,"pushed_at":"2026-07-13T12:49:54Z","description":"Kubeflow Notebooks"},
        {"name":"community-distribution","full_name":"kubeflow/community-distribution","language":"YAML","stars":1029,"forks":1071,"open_issues":26,"pushed_at":"2026-07-13T15:42:00Z","description":"Kubeflow Community Distribution"},
        {"name":"dashboard","full_name":"kubeflow/dashboard","language":"TypeScript","stars":16,"forks":60,"open_issues":89,"pushed_at":"2026-07-07T14:44:56Z","description":"Kubeflow Central Dashboard"},
    ]),
    ("org", "TeglonLabs", [
        {"name":"jank-crane","full_name":"TeglonLabs/jank-crane","language":"C++","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-06-08T19:03:37Z","description":"crane-jank converged-IR hub"},
        {"name":"mathpix-gem","full_name":"TeglonLabs/mathpix-gem","language":"Ruby","stars":2,"forks":0,"open_issues":11,"pushed_at":"2026-01-01T12:13:16Z","description":"Transform mathematical images to LaTeX"},
        {"name":"coin-flip-mcp","full_name":"TeglonLabs/coin-flip-mcp","language":"JavaScript","stars":0,"forks":2,"open_issues":1,"pushed_at":"2025-03-16T01:31:45Z","description":"MCP server for flipping coins"},
        {"name":"monad-mcp-server","full_name":"TeglonLabs/monad-mcp-server","language":None,"stars":0,"forks":0,"open_issues":0,"pushed_at":"2025-05-14T17:53:01Z","description":"Monad MCP Server"},
        {"name":"topoi","full_name":"TeglonLabs/topoi","language":"Python","stars":0,"forks":0,"open_issues":1,"pushed_at":"2025-01-24T06:47:38Z","description":None},
    ]),
    ("user", "bmorphism", [
        {"name":"gay-chat","full_name":"bmorphism/gay-chat","language":"Scheme","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-07-14T21:00:00Z","description":"gay://chat operationalization over Spritely Brassica Chat"},
        {"name":"Gay.jl","full_name":"bmorphism/Gay.jl","language":"Julia","stars":2,"forks":1,"open_issues":187,"pushed_at":"2026-07-14T08:57:38Z","description":"Wide-gamut color sampling with splittable determinism"},
        {"name":"anti-bullshit-mcp-server","full_name":"bmorphism/anti-bullshit-mcp-server","language":"JavaScript","stars":22,"forks":7,"open_issues":1,"pushed_at":"2026-07-12T19:31:54Z","description":"MCP server for analyzing claims and detecting manipulation"},
        {"name":"penrose-mcp","full_name":"bmorphism/penrose-mcp","language":"JavaScript","stars":9,"forks":4,"open_issues":0,"pushed_at":"2026-06-24T15:36:16Z","description":"Penrose server for the Infinity-Topos environment"},
        {"name":"flox-mcp-bb","full_name":"bmorphism/flox-mcp-bb","language":"Clojure","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-06-05T17:53:47Z","description":"Open-source MCP server for Flox"},
        {"name":"ocaml-mcp-sdk","full_name":"bmorphism/ocaml-mcp-sdk","language":"OCaml","stars":61,"forks":2,"open_issues":0,"pushed_at":"2026-05-08T16:50:34Z","description":"OCaml SDK for Model Context Protocol"},
        {"name":"babashka-mcp-server","full_name":"bmorphism/babashka-mcp-server","language":"JavaScript","stars":19,"forks":6,"open_issues":3,"pushed_at":"2026-06-05T13:16:11Z","description":"MCP server for Babashka"},
        {"name":"say-mcp-server","full_name":"bmorphism/say-mcp-server","language":"JavaScript","stars":20,"forks":9,"open_issues":3,"pushed_at":"2026-03-19T23:11:59Z","description":"MCP server for macOS text-to-speech"},
        {"name":"manifold-mcp-server","full_name":"bmorphism/manifold-mcp-server","language":"JavaScript","stars":14,"forks":9,"open_issues":5,"pushed_at":"2026-04-15T19:54:28Z","description":"MCP server for Manifold Markets prediction markets"},
        {"name":"marginalia-mcp-server","full_name":"bmorphism/marginalia-mcp-server","language":"JavaScript","stars":8,"forks":6,"open_issues":0,"pushed_at":"2026-03-27T16:55:55Z","description":"MCP server for managing marginalia and annotations"},
        {"name":"hypernym-mcp-server","full_name":"bmorphism/hypernym-mcp-server","language":"JavaScript","stars":6,"forks":5,"open_issues":0,"pushed_at":"2025-10-24T09:21:53Z","description":None},
        {"name":"risc0-cosmwasm-example","full_name":"bmorphism/risc0-cosmwasm-example","language":"Rust","stars":23,"forks":2,"open_issues":1,"pushed_at":"2025-05-21T13:35:37Z","description":"CosmWasm + zkVM RISC-V EFI template"},
        {"name":"whale","full_name":"bmorphism/whale","language":"MATLAB","stars":2,"forks":0,"open_issues":0,"pushed_at":"2026-04-20T15:04:09Z","description":"omniglot + sperm whale codas = metawhaling"},
        {"name":"shitcoin","full_name":"bmorphism/shitcoin","language":"Python","stars":5,"forks":0,"open_issues":0,"pushed_at":"2026-04-08T08:07:17Z","description":"gets denom for cw20 assets"},
        {"name":"satreadout","full_name":"bmorphism/satreadout","language":"HTML","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-06-20T13:05:44Z","description":"Machine-checked saturating non-Riemannian perceptual readout"},
    ]),
    ("user", "zubyul", [
        {"name":"voice-observatory","full_name":"zubyul/voice-observatory","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-24T05:56:20Z","description":"Passive macOS TUI observing voice-download pathways"},
        {"name":"ghostel-emacs-worlds","full_name":"zubyul/ghostel-emacs-worlds","language":"GLSL","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-24T00:21:00Z","description":"Ghostty config + ghostel family + alice/bob emacs-mods"},
        {"name":"big-bad-plurigrid-quiz","full_name":"zubyul/big-bad-plurigrid-quiz","language":"Emacs Lisp","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-09T18:51:35Z","description":"27 flashcards from bmorphism/plurigrid/zubyul recent activity"},
        {"name":"Gay.jl","full_name":"zubyul/Gay.jl","language":"Julia","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-03-28T11:30:07Z","description":"Wide-gamut color sampling with splittable determinism"},
        {"name":"kinesis-kb360pro","full_name":"zubyul/kinesis-kb360pro","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-03-26T10:29:44Z","description":"Claude Code skill for Kinesis Advantage360 Pro keyboard"},
        {"name":"gay-world","full_name":"zubyul/gay-world","language":"Python","stars":1,"forks":1,"open_issues":0,"pushed_at":"2026-04-05T06:54:03Z","description":"Goblin world builder"},
        {"name":"tilelang-kernels","full_name":"zubyul/tilelang-kernels","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-03-16T02:31:16Z","description":"TileLang GPU kernels for SplitMix64 color generation"},
        {"name":"hue-world","full_name":"zubyul/hue-world","language":"JavaScript","stars":0,"forks":0,"open_issues":0,"pushed_at":"2025-12-12T08:32:58Z","description":"Terminal Vibe Snipe puzzle game with ANSI true color"},
        {"name":"jonikas_lab_data_analysis_misc","full_name":"zubyul/jonikas_lab_data_analysis_misc","language":"Jupyter Notebook","stars":2,"forks":0,"open_issues":0,"pushed_at":"2026-03-26T09:05:21Z","description":"various scripts used to process large genetic sequence data"},
        {"name":"Nikolova_lab_data_analysis","full_name":"zubyul/Nikolova_lab_data_analysis","language":"R","stars":2,"forks":0,"open_issues":0,"pushed_at":"2026-03-26T09:05:23Z","description":"undergraduate thesis - cortical thickness study"},
    ]),
    ("user", "migalkin", [
        {"name":"NodePiece","full_name":"migalkin/NodePiece","language":"Python","stars":144,"forks":21,"open_issues":0,"pushed_at":"2026-05-07T05:40:02Z","description":"Compositional and Parameter-Efficient Representations for Large Knowledge Graphs (ICLR 22)"},
        {"name":"StarE","full_name":"migalkin/StarE","language":"Python","stars":89,"forks":16,"open_issues":1,"pushed_at":"2026-04-16T14:12:45Z","description":"EMNLP 2020: Message Passing for Hyper-Relational Knowledge Graphs"},
        {"name":"NBFNet_mlx","full_name":"migalkin/NBFNet_mlx","language":"Python","stars":10,"forks":1,"open_issues":1,"pushed_at":"2026-03-11T01:31:21Z","description":"Neural Bellman-Ford networks in MLX for Apple Silicon"},
        {"name":"kgcourse2021","full_name":"migalkin/kgcourse2021","language":"HTML","stars":24,"forks":8,"open_issues":0,"pushed_at":"2026-07-10T15:40:00Z","description":"Materials for Knowledge Graphs course"},
        {"name":"RWL","full_name":"migalkin/RWL","language":"Python","stars":8,"forks":1,"open_issues":0,"pushed_at":"2026-05-28T20:19:20Z","description":"Weisfeiler and Leman Go Relational (LOG 2022)"},
    ]),
    ("user", "DJedamski", [
        {"name":"kaggle_ncaa18","full_name":"DJedamski/kaggle_ncaa18","language":"Jupyter Notebook","stars":0,"forks":0,"open_issues":0,"pushed_at":"2018-02-26T16:33:24Z","description":"Code for NCAA March Madness competition"},
        {"name":"Kaggle","full_name":"DJedamski/Kaggle","language":None,"stars":1,"forks":0,"open_issues":0,"pushed_at":"2023-04-21T01:42:35Z","description":None},
        {"name":"Getting-and-Cleaning-Data","full_name":"DJedamski/Getting-and-Cleaning-Data","language":"R","stars":1,"forks":0,"open_issues":0,"pushed_at":"2023-04-21T01:42:34Z","description":"Coursera Project"},
        {"name":"School","full_name":"DJedamski/School","language":"R","stars":1,"forks":1,"open_issues":0,"pushed_at":"2023-04-21T01:42:33Z","description":"Projects from grad school"},
    ]),
    ("user", "wasita", [
        {"name":"wasita.github.io","full_name":"wasita/wasita.github.io","language":"Svelte","stars":1,"forks":0,"open_issues":8,"pushed_at":"2026-07-14T17:55:08Z","description":"personal website"},
        {"name":"wm-cv","full_name":"wasita/wm-cv","language":"Svelte","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-07-14T03:53:19Z","description":"Academic CV as a single page web app"},
        {"name":"magic-garden","full_name":"wasita/magic-garden","language":"Python","stars":2,"forks":1,"open_issues":1,"pushed_at":"2026-04-22T21:16:43Z","description":"a bot for the magic garden discord activity game"},
        {"name":"send2kobo","full_name":"wasita/send2kobo","language":"TypeScript","stars":1,"forks":0,"open_issues":0,"pushed_at":"2026-05-19T02:59:26Z","description":"Website for sending books to your kobo e-reader"},
        {"name":"proj-template","full_name":"wasita/proj-template","language":None,"stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-06-19T21:22:21Z","description":None},
    ]),
    ("user", "kristinezheng", [
        {"name":"kristinezheng.github.io","full_name":"kristinezheng/kristinezheng.github.io","language":"HTML","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-07-01T20:57:48Z","description":None},
        {"name":"lookit-jenga","full_name":"kristinezheng/lookit-jenga","language":"Jupyter Notebook","stars":0,"forks":0,"open_issues":0,"pushed_at":"2024-05-16T18:29:05Z","description":"Lookit study for 9.85"},
        {"name":"Green-Machine","full_name":"kristinezheng/Green-Machine","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2021-09-19T05:33:04Z","description":"HackMIT 2021: Sustainability Track"},
    ]),
    ("user", "M1shaaa", [
        {"name":"M1shaaa","full_name":"M1shaaa/M1shaaa","language":None,"stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-02-04T19:32:04Z","description":"Config files for my GitHub profile"},
        {"name":"lab-bookshelf-","full_name":"M1shaaa/lab-bookshelf-","language":"TypeScript","stars":0,"forks":0,"open_issues":0,"pushed_at":"2024-12-31T05:11:18Z","description":None},
        {"name":"Python-Lookit-Uploads","full_name":"M1shaaa/Python-Lookit-Uploads","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2024-02-15T22:59:37Z","description":"random projects"},
    ]),
    ("user", "AustinCStone", [
        {"name":"EpsteinSearch","full_name":"AustinCStone/EpsteinSearch","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-02-11T01:10:57Z","description":None},
        {"name":"TextGAN","full_name":"AustinCStone/TextGAN","language":"Python","stars":92,"forks":30,"open_issues":5,"pushed_at":"2025-03-03T13:26:32Z","description":"A generative adversarial network for text generation in TensorFlow"},
        {"name":"StereoVisionMRF","full_name":"AustinCStone/StereoVisionMRF","language":"Python","stars":11,"forks":4,"open_issues":0,"pushed_at":"2026-04-01T07:39:41Z","description":"Using MRF with loopy belief propagation for stereo vision"},
        {"name":"bmfork","full_name":"AustinCStone/bmfork","language":"Python","stars":0,"forks":0,"open_issues":1,"pushed_at":"2025-05-09T04:18:54Z","description":"forked on jan 8 2025"},
    ]),
]

# Aptos wallet data (all null due to resource_not_found)
APTOS_WALLETS = [
    ("alice", "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b", None),
    ("bob", "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d", None),
    ("A", "0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a", None),
    ("B", "0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13", None),
    ("C", "0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e", None),
    ("D", "0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1", None),
    ("E", "0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36", None),
    ("F", "0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71", None),
    ("G", "0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32", None),
    ("H", "0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f", None),
    ("I", "0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9", None),
    ("J", "0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54", None),
    ("K", "0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4", None),
    ("L", "0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9", None),
    ("M", "0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9", None),
    ("N", "0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c", None),
    ("O", "0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d", None),
    ("P", "0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948", None),
    ("Q", "0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9", None),
    ("R", "0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10", None),
    ("S", "0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386", None),
    ("T", "0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588", None),
    ("U", "0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956", None),
    ("V", "0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3", None),
    ("W", "0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0", None),
    ("X", "0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d", None),
    ("Y", "0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4", None),
    ("Z", "0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c", None),
]

MULTISIG_PROBES = [
    ("A-B", "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2),
    ("A-G", "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2),
    ("Y-Z", "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2),
    ("S-T", "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2),
    ("V-W", "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2),
]

NOW = datetime.utcnow().isoformat()
inc_id = 1
repo_id = 1

for source_type, source_name, repos in SOURCES:
    trit, color, name = gf3(inc_id)
    snapshot_hash = f"sweep-{source_name}-{NOW[:10]}"
    con.execute("""
        INSERT INTO world_increments VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [inc_id, NOW, trit, color, name, source_type, source_name, "repo_snapshot", None, None, snapshot_hash])

    for repo in repos:
        con.execute("""
            INSERT INTO repo_snapshots VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, [
            repo_id, NOW, inc_id, source_name,
            repo["name"], repo["full_name"],
            repo.get("language"), repo.get("stars", 0), repo.get("forks", 0),
            repo.get("open_issues", 0), repo.get("pushed_at"), repo.get("description")
        ])
        repo_id += 1
    inc_id += 1

# Insert Aptos snapshots
for world, address, balance in APTOS_WALLETS:
    con.execute("INSERT INTO aptos_snapshots VALUES (?, ?, ?, ?)", [NOW, world, address, balance])

# Insert multisig probes
for pair, address, sigs in MULTISIG_PROBES:
    healthy = sigs is not None and sigs > 0
    con.execute("INSERT INTO multisig_probes VALUES (?, ?, ?, ?, ?)", [NOW, pair, address, sigs, healthy])

# MNX unavailable (Vercel auth protected)
# No rows inserted for mnx_snapshots

# Summary queries
print("=== WORLD INCREMENTS ===")
print(con.execute("SELECT id, gf3_name, gf3_color, source_type, source_name FROM world_increments ORDER BY id").fetchdf().to_string())

print("\n=== REPO SNAPSHOT COUNTS ===")
print(con.execute("SELECT org_or_user, COUNT(*) as repos FROM repo_snapshots GROUP BY org_or_user ORDER BY repos DESC").fetchdf().to_string())

print("\n=== APTOS WALLETS (all null - CoinStore not initialized) ===")
print(con.execute("SELECT world, address, balance_apt FROM aptos_snapshots ORDER BY world").fetchdf().to_string())

print("\n=== MULTISIG PROBES ===")
print(con.execute("SELECT pair, address, sigs_required, healthy FROM multisig_probes").fetchdf().to_string())

con.close()
print("\nDuckDB built successfully at:", DB_PATH)
