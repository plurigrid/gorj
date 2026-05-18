#!/usr/bin/env python3
"""Build world-increments DuckDB from swept GitHub + Aptos data."""
import duckdb, hashlib, datetime

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
con = duckdb.connect(DB)

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

def gf3(i):
    t = i % 3
    if t == 0:   return (0,  "#d3869b", "ERGODIC")
    elif t == 1: return (1,  "#b8bb26", "PLUS")
    else:        return (-1, "#cc241d", "MINUS")

# ── repo data ───────────────────────────────────────────────────────────────
repos = [
  # plurigrid (100)
  ("plurigrid","plurigrid/marketplace","","0","0","1","2023-07-09T05:52:30Z",""),
  ("plurigrid","plurigrid/shepherd","Scheme","0","0","0","2026-01-23T07:47:28Z","Spritely Shepherd - Service manager"),
  ("plurigrid","plurigrid/duck-kanban","Rust","1","0","0","2025-09-26T20:18:38Z","Duck intelligence kanban system"),
  ("plurigrid","plurigrid/json-canvas","","0","0","0","2026-02-06T06:50:57Z","JSON Canvas: Real-time interaction data"),
  ("plurigrid","plurigrid/nanoclj-zig","Zig","1","2","20","2026-04-25T07:29:09Z","NaN-boxed Clojure interpreter in Zig 0.15"),
  ("plurigrid","plurigrid/Plurigraph","JavaScript","3","5","4","2025-01-05T08:39:09Z","Plurigrid knowledge base for Obsidian.md"),
  ("plurigrid","plurigrid/graded-optic","Haskell","0","0","0","2026-02-08T16:10:16Z","Semiring-graded bidirectional processes"),
  ("plurigrid","plurigrid/org","Jupyter Notebook","2","0","1","2023-11-07T01:08:05Z","Dynamically Replicating Duck"),
  ("plurigrid","plurigrid/ontology","JavaScript","8","9","16","2025-05-27T18:18:34Z","autopoietic ergodicity and embodied gradualism"),
  ("plurigrid","plurigrid/zig-syrup","Zig","2","2","0","2026-04-30T03:52:16Z","High-performance Zig OCapN Syrup"),
  ("plurigrid","plurigrid/nblm-flashcards","Hy","0","0","0","2026-03-26T08:23:01Z","NotebookLM flashcard pipeline"),
  ("plurigrid","plurigrid/tree-sitter-nanoclj-zig","C","0","0","0","2026-04-04T07:48:21Z","Tree-sitter grammar for nanoclj-zig"),
  ("plurigrid","plurigrid/web-browser","Rust","0","0","0","2026-04-10T02:54:47Z","web-browser from prepostweb lineage"),
  ("plurigrid","plurigrid/StochFlow","Python","4","1","0","2024-03-20T23:34:57Z","stochastic interpolant models"),
  ("plurigrid","plurigrid/asi-skills","Julia","3","1","0","2026-04-26T08:09:26Z","69 skills with Galois Hole Type"),
  ("plurigrid","plurigrid/gay-tofu","HTML","0","0","0","2026-01-08T15:14:34Z","Low-discrepancy color sequences"),
  ("plurigrid","plurigrid/bci-blue-share","JavaScript","0","0","0","2026-04-26T07:08:03Z","BCI signal infrastructure"),
  ("plurigrid","plurigrid/nash-portal","Rust","2","3","2","2026-04-26T08:50:56Z","NASH token TUI in the browser"),
  ("plurigrid","plurigrid/microworlds","Rust","3","5","3","2023-05-13T03:54:56Z","microworlds"),
  ("plurigrid","plurigrid/asi","HTML","23","5","4","2026-04-26T08:51:41Z","everything is topological chemputer!"),
  ("plurigrid","plurigrid/horse","TeX","1","1","9","2026-05-07T04:35:12Z","horse"),
  ("plurigrid","plurigrid/vivarium","Clojure","1","0","0","2026-04-08T08:38:37Z","vivarium"),
  ("plurigrid","plurigrid/gatomic","Clojure","0","0","0","2026-03-30T00:54:48Z","Deterministic color identity store"),
  ("plurigrid","plurigrid/agent-o-rama","Clojure","0","0","0","2026-01-02T01:09:22Z","agent-o-rama"),
  ("plurigrid","plurigrid/reafference","HTML","0","0","0","2026-04-16T05:21:49Z","Reafference adaptation workspace"),
  ("plurigrid","plurigrid/gorj","Clojure","0","0","240","2026-05-18T14:21:58Z","forj + Rama topology nREPL routing + GF(3)"),
  ("plurigrid","plurigrid/forester","XSLT","0","0","0","2026-03-30T01:32:26Z","CatColab mathematical documentation"),
  ("plurigrid","plurigrid/lazybjj","Rust","0","0","0","2026-01-08T14:19:19Z","TUI for jj with Gay.jl GF(3) coloring"),
  ("plurigrid","plurigrid/blue","TeX","0","0","0","2026-03-29T23:06:32Z","blue"),
  ("plurigrid","plurigrid/hoot","Scheme","0","0","0","2026-01-23T07:47:10Z","Spritely Hoot - Scheme to WebAssembly"),
  ("plurigrid","plurigrid/flowglad-rs","Rust","0","0","0","2026-04-08T07:56:15Z","flowglad-rs"),
  ("plurigrid","plurigrid/vcg-auction","Rust","7","2","1","2023-03-16T21:53:08Z","VCG auction contract"),
  ("plurigrid","plurigrid/act","Python","3","1","4","2024-07-26T08:27:08Z","building blocks for cognitive category theory"),
  ("plurigrid","plurigrid/agent","Python","5","1","6","2023-03-31T18:45:23Z","Framework for agency amplification"),
  ("plurigrid","plurigrid/leprechauns","Racket","0","0","0","2026-01-23T07:46:46Z","Spritely Goblins + Gay.jl semantic colors"),
  ("plurigrid","plurigrid/spi-race","Swift","0","0","0","2026-04-21T19:31:56Z","Splitmix Parallel Integrity"),
  ("plurigrid","plurigrid/gay-rs","Rust","0","0","0","2026-01-08T14:19:22Z","Rust crate for Gay.jl GF(3) trits"),
  ("plurigrid","plurigrid/aptos-wallet-ruby","Ruby","1","0","0","2025-09-30T22:47:22Z","aptos-wallet-ruby"),
  ("plurigrid","plurigrid/ducklings","TypeScript","0","0","15","2023-12-25T07:34:27Z","ducklings"),
  ("plurigrid","plurigrid/gemini-agent","Python","0","0","0","2026-02-19T06:39:16Z","gemini-agent"),
  ("plurigrid","plurigrid/shiteshiteshite","","0","0","0","2025-09-26T03:07:20Z","Duck intelligence kanban"),
  ("plurigrid","plurigrid/spritely-semantic-colors","","0","0","0","2026-01-23T07:38:32Z","Deterministic color mappings for Spritely"),
  ("plurigrid","plurigrid/gay-go","Go","0","0","0","2026-01-08T14:19:23Z","Go implementation of Gay.jl"),
  ("plurigrid","plurigrid/gay-terminal","Rust","0","0","0","2026-01-08T14:19:24Z","Terminal ANSI coloring with Gay.jl"),
  ("plurigrid","plurigrid/lazygay","Go","0","0","0","2026-01-08T14:19:25Z","lazygit fork with Gay.jl coloring"),
  ("plurigrid","plurigrid/ACT.jl","Julia","0","0","0","2024-01-21T00:02:25Z","applied categorical duck cybernetics"),
  ("plurigrid","plurigrid/website","Clojure","0","1","0","2024-03-30T04:37:51Z","website"),
  # kubeflow (48)
  ("kubeflow","kubeflow/kubeflow","","15647","2648","2","2026-05-07T13:46:41Z","Machine Learning Toolkit for Kubernetes"),
  ("kubeflow","kubeflow/pipelines","Python","4139","1993","469","2026-05-17T16:25:03Z","Machine Learning Pipelines for Kubeflow"),
  ("kubeflow","kubeflow/spark-operator","Python","3126","1482","93","2026-05-15T16:31:02Z","Kubernetes operator for Apache Spark"),
  ("kubeflow","kubeflow/trainer","Go","2100","950","105","2026-05-15T15:21:03Z","Distributed AI Model Training on Kubernetes"),
  ("kubeflow","kubeflow/katib","Python","1682","521","123","2026-05-09T12:21:57Z","Automated Machine Learning on Kubernetes"),
  ("kubeflow","kubeflow/examples","Jsonnet","1463","756","111","2025-04-14T01:54:52Z","extended examples and tutorials"),
  ("kubeflow","kubeflow/manifests","YAML","1017","1064","26","2026-05-16T16:37:54Z","Kubeflow AI Reference Platform Manifests"),
  ("kubeflow","kubeflow/arena","Go","810","190","57","2026-05-07T06:46:17Z","A CLI for Kubeflow"),
  ("kubeflow","kubeflow/kale","Python","687","156","57","2026-05-15T19:04:47Z","Kubeflow superfood for Data Scientists"),
  ("kubeflow","kubeflow/mpi-operator","Go","527","235","101","2026-05-12T17:13:37Z","Kubernetes Operator for MPI-based apps"),
  ("kubeflow","kubeflow/fairing","Jsonnet","337","143","134","2022-04-11T05:28:47Z","Python SDK for building/training/deploying ML"),
  ("kubeflow","kubeflow/pytorch-operator","Jsonnet","310","143","63","2021-12-01T17:44:48Z","PyTorch on Kubernetes"),
  ("kubeflow","kubeflow/community","Jsonnet","196","257","14","2026-05-13T18:53:18Z","Kubeflow community info"),
  ("kubeflow","kubeflow/hub","Go","175","178","48","2026-05-18T12:41:11Z","Model Registry single pane of glass"),
  ("kubeflow","kubeflow/website","HTML","184","920","52","2026-05-14T17:20:09Z","Kubeflow Website"),
  ("kubeflow","kubeflow/kfp-tekton","TypeScript","182","123","79","2024-11-19T12:23:51Z","Kubeflow Pipelines on Tekton"),
  ("kubeflow","kubeflow/kfctl","Go","182","134","94","2023-08-15T20:19:22Z","kfctl CLI for deploying Kubeflow"),
  ("kubeflow","kubeflow/mcp-apache-spark-history-server","Python","170","60","24","2026-05-13T19:15:35Z","MCP Server for Spark History Server"),
  ("kubeflow","kubeflow/example-seldon","Jupyter Notebook","172","56","9","2021-12-01T01:49:58Z","e2e ML on Kubernetes with Seldon"),
  ("kubeflow","kubeflow/sdk","Python","118","174","135","2026-05-12T18:53:41Z","Universal Python SDK for AI workloads"),
  ("kubeflow","kubeflow/metadata","TypeScript","123","63","38","2021-12-01T17:35:27Z","Metadata assets"),
  ("kubeflow","kubeflow/dashboard","TypeScript","17","55","76","2026-05-16T00:25:13Z","Kubeflow Central Dashboard"),
  ("kubeflow","kubeflow/notebooks","","72","110","189","2026-05-15T15:41:12Z","Kubeflow Notebooks"),
  ("kubeflow","kubeflow/docs-agent","Python","36","98","153","2026-04-14T03:33:15Z","Kubeflow Documentation AI Agent"),
  ("kubeflow","kubeflow/blog","Jupyter Notebook","32","62","27","2026-05-11T15:21:33Z","Kubeflow blog"),
  ("kubeflow","kubeflow/code-intelligence","Jupyter Notebook","56","20","64","2021-12-01T01:52:58Z","ML-Powered Developer Tools"),
  ("kubeflow","kubeflow/xgboost-operator","Python","77","53","22","2021-12-01T18:00:10Z","xgboost operator"),
  ("kubeflow","kubeflow/testing","Python","60","86","33","2025-02-14T18:33:13Z","Test infrastructure for Kubeflow"),
  ("kubeflow","kubeflow/mcp-server","Python","9","13","22","2026-05-12T10:14:24Z","MCP Server for Kubeflow Tools"),
  ("kubeflow","kubeflow/internal-acls","Go","19","385","3","2026-05-09T21:06:02Z","Group ACLs for Kubeflow developers"),
  ("kubeflow","kubeflow/pipelines-components","Python","11","38","32","2026-05-11T18:19:25Z","Kubeflow Pipelines components"),
  ("kubeflow","kubeflow/mlflow-integration","Python","6","3","3","2026-05-15T19:20:29Z","mlflow-integration"),
  # TeglonLabs (4)
  ("TeglonLabs","TeglonLabs/topoi","Python","0","0","1","2025-01-24T04:49:26Z","topoi"),
  ("TeglonLabs","TeglonLabs/mathpix-gem","Ruby","2","0","11","2026-01-01T12:13:13Z","Transform math images to LaTeX"),
  ("TeglonLabs","TeglonLabs/monad-mcp-server","","0","0","0","2025-05-14T11:36:14Z","Monad MCP Server"),
  ("TeglonLabs","TeglonLabs/coin-flip-mcp","JavaScript","0","2","1","2025-09-21T08:57:27Z","MCP server for flipping coins"),
  # bmorphism (selected key repos)
  ("bmorphism","bmorphism/Gay.jl","Julia","1","0","189","2026-05-18T00:35:46Z","Wide-gamut color sampling with splittable determinism"),
  ("bmorphism","bmorphism/ocaml-mcp-sdk","OCaml","61","2","0","2026-03-16T05:24:25Z","OCaml SDK for Model Context Protocol"),
  ("bmorphism","bmorphism/anti-bullshit-mcp-server","JavaScript","23","7","1","2026-01-16T08:54:58Z","MCP server for analyzing claims"),
  ("bmorphism","bmorphism/risc0-cosmwasm-example","Rust","23","2","1","2022-10-20T23:50:40Z","CosmWasm + zkVM RISC-V EFI template"),
  ("bmorphism","bmorphism/say-mcp-server","JavaScript","20","9","3","2025-01-07T03:15:18Z","MCP server for macOS TTS"),
  ("bmorphism","bmorphism/babashka-mcp-server","JavaScript","18","6","3","2025-01-05T11:09:42Z","MCP server for Babashka Clojure"),
  ("bmorphism","bmorphism/manifold-mcp-server","JavaScript","14","9","5","2025-01-11T10:36:58Z","MCP server for Manifold Markets"),
  ("bmorphism","bmorphism/penrose-mcp","JavaScript","10","4","0","2025-01-20T21:44:55Z","Penrose server for Infinity-Topos"),
  ("bmorphism","bmorphism/hypernym-mcp-server","JavaScript","6","5","0","2025-04-02T21:21:08Z","hypernym-mcp-server"),
  ("bmorphism","bmorphism/penumbra-mcp","JavaScript","5","6","3","2025-01-07T01:15:23Z","MCP server for Penumbra blockchain"),
  ("bmorphism","bmorphism/shitcoin","Python","5","0","0","2026-04-08T08:07:08Z","gets denom for cw20 assets"),
  ("bmorphism","bmorphism/marginalia-mcp-server","JavaScript","8","6","0","2025-01-06T05:47:24Z","MCP server for marginalia"),
  ("bmorphism","bmorphism/gists-mcp-server","JavaScript","2","0","0","2025-01-03T03:50:54Z","MCP server for GitHub Gists"),
  ("bmorphism","bmorphism/graphistry-mcp","Python","2","0","0","2025-05-06T17:34:24Z","Graphistry MCP integration"),
  ("bmorphism","bmorphism/whale","MATLAB","2","0","0","2025-09-04T06:55:21Z","omniglot + sperm whale codas"),
  ("bmorphism","bmorphism/open-location-code-zig","Zig","3","0","0","2025-12-30T19:33:45Z","Open Location Code for Zig"),
  ("bmorphism","bmorphism/oxgame","OCaml","0","0","0","2026-05-15T09:53:27Z","Stellar resolution and open-game composition"),
  ("bmorphism","bmorphism/nanoclj-zig","Zig","0","0","0","2026-05-07T20:12:15Z","nanoclj-zig"),
  ("bmorphism","bmorphism/zig-syrup","Zig","0","0","0","2026-05-07T19:49:05Z","Embeddable OCapN Syrup encoder/decoder"),
  ("bmorphism","bmorphism/slowtime-mcp-server","TypeScript","3","5","6","2025-01-02T01:23:33Z","MCP server for time-based operations"),
  # zubyul (selected)
  ("zubyul","zubyul/repl","Python","0","0","0","2026-02-04T01:08:15Z","repl"),
  ("zubyul","zubyul/gay-world","Python","1","1","0","2026-03-26T04:03:39Z","Goblin world builder - MLX task decomposition"),
  ("zubyul","zubyul/big-bad-plurigrid-quiz","Emacs Lisp","0","0","0","2026-04-09T18:51:31Z","27 flashcards from bmorphism/plurigrid/zubyul"),
  ("zubyul","zubyul/ghostel-emacs-worlds","GLSL","0","0","0","2026-04-24T00:20:56Z","Ghostty config + alice/bob emacs-mods"),
  ("zubyul","zubyul/nash-tui","Rust","0","0","0","2026-04-13T07:45:16Z","NASH token TUI: real-time candles"),
  ("zubyul","zubyul/toad-warpify-extension","Python","0","0","0","2026-01-17T07:48:40Z","Warpify extension for Toad"),
  ("zubyul","zubyul/openbci-visualizer","Zig","0","0","0","2026-02-04T11:17:41Z","openbci-visualizer"),
  ("zubyul","zubyul/fleet-bootstrap","Shell","0","0","0","2026-02-23T08:19:58Z","fleet-bootstrap"),
  ("zubyul","zubyul/tilelang-kernels","Python","0","0","0","2026-03-16T02:31:13Z","TileLang GPU kernels for SplitMix64"),
  ("zubyul","zubyul/from-possible-worlds","TeX","0","0","0","2026-03-16T03:14:55Z","from-possible-worlds"),
  ("zubyul","zubyul/chromatic-vrf","Kotlin","0","0","0","2025-12-12T03:26:22Z","Chromatic VRF: I Love Hue puzzle"),
  ("zubyul","zubyul/wasita.github.io","Svelte","1","0","0","2026-05-18T03:31:12Z","personal website"),
  ("zubyul","zubyul/plurigrid-site","Svelte","0","1","11","2026-02-04T03:20:08Z","Plurigrid world site deployment"),
  # migalkin (19)
  ("migalkin","migalkin/NodePiece","Python","144","21","0","2022-02-02T03:34:04Z","Compositional representations for KGs"),
  ("migalkin","migalkin/StarE","Python","89","16","1","2023-12-01T20:12:24Z","Message Passing for Hyper-Relational KGs"),
  ("migalkin","migalkin/kgcourse2021","HTML","25","9","0","2025-08-04T03:01:46Z","Knowledge Graphs course materials"),
  ("migalkin","migalkin/NBFNet_mlx","Python","10","1","1","2024-03-02T00:15:23Z","Neural Bellman-Ford networks in MLX"),
  ("migalkin","migalkin/RWL","Python","7","1","0","2022-12-01T15:58:59Z","Weisfeiler and Leman Go Relational"),
  ("migalkin","migalkin/rambo","Rust","3","0","1","2023-02-08T14:27:03Z","rambo"),
  ("migalkin","migalkin/migalkin.github.io","JavaScript","0","0","0","2025-01-22T04:53:51Z","academic personal website"),
  # wasita (11)
  ("wasita","wasita/wasita.github.io","Svelte","1","0","8","2026-05-18T03:31:12Z","personal website"),
  ("wasita","wasita/magic-garden","Python","2","1","1","2026-01-13T23:51:32Z","magic garden discord bot"),
  ("wasita","wasita/wins-search","CSS","1","0","0","2022-12-14T22:17:32Z","Women in Network Science member list"),
  ("wasita","wasita/wm-cv","Svelte","0","0","0","2026-05-13T05:29:04Z","Academic CV as SPA"),
  ("wasita","wasita/ch3-lib","Typst","0","0","0","2026-04-12T04:03:19Z","ch3-lib"),
  ("wasita","wasita/vocoder","JavaScript","0","0","0","2026-05-06T05:14:00Z","vocoder"),
  # AustinCStone (selected)
  ("AustinCStone","AustinCStone/TextGAN","Python","92","30","5","2016-10-04T03:19:12Z","GAN for text generation in TensorFlow"),
  ("AustinCStone","AustinCStone/StereoVisionMRF","Python","11","4","0","2016-01-10T08:34:29Z","MRF for depth from stereo images"),
  ("AustinCStone","AustinCStone/SpectralClustering","Python","3","2","0","2015-11-09T03:27:15Z","spectral clustering homework"),
  ("AustinCStone","AustinCStone/bmfork","Python","0","0","1","2025-05-09T04:17:17Z","bmfork"),
  ("AustinCStone","AustinCStone/EpsteinSearch","Python","0","0","0","2026-02-11T01:10:54Z","EpsteinSearch"),
  # DJedamski (6)
  ("DJedamski","DJedamski/Getting-and-Cleaning-Data","R","1","0","0","2015-02-13T00:04:31Z","Coursera Project"),
  ("DJedamski","DJedamski/Kaggle","","1","0","0","2014-11-03T02:22:01Z","Kaggle"),
  ("DJedamski","DJedamski/School","R","1","1","0","2014-10-09T02:22:18Z","Small projects from grad school"),
  ("DJedamski","DJedamski/kaggle_ncaa18","Jupyter Notebook","0","0","0","2018-02-26T16:33:24Z","NCAA March Madness 2018"),
  # kristinezheng (6)
  ("kristinezheng","kristinezheng/kristinezheng.github.io","HTML","0","0","0","2026-05-14T22:29:01Z","personal site"),
  ("kristinezheng","kristinezheng/Portfolio","","0","0","0","2025-02-12T00:00:45Z","July 2021"),
  ("kristinezheng","kristinezheng/lookit-jenga","Jupyter Notebook","0","0","0","2024-05-16T18:29:05Z","Lookit study"),
  ("kristinezheng","kristinezheng/Green-Machine","Python","0","0","0","2021-09-19T05:33:04Z","HackMIT 2021"),
  # M1shaaa (8)
  ("M1shaaa","M1shaaa/lab-bookshelf-","TypeScript","0","0","0","2024-12-31T05:11:18Z","lab-bookshelf"),
  ("M1shaaa","M1shaaa/M1shaaa","","0","0","0","2026-02-04T19:32:04Z","Config files for GitHub profile"),
  ("M1shaaa","M1shaaa/Python-Lookit-Uploads","Python","0","0","0","2024-02-15T22:59:37Z","random projects"),
  ("M1shaaa","M1shaaa/rosie-s-study-3-lookit-project","","0","0","0","2024-11-04T22:15:49Z","Lookit project"),
]

