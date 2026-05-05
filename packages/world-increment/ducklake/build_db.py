#!/usr/bin/env python3
"""Build world-increments.duckdb from collected GitHub + Aptos snapshot data."""
import subprocess, textwrap, sys

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"

def q(s):
    if s is None: return "NULL"
    return "'" + str(s).replace("'", "''") + "'"

def gf3(id_):
    r = id_ % 3
    if r == 0: return (0, "#d3869b", "ERGODIC")
    if r == 1: return (1, "#b8bb26", "PLUS")
    return (-1, "#cc241d", "MINUS")

# ── sources ──────────────────────────────────────────────────────────────────
INCREMENTS = [
    # (source_type, source_name, event_type)
    ("org",  "plurigrid",     "repo_sweep"),
    ("org",  "kubeflow",      "repo_sweep"),
    ("org",  "TeglonLabs",    "repo_sweep"),
    ("user", "bmorphism",     "repo_sweep"),
    ("user", "zubyul",        "repo_sweep"),
    ("user", "migalkin",      "social_graph"),
    ("user", "DJedamski",     "social_graph"),
    ("user", "wasita",        "social_graph"),
    ("user", "kristinezheng", "social_graph"),
    ("user", "M1shaaa",       "social_graph"),
    ("user", "AustinCStone",  "social_graph"),
]

