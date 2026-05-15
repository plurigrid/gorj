#!/usr/bin/env python3
"""Build world-increments DuckDB from GitHub sweep + Aptos snapshot data."""

import duckdb, hashlib, json, os

DB = os.path.join(os.path.dirname(__file__), "world-increments.duckdb")
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

def gf3(id_val):
    r = id_val % 3
    if r == 0:   return (0,  "#d3869b", "ERGODIC")
    elif r == 1: return (1,  "#b8bb26", "PLUS")
    else:        return (-1, "#cc241d", "MINUS")

def snap_hash(s):
    return hashlib.sha256(s.encode()).hexdigest()[:16]

# ── repo data ──────────────────────────────────────────────────────────────
repos = [
  # (org_or_user, full_name, language, stars, forks, open_issues, pushed_at, description)
  # plurigrid (100 repos)
  ("plurigrid","plurigrid/gmgm","",0,0,1,"2023-08-25T13:54:00Z",""),
  ("plurigrid","plurigrid/marketplace","",0,0,1,"2023-07-09T05:52:30Z",""),
  ("plurigrid","plurigrid/shepherd","Scheme",0,0,0,"2026-01-23T07:47:28Z","Spritely Shepherd - Service manager (mirror from Codeberg)"),
  ("plurigrid","plurigrid/bidder","Dart",0,0,1,"2023-03-15T15:23:22Z","simple flutter app which allows bidding in a vcg auction"),
  ("plurigrid","plurigrid/ACT.jl","Julia",0,0,0,"2024-01-21T00:02:25Z","applied categorical duck cybernetics"),
  ("plurigrid","plurigrid/duck-kanban","Rust",1,0,0,"2025-09-26T20:18:38Z","Duck intelligence kanban system with kundalini computational pattern recognition"),
  ("plurigrid","plurigrid/nanoclj-zig","Zig",1,2,20,"2026-04-25T07:29:09Z","NaN-boxed Clojure interpreter in Zig 0.15 — interaction nets, fuel-bounded eval, GF(3) trit conservation"),
  ("plurigrid","plurigrid/uncharacter","TypeScript",0,0,0,"2023-09-19T20:17:46Z",""),
  ("plurigrid","plurigrid/mesoplay","",0,0,0,"2023-08-09T06:19:03Z",""),
  ("plurigrid","plurigrid/json-canvas","",0,0,0,"2026-02-06T06:50:57Z","JSON Canvas: Real-time interaction data capture via W3C JSON-LD 1.1"),
  ("plurigrid","plurigrid/solid","Python",0,0,0,"2023-07-05T21:52:25Z",""),
  ("plurigrid","plurigrid/chateau","TypeScript",0,0,0,"2023-08-30T20:11:12Z",""),
  ("plurigrid","plurigrid/Plurigraph","JavaScript",3,5,4,"2025-01-05T08:39:09Z","Plurigrid knowledge base for use with Obsidian.md"),
  ("plurigrid","plurigrid/shiteshiteshite","",0,0,0,"2025-09-26T03:07:20Z","Duck intelligence kanban system"),
  ("plurigrid","plurigrid/paretae","TypeScript",0,0,14,"2023-11-20T05:14:42Z",""),
  ("plurigrid","plurigrid/graded-optic","Haskell",0,0,0,"2026-02-08T16:10:16Z","Semiring-graded bidirectional processes"),
  ("plurigrid","plurigrid/org","Jupyter Notebook",2,0,1,"2023-11-07T01:08:05Z","Dynamically Replicating Duck"),
  ("plurigrid","plurigrid/post-web","Svelte",0,0,0,"2023-06-18T00:24:24Z",""),
  ("plurigrid","plurigrid/solid-rs","",0,0,1,"2023-07-05T21:58:05Z",""),
  ("plurigrid","plurigrid/SwiftDuck","",0,0,0,"2024-08-08T18:19:06Z",""),
  ("plurigrid","plurigrid/poepoe","",0,0,1,"2023-07-09T22:20:50Z",""),
  ("plurigrid","plurigrid/ipegrafo","Python",0,0,0,"2023-07-03T07:29:40Z",""),
  ("plurigrid","plurigrid/polyglottal","TypeScript",0,0,0,"2023-07-03T06:23:45Z",""),
  ("plurigrid","plurigrid/nblm-flashcards","Hy",0,0,0,"2026-03-26T08:23:01Z","NotebookLM Enterprise flashcard pipeline"),
  ("plurigrid","plurigrid/tree-sitter-nanoclj-zig","C",0,0,0,"2026-04-04T07:48:21Z","Tree-sitter grammar for nanoclj-zig"),
  ("plurigrid","plurigrid/zig-syrup","Zig",2,2,0,"2026-04-30T03:52:16Z","High-performance Zig implementation of OCapN Syrup"),
  ("plurigrid","plurigrid/ontology","JavaScript",8,9,16,"2025-05-27T18:18:34Z","autopoietic ergodicity and embodied gradualism"),
  ("plurigrid","plurigrid/xenomorphic","",0,0,0,"2024-04-09T03:24:55Z",""),
  ("plurigrid","plurigrid/web-browser","Rust",0,0,0,"2026-04-10T02:54:47Z","web-browser — from prepostweb lineage"),
  ("plurigrid","plurigrid/pills","",0,0,0,"2023-05-02T10:03:03Z","metaphors for embodied gradualism"),
  ("plurigrid","plurigrid/plurigrid.github.io","HTML",1,2,2,"2023-01-20T03:27:34Z",""),
  ("plurigrid","plurigrid/StochFlow","Python",4,1,0,"2024-03-20T23:34:57Z","stochastic interpolant models and algorithms"),
  ("plurigrid","plurigrid/metamorphic","",0,0,0,"2024-04-09T03:22:41Z",""),
  ("plurigrid","plurigrid/tuttle","TypeScript",0,0,0,"2023-08-09T17:40:44Z",""),
  ("plurigrid","plurigrid/discohy","Hy",0,0,0,"2025-09-10T02:01:31Z",""),
  ("plurigrid","plurigrid/smoller","",0,0,1,"2023-07-06T07:38:04Z",""),
  ("plurigrid","plurigrid/synth","Rust",0,0,0,"2023-04-15T01:56:45Z",""),
  ("plurigrid","plurigrid/flowglad-rs","Rust",0,0,0,"2026-04-08T07:56:15Z",""),
  ("plurigrid","plurigrid/blue","TeX",0,0,0,"2026-03-29T23:06:32Z",""),
  ("plurigrid","plurigrid/agent-o-rama","Clojure",0,0,0,"2026-01-02T01:09:22Z",""),
  ("plurigrid","plurigrid/hoot","Scheme",0,0,0,"2026-01-23T07:47:10Z","Spritely Hoot - Scheme to WebAssembly compiler"),
  ("plurigrid","plurigrid/reafference","HTML",0,0,0,"2026-04-16T05:21:49Z","Reafference adaptation workspace"),
  ("plurigrid","plurigrid/smol","",0,0,1,"2023-07-02T08:45:32Z",""),
  ("plurigrid","plurigrid/commons-contracts","Rust",0,0,0,"2022-09-09T09:20:11Z","CosmWasm contracts to implement Commons Stack"),
  ("plurigrid","plurigrid/intent","",0,0,0,"2024-03-04T04:53:38Z","Simulations for An Analysis of Intent Markets"),
  ("plurigrid","plurigrid/website","Clojure",0,1,0,"2024-03-30T04:37:51Z",""),
  ("plurigrid","plurigrid/cf","",0,0,0,"2023-07-11T08:11:29Z",""),
  ("plurigrid","plurigrid/compose","",0,0,2,"2023-07-24T06:18:48Z",""),
  ("plurigrid","plurigrid/asi-skills","Julia",3,1,0,"2026-04-26T08:09:26Z","69 skills with Galois Hole Type accessibility"),
  ("plurigrid","plurigrid/gay-tofu","HTML",0,0,0,"2026-01-08T15:14:34Z","Low-discrepancy color sequences for visual TOFU authentication"),
  ("plurigrid","plurigrid/DiffusionVoiceDemo","Clojure",0,0,0,"2024-04-02T18:09:01Z",""),
  ("plurigrid","plurigrid/nash-portal","Rust",2,3,2,"2026-04-26T08:50:56Z","NASH token TUI in the browser"),
  ("plurigrid","plurigrid/bci-blue-share","JavaScript",0,0,0,"2026-04-26T07:08:03Z","BCI signal infrastructure"),
  ("plurigrid","plurigrid/microworlds","Rust",3,5,3,"2023-05-13T03:54:56Z",""),
  ("plurigrid","plurigrid/novella","TypeScript",1,0,0,"2024-01-27T08:12:55Z",""),
  ("plurigrid","plurigrid/grid","TypeScript",2,1,1,"2023-01-02T11:55:55Z","Plurigrid Testnet #0: Edith Clarke"),
  ("plurigrid","plurigrid/gatomic","Clojure",0,0,0,"2026-03-30T00:54:48Z","Deterministic color identity store with sonification"),
  ("plurigrid","plurigrid/fuckit","Clojure",0,0,0,"2023-11-14T21:26:14Z",""),
  ("plurigrid","plurigrid/novella-v3","",0,0,0,"2023-07-03T06:29:40Z",""),
  ("plurigrid","plurigrid/plurigrid-v4","TypeScript",0,0,0,"2023-07-03T06:31:59Z",""),
  ("plurigrid","plurigrid/gay-go","Go",0,0,0,"2026-01-08T14:19:23Z","Go implementation of Gay.jl deterministic coloring"),
  ("plurigrid","plurigrid/asi","HTML",23,5,4,"2026-04-26T08:51:41Z","everything is topological chemputer!"),
  ("plurigrid","plurigrid/goblinshare","Scheme",0,0,0,"2026-01-23T07:47:12Z","P2P filesharing demo for Goblins"),
  ("plurigrid","plurigrid/plurigrid-game.github.io","HTML",0,0,1,"2023-04-20T00:17:55Z",""),
  ("plurigrid","plurigrid/plurigrid.xyz","TypeScript",0,0,1,"2022-08-31T05:26:14Z",""),
  ("plurigrid","plurigrid/novella-v2","",0,0,0,"2023-07-03T06:22:38Z",""),
  ("plurigrid","plurigrid/horse","TeX",1,1,9,"2026-05-07T04:35:12Z",""),
  ("plurigrid","plurigrid/lazybjj","Rust",0,0,0,"2026-01-08T14:19:19Z","TUI for jj with Gay.jl GF(3) coloring"),
  ("plurigrid","plurigrid/plurigrid-rs","Rust",0,0,0,"2023-04-21T01:02:56Z",""),
  ("plurigrid","plurigrid/gemini-agent","Python",0,0,0,"2026-02-19T06:39:16Z",""),
  ("plurigrid","plurigrid/vivarium","Clojure",1,0,0,"2026-04-08T08:38:37Z",""),
  ("plurigrid","plurigrid/act","Python",3,1,4,"2024-07-26T08:27:08Z","building blocks for cognitive category theory"),
  ("plurigrid","plurigrid/am","Python",0,0,0,"2023-08-05T12:46:33Z",""),
  ("plurigrid","plurigrid/agent","Python",5,1,6,"2023-03-31T18:45:23Z","Framework for agency amplification"),
  ("plurigrid","plurigrid/spi-race","Swift",0,0,0,"2026-04-21T19:31:56Z","Splitmix Parallel Integrity"),
  ("plurigrid","plurigrid/spritely-semantic-colors","",0,0,0,"2026-01-23T07:38:32Z","Deterministic color mappings for Spritely/Goblins objects"),
  ("plurigrid","plurigrid/signe","Python",0,0,0,"2024-08-15T20:52:03Z","Signal messages data traversal"),
  ("plurigrid","plurigrid/CVAE-Flows","",0,0,0,"2023-10-24T14:41:32Z",""),
  ("plurigrid","plurigrid/omega","Clojure",0,0,0,"2023-11-07T21:08:46Z",""),
  ("plurigrid","plurigrid/telemind","",0,0,0,"2025-06-12T05:54:59Z",""),
  ("plurigrid","plurigrid/gay-rs","Rust",0,0,0,"2026-01-08T14:19:22Z","Rust crate for Gay.jl deterministic coloring with GF(3) trits"),
  ("plurigrid","plurigrid/gay-terminal","Rust",0,0,0,"2026-01-08T14:19:24Z","Terminal ANSI coloring with Gay.jl low-discrepancy sequences"),
  ("plurigrid","plurigrid/lazygay","Go",0,0,0,"2026-01-08T14:19:25Z","lazygit fork with Gay.jl deterministic commit coloring"),
  ("plurigrid","plurigrid/magenc","Scheme",0,0,0,"2026-01-23T07:47:11Z","Magenc Magnet URIs - Secure Object Permanence for the Web"),
  ("plurigrid","plurigrid/red","",0,0,0,"2026-03-29T22:58:46Z",""),
  ("plurigrid","plurigrid/morph-prover-cli","",0,1,0,"2023-10-18T03:49:03Z","Lean4"),
  ("plurigrid","plurigrid/vcg-auction","Rust",7,2,1,"2023-03-16T21:53:08Z","a simple contract that performs a VCG auction"),
  ("plurigrid","plurigrid/leprechauns","Racket",0,0,0,"2026-01-23T07:46:46Z","Spritely Goblins + Gay.jl semantic colors"),
  ("plurigrid","plurigrid/forester","XSLT",0,0,0,"2026-03-30T01:32:26Z","CatColab mathematical documentation forest"),
  ("plurigrid","plurigrid/commons","TypeScript",0,0,0,"2023-06-27T05:46:24Z",""),
  ("plurigrid","plurigrid/liquidity","",0,0,1,"2023-07-06T02:07:28Z",""),
  ("plurigrid","plurigrid/flussi","",0,0,1,"2023-07-15T06:40:11Z",""),
  ("plurigrid","plurigrid/VPP","Julia",0,1,0,"2023-01-11T18:41:07Z","Hyperreal Power Plant"),
  ("plurigrid","plurigrid/birbs","C++",0,0,0,"2023-04-15T01:56:32Z","Build native CosmWasm apps w/ Dart and Flutter!"),
  ("plurigrid","plurigrid/gridops","",0,0,2,"2022-07-16T03:02:28Z","monorepo: the monos for the monists"),
  ("plurigrid","plurigrid/cocreation-ui","",0,0,2,"2023-07-03T04:45:53Z",""),
  ("plurigrid","plurigrid/aptos-wallet-ruby","Ruby",1,0,0,"2025-09-30T22:47:22Z",""),
  ("plurigrid","plurigrid/gorj","Clojure",0,0,207,"2026-05-15T22:14:51Z","forj + Rama topology nREPL routing + GF(3) gay trit coloring"),
  ("plurigrid","plurigrid/ducklings","TypeScript",0,0,15,"2023-12-25T07:34:27Z",""),
  ("plurigrid","plurigrid/experiments","",0,0,0,"2023-11-17T05:39:07Z","Learning from Penrose development"),
  # kubeflow (48 repos)
  ("kubeflow","kubeflow/xgboost-operator","Python",77,53,22,"2021-12-01T18:00:10Z","Incubating project for xgboost operator"),
  ("kubeflow","kubeflow/testing","Python",60,86,33,"2025-02-14T18:33:13Z","Test infrastructure and tooling for Kubeflow."),
  ("kubeflow","kubeflow/spark-operator","Python",3125,1482,93,"2026-05-15T16:31:02Z","Kubernetes operator for managing the lifecycle of Apache Spark applications on Kubernetes."),
  ("kubeflow","kubeflow/crd-validation","Go",11,7,5,"2021-01-25T15:02:53Z","Validation Generation for Kubeflow CRD on Kubernetes"),
  ("kubeflow","kubeflow/trainer","Go",2098,949,103,"2026-05-15T15:21:03Z","Distributed AI Model Training and LLM Fine-Tuning on Kubernetes"),
  ("kubeflow","kubeflow/chainer-operator","Jsonnet",17,15,7,"2021-11-14T13:03:57Z","Repository for chainer operator"),
  ("kubeflow","kubeflow/metadata","TypeScript",123,63,38,"2021-12-01T17:35:27Z","Repository for assets related to Metadata."),
  ("kubeflow","kubeflow/mpi-operator","Go",526,235,100,"2026-05-12T17:13:37Z","Kubernetes Operator for MPI-based applications"),
  ("kubeflow","kubeflow/pipelines","Python",4140,1992,467,"2026-05-15T21:36:15Z","Machine Learning Pipelines for Kubeflow"),
  ("kubeflow","kubeflow/pipelines-components","Python",11,38,32,"2026-05-11T18:19:25Z","Kubeflow Pipelines"),
  ("kubeflow","kubeflow/mlflow-integration","Python",6,3,3,"2026-05-15T19:20:29Z",""),
  ("kubeflow","kubeflow/marketing-materials","",4,4,4,"2019-07-19T13:57:15Z",""),
  ("kubeflow","kubeflow/fairing","Jsonnet",337,143,134,"2022-04-11T05:28:47Z","Python SDK for building, training, and deploying ML models"),
  ("kubeflow","kubeflow/kubeflow","",15632,2648,2,"2026-05-07T13:46:41Z","Machine Learning Toolkit for Kubernetes"),
  ("kubeflow","kubeflow/frontend","JavaScript",8,18,12,"2021-12-01T17:41:37Z","Repository for kubeflow frontend"),
  ("kubeflow","kubeflow/internal-acls","Go",19,385,3,"2026-05-09T21:06:02Z","Repository used to main group ACLs used by Kubeflow developers"),
  ("kubeflow","kubeflow/batch-predict","Python",17,7,9,"2021-12-01T01:47:51Z","Repository for batch predict"),
  ("kubeflow","kubeflow/caffe2-operator","Go",16,12,2,"2021-12-01T01:58:06Z","Experimental repository for a caffe2 operator"),
  ("kubeflow","kubeflow/mcp-apache-spark-history-server","Python",170,60,24,"2026-05-13T19:15:35Z","MCP Server and CLI for Apache Spark History Server."),
  ("kubeflow","kubeflow/fate-operator","Go",51,15,6,"2024-02-22T19:44:08Z","Fate operator"),
  ("kubeflow","kubeflow/.github","",2,1,0,"2020-05-12T00:22:56Z","Org wide templates"),
  ("kubeflow","kubeflow/reporting","Jsonnet",2,5,1,"2021-12-01T01:42:32Z","Repository for collecting and analyzing metrics about Kubeflow usage."),
  ("kubeflow","kubeflow/mxnet-operator","Go",52,33,9,"2021-12-01T17:47:19Z","A Kubernetes operator for mxnet jobs"),
  ("kubeflow","kubeflow/community-infra","Go",3,9,4,"2021-01-25T14:49:49Z","Declarative configurations for KF community infrastructure"),
  ("kubeflow","kubeflow/kfserving-lts","Jsonnet",12,19,51,"2024-08-02T16:25:44Z",""),
  ("kubeflow","kubeflow/kfp-tekton","TypeScript",182,123,79,"2024-11-19T12:23:51Z","Kubeflow Pipelines on Tekton"),
  ("kubeflow","kubeflow/mcp-server","Python",7,8,18,"2026-05-12T10:14:24Z","MCP Server for AI-Assisted Development with Kubeflow Tools"),
  ("kubeflow","kubeflow/kfctl","Go",182,134,94,"2023-08-15T20:19:22Z","kfctl is a CLI for deploying and managing Kubeflow"),
  ("kubeflow","kubeflow/example-seldon","Jupyter Notebook",172,56,9,"2021-12-01T01:49:58Z","Example for end-to-end machine learning on Kubernetes using Kubeflow and Seldon Core"),
  ("kubeflow","kubeflow/kfp-tekton-backend","TypeScript",8,6,46,"2023-08-14T22:05:04Z","Experimental project plugging Tekton yaml behind KFP API and UI engine"),
  ("kubeflow","kubeflow/manifests","YAML",1017,1064,29,"2026-05-13T18:44:27Z","Kubeflow AI Reference Platform Deployment Manifests"),
  ("kubeflow","kubeflow/notebooks","",72,109,188,"2026-05-15T15:41:12Z","Kubeflow Notebooks"),
  ("kubeflow","kubeflow/common","Go",53,70,40,"2023-05-28T13:16:00Z","Common APIs and libraries shared by other Kubeflow operator repositories."),
  ("kubeflow","kubeflow/community","Jsonnet",196,257,14,"2026-05-13T18:53:18Z","Information about the Kubeflow community"),
  ("kubeflow","kubeflow/blog","Jupyter Notebook",32,62,27,"2026-05-11T15:21:33Z","Kubeflow blog based on fastpages"),
  ("kubeflow","kubeflow/pytorch-operator","Jsonnet",310,143,63,"2021-12-01T17:44:48Z","PyTorch on Kubernetes"),
  ("kubeflow","kubeflow/sdk","Python",117,174,136,"2026-05-12T18:53:41Z","Universal Python SDK to run AI workloads on Kubernetes"),
  ("kubeflow","kubeflow/hub","Go",175,178,51,"2026-05-15T15:36:02Z","Model Registry provides a single pane of glass for ML model developers"),
  ("kubeflow","kubeflow/kale","Python",687,156,57,"2026-05-15T19:04:47Z","Kubeflow's superfood for Data Scientists"),
  ("kubeflow","kubeflow/dashboard","TypeScript",17,55,79,"2026-05-13T03:07:39Z","Kubeflow Central Dashboard is the web interface for Kubeflow"),
  ("kubeflow","kubeflow/kubebench","Jsonnet",78,35,68,"2024-06-17T19:22:04Z","Repository for benchmarking"),
  ("kubeflow","kubeflow/.allstar","",2,0,0,"2022-12-06T23:07:59Z",""),
  ("kubeflow","kubeflow/website","HTML",184,920,54,"2026-05-14T17:20:09Z","Kubeflow Website"),
  ("kubeflow","kubeflow/code-intelligence","Jupyter Notebook",56,20,64,"2021-12-01T01:52:58Z","ML-Powered Developer Tools, using Kubeflow"),
  ("kubeflow","kubeflow/docs-agent","Python",36,98,153,"2026-04-14T03:33:15Z","Kubeflow Documentation AI Agent to power the Kubeflow Website"),
  ("kubeflow","kubeflow/katib","Python",1682,522,124,"2026-05-09T12:21:57Z","Automated Machine Learning on Kubernetes"),
  ("kubeflow","kubeflow/arena","Go",810,190,57,"2026-05-07T06:46:17Z","A CLI for Kubeflow."),
  ("kubeflow","kubeflow/examples","Jsonnet",1463,757,111,"2025-04-14T01:54:52Z","A repository to host extended examples and tutorials"),
  # TeglonLabs (4 repos)
  ("TeglonLabs","TeglonLabs/topoi","Python",0,0,1,"2025-01-24T04:49:26Z",""),
  ("TeglonLabs","TeglonLabs/mathpix-gem","Ruby",2,0,11,"2026-01-01T12:13:13Z","Transform mathematical images to LaTeX"),
  ("TeglonLabs","TeglonLabs/monad-mcp-server","",0,0,0,"2025-05-14T11:36:14Z","Monad MCP Server"),
  ("TeglonLabs","TeglonLabs/coin-flip-mcp","JavaScript",0,2,1,"2025-09-21T08:57:27Z","MCP server for flipping coins with varying degrees of randomness from random.org"),
  # migalkin (19 repos)
  ("migalkin","migalkin/ontologies","Web Ontology Language",0,0,0,"2015-12-06T13:49:53Z",""),
  ("migalkin","migalkin/datasciencecoursera","",0,0,0,"2015-02-12T23:57:16Z","The repo for the Coursera Data Science course"),
  ("migalkin","migalkin/migalkin.github.io","JavaScript",0,0,0,"2025-05-20T23:58:08Z","Github Pages template for academic personal websites"),
  ("migalkin","migalkin/LinkedData","",0,0,0,"2014-10-15T21:42:40Z","Information Workbench + Linked Open Data"),
  ("migalkin","migalkin/ekgs_clustering","Python",0,0,0,"2016-08-28T16:25:19Z",""),
  ("migalkin","migalkin/RWL","Python",7,1,0,"2025-02-10T14:12:14Z","Weisfeiler and Leman Go Relational (LOG 2022)"),
  ("migalkin","migalkin/edbt-experiments","",0,0,0,"2017-11-20T10:27:28Z",""),
  ("migalkin","migalkin/r_energyConsumption","R",0,0,0,"2016-05-12T21:00:17Z",""),
  ("migalkin","migalkin/InformationWorkbenchTestSrc","Java",0,0,0,"2014-10-15T21:42:40Z",""),
  ("migalkin","migalkin/SMJoin-experiments","R",1,0,0,"2020-03-04T15:56:23Z","ISWC 2017 SMJoin results"),
  ("migalkin","migalkin/rambo","Rust",3,0,1,"2023-02-28T16:37:22Z",""),
  ("migalkin","migalkin/StarE","Python",89,16,1,"2026-04-16T14:12:45Z","EMNLP 2020: Message Passing for Hyper-Relational Knowledge Graphs"),
  ("migalkin","migalkin/Tables_Provider","Java",0,0,0,"2015-03-20T00:17:36Z",""),
  ("migalkin","migalkin/NBFNet_mlx","Python",10,1,1,"2026-03-11T01:31:21Z","Neural Bellman-Ford networks implemented in MLX for Apple Silicon"),
  ("migalkin","migalkin/ciss2_project","Jupyter Notebook",0,0,6,"2019-06-28T23:14:33Z",""),
  ("migalkin","migalkin/SQuAD-es-mt","",0,1,0,"2020-07-14T17:18:37Z","Spanish version of SQuAD 1.1 and 2.0 obtained via machine translation"),
  ("migalkin","migalkin/kgcourse2021","HTML",25,9,0,"2026-02-16T05:16:08Z","Materials for Knowledge Graphs course"),
  ("migalkin","migalkin/NodePiece","Python",144,21,0,"2026-05-07T05:40:02Z","Compositional and Parameter-Efficient Representations (ICLR'22)"),
  ("migalkin","migalkin/netquery_rdf","Python",0,0,0,"2019-06-01T12:49:18Z","NIPS 2018 paper fork for RDF"),
  # wasita (11 repos)
  ("wasita","wasita/wasita.github.io","Svelte",1,0,8,"2026-05-14T02:10:55Z","personal website"),
  ("wasita","wasita/magic-garden","Python",2,1,1,"2026-04-22T21:16:43Z","a bot written for the magic garden discord activity game"),
  ("wasita","wasita/wins-search","CSS",1,0,0,"2023-06-03T19:01:11Z","Women in Network Science (WiNS) member list website"),
  ("wasita","wasita/ch3-lib","Typst",0,0,0,"2026-04-12T04:03:22Z",""),
  ("wasita","wasita/d60-keeb","",0,0,0,"2024-08-26T00:46:25Z",""),
  ("wasita","wasita/wm-cv","Svelte",0,0,0,"2026-05-13T05:29:08Z","Academic CV written as a single page web app"),
  ("wasita","wasita/send2kobo","TypeScript",0,0,0,"2025-12-12T19:09:16Z","Website for sending books to your kobo e-reader"),
  ("wasita","wasita/food-diary","Svelte",0,0,0,"2025-12-13T01:06:43Z",""),
  ("wasita","wasita/proj-template","",0,0,0,"2026-01-09T20:55:46Z",""),
  ("wasita","wasita/honeycomb-demo","JavaScript",0,0,0,"2021-12-07T21:38:28Z",""),
  ("wasita","wasita/vocoder","JavaScript",0,0,0,"2026-05-06T05:14:03Z",""),
  # kristinezheng (6 repos)
  ("kristinezheng","kristinezheng/Portfolio","",0,0,0,"2025-02-12T00:00:45Z","July 2021"),
  ("kristinezheng","kristinezheng/Green-Machine","Python",0,0,0,"2021-09-19T05:33:04Z","HackMIT 2021: Sustainability Track"),
  ("kristinezheng","kristinezheng/lookit-jenga","Jupyter Notebook",0,0,0,"2024-05-16T18:29:05Z","Lookit study for 9.85"),
  ("kristinezheng","kristinezheng/auditory-illusion","CSS",0,0,0,"2022-03-07T02:57:44Z","9.35 spring 2022 auditory illusion"),
  ("kristinezheng","kristinezheng/kristinezheng.github.io","HTML",0,0,0,"2026-05-14T22:29:01Z",""),
  ("kristinezheng","kristinezheng/graph_example","Python",0,0,0,"2021-10-08T07:29:53Z",""),
  # M1shaaa (8 repos)
  ("M1shaaa","M1shaaa/lab-bookshelf-","TypeScript",0,0,0,"2024-12-31T05:11:18Z",""),
  ("M1shaaa","M1shaaa/Lookit-Demo","",0,0,0,"2023-04-10T02:44:01Z",""),
  ("M1shaaa","M1shaaa/Classes","",0,0,0,"2023-12-06T18:20:27Z",""),
  ("M1shaaa","M1shaaa/rosie-s-study-3-lookit-project","",0,0,0,"2024-11-04T22:15:39Z",""),
  ("M1shaaa","M1shaaa/M1shaaa","",0,0,0,"2026-02-04T19:32:04Z","Config files for my GitHub profile."),
  ("M1shaaa","M1shaaa/Python-Lookit-Uploads","Python",0,0,0,"2024-02-15T22:59:37Z","random projects"),
  ("M1shaaa","M1shaaa/MNIST-Classifier","",0,0,0,"2023-11-28T06:10:47Z",""),
  ("M1shaaa","M1shaaa/Yale-Work","HTML",0,0,0,"2023-12-06T18:33:14Z",""),
  # AustinCStone (29 repos shown)
  ("AustinCStone","AustinCStone/TheanoStuff","Python",0,0,0,"2021-09-04T03:21:57Z","Getting acquainted with Theano"),
  ("AustinCStone","AustinCStone/Founderati-Server","Python",0,1,0,"2015-08-25T19:17:45Z","Server for Founderati"),
  ("AustinCStone","AustinCStone/SleepDetectionMoto360","Java",0,0,0,"2014-10-19T03:21:34Z","Uses heart rate and accelerometer data to detect when the wearer has entered R.E.M. sleep."),
  ("AustinCStone","AustinCStone/TFBirds","Python",0,0,0,"2019-01-30T08:07:22Z","Bird flocking simulator in TensorFlow."),
  ("AustinCStone","AustinCStone/bmfork","Python",0,0,1,"2025-05-09T04:18:54Z",""),
  ("AustinCStone","AustinCStone/stuffForAlec","JavaScript",0,0,0,"2015-01-05T01:34:25Z",""),
  ("AustinCStone","AustinCStone/Founderati-client","JavaScript",0,1,0,"2015-08-25T19:16:58Z","Founderati client"),
  ("AustinCStone","AustinCStone/stonks","Python",0,0,0,"2020-09-04T22:54:35Z","Playing around with some option calculations."),
  ("AustinCStone","AustinCStone/statsHw2","Python",0,0,0,"2015-09-28T00:50:31Z","Simple linear regression and model selection"),
  ("AustinCStone","AustinCStone/TextGAN","Python",92,30,5,"2025-03-03T13:26:32Z","A generative adversarial network for text generation, written in TensorFlow."),
  ("AustinCStone","AustinCStone/OptimalControl","Python",0,0,0,"2018-02-03T08:08:51Z","Practicing some concepts from control theory."),
  ("AustinCStone","AustinCStone/StereoVisionMRF","Python",11,4,0,"2026-04-01T07:39:41Z","Using a MRF with loopy belief propagation to infer depth from stereo images."),
  ("AustinCStone","AustinCStone/LensBuilder","Python",0,0,0,"2019-04-04T04:28:08Z","WIP optimize for the surface of a focusing lens by casting rays"),
  ("AustinCStone","AustinCStone/Genetic-Algorithm-Sorting-Network","Python",0,0,0,"2015-05-09T03:20:47Z",""),
  ("AustinCStone","AustinCStone/QuantumSearchAlgorithmSimulation","Java",0,0,0,"2014-11-07T02:09:38Z","A simulation of Grover's algorithm"),
  ("AustinCStone","AustinCStone/testLogin","Python",0,0,0,"2023-02-13T20:52:27Z",""),
  ("AustinCStone","AustinCStone/gibbs_sampling","Python",0,0,0,"2023-07-23T17:30:23Z","gibbs sampling and ancestral rejection sampling"),
  ("AustinCStone","AustinCStone/FlaskBlog","Python",0,0,0,"2014-12-17T23:45:06Z","A simple blog written with Flask"),
  ("AustinCStone","AustinCStone/bitmind-fork","",0,0,0,"2025-01-09T06:16:51Z","forked on jan 8 2025"),
  ("AustinCStone","AustinCStone/Royal-Road-With-Ditches-Genetic-Algorithm","Python",0,0,0,"2014-05-11T02:27:57Z","A modification of the Royal Road genetic algorithm."),
  ("AustinCStone","AustinCStone/Z-order-curve","Python",0,0,0,"2019-06-09T02:53:43Z","Demo implementation of z-order curve"),
  ("AustinCStone","AustinCStone/ConvNet","Python",0,0,0,"2015-09-07T22:25:29Z","A convolutional neural network for classifying the MNIST database."),
  ("AustinCStone","AustinCStone/SpectralClustering","Python",3,2,0,"2021-04-16T08:46:36Z","Implementing spectral clustering"),
  ("AustinCStone","AustinCStone/StructureFromMotion","Python",1,0,0,"2019-04-26T19:43:12Z","Recover 3D geometry from videos with unknown camera calibration"),
  ("AustinCStone","AustinCStone/austincstone.github.io","HTML",0,0,0,"2021-10-23T22:48:49Z",""),
  ("AustinCStone","AustinCStone/StatsModelingHw1","Python",0,0,0,"2015-09-19T04:13:53Z","My first homework for statistical modeling"),
  ("AustinCStone","AustinCStone/test","",0,0,0,"2021-09-21T21:15:50Z",""),
  ("AustinCStone","AustinCStone/EpsteinSearch","Python",0,0,0,"2026-02-11T01:10:57Z",""),
  ("AustinCStone","AustinCStone/LearningCuda","C",0,0,0,"2017-11-05T20:31:07Z","Me working through CUDA by example"),
  # DJedamski (6 repos)
  ("DJedamski","DJedamski/Project_Euler","",0,0,0,"2015-09-05T17:13:32Z",""),
  ("DJedamski","DJedamski/Getting-and-Cleaning-Data","R",1,0,0,"2023-04-21T01:42:34Z","Coursera Project"),
  ("DJedamski","DJedamski/kaggle_ncaa18","Jupyter Notebook",0,0,0,"2018-02-26T16:33:24Z","Code for NCAA March Madness competition (2018)"),
  ("DJedamski","DJedamski/Kaggle","",1,0,0,"2023-04-21T01:42:35Z",""),
  ("DJedamski","DJedamski/School","R",1,1,0,"2023-04-21T01:42:33Z","A couple small projects from grad school"),
  ("DJedamski","DJedamski/EDA","R",0,0,0,"2014-11-09T17:00:39Z","Coursera Project"),
]

