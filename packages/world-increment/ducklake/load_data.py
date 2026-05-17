#!/usr/bin/env python3
"""Load all swept data into world-increments.duckdb"""
import duckdb
import hashlib
from datetime import datetime

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
conn = duckdb.connect(DB)

NOW = datetime.utcnow().isoformat()

conn.execute("""
CREATE TABLE IF NOT EXISTS world_increments (
  id INTEGER, timestamp TIMESTAMP DEFAULT now(), gf3_trit INTEGER,
  gf3_color VARCHAR, gf3_name VARCHAR, source_type VARCHAR,
  source_name VARCHAR, event_type VARCHAR, repo_name VARCHAR,
  actor VARCHAR, snapshot_hash VARCHAR
)""")
conn.execute("""
CREATE TABLE IF NOT EXISTS repo_snapshots (
  id INTEGER, timestamp TIMESTAMP DEFAULT now(), increment_id INTEGER,
  org_or_user VARCHAR, repo_name VARCHAR, full_name VARCHAR,
  language VARCHAR, stars INTEGER, forks INTEGER, open_issues INTEGER,
  pushed_at VARCHAR, description VARCHAR
)""")
conn.execute("""
CREATE TABLE IF NOT EXISTS aptos_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  world VARCHAR, address VARCHAR, balance_apt DOUBLE
)""")
conn.execute("""
CREATE TABLE IF NOT EXISTS multisig_probes (
  timestamp TIMESTAMP DEFAULT now(),
  pair VARCHAR, address VARCHAR, sigs_required INTEGER, healthy BOOLEAN
)""")
conn.execute("""
CREATE TABLE IF NOT EXISTS mnx_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  ticker VARCHAR, name VARCHAR, category VARCHAR,
  price DOUBLE, change_pct DOUBLE
)""")

def gf3(n):
    t = n % 3
    if t == 0: return (0, "#d3869b", "ERGODIC")
    if t == 1: return (1, "#b8bb26", "PLUS")
    return (-1, "#cc241d", "MINUS")

def snap_hash(s): return hashlib.sha256(s.encode()).hexdigest()[:16]

# ── repo data ───────────────────────────────────────────────────────────────
repos = []