# ── repo snapshots: (org_or_user, repo_name, full_name, lang, stars, forks, issues, pushed_at, desc) ──
REPOS = [
# plurigrid (increment_id=1)
("plurigrid","zig-syrup","plurigrid/zig-syrup","Zig",2,2,0,"2026-04-30T03:52:16Z","High-performance Zig implementation of OCapN Syrup with CapTP optimizations"),
("plurigrid","asi","plurigrid/asi","HTML",18,5,4,"2026-04-26T08:51:41Z","everything is topological chemputer!"),
("plurigrid","nash-portal","plurigrid/nash-portal","Rust",2,2,0,"2026-04-26T08:50:56Z","NASH token TUI in the browser — ratzilla WASM + GeckoTerminal OHLCV candlesticks"),
("plurigrid","horse","plurigrid/horse","TeX",1,1,8,"2026-04-29T20:35:13Z",""),
("plurigrid","asi-skills","plurigrid/asi-skills","Julia",3,1,0,"2026-04-26T08:09:26Z","69 skills with Galois Hole Type accessibility (Seven Sketches §1.4.1)"),
("plurigrid","bci-blue-share","plurigrid/bci-blue-share","JavaScript",0,0,0,"2026-04-26T07:08:03Z","BCI signal infrastructure — bci.blue / bci.red / bci.horse"),
("plurigrid","nanoclj-zig","plurigrid/nanoclj-zig","Zig",1,1,20,"2026-04-25T07:29:09Z","NaN-boxed Clojure interpreter in Zig 0.15 — interaction nets, fuel-bounded eval, GF(3) trit conservation"),
("plurigrid","spi-race","plurigrid/spi-race","Swift",0,0,0,"2026-04-21T19:31:56Z","Splitmix Parallel Integrity — deterministic color generation at hardware bandwidth"),
("plurigrid","reafference","plurigrid/reafference","HTML",0,0,0,"2026-04-16T05:21:49Z","Reafference adaptation workspace"),
("plurigrid","gorj","plurigrid/gorj","Clojure",0,0,74,"2026-05-05T16:12:17Z","forj + Rama topology nREPL routing + GF(3) gay trit coloring"),
("plurigrid","web-browser","plurigrid/web-browser","Rust",0,0,0,"2026-04-10T02:54:47Z","web-browser — from prepostweb lineage"),
("plurigrid","vivarium","plurigrid/vivarium","Clojure",1,0,0,"2026-04-08T08:38:37Z",""),
("plurigrid","flowglad-rs","plurigrid/flowglad-rs","Rust",0,0,0,"2026-04-08T07:56:15Z",""),
("plurigrid","tree-sitter-nanoclj-zig","plurigrid/tree-sitter-nanoclj-zig","C",0,0,0,"2026-04-04T07:48:21Z","Tree-sitter grammar for nanoclj-zig"),
("plurigrid","forester","plurigrid/forester","XSLT",0,0,0,"2026-03-30T01:32:26Z","CatColab mathematical documentation forest"),
("plurigrid","gatomic","plurigrid/gatomic","Clojure",0,0,0,"2026-03-30T00:54:48Z","Deterministic color identity store with sonification — Gay + Datomic + Atomic"),
("plurigrid","nblm-flashcards","plurigrid/nblm-flashcards","Hy",0,0,0,"2026-03-26T08:23:01Z","NotebookLM Enterprise flashcard pipeline"),
("plurigrid","graded-optic","plurigrid/graded-optic","Haskell",0,0,0,"2026-02-08T16:10:16Z","Semiring-graded bidirectional processes"),
("plurigrid","ontology","plurigrid/ontology","JavaScript",7,9,16,"2025-05-27T18:18:34Z","autopoietic ergodicity and embodied gradualism"),
("plurigrid","Plurigraph","plurigrid/Plurigraph","JavaScript",2,5,4,"2025-01-05T08:39:09Z","Plurigrid knowledge base for use with Obsidian.md"),
("plurigrid","act","plurigrid/act","Python",3,1,4,"2024-07-26T08:27:08Z","building blocks for cognitive category theory"),
("plurigrid","StochFlow","plurigrid/StochFlow","Python",4,1,0,"2024-03-20T23:34:57Z","stochastic interpolant models and algorithms"),
("plurigrid","aptos-wallet-ruby","plurigrid/aptos-wallet-ruby","Ruby",1,0,0,"2025-09-30T22:47:22Z",""),
("plurigrid","duck-kanban","plurigrid/duck-kanban","Rust",1,0,0,"2025-09-26T20:18:38Z","Duck intelligence kanban system with kundalini computational pattern recognition"),
("plurigrid","gay-rs","plurigrid/gay-rs","Rust",0,0,0,"2026-01-08T14:19:22Z","Rust crate for Gay.jl deterministic coloring with GF(3) trits"),
("plurigrid","gay-go","plurigrid/gay-go","Go",0,0,0,"2026-01-08T14:19:23Z","Go implementation of Gay.jl deterministic coloring"),
("plurigrid","gay-terminal","plurigrid/gay-terminal","Rust",0,0,0,"2026-01-08T14:19:24Z","Terminal ANSI coloring with Gay.jl low-discrepancy sequences"),
("plurigrid","lazygay","plurigrid/lazygay","Go",0,0,0,"2026-01-08T14:19:25Z","lazygit fork with Gay.jl deterministic commit coloring"),
("plurigrid","gay-tofu","plurigrid/gay-tofu","HTML",0,0,0,"2026-01-08T15:14:34Z","Low-discrepancy color sequences for visual TOFU authentication"),
("plurigrid","lazybjj","plurigrid/lazybjj","Rust",0,0,0,"2026-01-08T14:19:19Z","TUI for jj with Gay.jl GF(3) coloring"),
# kubeflow (increment_id=2)
("kubeflow","spark-operator","kubeflow/spark-operator","Python",3123,1482,87,"2026-05-05T16:00:27Z","Kubernetes operator for managing Apache Spark applications"),
("kubeflow","sdk","kubeflow/sdk","Python",112,174,129,"2026-05-05T15:46:33Z","Universal Python SDK to run AI workloads on Kubernetes"),
("kubeflow","pipelines","kubeflow/pipelines","Python",4132,1987,488,"2026-05-05T12:59:12Z","Machine Learning Pipelines for Kubeflow"),
("kubeflow","kubeflow","kubeflow/kubeflow",None,15622,2647,0,"2026-05-05T13:57:05Z","Machine Learning Toolkit for Kubernetes"),
("kubeflow","trainer","kubeflow/trainer","Go",2096,948,127,"2026-05-05T10:43:10Z","Distributed AI Model Training and LLM Fine-Tuning on Kubernetes"),
("kubeflow","katib","kubeflow/katib","Python",1683,522,122,"2026-05-05T13:36:00Z","Automated Machine Learning on Kubernetes"),
("kubeflow","manifests","kubeflow/manifests","YAML",1015,1064,30,"2026-05-05T10:36:40Z","Kubeflow AI Reference Platform Deployment Manifests"),
("kubeflow","hub","kubeflow/hub","Go",175,178,46,"2026-05-05T13:13:50Z","Model Registry for MLOps lifecycle"),
("kubeflow","website","kubeflow/website","HTML",184,919,49,"2026-05-05T12:53:03Z","Kubeflow Website"),
("kubeflow","mpi-operator","kubeflow/mpi-operator","Go",524,235,100,"2026-05-05T04:59:32Z","Kubernetes Operator for MPI-based applications"),
("kubeflow","kale","kubeflow/kale","Python",684,156,52,"2026-05-05T17:09:13Z","Kubeflow superfood for Data Scientists"),
("kubeflow","testing","kubeflow/testing","Python",60,86,33,"2026-05-05T07:48:29Z","Test infrastructure and tooling for Kubeflow"),
("kubeflow","internal-acls","kubeflow/internal-acls","Go",18,384,2,"2026-05-05T14:47:02Z","Repository used to manage group ACLs"),
("kubeflow","arena","kubeflow/arena","Go",810,191,63,"2026-04-28T11:45:08Z","A CLI for Kubeflow"),
("kubeflow","mcp-apache-spark-history-server","kubeflow/mcp-apache-spark-history-server","Python",164,55,23,"2026-05-04T05:17:39Z","MCP Server and CLI for Apache Spark History Server"),
("kubeflow","docs-agent","kubeflow/docs-agent","Python",35,99,159,"2026-04-27T17:38:55Z","Kubeflow Documentation AI Agent"),
("kubeflow","community","kubeflow/community","Jsonnet",196,256,13,"2026-05-01T13:13:08Z","Information about the Kubeflow community"),
("kubeflow","notebooks","kubeflow/notebooks",None,71,106,196,"2026-05-01T13:59:08Z","Kubeflow Notebooks for AI/ML workloads"),
("kubeflow","dashboard","kubeflow/dashboard","TypeScript",17,55,71,"2026-04-30T16:36:08Z","Kubeflow Central Dashboard"),
("kubeflow","examples","kubeflow/examples","Jsonnet",1460,756,111,"2026-04-14T18:56:10Z","Extended examples and tutorials"),
# TeglonLabs (increment_id=3)
("TeglonLabs","mathpix-gem","TeglonLabs/mathpix-gem","Ruby",2,0,11,"2026-01-01T12:13:16Z","Transform mathematical images to LaTeX with security-first design"),
("TeglonLabs","monad-mcp-server","TeglonLabs/monad-mcp-server",None,0,0,0,"2025-05-14T17:53:01Z","Monad MCP Server"),
("TeglonLabs","topoi","TeglonLabs/topoi","Python",0,0,1,"2025-01-24T06:47:38Z",""),
("TeglonLabs","coin-flip-mcp","TeglonLabs/coin-flip-mcp","JavaScript",0,2,1,"2025-03-16T01:31:45Z","MCP server for flipping coins with varying degrees of randomness"),
# bmorphism (increment_id=4)
("bmorphism","boxxy","bmorphism/boxxy","Move",0,1,0,"2026-04-30T03:35:52Z",""),
("bmorphism","nanoclj-zig","bmorphism/nanoclj-zig","Zig",0,0,0,"2026-04-25T07:29:19Z",""),
("bmorphism","Gay.jl","bmorphism/Gay.jl","Julia",1,0,187,"2026-04-17T07:02:10Z","Wide-gamut color sampling with splittable determinism"),
("bmorphism","postweb","bmorphism/postweb","Go",0,0,0,"2026-04-09T10:52:07Z","postweb — evolved from prepostweb"),
("bmorphism","shitcoin","bmorphism/shitcoin","Python",5,0,0,"2026-04-08T08:07:17Z","gets denom for cw20 assets for permissionless degeneracy in IBC"),
("bmorphism","magic-world-org","bmorphism/magic-world-org","Python",1,0,0,"2026-05-01T01:06:25Z","Magic World Org (Local MLX)"),
("bmorphism","zig-syrup","bmorphism/zig-syrup","Zig",0,0,0,"2026-03-28T21:42:35Z","Embeddable OCapN Syrup encoder/decoder in Zig"),
("bmorphism","ocaml-mcp-sdk","bmorphism/ocaml-mcp-sdk","OCaml",60,2,0,"2026-03-28T02:37:19Z","OCaml SDK for Model Context Protocol"),
("bmorphism","flox-mcp-bb","bmorphism/flox-mcp-bb","Clojure",0,0,0,"2026-02-12T02:45:46Z","Open-source MCP server for Flox — Babashka/Clojure"),
("bmorphism","aella","bmorphism/aella","Rascal",1,0,0,"2026-04-02T17:15:48Z",""),
("bmorphism","GeoACSets.jl","bmorphism/GeoACSets.jl","Julia",0,1,1,"2026-01-19T13:55:07Z","Categorical data structures with geospatial capabilities"),
("bmorphism","anti-bullshit-mcp-server","bmorphism/anti-bullshit-mcp-server","JavaScript",23,7,1,"2026-02-05T15:46:59Z","MCP server for analyzing claims and detecting manipulation"),
("bmorphism","open-location-code-zig","bmorphism/open-location-code-zig","Zig",3,0,0,"2026-03-24T21:54:01Z","Open Location Code (Plus Codes) for Zig"),
("bmorphism","penrose-mcp","bmorphism/penrose-mcp","JavaScript",10,4,0,"2026-04-12T18:09:12Z","Penrose server for the Infinity-Topos environment"),
("bmorphism","manifold-mcp-server","bmorphism/manifold-mcp-server","JavaScript",14,9,5,"2026-04-15T19:54:28Z","MCP server for Manifold Markets prediction markets"),
("bmorphism","say-mcp-server","bmorphism/say-mcp-server","JavaScript",20,9,3,"2026-03-19T23:11:59Z","MCP server for macOS text-to-speech"),
("bmorphism","babashka-mcp-server","bmorphism/babashka-mcp-server","JavaScript",18,6,3,"2026-03-26T14:35:39Z","MCP server for interacting with Babashka"),
("bmorphism","marginalia-mcp-server","bmorphism/marginalia-mcp-server","JavaScript",8,6,0,"2026-03-27T16:55:55Z","MCP server for managing marginalia and annotations"),
("bmorphism","nats-mcp-server","bmorphism/nats-mcp-server",None,7,3,2,"2025-12-20T23:56:36Z","MCP server for NATS messaging system"),
("bmorphism","hypernym-mcp-server","bmorphism/hypernym-mcp-server","JavaScript",6,5,0,"2025-10-24T09:21:53Z",""),
("bmorphism","bafishka","bmorphism/bafishka","Clojure",1,0,0,"2025-11-01T06:36:06Z","Rust-native Fish shell-friendly file operations"),
("bmorphism","whale","bmorphism/whale","MATLAB",2,0,0,"2026-04-20T15:04:09Z","omniglot + sperm whale codas = metawhaling"),
("bmorphism","risc0-cosmwasm-example","bmorphism/risc0-cosmwasm-example","Rust",23,2,1,"2025-05-21T13:35:37Z","CosmWasm + zkVM RISC-V EFI template"),
("bmorphism","penumbra-mcp","bmorphism/penumbra-mcp","JavaScript",5,6,3,"2025-10-24T09:21:41Z","MCP server for interacting with Penumbra blockchain"),
("bmorphism","slowtime-mcp-server","bmorphism/slowtime-mcp-server","TypeScript",3,5,6,"2025-10-24T09:21:39Z","MCP server for secure time-based operations"),
("bmorphism","monero-rental-hash-war","bmorphism/monero-rental-hash-war","Haskell",1,0,0,"2025-10-24T09:25:25Z","Compositional OpenGame analysis of Monero rental hash war"),
("bmorphism","vibes","bmorphism/vibes","Clojure",0,0,0,"2024-11-13T15:56:31Z","Global Vibespace"),
("bmorphism","plurigrid-celo","bmorphism/plurigrid-celo","TypeScript",1,1,0,"2025-10-24T09:18:29Z","Celo e-app for Albany Plurigrid"),
("bmorphism","graphistry-mcp","bmorphism/graphistry-mcp","Python",2,0,0,"2025-10-24T09:22:41Z","Graphistry MCP integration for graph visualization"),
# zubyul (increment_id=5)
("zubyul","voice-observatory","zubyul/voice-observatory","Python",0,0,0,"2026-04-24T05:56:20Z","Passive macOS TUI observing voice-download pathways"),
("zubyul","ghostel-emacs-worlds","zubyul/ghostel-emacs-worlds","GLSL",0,0,0,"2026-04-24T00:21:00Z","Ghostty config + ghostel family + alice/bob emacs-mods"),
("zubyul","big-bad-plurigrid-quiz","zubyul/big-bad-plurigrid-quiz","Emacs Lisp",0,0,0,"2026-04-09T18:51:35Z","27 flashcards from recent activity + Emacs drill"),
("zubyul","Gay.jl","zubyul/Gay.jl","Julia",0,0,0,"2026-03-28T11:30:07Z","Wide-gamut color sampling with splittable determinism"),
("zubyul","kinesis-kb360pro","zubyul/kinesis-kb360pro","Python",0,0,0,"2026-03-26T10:29:44Z","Claude Code skill for Kinesis Advantage360 Pro keyboard"),
("zubyul","gay-world","zubyul/gay-world","Python",1,1,0,"2026-04-05T06:54:03Z","Goblin world builder: each goblin is a world"),
("zubyul","from-possible-worlds","zubyul/from-possible-worlds","TeX",0,0,0,"2026-03-16T03:07:20Z",""),
("zubyul","tilelang-kernels","zubyul/tilelang-kernels","Python",0,0,0,"2026-03-16T02:31:16Z","TileLang GPU kernels for SplitMix64 color generation"),
("zubyul","hue-world","zubyul/hue-world","JavaScript",0,0,0,"2025-12-12T08:32:58Z","Terminal Vibe Snipe puzzle game with ANSI true color"),
("zubyul","multiplayer-emacs","zubyul/multiplayer-emacs","HTML",0,0,0,"2025-12-12T08:07:30Z","Multiplayer world: Emacs split-pane Vibe Snipe"),
("zubyul","jonikas_lab_data_analysis_misc","zubyul/jonikas_lab_data_analysis_misc","Jupyter Notebook",2,0,0,"2026-03-26T09:05:21Z","various scripts to process large genetic sequence data"),
("zubyul","WGCNA","zubyul/WGCNA","HTML",2,0,0,"2026-03-26T09:05:26Z","weighted gene correlation network analysis project"),
("zubyul","Nikolova_lab_data_analysis","zubyul/Nikolova_lab_data_analysis","R",2,0,0,"2026-03-26T09:05:23Z","undergraduate thesis - cortical thickness to depression transcription factors"),
("zubyul","lastfm_analysis_copy","zubyul/lastfm_analysis_copy","Jupyter Notebook",1,0,0,"2026-03-26T09:05:23Z","lastfm data analysis"),
("zubyul","zubyul.github.io","zubyul/zubyul.github.io","CSS",1,0,0,"2026-03-26T09:05:35Z",""),
# migalkin (increment_id=6)
("migalkin","NodePiece","migalkin/NodePiece","Python",143,21,0,"2026-03-02T09:39:45Z","Compositional and Parameter-Efficient Representations for Large Knowledge Graphs (ICLR 22)"),
("migalkin","StarE","migalkin/StarE","Python",89,16,1,"2026-04-16T14:12:45Z","Message Passing for Hyper-Relational Knowledge Graphs (EMNLP 2020)"),
("migalkin","kgcourse2021","migalkin/kgcourse2021","HTML",25,9,0,"2026-02-16T05:16:08Z","Materials for Knowledge Graphs course"),
("migalkin","NBFNet_mlx","migalkin/NBFNet_mlx","Python",10,1,1,"2026-03-11T01:31:21Z","Neural Bellman-Ford networks in MLX for Apple Silicon"),
("migalkin","RWL","migalkin/RWL","Python",7,1,0,"2025-02-10T14:12:14Z","Weisfeiler and Leman Go Relational (LOG 2022)"),
("migalkin","rambo","migalkin/rambo","Rust",3,0,1,"2023-02-28T16:37:22Z",""),
("migalkin","migalkin.github.io","migalkin/migalkin.github.io","JavaScript",0,0,0,"2025-05-20T23:58:08Z","Personal academic website"),
# DJedamski (increment_id=7)
("DJedamski","kaggle_ncaa18","DJedamski/kaggle_ncaa18","Jupyter Notebook",0,0,0,"2018-02-26T16:33:24Z","Code for NCAA March Madness competition (2018)"),
("DJedamski","Kaggle","DJedamski/Kaggle",None,1,0,0,"2023-04-21T01:42:35Z",""),
("DJedamski","Getting-and-Cleaning-Data","DJedamski/Getting-and-Cleaning-Data","R",1,0,0,"2023-04-21T01:42:34Z","Coursera Project"),
("DJedamski","School","DJedamski/School","R",1,1,0,"2023-04-21T01:42:33Z","A couple small projects from grad school"),
("DJedamski","EDA","DJedamski/EDA","R",0,0,0,"2014-11-09T17:00:39Z","Coursera Project"),
("DJedamski","Project_Euler","DJedamski/Project_Euler",None,0,0,0,"2015-09-05T17:13:32Z",""),
# wasita (increment_id=8)
("wasita","wasita.github.io","wasita/wasita.github.io","Svelte",1,0,8,"2026-04-28T05:26:08Z","personal website"),
("wasita","magic-garden","wasita/magic-garden","Python",2,1,1,"2026-04-22T21:16:43Z","bot for auto-purchasing seeds in magic garden discord game"),
("wasita","ch3-lib","wasita/ch3-lib","Typst",0,0,0,"2026-04-12T04:03:22Z",""),
("wasita","wm-cv","wasita/wm-cv","Svelte",0,0,0,"2026-04-12T02:53:51Z","Academic CV as single page web app"),
("wasita","send2kobo","wasita/send2kobo","TypeScript",0,0,0,"2025-12-12T19:09:16Z","Website for sending books to your kobo e-reader"),
("wasita","food-diary","wasita/food-diary","Svelte",0,0,0,"2025-12-13T01:06:43Z",""),
("wasita","wins-search","wasita/wins-search","CSS",1,0,0,"2023-06-03T19:01:11Z","Women in Network Science member list website"),
("wasita","d60-keeb","wasita/d60-keeb",None,0,0,0,"2024-08-26T00:46:25Z",""),
# kristinezheng (increment_id=9)
("kristinezheng","kristinezheng.github.io","kristinezheng/kristinezheng.github.io","HTML",0,0,0,"2026-04-09T17:09:47Z",""),
("kristinezheng","lookit-jenga","kristinezheng/lookit-jenga","Jupyter Notebook",0,0,0,"2024-05-16T18:29:05Z","Lookit study for 9.85"),
("kristinezheng","Green-Machine","kristinezheng/Green-Machine","Python",0,0,0,"2021-09-19T05:33:04Z","HackMIT 2021: Sustainability Track"),
("kristinezheng","auditory-illusion","kristinezheng/auditory-illusion","CSS",0,0,0,"2022-03-07T02:57:44Z","9.35 spring 2022 auditory illusion"),
("kristinezheng","graph_example","kristinezheng/graph_example","Python",0,0,0,"2021-10-08T07:29:53Z",""),
("kristinezheng","Portfolio","kristinezheng/Portfolio",None,0,0,0,"2025-02-12T00:00:45Z","July 2021"),
# M1shaaa (increment_id=10)
("M1shaaa","M1shaaa","M1shaaa/M1shaaa",None,0,0,0,"2026-02-04T19:32:04Z","Config files for GitHub profile"),
("M1shaaa","lab-bookshelf-","M1shaaa/lab-bookshelf-","TypeScript",0,0,0,"2024-12-31T05:11:18Z",""),
("M1shaaa","Python-Lookit-Uploads","M1shaaa/Python-Lookit-Uploads","Python",0,0,0,"2024-02-15T22:59:37Z","random projects"),
("M1shaaa","MNIST-Classifier","M1shaaa/MNIST-Classifier",None,0,0,0,"2023-11-28T06:10:47Z",""),
("M1shaaa","Yale-Work","M1shaaa/Yale-Work","HTML",0,0,0,"2023-12-06T18:33:14Z",""),
# AustinCStone (increment_id=11)
("AustinCStone","TextGAN","AustinCStone/TextGAN","Python",92,30,5,"2025-03-03T13:26:32Z","A generative adversarial network for text generation in TensorFlow"),
("AustinCStone","StereoVisionMRF","AustinCStone/StereoVisionMRF","Python",11,4,0,"2026-04-01T07:39:41Z","Using a MRF with loopy belief propagation to infer depth from stereo images"),
("AustinCStone","SpectralClustering","AustinCStone/SpectralClustering","Python",3,2,0,"2021-04-16T08:46:36Z","Implementing spectral clustering"),
("AustinCStone","EpsteinSearch","AustinCStone/EpsteinSearch","Python",0,0,0,"2026-02-11T01:10:57Z",""),
("AustinCStone","bmforkupdate","AustinCStone/bmforkupdate","Python",0,0,0,"2025-05-09T04:50:16Z",""),
("AustinCStone","bmfork","AustinCStone/bmfork","Python",0,0,1,"2025-05-09T04:18:54Z",""),
("AustinCStone","stonks","AustinCStone/stonks","Python",0,0,0,"2020-09-04T22:54:35Z","Playing around with some option calculations"),
("AustinCStone","RealTimeRayTracingFractalWorld","AustinCStone/RealTimeRayTracingFractalWorld","C++",0,0,0,"2015-05-11T01:58:57Z","Real time ray tracing of a fractal world"),
("AustinCStone","logisticRegressionHaskell","AustinCStone/logisticRegressionHaskell","Haskell",1,0,0,"2018-02-02T13:34:28Z","Logistic regression in Haskell for MNIST"),
("AustinCStone","LensBuilder","AustinCStone/LensBuilder","Python",0,0,0,"2019-04-04T04:28:08Z","WIP optimize surface of a focusing lens by casting rays"),
("AustinCStone","TFBirds","AustinCStone/TFBirds","Python",0,0,0,"2019-01-30T08:07:22Z","Bird flocking simulator in TensorFlow"),
]

