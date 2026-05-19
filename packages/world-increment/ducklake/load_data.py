#!/usr/bin/env python3
import duckdb, hashlib, datetime

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
con = duckdb.connect(DB)

con.execute("""CREATE TABLE IF NOT EXISTS world_increments (
  id INTEGER, timestamp TIMESTAMP DEFAULT now(), gf3_trit INTEGER,
  gf3_color VARCHAR, gf3_name VARCHAR, source_type VARCHAR,
  source_name VARCHAR, event_type VARCHAR, repo_name VARCHAR,
  actor VARCHAR, snapshot_hash VARCHAR)""")
con.execute("""CREATE TABLE IF NOT EXISTS repo_snapshots (
  id INTEGER, timestamp TIMESTAMP DEFAULT now(), increment_id INTEGER,
  org_or_user VARCHAR, repo_name VARCHAR, full_name VARCHAR,
  language VARCHAR, stars INTEGER, forks INTEGER, open_issues INTEGER,
  pushed_at VARCHAR, description VARCHAR)""")
con.execute("""CREATE TABLE IF NOT EXISTS aptos_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  world VARCHAR, address VARCHAR, balance_apt DOUBLE)""")
con.execute("""CREATE TABLE IF NOT EXISTS multisig_probes (
  timestamp TIMESTAMP DEFAULT now(),
  pair VARCHAR, address VARCHAR, sigs_required INTEGER, healthy BOOLEAN)""")
con.execute("""CREATE TABLE IF NOT EXISTS mnx_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  ticker VARCHAR, name VARCHAR, category VARCHAR,
  price DOUBLE, change_pct DOUBLE)""")

GF3 = {0: (0, "#d3869b", "ERGODIC"), 1: (1, "#b8bb26", "PLUS"), 2: (-1, "#cc241d", "MINUS")}