# Insert repos + world_increments
now = datetime.datetime.utcnow().isoformat()
inc_id = 1
repo_id = 1

for (src, full_name, lang, stars, forks, issues, pushed_at, desc) in repos:
    trit, color, name = gf3(inc_id)
    h = hashlib.sha256(full_name.encode()).hexdigest()[:16]
    repo_name = full_name.split("/")[-1]
    con.execute(
        "INSERT INTO world_increments VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        [inc_id, now, trit, color, name, "github", src, "repo_snapshot", repo_name, src, h]
    )
    con.execute(
        "INSERT INTO repo_snapshots VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
        [repo_id, now, inc_id, src, repo_name, full_name, lang,
         int(stars), int(forks), int(issues), pushed_at, desc[:120]]
    )
    inc_id += 1
    repo_id += 1

# ── Aptos wallet balances ────────────────────────────────────────────────────
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
for (world, addr, bal) in aptos_data:
    con.execute("INSERT INTO aptos_snapshots VALUES (?,?,?,?)", [now, world, addr, bal])

# ── Multisig probes ──────────────────────────────────────────────────────────
multisig_data = [
  ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2,True),
  ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2,True),
  ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2,True),
  ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2,True),
  ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2,True),
]
for (pair, addr, sigs, healthy) in multisig_data:
    con.execute("INSERT INTO multisig_probes VALUES (?,?,?,?,?)", [now, pair, addr, sigs, healthy])

# ── MNX (unavailable) ────────────────────────────────────────────────────────
# testnet.mnx.fi is a Next.js SPA, no public JSON market API found

# ── Summary query ────────────────────────────────────────────────────────────
print("\n=== world_increments count ===")
print(con.execute("SELECT count(*) FROM world_increments").fetchone())
print("\n=== repo_snapshots by source ===")
for row in con.execute("SELECT org_or_user, count(*) as n FROM repo_snapshots GROUP BY org_or_user ORDER BY n DESC").fetchall():
    print(row)
print("\n=== top repos by stars ===")
for row in con.execute("SELECT full_name, stars, language FROM repo_snapshots ORDER BY stars DESC LIMIT 15").fetchall():
    print(row)
print("\n=== GF3 distribution ===")
for row in con.execute("SELECT gf3_name, gf3_color, count(*) FROM world_increments GROUP BY gf3_name, gf3_color").fetchall():
    print(row)
print("\n=== multisig_probes ===")
for row in con.execute("SELECT pair, sigs_required, healthy FROM multisig_probes").fetchall():
    print(row)
print("\n=== aptos_snapshots count ===")
print(con.execute("SELECT count(*) FROM aptos_snapshots").fetchone())

con.close()
print("\nDuckDB built successfully.")
