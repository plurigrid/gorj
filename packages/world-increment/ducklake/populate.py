#!/usr/bin/env python3
"""Populate world-increments DuckDB with GitHub sweep + Aptos/multisig snapshots."""
import duckdb, json, hashlib, time

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
    if t == 0: return (0, "#d3869b", "ERGODIC")
    if t == 1: return (1, "#b8bb26", "PLUS")
    return (-1, "#cc241d", "MINUS")

def snap_hash(s):
    return hashlib.sha256(s.encode()).hexdigest()[:16]

# ── World increment sources ──────────────────────────────────────────────────
SOURCES = [
    ("org",  "plurigrid",    "github_sweep"),
    ("org",  "kubeflow",     "github_sweep"),
    ("org",  "TeglonLabs",   "github_sweep"),
    ("user", "bmorphism",    "github_sweep"),
    ("user", "zubyul",       "github_sweep"),
    ("user", "migalkin",     "github_sweep"),
    ("user", "DJedamski",    "github_sweep"),
    ("user", "wasita",       "github_sweep"),
    ("user", "kristinezheng","github_sweep"),
    ("user", "M1shaaa",      "github_sweep"),
    ("user", "AustinCStone", "github_sweep"),
    ("chain","aptos_mainnet","wallet_snapshot"),
    ("chain","aptos_mainnet","multisig_probe"),
    ("market","mnx_testnet", "market_snapshot"),
]

con.execute("DELETE FROM world_increments")
for i, (stype, sname, etype) in enumerate(SOURCES, start=1):
    trit, color, name = gf3(i)
    h = snap_hash(f"{stype}{sname}{etype}{i}")
    con.execute("INSERT INTO world_increments VALUES (?,now(),?,?,?,?,?,?,?,?,?)",
                [i, trit, color, name, stype, sname, etype, None, None, h])

