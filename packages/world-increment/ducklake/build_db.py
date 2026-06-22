#!/usr/bin/env python3
"""Build world-increments DuckDB from sweep data."""
import duckdb
import hashlib
import json
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

# GF3 helper
def gf3(idx):
    t = idx % 3
    if t == 0:
        return (0, "#d3869b", "ERGODIC")
    elif t == 1:
        return (1, "#b8bb26", "PLUS")
    else:
        return (-1, "#cc241d", "MINUS")

def sha8(s):
    return hashlib.sha256(s.encode()).hexdigest()[:8]

# ── REPO DATA ────────────────────────────────────────────────────────────────

repos_raw = {
  "plurigrid": [
    ('plurigrid','asi','plurigrid/asi','HTML',26,8,4,'2026-06-10T12:51:42Z','everything is topological chemputer!'),
    ('plurigrid','place','plurigrid/place','TeX',1,1,9,'2026-06-20T00:28:26Z',None),
    ('plurigrid','eirobri','plurigrid/eirobri','Clojure',0,0,29,'2026-06-03T20:43:46Z','EiRoBri replay world'),
    ('plurigrid','nash-portal','plurigrid/nash-portal','Rust',2,3,1,'2026-05-19T01:49:59Z','NASH token TUI in the browser'),
    ('plurigrid','gorj','plurigrid/gorj','Clojure',0,0,730,'2026-06-21T23:12:12Z','forj + Rama topology nREPL routing + GF(3) gay trit coloring'),
    ('plurigrid','zig-syrup','plurigrid/zig-syrup','Zig',2,2,0,'2026-04-30T03:52:16Z','High-performance Zig OCapN Syrup'),
    ('plurigrid','asi-skills','plurigrid/asi-skills','Julia',3,0,0,'2026-04-26T08:09:26Z','69 skills with Galois Hole Type'),
    ('plurigrid','bci-blue-share','plurigrid/bci-blue-share','JavaScript',0,0,0,'2026-04-26T07:08:03Z','BCI signal infrastructure'),
    ('plurigrid','nanoclj-zig','plurigrid/nanoclj-zig','Zig',1,1,20,'2026-04-25T07:29:09Z','NaN-boxed Clojure interpreter in Zig'),
    ('plurigrid','spi-race','plurigrid/spi-race','Swift',0,0,0,'2026-04-21T19:31:56Z','Splitmix Parallel Integrity'),
    ('plurigrid','reafference','plurigrid/reafference','HTML',0,0,0,'2026-04-16T05:21:49Z','Reafference adaptation workspace'),
    ('plurigrid','web-browser','plurigrid/web-browser','Rust',0,0,0,'2026-04-10T02:54:47Z','web-browser from prepostweb lineage'),
    ('plurigrid','vivarium','plurigrid/vivarium','Clojure',1,0,0,'2026-04-08T08:38:37Z',None),
    ('plurigrid','flowglad-rs','plurigrid/flowglad-rs','Rust',0,0,0,'2026-04-08T07:56:15Z',None),
    ('plurigrid','tree-sitter-nanoclj-zig','plurigrid/tree-sitter-nanoclj-zig','C',0,0,0,'2026-04-04T07:48:21Z','Tree-sitter grammar for nanoclj-zig'),
    ('plurigrid','forester','plurigrid/forester','XSLT',0,0,0,'2026-03-30T01:32:26Z','CatColab mathematical documentation forest'),
    ('plurigrid','gatomic','plurigrid/gatomic','Clojure',0,0,0,'2026-03-30T00:54:48Z','Deterministic color identity store'),
    ('plurigrid','blue','plurigrid/blue','TeX',0,0,0,'2026-03-29T23:06:32Z',None),
    ('plurigrid','red','plurigrid/red',None,0,0,0,'2026-03-29T22:58:46Z',None),
    ('plurigrid','nblm-flashcards','plurigrid/nblm-flashcards','Hy',0,0,0,'2026-03-26T08:23:01Z','NotebookLM Enterprise flashcard pipeline'),
    ('plurigrid','gemini-agent','plurigrid/gemini-agent','Python',0,0,0,'2026-02-19T06:39:16Z',None),
    ('plurigrid','graded-optic','plurigrid/graded-optic','Haskell',0,0,0,'2026-02-08T16:10:16Z','Semiring-graded bidirectional processes'),
    ('plurigrid','json-canvas','plurigrid/json-canvas',None,0,0,0,'2026-02-06T06:50:57Z','JSON Canvas'),
    ('plurigrid','shepherd','plurigrid/shepherd','Scheme',0,0,0,'2026-01-23T07:47:28Z','Spritely Shepherd'),
    ('plurigrid','goblinshare','plurigrid/goblinshare','Scheme',0,0,0,'2026-01-23T07:47:12Z','P2P filesharing demo for Goblins'),
    ('plurigrid','magenc','plurigrid/magenc','Scheme',0,0,0,'2026-01-23T07:47:11Z','Magenc Magnet URIs'),
    ('plurigrid','hoot','plurigrid/hoot','Scheme',0,0,1,'2026-01-23T07:47:10Z','Spritely Hoot - Scheme to WebAssembly'),
    ('plurigrid','leprechauns','plurigrid/leprechauns','Racket',0,0,0,'2026-01-23T07:46:46Z','Spritely Goblins + Gay.jl'),
    ('plurigrid','spritely-semantic-colors','plurigrid/spritely-semantic-colors',None,0,0,0,'2026-01-23T07:38:32Z','Deterministic color mappings for Spritely'),
    ('plurigrid','gay-tofu','plurigrid/gay-tofu','HTML',0,0,0,'2026-01-08T15:14:34Z','Low-discrepancy color sequences'),
    ('plurigrid','lazygay','plurigrid/lazygay','Go',0,0,0,'2026-01-08T14:19:25Z','lazygit fork with Gay.jl'),
    ('plurigrid','gay-terminal','plurigrid/gay-terminal','Rust',0,0,0,'2026-01-08T14:19:24Z','Terminal ANSI coloring'),
    ('plurigrid','gay-go','plurigrid/gay-go','Go',0,0,0,'2026-01-08T14:19:23Z','Go implementation of Gay.jl'),
    ('plurigrid','gay-rs','plurigrid/gay-rs','Rust',0,0,0,'2026-01-08T14:19:22Z','Rust crate for Gay.jl'),
    ('plurigrid','lazybjj','plurigrid/lazybjj','Rust',0,0,0,'2026-01-08T14:19:19Z','TUI for jj with Gay.jl GF(3) coloring'),
    ('plurigrid','agent-o-rama','plurigrid/agent-o-rama','Clojure',0,0,0,'2026-01-02T01:09:22Z',None),
    ('plurigrid','aptos-wallet-ruby','plurigrid/aptos-wallet-ruby','Ruby',1,0,0,'2025-09-30T22:47:22Z',None),
    ('plurigrid','duck-kanban','plurigrid/duck-kanban','Rust',1,0,0,'2025-09-26T20:18:38Z','Duck intelligence kanban'),
    ('plurigrid','ontology','plurigrid/ontology','JavaScript',8,9,16,'2025-05-27T18:18:34Z','autopoietic ergodicity'),
    ('plurigrid','Plurigraph','plurigrid/Plurigraph','JavaScript',3,5,4,'2025-01-05T08:39:09Z','Plurigrid knowledge base'),
    ('plurigrid','act','plurigrid/act','Python',3,1,4,'2024-07-26T08:27:08Z','building blocks for cognitive category theory'),
    ('plurigrid','StochFlow','plurigrid/StochFlow','Python',4,1,0,'2024-03-20T23:34:57Z','stochastic interpolant models'),
    ('plurigrid','microworlds','plurigrid/microworlds','Rust',3,5,3,'2023-05-13T03:54:56Z','👽'),
    ('plurigrid','agent','plurigrid/agent','Python',5,1,6,'2023-03-31T18:45:23Z','Framework for agency amplification'),
    ('plurigrid','vcg-auction','plurigrid/vcg-auction','Rust',7,2,1,'2023-03-16T21:53:08Z','VCG auction contract'),
    ('plurigrid','grid','plurigrid/grid','TypeScript',2,1,1,'2023-01-02T11:55:55Z','Plurigrid Testnet #0'),
  ],
  "kubeflow": [
    ('kubeflow','katib','kubeflow/katib','Python',1684,528,116,'2026-06-20T23:29:45Z','Automated Machine Learning on Kubernetes'),
    ('kubeflow','pipelines','kubeflow/pipelines','Python',4156,2009,449,'2026-06-20T19:12:02Z','Machine Learning Pipelines for Kubeflow'),
    ('kubeflow','notebooks','kubeflow/notebooks',None,73,125,184,'2026-06-20T17:12:47Z','Kubeflow Notebooks'),
    ('kubeflow','mcp-apache-spark-history-server','kubeflow/mcp-apache-spark-history-server','Python',177,65,21,'2026-06-19T21:20:08Z','MCP Server for Apache Spark History Server'),
    ('kubeflow','trainer','kubeflow/trainer','Go',2118,971,119,'2026-06-19T15:46:05Z','Distributed AI Model Training on Kubernetes'),
    ('kubeflow','community','kubeflow/community','Jupyter Notebook',194,264,15,'2026-06-19T16:50:40Z','Kubeflow community'),
    ('kubeflow','spark-operator','kubeflow/spark-operator','Python',3127,1490,104,'2026-06-18T15:39:22Z','Kubernetes operator for Apache Spark'),
    ('kubeflow','kubeflow','kubeflow/kubeflow',None,15739,2680,0,'2026-06-18T11:45:16Z','Machine Learning Toolkit for Kubernetes'),
    ('kubeflow','dashboard','kubeflow/dashboard','TypeScript',16,59,80,'2026-06-21T00:56:24Z','Kubeflow Central Dashboard'),
    ('kubeflow','hub','kubeflow/hub','Go',173,183,39,'2026-06-20T15:40:26Z','Model Registry'),
    ('kubeflow','community-distribution','kubeflow/community-distribution','YAML',1026,1065,21,'2026-06-18T19:10:25Z','Kubeflow Community Distribution'),
    ('kubeflow','kale','kubeflow/kale','Python',694,155,55,'2026-06-20T11:20:36Z','Kubeflow superfood for Data Scientists'),
    ('kubeflow','sdk','kubeflow/sdk','Python',120,180,133,'2026-06-20T03:05:26Z','Universal Python SDK'),
    ('kubeflow','mpi-operator','kubeflow/mpi-operator','Go',528,236,106,'2026-06-15T13:03:34Z','Kubernetes Operator for MPI'),
    ('kubeflow','arena','kubeflow/arena','Go',813,190,43,'2026-05-07T06:46:17Z','A CLI for Kubeflow'),
    ('kubeflow','examples','kubeflow/examples','Jsonnet',1460,756,111,'2025-04-14T01:54:52Z','Extended examples and tutorials'),
    ('kubeflow','kfp-tekton','kubeflow/kfp-tekton','TypeScript',182,123,79,'2024-11-19T12:23:51Z','Kubeflow Pipelines on Tekton'),
    ('kubeflow','fairing','kubeflow/fairing','Jsonnet',337,143,134,'2022-04-11T05:28:47Z','Python SDK for building and deploying ML'),
    ('kubeflow','kfctl','kubeflow/kfctl','Go',182,134,94,'2023-08-15T20:19:22Z','CLI for deploying Kubeflow'),
    ('kubeflow','pytorch-operator','kubeflow/pytorch-operator','Jsonnet',310,143,63,'2021-12-01T17:44:48Z','PyTorch on Kubernetes'),
  ],
  "TeglonLabs": [
    ('TeglonLabs','jank-crane','TeglonLabs/jank-crane','C++',0,0,0,'2026-06-08T19:03:03Z','crane-jank converged-IR hub'),
    ('TeglonLabs','mathpix-gem','TeglonLabs/mathpix-gem','Ruby',2,0,11,'2026-01-01T12:13:13Z','Transform mathematical images to LaTeX'),
    ('TeglonLabs','coin-flip-mcp','TeglonLabs/coin-flip-mcp','JavaScript',0,2,1,'2025-09-21T08:57:27Z','MCP server for flipping coins'),
    ('TeglonLabs','monad-mcp-server','TeglonLabs/monad-mcp-server',None,0,0,0,'2025-05-14T11:36:14Z','Monad MCP Server'),
    ('TeglonLabs','topoi','TeglonLabs/topoi','Python',0,0,1,'2025-01-24T04:49:26Z',None),
  ],
  "bmorphism": [
    ('bmorphism','Gay.jl','bmorphism/Gay.jl','Julia',2,1,187,'2026-06-21T00:43:51Z','Wide-gamut color sampling with splittable determinism'),
    ('bmorphism','satreadout','bmorphism/satreadout','HTML',0,0,0,'2026-06-20T13:05:41Z','Machine-checked saturating non-Riemannian perceptual readout'),
    ('bmorphism','ocaml-mcp-sdk','bmorphism/ocaml-mcp-sdk','OCaml',61,2,0,'2026-03-16T05:24:25Z','OCaml SDK for Model Context Protocol'),
    ('bmorphism','say-mcp-server','bmorphism/say-mcp-server','JavaScript',20,9,3,'2025-01-07T03:15:18Z','MCP server for macOS text-to-speech'),
    ('bmorphism','babashka-mcp-server','bmorphism/babashka-mcp-server','JavaScript',19,6,3,'2025-01-05T11:09:42Z','MCP server for Babashka'),
    ('bmorphism','anti-bullshit-mcp-server','bmorphism/anti-bullshit-mcp-server','JavaScript',23,7,1,'2026-01-16T08:54:58Z','MCP server for analyzing claims'),
    ('bmorphism','manifold-mcp-server','bmorphism/manifold-mcp-server','JavaScript',14,9,5,'2025-01-11T10:36:58Z','MCP server for Manifold Markets'),
    ('bmorphism','penrose-mcp','bmorphism/penrose-mcp','JavaScript',10,4,0,'2025-01-20T21:44:55Z','Penrose server'),
    ('bmorphism','nats-mcp-server','bmorphism/nats-mcp-server',None,7,3,2,'2025-01-06T23:33:41Z','MCP server for NATS messaging'),
    ('bmorphism','marginalia-mcp-server','bmorphism/marginalia-mcp-server','JavaScript',8,6,0,'2025-01-06T05:47:24Z','MCP server for marginalia'),
    ('bmorphism','risc0-cosmwasm-example','bmorphism/risc0-cosmwasm-example','Rust',23,2,1,'2022-10-20T23:50:40Z','CosmWasm + zkVM RISC-V EFI template'),
    ('bmorphism','shitcoin','bmorphism/shitcoin','Python',5,0,0,'2026-04-08T08:07:08Z','cw20 assets for permissionless degeneracy'),
    ('bmorphism','hypernym-mcp-server','bmorphism/hypernym-mcp-server','JavaScript',6,5,0,'2025-04-02T21:21:08Z',None),
    ('bmorphism','penumbra-mcp','bmorphism/penumbra-mcp','JavaScript',5,6,3,'2025-01-07T01:15:23Z','MCP server for Penumbra blockchain'),
    ('bmorphism','open-location-code-zig','bmorphism/open-location-code-zig','Zig',3,0,0,'2025-12-30T19:33:45Z','Open Location Code for Zig'),
    ('bmorphism','vibespace-mcp-go-ternary','bmorphism/vibespace-mcp-go-ternary','HTML',0,1,3,'2026-01-11T12:50:40Z','Go MCP experience with NATS streaming'),
    ('bmorphism','slowtime-mcp-server','bmorphism/slowtime-mcp-server','TypeScript',3,5,6,'2025-01-02T01:23:33Z','MCP server for time-based operations'),
    ('bmorphism','graphistry-mcp','bmorphism/graphistry-mcp','Python',2,0,0,'2025-05-06T17:34:24Z','Graphistry MCP integration'),
    ('bmorphism','krep-mcp-server','bmorphism/krep-mcp-server','JavaScript',1,1,1,'2025-03-19T20:22:46Z','High-performance string search MCP'),
    ('bmorphism','world','bmorphism/world','Python',0,0,0,'2026-06-02T06:49:02Z','Local worlds launcher'),
  ],
  "zubyul": [
    ('zubyul','voice-observatory','zubyul/voice-observatory','Python',0,0,0,'2026-04-24T05:56:17Z','Passive macOS TUI observing voice-download pathways'),
    ('zubyul','ghostel-emacs-worlds','zubyul/ghostel-emacs-worlds','GLSL',0,0,0,'2026-04-24T00:20:56Z','Ghostty config + ghostel family'),
    ('zubyul','nash-tui','zubyul/nash-tui','Rust',0,0,0,'2026-04-13T07:45:16Z','NASH token TUI'),
    ('zubyul','nash-web','zubyul/nash-web','Rust',0,0,0,'2026-04-13T07:08:58Z','NASH token browser TUI via ratzilla WASM'),
    ('zubyul','big-bad-plurigrid-quiz','zubyul/big-bad-plurigrid-quiz','Emacs Lisp',0,0,0,'2026-04-09T18:51:31Z','27 flashcards from recent activity'),
    ('zubyul','Gay.jl','zubyul/Gay.jl','Julia',0,0,0,'2026-03-28T11:30:01Z','Wide-gamut color sampling'),
    ('zubyul','gay-world','zubyul/gay-world','Python',1,1,0,'2026-03-26T04:03:39Z','Goblin world builder'),
    ('zubyul','tilelang-kernels','zubyul/tilelang-kernels','Python',0,0,0,'2026-03-16T02:31:13Z','TileLang GPU kernels'),
    ('zubyul','gay-terminal-colors','zubyul/gay-terminal-colors','Clojure',0,0,0,'2026-02-21T07:38:14Z','Gay.jl world_terminal_fingerprint'),
    ('zubyul','vibesnipe','zubyul/vibesnipe','Move',0,0,1,'2026-01-30T22:36:03Z',None),
    ('zubyul','plurigrid-site','zubyul/plurigrid-site','Svelte',0,1,11,'2026-02-04T03:20:08Z','Plurigrid world: site deployment'),
    ('zubyul','cascade-world','zubyul/cascade-world','Python',1,0,0,'2025-09-19T18:25:12Z','Cascade development environment'),
    ('zubyul','WGCNA','zubyul/WGCNA','HTML',2,0,0,'2023-07-05T18:02:30Z','weighted gene correlation network analysis'),
    ('zubyul','jonikas_lab_data_analysis_misc','zubyul/jonikas_lab_data_analysis_misc','Jupyter Notebook',2,0,0,'2023-08-16T20:24:40Z','process large genetic sequence data'),
    ('zubyul','Nikolova_lab_data_analysis','zubyul/Nikolova_lab_data_analysis','R',2,0,0,'2023-06-16T13:56:58Z','undergraduate thesis HCP data'),
  ],
  "migalkin": [
    ('migalkin','NodePiece','migalkin/NodePiece','Python',144,21,0,'2026-05-07T05:40:02Z','Compositional and Parameter-Efficient Representations (ICLR22)'),
    ('migalkin','StarE','migalkin/StarE','Python',89,16,1,'2026-04-16T14:12:45Z','Message Passing for Hyper-Relational KGs (EMNLP 2020)'),
    ('migalkin','kgcourse2021','migalkin/kgcourse2021','HTML',25,9,0,'2026-02-16T05:16:08Z','Knowledge Graphs course materials'),
    ('migalkin','NBFNet_mlx','migalkin/NBFNet_mlx','Python',10,1,1,'2026-03-11T01:31:21Z','Neural Bellman-Ford networks in MLX'),
    ('migalkin','RWL','migalkin/RWL','Python',8,1,0,'2026-05-28T20:19:20Z','Weisfeiler and Leman Go Relational (LOG 2022)'),
    ('migalkin','rambo','migalkin/rambo','Rust',3,0,1,'2023-02-28T16:37:22Z',None),
    ('migalkin','migalkin.github.io','migalkin/migalkin.github.io','JavaScript',0,0,0,'2025-05-20T23:58:08Z','Github Pages for academic website'),
  ],
  "DJedamski": [
    ('DJedamski','kaggle_ncaa18','DJedamski/kaggle_ncaa18','Jupyter Notebook',0,0,0,'2018-02-26T16:33:24Z','NCAA March Madness 2018'),
    ('DJedamski','Kaggle','DJedamski/Kaggle',None,1,0,0,'2023-04-21T01:42:35Z',None),
    ('DJedamski','Getting-and-Cleaning-Data','DJedamski/Getting-and-Cleaning-Data','R',1,0,0,'2023-04-21T01:42:34Z','Coursera Project'),
    ('DJedamski','School','DJedamski/School','R',1,1,0,'2023-04-21T01:42:33Z','Projects from grad school'),
    ('DJedamski','EDA','DJedamski/EDA','R',0,0,0,'2014-11-09T17:00:39Z','Coursera Project'),
    ('DJedamski','Project_Euler','DJedamski/Project_Euler',None,0,0,0,'2015-09-05T17:13:32Z',None),
  ],
  "wasita": [
    ('wasita','proj-template','wasita/proj-template',None,0,0,0,'2026-06-19T21:22:21Z',None),
    ('wasita','wasita.github.io','wasita/wasita.github.io','Svelte',1,0,8,'2026-06-15T20:14:23Z','personal website'),
    ('wasita','wm-cv','wasita/wm-cv','Svelte',0,0,0,'2026-05-13T05:29:08Z','Academic CV web app'),
    ('wasita','vocoder','wasita/vocoder','JavaScript',0,0,0,'2026-05-06T05:14:03Z',None),
    ('wasita','magic-garden','wasita/magic-garden','Python',2,1,1,'2026-04-22T21:16:43Z','Magic garden Discord bot'),
    ('wasita','send2kobo','wasita/send2kobo','TypeScript',1,0,0,'2026-05-19T02:59:26Z','Website for sending books to kobo'),
    ('wasita','food-diary','wasita/food-diary','Svelte',0,0,0,'2025-12-13T01:06:43Z',None),
    ('wasita','d60-keeb','wasita/d60-keeb',None,0,0,0,'2024-08-26T00:46:25Z',None),
    ('wasita','wins-search','wasita/wins-search','CSS',1,0,0,'2023-06-03T19:01:11Z','Women in Network Science member list'),
    ('wasita','honeycomb-demo','wasita/honeycomb-demo','JavaScript',0,0,0,'2021-12-07T21:38:28Z',None),
  ],
  "kristinezheng": [
    ('kristinezheng','kristinezheng.github.io','kristinezheng/kristinezheng.github.io','HTML',0,0,0,'2026-06-07T22:53:10Z',None),
    ('kristinezheng','lookit-jenga','kristinezheng/lookit-jenga','Jupyter Notebook',0,0,0,'2024-05-16T18:29:05Z','Lookit study for 9.85'),
    ('kristinezheng','auditory-illusion','kristinezheng/auditory-illusion','CSS',0,0,0,'2022-03-07T02:57:44Z','9.35 spring 2022 auditory illusion'),
    ('kristinezheng','Green-Machine','kristinezheng/Green-Machine','Python',0,0,0,'2021-09-19T05:33:04Z','HackMIT 2021 Sustainability Track'),
    ('kristinezheng','graph_example','kristinezheng/graph_example','Python',0,0,0,'2021-10-08T07:29:53Z',None),
  ],
  "M1shaaa": [
    ('M1shaaa','M1shaaa','M1shaaa/M1shaaa',None,0,0,0,'2026-02-04T19:32:04Z','Config files for GitHub profile'),
    ('M1shaaa','lab-bookshelf-','M1shaaa/lab-bookshelf-','TypeScript',0,0,0,'2024-12-31T05:11:18Z',None),
    ('M1shaaa','rosie-s-study-3-lookit-project','M1shaaa/rosie-s-study-3-lookit-project',None,0,0,0,'2024-11-04T22:15:39Z',None),
    ('M1shaaa','Python-Lookit-Uploads','M1shaaa/Python-Lookit-Uploads','Python',0,0,0,'2024-02-15T22:59:37Z','random projects'),
    ('M1shaaa','Yale-Work','M1shaaa/Yale-Work','HTML',0,0,0,'2023-12-06T18:33:14Z',None),
    ('M1shaaa','Classes','M1shaaa/Classes',None,0,0,0,'2023-12-06T18:20:27Z',None),
    ('M1shaaa','MNIST-Classifier','M1shaaa/MNIST-Classifier',None,0,0,0,'2023-11-28T06:10:47Z',None),
    ('M1shaaa','Lookit-Demo','M1shaaa/Lookit-Demo',None,0,0,0,'2023-04-10T02:44:01Z',None),
  ],
  "AustinCStone": [
    ('AustinCStone','TextGAN','AustinCStone/TextGAN','Python',92,30,5,'2025-03-03T13:26:32Z','Generative adversarial network for text'),
    ('AustinCStone','StereoVisionMRF','AustinCStone/StereoVisionMRF','Python',11,4,0,'2026-04-01T07:39:41Z','MRF for depth inference from stereo images'),
    ('AustinCStone','SpectralClustering','AustinCStone/SpectralClustering','Python',3,2,0,'2021-04-16T08:36:36Z','Spectral clustering homework'),
    ('AustinCStone','EpsteinSearch','AustinCStone/EpsteinSearch','Python',0,0,0,'2026-02-11T01:10:57Z',None),
    ('AustinCStone','bmfork','AustinCStone/bmfork','Python',0,0,1,'2025-05-09T04:18:54Z',None),
    ('AustinCStone','bmforkupdate','AustinCStone/bmforkupdate','Python',0,0,0,'2025-05-09T04:50:16Z',None),
    ('AustinCStone','logisticRegressionHaskell','AustinCStone/logisticRegressionHaskell','Haskell',1,0,0,'2018-02-02T13:34:28Z','Logistic regression in Haskell'),
    ('AustinCStone','StructureFromMotion','AustinCStone/StructureFromMotion','Python',1,0,0,'2019-04-26T19:43:12Z','Recover 3D geometry from videos'),
    ('AustinCStone','stonks','AustinCStone/stonks','Python',0,0,0,'2020-09-04T22:54:35Z','Option calculations'),
    ('AustinCStone','TFBirds','AustinCStone/TFBirds','Python',0,0,0,'2019-01-30T08:07:22Z','Bird flocking simulator in TensorFlow'),
  ],
}

