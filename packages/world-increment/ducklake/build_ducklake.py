#!/usr/bin/env python3
"""World-increment sweep + Hamming swarm snapshot builder."""
import duckdb
import json
import subprocess
import time
import os
import hashlib
from datetime import datetime, timezone

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"

# GF(3) color chain
def gf3(id_num):
    t = id_num % 3
    if t == 0:
        return (0, "#d3869b", "ERGODIC")
    elif t == 1:
        return (1, "#b8bb26", "PLUS")
    else:
        return (-1, "#cc241d", "MINUS")

con = duckdb.connect(DB_PATH)

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

try:
    con.execute("CREATE SEQUENCE IF NOT EXISTS increment_seq START 1")
except:
    pass
try:
    con.execute("CREATE SEQUENCE IF NOT EXISTS repo_seq START 1")
except:
    pass

# ── GitHub repo data ──────────────────────────────────────────────────────────

repos = [
# plurigrid (100)
("plurigrid","plurigrid/asi","HTML",25,7,4,"2026-06-10T12:51:42Z","everything is topological chemputer!"),
("plurigrid","plurigrid/place","TeX",1,2,8,"2026-06-10T16:25:05Z",""),
("plurigrid","plurigrid/eirobri","Clojure",0,0,29,"2026-06-03T20:43:46Z","EiRoBri replay world"),
("plurigrid","plurigrid/nash-portal","Rust",2,3,1,"2026-05-19T01:49:59Z","NASH token TUI in the browser"),
("plurigrid","plurigrid/gorj","Clojure",0,0,508,"2026-06-11T20:13:02Z","forj + Rama topology nREPL routing + GF(3) gay trit coloring"),
("plurigrid","plurigrid/zig-syrup","Zig",2,2,0,"2026-04-30T03:52:16Z","High-performance Zig OCapN Syrup"),
("plurigrid","plurigrid/asi-skills","Julia",3,1,0,"2026-04-26T08:09:26Z","69 skills with Galois Hole Type accessibility"),
("plurigrid","plurigrid/bci-blue-share","JavaScript",0,0,0,"2026-04-26T07:08:03Z","BCI signal infrastructure"),
("plurigrid","plurigrid/nanoclj-zig","Zig",1,2,20,"2026-04-25T07:29:09Z","NaN-boxed Clojure interpreter in Zig"),
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
("plurigrid","plurigrid/json-canvas","",0,0,0,"2026-02-06T06:50:57Z","JSON Canvas real-time interaction data"),
("plurigrid","plurigrid/shepherd","Scheme",0,0,0,"2026-01-23T07:47:28Z","Spritely Shepherd"),
("plurigrid","plurigrid/goblinshare","Scheme",0,0,0,"2026-01-23T07:47:12Z","P2P filesharing demo for Goblins"),
("plurigrid","plurigrid/magenc","Scheme",0,0,0,"2026-01-23T07:47:11Z","Magenc Magnet URIs"),
("plurigrid","plurigrid/hoot","Scheme",0,0,1,"2026-01-23T07:47:10Z","Spritely Hoot Scheme to WebAssembly"),
("plurigrid","plurigrid/leprechauns","Racket",0,0,0,"2026-01-23T07:46:46Z","Spritely Goblins + Gay.jl semantic colors"),
("plurigrid","plurigrid/spritely-semantic-colors","",0,0,0,"2026-01-23T07:38:32Z","Deterministic color mappings for Spritely"),
("plurigrid","plurigrid/gay-tofu","HTML",0,0,0,"2026-01-08T15:14:34Z","Low-discrepancy color sequences for TOFU"),
("plurigrid","plurigrid/lazygay","Go",0,0,0,"2026-01-08T14:19:25Z","lazygit fork with Gay.jl coloring"),
("plurigrid","plurigrid/gay-terminal","Rust",0,0,0,"2026-01-08T14:19:24Z","Terminal ANSI coloring with Gay.jl"),
("plurigrid","plurigrid/gay-go","Go",0,0,0,"2026-01-08T14:19:23Z","Go implementation of Gay.jl"),
("plurigrid","plurigrid/gay-rs","Rust",0,0,0,"2026-01-08T14:19:22Z","Rust crate for Gay.jl"),
("plurigrid","plurigrid/lazybjj","Rust",0,0,0,"2026-01-08T14:19:19Z","TUI for jj with Gay.jl GF(3) coloring"),
("plurigrid","plurigrid/agent-o-rama","Clojure",0,0,0,"2026-01-02T01:09:22Z",""),
("plurigrid","plurigrid/aptos-wallet-ruby","Ruby",1,0,0,"2025-09-30T22:47:22Z",""),
("plurigrid","plurigrid/duck-kanban","Rust",1,0,0,"2025-09-26T20:18:38Z","Duck intelligence kanban system"),
("plurigrid","plurigrid/shiteshiteshite","",0,0,0,"2025-09-26T03:07:20Z","Duck intelligence kanban system"),
("plurigrid","plurigrid/discohy","Hy",0,0,0,"2025-09-10T02:01:31Z",""),
("plurigrid","plurigrid/telemind","",0,0,0,"2025-06-12T05:54:59Z",""),
("plurigrid","plurigrid/ontology","JavaScript",8,9,16,"2025-05-27T18:18:34Z","autopoietic ergodicity and embodied gradualism"),
("plurigrid","plurigrid/Plurigraph","JavaScript",3,5,4,"2025-01-05T08:39:09Z","Plurigrid knowledge base for Obsidian"),
("plurigrid","plurigrid/signe","Python",0,0,0,"2024-08-15T20:52:03Z","Signal messages data traversal"),
("plurigrid","plurigrid/SwiftDuck","",0,0,0,"2024-08-08T18:19:06Z",""),
("plurigrid","plurigrid/act","Python",3,1,4,"2024-07-26T08:27:08Z","building blocks for cognitive category theory"),
("plurigrid","plurigrid/xenomorphic","",0,0,0,"2024-04-09T03:24:55Z",""),
("plurigrid","plurigrid/metamorphic","",0,0,0,"2024-04-09T03:22:41Z",""),
("plurigrid","plurigrid/DiffusionVoiceDemo","Clojure",0,0,0,"2024-04-02T18:09:01Z",""),
("plurigrid","plurigrid/website","Clojure",0,1,0,"2024-03-30T04:37:51Z",""),
("plurigrid","plurigrid/StochFlow","Python",4,1,0,"2024-03-20T23:34:57Z","stochastic interpolant models"),
("plurigrid","plurigrid/intent","",0,0,0,"2024-03-04T04:53:38Z","Simulations for Intent Markets"),
("plurigrid","plurigrid/novella","TypeScript",1,0,0,"2024-01-27T08:12:55Z",""),
("plurigrid","plurigrid/ACT.jl","Julia",0,0,0,"2024-01-21T00:02:25Z","applied categorical duck cybernetics"),
("plurigrid","plurigrid/ducklings","TypeScript",0,0,15,"2023-12-25T07:34:27Z",""),
("plurigrid","plurigrid/paretae","TypeScript",0,0,14,"2023-11-20T05:14:42Z",""),
("plurigrid","plurigrid/experiments","",0,0,0,"2023-11-17T05:39:07Z","Learning archive of experiments"),
("plurigrid","plurigrid/fuckit","Clojure",0,0,0,"2023-11-14T21:26:14Z",""),
("plurigrid","plurigrid/omega","Clojure",0,0,0,"2023-11-07T21:08:46Z",""),
("plurigrid","plurigrid/org","Jupyter Notebook",2,0,1,"2023-11-07T01:08:05Z","Dynamically Replicating Duck"),
("plurigrid","plurigrid/CVAE-Flows","",0,0,0,"2023-10-24T14:41:32Z","Leveraging dihypergraphs for conversation flow"),
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
("plurigrid","plurigrid/birbs","C++",0,0,0,"2023-04-15T01:56:32Z","Build native CosmWasm apps"),
("plurigrid","plurigrid/agent","Python",5,1,6,"2023-03-31T18:45:23Z","Framework for agency amplification"),
("plurigrid","plurigrid/vcg-auction","Rust",7,2,1,"2023-03-16T21:53:08Z","simple contract VCG auction"),
("plurigrid","plurigrid/bidder","Dart",0,0,1,"2023-03-15T15:23:22Z","simple flutter app for VCG auction"),
("plurigrid","plurigrid/plurigrid.github.io","HTML",1,2,2,"2023-01-20T03:27:34Z",""),
("plurigrid","plurigrid/VPP","Julia",0,1,0,"2023-01-11T18:41:07Z","Hyperreal Power Plant"),
("plurigrid","plurigrid/grid","TypeScript",2,1,1,"2023-01-02T11:55:55Z","Plurigrid Testnet #0: Edith Clarke"),
("plurigrid","plurigrid/commons-contracts","Rust",0,0,0,"2022-09-09T09:20:11Z","CosmWasm contracts"),
("plurigrid","plurigrid/plurigrid.xyz","TypeScript",0,0,1,"2022-08-31T05:26:14Z",""),
# kubeflow (48)
("kubeflow","kubeflow/community","Jupyter Notebook",194,258,17,"2026-06-11T20:54:39Z","Information about the Kubeflow community"),
("kubeflow","kubeflow/trainer","Go",2111,965,118,"2026-06-11T20:46:11Z","Distributed AI Model Training and LLM Fine-Tuning on Kubernetes"),
("kubeflow","kubeflow/docs-agent","Python",38,95,150,"2026-06-11T18:43:15Z","Kubeflow Documentation AI Agent"),
("kubeflow","kubeflow/internal-acls","Go",19,389,1,"2026-06-11T18:23:36Z","Repository for group ACLs"),
("kubeflow","kubeflow/kubeflow","",15713,2671,3,"2026-06-11T16:32:05Z","Machine Learning Toolkit for Kubernetes"),
("kubeflow","kubeflow/website","HTML",184,923,47,"2026-06-11T16:32:01Z","Kubeflow Website"),
("kubeflow","kubeflow/blog","Jupyter Notebook",32,62,26,"2026-06-11T16:32:01Z","Kubeflow blog"),
("kubeflow","kubeflow/hub","Go",173,181,42,"2026-06-11T16:27:58Z","Model Registry single pane of glass"),
("kubeflow","kubeflow/pipelines","Python",4152,2005,493,"2026-06-11T16:09:57Z","Machine Learning Pipelines for Kubeflow"),
("kubeflow","kubeflow/mlflow-integration","Python",6,4,2,"2026-06-10T21:26:34Z",""),
("kubeflow","kubeflow/mcp-apache-spark-history-server","Python",177,64,21,"2026-06-10T18:49:04Z","MCP Server for Apache Spark History Server"),
("kubeflow","kubeflow/kale","Python",692,155,47,"2026-06-10T17:35:51Z","Kubeflow superfood for Data Scientists"),
("kubeflow","kubeflow/spark-operator","Python",3126,1489,101,"2026-06-09T17:15:24Z","Kubernetes operator for Apache Spark"),
("kubeflow","kubeflow/manifests","YAML",1022,1065,22,"2026-06-09T13:01:47Z","Kubeflow Community Distribution"),
("kubeflow","kubeflow/notebooks","",73,118,166,"2026-06-09T15:34:30Z","Kubeflow Notebooks interactive environments"),
("kubeflow","kubeflow/katib","Python",1683,525,119,"2026-06-05T23:23:35Z","Automated Machine Learning on Kubernetes"),
("kubeflow","kubeflow/dashboard","TypeScript",16,59,75,"2026-06-11T17:07:50Z","Kubeflow Central Dashboard"),
("kubeflow","kubeflow/sdk","Python",120,181,133,"2026-06-08T03:07:18Z","Universal Python SDK for AI workloads on Kubernetes"),
("kubeflow","kubeflow/mpi-operator","Go",528,236,104,"2026-06-02T14:30:58Z","Kubernetes Operator for MPI-based applications"),
("kubeflow","kubeflow/pipelines-components","Python",11,43,33,"2026-06-04T17:39:10Z","Kubeflow Pipelines components"),
("kubeflow","kubeflow/mcp-server","Python",11,20,25,"2026-05-12T10:14:24Z","MCP Server for AI-Assisted Kubeflow Development"),
("kubeflow","kubeflow/arena","Go",812,190,46,"2026-05-07T06:46:17Z","CLI for Kubeflow"),
("kubeflow","kubeflow/examples","Jsonnet",1461,756,111,"2025-04-14T01:54:52Z","Extended examples and tutorials"),
("kubeflow","kubeflow/testing","Python",60,86,33,"2025-02-14T18:33:13Z","Test infrastructure for Kubeflow"),
("kubeflow","kubeflow/kfp-tekton","TypeScript",182,123,79,"2024-11-19T12:23:51Z","Kubeflow Pipelines on Tekton"),
("kubeflow","kubeflow/kfserving-lts","Jsonnet",12,19,51,"2024-08-02T16:25:44Z",""),
("kubeflow","kubeflow/kubebench","Jsonnet",78,35,68,"2024-06-17T19:22:04Z","Repository for benchmarking"),
("kubeflow","kubeflow/fate-operator","Go",51,15,6,"2024-02-22T19:44:08Z","Fate operator"),
("kubeflow","kubeflow/kfctl","Go",182,134,94,"2023-08-15T20:19:22Z","CLI for deploying Kubeflow"),
("kubeflow","kubeflow/kfp-tekton-backend","TypeScript",8,6,46,"2023-08-14T22:05:04Z","Experimental Tekton backend for KFP"),
("kubeflow","kubeflow/common","Go",53,70,40,"2023-05-28T13:16:00Z","Common APIs and libraries for Kubeflow"),
("kubeflow","kubeflow/.allstar","",2,0,0,"2022-12-06T23:07:59Z",""),
("kubeflow","kubeflow/fairing","Jsonnet",337,143,134,"2022-04-11T05:28:47Z","Python SDK for building and training ML models"),
("kubeflow","kubeflow/xgboost-operator","Python",77,53,22,"2021-12-01T18:00:10Z","xgboost operator"),
("kubeflow","kubeflow/mxnet-operator","Go",52,33,9,"2021-12-01T17:47:19Z","Kubernetes operator for mxnet"),
("kubeflow","kubeflow/pytorch-operator","Jsonnet",310,143,63,"2021-12-01T17:44:48Z","PyTorch on Kubernetes"),
("kubeflow","kubeflow/frontend","JavaScript",8,18,12,"2021-12-01T17:41:37Z","Kubeflow frontend"),
("kubeflow","kubeflow/metadata","TypeScript",123,63,38,"2021-12-01T17:35:27Z","Metadata assets"),
("kubeflow","kubeflow/caffe2-operator","Go",16,12,2,"2021-12-01T01:58:06Z","Experimental caffe2 operator"),
("kubeflow","kubeflow/code-intelligence","Jupyter Notebook",56,20,64,"2021-12-01T01:52:58Z","ML-Powered Developer Tools"),
("kubeflow","kubeflow/example-seldon","Jupyter Notebook",172,56,9,"2021-12-01T01:49:58Z","Example Kubeflow + Seldon Core"),
("kubeflow","kubeflow/batch-predict","Python",17,7,9,"2021-12-01T01:47:51Z","Batch predict"),
("kubeflow","kubeflow/reporting","Jsonnet",2,5,1,"2021-12-01T01:42:32Z","Metrics about Kubeflow usage"),
("kubeflow","kubeflow/chainer-operator","Jsonnet",17,15,7,"2021-11-14T13:03:57Z","Chainer operator"),
("kubeflow","kubeflow/crd-validation","Go",11,7,5,"2021-01-25T15:02:53Z","Validation for Kubeflow CRD"),
("kubeflow","kubeflow/community-infra","Go",3,9,4,"2021-01-25T14:49:49Z","Declarative configs for KF community"),
("kubeflow","kubeflow/.github","",2,1,0,"2020-05-12T00:22:56Z","Org wide templates"),
("kubeflow","kubeflow/marketing-materials","",4,4,4,"2019-07-19T13:57:15Z",""),
# TeglonLabs (5)
("TeglonLabs","TeglonLabs/jank-crane","C++",0,0,0,"2026-06-08T19:03:03Z","crane-jank converged-IR hub"),
("TeglonLabs","TeglonLabs/mathpix-gem","Ruby",2,0,11,"2026-01-01T12:13:13Z","Mathematical images to LaTeX"),
("TeglonLabs","TeglonLabs/coin-flip-mcp","JavaScript",0,2,1,"2025-09-21T08:57:27Z","MCP server for flipping coins"),
("TeglonLabs","TeglonLabs/monad-mcp-server","",0,0,0,"2025-05-14T11:36:14Z","Monad MCP Server"),
("TeglonLabs","TeglonLabs/topoi","Python",0,0,1,"2025-01-24T04:49:26Z",""),
# bmorphism (100)
("bmorphism","bmorphism/satreadout","Lean",0,0,0,"2026-06-10T22:47:47Z","Machine-checked saturating non-Riemannian perceptual readout"),
("bmorphism","bmorphism/Gay.jl","Julia",1,1,189,"2026-06-11T00:43:04Z","Wide-gamut color sampling with splittable determinism"),
("bmorphism","bmorphism/world","Python",0,0,0,"2026-06-02T06:49:02Z","Local worlds launcher"),
("bmorphism","bmorphism/oxgame","OCaml",0,0,0,"2026-05-15T09:53:27Z","Stellar resolution and open-game composition"),
("bmorphism","bmorphism/nanoclj-zig","Zig",1,0,0,"2026-05-07T20:12:15Z",""),
("bmorphism","bmorphism/zig-syrup","Zig",0,0,0,"2026-05-07T19:49:05Z","Embeddable OCapN Syrup encoder/decoder in Zig"),
("bmorphism","bmorphism/boxxy","Move",0,1,0,"2026-04-30T03:35:47Z",""),
("bmorphism","bmorphism/postweb","Go",0,0,0,"2026-04-09T10:51:57Z","postweb evolved from prepostweb"),
("bmorphism","bmorphism/shitcoin","Python",5,0,0,"2026-04-08T08:07:08Z","gets denom for cw20 assets"),
("bmorphism","bmorphism/magic-world-org","Python",1,0,0,"2026-04-05T07:03:50Z","Magic World Org"),
("bmorphism","bmorphism/ocaml-mcp-sdk","OCaml",61,2,0,"2026-03-16T05:24:25Z","OCaml SDK for Model Context Protocol"),
("bmorphism","bmorphism/flox-mcp-bb","Clojure",0,0,0,"2026-02-12T02:45:43Z","Open-source MCP server for Flox"),
("bmorphism","bmorphism/vibesnipe-market","Move",0,0,9,"2026-02-05T10:23:25Z",""),
("bmorphism","bmorphism/tapes","",0,0,0,"2026-02-04T02:23:37Z","VHS tapes for terminal recordings"),
("bmorphism","bmorphism/duck-rio-heateq","Rust",0,0,0,"2026-02-02T23:33:32Z",""),
("bmorphism","bmorphism/aella","Rascal",1,0,0,"2026-02-01T02:44:30Z",""),
("bmorphism","bmorphism/hymlx","Python",1,0,0,"2026-01-22T12:20:32Z",""),
("bmorphism","bmorphism/GeoACSets.jl","Julia",0,1,1,"2026-01-19T13:57:13Z","Categorical data structures with geospatial capabilities"),
("bmorphism","bmorphism/anti-bullshit-mcp-server","JavaScript",23,7,1,"2026-01-16T08:54:58Z","MCP server for analyzing claims"),
("bmorphism","bmorphism/vibespace-mcp-go-ternary","HTML",0,1,3,"2026-01-11T12:50:40Z","Go MCP experience for vibes with ternary"),
("bmorphism","bmorphism/open-location-code-zig","Zig",3,0,0,"2025-12-30T19:33:45Z","Open Location Code for Zig"),
("bmorphism","bmorphism/bafishka","Clojure",1,0,0,"2025-12-19T09:38:00Z","Fish shell-friendly file operations"),
("bmorphism","bmorphism/gay-color-learnable","",0,0,0,"2025-12-15T18:41:02Z","Learnable color embeddings"),
("bmorphism","bmorphism/gay-hy","Hy",0,0,0,"2025-12-15T15:32:58Z","Hylang MLX color bandwidth protocol"),
("bmorphism","bmorphism/multiverse-color-game","Julia",0,0,0,"2025-12-12T05:28:11Z","2+1D Holographic Color Matching Game"),
("bmorphism","bmorphism/signal-mcp","Rust",0,0,0,"2025-12-11T07:20:08Z","O(n) to O(1) chromatic mode collapse"),
("bmorphism","bmorphism/xf.jl","Julia",0,0,0,"2025-12-05T22:12:17Z","Xenofeminist color synthesis"),
("bmorphism","bmorphism/deberta-goemotions","Python",0,0,0,"2025-10-22T18:32:24Z",""),
("bmorphism","bmorphism/monero-rental-hash-war","Haskell",1,0,0,"2025-10-05T23:08:54Z","Compositional OpenGame analysis"),
("bmorphism","bmorphism/duck-rs","Zig",0,0,0,"2025-10-05T00:21:07Z",""),
("bmorphism","bmorphism/schoenfinkel","Python",1,0,0,"2025-10-04T23:31:11Z","Post-quantum categorical gravity framework"),
("bmorphism","bmorphism/gay-spec","",1,0,0,"2025-10-02T02:01:56Z",""),
("bmorphism","bmorphism/bafishka-clean","Rust",1,0,0,"2025-09-25T19:22:10Z","Clean monadic Steel-SCI integration"),
("bmorphism","bmorphism/babashka-static-build","Dockerfile",1,0,0,"2025-09-05T02:26:32Z","Static musl babashka build for ARM64 Termux"),
("bmorphism","bmorphism/whale","MATLAB",2,0,0,"2025-09-04T06:55:21Z","omniglot + sperm whale codas = metawhaling"),
("bmorphism","bmorphism/infinity-topos","Python",1,0,0,"2025-08-29T05:39:49Z",""),
("bmorphism","bmorphism/elevenlabs-mcp-enhanced","Python",1,0,0,"2025-08-29T04:41:58Z","Enhanced ElevenLabs MCP server"),
("bmorphism","bmorphism/zeldar","Python",1,0,1,"2025-08-26T15:16:21Z","Burning Man Art Robot"),
("bmorphism","bmorphism/stellogen-quantum-operads","",1,0,0,"2025-07-15T04:49:41Z","Quantum Operads and ZX-Calculus"),
("bmorphism","bmorphism/apple-container-framework","Clojure",0,0,0,"2025-07-13T12:12:10Z","Apple Container Framework"),
("bmorphism","bmorphism/ezkl-ethglobal2025","Python",1,0,0,"2025-07-07T01:16:01Z",""),
("bmorphism","bmorphism/zk-haiku-nanogpt","Solidity",1,0,0,"2025-07-06T03:08:24Z","ZK-Haiku-NanoGPT"),
("bmorphism","bmorphism/rama-event-processor","Java",1,0,0,"2025-07-02T07:01:44Z","Processing events with Rama"),
("bmorphism","bmorphism/oxcaml-sci-canonical","OCaml",1,0,0,"2025-06-20T06:37:12Z","Canonical OxCaml-SCI implementation"),
("bmorphism","bmorphism/oxcaml-mcp","",0,0,0,"2025-06-20T04:04:34Z","OxCaml-MCP server"),
("bmorphism","bmorphism/oxcaml-sci","",0,0,0,"2025-06-20T03:48:11Z","OxCaml-SCI performance-optimized"),
("bmorphism","bmorphism/infinity-topos-impossibility","",0,0,14,"2025-05-29T01:55:28Z","Impossibility results for automated analysis"),
("bmorphism","bmorphism/graphistry-mcp","Python",2,0,0,"2025-05-06T17:34:24Z","Graphistry MCP integration"),
("bmorphism","bmorphism/hypernym-mcp-server","JavaScript",6,5,0,"2025-04-02T21:21:08Z",""),
("bmorphism","bmorphism/vibespace-mcp-go","",0,0,0,"2025-03-19T20:30:02Z","Go MCP experience for vibes"),
("bmorphism","bmorphism/krep-mcp-server","JavaScript",1,1,1,"2025-03-19T20:22:46Z","High-performance string search MCP server"),
("bmorphism","bmorphism/minecraft-mcp-golf","",0,0,0,"2025-03-16T10:33:31Z","Minecraft server with MCP capabilities"),
("bmorphism","bmorphism/worlds-code-explorer","",0,0,0,"2025-03-16T05:46:58Z","Code projects from different worlds"),
("bmorphism","bmorphism/voice-fn","",0,0,0,"2025-02-24T22:28:32Z","Clojure framework for voice-enabled AI"),
("bmorphism","bmorphism/lumon-tui","Python",1,0,0,"2025-02-02T11:24:21Z","Terminal parallel worlds a la Lumon"),
("bmorphism","bmorphism/goose-diagrams","",0,0,0,"2025-01-31T08:46:44Z","ASCII art diagrams for Goose AI"),
("bmorphism","bmorphism/MetaLab","",0,0,0,"2025-01-30T11:40:33Z","Space for cutting-edge tech experiments"),
("bmorphism","bmorphism/penrose-mcp","JavaScript",10,4,0,"2025-01-20T21:44:55Z","Penrose server for Infinity-Topos"),
("bmorphism","bmorphism/penrose-mcp-server","",0,0,0,"2025-01-20T20:24:07Z","MCP server for Penrose system"),
("bmorphism","bmorphism/test-repo-3141592","",0,0,1,"2025-01-11T15:06:57Z","Test repository for tool exploration"),
("bmorphism","bmorphism/manifold-mcp-server","JavaScript",14,9,5,"2025-01-11T10:36:58Z","MCP server for Manifold Markets"),
("bmorphism","bmorphism/say-mcp-server","JavaScript",20,9,3,"2025-01-07T03:15:18Z","MCP server for macOS text-to-speech"),
("bmorphism","bmorphism/penumbra-mcp","JavaScript",5,6,3,"2025-01-07T01:15:23Z","MCP server for Penumbra blockchain"),
("bmorphism","bmorphism/nats-mcp-server","",7,3,2,"2025-01-06T23:33:41Z","MCP server for NATS messaging"),
("bmorphism","bmorphism/marginalia-mcp-server","JavaScript",8,6,0,"2025-01-06T05:47:24Z","MCP server for managing marginalia"),
("bmorphism","bmorphism/babashka-mcp-server","JavaScript",19,6,3,"2025-01-05T11:09:42Z","MCP server for Babashka"),
("bmorphism","bmorphism/openbci-mcp-server","",0,0,0,"2025-01-05T07:00:10Z","MCP server for OpenBCI hardware"),
("bmorphism","bmorphism/gists-mcp-server","JavaScript",2,0,0,"2025-01-03T03:50:54Z","MCP server for GitHub Gists"),
("bmorphism","bmorphism/neural-category-diagrams","",0,0,0,"2025-01-02T05:47:22Z","Neural architectures through category theory"),
("bmorphism","bmorphism/slowtime-mcp-server","TypeScript",3,5,6,"2025-01-02T01:23:33Z","MCP server for secure time-based operations"),
("bmorphism","bmorphism/open-games-agda","Agda",0,0,0,"2024-12-22T11:16:29Z","Formalization of open games in Agda"),
("bmorphism","bmorphism/yoyo","Just",0,0,0,"2024-11-30T04:00:12Z",""),
("bmorphism","bmorphism/uss-cogsexy","",0,0,0,"2024-11-23T20:52:30Z","Cognitive Firewall"),
("bmorphism","bmorphism/vibes","Clojure",0,0,0,"2024-11-13T15:56:28Z","Global Vibespace"),
("bmorphism","bmorphism/untime","Swift",1,0,0,"2024-09-06T23:39:08Z",""),
("bmorphism","bmorphism/cf","Handlebars",0,0,0,"2024-08-07T01:14:25Z","collective futures"),
("bmorphism","bmorphism/collective","",0,0,0,"2024-08-07T01:08:28Z",""),
("bmorphism","bmorphism/pretopos","TeX",0,0,0,"2024-07-27T12:34:14Z",""),
("bmorphism","bmorphism/c-house-town","TypeScript",1,0,0,"2024-07-25T21:13:04Z",""),
("bmorphism","bmorphism/galahack2024","TypeScript",2,0,0,"2024-03-21T15:48:19Z",""),
("bmorphism","bmorphism/crags","Python",1,0,0,"2024-01-14T04:21:45Z","RAGs categorically"),
("bmorphism","bmorphism/hacker-news-alert-chatgpt-slack","Rust",0,0,0,"2023-08-31T09:56:37Z","Monitor Hacker News with ChatGPT summary"),
("bmorphism","bmorphism/summarize-github-issues","Rust",0,0,0,"2023-08-31T09:44:28Z","Summarize GitHub issues via ChatGPT"),
("bmorphism","bmorphism/slackduck","Rust",0,0,0,"2023-08-31T09:24:05Z","Slack bot with ChatGPT backend"),
("bmorphism","bmorphism/telega","Rust",1,0,0,"2023-08-23T17:20:29Z","absurd wasm32-wasi flow"),
("bmorphism","bmorphism/io","Handlebars",0,0,0,"2023-08-20T07:15:36Z",""),
("bmorphism","bmorphism/mesocunt2001","Rust",0,0,0,"2023-08-19T07:49:43Z","Customized Telegram bot"),
("bmorphism","bmorphism/mesocunt","Rust",0,0,0,"2023-08-18T10:13:33Z","Customizable Discord bot"),
("bmorphism","bmorphism/meso","Jupyter Notebook",1,1,0,"2023-08-09T06:04:11Z","Scripts for Markov Kernels"),
("bmorphism","bmorphism/monaduck69","Svelte",0,0,1,"2023-07-19T12:43:12Z","SvelteKit template"),
("bmorphism","bmorphism/banana","Python",0,0,0,"2023-02-23T15:12:07Z",""),
("bmorphism","bmorphism/Plurigrid.jl","Julia",0,1,0,"2023-01-04T14:53:02Z",""),
("bmorphism","bmorphism/plurigrid-celo","TypeScript",1,1,0,"2022-12-09T10:07:25Z","Celo e-app for Albany Plurigrid"),
("bmorphism","bmorphism/risc0-cosmwasm-example","Rust",23,2,1,"2022-10-20T23:50:40Z","CosmWasm + zkVM RISC-V EFI template"),
("bmorphism","bmorphism/knxwledge","",0,1,1,"2022-10-02T02:23:31Z",""),
("bmorphism","bmorphism/OTC-0","JavaScript",3,0,0,"2022-06-07T22:18:08Z",""),
("bmorphism","bmorphism/matrix5","",0,0,0,"2022-05-25T06:01:57Z","glowing in public"),
("bmorphism","bmorphism/pluridrop","TypeScript",2,0,0,"2022-04-10T00:13:47Z","ETHPortland2022 hack"),
("bmorphism","bmorphism/kfsummit19","Python",0,0,0,"2019-10-28T16:40:46Z","Kubeflow pipelines on Anthos"),
("bmorphism","bmorphism/recommenders","Python",0,0,0,"2019-09-11T07:43:03Z",""),
# zubyul (49)
("zubyul","zubyul/voice-observatory","Python",0,0,0,"2026-04-24T05:56:17Z","Passive macOS TUI observing voice-download pathways"),
("zubyul","zubyul/ghostel-emacs-worlds","GLSL",0,0,0,"2026-04-24T00:20:56Z","Ghostty config + ghostel family"),
("zubyul","zubyul/nash-tui","Rust",0,0,0,"2026-04-13T07:45:16Z","NASH token TUI real-time candles"),
("zubyul","zubyul/nash-web","Rust",0,0,0,"2026-04-13T07:08:58Z","NASH token browser TUI via ratzilla WASM"),
("zubyul","zubyul/big-bad-plurigrid-quiz","Emacs Lisp",0,0,0,"2026-04-09T18:51:31Z","27 flashcards from bmorphism/plurigrid/zubyul"),
("zubyul","zubyul/Gay.jl","Julia",0,0,0,"2026-03-28T11:30:01Z","Wide-gamut color sampling with splittable determinism"),
("zubyul","zubyul/kinesis-kb360pro","Python",0,0,0,"2026-03-26T10:29:40Z","Claude Code skill for Kinesis Advantage360 Pro"),
("zubyul","zubyul/gay-world","Python",1,1,0,"2026-03-26T04:03:39Z","Goblin world builder"),
("zubyul","zubyul/from-possible-worlds","TeX",0,0,0,"2026-03-16T03:14:55Z",""),
("zubyul","zubyul/tilelang-kernels","Python",0,0,0,"2026-03-16T02:31:13Z","TileLang GPU kernels for SplitMix64 color generation"),
("zubyul","zubyul/fleet-bootstrap","Shell",0,0,0,"2026-02-23T08:19:58Z",""),
("zubyul","zubyul/gay-terminal-colors","Clojure",0,0,0,"2026-02-21T07:38:14Z","Gay.jl world_terminal_fingerprint"),
("zubyul","zubyul/basin","Rust",0,0,0,"2026-02-13T10:31:47Z",""),
("zubyul","zubyul/openbci-visualizer","Zig",0,0,0,"2026-02-04T11:17:41Z",""),
("zubyul","zubyul/plurigrid-site","Svelte",0,1,11,"2026-02-04T03:20:08Z","Plurigrid world site deployment"),
("zubyul","zubyul/repl","Python",0,0,0,"2026-02-04T01:08:15Z",""),
("zubyul","zubyul/instance-onboarding","Shell",0,0,0,"2026-02-02T11:44:07Z",""),
("zubyul","zubyul/vibesnipe","Move",0,0,1,"2026-01-30T22:36:03Z",""),
("zubyul","zubyul/zubyul.github.io","CSS",1,0,0,"2026-01-27T03:24:34Z",""),
("zubyul","zubyul/toad-warpify-extension","Python",0,0,0,"2026-01-17T07:48:40Z","Warpify extension for Toad"),
("zubyul","zubyul/thread-site","Haskell",0,0,0,"2025-12-23T23:53:27Z",""),
("zubyul","zubyul/GayMove","Move",0,0,0,"2025-12-18T09:40:08Z",""),
("zubyul","zubyul/gay-brain-world","Python",0,0,0,"2025-12-16T01:19:28Z","Gay.jl SPI colors for Moduleur Brain"),
("zubyul","zubyul/multiplayer","HTML",0,0,0,"2025-12-12T08:56:16Z",""),
("zubyul","zubyul/cat-world","TypeScript",0,0,0,"2025-12-12T08:47:14Z","Cat gaze tracker"),
("zubyul","zubyul/hue-world","JavaScript",0,0,0,"2025-12-12T08:32:59Z","Terminal Vibe Snipe puzzle game"),
("zubyul","zubyul/multiplayer-emacs","HTML",0,0,0,"2025-12-12T08:07:38Z","Multiplayer world Emacs split-pane"),
("zubyul","zubyul/vibe-snipe","Kotlin",0,0,0,"2025-12-12T03:46:26Z",""),
("zubyul","zubyul/chromatic-vrf","Kotlin",0,0,0,"2025-12-12T03:26:22Z","Chromatic VRF puzzle"),
("zubyul","zubyul/quantum-telephone","Jupyter Notebook",0,0,0,"2025-12-08T22:54:16Z","Quantum telephone world"),
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
("zubyul","zubyul/jonikas_lab_data_analysis_misc","Jupyter Notebook",2,0,0,"2023-08-16T20:24:40Z","various scripts for large genetic sequence data"),
("zubyul","zubyul/WGCNA","HTML",2,0,0,"2023-07-05T18:02:30Z","weighted gene correlation network analysis"),
("zubyul","zubyul/Dr_Niv_Qs","Jupyter Notebook",0,0,0,"2023-06-29T04:46:01Z","Dr. Niv Interview Questions"),
("zubyul","zubyul/reddit_scraper","Python",0,0,0,"2023-06-16T14:06:07Z",""),
("zubyul","zubyul/Python_Undergrad","Python",0,0,0,"2023-06-16T14:02:18Z",""),
("zubyul","zubyul/Nikolova_lab_data_analysis","R",2,0,0,"2023-06-16T13:56:58Z","undergraduate thesis cortical thickness"),
("zubyul","zubyul/lastfm_analysis_copy","Jupyter Notebook",1,0,0,"2023-06-15T22:20:35Z","lastfm data analysis"),
# migalkin (19)
("migalkin","migalkin/kgcourse2021","HTML",25,9,0,"2026-02-16T05:16:08Z","Knowledge Graphs course materials"),
("migalkin","migalkin/migalkin.github.io","JavaScript",0,0,0,"2025-05-20T23:58:08Z","Github Pages academic website"),
("migalkin","migalkin/NBFNet_mlx","Python",10,1,1,"2026-03-11T01:31:21Z","Neural Bellman-Ford networks in MLX"),
("migalkin","migalkin/StarE","Python",89,16,1,"2026-04-16T14:12:45Z","Message Passing for Hyper-Relational KGs"),
("migalkin","migalkin/rambo","Rust",3,0,1,"2023-02-28T16:37:22Z",""),
("migalkin","migalkin/ciss2_project","Jupyter Notebook",0,0,6,"2019-06-28T23:14:33Z",""),
("migalkin","migalkin/RWL","Python",8,1,0,"2026-05-28T20:19:20Z","Weisfeiler and Leman Go Relational"),
("migalkin","migalkin/NodePiece","Python",144,21,0,"2026-05-07T05:40:02Z","Compositional Representations for Large KGs"),
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
# DJedamski (6)
("DJedamski","DJedamski/kaggle_ncaa18","Jupyter Notebook",0,0,0,"2018-02-26T16:33:24Z","NCAA March Madness competition code"),
("DJedamski","DJedamski/Project_Euler","",0,0,0,"2015-09-05T17:13:32Z",""),
("DJedamski","DJedamski/EDA","R",0,0,0,"2014-11-09T17:00:39Z","Coursera Project"),
("DJedamski","DJedamski/Kaggle","",1,0,0,"2023-04-21T01:42:35Z",""),
("DJedamski","DJedamski/Getting-and-Cleaning-Data","R",1,0,0,"2023-04-21T01:42:34Z","Coursera Project"),
("DJedamski","DJedamski/School","R",1,1,0,"2023-04-21T01:42:33Z","Projects from grad school"),
# wasita (11)
("wasita","wasita/wasita.github.io","Svelte",1,0,8,"2026-06-01T04:15:14Z","personal website"),
("wasita","wasita/wm-cv","Svelte",0,0,0,"2026-05-13T05:29:08Z","Academic CV single page web app"),
("wasita","wasita/vocoder","JavaScript",0,0,0,"2026-05-06T05:14:03Z",""),
("wasita","wasita/ch3-lib","Typst",0,0,0,"2026-04-12T04:03:22Z",""),
("wasita","wasita/magic-garden","Python",2,1,1,"2026-04-22T21:16:43Z","bot for magic garden discord game"),
("wasita","wasita/proj-template","",0,0,0,"2026-01-09T20:55:46Z",""),
("wasita","wasita/food-diary","Svelte",0,0,0,"2025-12-13T01:06:43Z",""),
("wasita","wasita/send2kobo","TypeScript",1,0,0,"2026-05-19T02:59:26Z","Website for sending books to kobo"),
("wasita","wasita/d60-keeb","",0,0,0,"2024-08-26T00:46:25Z",""),
("wasita","wasita/wins-search","CSS",1,0,0,"2023-06-03T19:01:11Z","Women in Network Science member list"),
("wasita","wasita/honeycomb-demo","JavaScript",0,0,0,"2021-12-07T21:38:28Z",""),
# kristinezheng (5)
("kristinezheng","kristinezheng/kristinezheng.github.io","HTML",0,0,0,"2026-06-07T22:53:10Z",""),
("kristinezheng","kristinezheng/lookit-jenga","Jupyter Notebook",0,0,0,"2024-05-16T18:29:05Z","Lookit study"),
("kristinezheng","kristinezheng/auditory-illusion","CSS",0,0,0,"2022-03-07T02:57:44Z","auditory illusion"),
("kristinezheng","kristinezheng/graph_example","Python",0,0,0,"2021-10-08T07:29:53Z",""),
("kristinezheng","kristinezheng/Green-Machine","Python",0,0,0,"2021-09-19T05:33:04Z","HackMIT 2021 Sustainability Track"),
# M1shaaa (8)
("M1shaaa","M1shaaa/M1shaaa","",0,0,0,"2026-02-04T19:32:04Z","Config files for GitHub profile"),
("M1shaaa","M1shaaa/lab-bookshelf-","TypeScript",0,0,0,"2024-12-31T05:11:18Z",""),
("M1shaaa","M1shaaa/rosie-s-study-3-lookit-project","",0,0,0,"2024-11-04T22:15:39Z",""),
("M1shaaa","M1shaaa/Python-Lookit-Uploads","Python",0,0,0,"2024-02-15T22:59:37Z","random projects"),
("M1shaaa","M1shaaa/Classes","",0,0,0,"2023-12-06T18:20:27Z",""),
("M1shaaa","M1shaaa/Yale-Work","HTML",0,0,0,"2023-12-06T18:33:14Z",""),
("M1shaaa","M1shaaa/MNIST-Classifier","",0,0,0,"2023-11-28T06:10:47Z",""),
("M1shaaa","M1shaaa/Lookit-Demo","",0,0,0,"2023-04-10T02:44:01Z",""),
# AustinCStone (40)
("AustinCStone","AustinCStone/EpsteinSearch","Python",0,0,0,"2026-02-11T01:10:57Z",""),
("AustinCStone","AustinCStone/bmforkupdate","Python",0,0,0,"2025-05-09T04:50:16Z",""),
("AustinCStone","AustinCStone/bmfork","Python",0,0,1,"2025-05-09T04:18:54Z",""),
("AustinCStone","AustinCStone/bitmind-fork","",0,0,0,"2025-01-09T06:16:51Z","forked on jan 8 2025"),
("AustinCStone","AustinCStone/testLogin","Python",0,0,0,"2023-02-13T20:52:27Z",""),
("AustinCStone","AustinCStone/austincstone.github.io","HTML",0,0,0,"2021-10-23T22:48:49Z",""),
("AustinCStone","AustinCStone/test","",0,0,0,"2021-09-21T21:15:50Z",""),
("AustinCStone","AustinCStone/stonks","Python",0,0,0,"2020-09-04T22:54:35Z","Playing around with option calculations"),
("AustinCStone","AustinCStone/Z-order-curve","Python",0,0,0,"2019-06-09T02:53:43Z","Space filling z-order curve demo"),
("AustinCStone","AustinCStone/LensBuilder","Python",0,0,0,"2019-04-04T04:28:08Z","Optimize surface of a focusing lens"),
("AustinCStone","AustinCStone/TFBirds","Python",0,0,0,"2019-01-30T08:07:22Z","Bird flocking simulator in TensorFlow"),
("AustinCStone","AustinCStone/StructureFromMotion","Python",1,0,0,"2019-04-26T19:43:12Z","Recover 3D geometry from videos"),
("AustinCStone","AustinCStone/OptimalControl","Python",0,0,0,"2018-02-03T08:08:51Z","Concepts from control theory"),
("AustinCStone","AustinCStone/LearningCuda","C",0,0,0,"2017-11-05T20:31:07Z","CUDA by example"),
("AustinCStone","AustinCStone/TextGAN","Python",92,30,5,"2025-03-03T13:26:32Z","Generative adversarial network for text"),
("AustinCStone","AustinCStone/StereoVisionMRF","Python",11,4,0,"2026-04-01T07:39:41Z","MRF for depth from stereo images"),
("AustinCStone","AustinCStone/SpectralClustering","Python",3,2,0,"2021-04-16T08:46:36Z","Spectral clustering implementation"),
("AustinCStone","AustinCStone/statsHw2","Python",0,0,0,"2015-09-28T00:50:31Z","Linear regression and model selection"),
("AustinCStone","AustinCStone/StatsModelingHw1","Python",0,0,0,"2015-09-19T04:13:53Z","Statistical modeling homework"),
("AustinCStone","AustinCStone/ConvNet","Python",0,0,0,"2015-09-07T22:25:29Z","CNN for MNIST"),
("AustinCStone","AustinCStone/TheanoStuff","Python",0,0,0,"2021-09-04T03:21:57Z","Theano experiments"),
("AustinCStone","AustinCStone/bash_profile","",0,0,0,"2015-08-26T17:59:33Z","bash profile"),
("AustinCStone","AustinCStone/Founderati-Server","Python",0,1,0,"2015-08-25T19:17:45Z","Server for Founderati"),
("AustinCStone","AustinCStone/Founderati-client","JavaScript",0,1,0,"2015-08-25T19:16:58Z","AngelList/LinkedIn alternative"),
("AustinCStone","AustinCStone/logisticRegressionHaskell","Haskell",1,0,0,"2018-02-02T13:34:28Z","Logistic regression in Haskell"),
("AustinCStone","AustinCStone/Genetic-Algorithm-Sorting-Network","Python",0,0,0,"2015-05-09T03:20:27Z","Genetic Algorithm Sorting Network"),
("AustinCStone","AustinCStone/RealTimeRayTracingFractalWorld","C++",0,0,0,"2015-05-11T01:58:57Z","Real time ray tracing fractal world"),
("AustinCStone","AustinCStone/gibbs_sampling","Python",0,0,0,"2023-07-23T17:30:23Z","Gibbs sampling and ancestral rejection"),
("AustinCStone","AustinCStone/lexer","C",0,0,0,"2015-02-09T22:45:55Z","Lexer for prolog"),
("AustinCStone","AustinCStone/HTTPCache","Java",0,0,0,"2015-02-05T22:04:01Z","HTTP response caching"),
("AustinCStone","AustinCStone/DigitRecognition","Matlab",0,0,0,"2015-02-02T04:35:23Z","Classify handwritten digits"),
("AustinCStone","AustinCStone/stuffForAlec","JavaScript",0,0,0,"2015-01-05T01:34:25Z",""),
("AustinCStone","AustinCStone/FlaskBlog","Python",0,0,0,"2014-12-17T23:45:46Z","Simple blog with Flask"),
("AustinCStone","AustinCStone/PrologParserAndEvaluator","",0,0,0,"2014-10-10T01:17:52Z","Parser and evaluator in prolog"),
("AustinCStone","AustinCStone/QuantumSearchAlgorithmSimulation","Java",0,0,0,"2014-11-07T02:09:38Z","Grover's algorithm simulation"),
("AustinCStone","AustinCStone/SleepDetectionMoto360","Java",0,0,0,"2014-10-19T03:21:34Z","Sleep detection app for Moto 360"),
("AustinCStone","AustinCStone/Connectomics","TeX",0,0,0,"2014-05-22T19:27:53Z","Kaggle Connectomics Challenge MCMC"),
("AustinCStone","AustinCStone/Eigenface-Recognition","Matlab",0,0,0,"2014-05-22T19:32:41Z",""),
("AustinCStone","AustinCStone/Royal-Road-With-Ditches-Genetic-Algorithm","Python",0,0,0,"2014-05-11T02:27:49Z","Royal Road genetic algorithm"),
("AustinCStone","AustinCStone/Netflix_Prize_Challenge","M",0,0,0,"2014-05-11T02:22:57Z","Predict movie ratings"),
]