# plurigrid (100 repos)
plurigrid_repos = [
("plurigrid","plurigrid/gorj","Clojure",0,0,226,"2026-05-17T14:08:06Z","forj + Rama topology nREPL routing + GF(3) gay trit coloring"),
("plurigrid","plurigrid/zig-syrup","Zig",2,2,0,"2026-04-30T03:52:16Z","High-performance Zig OCapN Syrup with CapTP optimizations"),
("plurigrid","plurigrid/asi","HTML",23,5,4,"2026-04-26T08:51:41Z","everything is topological chemputer!"),
("plurigrid","plurigrid/nash-portal","Rust",2,3,2,"2026-04-26T08:50:56Z","NASH token TUI in the browser"),
("plurigrid","plurigrid/horse","TeX",1,1,9,"2026-05-07T04:35:12Z",""),
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
("plurigrid","plurigrid/gatomic","Clojure",0,0,0,"2026-03-30T00:54:48Z","Deterministic color identity store with sonification"),
("plurigrid","plurigrid/blue","TeX",0,0,0,"2026-03-29T23:06:32Z",""),
("plurigrid","plurigrid/red","",0,0,0,"2026-03-29T22:58:46Z",""),
("plurigrid","plurigrid/nblm-flashcards","Hy",0,0,0,"2026-03-26T08:23:01Z","NotebookLM Enterprise flashcard pipeline"),
("plurigrid","plurigrid/gemini-agent","Python",0,0,0,"2026-02-19T06:39:16Z",""),
("plurigrid","plurigrid/graded-optic","Haskell",0,0,0,"2026-02-08T16:10:16Z","Semiring-graded bidirectional processes"),
("plurigrid","plurigrid/json-canvas","",0,0,0,"2026-02-06T06:50:57Z","JSON Canvas real-time interaction data capture"),
("plurigrid","plurigrid/shepherd","Scheme",0,0,0,"2026-01-23T07:47:28Z","Spritely Shepherd service manager"),
("plurigrid","plurigrid/goblinshare","Scheme",0,0,0,"2026-01-23T07:47:12Z","P2P filesharing demo for Goblins"),
("plurigrid","plurigrid/magenc","Scheme",0,0,0,"2026-01-23T07:47:11Z","Magenc Magnet URIs"),
("plurigrid","plurigrid/hoot","Scheme",0,0,0,"2026-01-23T07:47:10Z","Spritely Hoot Scheme to WebAssembly compiler"),
("plurigrid","plurigrid/leprechauns","Racket",0,0,0,"2026-01-23T07:46:46Z","Spritely Goblins + Gay.jl semantic colors"),
("plurigrid","plurigrid/spritely-semantic-colors","",0,0,0,"2026-01-23T07:38:32Z","Deterministic color mappings for Spritely/Goblins"),
("plurigrid","plurigrid/gay-tofu","HTML",0,0,0,"2026-01-08T15:14:34Z","Low-discrepancy color sequences for visual TOFU"),
("plurigrid","plurigrid/lazygay","Go",0,0,0,"2026-01-08T14:19:25Z","lazygit fork with Gay.jl deterministic commit coloring"),
("plurigrid","plurigrid/gay-terminal","Rust",0,0,0,"2026-01-08T14:19:24Z","Terminal ANSI coloring with Gay.jl"),
("plurigrid","plurigrid/gay-go","Go",0,0,0,"2026-01-08T14:19:23Z","Go implementation of Gay.jl deterministic coloring"),
("plurigrid","plurigrid/gay-rs","Rust",0,0,0,"2026-01-08T14:19:22Z","Rust crate for Gay.jl deterministic coloring"),
("plurigrid","plurigrid/lazybjj","Rust",0,0,0,"2026-01-08T14:19:19Z","TUI for jj with Gay.jl GF(3) coloring"),
("plurigrid","plurigrid/agent-o-rama","Clojure",0,0,0,"2026-01-02T01:09:22Z",""),
("plurigrid","plurigrid/aptos-wallet-ruby","Ruby",1,0,0,"2025-09-30T22:47:22Z",""),
("plurigrid","plurigrid/duck-kanban","Rust",1,0,0,"2025-09-26T20:18:38Z","Duck intelligence kanban system"),
("plurigrid","plurigrid/shiteshiteshite","",0,0,0,"2025-09-26T03:07:20Z","Duck intelligence kanban system"),
("plurigrid","plurigrid/discohy","Hy",0,0,0,"2025-09-10T02:01:31Z",""),
("plurigrid","plurigrid/telemind","",0,0,0,"2025-06-12T05:54:59Z",""),
("plurigrid","plurigrid/ontology","JavaScript",8,9,16,"2025-05-27T18:18:34Z","autopoietic ergodicity and embodied gradualism"),
("plurigrid","plurigrid/Plurigraph","JavaScript",3,5,4,"2025-01-05T08:39:09Z","Plurigrid knowledge base for Obsidian.md"),
("plurigrid","plurigrid/signe","Python",0,0,0,"2024-08-15T20:52:03Z","Signal messages data traversal"),
("plurigrid","plurigrid/SwiftDuck","",0,0,0,"2024-08-08T18:19:06Z",""),
("plurigrid","plurigrid/act","Python",3,1,4,"2024-07-26T08:27:08Z","building blocks for cognitive category theory"),
("plurigrid","plurigrid/xenomorphic","",0,0,0,"2024-04-09T03:24:55Z",""),
("plurigrid","plurigrid/metamorphic","",0,0,0,"2024-04-09T03:22:41Z",""),
("plurigrid","plurigrid/DiffusionVoiceDemo","Clojure",0,0,0,"2024-04-02T18:09:01Z",""),
("plurigrid","plurigrid/website","Clojure",0,1,0,"2024-03-30T04:37:51Z",""),
("plurigrid","plurigrid/StochFlow","Python",4,1,0,"2024-03-20T23:34:57Z","stochastic interpolant models"),
("plurigrid","plurigrid/intent","",0,0,0,"2024-03-04T04:53:38Z","Simulations for intent markets"),
("plurigrid","plurigrid/novella","TypeScript",1,0,0,"2024-01-27T08:12:55Z",""),
("plurigrid","plurigrid/ACT.jl","Julia",0,0,0,"2024-01-21T00:02:25Z","applied categorical duck cybernetics"),
("plurigrid","plurigrid/ducklings","TypeScript",0,0,15,"2023-12-25T07:34:27Z",""),
("plurigrid","plurigrid/paretae","TypeScript",0,0,14,"2023-11-20T05:14:42Z",""),
("plurigrid","plurigrid/experiments","",0,0,0,"2023-11-17T05:39:07Z","Learning from experiments"),
("plurigrid","plurigrid/fuckit","Clojure",0,0,0,"2023-11-14T21:26:14Z",""),
("plurigrid","plurigrid/omega","Clojure",0,0,0,"2023-11-07T21:08:46Z",""),
("plurigrid","plurigrid/org","Jupyter Notebook",2,0,1,"2023-11-07T01:08:05Z","Dynamically Replicating Duck"),
("plurigrid","plurigrid/CVAE-Flows","",0,0,0,"2023-10-24T14:41:32Z","Latent spaces for conversation context"),
("plurigrid","plurigrid/morph-prover-cli","",0,1,0,"2023-10-18T03:49:03Z","Lean4"),
("plurigrid","plurigrid/uncharacter","TypeScript",0,0,0,"2023-09-19T20:17:46Z",""),
("plurigrid","plurigrid/chateau","TypeScript",0,0,0,"2023-08-30T20:11:12Z",""),
("plurigrid","plurigrid/gmgm","",0,0,1,"2023-08-25T13:54:00Z",""),
("plurigrid","plurigrid/tuttle","TypeScript",0,0,0,"2023-08-09T17:40:44Z",""),
("plurigrid","plurigrid/mesoplay","",0,0,0,"2023-08-09T06:19:03Z",""),
("plurigrid","plurigrid/am","Python",0,0,0,"2023-08-05T12:46:33Z",""),
("plurigrid","plurigrid/compose","",0,0,2,"2023-07-24T06:18:48Z",""),
("plurigrid","plurigrid/flussi","",0,0,1,"2023-07-15T06:40:11Z",""),
("plurigrid","plurigrid/cf","",0,0,0,"2023-07-11T08:11:29Z",""),
("plurigrid","plurigrid/poepoe","",0,0,1,"2023-07-09T22:20:50Z",""),
("plurigrid","plurigrid/marketplace","",0,0,1,"2023-07-09T05:52:30Z",""),
("plurigrid","plurigrid/smoller","",0,0,1,"2023-07-06T07:38:04Z",""),
("plurigrid","plurigrid/liquidity","",0,0,1,"2023-07-06T02:07:28Z",""),
("plurigrid","plurigrid/solid-rs","",0,0,1,"2023-07-05T21:58:05Z",""),
("plurigrid","plurigrid/solid","Python",0,0,0,"2023-07-05T21:52:25Z",""),
("plurigrid","plurigrid/ipegrafo","Python",0,0,0,"2023-07-03T07:29:40Z",""),
("plurigrid","plurigrid/plurigrid-v4","TypeScript",0,0,0,"2023-07-03T06:31:59Z",""),
("plurigrid","plurigrid/novella-v3","",0,0,0,"2023-07-03T06:29:40Z",""),
("plurigrid","plurigrid/polyglottal","TypeScript",0,0,0,"2023-07-03T06:23:45Z",""),
("plurigrid","plurigrid/novella-v2","",0,0,0,"2023-07-03T06:22:38Z",""),
("plurigrid","plurigrid/cocreation-ui","",0,0,2,"2023-07-03T04:45:53Z",""),
("plurigrid","plurigrid/smol","",0,0,1,"2023-07-02T08:45:32Z",""),
("plurigrid","plurigrid/commons","TypeScript",0,0,0,"2023-06-27T05:46:24Z",""),
("plurigrid","plurigrid/post-web","Svelte",0,0,0,"2023-06-18T00:24:24Z",""),
("plurigrid","plurigrid/microworlds","Rust",3,5,3,"2023-05-13T03:54:56Z",""),
("plurigrid","plurigrid/pills","",0,0,0,"2023-05-02T10:03:03Z","metaphors for embodied gradualism"),
("plurigrid","plurigrid/plurigrid-rs","Rust",0,0,0,"2023-04-21T01:02:56Z",""),
("plurigrid","plurigrid/plurigrid-game.github.io","HTML",0,0,1,"2023-04-20T00:17:55Z",""),
("plurigrid","plurigrid/synth","Rust",0,0,0,"2023-04-15T01:56:45Z",""),
("plurigrid","plurigrid/birbs","C++",0,0,0,"2023-04-15T01:56:32Z","Build native CosmWasm apps w/ Dart and Flutter"),
("plurigrid","plurigrid/agent","Python",5,1,6,"2023-03-31T18:45:23Z","Framework for agency amplification"),
("plurigrid","plurigrid/vcg-auction","Rust",7,2,1,"2023-03-16T21:53:08Z","simple contract that performs VCG auction"),
("plurigrid","plurigrid/bidder","Dart",0,0,1,"2023-03-15T15:23:22Z","simple flutter app for vcg auction bidding"),
("plurigrid","plurigrid/plurigrid.github.io","HTML",1,2,2,"2023-01-20T03:27:34Z",""),
("plurigrid","plurigrid/VPP","Julia",0,1,0,"2023-01-11T18:41:07Z","Hyperreal Power Plant"),
("plurigrid","plurigrid/grid","TypeScript",2,1,1,"2023-01-02T11:55:55Z","Plurigrid Testnet #0: Edith Clarke"),
("plurigrid","plurigrid/commons-contracts","Rust",0,0,0,"2022-09-09T09:20:11Z","CosmWasm contracts for Commons Stack"),
("plurigrid","plurigrid/plurigrid.xyz","TypeScript",0,0,1,"2022-08-31T05:26:14Z",""),
("plurigrid","plurigrid/gridops","",0,0,2,"2022-07-16T03:02:28Z","monorepo for the monists"),
]