# ── Repo snapshots ───────────────────────────────────────────────────────────
REPOS = [
# TeglonLabs
{"ou":"TeglonLabs","rn":"mathpix-gem","fn":"TeglonLabs/mathpix-gem","lang":"Ruby","s":2,"f":0,"oi":11,"pa":"2026-01-01T12:13:13Z","d":"Transform mathematical images to LaTeX"},
{"ou":"TeglonLabs","rn":"coin-flip-mcp","fn":"TeglonLabs/coin-flip-mcp","lang":"JavaScript","s":0,"f":2,"oi":1,"pa":"2025-09-21T08:57:27Z","d":"MCP server for flipping coins"},
{"ou":"TeglonLabs","rn":"monad-mcp-server","fn":"TeglonLabs/monad-mcp-server","lang":None,"s":0,"f":0,"oi":0,"pa":"2025-05-14T11:36:14Z","d":"Monad MCP Server"},
{"ou":"TeglonLabs","rn":"topoi","fn":"TeglonLabs/topoi","lang":"Python","s":0,"f":0,"oi":1,"pa":"2025-01-24T04:49:26Z","d":None},
# kubeflow
{"ou":"kubeflow","rn":"pipelines","fn":"kubeflow/pipelines","lang":"Python","s":4153,"f":2006,"oi":494,"pa":"2026-06-06T11:07:54Z","d":"Machine Learning Pipelines for Kubeflow"},
{"ou":"kubeflow","rn":"notebooks","fn":"kubeflow/notebooks","lang":None,"s":73,"f":118,"oi":182,"pa":"2026-06-06T01:03:23Z","d":"Kubeflow Notebooks"},
{"ou":"kubeflow","rn":"community","fn":"kubeflow/community","lang":"Jupyter Notebook","s":194,"f":257,"oi":15,"pa":"2026-06-05T17:29:18Z","d":"Kubeflow community information"},
{"ou":"kubeflow","rn":"manifests","fn":"kubeflow/manifests","lang":"YAML","s":1020,"f":1065,"oi":22,"pa":"2026-06-05T14:42:22Z","d":"Kubeflow Community Distribution"},
{"ou":"kubeflow","rn":"hub","fn":"kubeflow/hub","lang":"Go","s":175,"f":182,"oi":44,"pa":"2026-06-05T15:39:48Z","d":"Model Registry"},
{"ou":"kubeflow","rn":"trainer","fn":"kubeflow/trainer","lang":"Go","s":2112,"f":964,"oi":123,"pa":"2026-06-05T03:17:48Z","d":"Distributed AI Model Training on Kubernetes"},
{"ou":"kubeflow","rn":"website","fn":"kubeflow/website","lang":"HTML","s":184,"f":921,"oi":46,"pa":"2026-06-05T02:01:44Z","d":"Kubeflow Website"},
{"ou":"kubeflow","rn":"kale","fn":"kubeflow/kale","lang":"Python","s":691,"f":155,"oi":48,"pa":"2026-06-05T21:02:41Z","d":"Kubeflow's superfood for Data Scientists"},
{"ou":"kubeflow","rn":"spark-operator","fn":"kubeflow/spark-operator","lang":"Python","s":3125,"f":1488,"oi":99,"pa":"2026-06-04T17:55:40Z","d":"Kubernetes operator for Apache Spark"},
{"ou":"kubeflow","rn":"mcp-apache-spark-history-server","fn":"kubeflow/mcp-apache-spark-history-server","lang":"Python","s":174,"f":62,"oi":22,"pa":"2026-06-04T17:24:33Z","d":"MCP Server for Spark History Server"},
{"ou":"kubeflow","rn":"dashboard","fn":"kubeflow/dashboard","lang":"TypeScript","s":16,"f":57,"oi":72,"pa":"2026-06-05T19:15:56Z","d":"Kubeflow Central Dashboard"},
{"ou":"kubeflow","rn":"katib","fn":"kubeflow/katib","lang":"Python","s":1685,"f":526,"oi":120,"pa":"2026-06-05T23:23:35Z","d":"Automated Machine Learning on Kubernetes"},
{"ou":"kubeflow","rn":"sdk","fn":"kubeflow/sdk","lang":"Python","s":120,"f":181,"oi":137,"pa":"2026-06-04T03:07:45Z","d":"Universal Python SDK for Kubernetes AI"},
{"ou":"kubeflow","rn":"internal-acls","fn":"kubeflow/internal-acls","lang":"Go","s":19,"f":388,"oi":2,"pa":"2026-06-01T16:22:32Z","d":"Group ACLs for Kubeflow developers"},
{"ou":"kubeflow","rn":"mpi-operator","fn":"kubeflow/mpi-operator","lang":"Go","s":528,"f":235,"oi":103,"pa":"2026-06-02T14:30:58Z","d":"MPI-based applications on Kubernetes"},
{"ou":"kubeflow","rn":"kubeflow","fn":"kubeflow/kubeflow","lang":None,"s":15706,"f":2671,"oi":3,"pa":"2026-05-24T11:31:41Z","d":"Machine Learning Toolkit for Kubernetes"},
{"ou":"kubeflow","rn":"arena","fn":"kubeflow/arena","lang":"Go","s":811,"f":191,"oi":46,"pa":"2026-05-07T06:46:17Z","d":"A CLI for Kubeflow"},
{"ou":"kubeflow","rn":"examples","fn":"kubeflow/examples","lang":"Jsonnet","s":1462,"f":756,"oi":111,"pa":"2025-04-14T01:54:52Z","d":"Extended examples and tutorials"},
{"ou":"kubeflow","rn":"fairing","fn":"kubeflow/fairing","lang":"Jsonnet","s":337,"f":143,"oi":134,"pa":"2022-04-11T05:28:47Z","d":"Python SDK for building and deploying ML"},
{"ou":"kubeflow","rn":"mcp-server","fn":"kubeflow/mcp-server","lang":"Python","s":10,"f":19,"oi":25,"pa":"2026-05-12T10:14:24Z","d":"MCP Server for Kubeflow"},
# plurigrid
{"ou":"plurigrid","rn":"gorj","fn":"plurigrid/gorj","lang":"Clojure","s":0,"f":0,"oi":414,"pa":"2026-06-07T08:18:03Z","d":"forj + Rama + GF(3) gay trit coloring"},
{"ou":"plurigrid","rn":"place","fn":"plurigrid/place","lang":"TeX","s":1,"f":2,"oi":8,"pa":"2026-06-04T09:51:50Z","d":None},
{"ou":"plurigrid","rn":"eirobri","fn":"plurigrid/eirobri","lang":"Clojure","s":0,"f":0,"oi":29,"pa":"2026-06-03T20:43:46Z","d":"EiRoBri replay world"},
{"ou":"plurigrid","rn":"nash-portal","fn":"plurigrid/nash-portal","lang":"Rust","s":2,"f":3,"oi":1,"pa":"2026-05-19T01:49:59Z","d":"NASH token TUI in the browser"},
{"ou":"plurigrid","rn":"zig-syrup","fn":"plurigrid/zig-syrup","lang":"Zig","s":2,"f":2,"oi":0,"pa":"2026-04-30T03:52:16Z","d":"OCapN Syrup in Zig"},
{"ou":"plurigrid","rn":"asi","fn":"plurigrid/asi","lang":"HTML","s":25,"f":7,"oi":4,"pa":"2026-04-26T08:51:41Z","d":"everything is topological chemputer!"},
{"ou":"plurigrid","rn":"asi-skills","fn":"plurigrid/asi-skills","lang":"Julia","s":3,"f":1,"oi":0,"pa":"2026-04-26T08:09:26Z","d":"69 skills with Galois Hole Type"},
{"ou":"plurigrid","rn":"nanoclj-zig","fn":"plurigrid/nanoclj-zig","lang":"Zig","s":1,"f":2,"oi":20,"pa":"2026-04-25T07:29:09Z","d":"NaN-boxed Clojure interpreter in Zig"},
{"ou":"plurigrid","rn":"spi-race","fn":"plurigrid/spi-race","lang":"Swift","s":0,"f":0,"oi":0,"pa":"2026-04-21T19:31:56Z","d":"Splitmix Parallel Integrity"},
{"ou":"plurigrid","rn":"reafference","fn":"plurigrid/reafference","lang":"HTML","s":0,"f":0,"oi":0,"pa":"2026-04-16T05:21:49Z","d":"Reafference adaptation workspace"},
{"ou":"plurigrid","rn":"web-browser","fn":"plurigrid/web-browser","lang":"Rust","s":0,"f":0,"oi":0,"pa":"2026-04-10T02:54:47Z","d":"web-browser from prepostweb lineage"},
{"ou":"plurigrid","rn":"vivarium","fn":"plurigrid/vivarium","lang":"Clojure","s":1,"f":0,"oi":0,"pa":"2026-04-08T08:38:37Z","d":None},
{"ou":"plurigrid","rn":"forester","fn":"plurigrid/forester","lang":"XSLT","s":0,"f":0,"oi":0,"pa":"2026-03-30T01:32:26Z","d":"CatColab mathematical documentation forest"},
{"ou":"plurigrid","rn":"gatomic","fn":"plurigrid/gatomic","lang":"Clojure","s":0,"f":0,"oi":0,"pa":"2026-03-30T00:54:48Z","d":"Deterministic color identity store"},
{"ou":"plurigrid","rn":"nblm-flashcards","fn":"plurigrid/nblm-flashcards","lang":"Hy","s":0,"f":0,"oi":0,"pa":"2026-03-26T08:23:01Z","d":"NotebookLM flashcard pipeline"},
{"ou":"plurigrid","rn":"graded-optic","fn":"plurigrid/graded-optic","lang":"Haskell","s":0,"f":0,"oi":0,"pa":"2026-02-08T16:10:16Z","d":"Semiring-graded bidirectional processes"},
{"ou":"plurigrid","rn":"shepherd","fn":"plurigrid/shepherd","lang":"Scheme","s":0,"f":0,"oi":0,"pa":"2026-01-23T07:47:28Z","d":"Spritely Shepherd service manager"},
{"ou":"plurigrid","rn":"hoot","fn":"plurigrid/hoot","lang":"Scheme","s":0,"f":0,"oi":1,"pa":"2026-01-23T07:47:10Z","d":"Spritely Hoot - Scheme to WebAssembly"},
{"ou":"plurigrid","rn":"leprechauns","fn":"plurigrid/leprechauns","lang":"Racket","s":0,"f":0,"oi":0,"pa":"2026-01-23T07:46:46Z","d":"Spritely Goblins + Gay.jl"},
{"ou":"plurigrid","rn":"gay-tofu","fn":"plurigrid/gay-tofu","lang":"HTML","s":0,"f":0,"oi":0,"pa":"2026-01-08T15:14:34Z","d":"Low-discrepancy color sequences for TOFU"},
{"ou":"plurigrid","rn":"lazygay","fn":"plurigrid/lazygay","lang":"Go","s":0,"f":0,"oi":0,"pa":"2026-01-08T14:19:25Z","d":"lazygit fork with Gay.jl commit coloring"},
{"ou":"plurigrid","rn":"gay-terminal","fn":"plurigrid/gay-terminal","lang":"Rust","s":0,"f":0,"oi":0,"pa":"2026-01-08T14:19:24Z","d":"Terminal ANSI coloring with Gay.jl"},
{"ou":"plurigrid","rn":"gay-go","fn":"plurigrid/gay-go","lang":"Go","s":0,"f":0,"oi":0,"pa":"2026-01-08T14:19:23Z","d":"Go implementation of Gay.jl coloring"},
{"ou":"plurigrid","rn":"gay-rs","fn":"plurigrid/gay-rs","lang":"Rust","s":0,"f":0,"oi":0,"pa":"2026-01-08T14:19:22Z","d":"Rust crate for Gay.jl GF(3) trits"},
{"ou":"plurigrid","rn":"lazybjj","fn":"plurigrid/lazybjj","lang":"Rust","s":0,"f":0,"oi":0,"pa":"2026-01-08T14:19:19Z","d":"TUI for jj with Gay.jl GF(3) coloring"},
{"ou":"plurigrid","rn":"agent-o-rama","fn":"plurigrid/agent-o-rama","lang":"Clojure","s":0,"f":0,"oi":0,"pa":"2026-01-02T01:09:22Z","d":None},
{"ou":"plurigrid","rn":"aptos-wallet-ruby","fn":"plurigrid/aptos-wallet-ruby","lang":"Ruby","s":1,"f":0,"oi":0,"pa":"2025-09-30T22:47:22Z","d":None},
{"ou":"plurigrid","rn":"duck-kanban","fn":"plurigrid/duck-kanban","lang":"Rust","s":1,"f":0,"oi":0,"pa":"2025-09-26T20:18:38Z","d":"Duck intelligence kanban"},
{"ou":"plurigrid","rn":"ontology","fn":"plurigrid/ontology","lang":"JavaScript","s":8,"f":9,"oi":16,"pa":"2025-05-27T18:18:34Z","d":"autopoietic ergodicity"},
{"ou":"plurigrid","rn":"Plurigraph","fn":"plurigrid/Plurigraph","lang":"JavaScript","s":3,"f":5,"oi":4,"pa":"2025-01-05T08:39:09Z","d":"Plurigrid knowledge base for Obsidian"},
{"ou":"plurigrid","rn":"act","fn":"plurigrid/act","lang":"Python","s":3,"f":1,"oi":4,"pa":"2024-07-26T08:27:08Z","d":"cognitive category theory building blocks"},
{"ou":"plurigrid","rn":"StochFlow","fn":"plurigrid/StochFlow","lang":"Python","s":4,"f":1,"oi":0,"pa":"2024-03-20T23:34:57Z","d":"Stochastic interpolant models"},
{"ou":"plurigrid","rn":"microworlds","fn":"plurigrid/microworlds","lang":"Rust","s":3,"f":5,"oi":3,"pa":"2023-05-13T03:54:56Z","d":"microworlds"},
{"ou":"plurigrid","rn":"vcg-auction","fn":"plurigrid/vcg-auction","lang":"Rust","s":7,"f":2,"oi":1,"pa":"2023-03-16T21:53:08Z","d":"VCG auction contract"},
{"ou":"plurigrid","rn":"agent","fn":"plurigrid/agent","lang":"Python","s":5,"f":1,"oi":6,"pa":"2023-03-31T18:45:23Z","d":"Agency amplification framework"},
# zubyul
{"ou":"zubyul","rn":"voice-observatory","fn":"zubyul/voice-observatory","lang":"Python","s":0,"f":0,"oi":0,"pa":"2026-04-24T05:56:17Z","d":"Passive macOS TUI observing voice-download pathways"},
{"ou":"zubyul","rn":"ghostel-emacs-worlds","fn":"zubyul/ghostel-emacs-worlds","lang":"GLSL","s":0,"f":0,"oi":0,"pa":"2026-04-24T00:20:56Z","d":"Ghostty config + emacs-mods"},
{"ou":"zubyul","rn":"nash-tui","fn":"zubyul/nash-tui","lang":"Rust","s":0,"f":0,"oi":0,"pa":"2026-04-13T07:45:16Z","d":"NASH token TUI"},
{"ou":"zubyul","rn":"nash-web","fn":"zubyul/nash-web","lang":"Rust","s":0,"f":0,"oi":0,"pa":"2026-04-13T07:08:58Z","d":"NASH token browser TUI"},
{"ou":"zubyul","rn":"big-bad-plurigrid-quiz","fn":"zubyul/big-bad-plurigrid-quiz","lang":"Emacs Lisp","s":0,"f":0,"oi":0,"pa":"2026-04-09T18:51:31Z","d":"27 flashcards from recent activity"},
{"ou":"zubyul","rn":"Gay.jl","fn":"zubyul/Gay.jl","lang":"Julia","s":0,"f":0,"oi":0,"pa":"2026-03-28T11:30:01Z","d":"Wide-gamut color sampling with splittable determinism"},
{"ou":"zubyul","rn":"kinesis-kb360pro","fn":"zubyul/kinesis-kb360pro","lang":"Python","s":0,"f":0,"oi":0,"pa":"2026-03-26T10:29:40Z","d":"Claude Code skill for Kinesis Advantage360 Pro"},
{"ou":"zubyul","rn":"gay-world","fn":"zubyul/gay-world","lang":"Python","s":1,"f":1,"oi":0,"pa":"2026-03-26T04:03:39Z","d":"Goblin world builder"},
{"ou":"zubyul","rn":"tilelang-kernels","fn":"zubyul/tilelang-kernels","lang":"Python","s":0,"f":0,"oi":0,"pa":"2026-03-16T02:31:13Z","d":"TileLang GPU kernels for GF(3)"},
{"ou":"zubyul","rn":"gay-terminal-colors","fn":"zubyul/gay-terminal-colors","lang":"Clojure","s":0,"f":0,"oi":0,"pa":"2026-02-21T07:38:14Z","d":"Gay.jl world_terminal_fingerprint"},
{"ou":"zubyul","rn":"basin","fn":"zubyul/basin","lang":"Rust","s":0,"f":0,"oi":0,"pa":"2026-02-13T10:31:47Z","d":None},
{"ou":"zubyul","rn":"openbci-visualizer","fn":"zubyul/openbci-visualizer","lang":"Zig","s":0,"f":0,"oi":0,"pa":"2026-02-04T11:17:41Z","d":None},
{"ou":"zubyul","rn":"plurigrid-site","fn":"zubyul/plurigrid-site","lang":"Svelte","s":0,"f":1,"oi":11,"pa":"2026-02-04T03:20:08Z","d":"Plurigrid world: site deployment"},
{"ou":"zubyul","rn":"vibesnipe","fn":"zubyul/vibesnipe","lang":"Move","s":0,"f":0,"oi":1,"pa":"2026-01-30T22:36:03Z","d":None},
{"ou":"zubyul","rn":"zubyul.github.io","fn":"zubyul/zubyul.github.io","lang":"CSS","s":1,"f":0,"oi":0,"pa":"2026-01-27T03:24:34Z","d":None},
{"ou":"zubyul","rn":"toad-warpify-extension","fn":"zubyul/toad-warpify-extension","lang":"Python","s":0,"f":0,"oi":0,"pa":"2026-01-17T07:48:40Z","d":"Warpify extension for Toad"},
{"ou":"zubyul","rn":"cat-world","fn":"zubyul/cat-world","lang":"TypeScript","s":0,"f":0,"oi":0,"pa":"2025-12-12T08:47:14Z","d":"Cat gaze tracker"},
{"ou":"zubyul","rn":"chromatic-vrf","fn":"zubyul/chromatic-vrf","lang":"Kotlin","s":0,"f":0,"oi":0,"pa":"2025-12-12T03:26:22Z","d":"Chromatic VRF: I Love Hue puzzle"},
{"ou":"zubyul","rn":"quantum-telephone","fn":"zubyul/quantum-telephone","lang":"Jupyter Notebook","s":0,"f":0,"oi":0,"pa":"2025-12-08T22:54:16Z","d":"Quantum telephone world"},
{"ou":"zubyul","rn":"c-elegans-connectome","fn":"zubyul/c-elegans-connectome","lang":"JavaScript","s":0,"f":0,"oi":0,"pa":"2025-11-22T15:43:55Z","d":None},
{"ou":"zubyul","rn":"cascade-world","fn":"zubyul/cascade-world","lang":"Python","s":1,"f":0,"oi":0,"pa":"2025-09-19T18:25:12Z","d":"Cascade development environment"},
{"ou":"zubyul","rn":"ghostty-modifications","fn":"zubyul/ghostty-modifications","lang":"JavaScript","s":1,"f":0,"oi":0,"pa":"2025-09-15T02:45:21Z","d":"Ghostty terminal modifications"},
{"ou":"zubyul","rn":"GoofyLifeChoices","fn":"zubyul/GoofyLifeChoices","lang":"Python","s":1,"f":0,"oi":0,"pa":"2025-07-30T18:48:13Z","d":None},
{"ou":"zubyul","rn":"GayMove","fn":"zubyul/GayMove","lang":"Move","s":0,"f":0,"oi":0,"pa":"2025-12-18T09:40:08Z","d":None},
{"ou":"zubyul","rn":"jonikas_lab_data_analysis_misc","fn":"zubyul/jonikas_lab_data_analysis_misc","lang":"Jupyter Notebook","s":2,"f":0,"oi":0,"pa":"2023-08-16T20:24:40Z","d":"scripts to process large genetic sequence data"},
{"ou":"zubyul","rn":"WGCNA","fn":"zubyul/WGCNA","lang":"HTML","s":2,"f":0,"oi":0,"pa":"2023-07-05T18:02:30Z","d":"weighted gene correlation network analysis"},
{"ou":"zubyul","rn":"Nikolova_lab_data_analysis","fn":"zubyul/Nikolova_lab_data_analysis","lang":"R","s":2,"f":0,"oi":0,"pa":"2023-06-16T13:56:58Z","d":"cortical thickness and transcription factors"},
# migalkin
{"ou":"migalkin","rn":"NodePiece","fn":"migalkin/NodePiece","lang":"Python","s":144,"f":21,"oi":0,"pa":"2022-02-02T03:34:04Z","d":"Compositional Representations for Large KGs (ICLR'22)"},
{"ou":"migalkin","rn":"StarE","fn":"migalkin/StarE","lang":"Python","s":89,"f":16,"oi":1,"pa":"2023-12-01T20:12:24Z","d":"Message Passing for Hyper-Relational KGs (EMNLP 2020)"},
{"ou":"migalkin","rn":"kgcourse2021","fn":"migalkin/kgcourse2021","lang":"HTML","s":25,"f":9,"oi":0,"pa":"2025-08-04T03:01:46Z","d":"Knowledge Graphs course materials"},
{"ou":"migalkin","rn":"NBFNet_mlx","fn":"migalkin/NBFNet_mlx","lang":"Python","s":10,"f":1,"oi":1,"pa":"2024-03-02T00:15:23Z","d":"Neural Bellman-Ford in MLX for Apple Silicon"},
{"ou":"migalkin","rn":"RWL","fn":"migalkin/RWL","lang":"Python","s":8,"f":1,"oi":0,"pa":"2022-12-01T15:58:59Z","d":"Weisfeiler and Leman Go Relational (LOG 2022)"},
{"ou":"migalkin","rn":"rambo","fn":"migalkin/rambo","lang":"Rust","s":3,"f":0,"oi":1,"pa":"2023-02-08T14:27:03Z","d":None},
{"ou":"migalkin","rn":"SMJoin-experiments","fn":"migalkin/SMJoin-experiments","lang":"R","s":1,"f":0,"oi":0,"pa":"2017-06-06T12:20:23Z","d":"ISWC 2017 SMJoin results"},
# wasita
{"ou":"wasita","rn":"wasita.github.io","fn":"wasita/wasita.github.io","lang":"Svelte","s":1,"f":0,"oi":8,"pa":"2026-06-01T04:15:56Z","d":"personal website"},
{"ou":"wasita","rn":"wm-cv","fn":"wasita/wm-cv","lang":"Svelte","s":0,"f":0,"oi":0,"pa":"2026-05-13T05:29:04Z","d":"Academic CV as single page web app"},
{"ou":"wasita","rn":"vocoder","fn":"wasita/vocoder","lang":"JavaScript","s":0,"f":0,"oi":0,"pa":"2026-05-06T05:14:00Z","d":None},
{"ou":"wasita","rn":"magic-garden","fn":"wasita/magic-garden","lang":"Python","s":2,"f":1,"oi":1,"pa":"2026-01-13T23:51:32Z","d":"bot for magic garden discord"},
{"ou":"wasita","rn":"send2kobo","fn":"wasita/send2kobo","lang":"TypeScript","s":1,"f":0,"oi":0,"pa":"2025-12-12T19:09:12Z","d":"Website for sending books to kobo"},
{"ou":"wasita","rn":"wins-search","fn":"wasita/wins-search","lang":"CSS","s":1,"f":0,"oi":0,"pa":"2022-12-14T22:17:32Z","d":"Women in Network Science member list"},
# DJedamski
{"ou":"DJedamski","rn":"kaggle_ncaa18","fn":"DJedamski/kaggle_ncaa18","lang":"Jupyter Notebook","s":0,"f":0,"oi":0,"pa":"2018-03-07T12:36:09Z","d":"NCAA March Madness competition (2018)"},
{"ou":"DJedamski","rn":"Project_Euler","fn":"DJedamski/Project_Euler","lang":None,"s":0,"f":0,"oi":0,"pa":"2015-10-14T02:10:45Z","d":None},
{"ou":"DJedamski","rn":"EDA","fn":"DJedamski/EDA","lang":"R","s":0,"f":0,"oi":0,"pa":"2014-11-09T16:51:34Z","d":"Coursera Project"},
{"ou":"DJedamski","rn":"Kaggle","fn":"DJedamski/Kaggle","lang":None,"s":1,"f":0,"oi":0,"pa":"2014-11-03T02:22:01Z","d":None},
{"ou":"DJedamski","rn":"Getting-and-Cleaning-Data","fn":"DJedamski/Getting-and-Cleaning-Data","lang":"R","s":1,"f":0,"oi":0,"pa":"2014-10-26T20:53:14Z","d":"Coursera Project"},
{"ou":"DJedamski","rn":"School","fn":"DJedamski/School","lang":"R","s":1,"f":1,"oi":0,"pa":"2014-10-09T02:55:13Z","d":"grad school projects"},
# kristinezheng
{"ou":"kristinezheng","rn":"kristinezheng.github.io","fn":"kristinezheng/kristinezheng.github.io","lang":"HTML","s":0,"f":0,"oi":0,"pa":"2026-05-14T22:28:57Z","d":None},
{"ou":"kristinezheng","rn":"lookit-jenga","fn":"kristinezheng/lookit-jenga","lang":"Jupyter Notebook","s":0,"f":0,"oi":0,"pa":"2024-05-16T18:29:01Z","d":"Lookit study for 9.85"},
{"ou":"kristinezheng","rn":"auditory-illusion","fn":"kristinezheng/auditory-illusion","lang":"CSS","s":0,"f":0,"oi":0,"pa":"2022-03-11T19:22:33Z","d":"9.35 auditory illusion"},
{"ou":"kristinezheng","rn":"graph_example","fn":"kristinezheng/graph_example","lang":"Python","s":0,"f":0,"oi":0,"pa":"2021-10-08T07:29:51Z","d":None},
{"ou":"kristinezheng","rn":"Green-Machine","fn":"kristinezheng/Green-Machine","lang":"Python","s":0,"f":0,"oi":0,"pa":"2021-09-19T05:33:01Z","d":"HackMIT 2021: Sustainability Track"},
# M1shaaa
{"ou":"M1shaaa","rn":"M1shaaa","fn":"M1shaaa/M1shaaa","lang":None,"s":0,"f":0,"oi":0,"pa":"2026-06-07T03:33:05Z","d":"Config files for GitHub profile"},
{"ou":"M1shaaa","rn":"lab-bookshelf-","fn":"M1shaaa/lab-bookshelf-","lang":"TypeScript","s":0,"f":0,"oi":0,"pa":"2024-12-31T05:11:14Z","d":None},
{"ou":"M1shaaa","rn":"rosie-s-study-3-lookit-project","fn":"M1shaaa/rosie-s-study-3-lookit-project","lang":None,"s":0,"f":0,"oi":0,"pa":"2024-11-04T22:15:35Z","d":None},
{"ou":"M1shaaa","rn":"Python-Lookit-Uploads","fn":"M1shaaa/Python-Lookit-Uploads","lang":"Python","s":0,"f":0,"oi":0,"pa":"2024-02-16T15:20:50Z","d":"random projects"},
{"ou":"M1shaaa","rn":"Classes","fn":"M1shaaa/Classes","lang":None,"s":0,"f":0,"oi":0,"pa":"2023-12-07T08:16:20Z","d":None},
{"ou":"M1shaaa","rn":"MNIST-Classifier","fn":"M1shaaa/MNIST-Classifier","lang":None,"s":0,"f":0,"oi":0,"pa":"2023-11-28T06:12:13Z","d":None},
{"ou":"M1shaaa","rn":"Lookit-Demo","fn":"M1shaaa/Lookit-Demo","lang":None,"s":0,"f":0,"oi":0,"pa":"2023-04-10T02:50:03Z","d":None},
{"ou":"M1shaaa","rn":"Yale-Work","fn":"M1shaaa/Yale-Work","lang":"HTML","s":0,"f":0,"oi":0,"pa":"2023-12-06T18:33:10Z","d":None},
# AustinCStone
{"ou":"AustinCStone","rn":"TextGAN","fn":"AustinCStone/TextGAN","lang":"Python","s":92,"f":30,"oi":5,"pa":"2016-10-04T03:19:12Z","d":"GAN for text generation in TensorFlow"},
{"ou":"AustinCStone","rn":"StereoVisionMRF","fn":"AustinCStone/StereoVisionMRF","lang":"Python","s":11,"f":4,"oi":0,"pa":"2016-01-10T08:34:29Z","d":"MRF with loopy belief propagation for depth"},
{"ou":"AustinCStone","rn":"SpectralClustering","fn":"AustinCStone/SpectralClustering","lang":"Python","s":3,"f":2,"oi":0,"pa":"2015-11-09T03:27:15Z","d":"Spectral clustering implementation"},
{"ou":"AustinCStone","rn":"StructureFromMotion","fn":"AustinCStone/StructureFromMotion","lang":"Python","s":1,"f":0,"oi":0,"pa":"2018-06-10T18:56:16Z","d":"Recover 3D geometry from videos"},
{"ou":"AustinCStone","rn":"EpsteinSearch","fn":"AustinCStone/EpsteinSearch","lang":"Python","s":0,"f":0,"oi":0,"pa":"2026-02-11T01:10:54Z","d":None},
{"ou":"AustinCStone","rn":"bmforkupdate","fn":"AustinCStone/bmforkupdate","lang":"Python","s":0,"f":0,"oi":0,"pa":"2025-05-09T04:49:24Z","d":None},
{"ou":"AustinCStone","rn":"TFBirds","fn":"AustinCStone/TFBirds","lang":"Python","s":0,"f":0,"oi":0,"pa":"2019-01-30T08:07:21Z","d":"Bird flocking simulator in TensorFlow"},
{"ou":"AustinCStone","rn":"LensBuilder","fn":"AustinCStone/LensBuilder","lang":"Python","s":0,"f":0,"oi":0,"pa":"2019-04-04T04:28:05Z","d":"WIP optimize for focusing lens"},
{"ou":"AustinCStone","rn":"logisticRegressionHaskell","fn":"AustinCStone/logisticRegressionHaskell","lang":"Haskell","s":1,"f":0,"oi":0,"pa":"2015-06-07T19:37:42Z","d":"Logistic regression in Haskell"},
{"ou":"AustinCStone","rn":"Connectomics","fn":"AustinCStone/Connectomics","lang":"TeX","s":0,"f":0,"oi":0,"pa":"2014-05-11T05:30:07Z","d":"2013-2014 Kaggle Connectomics Challenge"},
]