print(f"Inserting {len(repos)} repos into DuckDB...")
inc_id = 1
repo_id = 1
for (org_or_user, full_name, language, stars, forks, open_issues, pushed_at, description) in repos:
    trit, color, name = gf3(inc_id)
    snap_hash = hashlib.md5(f"{full_name}{pushed_at}".encode()).hexdigest()[:16]
    repo_name = full_name.split("/")[1]
    con.execute("""
        INSERT INTO world_increments VALUES (?, now(), ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [inc_id, trit, color, name, "github", org_or_user, "repo_snapshot", repo_name, org_or_user, snap_hash])
    con.execute("""
        INSERT INTO repo_snapshots VALUES (?, now(), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [repo_id, inc_id, org_or_user, repo_name, full_name, language or "", stars, forks, open_issues, pushed_at, description or ""])
    inc_id += 1
    repo_id += 1

print(f"GitHub repos inserted. Next increment id: {inc_id}")

# ── Aptos wallet balances ─────────────────────────────────────────────────────

APTOS_BASE = "https://fullnode.mainnet.aptoslabs.com/v1"
COIN_RESOURCE = "0x1::coin::CoinStore%3C0x1::aptos_coin::AptosCoin%3E"

aptos_addresses = [
    ("alice", "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b"),
    ("bob",   "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d"),
    ("A", "0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a"),
    ("B", "0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13"),
    ("C", "0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e"),
    ("D", "0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1"),
    ("E", "0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36"),
    ("F", "0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71"),
    ("G", "0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32"),
    ("H", "0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f"),
    ("I", "0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9"),
    ("J", "0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54"),
    ("K", "0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4"),
    ("L", "0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9"),
    ("M", "0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9"),
    ("N", "0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c"),
    ("O", "0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d"),
    ("P", "0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948"),
    ("Q", "0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9"),
    ("R", "0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10"),
    ("S", "0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386"),
    ("T", "0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588"),
    ("U", "0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956"),
    ("V", "0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3"),
    ("W", "0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0"),
    ("X", "0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d"),
    ("Y", "0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4"),
    ("Z", "0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c"),
]

aptos_results = []
print("Querying Aptos balances...")
for world, addr in aptos_addresses:
    url = f"{APTOS_BASE}/accounts/{addr}/resource/{COIN_RESOURCE}"
    try:
        result = subprocess.run(
            ["curl", "-s", "--max-time", "10", url],
            capture_output=True, text=True
        )
        data = json.loads(result.stdout)
        raw = data.get("data", {}).get("coin", {}).get("value", None)
        if raw is not None:
            balance = int(raw) / 100_000_000
        else:
            balance = None
    except Exception as e:
        balance = None
    aptos_results.append((world, addr, balance))
    status = f"{balance:.8f} APT" if balance is not None else "N/A (no account)"
    print(f"  {world}: {status}")
    time.sleep(1)

for world, addr, balance in aptos_results:
    b = balance if balance is not None else 0.0
    con.execute("INSERT INTO aptos_snapshots VALUES (now(), ?, ?, ?)", [world, addr, b])

print(f"Aptos balances inserted: {len(aptos_results)} addresses")

# ── Multisig probes ────────────────────────────────────────────────────────────

MULTISIG_VIEW_URL = "https://fullnode.mainnet.aptoslabs.com/v1/view"

multisig_addrs = [
    ("A-B", "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003"),
    ("A-G", "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096"),
    ("Y-Z", "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883"),
    ("S-T", "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883"),
    ("V-W", "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d"),
]

multisig_results = []
print("Probing multisig contracts...")
for pair, addr in multisig_addrs:
    payload = json.dumps({
        "function": "0x1::multisig_account::num_signatures_required",
        "type_arguments": [],
        "arguments": [addr]
    })
    try:
        result = subprocess.run(
            ["curl", "-s", "--max-time", "10", "-X", "POST",
             "-H", "Content-Type: application/json",
             "-d", payload, MULTISIG_VIEW_URL],
            capture_output=True, text=True
        )
        data = json.loads(result.stdout)
        if isinstance(data, list) and len(data) > 0:
            sigs = int(data[0])
            healthy = True
        else:
            sigs = -1
            healthy = False
    except Exception as e:
        sigs = -1
        healthy = False
    multisig_results.append((pair, addr, sigs, healthy))
    print(f"  {pair} ({addr[:16]}...): sigs_required={sigs}, healthy={healthy}")
    time.sleep(1)

for pair, addr, sigs, healthy in multisig_results:
    con.execute("INSERT INTO multisig_probes VALUES (now(), ?, ?, ?, ?)", [pair, addr, sigs, healthy])

print(f"Multisig probes inserted: {len(multisig_results)}")

# ── MNX Markets ───────────────────────────────────────────────────────────────

mnx_results = []
print("Fetching MNX Markets...")
mnx_urls_to_try = [
    "https://testnet.mnx.fi/api/markets",
    "https://testnet.mnx.fi/api/tickers",
    "https://testnet.mnx.fi/api/v1/markets",
    "https://testnet.mnx.fi/api/v1/tickers",
]

mnx_raw = None
for url in mnx_urls_to_try:
    try:
        result = subprocess.run(
            ["curl", "-s", "--max-time", "10", "-L", url],
            capture_output=True, text=True
        )
        if result.stdout and len(result.stdout) > 10:
            try:
                parsed = json.loads(result.stdout)
                mnx_raw = parsed
                print(f"  Got data from {url}")
                break
            except:
                pass
    except:
        pass

if mnx_raw is None:
    print("  MNX testnet API unavailable — noting as unavailable")
    con.execute("INSERT INTO mnx_snapshots VALUES (now(), 'N/A', 'MNX testnet unavailable', 'unavailable', 0.0, 0.0)")
else:
    if isinstance(mnx_raw, list):
        for item in mnx_raw[:20]:
            ticker = item.get("ticker", item.get("symbol", ""))
            name = item.get("name", "")
            category = item.get("category", item.get("type", ""))
            price = float(item.get("price", item.get("last", 0.0)) or 0.0)
            change = float(item.get("change_pct", item.get("change24h", 0.0)) or 0.0)
            mnx_results.append((ticker, name, category, price, change))
    elif isinstance(mnx_raw, dict):
        for k, v in list(mnx_raw.items())[:20]:
            if isinstance(v, dict):
                ticker = v.get("ticker", k)
                name = v.get("name", k)
                category = v.get("category", "")
                price = float(v.get("price", 0.0) or 0.0)
                change = float(v.get("change_pct", 0.0) or 0.0)
                mnx_results.append((ticker, name, category, price, change))
    for ticker, name, category, price, change in mnx_results:
        con.execute("INSERT INTO mnx_snapshots VALUES (now(), ?, ?, ?, ?, ?)", [ticker, name, category, price, change])

print(f"MNX data: {len(mnx_results)} entries")

# ── Verify counts ─────────────────────────────────────────────────────────────

counts = con.execute("""
    SELECT
        (SELECT COUNT(*) FROM world_increments) as increments,
        (SELECT COUNT(*) FROM repo_snapshots) as repos,
        (SELECT COUNT(*) FROM aptos_snapshots) as aptos,
        (SELECT COUNT(*) FROM multisig_probes) as multisigs,
        (SELECT COUNT(*) FROM mnx_snapshots) as mnx
""").fetchone()

print(f"\nDuckDB counts: increments={counts[0]}, repos={counts[1]}, aptos={counts[2]}, multisigs={counts[3]}, mnx={counts[4]}")

# ── Generate LATEST_SWEEP.md ──────────────────────────────────────────────────

now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

top_repos = con.execute("""
    SELECT full_name, language, stars, forks, pushed_at
    FROM repo_snapshots
    ORDER BY stars DESC
    LIMIT 15
""").fetchall()

repo_counts = con.execute("""
    SELECT org_or_user, COUNT(*) as cnt
    FROM repo_snapshots
    GROUP BY org_or_user
    ORDER BY cnt DESC
""").fetchall()

aptos_rows = con.execute("""
    SELECT world, address, balance_apt
    FROM aptos_snapshots
    ORDER BY world
""").fetchall()

multisig_rows = con.execute("""
    SELECT pair, address, sigs_required, healthy
    FROM multisig_probes
    ORDER BY pair
""").fetchall()

gf3_dist = con.execute("""
    SELECT gf3_name, gf3_color, COUNT(*) as cnt
    FROM world_increments
    GROUP BY gf3_name, gf3_color
    ORDER BY gf3_name
""").fetchall()

md_lines = [
    f"# World-Increment Sweep + Hamming Swarm Snapshot",
    f"",
    f"**Generated:** {now_str}",
    f"**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`",
    f"",
    f"---",
    f"",
    f"## JOB 1: GitHub Social Graph Sweep",
    f"",
    f"### Sources Swept",
    f"| Source | Type | Repos |",
    f"|--------|------|-------|",
]
for src, cnt in repo_counts:
    src_type = "org" if src in ["plurigrid", "kubeflow", "TeglonLabs"] else "user"
    md_lines.append(f"| {src} | {src_type} | {cnt} |")

md_lines += [
    f"",
    f"**Total repos snapshotted:** {counts[1]}",
    f"",
    f"### GF(3) Color Chain Distribution",
    f"| Trit | Color | Name | Count |",
    f"|------|-------|------|-------|",
]
for gname, gcolor, gcnt in gf3_dist:
    trit = {"ERGODIC": 0, "PLUS": 1, "MINUS": -1}[gname]
    md_lines.append(f"| {trit} | `{gcolor}` | {gname} | {gcnt} |")

md_lines += [
    f"",
    f"### Top 15 Repos by Stars",
    f"| Repo | Language | Stars | Forks | Last Push |",
    f"|------|----------|-------|-------|-----------|",
]
for full_name, lang, stars, forks, pushed in top_repos:
    md_lines.append(f"| {full_name} | {lang or '-'} | {stars} | {forks} | {pushed[:10]} |")

md_lines += [
    f"",
    f"---",
    f"",
    f"## JOB 2: Hamming Swarm Snapshot",
    f"",
    f"### Aptos Wallet Balances",
    f"| World | Address | Balance (APT) |",
    f"|-------|---------|---------------|",
]
total_apt = 0.0
for world, addr, bal in aptos_rows:
    total_apt += bal
    bal_str = f"{bal:.8f}" if bal > 0 else "0 (no account)"
    short_addr = addr[:12] + "..." + addr[-8:]
    md_lines.append(f"| {world} | `{short_addr}` | {bal_str} |")

md_lines += [
    f"",
    f"**Total APT across all wallets:** {total_apt:.8f} APT",
    f"",
    f"### Multisig Contract Probes",
    f"| Pair | Address | Sigs Required | Healthy |",
    f"|------|---------|---------------|---------|",
]
for pair, addr, sigs, healthy in multisig_rows:
    short_addr = addr[:12] + "..." + addr[-8:]
    health_str = "✓" if healthy else "✗"
    sigs_str = str(sigs) if sigs >= 0 else "N/A"
    md_lines.append(f"| {pair} | `{short_addr}` | {sigs_str} | {health_str} |")

md_lines += [
    f"",
    f"### MNX Markets",
]
if len(mnx_results) == 0:
    md_lines.append(f"MNX testnet (`testnet.mnx.fi`) API is unavailable — SPA returned no parseable market data.")
else:
    md_lines += [
        f"| Ticker | Name | Category | Price | Change % |",
        f"|--------|------|----------|-------|----------|",
    ]
    for ticker, name, category, price, change in mnx_results:
        md_lines.append(f"| {ticker} | {name} | {category} | {price} | {change} |")

md_lines += [
    f"",
    f"---",
    f"",
    f"## DuckDB Summary",
    f"",
    f"| Table | Rows |",
    f"|-------|------|",
    f"| world_increments | {counts[0]} |",
    f"| repo_snapshots | {counts[1]} |",
    f"| aptos_snapshots | {counts[2]} |",
    f"| multisig_probes | {counts[3]} |",
    f"| mnx_snapshots | {counts[4]} |",
    f"",
]

md_content = "\n".join(md_lines)
md_path = "/home/user/gorj/packages/world-increment/ducklake/LATEST_SWEEP.md"
with open(md_path, "w") as f:
    f.write(md_content)

print(f"\nWrote {md_path}")
con.close()
print("Done.")