# ── Aptos balances ────────────────────────────────────────────────────────────
APTOS = [
    ("alice",  "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b", 0.0),
    ("bob",    "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d", 0.0),
    ("A",      "0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a", 0.0),
    ("B",      "0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13", 0.0),
    ("C",      "0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e", 0.0),
    ("D",      "0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1", 0.0),
    ("E",      "0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36", 0.0),
    ("F",      "0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71", 0.0),
    ("G",      "0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32", 0.0),
    ("H",      "0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f", 0.0),
    ("I",      "0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9", 0.0),
    ("J",      "0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54", 0.0),
    ("K",      "0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4", 0.0),
    ("L",      "0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9", 0.0),
    ("M",      "0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9", 0.0),
    ("N",      "0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c", 0.0),
    ("O",      "0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d", 0.0),
    ("P",      "0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948", 0.0),
    ("Q",      "0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9", 0.0),
    ("R",      "0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10", 0.0),
    ("S",      "0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386", 0.0),
    ("T",      "0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588", 0.0),
    ("U",      "0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956", 0.0),
    ("V",      "0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3", 0.0),
    ("W",      "0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0", 0.0),
    ("X",      "0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d", 0.0),
    ("Y",      "0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4", 0.0),
    ("Z",      "0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c", 0.0),
]