# kubeflow (48 repos)
kubeflow_repos = [
("kubeflow","kubeflow/manifests","YAML",1017,1064,25,"2026-05-16T16:37:54Z","Kubeflow AI Reference Platform Deployment Manifests"),
("kubeflow","kubeflow/pipelines","Python",4139,1993,467,"2026-05-15T21:36:15Z","Machine Learning Pipelines for Kubeflow"),
("kubeflow","kubeflow/mlflow-integration","Python",6,3,3,"2026-05-15T19:20:29Z",""),
("kubeflow","kubeflow/kale","Python",687,156,57,"2026-05-15T19:04:47Z","Kubeflow superfood for Data Scientists"),
("kubeflow","kubeflow/spark-operator","Python",3125,1482,93,"2026-05-15T16:31:02Z","Kubernetes operator for Apache Spark applications"),
("kubeflow","kubeflow/hub","Go",175,178,50,"2026-05-15T15:36:02Z","Model Registry single pane of glass for ML models"),
("kubeflow","kubeflow/trainer","Go",2099,949,104,"2026-05-15T15:21:03Z","Distributed AI Model Training and LLM Fine-Tuning"),
("kubeflow","kubeflow/website","HTML",184,920,52,"2026-05-14T17:20:09Z","Kubeflow Website"),
("kubeflow","kubeflow/mcp-apache-spark-history-server","Python",170,60,24,"2026-05-13T19:15:35Z","MCP Server for Apache Spark History Server"),
("kubeflow","kubeflow/sdk","Python",117,174,136,"2026-05-12T18:53:41Z","Universal Python SDK to run AI workloads on Kubernetes"),
("kubeflow","kubeflow/mpi-operator","Go",527,235,100,"2026-05-12T17:13:37Z","Kubernetes Operator for MPI-based applications"),
("kubeflow","kubeflow/mcp-server","Python",9,12,21,"2026-05-12T10:14:24Z","MCP Server for AI-Assisted Development with Kubeflow"),
("kubeflow","kubeflow/notebooks","",72,109,189,"2026-05-15T15:41:12Z","Kubeflow Notebooks for interactive development environments"),
("kubeflow","kubeflow/community","Jsonnet",196,257,14,"2026-05-13T18:53:18Z","Kubeflow community information"),
("kubeflow","kubeflow/blog","Jupyter Notebook",32,62,27,"2026-05-11T15:21:33Z","Kubeflow blog"),
("kubeflow","kubeflow/dashboard","TypeScript",17,55,76,"2026-05-16T00:25:13Z","Kubeflow Central Dashboard"),
("kubeflow","kubeflow/internal-acls","Go",19,385,3,"2026-05-09T21:06:02Z","Group ACLs for Kubeflow developers"),
("kubeflow","kubeflow/katib","Python",1682,521,122,"2026-05-09T12:21:57Z","Automated Machine Learning on Kubernetes"),
("kubeflow","kubeflow/pipelines-components","Python",11,38,32,"2026-05-11T18:19:25Z","Kubeflow Pipelines components"),
("kubeflow","kubeflow/kubeflow","",15639,2647,2,"2026-05-07T13:46:41Z","Machine Learning Toolkit for Kubernetes"),
("kubeflow","kubeflow/arena","Go",810,190,57,"2026-05-07T06:46:17Z","A CLI for Kubeflow"),
("kubeflow","kubeflow/docs-agent","Python",36,98,153,"2026-04-14T03:33:15Z","Kubeflow Documentation AI Agent"),
("kubeflow","kubeflow/examples","Jsonnet",1463,757,111,"2025-04-14T01:54:52Z","Extended examples and tutorials"),
("kubeflow","kubeflow/testing","Python",60,86,33,"2025-02-14T18:33:13Z","Test infrastructure for Kubeflow"),
("kubeflow","kubeflow/kfp-tekton","TypeScript",182,123,79,"2024-11-19T12:23:51Z","Kubeflow Pipelines on Tekton"),
("kubeflow","kubeflow/kfserving-lts","Jsonnet",12,19,51,"2024-08-02T16:25:44Z",""),
("kubeflow","kubeflow/kubebench","Jsonnet",78,35,68,"2024-06-17T19:22:04Z","Benchmarking repository"),
("kubeflow","kubeflow/fate-operator","Go",51,15,6,"2024-02-22T19:44:08Z","Fate operator"),
("kubeflow","kubeflow/kfctl","Go",182,134,94,"2023-08-15T20:19:22Z","kfctl CLI for deploying Kubeflow"),
("kubeflow","kubeflow/kfp-tekton-backend","TypeScript",8,6,46,"2023-08-14T22:05:04Z","Tekton yaml behind KFP API engine"),
("kubeflow","kubeflow/common","Go",53,70,40,"2023-05-28T13:16:00Z","Common APIs shared by Kubeflow operators"),
("kubeflow","kubeflow/.allstar","",2,0,0,"2022-12-06T23:07:59Z",""),
("kubeflow","kubeflow/fairing","Jsonnet",337,143,134,"2022-04-11T05:28:47Z","Python SDK for building and deploying ML models"),
("kubeflow","kubeflow/xgboost-operator","Python",77,53,22,"2021-12-01T18:00:10Z","Kubernetes operator for xgboost"),
("kubeflow","kubeflow/mxnet-operator","Go",52,33,9,"2021-12-01T17:47:19Z","Kubernetes operator for mxnet jobs"),
("kubeflow","kubeflow/pytorch-operator","Jsonnet",310,143,63,"2021-12-01T17:44:48Z","PyTorch on Kubernetes"),
("kubeflow","kubeflow/frontend","JavaScript",8,18,12,"2021-12-01T17:41:37Z","Kubeflow frontend"),
("kubeflow","kubeflow/metadata","TypeScript",123,63,38,"2021-12-01T17:35:27Z","Metadata repository"),
("kubeflow","kubeflow/caffe2-operator","Go",16,12,2,"2021-12-01T01:58:06Z","Experimental caffe2 operator"),
("kubeflow","kubeflow/code-intelligence","Jupyter Notebook",56,20,64,"2021-12-01T01:52:58Z","ML-Powered Developer Tools"),
("kubeflow","kubeflow/example-seldon","Jupyter Notebook",172,56,9,"2021-12-01T01:49:58Z","End-to-end ML on Kubernetes with Kubeflow"),
("kubeflow","kubeflow/batch-predict","Python",17,7,9,"2021-12-01T01:47:51Z","Batch predict repository"),
("kubeflow","kubeflow/reporting","Jsonnet",2,5,1,"2021-12-01T01:42:32Z","Metrics about Kubeflow usage"),
("kubeflow","kubeflow/chainer-operator","Jsonnet",17,15,7,"2021-11-14T13:03:57Z","Chainer operator"),
("kubeflow","kubeflow/crd-validation","Go",11,7,5,"2021-01-25T15:02:53Z","Validation Generation for Kubeflow CRD"),
("kubeflow","kubeflow/community-infra","Go",3,9,4,"2021-01-25T14:49:49Z","Declarative configs for KF community infra"),
("kubeflow","kubeflow/.github","",2,1,0,"2020-05-12T00:22:56Z","Org wide templates"),
("kubeflow","kubeflow/marketing-materials","",4,4,4,"2019-07-19T13:57:15Z",""),
]

# TeglonLabs (4 repos)
teglon_repos = [
("TeglonLabs","TeglonLabs/mathpix-gem","Ruby",2,0,11,"2026-01-01T12:13:13Z","Transform mathematical images to LaTeX and documents to markdown"),
("TeglonLabs","TeglonLabs/monad-mcp-server","","",0,0,"2025-05-14T11:36:14Z","Monad MCP Server"),
("TeglonLabs","TeglonLabs/topoi","Python",0,0,1,"2025-01-24T04:49:26Z",""),
("TeglonLabs","TeglonLabs/coin-flip-mcp","JavaScript",0,2,1,"2025-09-21T08:57:27Z","MCP server for flipping coins with random.org"),
]