# ── repo data from all sources ──────────────────────────────────────────────
repos = [
# plurigrid (100 repos)
("plurigrid","plurigrid/gorj","Clojure",0,0,250,"2026-05-19T00:16:50Z","forj + Rama topology nREPL routing + GF(3) gay trit coloring"),
("plurigrid","plurigrid/horse","TeX",1,1,9,"2026-05-07T04:35:12Z",""),
("plurigrid","plurigrid/zig-syrup","Zig",2,2,0,"2026-04-30T03:52:16Z","High-performance Zig implementation of OCapN Syrup"),
("plurigrid","plurigrid/asi","HTML",23,5,4,"2026-04-26T08:51:41Z","everything is topological chemputer!"),
("plurigrid","plurigrid/nash-portal","Rust",2,3,2,"2026-04-26T08:50:56Z","NASH token TUI in the browser"),
("plurigrid","plurigrid/asi-skills","Julia",3,1,0,"2026-04-26T08:09:26Z","69 skills with Galois Hole Type accessibility"),
("plurigrid","plurigrid/bci-blue-share","JavaScript",0,0,0,"2026-04-26T07:08:03Z","BCI signal infrastructure"),
("plurigrid","plurigrid/nanoclj-zig","Zig",1,2,20,"2026-04-25T07:29:09Z","NaN-boxed Clojure interpreter in Zig 0.15"),
("plurigrid","plurigrid/spi-race","Swift",0,0,0,"2026-04-21T19:31:56Z","Splitmix Parallel Integrity"),
("plurigrid","plurigrid/reafference","HTML",0,0,0,"2026-04-16T05:21:49Z","Reafference adaptation workspace"),
("plurigrid","plurigrid/web-browser","Rust",0,0,0,"2026-04-10T02:54:47Z","web-browser from prepostweb lineage"),
("plurigrid","plurigrid/vivarium","Clojure",1,0,0,"2026-04-08T08:38:37Z",""),
("plurigrid","plurigrid/flowglad-rs","Rust",0,0,0,"2026-04-08T07:56:15Z",""),
("plurigrid","plurigrid/tree-sitter-nanoclj-zig","C",0,0,0,"2026-04-04T07:48:21Z","Tree-sitter grammar for nanoclj-zig"),
("plurigrid","plurigrid/forester","XSLT",0,0,0,"2026-03-30T01:32:26Z","CatColab mathematical documentation forest"),
("plurigrid","plurigrid/gatomic","Clojure",0,0,0,"2026-03-30T00:54:48Z","Deterministic color identity store"),
("plurigrid","plurigrid/blue","TeX",0,0,0,"2026-03-29T23:06:32Z",""),
("plurigrid","plurigrid/red","",0,0,0,"2026-03-29T22:58:46Z",""),
("plurigrid","plurigrid/nblm-flashcards","Hy",0,0,0,"2026-03-26T08:23:01Z","NotebookLM Enterprise flashcard pipeline"),
("plurigrid","plurigrid/gemini-agent","Python",0,0,0,"2026-02-19T06:39:16Z",""),
("plurigrid","plurigrid/graded-optic","Haskell",0,0,0,"2026-02-08T16:10:16Z","Semiring-graded bidirectional processes"),
("plurigrid","plurigrid/json-canvas","",0,0,0,"2026-02-06T06:50:57Z","JSON Canvas: Real-time interaction data capture"),
("plurigrid","plurigrid/shepherd","Scheme",0,0,0,"2026-01-23T07:47:28Z","Spritely Shepherd - Service manager"),
("plurigrid","plurigrid/goblinshare","Scheme",0,0,0,"2026-01-23T07:47:12Z","P2P filesharing demo for Goblins"),
("plurigrid","plurigrid/magenc","Scheme",0,0,0,"2026-01-23T07:47:11Z","Magenc Magnet URIs"),
("plurigrid","plurigrid/hoot","Scheme",0,0,1,"2026-01-23T07:47:10Z","Spritely Hoot - Scheme to WebAssembly compiler"),
("plurigrid","plurigrid/leprechauns","Racket",0,0,0,"2026-01-23T07:46:46Z","Spritely Goblins + Gay.jl semantic colors"),
("plurigrid","plurigrid/spritely-semantic-colors","",0,0,0,"2026-01-23T07:38:32Z","Deterministic color mappings for Spritely"),
("plurigrid","plurigrid/gay-tofu","HTML",0,0,0,"2026-01-08T15:14:34Z","Low-discrepancy color sequences for visual TOFU"),
("plurigrid","plurigrid/lazygay","Go",0,0,0,"2026-01-08T14:19:25Z","lazygit fork with Gay.jl deterministic commit coloring"),
("plurigrid","plurigrid/gay-terminal","Rust",0,0,0,"2026-01-08T14:19:24Z","Terminal ANSI coloring with Gay.jl"),
("plurigrid","plurigrid/gay-go","Go",0,0,0,"2026-01-08T14:19:23Z","Go implementation of Gay.jl"),
("plurigrid","plurigrid/gay-rs","Rust",0,0,0,"2026-01-08T14:19:22Z","Rust crate for Gay.jl deterministic coloring"),
("plurigrid","plurigrid/lazybjj","Rust",0,0,0,"2026-01-08T14:19:19Z","TUI for jj with Gay.jl GF(3) coloring"),
("plurigrid","plurigrid/agent-o-rama","Clojure",0,0,0,"2026-01-02T01:09:22Z",""),
("plurigrid","plurigrid/aptos-wallet-ruby","Ruby",1,0,0,"2025-09-30T22:47:22Z",""),
("plurigrid","plurigrid/duck-kanban","Rust",1,0,0,"2025-09-26T20:18:38Z","Duck intelligence kanban system"),
("plurigrid","plurigrid/discohy","Hy",0,0,0,"2025-09-10T02:01:31Z",""),
("plurigrid","plurigrid/ontology","JavaScript",8,9,16,"2025-05-27T18:18:34Z","autopoietic ergodicity and embodied gradualism"),
("plurigrid","plurigrid/Plurigraph","JavaScript",3,5,4,"2025-01-05T08:39:09Z","Plurigrid knowledge base for Obsidian.md"),
("plurigrid","plurigrid/act","Python",3,1,4,"2024-07-26T08:27:08Z","building blocks for cognitive category theory"),
("plurigrid","plurigrid/StochFlow","Python",4,1,0,"2024-03-20T23:34:57Z","stochastic interpolant models"),
("plurigrid","plurigrid/microworlds","Rust",3,5,3,"2023-05-13T03:54:56Z",""),
("plurigrid","plurigrid/agent","Python",5,1,6,"2023-03-31T18:45:23Z","Framework for agency amplification"),
("plurigrid","plurigrid/vcg-auction","Rust",7,2,1,"2023-03-16T21:53:08Z","a simple contract that performs a VCG auction"),
# kubeflow (48 repos)
("kubeflow","kubeflow/kubeflow","",15647,2648,2,"2026-05-07T13:46:41Z","Machine Learning Toolkit for Kubernetes"),
("kubeflow","kubeflow/pipelines","Python",4140,1993,470,"2026-05-18T19:16:44Z","Machine Learning Pipelines for Kubeflow"),
("kubeflow","kubeflow/spark-operator","Python",3126,1482,86,"2026-05-19T00:16:25Z","Kubernetes operator for Apache Spark"),
("kubeflow","kubeflow/trainer","Go",2100,951,101,"2026-05-18T21:15:02Z","Distributed AI Model Training"),
("kubeflow","kubeflow/katib","Python",1682,522,124,"2026-05-09T12:21:57Z","Automated Machine Learning on Kubernetes"),
("kubeflow","kubeflow/examples","Jsonnet",1463,756,111,"2025-04-14T01:54:52Z","Extended examples and tutorials"),
("kubeflow","kubeflow/manifests","YAML",1017,1064,27,"2026-05-16T16:37:54Z","Kubeflow AI Reference Platform Deployment Manifests"),
("kubeflow","kubeflow/arena","Go",810,190,57,"2026-05-07T06:46:17Z","A CLI for Kubeflow"),
("kubeflow","kubeflow/kale","Python",687,156,54,"2026-05-18T19:17:55Z","Kubeflow's superfood for Data Scientists"),
("kubeflow","kubeflow/mpi-operator","Go",527,235,102,"2026-05-18T22:43:45Z","Kubernetes Operator for MPI-based applications"),
("kubeflow","kubeflow/pytorch-operator","Jsonnet",310,143,63,"2021-12-01T17:44:48Z","PyTorch on Kubernetes"),
("kubeflow","kubeflow/fairing","Jsonnet",337,143,134,"2022-04-11T05:28:47Z","Python SDK for building, training, deploying ML models"),
("kubeflow","kubeflow/hub","Go",175,178,49,"2026-05-18T22:58:59Z","Model Registry for ML model developers"),
("kubeflow","kubeflow/mcp-apache-spark-history-server","Python",170,60,22,"2026-05-18T22:08:06Z","MCP Server and CLI for Apache Spark History Server"),
("kubeflow","kubeflow/kfp-tekton","TypeScript",182,123,79,"2024-11-19T12:23:51Z","Kubeflow Pipelines on Tekton"),
("kubeflow","kubeflow/kfctl","Go",182,134,94,"2023-08-15T20:19:22Z","kfctl CLI for deploying Kubeflow"),
("kubeflow","kubeflow/community","Jupyter Notebook",196,257,13,"2026-05-18T17:12:00Z","Kubeflow community information"),
("kubeflow","kubeflow/website","HTML",184,920,52,"2026-05-14T17:20:09Z","Kubeflow Website"),
("kubeflow","kubeflow","kubeflow/metadata","TypeScript",123,63,38,"2021-12-01T17:35:27Z","Repository for assets related to Metadata"),
("kubeflow","kubeflow/sdk","Python",118,174,131,"2026-05-18T19:07:21Z","Universal Python SDK to run AI workloads"),
("kubeflow","kubeflow/notebooks","",72,110,187,"2026-05-19T00:32:23Z","Kubeflow Notebooks for interactive dev environments"),
("kubeflow","kubeflow/xgboost-operator","Python",77,53,22,"2021-12-01T18:00:10Z","Incubating project for xgboost operator"),
("kubeflow","kubeflow/kubebench","Jsonnet",78,35,68,"2024-06-17T19:22:04Z","Repository for benchmarking"),
("kubeflow","kubeflow/docs-agent","Python",36,98,153,"2026-04-14T03:33:15Z","Kubeflow Documentation AI Agent"),
("kubeflow","kubeflow/blog","Jupyter Notebook",32,62,27,"2026-05-11T15:21:33Z","Kubeflow blog based on fastpages"),
# TeglonLabs (4 repos)
("TeglonLabs","TeglonLabs/mathpix-gem","Ruby",2,0,11,"2026-01-01T12:13:13Z","Transform mathematical images to LaTeX"),
("TeglonLabs","TeglonLabs/coin-flip-mcp","JavaScript",0,2,1,"2025-09-21T08:57:27Z","MCP server for flipping coins with random.org"),
("TeglonLabs","TeglonLabs/monad-mcp-server","",0,0,0,"2025-05-14T11:36:14Z","Monad MCP Server"),
("TeglonLabs","TeglonLabs/topoi","Python",0,0,1,"2025-01-24T04:49:26Z",""),
# bmorphism (117 repos - key ones)
("bmorphism","bmorphism/Gay.jl","Julia",0,0,189,"2026-05-19T00:37:58Z","Wide-gamut color sampling with splittable determinism"),
("bmorphism","bmorphism/oxgame","OCaml",0,0,0,"2026-05-15T09:53:27Z","Stellar resolution and open-game composition for OCaml"),
("bmorphism","bmorphism/nanoclj-zig","Zig",0,0,0,"2026-05-07T20:12:15Z",""),
("bmorphism","bmorphism/zig-syrup","Zig",0,0,0,"2026-05-07T19:49:05Z","Embeddable OCapN Syrup encoder/decoder in Zig"),
("bmorphism","bmorphism/postweb","Go",0,0,0,"2026-04-09T10:51:57Z","postweb evolved from prepostweb"),
("bmorphism","bmorphism/magic-world-org","Python",0,0,0,"2026-04-05T07:03:50Z","Magic World Org (Local MLX)"),
("bmorphism","bmorphism/ocaml-mcp-sdk","OCaml",0,0,0,"2026-03-16T05:24:25Z","OCaml SDK for Model Context Protocol"),
("bmorphism","bmorphism/flox-mcp-bb","Clojure",0,0,0,"2026-02-12T02:45:43Z","Open-source MCP server for Flox"),
("bmorphism","bmorphism/vibesnipe-market","Move",0,0,9,"2026-02-05T10:23:25Z",""),
("bmorphism","bmorphism/vibespace-mcp-go-ternary","HTML",0,0,3,"2026-01-11T12:50:40Z","Go MCP experience for vibes and worlds with NATS"),
("bmorphism","bmorphism/anti-bullshit-mcp-server","JavaScript",0,0,1,"2026-01-16T08:54:58Z","MCP server for analyzing claims"),
("bmorphism","bmorphism/open-location-code-zig","Zig",0,0,0,"2025-12-30T19:33:45Z","Open Location Code for Zig"),
("bmorphism","bmorphism/gay-hy","Hy",0,0,0,"2025-12-15T15:32:58Z","Hylang MLX color bandwidth protocol"),
("bmorphism","bmorphism/signal-mcp","Rust",0,0,0,"2025-12-11T07:20:08Z","O(n)→O(1) chromatic mode collapse via Galois connection"),
("bmorphism","bmorphism/multiverse-color-game","Julia",0,0,0,"2025-12-12T05:28:11Z","2+1D Holographic Color Matching Game"),
("bmorphism","bmorphism/monero-rental-hash-war","Haskell",0,0,0,"2025-10-05T23:08:54Z","Compositional OpenGame analysis of Monero"),
("bmorphism","bmorphism/manifold-mcp-server","JavaScript",0,0,5,"2025-01-11T10:36:58Z","MCP server for Manifold Markets"),
("bmorphism","bmorphism/slowtime-mcp-server","TypeScript",0,0,6,"2025-01-02T01:23:33Z","A Model Context Protocol server for time-based ops"),
("bmorphism","bmorphism/open-games-agda","Agda",0,0,0,"2024-12-22T11:16:29Z","Formalization of open games in Agda"),
("bmorphism","bmorphism/vibes","Clojure",0,0,0,"2024-11-13T15:56:28Z","Global Vibespace"),
# zubyul (50 repos)
("zubyul","zubyul/voice-observatory","Python",0,0,0,"2026-04-24T05:56:17Z","Passive macOS TUI observing voice-download pathways"),
("zubyul","zubyul/ghostel-emacs-worlds","GLSL",0,0,0,"2026-04-24T00:20:56Z","Ghostty config + ghostel family + alice/bob emacs-mods"),
("zubyul","zubyul/nash-tui","Rust",0,0,0,"2026-04-13T07:45:16Z","NASH token TUI: real-time candles"),
("zubyul","zubyul/nash-web","Rust",0,0,0,"2026-04-13T07:08:58Z","NASH token browser TUI via ratzilla WASM"),
("zubyul","zubyul/big-bad-plurigrid-quiz","Emacs Lisp",0,0,0,"2026-04-09T18:51:31Z","27 flashcards from bmorphism/plurigrid/zubyul activity"),
("zubyul","zubyul/Gay.jl","Julia",0,0,0,"2026-03-28T11:30:01Z","Wide-gamut color sampling with splittable determinism"),
("zubyul","zubyul/gay-world","Python",1,1,0,"2026-03-26T04:03:39Z","Goblin world builder"),
("zubyul","zubyul/tilelang-kernels","Python",0,0,0,"2026-03-16T02:31:13Z","TileLang GPU kernels for SplitMix64 color generation"),
("zubyul","zubyul/gay-terminal-colors","Clojure",0,0,0,"2026-02-21T07:38:14Z","Gay.jl world_terminal_fingerprint"),
("zubyul","zubyul/plurigrid-site","Svelte",0,1,11,"2026-02-04T03:20:08Z","Plurigrid world: site deployment"),
("zubyul","zubyul/openbci-visualizer","Zig",0,0,0,"2026-02-04T11:17:41Z",""),
("zubyul","zubyul/vibesnipe","Move",0,0,1,"2026-01-30T22:36:03Z",""),
("zubyul","zubyul/zubyul.github.io","CSS",1,0,0,"2026-01-27T03:24:34Z",""),
("zubyul","zubyul/toad-warpify-extension","Python",0,0,0,"2026-01-17T07:48:40Z","Warpify extension for Toad"),
("zubyul","zubyul/ghostty-modifications","JavaScript",1,0,0,"2025-09-15T02:45:21Z","Ghostty terminal modifications and MCP servers"),
("zubyul","zubyul/cascade-world","Python",1,0,0,"2025-09-19T18:25:12Z","Cascade development environment"),
("zubyul","zubyul/defcon","JavaScript",1,0,0,"2025-09-17T02:07:00Z",""),
("zubyul","zubyul/GoofyLifeChoices","Python",1,0,0,"2025-07-30T18:48:13Z",""),
# migalkin (19 repos)
("migalkin","migalkin/NodePiece","Python",144,21,0,"2026-05-07T05:40:02Z","Compositional and Parameter-Efficient Representations for KGs"),
("migalkin","migalkin/StarE","Python",89,16,1,"2026-04-16T14:12:45Z","Message Passing for Hyper-Relational Knowledge Graphs"),
("migalkin","migalkin/kgcourse2021","HTML",25,9,0,"2026-02-16T05:16:08Z","Materials for Knowledge Graphs course"),
("migalkin","migalkin/NBFNet_mlx","Python",10,1,1,"2026-03-11T01:31:21Z","Neural Bellman-Ford networks in MLX for Apple Silicon"),
("migalkin","migalkin/RWL","Python",7,1,0,"2025-02-10T14:12:14Z","Weisfeiler and Leman Go Relational"),
("migalkin","migalkin/rambo","Rust",3,0,1,"2023-02-28T16:37:22Z",""),
("migalkin","migalkin/SMJoin-experiments","R",1,0,0,"2020-03-04T15:56:23Z","ISWC 2017 SMJoin results"),
("migalkin","migalkin/School","R",1,0,0,"2014-10-09T02:22:18Z","Projects from grad school"),
# wasita (11 repos)
("wasita","wasita/wasita.github.io","Svelte",1,0,8,"2026-05-18T22:47:03Z","personal website"),
("wasita","wasita/magic-garden","Python",2,1,1,"2026-04-22T21:16:43Z","bot for magic garden discord game"),
("wasita","wasita/vocoder","JavaScript",0,0,0,"2026-05-06T05:14:03Z",""),
("wasita","wasita/wins-search","CSS",1,0,0,"2023-06-03T19:01:11Z","Women in Network Science member list website"),
("wasita","wasita/send2kobo","TypeScript",0,0,0,"2025-12-12T19:09:16Z","Website for sending books to Kobo e-reader"),
("wasita","wasita/wm-cv","Svelte",0,0,0,"2026-05-13T05:29:08Z","Academic CV as single page web app"),
# AustinCStone (40 repos)
("AustinCStone","AustinCStone/TextGAN","Python",92,30,5,"2025-03-03T13:26:32Z","Generative adversarial network for text generation"),
("AustinCStone","AustinCStone/StereoVisionMRF","Python",11,4,0,"2026-04-01T07:39:41Z","Using MRF for depth from stereo images"),
("AustinCStone","AustinCStone/SpectralClustering","Python",3,2,0,"2021-04-16T08:46:36Z","Implementing spectral clustering"),
("AustinCStone","AustinCStone/logisticRegressionHaskell","Haskell",1,0,0,"2018-02-02T13:34:28Z","Logistic regression in Haskell"),
("AustinCStone","AustinCStone/StructureFromMotion","Python",1,0,0,"2019-04-26T19:43:12Z","Recover 3D geometry from videos"),
("AustinCStone","AustinCStone/EpsteinSearch","Python",0,0,0,"2026-02-11T01:10:57Z",""),
# DJedamski (6 repos)
("DJedamski","DJedamski/kaggle_ncaa18","Jupyter Notebook",0,0,0,"2018-02-26T16:33:24Z","Code for NCAA March Madness competition"),
("DJedamski","DJedamski/Kaggle","",1,0,0,"2023-04-21T01:42:35Z",""),
("DJedamski","DJedamski/Getting-and-Cleaning-Data","R",1,0,0,"2023-04-21T01:42:34Z","Coursera Project"),
("DJedamski","DJedamski/School","R",1,1,0,"2023-04-21T01:42:33Z","A couple small projects from grad school"),
# kristinezheng (6 repos)
("kristinezheng","kristinezheng/kristinezheng.github.io","HTML",0,0,0,"2026-05-14T22:29:01Z",""),
("kristinezheng","kristinezheng/lookit-jenga","Jupyter Notebook",0,0,0,"2024-05-16T18:29:05Z","Lookit study for 9.85"),
("kristinezheng","kristinezheng/Green-Machine","Python",0,0,0,"2021-09-19T05:33:04Z","HackMIT 2021: Sustainability Track"),
# M1shaaa (8 repos)
("M1shaaa","M1shaaa/M1shaaa","",0,0,0,"2026-02-04T19:32:04Z","Config files for GitHub profile"),
("M1shaaa","M1shaaa/lab-bookshelf-","TypeScript",0,0,0,"2024-12-31T05:11:18Z",""),
("M1shaaa","M1shaaa/Python-Lookit-Uploads","Python",0,0,0,"2024-02-15T22:59:37Z","random projects"),
]