# Insert repo_snapshots + world_increments
inc_id = 1
repo_id = 1
for (org, full_name, lang, stars, forks, issues, pushed_at, desc) in repos:
    trit, color, name = gf3(inc_id)
    h = snap_hash(full_name + pushed_at)
    repo_short = full_name.split("/", 1)[-1]
    con.execute("""
      INSERT INTO world_increments VALUES (?, now(), ?, ?, ?, 'github_repo', ?, 'repo_push', ?, ?, ?)
    """, [inc_id, trit, color, name, org, repo_short, org, h])
    con.execute("""
      INSERT INTO repo_snapshots VALUES (?, now(), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [repo_id, inc_id, org, repo_short, full_name, lang or None,
          stars, forks, issues, pushed_at, desc or None])
    inc_id += 1
    repo_id += 1

print(f"Inserted {inc_id-1} world_increments and repo_snapshots")

# ── Aptos snapshots ────────────────────────────────────────────────────────
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
for (world, addr, bal) in aptos:
    con.execute("INSERT INTO aptos_snapshots VALUES (now(), ?, ?, ?)", [world, addr, bal])
print(f"Inserted {len(aptos)} aptos_snapshots")

# ── Multisig probes ────────────────────────────────────────────────────────
multisigs = [
  ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2,True),
  ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2,True),
  ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2,True),
  ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2,True),
  ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2,True),
]
for (pair, addr, sigs, healthy) in multisigs:
    con.execute("INSERT INTO multisig_probes VALUES (now(), ?, ?, ?, ?)", [pair, addr, sigs, healthy])
print(f"Inserted {len(multisigs)} multisig_probes (all sigs_required=2, healthy=True)")

# MNX: SPA, no public API data available
print("MNX: Next.js SPA - no market data API accessible; mnx_snapshots table created but empty")

# ── Summary query ──────────────────────────────────────────────────────────
r = con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0]
print(f"Total world_increments: {r}")
r2 = con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0]
print(f"Total repo_snapshots: {r2}")

con.close()
print("Done.")
