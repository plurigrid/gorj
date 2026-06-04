#!/usr/bin/env python3
"""Build the world-increment DuckDB ducklake."""
import duckdb
import hashlib
from datetime import datetime

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
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
con.execute("CREATE SEQUENCE IF NOT EXISTS increment_seq START 1")
con.execute("CREATE SEQUENCE IF NOT EXISTS repo_seq START 1")
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

def gf3(id_):
    m = id_ % 3
    if m == 0: return (0, "#d3869b", "ERGODIC")
    if m == 1: return (1, "#b8bb26", "PLUS")
    return (-1, "#cc241d", "MINUS")

def snap_hash(s): return hashlib.sha256(s.encode()).hexdigest()[:16]

# ── Repo data ─────────────────────────────────────────────────────────────
# Format: (org_or_user, full_name, language, stars, forks, open_issues, pushed_at, description)
REPOS = [
# plurigrid
("plurigrid","plurigrid/place","TeX",1,2,11,"2026-06-03T07:12:32Z",None),
("plurigrid","plurigrid/eirobri","Clojure",0,0,29,"2026-06-03T20:43:46Z","EiRoBri replay world"),
("plurigrid","plurigrid/nash-portal","Rust",2,3,1,"2026-05-19T01:49:59Z","NASH token TUI in the browser"),
("plurigrid","plurigrid/gorj","Clojure",0,0,337,"2026-06-04T01:22:53Z","forj + Rama topology nREPL routing + GF(3) gay trit coloring"),
("plurigrid","plurigrid/zig-syrup","Zig",2,2,0,"2026-04-30T03:52:16Z","High-performance Zig implementation of OCapN Syrup"),
("plurigrid","plurigrid/asi","HTML",24,6,4,"2026-04-26T08:51:41Z","everything is topological chemputer!"),
("plurigrid","plurigrid/asi-skills","Julia",3,1,0,"2026-04-26T08:09:26Z","69 skills with Galois Hole Type accessibility"),
("plurigrid","plurigrid/bci-blue-share","JavaScript",0,0,0,"2026-04-26T07:08:03Z","BCI signal infrastructure"),
("plurigrid","plurigrid/nanoclj-zig","Zig",1,2,20,"2026-04-25T07:29:09Z","NaN-boxed Clojure interpreter in Zig 0.15"),
("plurigrid","plurigrid/spi-race","Swift",0,0,0,"2026-04-21T19:31:56Z","Splitmix Parallel Integrity"),
("plurigrid","plurigrid/reafference","HTML",0,0,0,"2026-04-16T05:21:49Z","Reafference adaptation workspace"),
("plurigrid","plurigrid/web-browser","Rust",0,0,0,"2026-04-10T02:54:47Z","web-browser from prepostweb lineage"),
("plurigrid","plurigrid/vivarium","Clojure",1,0,0,"2026-04-08T08:38:37Z",None),
("plurigrid","plurigrid/flowglad-rs","Rust",0,0,0,"2026-04-08T07:56:15Z",None),
("plurigrid","plurigrid/tree-sitter-nanoclj-zig","C",0,0,0,"2026-04-04T07:48:21Z","Tree-sitter grammar for nanoclj-zig"),
("plurigrid","plurigrid/forester","XSLT",0,0,0,"2026-03-30T01:32:26Z","CatColab mathematical documentation forest"),
("plurigrid","plurigrid/gatomic","Clojure",0,0,0,"2026-03-30T00:54:48Z","Deterministic color identity store with sonification"),
("plurigrid","plurigrid/blue","TeX",0,0,0,"2026-03-29T23:06:32Z",None),
("plurigrid","plurigrid/red",None,0,0,0,"2026-03-29T22:58:46Z",None),
("plurigrid","plurigrid/nblm-flashcards","Hy",0,0,0,"2026-03-26T08:23:01Z","NotebookLM Enterprise flashcard pipeline"),
("plurigrid","plurigrid/gemini-agent","Python",0,0,0,"2026-02-19T06:39:16Z",None),
("plurigrid","plurigrid/graded-optic","Haskell",0,0,0,"2026-02-08T16:10:16Z","Semiring-graded bidirectional processes"),
("plurigrid","plurigrid/json-canvas",None,0,0,0,"2026-02-06T06:50:57Z","JSON Canvas: Real-time interaction data capture"),
("plurigrid","plurigrid/shepherd","Scheme",0,0,0,"2026-01-23T07:47:28Z","Spritely Shepherd - Service manager"),
("plurigrid","plurigrid/goblinshare","Scheme",0,0,0,"2026-01-23T07:47:12Z","P2P filesharing demo for Goblins"),
("plurigrid","plurigrid/magenc","Scheme",0,0,0,"2026-01-23T07:47:11Z","Magenc Magnet URIs"),
("plurigrid","plurigrid/hoot","Scheme",0,0,1,"2026-01-23T07:47:10Z","Spritely Hoot - Scheme to WebAssembly compiler"),
("plurigrid","plurigrid/leprechauns","Racket",0,0,0,"2026-01-23T07:46:46Z","Spritely Goblins + Gay.jl semantic colors"),
("plurigrid","plurigrid/spritely-semantic-colors",None,0,0,0,"2026-01-23T07:38:32Z","Deterministic color mappings for Spritely"),
("plurigrid","plurigrid/gay-tofu","HTML",0,0,0,"2026-01-08T15:14:34Z","Low-discrepancy color sequences for visual TOFU"),
("plurigrid","plurigrid/lazygay","Go",0,0,0,"2026-01-08T14:19:25Z","lazygit fork with Gay.jl deterministic commit coloring"),
("plurigrid","plurigrid/gay-terminal","Rust",0,0,0,"2026-01-08T14:19:24Z","Terminal ANSI coloring with Gay.jl"),
("plurigrid","plurigrid/gay-go","Go",0,0,0,"2026-01-08T14:19:23Z","Go implementation of Gay.jl deterministic coloring"),
("plurigrid","plurigrid/gay-rs","Rust",0,0,0,"2026-01-08T14:19:22Z","Rust crate for Gay.jl deterministic coloring"),
("plurigrid","plurigrid/lazybjj","Rust",0,0,0,"2026-01-08T14:19:19Z","TUI for jj with Gay.jl GF(3) coloring"),
("plurigrid","plurigrid/agent-o-rama","Clojure",0,0,0,"2026-01-02T01:09:22Z",None),
("plurigrid","plurigrid/aptos-wallet-ruby","Ruby",1,0,0,"2025-09-30T22:47:22Z",None),
("plurigrid","plurigrid/duck-kanban","Rust",1,0,0,"2025-09-26T20:18:38Z","Duck intelligence kanban system"),
("plurigrid","plurigrid/shiteshiteshite",None,0,0,0,"2025-09-26T03:07:20Z","Duck intelligence kanban system"),
("plurigrid","plurigrid/discohy","Hy",0,0,0,"2025-09-10T02:01:31Z",None),
("plurigrid","plurigrid/telemind",None,0,0,0,"2025-06-12T05:54:59Z",None),
("plurigrid","plurigrid/ontology","JavaScript",8,9,16,"2025-05-27T18:18:34Z","autopoietic ergodicity and embodied gradualism"),
("plurigrid","plurigrid/Plurigraph","JavaScript",3,5,4,"2025-01-05T08:39:09Z","Plurigrid knowledge base for use with Obsidian.md"),
("plurigrid","plurigrid/signe","Python",0,0,0,"2024-08-15T20:52:03Z","Signal messages data traversal"),
("plurigrid","plurigrid/SwiftDuck",None,0,0,0,"2024-08-08T18:19:06Z",None),
("plurigrid","plurigrid/act","Python",3,1,4,"2024-07-26T08:27:08Z","building blocks for cognitive category theory"),
("plurigrid","plurigrid/xenomorphic",None,0,0,0,"2024-04-09T03:24:55Z",None),
("plurigrid","plurigrid/metamorphic",None,0,0,0,"2024-04-09T03:22:41Z",None),
("plurigrid","plurigrid/DiffusionVoiceDemo","Clojure",0,0,0,"2024-04-02T18:09:01Z",None),
("plurigrid","plurigrid/website","Clojure",0,1,0,"2024-03-30T04:37:51Z",None),
("plurigrid","plurigrid/StochFlow","Python",4,1,0,"2024-03-20T23:34:57Z","stochastic interpolant models"),
("plurigrid","plurigrid/intent",None,0,0,0,"2024-03-04T04:53:38Z","Simulations for An Analysis of Intent Markets"),
("plurigrid","plurigrid/novella","TypeScript",1,0,0,"2024-01-27T08:12:55Z",None),
("plurigrid","plurigrid/ACT.jl","Julia",0,0,0,"2024-01-21T00:02:25Z","applied categorical duck cybernetics"),
("plurigrid","plurigrid/ducklings","TypeScript",0,0,15,"2023-12-25T07:34:27Z",None),
("plurigrid","plurigrid/paretae","TypeScript",0,0,14,"2023-11-20T05:14:42Z",None),
("plurigrid","plurigrid/experiments",None,0,0,0,"2023-11-17T05:39:07Z","Learning from Penrose development"),
("plurigrid","plurigrid/fuckit","Clojure",0,0,0,"2023-11-14T21:26:14Z",None),
("plurigrid","plurigrid/omega","Clojure",0,0,0,"2023-11-07T21:08:46Z",None),
("plurigrid","plurigrid/org","Jupyter Notebook",2,0,1,"2023-11-07T01:08:05Z","Dynamically Replicating Duck"),
("plurigrid","plurigrid/CVAE-Flows",None,0,0,0,"2023-10-24T14:41:32Z","dihypergraphs and latent spaces"),
("plurigrid","plurigrid/morph-prover-cli",None,0,1,0,"2023-10-18T03:49:03Z","Lean4"),
("plurigrid","plurigrid/uncharacter","TypeScript",0,0,0,"2023-09-19T20:17:46Z",None),
("plurigrid","plurigrid/chateau","TypeScript",0,0,0,"2023-08-30T20:11:12Z",None),
("plurigrid","plurigrid/gmgm",None,0,0,1,"2023-08-25T13:54:00Z",None),
("plurigrid","plurigrid/tuttle","TypeScript",0,0,0,"2023-08-09T17:40:44Z",None),
("plurigrid","plurigrid/mesoplay",None,0,0,0,"2023-08-09T06:19:03Z",None),
("plurigrid","plurigrid/am","Python",0,0,0,"2023-08-05T12:46:33Z",None),
("plurigrid","plurigrid/compose",None,0,0,2,"2023-07-24T06:18:48Z",None),
("plurigrid","plurigrid/flussi",None,0,0,1,"2023-07-15T06:40:11Z",None),
("plurigrid","plurigrid/cf",None,0,0,0,"2023-07-11T08:11:29Z",None),
("plurigrid","plurigrid/poepoe",None,0,0,1,"2023-07-09T22:20:50Z",None),
("plurigrid","plurigrid/marketplace",None,0,0,1,"2023-07-09T05:52:30Z",None),
("plurigrid","plurigrid/smoller",None,0,0,1,"2023-07-06T07:38:04Z",None),
("plurigrid","plurigrid/liquidity",None,0,0,1,"2023-07-06T02:07:28Z",None),
("plurigrid","plurigrid/solid-rs",None,0,0,1,"2023-07-05T21:58:05Z",None),
("plurigrid","plurigrid/solid","Python",0,0,0,"2023-07-05T21:52:25Z",None),
("plurigrid","plurigrid/ipegrafo","Python",0,0,0,"2023-07-03T07:29:40Z",None),
("plurigrid","plurigrid/plurigrid-v4","TypeScript",0,0,0,"2023-07-03T06:31:59Z",None),
("plurigrid","plurigrid/novella-v3",None,0,0,0,"2023-07-03T06:29:40Z",None),
("plurigrid","plurigrid/polyglottal","TypeScript",0,0,0,"2023-07-03T06:23:45Z",None),
("plurigrid","plurigrid/novella-v2",None,0,0,0,"2023-07-03T06:22:38Z",None),
("plurigrid","plurigrid/cocreation-ui",None,0,0,2,"2023-07-03T04:45:53Z",None),
("plurigrid","plurigrid/smol",None,0,0,1,"2023-07-02T08:45:32Z",None),
("plurigrid","plurigrid/commons","TypeScript",0,0,0,"2023-06-27T05:46:24Z",None),
("plurigrid","plurigrid/post-web","Svelte",0,0,0,"2023-06-18T00:24:24Z",None),
("plurigrid","plurigrid/microworlds","Rust",3,5,3,"2023-05-13T03:54:56Z","alien worlds"),
("plurigrid","plurigrid/pills",None,0,0,0,"2023-05-02T10:03:03Z","metaphors for embodied gradualism"),
("plurigrid","plurigrid/plurigrid-rs","Rust",0,0,0,"2023-04-21T01:02:56Z",None),
("plurigrid","plurigrid/plurigrid-game.github.io","HTML",0,0,1,"2023-04-20T00:17:55Z",None),
("plurigrid","plurigrid/synth","Rust",0,0,0,"2023-04-15T01:56:45Z",None),
("plurigrid","plurigrid/birbs","C++",0,0,0,"2023-04-15T01:56:32Z","Build native CosmWasm apps w/ Dart and Flutter"),
("plurigrid","plurigrid/agent","Python",5,1,6,"2023-03-31T18:45:23Z","Framework for agency amplification"),
("plurigrid","plurigrid/vcg-auction","Rust",7,2,1,"2023-03-16T21:53:08Z","simple contract that performs a VCG auction"),
("plurigrid","plurigrid/bidder","Dart",0,0,1,"2023-03-15T15:23:22Z","simple flutter app for bidding in a vcg auction"),
("plurigrid","plurigrid/plurigrid.github.io","HTML",1,2,2,"2023-01-20T03:27:34Z",None),
("plurigrid","plurigrid/VPP","Julia",0,1,0,"2023-01-11T18:41:07Z","Hyperreal Power Plant"),
("plurigrid","plurigrid/grid","TypeScript",2,1,1,"2023-01-02T11:55:55Z","Plurigrid Testnet #0: Edith Clarke"),
("plurigrid","plurigrid/commons-contracts","Rust",0,0,0,"2022-09-09T09:20:11Z","CosmWasm contracts to implement Commons Stack"),
("plurigrid","plurigrid/plurigrid.xyz","TypeScript",0,0,1,"2022-08-31T05:26:14Z",None),
# kubeflow
("kubeflow","kubeflow/pipelines","Python",4151,2004,490,"2026-06-03T21:06:23Z","Machine Learning Pipelines for Kubeflow"),
("kubeflow","kubeflow/trainer","Go",2110,964,129,"2026-06-03T17:02:37Z","Distributed AI Model Training on Kubernetes"),
("kubeflow","kubeflow/spark-operator","Python",3124,1488,101,"2026-06-03T17:01:00Z","Kubernetes operator for Apache Spark"),
("kubeflow","kubeflow/hub","Go",175,182,43,"2026-06-04T00:19:49Z","Model Registry for ML model developers"),
("kubeflow","kubeflow/notebooks",None,73,118,183,"2026-06-02T20:24:23Z","Kubeflow Notebooks for AI/ML workloads"),
("kubeflow","kubeflow/community","Jupyter Notebook",195,257,17,"2026-06-02T15:52:13Z","Kubeflow community information"),
("kubeflow","kubeflow/sdk","Python",120,181,136,"2026-06-03T15:18:55Z","Universal Python SDK for AI workloads on Kubernetes"),
("kubeflow","kubeflow/kale","Python",690,155,48,"2026-06-01T23:05:01Z","Kubeflow superfood for Data Scientists"),
("kubeflow","kubeflow/internal-acls","Go",19,388,2,"2026-06-01T16:22:32Z","Group ACLs for Kubeflow developers"),
("kubeflow","kubeflow/mcp-apache-spark-history-server","Python",173,61,21,"2026-06-01T19:56:25Z","MCP Server for Apache Spark History Server"),
("kubeflow","kubeflow/manifests","YAML",1020,1065,26,"2026-06-02T18:56:27Z","Kubeflow AI Reference Platform Deployment Manifests"),
("kubeflow","kubeflow/mpi-operator","Go",528,235,103,"2026-06-02T14:30:58Z","Kubernetes Operator for MPI-based applications"),
("kubeflow","kubeflow/pipelines-components","Python",11,42,32,"2026-06-03T23:40:46Z","Kubeflow Pipelines components"),
("kubeflow","kubeflow/website","HTML",184,921,50,"2026-05-28T14:05:25Z","Kubeflow Website"),
("kubeflow","kubeflow/katib","Python",1685,525,121,"2026-06-04T01:14:59Z","Automated Machine Learning on Kubernetes"),
("kubeflow","kubeflow/mlflow-integration","Python",6,3,2,"2026-05-27T15:42:37Z",None),
("kubeflow","kubeflow/blog","Jupyter Notebook",32,62,26,"2026-05-25T13:02:24Z","Kubeflow blog"),
("kubeflow","kubeflow/kubeflow",None,15704,2668,3,"2026-05-24T11:31:41Z","Machine Learning Toolkit for Kubernetes"),
("kubeflow","kubeflow/dashboard","TypeScript",16,57,84,"2026-06-03T21:08:19Z","Kubeflow Central Dashboard"),
("kubeflow","kubeflow/mcp-server","Python",10,18,22,"2026-05-12T10:14:24Z","MCP Server for Kubeflow Tools"),
("kubeflow","kubeflow/arena","Go",811,191,49,"2026-05-07T06:46:17Z","A CLI for Kubeflow"),
("kubeflow","kubeflow/docs-agent","Python",37,95,151,"2026-04-14T03:33:15Z","Kubeflow Documentation AI Agent"),
("kubeflow","kubeflow/examples","Jsonnet",1462,756,111,"2025-04-14T01:54:52Z","Extended examples and tutorials"),
("kubeflow","kubeflow/testing","Python",60,86,33,"2025-02-14T18:33:13Z","Test infrastructure and tooling for Kubeflow"),
("kubeflow","kubeflow/kfp-tekton","TypeScript",182,123,79,"2024-11-19T12:23:51Z","Kubeflow Pipelines on Tekton"),
("kubeflow","kubeflow/kfserving-lts","Jsonnet",12,19,51,"2024-08-02T16:25:44Z",None),
("kubeflow","kubeflow/kubebench","Jsonnet",78,35,68,"2024-06-17T19:22:04Z","Repository for benchmarking"),
("kubeflow","kubeflow/fate-operator","Go",51,15,6,"2024-02-22T19:44:08Z","Fate operator"),
("kubeflow","kubeflow/kfctl","Go",182,134,94,"2023-08-15T20:19:22Z","CLI for deploying and managing Kubeflow"),
("kubeflow","kubeflow/kfp-tekton-backend","TypeScript",8,6,46,"2023-08-14T22:05:04Z","Tekton yaml behind KFP API"),
("kubeflow","kubeflow/common","Go",53,70,40,"2023-05-28T13:16:00Z","Common APIs for Kubeflow operators"),
("kubeflow","kubeflow/.allstar",None,2,0,0,"2022-12-06T23:07:59Z",None),
("kubeflow","kubeflow/fairing","Jsonnet",337,143,134,"2022-04-11T05:28:47Z","Python SDK for building and training ML models"),
("kubeflow","kubeflow/xgboost-operator","Python",77,53,22,"2021-12-01T18:00:10Z","Incubating project for xgboost operator"),
("kubeflow","kubeflow/mxnet-operator","Go",52,33,9,"2021-12-01T17:47:19Z","Kubernetes operator for mxnet jobs"),
("kubeflow","kubeflow/pytorch-operator","Jsonnet",310,143,63,"2021-12-01T17:44:48Z","PyTorch on Kubernetes"),
("kubeflow","kubeflow/frontend","JavaScript",8,18,12,"2021-12-01T17:41:37Z","Kubeflow frontend"),
("kubeflow","kubeflow/metadata","TypeScript",123,63,38,"2021-12-01T17:35:27Z","Metadata assets"),
("kubeflow","kubeflow/caffe2-operator","Go",16,12,2,"2021-12-01T01:58:06Z","Experimental caffe2 operator"),
("kubeflow","kubeflow/code-intelligence","Jupyter Notebook",56,20,64,"2021-12-01T01:52:58Z","ML-Powered Developer Tools"),
("kubeflow","kubeflow/example-seldon","Jupyter Notebook",172,56,9,"2021-12-01T01:49:58Z","End-to-end ML on Kubernetes"),
("kubeflow","kubeflow/batch-predict","Python",17,7,9,"2021-12-01T01:47:51Z","Batch predict repository"),
("kubeflow","kubeflow/reporting","Jsonnet",2,5,1,"2021-12-01T01:42:32Z","Metrics about Kubeflow usage"),
("kubeflow","kubeflow/chainer-operator","Jsonnet",17,15,7,"2021-11-14T13:03:57Z","Chainer operator"),
("kubeflow","kubeflow/crd-validation","Go",11,7,5,"2021-01-25T15:02:53Z","Validation Generation for Kubeflow CRD"),
("kubeflow","kubeflow/community-infra","Go",3,9,4,"2021-01-25T14:49:49Z","Declarative KF community infrastructure"),
("kubeflow","kubeflow/.github",None,2,1,0,"2020-05-12T00:22:56Z","Org wide templates"),
("kubeflow","kubeflow/marketing-materials",None,4,4,4,"2019-07-19T13:57:15Z",None),
# TeglonLabs
("TeglonLabs","TeglonLabs/mathpix-gem","Ruby",2,0,11,"2026-01-01T12:13:13Z","Transform mathematical images to LaTeX with security-first design"),
("TeglonLabs","TeglonLabs/coin-flip-mcp","JavaScript",0,2,1,"2025-09-21T08:57:27Z","MCP server for flipping coins with varying degrees of randomness"),
("TeglonLabs","TeglonLabs/monad-mcp-server",None,0,0,0,"2025-05-14T11:36:14Z","Monad MCP Server"),
("TeglonLabs","TeglonLabs/topoi","Python",0,0,1,"2025-01-24T04:49:26Z",None),
# bmorphism
("bmorphism","bmorphism/world","Python",0,0,0,"2026-06-02T06:49:02Z","Local worlds launcher for SA3, jank, and world proofs"),
("bmorphism","bmorphism/Gay.jl","Julia",1,0,189,"2026-06-04T00:48:40Z","Wide-gamut color sampling with splittable determinism"),
("bmorphism","bmorphism/oxgame","OCaml",0,0,0,"2026-05-15T09:53:27Z","Stellar resolution and open-game composition for OCaml"),
("bmorphism","bmorphism/nanoclj-zig","Zig",0,0,0,"2026-05-07T20:12:15Z",None),
("bmorphism","bmorphism/zig-syrup","Zig",0,0,0,"2026-05-07T19:49:05Z","Embeddable OCapN Syrup in Zig"),
("bmorphism","bmorphism/boxxy","Move",0,1,0,"2026-04-30T03:35:47Z",None),
("bmorphism","bmorphism/postweb","Go",0,0,0,"2026-04-09T10:51:57Z","postweb from prepostweb"),
("bmorphism","bmorphism/shitcoin","Python",5,0,0,"2026-04-08T08:07:08Z","denom for cw20 assets for permissionless degeneracy"),
("bmorphism","bmorphism/magic-world-org","Python",1,0,0,"2026-04-05T07:03:50Z","Magic World Org (Local MLX)"),
("bmorphism","bmorphism/ocaml-mcp-sdk","OCaml",61,2,0,"2026-03-16T05:24:25Z","OCaml SDK for Model Context Protocol"),
("bmorphism","bmorphism/flox-mcp-bb","Clojure",0,0,0,"2026-02-12T02:45:43Z","Open-source MCP server for Flox"),
("bmorphism","bmorphism/vibesnipe-market","Move",0,0,9,"2026-02-05T10:23:25Z",None),
("bmorphism","bmorphism/tapes",None,0,0,0,"2026-02-04T02:23:37Z","VHS tapes for terminal recordings"),
("bmorphism","bmorphism/duck-rio-heateq","Rust",0,0,0,"2026-02-02T23:33:32Z",None),
("bmorphism","bmorphism/aella","Rascal",1,0,0,"2026-02-01T02:44:30Z",None),
("bmorphism","bmorphism/hymlx","Python",1,0,0,"2026-01-22T12:20:32Z",None),
("bmorphism","bmorphism/GeoACSets.jl","Julia",0,1,1,"2026-01-19T13:57:13Z","Categorical data structures with geospatial capabilities"),
("bmorphism","bmorphism/anti-bullshit-mcp-server","JavaScript",23,7,1,"2026-01-16T08:54:58Z","MCP server for analyzing claims and detecting manipulation"),
("bmorphism","bmorphism/vibespace-mcp-go-ternary","HTML",0,1,3,"2026-01-11T12:50:40Z","Go implementation of MCP for vibes and worlds"),
("bmorphism","bmorphism/open-location-code-zig","Zig",3,0,0,"2025-12-30T19:33:45Z","Open Location Code for Zig"),
("bmorphism","bmorphism/bafishka","Clojure",1,0,0,"2025-12-19T09:38:00Z","Rust-native Fish shell-friendly file operations"),
("bmorphism","bmorphism/gay-color-learnable",None,0,0,0,"2025-12-15T18:41:02Z","Learnable color embeddings connecting Graphistry, Ghidra, Charm"),
("bmorphism","bmorphism/gay-hy","Hy",0,0,0,"2025-12-15T15:32:58Z","Hylang MLX color bandwidth protocol"),
("bmorphism","bmorphism/multiverse-color-game","Julia",0,0,0,"2025-12-12T05:28:11Z","Holographic Color Matching Game for VisionPro"),
("bmorphism","bmorphism/signal-mcp","Rust",0,0,0,"2025-12-11T07:20:08Z","Chromatic mode collapse via Galois connection"),
("bmorphism","bmorphism/xf.jl","Julia",0,0,0,"2025-12-05T22:12:17Z","Xenofeminist color synthesis"),
("bmorphism","bmorphism/deberta-goemotions","Python",0,0,0,"2025-10-22T18:32:24Z",None),
("bmorphism","bmorphism/monero-rental-hash-war","Haskell",1,0,0,"2025-10-05T23:08:54Z","Compositional OpenGame analysis of Monero rental hash war"),
("bmorphism","bmorphism/duck-rs","Zig",0,0,0,"2025-10-05T00:21:07Z",None),
("bmorphism","bmorphism/schoenfinkel","Python",1,0,0,"2025-10-04T23:31:11Z","Post-quantum categorical gravity framework"),
("bmorphism","bmorphism/gay-spec",None,1,0,0,"2025-10-02T02:01:56Z",None),
("bmorphism","bmorphism/bafishka-clean","Rust",1,0,0,"2025-09-25T19:22:10Z","Clean monadic Steel-SCI integration"),
("bmorphism","bmorphism/babashka-static-build","Dockerfile",1,0,0,"2025-09-05T02:26:32Z","Static musl babashka build for ARM64 Termux"),
("bmorphism","bmorphism/whale","MATLAB",2,0,0,"2025-09-04T06:55:21Z","omniglot + sperm whale codas = metawhaling"),
("bmorphism","bmorphism/infinity-topos","Python",1,0,0,"2025-08-29T05:39:49Z",None),
("bmorphism","bmorphism/elevenlabs-mcp-enhanced","Python",1,0,0,"2025-08-29T04:41:58Z","Enhanced ElevenLabs MCP server"),
("bmorphism","bmorphism/zeldar","Python",1,0,1,"2025-08-26T15:16:21Z","Burning Man Art Robot"),
("bmorphism","bmorphism/stellogen-quantum-operads",None,1,0,0,"2025-07-15T04:49:41Z","Quantum Operads and ZX-Calculus Implementation"),
("bmorphism","bmorphism/apple-container-framework","Clojure",0,0,0,"2025-07-13T12:12:10Z","Apple Container Framework - High-performance Babashka library"),
("bmorphism","bmorphism/ezkl-ethglobal2025","Python",1,0,0,"2025-07-07T01:16:01Z",None),
("bmorphism","bmorphism/zk-haiku-nanogpt","Solidity",1,0,0,"2025-07-06T03:08:24Z","ZK-Haiku-NanoGPT: Agentic Proof-Chaining Framework"),
("bmorphism","bmorphism/rama-event-processor","Java",1,0,0,"2025-07-02T07:01:44Z","Processing events with Rama"),
("bmorphism","bmorphism/oxcaml-sci-canonical","OCaml",1,0,0,"2025-06-20T06:37:12Z","Canonical OxCaml-SCI implementation"),
("bmorphism","bmorphism/oxcaml-mcp",None,0,0,0,"2025-06-20T04:04:34Z","OxCaml-MCP: High-performance Model Control Protocol server"),
("bmorphism","bmorphism/oxcaml-sci",None,0,0,0,"2025-06-20T03:48:11Z","OxCaml-SCI: Performance-optimized Scientific Computing Interface"),
("bmorphism","bmorphism/infinity-topos-impossibility",None,0,0,14,"2025-05-29T01:55:28Z","Impossibility results for automated analysis verification"),
("bmorphism","bmorphism/graphistry-mcp","Python",2,0,0,"2025-05-06T17:34:24Z","Graphistry MCP integration for graph visualization"),
("bmorphism","bmorphism/hypernym-mcp-server","JavaScript",6,5,0,"2025-04-02T21:21:08Z",None),
("bmorphism","bmorphism/vibespace-mcp-go",None,0,0,0,"2025-03-19T20:30:02Z","Go implementation of MCP for vibes and worlds with NATS"),
("bmorphism","bmorphism/krep-mcp-server","JavaScript",1,1,1,"2025-03-19T20:22:46Z","High-performance string search MCP server"),
("bmorphism","bmorphism/minecraft-mcp-golf",None,0,0,0,"2025-03-16T10:33:31Z","Minecraft server with MCP capabilities"),
("bmorphism","bmorphism/worlds-code-explorer",None,0,0,0,"2025-03-16T05:46:58Z","Explore and organize code projects from different worlds"),
("bmorphism","bmorphism/voice-fn",None,0,0,0,"2025-02-24T22:28:32Z","Clojure framework for real-time voice-enabled AI applications"),
("bmorphism","bmorphism/lumon-tui","Python",1,0,0,"2025-02-02T11:24:21Z","Terminal-based parallel worlds implementation"),
("bmorphism","bmorphism/goose-diagrams",None,0,0,0,"2025-01-31T08:46:44Z","ASCII art diagrams of Goose AI architecture"),
("bmorphism","bmorphism/MetaLab",None,0,0,0,"2025-01-30T11:40:33Z","Learning and experimenting with cutting-edge technologies"),
("bmorphism","bmorphism/penrose-mcp","JavaScript",10,4,0,"2025-01-20T21:44:55Z","Penrose server for the Infinity-Topos environment"),
("bmorphism","bmorphism/penrose-mcp-server",None,0,0,0,"2025-01-20T20:24:07Z","MCP server for Penrose system integration"),
("bmorphism","bmorphism/test-repo-3141592",None,0,0,1,"2025-01-11T15:06:57Z","Test repository"),
("bmorphism","bmorphism/manifold-mcp-server","JavaScript",14,9,5,"2025-01-11T10:36:58Z","MCP server for Manifold Markets prediction markets"),
("bmorphism","bmorphism/say-mcp-server","JavaScript",20,9,3,"2025-01-07T03:15:18Z","MCP server for macOS text-to-speech"),
("bmorphism","bmorphism/penumbra-mcp","JavaScript",5,6,3,"2025-01-07T01:15:23Z","MCP server for Penumbra blockchain"),
("bmorphism","bmorphism/nats-mcp-server",None,7,3,2,"2025-01-06T23:33:41Z","MCP server for NATS messaging system"),
("bmorphism","bmorphism/marginalia-mcp-server","JavaScript",8,6,0,"2025-01-06T05:47:24Z","MCP server for managing marginalia and annotations"),
("bmorphism","bmorphism/babashka-mcp-server","JavaScript",18,6,3,"2025-01-05T11:09:42Z","MCP server for interacting with Babashka"),
("bmorphism","bmorphism/openbci-mcp-server",None,0,0,0,"2025-01-05T07:00:10Z","MCP server for OpenBCI hardware"),
("bmorphism","bmorphism/gists-mcp-server","JavaScript",2,0,0,"2025-01-03T03:50:54Z","MCP server for GitHub Gists"),
("bmorphism","bmorphism/neural-category-diagrams",None,0,0,0,"2025-01-02T05:47:22Z","Diagrams of neural architectures through category theory"),
("bmorphism","bmorphism/slowtime-mcp-server","TypeScript",3,5,6,"2025-01-02T01:23:33Z","MCP server for secure time-based operations"),
("bmorphism","bmorphism/open-games-agda","Agda",0,0,0,"2024-12-22T11:16:29Z","Formalization of open games in Agda"),
("bmorphism","bmorphism/yoyo","Just",0,0,0,"2024-11-30T04:00:12Z",None),
("bmorphism","bmorphism/uss-cogsexy",None,0,0,0,"2024-11-23T20:52:30Z","Cognitive Firewall: information reflow and non-linear countermeasures"),
("bmorphism","bmorphism/vibes","Clojure",0,0,0,"2024-11-13T15:56:28Z","Global Vibespace"),
("bmorphism","bmorphism/untime","Swift",1,0,0,"2024-09-06T23:39:08Z",None),
("bmorphism","bmorphism/cf","Handlebars",0,0,0,"2024-08-07T01:14:25Z","collective futures"),
("bmorphism","bmorphism/collective",None,0,0,0,"2024-08-07T01:08:28Z",None),
("bmorphism","bmorphism/pretopos","TeX",0,0,0,"2024-07-27T12:34:14Z",None),
("bmorphism","bmorphism/c-house-town","TypeScript",1,0,0,"2024-07-25T21:13:04Z",None),
("bmorphism","bmorphism/galahack2024","TypeScript",2,0,0,"2024-03-21T15:43:19Z",None),
("bmorphism","bmorphism/crags","Python",1,0,0,"2024-01-14T04:21:45Z","RAGs. categorically."),
("bmorphism","bmorphism/hacker-news-alert-chatgpt-slack","Rust",0,0,0,"2023-08-31T09:56:37Z","Monitor Hacker News with ChatGPT"),
("bmorphism","bmorphism/summarize-github-issues","Rust",0,0,0,"2023-08-31T09:44:28Z","Summarize GitHub issues with ChatGPT"),
("bmorphism","bmorphism/slackduck","Rust",0,0,0,"2023-08-31T09:24:05Z","A Slack bot with ChatGPT backend"),
("bmorphism","bmorphism/telega","Rust",1,0,0,"2023-08-23T17:20:29Z","absurd wasm32-wasi flow connecting components"),
("bmorphism","bmorphism/io","Handlebars",0,0,0,"2023-08-20T07:15:36Z",None),
("bmorphism","bmorphism/mesocunt2001","Rust",0,0,0,"2023-08-19T07:49:43Z","Customized Telegram bot with Claude backend"),
("bmorphism","bmorphism/mesocunt","Rust",0,0,0,"2023-08-18T10:13:33Z","Customizable Discord bot with ChatGPT backend"),
("bmorphism","bmorphism/meso","Jupyter Notebook",1,1,0,"2023-08-09T06:04:11Z","Scripts simulating inverse transformations of Markov Kernels"),
("bmorphism","bmorphism/monaduck69","Svelte",0,0,1,"2023-07-19T12:43:12Z","SvelteKit template"),
("bmorphism","bmorphism/banana","Python",0,0,0,"2023-02-23T15:12:07Z",None),
("bmorphism","bmorphism/Plurigrid.jl","Julia",0,1,0,"2023-01-04T14:53:02Z",None),
("bmorphism","bmorphism/plurigrid-celo","TypeScript",1,1,0,"2022-12-09T10:07:25Z","Celo e-app for Albany Plurigrid"),
("bmorphism","bmorphism/risc0-cosmwasm-example","Rust",23,2,1,"2022-10-20T23:50:40Z","CosmWasm + zkVM RISC-V EFI template"),
("bmorphism","bmorphism/knxwledge",None,0,1,1,"2022-10-02T02:23:31Z",None),
("bmorphism","bmorphism/OTC-0","JavaScript",3,0,0,"2022-06-07T22:18:08Z",None),
("bmorphism","bmorphism/matrix5",None,0,0,0,"2022-05-25T06:01:57Z","glowing in public"),
("bmorphism","bmorphism/pluridrop","TypeScript",2,0,0,"2022-04-10T00:13:47Z","ETHPortland2022 hack"),
("bmorphism","bmorphism/kfsummit19","Python",0,0,0,"2019-10-28T16:40:46Z","Kubeflow pipelines on Anthos"),
("bmorphism","bmorphism/recommenders","Python",0,0,0,"2019-09-11T07:43:03Z",None),
("bmorphism","bmorphism/deepfakes","Python",1,0,2,"2019-04-28T22:53:40Z",None),
# zubyul
("zubyul","zubyul/voice-observatory","Python",0,0,0,"2026-04-24T05:56:17Z","Passive macOS TUI observing voice-download pathways"),
("zubyul","zubyul/ghostel-emacs-worlds","GLSL",0,0,0,"2026-04-24T00:20:56Z","Ghostty config + ghostel family + alice/bob emacs-mods"),
("zubyul","zubyul/nash-tui","Rust",0,0,0,"2026-04-13T07:45:16Z","NASH token TUI: real-time candles via GeckoTerminal"),
("zubyul","zubyul/nash-web","Rust",0,0,0,"2026-04-13T07:08:58Z","NASH token browser TUI via ratzilla WASM"),
("zubyul","zubyul/big-bad-plurigrid-quiz","Emacs Lisp",0,0,0,"2026-04-09T18:51:31Z","27 flashcards from bmorphism/plurigrid/zubyul activity"),
("zubyul","zubyul/Gay.jl","Julia",0,0,0,"2026-03-28T11:30:01Z","Wide-gamut color sampling with splittable determinism"),
("zubyul","zubyul/kinesis-kb360pro","Python",0,0,0,"2026-03-26T10:29:40Z","Claude Code skill for Kinesis Advantage360 Pro"),
("zubyul","zubyul/gay-world","Python",1,1,0,"2026-03-26T04:03:39Z","Goblin world builder: each goblin is a world"),
("zubyul","zubyul/from-possible-worlds","TeX",0,0,0,"2026-03-16T03:14:55Z",None),
("zubyul","zubyul/tilelang-kernels","Python",0,0,0,"2026-03-16T02:31:13Z","TileLang GPU kernels for SplitMix64 color generation"),
("zubyul","zubyul/fleet-bootstrap","Shell",0,0,0,"2026-02-23T08:19:58Z",None),
("zubyul","zubyul/gay-terminal-colors","Clojure",0,0,0,"2026-02-21T07:38:14Z","Gay.jl world_terminal_fingerprint"),
("zubyul","zubyul/basin","Rust",0,0,0,"2026-02-13T10:31:47Z",None),
("zubyul","zubyul/openbci-visualizer","Zig",0,0,0,"2026-02-04T11:17:41Z",None),
("zubyul","zubyul/plurigrid-site","Svelte",0,1,11,"2026-02-04T03:20:08Z","Plurigrid world: site deployment"),
("zubyul","zubyul/repl","Python",0,0,0,"2026-02-04T01:08:15Z",None),
("zubyul","zubyul/instance-onboarding","Shell",0,0,0,"2026-02-02T11:44:07Z",None),
("zubyul","zubyul/vibesnipe","Move",0,0,1,"2026-01-30T22:36:03Z",None),
("zubyul","zubyul/zubyul.github.io","CSS",1,0,0,"2026-01-27T03:24:34Z",None),
("zubyul","zubyul/toad-warpify-extension","Python",0,0,0,"2026-01-17T07:48:40Z","Warpify extension for Toad - enables ACP agents"),
("zubyul","zubyul/thread-site","Haskell",0,0,0,"2025-12-23T23:53:27Z",None),
("zubyul","zubyul/GayMove","Move",0,0,0,"2025-12-18T09:40:08Z",None),
("zubyul","zubyul/gay-brain-world","Python",0,0,0,"2025-12-16T01:19:28Z","Gay.jl SPI colors for Moduleur Brain"),
("zubyul","zubyul/multiplayer","HTML",0,0,0,"2025-12-12T08:56:16Z",None),
("zubyul","zubyul/cat-world","TypeScript",0,0,0,"2025-12-12T08:47:14Z","Cat gaze tracker with bird videos"),
("zubyul","zubyul/hue-world","JavaScript",0,0,0,"2025-12-12T08:32:59Z","Terminal Vibe Snipe puzzle game"),
("zubyul","zubyul/multiplayer-emacs","HTML",0,0,0,"2025-12-12T08:07:38Z","Multiplayer Emacs split-pane Vibe Snipe"),
("zubyul","zubyul/vibe-snipe","Kotlin",0,0,0,"2025-12-12T03:46:26Z",None),
("zubyul","zubyul/chromatic-vrf","Kotlin",0,0,0,"2025-12-12T03:26:22Z","Chromatic VRF: I Love Hue puzzle with Gay.jl MCMC"),
("zubyul","zubyul/quantum-telephone","Jupyter Notebook",0,0,0,"2025-12-08T22:54:16Z","Quantum telephone world: entangled message passing"),
("zubyul","zubyul/c-elegans-connectome","JavaScript",0,0,0,"2025-11-22T15:43:55Z",None),
("zubyul","zubyul/zoterobsidian","Shell",0,0,0,"2025-09-28T16:50:50Z",None),
("zubyul","zubyul/cascade-world","Python",1,0,0,"2025-09-19T18:25:12Z","Cascade development environment"),
("zubyul","zubyul/plurigrid-playbook",None,0,0,0,"2025-09-17T02:10:35Z",None),
("zubyul","zubyul/defcon","JavaScript",1,0,0,"2025-09-17T02:07:00Z",None),
("zubyul","zubyul/ghostty-modifications","JavaScript",1,0,0,"2025-09-15T02:45:21Z","Ghostty terminal modifications and MCP servers"),
("zubyul","zubyul/GoofyLifeChoices","Python",1,0,0,"2025-07-30T18:48:13Z",None),
("zubyul","zubyul/book","HTML",0,0,0,"2025-05-15T20:30:39Z",None),
("zubyul","zubyul/ezAR",None,0,0,0,"2025-02-03T21:02:26Z",None),
("zubyul","zubyul/obsidian",None,0,0,0,"2024-05-24T18:26:28Z",None),
("zubyul","zubyul/private","SCSS",0,0,0,"2023-10-05T21:03:16Z",None),
("zubyul","zubyul/jonikas_for_weronika.-annotated-code","Jupyter Notebook",1,0,0,"2023-08-17T02:46:42Z",None),
("zubyul","zubyul/jonikas_lab_data_analysis_misc","Jupyter Notebook",2,0,0,"2023-08-16T20:24:40Z","various scripts for large genetic sequence data"),
("zubyul","zubyul/WGCNA","HTML",2,0,0,"2023-07-05T18:02:30Z","weighted gene correlation network analysis"),
("zubyul","zubyul/Dr_Niv_Qs","Jupyter Notebook",0,0,0,"2023-06-29T04:44:01Z","Dr. Niv Interview Questions"),
("zubyul","zubyul/reddit_scraper","Python",0,0,0,"2023-06-16T14:06:07Z",None),
("zubyul","zubyul/Python_Undergrad","Python",0,0,0,"2023-06-16T14:02:18Z",None),
("zubyul","zubyul/Nikolova_lab_data_analysis","R",2,0,0,"2023-06-16T13:56:58Z","undergraduate thesis - cortical thickness study"),
("zubyul","zubyul/lastfm_analysis_copy","Jupyter Notebook",1,0,0,"2023-06-15T22:20:35Z","lastfm data analysis"),
# DJedamski
("DJedamski","DJedamski/kaggle_ncaa18","Jupyter Notebook",0,0,0,"2018-03-07T12:36:09Z","NCAA March Madness competition 2018"),
("DJedamski","DJedamski/Project_Euler","Python",0,0,0,"2015-10-14T02:10:45Z",None),
("DJedamski","DJedamski/EDA","R",0,0,0,"2014-11-09T16:51:34Z","Coursera Project"),
("DJedamski","DJedamski/Kaggle",None,1,0,0,"2014-11-03T02:22:01Z",None),
("DJedamski","DJedamski/Getting-and-Cleaning-Data","R",1,0,0,"2014-10-26T20:53:14Z","Coursera Project"),
("DJedamski","DJedamski/School","R",1,1,0,"2014-10-09T02:55:13Z","A couple small projects from grad school"),
# kristinezheng
("kristinezheng","kristinezheng/kristinezheng.github.io","HTML",0,0,0,"2026-05-14T22:28:57Z","personal website"),
("kristinezheng","kristinezheng/Portfolio","HTML",0,0,0,"2025-02-12T00:00:42Z","portfolio site"),
("kristinezheng","kristinezheng/lookit-jenga","Jupyter Notebook",0,0,0,"2024-05-16T18:29:01Z","Lookit study for 9.85"),
("kristinezheng","kristinezheng/auditory-illusion","CSS",0,0,0,"2022-03-11T19:22:33Z","9.35 spring 2022 auditory illusion"),
("kristinezheng","kristinezheng/graph_example","Python",0,0,0,"2021-10-08T07:29:51Z",None),
("kristinezheng","kristinezheng/Green-Machine","Python",0,0,0,"2021-09-19T05:33:01Z","HackMIT 2021: Sustainability Track"),
# M1shaaa
("M1shaaa","M1shaaa/M1shaaa",None,0,0,0,"2026-06-03T16:41:23Z","Config files for GitHub profile"),
("M1shaaa","M1shaaa/lab-bookshelf-","TypeScript",0,0,0,"2024-12-31T05:11:14Z",None),
("M1shaaa","M1shaaa/rosie-s-study-3-lookit-project",None,0,0,0,"2024-11-04T22:15:35Z",None),
("M1shaaa","M1shaaa/Python-Lookit-Uploads","Python",0,0,0,"2024-02-16T15:20:50Z","random projects"),
("M1shaaa","M1shaaa/Classes",None,0,0,0,"2023-12-07T08:16:20Z",None),
("M1shaaa","M1shaaa/Yale-Work","HTML",0,0,0,"2023-12-06T18:33:10Z",None),
("M1shaaa","M1shaaa/MNIST-Classifier",None,0,0,0,"2023-11-28T06:12:13Z",None),
("M1shaaa","M1shaaa/Lookit-Demo",None,0,0,0,"2023-04-10T02:50:03Z",None),
# migalkin
("migalkin","migalkin/kgcourse2021","HTML",25,9,0,"2025-08-04T03:01:46Z","Knowledge Graphs course materials"),
("migalkin","migalkin/migalkin.github.io","JavaScript",0,0,0,"2025-01-22T04:53:51Z","Academic personal website"),
("migalkin","migalkin/NBFNet_mlx","Python",10,1,1,"2024-03-02T00:15:23Z","Neural Bellman-Ford networks in MLX for Apple Silicon"),
("migalkin","migalkin/StarE","Python",89,16,1,"2023-12-01T20:12:24Z","Message Passing for Hyper-Relational Knowledge Graphs"),
("migalkin","migalkin/rambo","Rust",3,0,1,"2023-02-08T14:27:03Z",None),
("migalkin","migalkin/ciss2_project","Jupyter Notebook",0,0,6,"2022-12-08T05:50:27Z",None),
("migalkin","migalkin/RWL","Python",8,1,0,"2022-12-01T15:58:59Z","Weisfeiler and Leman Go Relational"),
("migalkin","migalkin/NodePiece","Python",144,21,0,"2022-02-02T03:34:04Z","Compositional Representations for Large Knowledge Graphs"),
("migalkin","migalkin/SQuAD-es-mt",None,0,1,0,"2020-07-14T17:13:08Z","Spanish version of SQuAD via machine translation"),
("migalkin","migalkin/netquery_rdf","Python",0,0,0,"2019-06-01T12:49:16Z","NIPS 2018 paper fork for RDF"),
("migalkin","migalkin/edbt-experiments",None,0,0,0,"2017-11-23T15:27:49Z",None),
("migalkin","migalkin/SMJoin-experiments","R",1,0,0,"2017-06-06T12:20:23Z","ISWC 2017 SMJoin results"),
("migalkin","migalkin/ekgs_clustering","Python",0,0,0,"2016-08-28T16:28:02Z",None),
("migalkin","migalkin/r_energyConsumption","R",0,0,0,"2016-05-12T21:00:16Z",None),
("migalkin","migalkin/ontologies","Web Ontology Language",0,0,0,"2015-12-06T13:49:53Z",None),
("migalkin","migalkin/Tables_Provider","Java",0,0,0,"2015-03-20T00:17:35Z",None),
("migalkin","migalkin/datasciencecoursera",None,0,0,0,"2015-02-13T00:04:31Z","Coursera Data Science course"),
("migalkin","migalkin/InformationWorkbenchTestSrc","Java",0,0,0,"2013-06-22T15:46:54Z",None),
("migalkin","migalkin/LinkedData",None,0,0,0,"2013-05-20T07:43:46Z","Information Workbench + Linked Open Data"),
# AustinCStone
("AustinCStone","AustinCStone/EpsteinSearch","Python",0,0,0,"2026-02-11T01:10:54Z",None),
("AustinCStone","AustinCStone/bmforkupdate","Python",0,0,0,"2025-05-09T04:49:24Z",None),
("AustinCStone","AustinCStone/bmfork","Python",0,0,1,"2025-05-09T04:17:17Z",None),
("AustinCStone","AustinCStone/bitmind-fork",None,0,0,0,"2025-01-09T06:16:51Z","forked on jan 8 2025"),
("AustinCStone","AustinCStone/testLogin","Python",0,0,0,"2023-02-13T20:52:23Z",None),
("AustinCStone","AustinCStone/austincstone.github.io","HTML",0,0,0,"2021-10-23T22:48:46Z",None),
("AustinCStone","AustinCStone/test",None,0,0,0,"2021-09-21T21:15:51Z",None),
("AustinCStone","AustinCStone/stonks","Python",0,0,0,"2020-09-04T22:54:33Z","Playing around with option calculations"),
("AustinCStone","AustinCStone/Z-order-curve","Python",0,0,0,"2019-06-09T02:53:41Z","Demo of space filling z-order curve"),
("AustinCStone","AustinCStone/LensBuilder","Python",0,0,0,"2019-04-04T04:28:05Z","WIP optimize for surface of a focusing lens"),
("AustinCStone","AustinCStone/TFBirds","Python",0,0,0,"2019-01-30T08:07:21Z","Bird flocking simulator in TensorFlow"),
("AustinCStone","AustinCStone/StructureFromMotion","Python",1,0,0,"2018-06-10T18:56:16Z","Recover 3D geometry from videos"),
("AustinCStone","AustinCStone/OptimalControl","Python",0,0,0,"2018-02-19T23:13:55Z","Concepts from control theory"),
("AustinCStone","AustinCStone/LearningCuda","C",0,0,0,"2017-11-05T23:48:04Z","Working through CUDA by example"),
("AustinCStone","AustinCStone/TextGAN","Python",92,30,5,"2016-10-04T03:19:12Z","Generative adversarial network for text generation"),
("AustinCStone","AustinCStone/StereoVisionMRF","Python",11,4,0,"2016-01-10T08:34:29Z","MRF for depth from stereo images"),
("AustinCStone","AustinCStone/SpectralClustering","Python",3,2,0,"2015-11-09T03:27:15Z","Spectral clustering implementation"),
("AustinCStone","AustinCStone/statsHw2","Python",0,0,0,"2015-09-28T15:56:31Z","Linear regression and model selection"),
("AustinCStone","AustinCStone/StatsModelingHw1","Python",0,0,0,"2015-09-19T04:13:52Z","First homework for statistical modeling"),
("AustinCStone","AustinCStone/ConvNet","Python",0,0,0,"2015-09-08T00:43:12Z","Deep convolutional neural network for MNIST"),
("AustinCStone","AustinCStone/TheanoStuff","Python",0,0,0,"2015-09-04T02:14:00Z","Getting acquainted with Theano"),
("AustinCStone","AustinCStone/bash_profile",None,0,0,0,"2015-08-26T17:59:50Z","bash profile"),
("AustinCStone","AustinCStone/Founderati-Server","Python",0,1,0,"2015-08-25T19:17:44Z","Server for Founderati"),
("AustinCStone","AustinCStone/Founderati-client","JavaScript",0,1,0,"2015-08-25T19:16:57Z","AngelList or LinkedIn for hackers"),
("AustinCStone","AustinCStone/logisticRegressionHaskell","Haskell",1,0,0,"2015-06-07T19:37:42Z","Logistic regression in Haskell for MNIST"),
("AustinCStone","AustinCStone/Genetic-Algorithm-Sorting-Network","Python",0,0,0,"2015-05-12T19:30:48Z",None),
("AustinCStone","AustinCStone/RealTimeRayTracingFractalWorld","C++",0,0,0,"2015-05-11T02:03:41Z","Real time ray tracing of a fractal world"),
("AustinCStone","AustinCStone/gibbs_sampling","Python",0,0,0,"2015-04-09T03:15:55Z","Convergence of gibbs sampling and ancestral rejection sampling"),
("AustinCStone","AustinCStone/lexer","C",0,0,0,"2015-02-09T22:45:55Z","A lexer for prolog"),
("AustinCStone","AustinCStone/HTTPCache","Java",0,0,0,"2015-02-05T22:04:01Z","Caches responses from GET requests"),
("AustinCStone","AustinCStone/DigitRecognition","Matlab",0,0,0,"2015-02-02T04:35:23Z","Classify handwritten digits"),
("AustinCStone","AustinCStone/stuffForAlec","JavaScript",0,0,0,"2015-01-05T01:34:22Z",None),
("AustinCStone","AustinCStone/FlaskBlog","Python",0,0,0,"2014-12-17T23:45:06Z","A simple blog written with Flask"),
("AustinCStone","AustinCStone/PrologParserAndEvaluator",None,0,0,0,"2014-11-07T02:24:27Z","Parser and evaluator written in prolog"),
("AustinCStone","AustinCStone/QuantumSearchAlgorithmSimulation","Java",0,0,0,"2014-11-07T02:09:38Z","Simulation of Grover algorithm"),
("AustinCStone","AustinCStone/SleepDetectionMoto360","Java",0,0,0,"2014-10-19T03:24:05Z","Sleep detection for Moto 360 smartwatch"),
("AustinCStone","AustinCStone/Connectomics","TeX",0,0,0,"2014-05-11T05:30:07Z","Kaggle Connectomics Challenge"),
("AustinCStone","AustinCStone/Eigenface-Recognition","Matlab",0,0,0,"2014-05-11T03:56:10Z",None),
("AustinCStone","AustinCStone/Royal-Road-With-Ditches-Genetic-Algorithm","Python",0,0,0,"2014-05-11T02:27:57Z","Royal Road genetic algorithm modification"),
("AustinCStone","AustinCStone/Netflix_Prize_Challenge","M",0,0,0,"2014-05-11T02:23:07Z","Predict movie ratings"),
# wasita
("wasita","wasita/wasita.github.io","Svelte",1,0,8,"2026-06-01T04:15:56Z","personal website"),
("wasita","wasita/wm-cv","Svelte",0,0,0,"2026-05-13T05:29:04Z","Academic CV as single page web app"),
("wasita","wasita/vocoder","JavaScript",0,0,0,"2026-05-06T05:14:00Z",None),
("wasita","wasita/ch3-lib","Typst",0,0,0,"2026-04-12T04:03:19Z",None),
("wasita","wasita/magic-garden","Python",2,1,1,"2026-01-13T23:51:32Z","bot for magic garden discord activity game"),
("wasita","wasita/proj-template",None,0,0,0,"2026-01-09T20:55:42Z",None),
("wasita","wasita/food-diary","Svelte",0,0,0,"2025-12-13T01:06:39Z",None),
("wasita","wasita/send2kobo","TypeScript",1,0,0,"2025-12-12T19:09:12Z","Website for sending books to kobo e-reader"),
("wasita","wasita/d60-keeb",None,0,0,0,"2024-08-26T00:46:22Z",None),
("wasita","wasita/wins-search","CSS",1,0,0,"2022-12-14T22:17:32Z","Women in Network Science member list website"),
("wasita","wasita/honeycomb-demo","JavaScript",0,0,0,"2021-12-07T21:38:28Z",None),
]