# ── insert world_increments (one per source) ─────────────────────────────────
sources = ["plurigrid","kubeflow","TeglonLabs","bmorphism","zubyul",
           "migalkin","wasita","AustinCStone","DJedamski","kristinezheng","M1shaaa"]
increment_ids = {}
for i, src in enumerate(sources, 1):
    trit, color, name = GF3[i % 3]
    h = hashlib.sha256(f"{src}-{datetime.datetime.utcnow().isoformat()}".encode()).hexdigest()[:16]
    con.execute("""
        INSERT INTO world_increments VALUES (?,now(),?,?,?,'org_or_user',?,
            'repo_snapshot','','',?)
    """, [i, trit, color, name, src, h])
    increment_ids[src] = i

# ── insert repo_snapshots ────────────────────────────────────────────────────
rid = 1
for r in repos:
    if len(r) == 8:
        org, full, lang, stars, forks, issues, pushed, desc = r
    else:
        # skip malformed
        continue
    inc_id = increment_ids.get(org, 1)
    short = full.split("/")[-1]
    trit, color, name = GF3[rid % 3]
    con.execute("""
        INSERT INTO repo_snapshots VALUES (?,now(),?,?,?,?,?,?,?,?,?,?)
    """, [rid, inc_id, org, short, full, lang, stars, forks, issues, pushed, desc[:200]])
    rid += 1