# Source types
source_type_map = {
  "plurigrid": "org", "kubeflow": "org", "TeglonLabs": "org",
  "bmorphism": "user", "zubyul": "user",
  "migalkin": "social_graph", "DJedamski": "social_graph",
  "wasita": "social_graph", "kristinezheng": "social_graph",
  "M1shaaa": "social_graph", "AustinCStone": "social_graph",
}

inc_id = 1
repo_id = 1
ts = datetime.utcnow().isoformat()

for owner, repos in repos_raw.items():
    stype = source_type_map.get(owner, "user")
    for repo in repos:
        org_user, name, full_name, lang, stars, forks, issues, pushed_at, desc = repo
        trit, color, gf3name = gf3(inc_id)
        h = sha8(full_name + pushed_at)
        con.execute("""
            INSERT INTO world_increments VALUES (?,?,?,?,?,?,?,?,?,?,?)
        """, [inc_id, ts, trit, color, gf3name, stype, owner, "repo_push", name, owner, h])
        con.execute("""
            INSERT INTO repo_snapshots VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
        """, [repo_id, ts, inc_id, org_user, name, full_name, lang, stars, forks, issues, pushed_at, desc])
        inc_id += 1
        repo_id += 1

print(f"Inserted {inc_id-1} world_increments and {repo_id-1} repo_snapshots")