# bmorphism (100 repos - abbreviated for insert)
bmorphism_repos = [
("bmorphism","bmorphism/Gay.jl","Julia",1,0,189,"2026-05-17T00:34:34Z","Wide-gamut color sampling with splittable determinism"),
("bmorphism","bmorphism/oxgame","OCaml",0,0,0,"2026-05-15T09:53:27Z","Stellar resolution and open-game composition for OCaml"),
("bmorphism","bmorphism/boxxy","Move",0,1,0,"2026-04-30T03:35:47Z",""),
("bmorphism","bmorphism/nanoclj-zig","Zig",0,0,0,"2026-05-07T20:12:15Z",""),
("bmorphism","bmorphism/postweb","Go",0,0,0,"2026-04-09T10:51:57Z","postweb"),
("bmorphism","bmorphism/shitcoin","Python",5,0,0,"2026-04-08T08:07:08Z","gets denom for cw20 assets"),
("bmorphism","bmorphism/magic-world-org","Python",1,0,0,"2026-04-05T07:03:50Z","Magic World Org Local MLX"),
("bmorphism","bmorphism/zig-syrup","Zig",0,0,0,"2026-05-07T19:49:05Z","Embeddable OCapN Syrup encoder/decoder in Zig"),
("bmorphism","bmorphism/ocaml-mcp-sdk","OCaml",61,2,0,"2026-03-16T05:24:25Z","OCaml SDK for Model Context Protocol"),
("bmorphism","bmorphism/flox-mcp-bb","Clojure",0,0,0,"2026-02-12T02:45:43Z","Open-source MCP server for Flox"),
("bmorphism","bmorphism/vibesnipe-market","Move",0,0,9,"2026-02-05T10:23:25Z",""),
("bmorphism","bmorphism/tapes","",0,0,0,"2026-02-04T02:23:37Z","VHS tapes for terminal recordings"),
("bmorphism","bmorphism/duck-rio-heateq","Rust",0,0,0,"2026-02-02T23:33:32Z",""),
("bmorphism","bmorphism/aella","Rascal",1,0,0,"2026-02-01T02:44:30Z",""),
("bmorphism","bmorphism/hymlx","Python",1,0,0,"2026-01-22T12:20:32Z",""),
("bmorphism","bmorphism/GeoACSets.jl","Julia",0,1,1,"2026-01-19T13:57:13Z","Categorical data structures with geospatial capabilities"),
("bmorphism","bmorphism/anti-bullshit-mcp-server","JavaScript",23,7,1,"2026-01-16T08:54:58Z","MCP server for analyzing claims and detecting manipulation"),
("bmorphism","bmorphism/open-location-code-zig","Zig",3,0,0,"2025-12-30T19:33:45Z","Open Location Code for Zig"),
("bmorphism","bmorphism/gay-color-learnable","",0,0,0,"2025-12-15T18:41:02Z","Learnable color embeddings via Gay.jl SPI"),
("bmorphism","bmorphism/gay-hy","Hy",0,0,0,"2025-12-15T15:32:58Z","Hylang MLX color bandwidth protocol"),
("bmorphism","bmorphism/multiverse-color-game","Julia",0,0,0,"2025-12-12T05:28:11Z","2+1D Holographic Color Matching Game"),
("bmorphism","bmorphism/signal-mcp","Rust",0,0,0,"2025-12-11T07:20:08Z","O(n)->O(1) chromatic mode collapse"),
("bmorphism","bmorphism/xf.jl","Julia",0,0,0,"2025-12-05T22:12:17Z","Xenofeminist color synthesis"),
("bmorphism","bmorphism/bafishka","Clojure",1,0,0,"2025-12-19T09:38:00Z","Rust-native Fish shell file operations"),
("bmorphism","bmorphism/deberta-goemotions","Python",0,0,0,"2025-10-22T18:32:24Z",""),
("bmorphism","bmorphism/monero-rental-hash-war","Haskell",1,0,0,"2025-10-05T23:08:54Z","Compositional OpenGame analysis of Monero hash war"),
("bmorphism","bmorphism/schoenfinkel","Python",1,0,0,"2025-10-04T23:31:11Z","Post-quantum categorical gravity framework"),
("bmorphism","bmorphism/gay-spec","",1,0,0,"2025-10-02T02:01:56Z",""),
("bmorphism","bmorphism/bafishka-clean","Rust",1,0,0,"2025-09-25T19:22:10Z","Clean monadic Steel-SCI integration"),
("bmorphism","bmorphism/duck-rs","Zig",0,0,0,"2025-10-05T00:21:07Z",""),
("bmorphism","bmorphism/babashka-static-build","Dockerfile",1,0,0,"2025-09-05T02:26:32Z","Static musl babashka build for ARM64 Termux"),
("bmorphism","bmorphism/whale","MATLAB",2,0,0,"2025-09-04T06:55:21Z","omniglot + sperm whale codas = metawhaling"),
("bmorphism","bmorphism/infinity-topos","Python",1,0,0,"2025-08-29T05:39:49Z",""),
("bmorphism","bmorphism/elevenlabs-mcp-enhanced","Python",1,0,0,"2025-08-29T04:41:58Z","Enhanced ElevenLabs MCP server"),
("bmorphism","bmorphism/zeldar","Python",1,0,1,"2025-08-26T15:16:21Z","Burning Man Art Robot"),
("bmorphism","bmorphism/stellogen-quantum-operads","",1,0,0,"2025-07-15T04:49:41Z","Quantum Operads and ZX-Calculus in Stellogen"),
("bmorphism","bmorphism/apple-container-framework","Clojure",0,0,0,"2025-07-13T12:12:10Z","Apple Container Framework for VM snapshots"),
("bmorphism","bmorphism/ezkl-ethglobal2025","Python",1,0,0,"2025-07-07T01:16:01Z",""),
("bmorphism","bmorphism/zk-haiku-nanogpt","Solidity",1,0,0,"2025-07-06T03:08:24Z","ZK-Haiku-NanoGPT agentic proof-chaining"),
("bmorphism","bmorphism/rama-event-processor","Java",1,0,0,"2025-07-02T07:01:44Z","Processing events with Rama"),
("bmorphism","bmorphism/vibespace-mcp-go-ternary","HTML",0,1,3,"2026-01-11T12:50:40Z","Go MCP experience with NATS streaming and balanced ternary"),
("bmorphism","bmorphism/oxcaml-sci-canonical","OCaml",1,0,0,"2025-06-20T06:37:12Z","Canonical OxCaml-SCI implementation"),
("bmorphism","bmorphism/oxcaml-mcp","",0,0,0,"2025-06-20T04:04:34Z","OxCaml-MCP high-performance MCP server"),
("bmorphism","bmorphism/oxcaml-sci","",0,0,0,"2025-06-20T03:48:11Z","OxCaml-SCI Scientific Computing Interface"),
("bmorphism","bmorphism/infinity-topos-impossibility","",0,0,14,"2025-05-29T01:55:28Z","Impossibility results for automated analysis"),
("bmorphism","bmorphism/graphistry-mcp","Python",2,0,0,"2025-05-06T17:34:24Z","Graphistry MCP integration for graph visualization"),
("bmorphism","bmorphism/hypernym-mcp-server","JavaScript",6,5,0,"2025-04-02T21:21:08Z",""),
("bmorphism","bmorphism/vibespace-mcp-go","",0,0,0,"2025-03-19T20:30:02Z","Go MCP experience with NATS streaming"),
("bmorphism","bmorphism/krep-mcp-server","JavaScript",1,1,1,"2025-03-19T20:22:46Z","High-performance string search MCP server"),
("bmorphism","bmorphism/minecraft-mcp-golf","",0,0,0,"2025-03-16T10:33:31Z","Minecraft server with MCP capabilities"),
("bmorphism","bmorphism/worlds-code-explorer","",0,0,0,"2025-03-16T05:46:58Z","Code explorer for different worlds"),
("bmorphism","bmorphism/voice-fn","",0,0,0,"2025-02-24T22:28:32Z","Clojure framework for voice-enabled AI apps"),
("bmorphism","bmorphism/lumon-tui","Python",1,0,0,"2025-02-02T11:24:21Z","Terminal parallel worlds inspired by Lumon Industries"),
("bmorphism","bmorphism/goose-diagrams","",0,0,0,"2025-01-31T08:46:44Z","ASCII art diagrams for Goose AI"),
("bmorphism","bmorphism/MetaLab","",0,0,0,"2025-01-30T11:40:33Z","Learning and experimenting with technologies"),
("bmorphism","bmorphism/penrose-mcp","JavaScript",10,4,0,"2025-01-20T21:44:55Z","Penrose server for Infinity-Topos"),
("bmorphism","bmorphism/penrose-mcp-server","",0,0,0,"2025-01-20T20:24:07Z","MCP server for Penrose"),
("bmorphism","bmorphism/test-repo-3141592","",0,0,1,"2025-01-11T15:06:57Z","Test repository"),
("bmorphism","bmorphism/manifold-mcp-server","JavaScript",14,9,5,"2025-01-11T10:36:58Z","MCP server for Manifold Markets"),
("bmorphism","bmorphism/say-mcp-server","JavaScript",20,9,3,"2025-01-07T03:15:18Z","MCP server for macOS text-to-speech"),
("bmorphism","bmorphism/penumbra-mcp","JavaScript",5,6,3,"2025-01-07T01:15:23Z","MCP server for Penumbra blockchain"),
("bmorphism","bmorphism/nats-mcp-server","",7,3,2,"2025-01-06T23:33:41Z","MCP server for NATS messaging"),
("bmorphism","bmorphism/marginalia-mcp-server","JavaScript",8,6,0,"2025-01-06T05:47:24Z","MCP server for marginalia and annotations"),
("bmorphism","bmorphism/babashka-mcp-server","JavaScript",18,6,3,"2025-01-05T11:09:42Z","MCP server for Babashka Clojure"),
("bmorphism","bmorphism/openbci-mcp-server","",0,0,0,"2025-01-05T07:00:10Z","MCP server for OpenBCI hardware"),
("bmorphism","bmorphism/gists-mcp-server","JavaScript",2,0,0,"2025-01-03T03:50:54Z","MCP server for GitHub Gists"),
("bmorphism","bmorphism/neural-category-diagrams","",0,0,0,"2025-01-02T05:47:22Z","Diagrams for neural architectures via category theory"),
("bmorphism","bmorphism/slowtime-mcp-server","TypeScript",3,5,6,"2025-01-02T01:23:33Z","MCP server for secure time-based operations"),
("bmorphism","bmorphism/open-games-agda","Agda",0,0,0,"2024-12-22T11:16:29Z","Formalization of open games in Agda"),
("bmorphism","bmorphism/yoyo","Just",0,0,0,"2024-11-30T04:00:12Z",""),
("bmorphism","bmorphism/uss-cogsexy","",0,0,0,"2024-11-23T20:52:30Z","Cognitive Firewall information reflow"),
("bmorphism","bmorphism/vibes","Clojure",0,0,0,"2024-11-13T15:56:28Z","Global Vibespace"),
("bmorphism","bmorphism/untime","Swift",1,0,0,"2024-09-06T23:39:08Z",""),
("bmorphism","bmorphism/cf","Handlebars",0,0,0,"2024-08-07T01:14:25Z","collective futures"),
("bmorphism","bmorphism/collective","",0,0,0,"2024-08-07T01:08:28Z",""),
("bmorphism","bmorphism/pretopos","TeX",0,0,0,"2024-07-27T12:34:14Z",""),
("bmorphism","bmorphism/c-house-town","TypeScript",1,0,0,"2024-07-25T21:13:04Z",""),
("bmorphism","bmorphism/galahack2024","TypeScript",2,0,0,"2024-03-21T15:48:19Z",""),
("bmorphism","bmorphism/crags","Python",1,0,0,"2024-01-14T04:21:45Z","RAGs categorically"),
("bmorphism","bmorphism/hacker-news-alert-chatgpt-slack","Rust",0,0,0,"2023-08-31T09:56:37Z","Monitor HN and summarize with ChatGPT"),
("bmorphism","bmorphism/summarize-github-issues","Rust",0,0,0,"2023-08-31T09:44:28Z","Summarize GitHub issues with ChatGPT"),
("bmorphism","bmorphism/slackduck","Rust",0,0,0,"2023-08-31T09:24:05Z","Slack bot with ChatGPT backend"),
("bmorphism","bmorphism/telega","Rust",1,0,0,"2023-08-23T17:20:29Z","absurd wasm32-wasi flow"),
("bmorphism","bmorphism/io","Handlebars",0,0,0,"2023-08-20T07:15:36Z",""),
("bmorphism","bmorphism/mesocunt2001","Rust",0,0,0,"2023-08-19T07:49:43Z","Telegram bot with Claude backend"),
("bmorphism","bmorphism/mesocunt","Rust",0,0,0,"2023-08-18T10:13:33Z","Discord bot with ChatGPT backend"),
("bmorphism","bmorphism/meso","Jupyter Notebook",1,1,0,"2023-08-09T06:04:11Z","Scripts for Markov Kernel inference"),
("bmorphism","bmorphism/monaduck69","Svelte",0,0,1,"2023-07-19T12:43:12Z","SvelteKit template"),
("bmorphism","bmorphism/banana","Python",0,0,0,"2023-02-23T15:12:07Z",""),
("bmorphism","bmorphism/Plurigrid.jl","Julia",0,1,0,"2023-01-04T14:53:02Z",""),
("bmorphism","bmorphism/plurigrid-celo","TypeScript",1,1,0,"2022-12-09T10:07:25Z","Celo e-app for Albany Plurigrid"),
("bmorphism","bmorphism/risc0-cosmwasm-example","Rust",23,2,1,"2022-10-20T23:50:40Z","CosmWasm + zkVM RISC-V EFI template"),
("bmorphism","bmorphism/knxwledge","",0,1,1,"2022-10-02T02:23:31Z",""),
("bmorphism","bmorphism/OTC-0","JavaScript",3,0,0,"2022-06-07T22:18:08Z",""),
("bmorphism","bmorphism/matrix5","",0,0,0,"2022-05-25T06:01:57Z","glowing in public"),
("bmorphism","bmorphism/pluridrop","TypeScript",2,0,0,"2022-04-10T00:13:47Z","ETHPortland2022 hack"),
("bmorphism","bmorphism/kfsummit19","Python",0,0,0,"2019-10-28T16:40:46Z","kubeflow pipelines on Anthos"),
("bmorphism","bmorphism/recommenders","Python",0,0,0,"2019-09-11T07:43:03Z",""),
("bmorphism","bmorphism/deepfakes","Python",1,0,2,"2019-04-28T22:53:40Z",""),
("bmorphism","bmorphism/dotemacs","Emacs Lisp",1,0,0,"2019-03-29T22:57:59Z",""),
]