# ── Aptos snapshots ───────────────────────────────────────────────────────────
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
    con.execute("INSERT INTO aptos_snapshots VALUES (now(),?,?,?)", [world, addr, bal])

# ── Multisig probes ───────────────────────────────────────────────────────────
multisigs = [
("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2,True),
("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2,True),
("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2,True),
("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2,True),
("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2,True),
]
for pair, addr, sigs, healthy in multisigs:
    con.execute("INSERT INTO multisig_probes VALUES (now(),?,?,?,?)", [pair, addr, sigs, healthy])

# ── MNX (SPA, no API data available) ─────────────────────────────────────────
con.execute("INSERT INTO mnx_snapshots VALUES (now(),'N/A','testnet.mnx.fi','SPA-unavailable',NULL,NULL)")

con.commit()

# ── verify ───────────────────────────────────────────────────────────────────
print("=== world_increments:", con.execute("SELECT count(*) FROM world_increments").fetchone()[0])
print("=== repo_snapshots:", con.execute("SELECT count(*) FROM repo_snapshots").fetchone()[0])
print("=== aptos_snapshots:", con.execute("SELECT count(*) FROM aptos_snapshots").fetchone()[0])
print("=== multisig_probes:", con.execute("SELECT count(*) FROM multisig_probes").fetchone()[0])
print("=== mnx_snapshots:", con.execute("SELECT count(*) FROM mnx_snapshots").fetchone()[0])
print("=== repos by source:")
for row in con.execute("SELECT org_or_user, count(*) AS cnt FROM repo_snapshots GROUP BY org_or_user ORDER BY cnt DESC").fetchall():
    print(f"    {row[0]}: {row[1]}")
con.close()
print("DONE")