# ── APTOS SNAPSHOTS ──────────────────────────────────────────────────────────
aptos_data = [
  ("alice","0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b",None),
  ("bob","0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d",None),
  ("A","0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a",None),
  ("B","0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13",None),
  ("C","0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e",None),
  ("D","0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1",None),
  ("E","0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36",None),
  ("F","0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71",None),
  ("G","0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32",None),
  ("H","0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f",None),
  ("I","0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9",None),
  ("J","0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54",None),
  ("K","0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4",None),
  ("L","0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9",None),
  ("M","0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9",None),
  ("N","0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c",None),
  ("O","0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d",None),
  ("P","0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948",None),
  ("Q","0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9",None),
  ("R","0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10",None),
  ("S","0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386",None),
  ("T","0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588",None),
  ("U","0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956",None),
  ("V","0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3",None),
  ("W","0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0",None),
  ("X","0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d",None),
  ("Y","0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4",None),
  ("Z","0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c",None),
]
for world, addr, bal in aptos_data:
    con.execute("INSERT INTO aptos_snapshots VALUES (?,?,?,?)", [ts, world, addr, bal])
print(f"Inserted {len(aptos_data)} aptos_snapshots (all null - fullnode blocked by network policy)")

# ── MULTISIG PROBES ──────────────────────────────────────────────────────────
multisig_data = [
  ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2,True),
  ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2,True),
  ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2,True),
  ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2,True),
  ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2,True),
]
for pair, addr, sigs, healthy in multisig_data:
    con.execute("INSERT INTO multisig_probes VALUES (?,?,?,?,?)", [ts, pair, addr, sigs, healthy])
print(f"Inserted {len(multisig_data)} multisig_probes (all healthy, sigs_required=2)")

# MNX snapshots - Vercel auth required, no data available
print("MNX: testnet.mnx.fi requires Vercel authentication — no market data inserted")

# Verify
r = con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0]
rs = con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0]
a = con.execute("SELECT COUNT(*) FROM aptos_snapshots").fetchone()[0]
m = con.execute("SELECT COUNT(*) FROM multisig_probes").fetchone()[0]
print(f"\nDB summary: world_increments={r}, repo_snapshots={rs}, aptos_snapshots={a}, multisig_probes={m}")

# Top repos by stars
print("\nTop 10 repos by stars:")
for row in con.execute("SELECT full_name, stars, language FROM repo_snapshots ORDER BY stars DESC LIMIT 10").fetchall():
    print(f"  {row[0]}: {row[1]}★ [{row[2]}]")

con.close()
print("\nDone.")