# ── multisig probes ───────────────────────────────────────────────────────────
MULTISIG = [
    ("A-B", "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2, True),
    ("A-G", "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2, True),
    ("Y-Z", "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2, True),
    ("S-T", "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2, True),
    ("V-W", "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2, True),
]

# ── build SQL ─────────────────────────────────────────────────────────────────
lines = [
"CREATE TABLE IF NOT EXISTS world_increments (",
"  id INTEGER, timestamp TIMESTAMP DEFAULT now(), gf3_trit INTEGER,",
"  gf3_color VARCHAR, gf3_name VARCHAR, source_type VARCHAR,",
"  source_name VARCHAR, event_type VARCHAR, repo_name VARCHAR,",
"  actor VARCHAR, snapshot_hash VARCHAR",
");",
"CREATE TABLE IF NOT EXISTS repo_snapshots (",
"  id INTEGER, timestamp TIMESTAMP DEFAULT now(), increment_id INTEGER,",
"  org_or_user VARCHAR, repo_name VARCHAR, full_name VARCHAR,",
"  language VARCHAR, stars INTEGER, forks INTEGER, open_issues INTEGER,",
"  pushed_at VARCHAR, description VARCHAR",
");",
"CREATE TABLE IF NOT EXISTS aptos_snapshots (",
"  timestamp TIMESTAMP DEFAULT now(),",
"  world VARCHAR, address VARCHAR, balance_apt DOUBLE",
");",
"CREATE TABLE IF NOT EXISTS multisig_probes (",
"  timestamp TIMESTAMP DEFAULT now(),",
"  pair VARCHAR, address VARCHAR, sigs_required INTEGER, healthy BOOLEAN",
");",
"CREATE TABLE IF NOT EXISTS mnx_snapshots (",
"  timestamp TIMESTAMP DEFAULT now(),",
"  ticker VARCHAR, name VARCHAR, category VARCHAR,",
"  price DOUBLE, change_pct DOUBLE",
");",
"CREATE SEQUENCE IF NOT EXISTS increment_seq START 1;",
"CREATE SEQUENCE IF NOT EXISTS repo_seq START 1;",
]

# world_increments
for i, (stype, sname, etype) in enumerate(INCREMENTS, 1):
    trit, color, name = gf3(i)
    lines.append(
        f"INSERT INTO world_increments VALUES ({i}, now(), {trit}, {q(color)}, {q(name)}, "
        f"{q(stype)}, {q(sname)}, {q(etype)}, NULL, NULL, NULL);"
    )

# repo_snapshots — assign increment_id by matching org_or_user to INCREMENTS
inc_map = {sname: i+1 for i, (_, sname, _) in enumerate(INCREMENTS)}

for rid, (ou, rname, full, lang, stars, forks, issues, pushed, desc) in enumerate(REPOS, 1):
    inc_id = inc_map.get(ou, 1)
    lines.append(
        f"INSERT INTO repo_snapshots VALUES ({rid}, now(), {inc_id}, "
        f"{q(ou)}, {q(rname)}, {q(full)}, {q(lang)}, {stars}, {forks}, {issues}, "
        f"{q(pushed)}, {q(desc)});"
    )

# aptos_snapshots
for world, addr, bal in APTOS:
    lines.append(f"INSERT INTO aptos_snapshots VALUES (now(), {q(world)}, {q(addr)}, {bal});")

# multisig_probes
for pair, addr, sigs, healthy in MULTISIG:
    lines.append(f"INSERT INTO multisig_probes VALUES (now(), {q(pair)}, {q(addr)}, {sigs}, {str(healthy).lower()});")

# MNX — SPA, no API data
lines.append("-- MNX Markets: testnet.mnx.fi is a Next.js SPA; no REST API yielded JSON market data.")

sql = "\n".join(lines)

sql_path = "/tmp/build_world_increments.sql"
with open(sql_path, "w") as f:
    f.write(sql)

print(f"SQL written ({len(lines)} statements)")

# Execute
result = subprocess.run(
    ["duckdb", DB, "-c", f".read {sql_path}"],
    capture_output=True, text=True
)
print("STDOUT:", result.stdout[:2000] if result.stdout else "(none)")
print("STDERR:", result.stderr[:2000] if result.stderr else "(none)")
print("Return code:", result.returncode)

# Verify
verify = subprocess.run(
    ["duckdb", DB, "-c",
     "SELECT 'world_increments' tbl, count(*) n FROM world_increments UNION ALL "
     "SELECT 'repo_snapshots', count(*) FROM repo_snapshots UNION ALL "
     "SELECT 'aptos_snapshots', count(*) FROM aptos_snapshots UNION ALL "
     "SELECT 'multisig_probes', count(*) FROM multisig_probes;"],
    capture_output=True, text=True
)
print("Verification:")
print(verify.stdout)
if verify.stderr:
    print("Verify STDERR:", verify.stderr[:500])
