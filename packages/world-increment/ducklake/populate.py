#!/usr/bin/env python3
"""Populate world-increments DuckDB with GitHub sweep and Hamming swarm snapshot."""
import duckdb, json, os, hashlib
from datetime import datetime

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"

# GF(3) color chain
def gf3(id):
    t = id % 3
    if t == 0: return (0, "#d3869b", "ERGODIC")
    if t == 1: return (1, "#b8bb26", "PLUS")
    return (-1, "#cc241d", "MINUS")

def snap_hash(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()[:16]

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
con.execute("CREATE SEQUENCE IF NOT EXISTS increment_seq START 1")
con.execute("CREATE SEQUENCE IF NOT EXISTS repo_seq START 1")

# ── Repo data ───────────────────────────────────────────────────────────────
repos = []

# plurigrid (100 repos)
plurigrid_repos = [
  ("plurigrid/place","place","TeX",1,2,11,"2026-06-03T07:12:32Z",""),
  ("plurigrid/eirobri","eirobri","Clojure",0,0,29,"2026-06-03T20:43:46Z","EiRoBri replay world"),
  ("plurigrid/nash-portal","nash-portal","Rust",2,3,1,"2026-05-19T01:49:59Z","NASH token TUI in the browser"),
  ("plurigrid/gorj","gorj","Clojure",0,0,338,"2026-06-04T02:21:40Z","forj + Rama topology nREPL routing"),
  ("plurigrid/zig-syrup","zig-syrup","Zig",2,2,0,"2026-04-30T03:52:16Z","High-performance Zig OCapN Syrup"),
  ("plurigrid/asi","asi","HTML",24,6,4,"2026-04-26T08:51:41Z","everything is topological chemputer"),
  ("plurigrid/asi-skills","asi-skills","Julia",3,1,0,"2026-04-26T08:09:26Z","69 skills with Galois Hole Type"),
  ("plurigrid/bci-blue-share","bci-blue-share","JavaScript",0,0,0,"2026-04-26T07:08:03Z","BCI signal infrastructure"),
  ("plurigrid/nanoclj-zig","nanoclj-zig","Zig",1,2,20,"2026-04-25T07:29:09Z","NaN-boxed Clojure interpreter in Zig"),
  ("plurigrid/spi-race","spi-race","Swift",0,0,0,"2026-04-21T19:31:56Z","Splitmix Parallel Integrity"),
  ("plurigrid/reafference","reafference","HTML",0,0,0,"2026-04-16T05:21:49Z","Reafference adaptation workspace"),
  ("plurigrid/web-browser","web-browser","Rust",0,0,0,"2026-04-10T02:54:47Z","web-browser from prepostweb lineage"),
  ("plurigrid/vivarium","vivarium","Clojure",1,0,0,"2026-04-08T08:38:37Z",""),
  ("plurigrid/flowglad-rs","flowglad-rs","Rust",0,0,0,"2026-04-08T07:56:15Z",""),
  ("plurigrid/tree-sitter-nanoclj-zig","tree-sitter-nanoclj-zig","C",0,0,0,"2026-04-04T07:48:21Z","Tree-sitter grammar for nanoclj-zig"),
  ("plurigrid/forester","forester","XSLT",0,0,0,"2026-03-30T01:32:26Z","CatColab mathematical documentation forest"),
  ("plurigrid/gatomic","gatomic","Clojure",0,0,0,"2026-03-30T00:54:48Z","Gay + Datomic + Atomic color store"),
  ("plurigrid/blue","blue","TeX",0,0,0,"2026-03-29T23:06:32Z",""),
  ("plurigrid/red","red","",0,0,0,"2026-03-29T22:58:46Z",""),
  ("plurigrid/nblm-flashcards","nblm-flashcards","Hy",0,0,0,"2026-03-26T08:23:01Z","NotebookLM flashcard pipeline"),
  ("plurigrid/gemini-agent","gemini-agent","Python",0,0,0,"2026-02-19T06:39:16Z",""),
  ("plurigrid/graded-optic","graded-optic","Haskell",0,0,0,"2026-02-08T16:10:16Z","Semiring-graded bidirectional processes"),
  ("plurigrid/json-canvas","json-canvas","",0,0,0,"2026-02-06T06:50:57Z","JSON Canvas real-time interaction data"),
  ("plurigrid/shepherd","shepherd","Scheme",0,0,0,"2026-01-23T07:47:28Z","Spritely Shepherd service manager"),
  ("plurigrid/goblinshare","goblinshare","Scheme",0,0,0,"2026-01-23T07:47:12Z","P2P filesharing demo for Goblins"),
  ("plurigrid/magenc","magenc","Scheme",0,0,0,"2026-01-23T07:47:11Z","Magenc Magnet URIs"),
  ("plurigrid/hoot","hoot","Scheme",0,0,1,"2026-01-23T07:47:10Z","Spritely Hoot Scheme to WebAssembly"),
  ("plurigrid/leprechauns","leprechauns","Racket",0,0,0,"2026-01-23T07:46:46Z","Spritely Goblins + Gay.jl colors"),
  ("plurigrid/spritely-semantic-colors","spritely-semantic-colors","",0,0,0,"2026-01-23T07:38:32Z","Spritely/Goblins GF3 color mappings"),
  ("plurigrid/gay-tofu","gay-tofu","HTML",0,0,0,"2026-01-08T15:14:34Z","Low-discrepancy color sequences TOFU"),
  ("plurigrid/lazygay","lazygay","Go",0,0,0,"2026-01-08T14:19:25Z","lazygit fork with Gay.jl coloring"),
  ("plurigrid/gay-terminal","gay-terminal","Rust",0,0,0,"2026-01-08T14:19:24Z","Terminal ANSI coloring with Gay.jl"),
  ("plurigrid/gay-go","gay-go","Go",0,0,0,"2026-01-08T14:19:23Z","Go implementation of Gay.jl"),
  ("plurigrid/gay-rs","gay-rs","Rust",0,0,0,"2026-01-08T14:19:22Z","Rust crate for Gay.jl GF(3) trits"),
  ("plurigrid/lazybjj","lazybjj","Rust",0,0,0,"2026-01-08T14:19:19Z","TUI for jj with Gay.jl GF(3) coloring"),
  ("plurigrid/agent-o-rama","agent-o-rama","Clojure",0,0,0,"2026-01-02T01:09:22Z",""),
  ("plurigrid/aptos-wallet-ruby","aptos-wallet-ruby","Ruby",1,0,0,"2025-09-30T22:47:22Z",""),
  ("plurigrid/duck-kanban","duck-kanban","Rust",1,0,0,"2025-09-26T20:18:38Z","Duck intelligence kanban system"),
  ("plurigrid/shiteshiteshite","shiteshiteshite","",0,0,0,"2025-09-26T03:07:20Z",""),
  ("plurigrid/discohy","discohy","Hy",0,0,0,"2025-09-10T02:01:31Z",""),
  ("plurigrid/telemind","telemind","",0,0,0,"2025-06-12T05:54:59Z",""),
  ("plurigrid/ontology","ontology","JavaScript",8,9,16,"2025-05-27T18:18:34Z","autopoietic ergodicity"),
  ("plurigrid/Plurigraph","Plurigraph","JavaScript",3,5,4,"2025-01-05T08:39:09Z","Plurigrid knowledge base for Obsidian"),
  ("plurigrid/signe","signe","Python",0,0,0,"2024-08-15T20:52:03Z","Signal messages data traversal"),
  ("plurigrid/SwiftDuck","SwiftDuck","",0,0,0,"2024-08-08T18:19:06Z",""),
  ("plurigrid/act","act","Python",3,1,4,"2024-07-26T08:27:08Z","blocks for cognitive category theory"),
  ("plurigrid/xenomorphic","xenomorphic","",0,0,0,"2024-04-09T03:24:55Z",""),
  ("plurigrid/metamorphic","metamorphic","",0,0,0,"2024-04-09T03:22:41Z",""),
  ("plurigrid/DiffusionVoiceDemo","DiffusionVoiceDemo","Clojure",0,0,0,"2024-04-02T18:09:01Z",""),
  ("plurigrid/website","website","Clojure",0,1,0,"2024-03-30T04:37:51Z",""),
  ("plurigrid/StochFlow","StochFlow","Python",4,1,0,"2024-03-20T23:34:57Z","stochastic interpolant models"),
  ("plurigrid/intent","intent","",0,0,0,"2024-03-04T04:53:38Z","Intent Markets simulations"),
  ("plurigrid/novella","novella","TypeScript",1,0,0,"2024-01-27T08:12:55Z",""),
  ("plurigrid/ACT.jl","ACT.jl","Julia",0,0,0,"2024-01-21T00:02:25Z","applied categorical duck cybernetics"),
  ("plurigrid/ducklings","ducklings","TypeScript",0,0,15,"2023-12-25T07:34:27Z",""),
  ("plurigrid/paretae","paretae","TypeScript",0,0,14,"2023-11-20T05:14:42Z",""),
  ("plurigrid/experiments","experiments","",0,0,0,"2023-11-17T05:39:07Z",""),
  ("plurigrid/fuckit","fuckit","Clojure",0,0,0,"2023-11-14T21:26:14Z",""),
  ("plurigrid/omega","omega","Clojure",0,0,0,"2023-11-07T21:08:46Z",""),
  ("plurigrid/org","org","Jupyter Notebook",2,0,1,"2023-11-07T01:08:05Z","Duck Repo Analysis"),
  ("plurigrid/CVAE-Flows","CVAE-Flows","",0,0,0,"2023-10-24T14:41:32Z",""),
  ("plurigrid/morph-prover-cli","morph-prover-cli","",0,1,0,"2023-10-18T03:49:03Z","Lean4"),
  ("plurigrid/uncharacter","uncharacter","TypeScript",0,0,0,"2023-09-19T20:17:46Z",""),
  ("plurigrid/chateau","chateau","TypeScript",0,0,0,"2023-08-30T20:11:12Z",""),
  ("plurigrid/gmgm","gmgm","",0,0,1,"2023-08-25T13:54:00Z",""),
  ("plurigrid/tuttle","tuttle","TypeScript",0,0,0,"2023-08-09T17:40:44Z",""),
  ("plurigrid/mesoplay","mesoplay","",0,0,0,"2023-08-09T06:19:03Z",""),
  ("plurigrid/am","am","Python",0,0,0,"2023-08-05T12:46:33Z",""),
  ("plurigrid/compose","compose","",0,0,2,"2023-07-24T06:18:48Z",""),
  ("plurigrid/flussi","flussi","",0,0,1,"2023-07-15T06:40:11Z",""),
  ("plurigrid/cf","cf","",0,0,0,"2023-07-11T08:11:29Z",""),
  ("plurigrid/poepoe","poepoe","",0,0,1,"2023-07-09T22:20:50Z",""),
  ("plurigrid/marketplace","marketplace","",0,0,1,"2023-07-09T05:52:30Z",""),
  ("plurigrid/smoller","smoller","",0,0,1,"2023-07-06T07:38:04Z",""),
  ("plurigrid/liquidity","liquidity","",0,0,1,"2023-07-06T02:07:28Z",""),
  ("plurigrid/solid-rs","solid-rs","",0,0,1,"2023-07-05T21:58:05Z",""),
  ("plurigrid/solid","solid","Python",0,0,0,"2023-07-05T21:52:25Z",""),
  ("plurigrid/ipegrafo","ipegrafo","Python",0,0,0,"2023-07-03T07:29:40Z",""),
  ("plurigrid/plurigrid-v4","plurigrid-v4","TypeScript",0,0,0,"2023-07-03T06:31:59Z",""),
  ("plurigrid/novella-v3","novella-v3","",0,0,0,"2023-07-03T06:29:40Z",""),
  ("plurigrid/polyglottal","polyglottal","TypeScript",0,0,0,"2023-07-03T06:23:45Z",""),
  ("plurigrid/novella-v2","novella-v2","",0,0,0,"2023-07-03T06:22:38Z",""),
  ("plurigrid/cocreation-ui","cocreation-ui","",0,0,2,"2023-07-03T04:45:53Z",""),
  ("plurigrid/smol","smol","",0,0,1,"2023-07-02T08:45:32Z",""),
  ("plurigrid/commons","commons","TypeScript",0,0,0,"2023-06-27T05:46:24Z",""),
  ("plurigrid/post-web","post-web","Svelte",0,0,0,"2023-06-18T00:24:24Z",""),
  ("plurigrid/microworlds","microworlds","Rust",3,5,3,"2023-05-13T03:54:56Z",""),
  ("plurigrid/pills","pills","",0,0,0,"2023-05-02T10:03:03Z","metaphors for embodied gradualism"),
  ("plurigrid/plurigrid-rs","plurigrid-rs","Rust",0,0,0,"2023-04-21T01:02:56Z",""),
  ("plurigrid/plurigrid-game.github.io","plurigrid-game.github.io","HTML",0,0,1,"2023-04-20T00:17:55Z",""),
  ("plurigrid/synth","synth","Rust",0,0,0,"2023-04-15T01:56:45Z",""),
  ("plurigrid/birbs","birbs","C++",0,0,0,"2023-04-15T01:56:32Z","CosmWasm apps w/ Dart and Flutter"),
  ("plurigrid/agent","agent","Python",5,1,6,"2023-03-31T18:45:23Z","Framework for agency amplification"),
  ("plurigrid/vcg-auction","vcg-auction","Rust",7,2,1,"2023-03-16T21:53:08Z","VCG auction contract"),
  ("plurigrid/bidder","bidder","Dart",0,0,1,"2023-03-15T15:23:22Z","flutter VCG auction bidding app"),
  ("plurigrid/plurigrid.github.io","plurigrid.github.io","HTML",1,2,2,"2023-01-20T03:27:34Z",""),
  ("plurigrid/VPP","VPP","Julia",0,1,0,"2023-01-11T18:41:07Z","Hyperreal Power Plant"),
  ("plurigrid/grid","grid","TypeScript",2,1,1,"2023-01-02T11:55:55Z","Plurigrid Testnet #0: Edith Clarke"),
  ("plurigrid/commons-contracts","commons-contracts","Rust",0,0,0,"2022-09-09T09:20:11Z","CosmWasm Commons Stack contracts"),
  ("plurigrid/plurigrid.xyz","plurigrid.xyz","TypeScript",0,0,1,"2022-08-31T05:26:14Z",""),
]
for fn,name,lang,stars,forks,issues,pushed,desc in plurigrid_repos:
    repos.append(("org","plurigrid",name,fn,lang,stars,forks,issues,pushed,desc[:100]))

# kubeflow (48 repos - key ones)
kubeflow_repos = [
  ("kubeflow/pipelines","pipelines","Python",4151,2004,491,"2026-06-03T21:06:23Z","Machine Learning Pipelines for Kubeflow"),
  ("kubeflow/trainer","trainer","Go",2110,964,129,"2026-06-03T17:02:37Z","Distributed AI Model Training on Kubernetes"),
  ("kubeflow/spark-operator","spark-operator","Python",3124,1488,101,"2026-06-03T17:01:00Z","Kubernetes operator for Apache Spark"),
  ("kubeflow/hub","hub","Go",175,182,43,"2026-06-04T00:19:49Z","Model Registry for ML model developers"),
  ("kubeflow/notebooks","notebooks","",73,118,185,"2026-06-04T02:11:40Z","Kubeflow Notebooks for AI/ML/Data Science"),
  ("kubeflow/community","community","Jupyter Notebook",195,257,17,"2026-06-02T15:52:13Z","Kubeflow community info and governance"),
  ("kubeflow/sdk","sdk","Python",120,181,136,"2026-06-03T15:18:55Z","Universal Python SDK for AI workloads on K8s"),
  ("kubeflow/kale","kale","Python",690,155,48,"2026-06-01T23:05:01Z","Kubeflow superfood for Data Scientists"),
  ("kubeflow/internal-acls","internal-acls","Go",19,388,2,"2026-06-01T16:22:32Z","Group ACLs for Kubeflow developers"),
  ("kubeflow/mcp-apache-spark-history-server","mcp-apache-spark-history-server","Python",173,61,21,"2026-06-01T19:56:25Z","MCP Server for Apache Spark History Server"),
  ("kubeflow/manifests","manifests","YAML",1020,1065,26,"2026-06-02T18:56:27Z","Kubeflow AI Reference Platform Manifests"),
  ("kubeflow/mpi-operator","mpi-operator","Go",528,235,103,"2026-06-02T14:30:58Z","Kubernetes Operator for MPI workloads"),
  ("kubeflow/pipelines-components","pipelines-components","Python",11,42,32,"2026-06-03T23:40:46Z","Kubeflow Pipelines components"),
  ("kubeflow/website","website","HTML",184,921,50,"2026-05-28T14:05:25Z","Kubeflow Website"),
  ("kubeflow/katib","katib","Python",1685,525,121,"2026-06-04T01:14:59Z","Automated Machine Learning on Kubernetes"),
  ("kubeflow/mlflow-integration","mlflow-integration","Python",6,3,2,"2026-05-27T15:42:37Z",""),
  ("kubeflow/blog","blog","Jupyter Notebook",32,62,26,"2026-05-25T13:02:24Z","Kubeflow blog"),
  ("kubeflow/kubeflow","kubeflow","",15704,2668,3,"2026-05-24T11:31:41Z","Machine Learning Toolkit for Kubernetes"),
  ("kubeflow/dashboard","dashboard","TypeScript",16,57,84,"2026-06-04T02:16:43Z","Kubeflow Central Dashboard"),
  ("kubeflow/mcp-server","mcp-server","Python",10,18,22,"2026-05-12T10:14:24Z","MCP Server for Kubeflow Tools"),
  ("kubeflow/arena","arena","Go",811,191,49,"2026-05-07T06:46:17Z","A CLI for Kubeflow"),
  ("kubeflow/docs-agent","docs-agent","Python",37,95,151,"2026-04-14T03:33:15Z","Kubeflow Documentation AI Agent"),
  ("kubeflow/examples","examples","Jsonnet",1462,756,111,"2025-04-14T01:54:52Z","Extended examples and tutorials"),
  ("kubeflow/testing","testing","Python",60,86,33,"2025-02-14T18:33:13Z","Test infrastructure for Kubeflow"),
  ("kubeflow/kfp-tekton","kfp-tekton","TypeScript",182,123,79,"2024-11-19T12:23:51Z","Kubeflow Pipelines on Tekton"),
  ("kubeflow/kfserving-lts","kfserving-lts","Jsonnet",12,19,51,"2024-08-02T16:25:44Z",""),
  ("kubeflow/kubebench","kubebench","Jsonnet",78,35,68,"2024-06-17T19:22:04Z","Benchmarking for Kubeflow"),
  ("kubeflow/fate-operator","fate-operator","Go",51,15,6,"2024-02-22T19:44:08Z","Fate operator for Kubernetes"),
  ("kubeflow/kfctl","kfctl","Go",182,134,94,"2023-08-15T20:19:22Z","CLI for deploying Kubeflow"),
  ("kubeflow/kfp-tekton-backend","kfp-tekton-backend","TypeScript",8,6,46,"2023-08-14T22:05:04Z","Tekton backend for KFP"),
  ("kubeflow/common","common","Go",53,70,40,"2023-05-28T13:16:00Z","Common APIs for Kubeflow operators"),
  ("kubeflow/.allstar","allstar","",2,0,0,"2022-12-06T23:07:59Z",""),
  ("kubeflow/fairing","fairing","Jsonnet",337,143,134,"2022-04-11T05:28:47Z","Python SDK for ML model training/deploy"),
  ("kubeflow/xgboost-operator","xgboost-operator","Python",77,53,22,"2021-12-01T18:00:10Z","XGBoost operator for Kubernetes"),
  ("kubeflow/mxnet-operator","mxnet-operator","Go",52,33,9,"2021-12-01T17:47:19Z","MXNet operator for Kubernetes"),
  ("kubeflow/pytorch-operator","pytorch-operator","Jsonnet",310,143,63,"2021-12-01T17:44:48Z","PyTorch on Kubernetes"),
  ("kubeflow/frontend","frontend","JavaScript",8,18,12,"2021-12-01T17:41:37Z","Kubeflow frontend"),
  ("kubeflow/metadata","metadata","TypeScript",123,63,38,"2021-12-01T17:35:27Z","Kubeflow Metadata"),
  ("kubeflow/caffe2-operator","caffe2-operator","Go",16,12,2,"2021-12-01T01:58:06Z","Caffe2 operator"),
  ("kubeflow/code-intelligence","code-intelligence","Jupyter Notebook",56,20,64,"2021-12-01T01:52:58Z","ML-Powered Developer Tools"),
  ("kubeflow/example-seldon","example-seldon","Jupyter Notebook",172,56,9,"2021-12-01T01:49:58Z","Example for ML on Kubernetes"),
  ("kubeflow/batch-predict","batch-predict","Python",17,7,9,"2021-12-01T01:47:51Z","Batch predict"),
  ("kubeflow/reporting","reporting","Jsonnet",2,5,1,"2021-12-01T01:42:32Z","Kubeflow usage metrics"),
  ("kubeflow/chainer-operator","chainer-operator","Jsonnet",17,15,7,"2021-11-14T13:03:57Z","Chainer operator"),
  ("kubeflow/crd-validation","crd-validation","Go",11,7,5,"2021-01-25T15:02:53Z","CRD validation for Kubeflow"),
  ("kubeflow/community-infra","community-infra","Go",3,9,4,"2021-01-25T14:49:49Z","KF community infra"),
  ("kubeflow/.github","github","",2,1,0,"2020-05-12T00:22:56Z","Org wide templates"),
  ("kubeflow/marketing-materials","marketing-materials","",4,4,4,"2019-07-19T13:57:15Z",""),
]
for fn,name,lang,stars,forks,issues,pushed,desc in kubeflow_repos:
    repos.append(("org","kubeflow",name,fn,lang,stars,forks,issues,pushed,desc[:100]))

# TeglonLabs (4 repos)
teglon_repos = [
  ("TeglonLabs/mathpix-gem","mathpix-gem","Ruby",2,0,11,"2026-01-01T12:13:16Z","Transform mathematical images to LaTeX"),
  ("TeglonLabs/topoi","topoi","Python",0,0,1,"2025-01-24T06:47:38Z",""),
  ("TeglonLabs/monad-mcp-server","monad-mcp-server","",0,0,0,"2025-05-14T17:53:01Z","Monad MCP Server"),
  ("TeglonLabs/coin-flip-mcp","coin-flip-mcp","JavaScript",0,2,1,"2025-03-16T01:31:45Z","MCP server for flipping coins"),
]
for fn,name,lang,stars,forks,issues,pushed,desc in teglon_repos:
    repos.append(("org","TeglonLabs",name,fn,lang,stars,forks,issues,pushed,desc[:100]))

# bmorphism (103 repos - key ones)
bmorphism_repos = [
  ("bmorphism/ocaml-mcp-sdk","ocaml-mcp-sdk","OCaml",61,2,0,"2026-05-08T16:50:34Z","OCaml SDK for Model Context Protocol"),
  ("bmorphism/anti-bullshit-mcp-server","anti-bullshit-mcp-server","JavaScript",23,7,1,"2026-02-05T15:46:59Z","MCP server for analyzing claims"),
  ("bmorphism/risc0-cosmwasm-example","risc0-cosmwasm-example","Rust",23,2,1,"2025-05-21T13:35:37Z","CosmWasm + zkVM RISC-V EFI template"),
  ("bmorphism/say-mcp-server","say-mcp-server","JavaScript",20,9,3,"2026-03-19T23:11:59Z","MCP server for macOS text-to-speech"),
  ("bmorphism/babashka-mcp-server","babashka-mcp-server","JavaScript",18,6,3,"2026-03-26T14:35:39Z","MCP server for Babashka/Clojure"),
  ("bmorphism/manifold-mcp-server","manifold-mcp-server","JavaScript",14,9,5,"2026-04-15T19:54:28Z","MCP server for Manifold Markets"),
  ("bmorphism/penrose-mcp","penrose-mcp","JavaScript",10,4,0,"2026-04-12T18:09:12Z","Penrose server for Infinity-Topos"),
  ("bmorphism/marginalia-mcp-server","marginalia-mcp-server","JavaScript",8,6,0,"2026-03-27T16:55:55Z","MCP server for marginalia/annotations"),
  ("bmorphism/nats-mcp-server","nats-mcp-server","",7,3,2,"2025-12-20T23:56:36Z","MCP server for NATS messaging"),
  ("bmorphism/hypernym-mcp-server","hypernym-mcp-server","JavaScript",6,5,0,"2025-10-24T09:21:53Z",""),
  ("bmorphism/penumbra-mcp","penumbra-mcp","JavaScript",5,6,3,"2025-10-24T09:21:41Z","MCP server for Penumbra blockchain"),
  ("bmorphism/shitcoin","shitcoin","Python",5,0,0,"2026-04-08T08:07:17Z","gets denom for cw20 assets IBC"),
  ("bmorphism/talks","talks","JavaScript",3,1,0,"2025-10-24T09:15:58Z",""),
  ("bmorphism/open-location-code-zig","open-location-code-zig","Zig",3,0,0,"2026-03-24T21:54:01Z","Open Location Code for Zig"),
  ("bmorphism/slowtime-mcp-server","slowtime-mcp-server","TypeScript",3,5,6,"2025-10-24T09:21:39Z","MCP server for secure time operations"),
  ("bmorphism/OTC-0","OTC-0","JavaScript",3,0,0,"2025-10-24T09:17:50Z",""),
  ("bmorphism/graphistry-mcp","graphistry-mcp","Python",2,0,0,"2025-10-24T09:22:41Z","Graphistry MCP graph visualization"),
  ("bmorphism/whale","whale","MATLAB",2,0,0,"2026-04-20T15:04:09Z","omniglot + sperm whale codas"),
  ("bmorphism/gists-mcp-server","gists-mcp-server","JavaScript",2,0,0,"2025-10-24T09:21:39Z","MCP server for GitHub Gists"),
  ("bmorphism/galahack2024","galahack2024","TypeScript",2,0,0,"2025-10-24T09:20:01Z",""),
  ("bmorphism/pluridrop","pluridrop","TypeScript",2,0,0,"2025-10-24T09:17:43Z","ETHPortland2022 hack"),
  ("bmorphism/zeldar","zeldar","Python",1,0,1,"2025-10-24T09:23:57Z","Burning Man Art Robot"),
  ("bmorphism/monero-rental-hash-war","monero-rental-hash-war","Haskell",1,0,0,"2025-10-24T09:25:25Z","Compositional OpenGame Monero analysis"),
  ("bmorphism/rama-event-processor","rama-event-processor","Java",1,0,0,"2025-10-24T09:23:16Z","Processing events with Rama"),
  ("bmorphism/lumon-tui","lumon-tui","Python",1,0,0,"2025-10-24T09:21:53Z","TUI parallel worlds Lumon Industries"),
  ("bmorphism/Gay.jl","Gay.jl","Julia",1,0,189,"2026-05-15T12:46:42Z","Wide-gamut color sampling splittable"),
  ("bmorphism/world","world","Python",0,0,0,"2026-06-02T06:49:06Z","Local worlds launcher for SA3 jank"),
  ("bmorphism/magic-world-org","magic-world-org","Python",1,0,0,"2026-05-01T01:06:25Z","Magic World Org Local MLX"),
  ("bmorphism/vibespace-mcp-go-ternary","vibespace-mcp-go-ternary","HTML",0,1,3,"2025-03-19T21:42:56Z","MCP for vibes with balanced ternary"),
  ("bmorphism/oxgame","oxgame","OCaml",0,0,0,"2026-05-15T09:55:59Z","Stellar resolution open-game OCaml"),
  ("bmorphism/postweb","postweb","Go",0,0,0,"2026-04-09T10:52:07Z","postweb evolved from prepostweb"),
  ("bmorphism/nanoclj-zig","nanoclj-zig","Zig",0,0,0,"2026-04-25T07:29:19Z",""),
  ("bmorphism/flox-mcp-bb","flox-mcp-bb","Clojure",0,0,0,"2026-02-12T02:45:46Z","MCP server for Flox Babashka"),
  ("bmorphism/aella","aella","Rascal",1,0,0,"2026-04-02T17:15:48Z",""),
  ("bmorphism/hymlx","hymlx","Python",1,0,0,"2026-01-22T21:44:46Z",""),
  ("bmorphism/krep-mcp-server","krep-mcp-server","JavaScript",1,1,1,"2026-02-10T11:23:43Z","High-performance string search MCP"),
  ("bmorphism/stellogen-quantum-operads","stellogen-quantum-operads","",1,0,0,"2026-02-02T23:59:31Z","Quantum Operads and ZX-Calculus"),
]
for fn,name,lang,stars,forks,issues,pushed,desc in bmorphism_repos:
    repos.append(("user","bmorphism",name,fn,lang,stars,forks,issues,pushed,desc[:100]))

# zubyul (49 repos - key ones)
zubyul_repos = [
  ("zubyul/WGCNA","WGCNA","HTML",2,0,0,"2026-03-26T09:05:26Z","weighted gene correlation network analysis"),
  ("zubyul/jonikas_lab_data_analysis_misc","jonikas_lab_data_analysis_misc","Jupyter Notebook",2,0,0,"2026-03-26T09:05:21Z","scripts for genetic sequence data"),
  ("zubyul/Nikolova_lab_data_analysis","Nikolova_lab_data_analysis","R",2,0,0,"2026-03-26T09:05:23Z","cortical thickness to transcription factors"),
  ("zubyul/gay-world","gay-world","Python",1,1,0,"2026-04-05T06:54:03Z","Goblin world builder MLX task decomposition"),
  ("zubyul/cascade-world","cascade-world","Python",1,0,0,"2026-03-26T09:06:01Z","Cascade development environment"),
  ("zubyul/jonikas_for_weronika.-annotated-code","jonikas_for_weronika.-annotated-code","Jupyter Notebook",1,0,0,"2026-03-26T09:05:27Z",""),
  ("zubyul/ghostty-modifications","ghostty-modifications","JavaScript",1,0,0,"2025-09-23T23:31:33Z","Ghostty terminal modifications and MCP"),
  ("zubyul/zubyul.github.io","zubyul.github.io","CSS",1,0,0,"2026-03-26T09:05:35Z",""),
  ("zubyul/GoofyLifeChoices","GoofyLifeChoices","Python",1,0,0,"2025-09-23T23:31:39Z",""),
  ("zubyul/lastfm_analysis_copy","lastfm_analysis_copy","Jupyter Notebook",1,0,0,"2026-03-26T09:05:23Z","lastfm data analysis"),
  ("zubyul/big-bad-plurigrid-quiz","big-bad-plurigrid-quiz","Emacs Lisp",0,0,0,"2026-04-09T18:51:35Z","27 flashcards from plurigrid activity"),
  ("zubyul/ghostel-emacs-worlds","ghostel-emacs-worlds","GLSL",0,0,0,"2026-04-24T00:21:00Z","Ghostty + alice/bob emacs-mods"),
  ("zubyul/voice-observatory","voice-observatory","Python",0,0,0,"2026-04-24T05:56:20Z","Passive macOS TUI voice-download paths"),
  ("zubyul/Gay.jl","Gay.jl","Julia",0,0,0,"2026-03-28T11:30:07Z","Wide-gamut color sampling splittable"),
  ("zubyul/tilelang-kernels","tilelang-kernels","Python",0,0,0,"2026-03-16T02:31:16Z","TileLang GPU kernels SplitMix64 GF(3)"),
  ("zubyul/from-possible-worlds","from-possible-worlds","TeX",0,0,0,"2026-03-16T03:07:20Z",""),
  ("zubyul/kinesis-kb360pro","kinesis-kb360pro","Python",0,0,0,"2026-03-26T10:29:44Z","Kinesis Advantage360 Pro keyboard config"),
  ("zubyul/gay-terminal-colors","gay-terminal-colors","Clojure",0,0,0,"2026-03-26T09:05:55Z","Gay.jl world_terminal_fingerprint"),
  ("zubyul/nash-tui","nash-tui","Rust",0,0,0,"2026-04-13T05:46:08Z","NASH token TUI real-time candles"),
  ("zubyul/nash-web","nash-web","Rust",0,0,0,"2026-04-13T07:09:02Z","NASH token browser TUI via ratzilla"),
  ("zubyul/hue-world","hue-world","JavaScript",0,0,0,"2026-03-26T09:05:56Z","Terminal Vibe Snipe puzzle game ANSI"),
  ("zubyul/multiplayer-emacs","multiplayer-emacs","HTML",0,0,0,"2026-03-26T09:06:00Z","Multiplayer Emacs Vibe Snipe swarm"),
]
for fn,name,lang,stars,forks,issues,pushed,desc in zubyul_repos:
    repos.append(("user","zubyul",name,fn,lang,stars,forks,issues,pushed,desc[:100]))

# migalkin (19 repos)
migalkin_repos = [
  ("migalkin/NodePiece","NodePiece","Python",144,21,0,"2026-05-07T05:40:02Z","Parameter-Efficient KG Representations ICLR22"),
  ("migalkin/StarE","StarE","Python",89,16,1,"2026-04-16T14:12:45Z","Message Passing Hyper-Relational KGs EMNLP20"),
  ("migalkin/kgcourse2021","kgcourse2021","HTML",25,9,0,"2026-02-16T05:16:08Z","Knowledge Graphs course materials"),
  ("migalkin/NBFNet_mlx","NBFNet_mlx","Python",10,1,1,"2026-03-11T01:31:21Z","Neural Bellman-Ford networks in MLX"),
  ("migalkin/RWL","RWL","Python",8,1,0,"2026-05-28T20:19:20Z","Weisfeiler and Leman Go Relational LOG22"),
  ("migalkin/rambo","rambo","Rust",3,0,1,"2023-02-28T16:37:22Z",""),
  ("migalkin/SMJoin-experiments","SMJoin-experiments","R",1,0,0,"2020-03-04T15:56:23Z","ISWC 2017 SMJoin results"),
  ("migalkin/migalkin.github.io","migalkin.github.io","JavaScript",0,0,0,"2025-05-20T23:58:08Z","Academic personal website"),
]
for fn,name,lang,stars,forks,issues,pushed,desc in migalkin_repos:
    repos.append(("user","migalkin",name,fn,lang,stars,forks,issues,pushed,desc[:100]))

# AustinCStone (40 repos)
austin_repos = [
  ("AustinCStone/TextGAN","TextGAN","Python",92,30,5,"2025-03-03T13:26:32Z","GAN for text generation TensorFlow"),
  ("AustinCStone/StereoVisionMRF","StereoVisionMRF","Python",11,4,0,"2026-04-01T07:39:41Z","MRF loopy belief propagation depth"),
  ("AustinCStone/SpectralClustering","SpectralClustering","Python",3,2,0,"2021-04-16T08:46:36Z","Spectral clustering homework"),
  ("AustinCStone/StructureFromMotion","StructureFromMotion","Python",1,0,0,"2019-04-26T19:43:12Z","Recover 3D geometry from videos"),
  ("AustinCStone/logisticRegressionHaskell","logisticRegressionHaskell","Haskell",1,0,0,"2018-02-02T13:34:28Z","Logistic regression in Haskell"),
  ("AustinCStone/bmfork","bmfork","Python",0,0,1,"2025-05-09T04:18:54Z",""),
  ("AustinCStone/EpsteinSearch","EpsteinSearch","Python",0,0,0,"2026-02-11T01:10:57Z",""),
  ("AustinCStone/bitmind-fork","bitmind-fork","",0,0,0,"2025-01-09T06:16:51Z","forked jan 8 2025"),
]
for fn,name,lang,stars,forks,issues,pushed,desc in austin_repos:
    repos.append(("user","AustinCStone",name,fn,lang,stars,forks,issues,pushed,desc[:100]))

# DJedamski (6 repos)
dj_repos = [
  ("DJedamski/Getting-and-Cleaning-Data","Getting-and-Cleaning-Data","R",1,0,0,"2023-04-21T01:42:34Z","Coursera Project"),
  ("DJedamski/Kaggle","Kaggle","",1,0,0,"2023-04-21T01:42:35Z",""),
  ("DJedamski/School","School","R",1,1,0,"2023-04-21T01:42:33Z","Grad school projects"),
  ("DJedamski/kaggle_ncaa18","kaggle_ncaa18","Jupyter Notebook",0,0,0,"2018-02-26T16:33:24Z","NCAA March Madness 2018"),
]
for fn,name,lang,stars,forks,issues,pushed,desc in dj_repos:
    repos.append(("user","DJedamski",name,fn,lang,stars,forks,issues,pushed,desc[:100]))

# wasita (11 repos)
wasita_repos = [
  ("wasita/magic-garden","magic-garden","Python",2,1,1,"2026-04-22T21:16:43Z","Bot for Discord magic-garden game"),
  ("wasita/wasita.github.io","wasita.github.io","Svelte",1,0,8,"2026-06-01T04:15:14Z","personal website"),
  ("wasita/wins-search","wins-search","CSS",1,0,0,"2023-06-03T19:01:11Z","Women in Network Science website"),
  ("wasita/send2kobo","send2kobo","TypeScript",1,0,0,"2026-05-19T02:59:26Z","Website sending books to Kobo"),
  ("wasita/ch3-lib","ch3-lib","Typst",0,0,0,"2026-04-12T04:03:22Z",""),
  ("wasita/wm-cv","wm-cv","Svelte",0,0,0,"2026-05-13T05:29:08Z","Academic CV single page app"),
  ("wasita/vocoder","vocoder","JavaScript",0,0,0,"2026-05-06T05:14:03Z",""),
]
for fn,name,lang,stars,forks,issues,pushed,desc in wasita_repos:
    repos.append(("user","wasita",name,fn,lang,stars,forks,issues,pushed,desc[:100]))

# kristinezheng (6 repos)
kz_repos = [
  ("kristinezheng/Portfolio","Portfolio","",0,0,0,"2025-02-12T00:00:45Z","July 2021 portfolio"),
  ("kristinezheng/Green-Machine","Green-Machine","Python",0,0,0,"2021-09-19T05:33:04Z","HackMIT 2021 Sustainability Track"),
  ("kristinezheng/lookit-jenga","lookit-jenga","Jupyter Notebook",0,0,0,"2024-05-16T18:29:05Z","Lookit study for 9.85"),
  ("kristinezheng/kristinezheng.github.io","kristinezheng.github.io","HTML",0,0,0,"2026-05-14T22:29:01Z",""),
]
for fn,name,lang,stars,forks,issues,pushed,desc in kz_repos:
    repos.append(("user","kristinezheng",name,fn,lang,stars,forks,issues,pushed,desc[:100]))

# M1shaaa (8 repos)
m_repos = [
  ("M1shaaa/lab-bookshelf-","lab-bookshelf-","TypeScript",0,0,0,"2024-12-31T05:11:18Z",""),
  ("M1shaaa/Classes","Classes","",0,0,0,"2023-12-06T18:20:27Z",""),
  ("M1shaaa/Python-Lookit-Uploads","Python-Lookit-Uploads","Python",0,0,0,"2024-02-15T22:59:37Z","random projects"),
  ("M1shaaa/M1shaaa","M1shaaa","",0,0,0,"2026-02-04T19:32:04Z","GitHub profile config"),
  ("M1shaaa/Yale-Work","Yale-Work","HTML",0,0,0,"2023-12-06T18:33:14Z",""),
]
for fn,name,lang,stars,forks,issues,pushed,desc in m_repos:
    repos.append(("user","M1shaaa",name,fn,lang,stars,forks,issues,pushed,desc[:100]))

print(f"Total repos to insert: {len(repos)}")

# Insert world_increments and repo_snapshots
ts = datetime.utcnow().isoformat()
inc_id = 1
repo_id = 1

for source_type, source_name, repo_name, full_name, language, stars, forks, issues, pushed_at, description in repos:
    trit, color, gname = gf3(inc_id)
    h = snap_hash({"fn": full_name, "stars": stars, "pushed": pushed_at})
    con.execute("""
        INSERT INTO world_increments (id, timestamp, gf3_trit, gf3_color, gf3_name, source_type, source_name, event_type, repo_name, actor, snapshot_hash)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [inc_id, ts, trit, color, gname, source_type, source_name, "repo_snapshot", repo_name, source_name, h])
    con.execute("""
        INSERT INTO repo_snapshots (id, timestamp, increment_id, org_or_user, repo_name, full_name, language, stars, forks, open_issues, pushed_at, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [repo_id, ts, inc_id, source_name, repo_name, full_name, language, stars, forks, issues, pushed_at, description])
    inc_id += 1
    repo_id += 1

# Aptos snapshots - all addresses
aptos_wallets = {
    "alice": "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b",
    "bob": "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d",
    "A": "0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a",
    "B": "0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13",
    "C": "0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e",
    "D": "0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1",
    "E": "0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36",
    "F": "0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71",
    "G": "0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32",
    "H": "0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f",
    "I": "0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9",
    "J": "0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54",
    "K": "0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4",
    "L": "0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9",
    "M": "0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9",
    "N": "0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c",
    "O": "0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d",
    "P": "0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948",
    "Q": "0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9",
    "R": "0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10",
    "S": "0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386",
    "T": "0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588",
    "U": "0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956",
    "V": "0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3",
    "W": "0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0",
    "X": "0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d",
    "Y": "0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4",
    "Z": "0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c",
}
for world, addr in aptos_wallets.items():
    # All returned resource_not_found → balance = 0 APT
    con.execute("INSERT INTO aptos_snapshots (timestamp, world, address, balance_apt) VALUES (?, ?, ?, ?)",
                [ts, world, addr, 0.0])

# Multisig probes - all returned ["2"]
multisig = [
    ("A-B", "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2, True),
    ("A-G", "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2, True),
    ("Y-Z", "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2, True),
    ("S-T", "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2, True),
    ("V-W", "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2, True),
]
for pair, addr, sigs, healthy in multisig:
    con.execute("INSERT INTO multisig_probes (timestamp, pair, address, sigs_required, healthy) VALUES (?, ?, ?, ?, ?)",
                [ts, pair, addr, sigs, healthy])

# MNX: SPA-only, no JSON API available
# mnx_snapshots stays empty

con.commit()

# Verify
print("=== world_increments ===")
print(con.execute("SELECT COUNT(*) FROM world_increments").fetchone())
print("=== repo_snapshots ===")
print(con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone())
print("=== aptos_snapshots ===")
print(con.execute("SELECT COUNT(*) FROM aptos_snapshots").fetchone())
print("=== multisig_probes ===")
print(con.execute("SELECT COUNT(*) FROM multisig_probes").fetchone())

# GF3 color distribution
print("\n=== GF3 color chain distribution ===")
for row in con.execute("SELECT gf3_name, gf3_color, gf3_trit, COUNT(*) FROM world_increments GROUP BY ALL ORDER BY gf3_trit").fetchall():
    print(row)

# Top repos by stars
print("\n=== Top 10 repos by stars ===")
for row in con.execute("SELECT org_or_user, repo_name, language, stars FROM repo_snapshots ORDER BY stars DESC LIMIT 10").fetchall():
    print(row)

con.close()
print("\nDone!")