# zubyul (49 repos)
zubyul_repos = [
("zubyul","zubyul/voice-observatory","Python",0,0,0,"2026-04-24T05:56:17Z","Passive macOS TUI observing voice-download pathways"),
("zubyul","zubyul/ghostel-emacs-worlds","GLSL",0,0,0,"2026-04-24T00:20:56Z","Ghostty config + ghostel family + alice/bob emacs-mods"),
("zubyul","zubyul/nash-web","Rust",0,0,0,"2026-04-13T07:08:58Z","NASH token browser TUI via ratzilla WASM"),
("zubyul","zubyul/nash-tui","Rust",0,0,0,"2026-04-13T07:45:16Z","NASH token TUI real-time candles via GeckoTerminal"),
("zubyul","zubyul/big-bad-plurigrid-quiz","Emacs Lisp",0,0,0,"2026-04-09T18:51:31Z","27 flashcards from plurigrid activity"),
("zubyul","zubyul/Gay.jl","Julia",0,0,0,"2026-03-28T11:30:01Z","Wide-gamut color sampling with splittable determinism"),
("zubyul","zubyul/kinesis-kb360pro","Python",0,0,0,"2026-03-26T10:29:40Z","Claude Code skill for Kinesis Advantage360 Pro keyboard"),
("zubyul","zubyul/gay-world","Python",1,1,0,"2026-03-26T04:03:39Z","Goblin world builder with Gay.jl"),
("zubyul","zubyul/from-possible-worlds","TeX",0,0,0,"2026-03-16T03:14:55Z",""),
("zubyul","zubyul/tilelang-kernels","Python",0,0,0,"2026-03-16T02:31:13Z","TileLang GPU kernels for SplitMix64 color generation"),
("zubyul","zubyul/fleet-bootstrap","Shell",0,0,0,"2026-02-23T08:19:58Z",""),
("zubyul","zubyul/gay-terminal-colors","Clojure",0,0,0,"2026-02-21T07:38:14Z","Gay.jl world_terminal_fingerprint SplitMix64 per-terminal"),
("zubyul","zubyul/basin","Rust",0,0,0,"2026-02-13T10:31:47Z",""),
("zubyul","zubyul/openbci-visualizer","Zig",0,0,0,"2026-02-04T11:17:41Z",""),
("zubyul","zubyul/plurigrid-site","Svelte",0,1,11,"2026-02-04T03:20:08Z","Plurigrid world site deployment"),
("zubyul","zubyul/repl","Python",0,0,0,"2026-02-04T01:08:15Z",""),
("zubyul","zubyul/instance-onboarding","Shell",0,0,0,"2026-02-02T11:44:07Z",""),
("zubyul","zubyul/vibesnipe","Move",0,0,1,"2026-01-30T22:36:03Z",""),
("zubyul","zubyul/zubyul.github.io","CSS",1,0,0,"2026-01-27T03:24:34Z",""),
("zubyul","zubyul/toad-warpify-extension","Python",0,0,0,"2026-01-17T07:48:40Z","Warpify extension for Toad ACP agents"),
("zubyul","zubyul/thread-site","Haskell",0,0,0,"2025-12-23T23:53:27Z",""),
("zubyul","zubyul/GayMove","Move",0,0,0,"2025-12-18T09:40:08Z",""),
("zubyul","zubyul/gay-brain-world","Python",0,0,0,"2025-12-16T01:19:28Z","Gay.jl SPI colors for Moduleur Brain + OpenBCI EEG"),
("zubyul","zubyul/multiplayer","HTML",0,0,0,"2025-12-12T08:56:16Z",""),
("zubyul","zubyul/cat-world","TypeScript",0,0,0,"2025-12-12T08:47:14Z","Cat gaze tracker for bird video preferences"),
("zubyul","zubyul/hue-world","JavaScript",0,0,0,"2025-12-12T08:32:59Z","Terminal Vibe Snipe puzzle game"),
("zubyul","zubyul/multiplayer-emacs","HTML",0,0,0,"2025-12-12T08:07:38Z","Multiplayer Emacs split-pane Vibe Snipe"),
("zubyul","zubyul/vibe-snipe","Kotlin",0,0,0,"2025-12-12T03:46:26Z",""),
("zubyul","zubyul/chromatic-vrf","Kotlin",0,0,0,"2025-12-12T03:26:22Z","Chromatic VRF I Love Hue puzzle"),
("zubyul","zubyul/quantum-telephone","Jupyter Notebook",0,0,0,"2025-12-08T22:54:16Z","Quantum telephone entangled message passing"),
("zubyul","zubyul/c-elegans-connectome","JavaScript",0,0,0,"2025-11-22T15:43:55Z",""),
("zubyul","zubyul/zoterobsidian","Shell",0,0,0,"2025-09-28T16:50:50Z",""),
("zubyul","zubyul/cascade-world","Python",1,0,0,"2025-09-19T18:25:12Z","Cascade development environment"),
("zubyul","zubyul/plurigrid-playbook","",0,0,0,"2025-09-17T02:10:35Z",""),
("zubyul","zubyul/defcon","JavaScript",1,0,0,"2025-09-17T02:07:00Z",""),
("zubyul","zubyul/ghostty-modifications","JavaScript",1,0,0,"2025-09-15T02:45:21Z","Ghostty terminal modifications and MCP servers"),
("zubyul","zubyul/GoofyLifeChoices","Python",1,0,0,"2025-07-30T18:48:13Z",""),
("zubyul","zubyul/book","HTML",0,0,0,"2025-05-15T20:30:39Z",""),
("zubyul","zubyul/ezAR","",0,0,0,"2025-02-03T21:02:26Z",""),
("zubyul","zubyul/obsidian","",0,0,0,"2024-05-24T18:26:28Z",""),
("zubyul","zubyul/private","SCSS",0,0,0,"2023-10-05T21:03:16Z",""),
("zubyul","zubyul/jonikas_for_weronika.-annotated-code","Jupyter Notebook",1,0,0,"2023-08-17T02:46:42Z",""),
("zubyul","zubyul/jonikas_lab_data_analysis_misc","Jupyter Notebook",2,0,0,"2023-08-16T20:24:40Z","Scripts for genetic sequence data processing"),
("zubyul","zubyul/WGCNA","HTML",2,0,0,"2023-07-05T18:02:30Z","Weighted gene correlation network analysis"),
("zubyul","zubyul/Dr_Niv_Qs","Jupyter Notebook",0,0,0,"2023-06-29T04:44:01Z","Dr. Niv Interview Questions"),
("zubyul","zubyul/reddit_scraper","Python",0,0,0,"2023-06-16T14:06:07Z",""),
("zubyul","zubyul/Python_Undergrad","Python",0,0,0,"2023-06-16T14:02:18Z",""),
("zubyul","zubyul/Nikolova_lab_data_analysis","R",2,0,0,"2023-06-16T13:56:58Z","Undergraduate thesis cortical thickness study"),
("zubyul","zubyul/lastfm_analysis_copy","Jupyter Notebook",1,0,0,"2023-06-15T22:20:35Z","lastfm data analysis"),
]