ts = datetime.utcnow().isoformat()

# Insert world_increments and repo_snapshots
inc_id = 1
repo_id = 1
for org_or_user, full_name, language, stars, forks, open_issues, pushed_at, description in REPOS:
    trit, color, name = gf3(inc_id)
    repo_name = full_name.split("/", 1)[1] if "/" in full_name else full_name
    h = snap_hash(full_name + (pushed_at or ""))
    con.execute("""
        INSERT INTO world_increments VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [inc_id, ts, trit, color, name, "github", org_or_user, "repo_push", repo_name, org_or_user, h])
    con.execute("""
        INSERT INTO repo_snapshots VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [repo_id, ts, inc_id, org_or_user, repo_name, full_name, language, stars, forks, open_issues, pushed_at, description])
    inc_id += 1
    repo_id += 1

print(f"Inserted {repo_id - 1} repos / increments")

# ── Aptos snapshots ──────────────────────────────────────────────────────────
APTOS = [
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
for world, address, balance in APTOS:
    con.execute("INSERT INTO aptos_snapshots VALUES (?, ?, ?, ?)", [ts, world, address, balance])
print(f"Inserted {len(APTOS)} Aptos snapshots")

# ── Multisig probes ──────────────────────────────────────────────────────────
MULTISIGS = [
    ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2,True),
    ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2,True),
    ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2,True),
    ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2,True),
    ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2,True),
]
for pair, address, sigs, healthy in MULTISIGS:
    con.execute("INSERT INTO multisig_probes VALUES (?, ?, ?, ?, ?)", [ts, pair, address, sigs, healthy])
print(f"Inserted {len(MULTISIGS)} multisig probes")

# MNX: SPA, no API data available
# (no rows inserted)
print("MNX: Next.js SPA - no structured market data returned by API routes")

# ── Verification ─────────────────────────────────────────────────────────────
r = con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0]
rs = con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0]
ap = con.execute("SELECT COUNT(*) FROM aptos_snapshots").fetchone()[0]
ms = con.execute("SELECT COUNT(*) FROM multisig_probes").fetchone()[0]
print(f"\nDB summary:")
print(f"  world_increments: {r}")
print(f"  repo_snapshots:   {rs}")
print(f"  aptos_snapshots:  {ap}")
print(f"  multisig_probes:  {ms}")

# sample GF3 distribution
dist = con.execute("SELECT gf3_name, COUNT(*) FROM world_increments GROUP BY gf3_name").fetchall()
for row in dist:
    print(f"  GF3 {row[0]}: {row[1]}")

con.close()
print("\nDone. DB at", DB_PATH)