con.execute("DELETE FROM repo_snapshots")
for i, r in enumerate(REPOS, start=1):
    trit, color, name = gf3(i)
    # find increment_id by matching source
    inc = con.execute("SELECT id FROM world_increments WHERE source_name=? LIMIT 1", [r["ou"]]).fetchone()
    inc_id = inc[0] if inc else 1
    con.execute("""INSERT INTO repo_snapshots VALUES (?,now(),?,?,?,?,?,?,?,?,?,?)""",
                [i, inc_id, r["ou"], r["rn"], r["fn"], r["lang"],
                 r["s"], r["f"], r["oi"], r["pa"], r["d"]])

# ── Aptos snapshots ──────────────────────────────────────────────────────────
APTOS = [
  {"w":"alice","a":"0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b","b":0.0},
  {"w":"bob","a":"0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d","b":0.0},
  {"w":"A","a":"0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a","b":0.0},
  {"w":"B","a":"0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13","b":0.0},
  {"w":"C","a":"0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e","b":0.0},
  {"w":"D","a":"0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1","b":0.0},
  {"w":"E","a":"0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36","b":0.0},
  {"w":"F","a":"0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71","b":0.0},
  {"w":"G","a":"0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32","b":0.0},
  {"w":"H","a":"0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f","b":0.0},
  {"w":"I","a":"0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9","b":0.0},
  {"w":"J","a":"0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54","b":0.0},
  {"w":"K","a":"0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4","b":0.0},
  {"w":"L","a":"0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9","b":0.0},
  {"w":"M","a":"0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9","b":0.0},
  {"w":"N","a":"0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c","b":0.0},
  {"w":"O","a":"0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d","b":0.0},
  {"w":"P","a":"0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948","b":0.0},
  {"w":"Q","a":"0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9","b":0.0},
  {"w":"R","a":"0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10","b":0.0},
  {"w":"S","a":"0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386","b":0.0},
  {"w":"T","a":"0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588","b":0.0},
  {"w":"U","a":"0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956","b":0.0},
  {"w":"V","a":"0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3","b":0.0},
  {"w":"W","a":"0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0","b":0.0},
  {"w":"X","a":"0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d","b":0.0},
  {"w":"Y","a":"0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4","b":0.0},
  {"w":"Z","a":"0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c","b":0.0},
]
con.execute("DELETE FROM aptos_snapshots")
for a in APTOS:
    con.execute("INSERT INTO aptos_snapshots VALUES (now(),?,?,?)", [a["w"], a["a"], a["b"]])

# ── Multisig probes ──────────────────────────────────────────────────────────
MULTISIG = [
  {"p":"A-B","a":"0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003","s":2,"h":True},
  {"p":"A-G","a":"0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096","s":2,"h":True},
  {"p":"Y-Z","a":"0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883","s":2,"h":True},
  {"p":"S-T","a":"0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883","s":2,"h":True},
  {"p":"V-W","a":"0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d","s":2,"h":True},
]
con.execute("DELETE FROM multisig_probes")
for m in MULTISIG:
    con.execute("INSERT INTO multisig_probes VALUES (now(),?,?,?,?)", [m["p"], m["a"], m["s"], m["h"]])

# ── MNX snapshots (unavailable - Vercel auth required) ──────────────────────
# no rows inserted

con.close()
print(f"Done. {len(REPOS)} repos, {len(APTOS)} Aptos wallets, {len(MULTISIG)} multisig probes.")