# Social graph users
migalkin_repos = [
("migalkin","migalkin/kgcourse2021","HTML",25,9,0,"2026-02-16T05:16:08Z","Materials for Knowledge Graphs course"),
("migalkin","migalkin/migalkin.github.io","JavaScript",0,0,0,"2025-05-20T23:58:08Z","Github Pages academic website"),
("migalkin","migalkin/NBFNet_mlx","Python",10,1,1,"2026-03-11T01:31:21Z","Neural Bellman-Ford networks in MLX for Apple Silicon"),
("migalkin","migalkin/StarE","Python",89,16,1,"2026-04-16T14:12:45Z","Message Passing for Hyper-Relational Knowledge Graphs"),
("migalkin","migalkin/rambo","Rust",3,0,1,"2023-02-28T16:37:22Z",""),
("migalkin","migalkin/ciss2_project","Jupyter Notebook",0,0,6,"2019-06-28T23:14:33Z",""),
("migalkin","migalkin/RWL","Python",7,1,0,"2025-02-10T14:12:14Z","Weisfeiler and Leman Go Relational"),
("migalkin","migalkin/NodePiece","Python",144,21,0,"2026-05-07T05:40:02Z","Compositional Representations for Large Knowledge Graphs"),
("migalkin","migalkin/SQuAD-es-mt","",0,1,0,"2020-07-14T17:18:37Z","Spanish SQuAD via machine translation"),
("migalkin","migalkin/netquery_rdf","Python",0,0,0,"2019-06-01T12:49:18Z","NIPS 2018 paper fork for RDF"),
("migalkin","migalkin/edbt-experiments","",0,0,0,"2017-11-20T10:27:28Z",""),
("migalkin","migalkin/SMJoin-experiments","R",1,0,0,"2020-03-04T15:56:23Z","ISWC 2017 SMJoin results"),
("migalkin","migalkin/ekgs_clustering","Python",0,0,0,"2016-08-28T16:25:19Z",""),
("migalkin","migalkin/r_energyConsumption","R",0,0,0,"2016-05-12T21:00:17Z",""),
("migalkin","migalkin/ontologies","Web Ontology Language",0,0,0,"2015-12-06T13:49:53Z",""),
("migalkin","migalkin/Tables_Provider","Java",0,0,0,"2015-03-20T00:17:36Z",""),
("migalkin","migalkin/datasciencecoursera","",0,0,0,"2015-02-12T23:57:16Z","Coursera Data Science course"),
("migalkin","migalkin/InformationWorkbenchTestSrc","Java",0,0,0,"2014-10-15T21:42:40Z",""),
("migalkin","migalkin/LinkedData","",0,0,0,"2014-10-15T21:42:40Z","Information Workbench + Linked Open Data"),
]

djedamski_repos = [
("DJedamski","DJedamski/kaggle_ncaa18","Jupyter Notebook",0,0,0,"2018-02-26T16:33:24Z","Code for NCAA March Madness 2018"),
("DJedamski","DJedamski/Project_Euler","",0,0,0,"2015-09-05T17:13:32Z",""),
("DJedamski","DJedamski/EDA","R",0,0,0,"2014-11-09T17:00:39Z","Coursera Project"),
("DJedamski","DJedamski/Kaggle","",1,0,0,"2023-04-21T01:42:35Z",""),
("DJedamski","DJedamski/Getting-and-Cleaning-Data","R",1,0,0,"2023-04-21T01:42:34Z","Coursera Project"),
("DJedamski","DJedamski/School","R",1,1,0,"2023-04-21T01:42:33Z","Small projects from grad school"),
]

wasita_repos = [
("wasita","wasita/wasita.github.io","Svelte",1,0,8,"2026-05-17T00:36:54Z","Personal website"),
("wasita","wasita/wm-cv","Svelte",0,0,0,"2026-05-13T05:29:08Z","Academic CV as single page web app"),
("wasita","wasita/vocoder","JavaScript",0,0,0,"2026-05-06T05:14:03Z",""),
("wasita","wasita/ch3-lib","Typst",0,0,0,"2026-04-12T04:03:22Z",""),
("wasita","wasita/magic-garden","Python",2,1,1,"2026-04-22T21:16:43Z","Discord bot for magic garden auto-purchasing seeds"),
("wasita","wasita/proj-template","",0,0,0,"2026-01-09T20:55:46Z",""),
("wasita","wasita/food-diary","Svelte",0,0,0,"2025-12-13T01:06:43Z",""),
("wasita","wasita/send2kobo","TypeScript",0,0,0,"2025-12-12T19:09:16Z","Website for sending books to Kobo e-reader"),
("wasita","wasita/d60-keeb","",0,0,0,"2024-08-26T00:46:25Z",""),
("wasita","wasita/wins-search","CSS",1,0,0,"2023-06-03T19:01:11Z","Women in Network Science member list"),
("wasita","wasita/honeycomb-demo","JavaScript",0,0,0,"2021-12-07T21:38:28Z",""),
]

kristine_repos = [
("kristinezheng","kristinezheng/kristinezheng.github.io","HTML",0,0,0,"2026-05-14T22:29:01Z",""),
("kristinezheng","kristinezheng/Portfolio","",0,0,0,"2025-02-12T00:00:45Z","July 2021"),
("kristinezheng","kristinezheng/lookit-jenga","Jupyter Notebook",0,0,0,"2024-05-16T18:29:05Z","Lookit study for 9.85"),
("kristinezheng","kristinezheng/auditory-illusion","CSS",0,0,0,"2022-03-07T02:57:44Z","9.35 spring 2022 auditory illusion"),
("kristinezheng","kristinezheng/graph_example","Python",0,0,0,"2021-10-08T07:29:53Z",""),
("kristinezheng","kristinezheng/Green-Machine","Python",0,0,0,"2021-09-19T05:33:04Z","HackMIT 2021 Sustainability Track"),
]

m1sha_repos = [
("M1shaaa","M1shaaa/M1shaaa","",0,0,0,"2026-02-04T19:32:04Z","Config files for GitHub profile"),
("M1shaaa","M1shaaa/lab-bookshelf-","TypeScript",0,0,0,"2024-12-31T05:11:18Z",""),
("M1shaaa","M1shaaa/rosie-s-study-3-lookit-project","",0,0,0,"2024-11-04T22:15:39Z",""),
("M1shaaa","M1shaaa/Python-Lookit-Uploads","Python",0,0,0,"2024-02-15T22:59:37Z","Random projects"),
("M1shaaa","M1shaaa/Classes","",0,0,0,"2023-12-06T18:20:27Z",""),
("M1shaaa","M1shaaa/Yale-Work","HTML",0,0,0,"2023-12-06T18:33:14Z",""),
("M1shaaa","M1shaaa/MNIST-Classifier","",0,0,0,"2023-11-28T06:10:47Z",""),
("M1shaaa","M1shaaa/Lookit-Demo","",0,0,0,"2023-04-10T02:44:01Z",""),
]

austinc_repos = [
("AustinCStone","AustinCStone/EpsteinSearch","Python",0,0,0,"2026-02-11T01:10:57Z",""),
("AustinCStone","AustinCStone/bmforkupdate","Python",0,0,0,"2025-05-09T04:50:16Z",""),
("AustinCStone","AustinCStone/bmfork","Python",0,0,1,"2025-05-09T04:18:54Z",""),
("AustinCStone","AustinCStone/bitmind-fork","",0,0,0,"2025-01-09T06:16:51Z","Forked on jan 8 2025"),
("AustinCStone","AustinCStone/testLogin","Python",0,0,0,"2023-02-13T20:52:27Z",""),
("AustinCStone","AustinCStone/austincstone.github.io","HTML",0,0,0,"2021-10-23T22:48:49Z",""),
("AustinCStone","AustinCStone/test","",0,0,0,"2021-09-21T21:15:50Z",""),
("AustinCStone","AustinCStone/stonks","Python",0,0,0,"2020-09-04T22:54:35Z","Playing around with option calculations"),
("AustinCStone","AustinCStone/Z-order-curve","Python",0,0,0,"2019-06-09T02:53:43Z","Space filling z-order curve demo"),
("AustinCStone","AustinCStone/LensBuilder","Python",0,0,0,"2019-04-04T04:28:08Z","Optimize surface of a focusing lens"),
("AustinCStone","AustinCStone/TFBirds","Python",0,0,0,"2019-01-30T08:07:22Z","Bird flocking simulator in TensorFlow"),
("AustinCStone","AustinCStone/StructureFromMotion","Python",1,0,0,"2019-04-26T19:43:12Z","Recover 3D geometry from videos"),
("AustinCStone","AustinCStone/OptimalControl","Python",0,0,0,"2018-02-03T08:08:51Z","Control theory concepts"),
("AustinCStone","AustinCStone/LearningCuda","C",0,0,0,"2017-11-05T20:31:07Z","CUDA by example"),
("AustinCStone","AustinCStone/TextGAN","Python",92,30,5,"2025-03-03T13:26:32Z","GAN for text generation in TensorFlow"),
("AustinCStone","AustinCStone/StereoVisionMRF","Python",11,4,0,"2026-04-01T07:39:41Z","Infer depth from stereo images with MRF"),
("AustinCStone","AustinCStone/SpectralClustering","Python",3,2,0,"2021-04-16T08:46:36Z","Spectral clustering homework"),
("AustinCStone","AustinCStone/statsHw2","Python",0,0,0,"2015-09-28T00:50:31Z","Simple linear regression"),
("AustinCStone","AustinCStone/StatsModelingHw1","Python",0,0,0,"2015-09-19T04:13:53Z","Statistical modeling homework"),
("AustinCStone","AustinCStone/ConvNet","Python",0,0,0,"2015-09-07T22:25:29Z","Deep CNN for MNIST"),
("AustinCStone","AustinCStone/TheanoStuff","Python",0,0,0,"2021-09-04T03:21:57Z","Getting acquainted with Theano"),
("AustinCStone","AustinCStone/bash_profile","",0,0,0,"2015-08-26T17:59:33Z","bash profile"),
("AustinCStone","AustinCStone/Founderati-Server","Python",0,1,0,"2015-08-25T19:17:45Z","Server for Founderati"),
("AustinCStone","AustinCStone/Founderati-client","JavaScript",0,1,0,"2015-08-25T19:16:58Z","AngelList / LinkedIn alternative for entrepreneurs"),
("AustinCStone","AustinCStone/logisticRegressionHaskell","Haskell",1,0,0,"2018-02-02T13:34:28Z","Logistic regression in Haskell for MNIST"),
("AustinCStone","AustinCStone/Genetic-Algorithm-Sorting-Network","Python",0,0,0,"2015-05-09T03:20:47Z",""),
("AustinCStone","AustinCStone/RealTimeRayTracingFractalWorld","C++",0,0,0,"2015-05-11T01:57:30Z","Real time ray tracing fractal world"),
("AustinCStone","AustinCStone/gibbs_sampling","Python",0,0,0,"2023-07-23T17:30:23Z","Gibbs sampling and ancestral rejection sampling"),
("AustinCStone","AustinCStone/lexer","C",0,0,0,"2015-02-09T22:45:55Z","Lexer for prolog"),
("AustinCStone","AustinCStone/HTTPCache","Java",0,0,0,"2015-02-05T22:04:01Z","HTTP URL response caching"),
]

all_repo_groups = [
    plurigrid_repos, kubeflow_repos, teglon_repos,
    bmorphism_repos, zubyul_repos, migalkin_repos,
    djedamski_repos, wasita_repos, kristine_repos,
    m1sha_repos, austinc_repos,
]

# Flatten and assign IDs
flat_repos = []
for group in all_repo_groups:
    flat_repos.extend(group)

# Insert world_increments (one per source)
sources = [
    ("org", "plurigrid"), ("org", "kubeflow"), ("org", "TeglonLabs"),
    ("user", "bmorphism"), ("user", "zubyul"),
    ("user", "migalkin"), ("user", "DJedamski"), ("user", "wasita"),
    ("user", "kristinezheng"), ("user", "M1shaaa"), ("user", "AustinCStone"),
]

print(f"Inserting {len(sources)} world_increment records...")
for i, (src_type, src_name) in enumerate(sources, 1):
    trit, color, name = gf3(i)
    h = snap_hash(f"{src_type}:{src_name}:{NOW}")
    conn.execute("""
        INSERT INTO world_increments (id, gf3_trit, gf3_color, gf3_name,
            source_type, source_name, event_type, repo_name, actor, snapshot_hash)
        VALUES (?, ?, ?, ?, ?, ?, 'repo_sweep', '', ?, ?)
    """, [i, trit, color, name, src_type, src_name, src_name, h])

print("Inserting repo_snapshots...")
for seq, r in enumerate(flat_repos, 1):
    # Find which increment this belongs to
    src = r[0]
    inc_id = next(i for i, (_, s) in enumerate(sources, 1) if s == src)
    org_user, full_name, lang, stars, forks, issues, pushed, desc = r
    repo_name = full_name.split("/", 1)[1] if "/" in full_name else full_name
    stars_int = int(stars) if isinstance(stars, (int, float)) else 0
    forks_int = int(forks) if isinstance(forks, (int, float)) else 0
    issues_int = int(issues) if isinstance(issues, (int, float)) else 0
    conn.execute("""
        INSERT INTO repo_snapshots (id, increment_id, org_or_user, repo_name,
            full_name, language, stars, forks, open_issues, pushed_at, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [seq, inc_id, org_user, repo_name, full_name, lang,
          stars_int, forks_int, issues_int, pushed, desc[:255]])

print("Inserting aptos_snapshots...")
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
    conn.execute("INSERT INTO aptos_snapshots (world, address, balance_apt) VALUES (?,?,?)",
                 [world, addr, bal])

print("Inserting multisig_probes...")
multisigs = [
    ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2),
    ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2),
    ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2),
    ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2),
    ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2),
]
for pair, addr, sigs in multisigs:
    conn.execute("INSERT INTO multisig_probes (pair, address, sigs_required, healthy) VALUES (?,?,?,?)",
                 [pair, addr, sigs, sigs > 0])

print("Verifying counts...")
for tbl in ["world_increments","repo_snapshots","aptos_snapshots","multisig_probes"]:
    cnt = conn.execute(f"SELECT COUNT(*) FROM {tbl}").fetchone()[0]
    print(f"  {tbl}: {cnt} rows")

conn.close()
print("Done!")
