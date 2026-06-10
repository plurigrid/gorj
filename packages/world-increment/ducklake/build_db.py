#!/usr/bin/env python3
"""Build world-increments DuckDB from collected sweep data."""
import subprocess
import sys
import hashlib
import json
from datetime import datetime

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"

def run_sql(sql):
    r = subprocess.run(
        ["duckdb", DB, "-c", sql],
        capture_output=True, text=True
    )
    if r.returncode != 0:
        print(f"SQL ERROR: {r.stderr}\nSQL: {sql[:200]}", file=sys.stderr)
    return r.stdout

def run_sql_file(path):
    r = subprocess.run(
        ["duckdb", DB, "-f", path],
        capture_output=True, text=True
    )
    if r.returncode != 0:
        print(f"SQL FILE ERROR: {r.stderr}", file=sys.stderr)
    return r.stdout

# DDL
DDL = """
CREATE TABLE IF NOT EXISTS world_increments (
  id INTEGER,
  timestamp TIMESTAMP DEFAULT now(),
  gf3_trit INTEGER,
  gf3_color VARCHAR,
  gf3_name VARCHAR,
  source_type VARCHAR,
  source_name VARCHAR,
  event_type VARCHAR,
  repo_name VARCHAR,
  actor VARCHAR,
  snapshot_hash VARCHAR
);
CREATE TABLE IF NOT EXISTS repo_snapshots (
  id INTEGER,
  timestamp TIMESTAMP DEFAULT now(),
  increment_id INTEGER,
  org_or_user VARCHAR,
  repo_name VARCHAR,
  full_name VARCHAR,
  language VARCHAR,
  stars INTEGER,
  forks INTEGER,
  open_issues INTEGER,
  pushed_at VARCHAR,
  description VARCHAR
);
CREATE SEQUENCE IF NOT EXISTS increment_seq START 1;
CREATE SEQUENCE IF NOT EXISTS repo_seq START 1;
CREATE TABLE IF NOT EXISTS aptos_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  world VARCHAR,
  address VARCHAR,
  balance_apt DOUBLE
);
CREATE TABLE IF NOT EXISTS multisig_probes (
  timestamp TIMESTAMP DEFAULT now(),
  pair VARCHAR,
  address VARCHAR,
  sigs_required INTEGER,
  healthy BOOLEAN
);
CREATE TABLE IF NOT EXISTS mnx_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  ticker VARCHAR,
  name VARCHAR,
  category VARCHAR,
  price DOUBLE,
  change_pct DOUBLE
);
"""

print("Creating tables...")
run_sql(DDL)

# GF3 color chain
def gf3(n):
    t = n % 3
    if t == 0:
        return (0, "#d3869b", "ERGODIC")
    elif t == 1:
        return (1, "#b8bb26", "PLUS")
    else:
        return (-1, "#cc241d", "MINUS")

# All repos collected
repos = []

# plurigrid (100 repos)
plurigrid_repos = [
    ("plurigrid/asi","HTML",25,7,4,"2026-06-10T12:51:42Z","everything is topological chemputer!"),
    ("plurigrid/place","TeX",1,2,8,"2026-06-10T16:25:05Z",""),
    ("plurigrid/eirobri","Clojure",0,0,29,"2026-06-03T20:43:46Z","EiRoBri replay world"),
    ("plurigrid/nash-portal","Rust",2,3,1,"2026-05-19T01:49:59Z","NASH token TUI in the browser"),
    ("plurigrid/gorj","Clojure",0,0,485,"2026-06-10T20:15:23Z","forj + Rama topology nREPL routing + GF(3) gay trit coloring"),
    ("plurigrid/zig-syrup","Zig",2,2,0,"2026-04-30T03:52:16Z","High-performance Zig implementation of OCapN Syrup"),
    ("plurigrid/asi-skills","Julia",3,1,0,"2026-04-26T08:09:26Z","69 skills with Galois Hole Type accessibility"),
    ("plurigrid/bci-blue-share","JavaScript",0,0,0,"2026-04-26T07:08:03Z","BCI signal infrastructure"),
    ("plurigrid/nanoclj-zig","Zig",1,2,20,"2026-04-25T07:29:09Z","NaN-boxed Clojure interpreter in Zig 0.15"),
    ("plurigrid/spi-race","Swift",0,0,0,"2026-04-21T19:31:56Z","Splitmix Parallel Integrity"),
    ("plurigrid/reafference","HTML",0,0,0,"2026-04-16T05:21:49Z","Reafference adaptation workspace"),
    ("plurigrid/web-browser","Rust",0,0,0,"2026-04-10T02:54:47Z","web-browser from prepostweb lineage"),
    ("plurigrid/vivarium","Clojure",1,0,0,"2026-04-08T08:38:37Z",""),
    ("plurigrid/flowglad-rs","Rust",0,0,0,"2026-04-08T07:56:15Z",""),
    ("plurigrid/tree-sitter-nanoclj-zig","C",0,0,0,"2026-04-04T07:48:21Z","Tree-sitter grammar for nanoclj-zig"),
    ("plurigrid/forester","XSLT",0,0,0,"2026-03-30T01:32:26Z","CatColab mathematical documentation forest"),
    ("plurigrid/gatomic","Clojure",0,0,0,"2026-03-30T00:54:48Z","Deterministic color identity store with sonification"),
    ("plurigrid/blue","TeX",0,0,0,"2026-03-29T23:06:32Z",""),
    ("plurigrid/red","",0,0,0,"2026-03-29T22:58:46Z",""),
    ("plurigrid/nblm-flashcards","Hy",0,0,0,"2026-03-26T08:23:01Z","NotebookLM Enterprise flashcard pipeline"),
    ("plurigrid/gemini-agent","Python",0,0,0,"2026-02-19T06:39:16Z",""),
    ("plurigrid/graded-optic","Haskell",0,0,0,"2026-02-08T16:10:16Z","Semiring-graded bidirectional processes"),
    ("plurigrid/json-canvas","",0,0,0,"2026-02-06T06:50:57Z","JSON Canvas: Real-time interaction data capture"),
    ("plurigrid/shepherd","Scheme",0,0,0,"2026-01-23T07:47:28Z","Spritely Shepherd - Service manager"),
    ("plurigrid/goblinshare","Scheme",0,0,0,"2026-01-23T07:47:12Z","P2P filesharing demo for Goblins"),
    ("plurigrid/magenc","Scheme",0,0,0,"2026-01-23T07:47:11Z","Magenc Magnet URIs"),
    ("plurigrid/hoot","Scheme",0,0,1,"2026-01-23T07:47:10Z","Spritely Hoot - Scheme to WebAssembly compiler"),
    ("plurigrid/leprechauns","Racket",0,0,0,"2026-01-23T07:46:46Z","Spritely Goblins + Gay.jl semantic colors"),
    ("plurigrid/spritely-semantic-colors","",0,0,0,"2026-01-23T07:38:32Z","Deterministic color mappings for Spritely/Goblins objects"),
    ("plurigrid/gay-tofu","HTML",0,0,0,"2026-01-08T15:14:34Z","Low-discrepancy color sequences for visual TOFU authentication"),
    ("plurigrid/lazygay","Go",0,0,0,"2026-01-08T14:19:25Z","lazygit fork with Gay.jl deterministic commit coloring"),
    ("plurigrid/gay-terminal","Rust",0,0,0,"2026-01-08T14:19:24Z","Terminal ANSI coloring with Gay.jl low-discrepancy sequences"),
    ("plurigrid/gay-go","Go",0,0,0,"2026-01-08T14:19:23Z","Go implementation of Gay.jl deterministic coloring"),
    ("plurigrid/gay-rs","Rust",0,0,0,"2026-01-08T14:19:22Z","Rust crate for Gay.jl deterministic coloring with GF(3) trits"),
    ("plurigrid/lazybjj","Rust",0,0,0,"2026-01-08T14:19:19Z","TUI for jj with Gay.jl GF(3) coloring"),
    ("plurigrid/agent-o-rama","Clojure",0,0,0,"2026-01-02T01:09:22Z",""),
    ("plurigrid/aptos-wallet-ruby","Ruby",1,0,0,"2025-09-30T22:47:22Z",""),
    ("plurigrid/duck-kanban","Rust",1,0,0,"2025-09-26T20:18:38Z","Duck intelligence kanban system"),
    ("plurigrid/shiteshiteshite","",0,0,0,"2025-09-26T03:07:20Z","Duck intelligence kanban system"),
    ("plurigrid/discohy","Hy",0,0,0,"2025-09-10T02:01:31Z",""),
    ("plurigrid/telemind","",0,0,0,"2025-06-12T05:54:59Z",""),
    ("plurigrid/ontology","JavaScript",8,9,16,"2025-05-27T18:18:34Z","autopoietic ergodicity and embodied gradualism"),
    ("plurigrid/Plurigraph","JavaScript",3,5,4,"2025-01-05T08:39:09Z","Plurigrid knowledge base for use with Obsidian.md"),
    ("plurigrid/signe","Python",0,0,0,"2024-08-15T20:52:03Z","Signal messages data traversal"),
    ("plurigrid/SwiftDuck","",0,0,0,"2024-08-08T18:19:06Z",""),
    ("plurigrid/act","Python",3,1,4,"2024-07-26T08:27:08Z","building blocks for cognitive category theory"),
    ("plurigrid/xenomorphic","",0,0,0,"2024-04-09T03:24:55Z",""),
    ("plurigrid/metamorphic","",0,0,0,"2024-04-09T03:22:41Z",""),
    ("plurigrid/DiffusionVoiceDemo","Clojure",0,0,0,"2024-04-02T18:09:01Z",""),
    ("plurigrid/website","Clojure",0,1,0,"2024-03-30T04:37:51Z",""),
    ("plurigrid/StochFlow","Python",4,1,0,"2024-03-20T23:34:57Z","Python library for stochastic interpolant models"),
    ("plurigrid/intent","",0,0,0,"2024-03-04T04:53:38Z","Simulations for An Analysis of Intent Markets"),
    ("plurigrid/novella","TypeScript",1,0,0,"2024-01-27T08:12:55Z",""),
    ("plurigrid/ACT.jl","Julia",0,0,0,"2024-01-21T00:02:25Z","applied categorical duck cybernetics"),
    ("plurigrid/ducklings","TypeScript",0,0,15,"2023-12-25T07:34:27Z",""),
    ("plurigrid/paretae","TypeScript",0,0,14,"2023-11-20T05:14:42Z",""),
    ("plurigrid/experiments","",0,0,0,"2023-11-17T05:39:07Z","Learning from computational experiments"),
    ("plurigrid/fuckit","Clojure",0,0,0,"2023-11-14T21:26:14Z",""),
    ("plurigrid/omega","Clojure",0,0,0,"2023-11-07T21:08:46Z",""),
    ("plurigrid/org","Jupyter Notebook",2,0,1,"2023-11-07T01:08:05Z","Dynamically Replicating Duck"),
    ("plurigrid/CVAE-Flows","",0,0,0,"2023-10-24T14:41:32Z","Leveraging dihypergraphs for conversation context"),
    ("plurigrid/morph-prover-cli","",0,1,0,"2023-10-18T03:49:03Z","Lean4"),
    ("plurigrid/uncharacter","TypeScript",0,0,0,"2023-09-19T20:17:46Z",""),
    ("plurigrid/chateau","TypeScript",0,0,0,"2023-08-30T20:11:12Z",""),
    ("plurigrid/gmgm","",0,0,1,"2023-08-25T13:54:00Z",""),
    ("plurigrid/tuttle","TypeScript",0,0,0,"2023-08-09T17:40:44Z",""),
    ("plurigrid/mesoplay","",0,0,0,"2023-08-09T06:19:03Z",""),
    ("plurigrid/am","Python",0,0,0,"2023-08-05T12:46:33Z",""),
    ("plurigrid/compose","",0,0,2,"2023-07-24T06:18:48Z",""),
    ("plurigrid/flussi","",0,0,1,"2023-07-15T06:40:11Z",""),
    ("plurigrid/cf","",0,0,0,"2023-07-11T08:11:29Z",""),
    ("plurigrid/poepoe","",0,0,1,"2023-07-09T22:20:50Z",""),
    ("plurigrid/marketplace","",0,0,1,"2023-07-09T05:52:30Z",""),
    ("plurigrid/smoller","",0,0,1,"2023-07-06T07:38:04Z",""),
    ("plurigrid/liquidity","",0,0,1,"2023-07-06T02:07:28Z",""),
    ("plurigrid/solid-rs","",0,0,1,"2023-07-05T21:58:05Z",""),
    ("plurigrid/solid","Python",0,0,0,"2023-07-05T21:52:25Z",""),
    ("plurigrid/ipegrafo","Python",0,0,0,"2023-07-03T07:29:40Z",""),
    ("plurigrid/plurigrid-v4","TypeScript",0,0,0,"2023-07-03T06:31:59Z",""),
    ("plurigrid/novella-v3","",0,0,0,"2023-07-03T06:29:40Z",""),
    ("plurigrid/polyglottal","TypeScript",0,0,0,"2023-07-03T06:23:45Z",""),
    ("plurigrid/novella-v2","",0,0,0,"2023-07-03T06:22:38Z",""),
    ("plurigrid/cocreation-ui","",0,0,2,"2023-07-03T04:45:53Z",""),
    ("plurigrid/smol","",0,0,1,"2023-07-02T08:45:32Z",""),
    ("plurigrid/commons","TypeScript",0,0,0,"2023-06-27T05:46:24Z",""),
    ("plurigrid/post-web","Svelte",0,0,0,"2023-06-18T00:24:24Z",""),
    ("plurigrid/microworlds","Rust",3,5,3,"2023-05-13T03:54:56Z","👽"),
    ("plurigrid/pills","",0,0,0,"2023-05-02T10:03:03Z","metaphors for embodied gradualism"),
    ("plurigrid/plurigrid-rs","Rust",0,0,0,"2023-04-21T01:02:56Z",""),
    ("plurigrid/plurigrid-game.github.io","HTML",0,0,1,"2023-04-20T00:17:55Z",""),
    ("plurigrid/synth","Rust",0,0,0,"2023-04-15T01:56:45Z",""),
    ("plurigrid/birbs","C++",0,0,0,"2023-04-15T01:56:32Z","Build native CosmWasm apps"),
    ("plurigrid/agent","Python",5,1,6,"2023-03-31T18:45:23Z","Framework for agency amplification"),
    ("plurigrid/vcg-auction","Rust",7,2,1,"2023-03-16T21:53:08Z","a simple contract that performs a VCG auction"),
    ("plurigrid/bidder","Dart",0,0,1,"2023-03-15T15:23:22Z","simple flutter app for vcg auction bidding"),
    ("plurigrid/plurigrid.github.io","HTML",1,2,2,"2023-01-20T03:27:34Z",""),
    ("plurigrid/VPP","Julia",0,1,0,"2023-01-11T18:41:07Z","Hyperreal Power Plant"),
    ("plurigrid/grid","TypeScript",2,1,1,"2023-01-02T11:55:55Z","Plurigrid Testnet #0: Edith Clarke"),
    ("plurigrid/commons-contracts","Rust",0,0,0,"2022-09-09T09:20:11Z","CosmWasm contracts for Commons Stack"),
    ("plurigrid/plurigrid.xyz","TypeScript",0,0,1,"2022-08-31T05:26:14Z",""),
]
for r in plurigrid_repos:
    repos.append(("org", "plurigrid") + r)

# kubeflow repos
kubeflow_repos = [
    ("kubeflow/mlflow-integration","Python",6,4,2,"2026-06-10T21:26:34Z",""),
    ("kubeflow/mcp-apache-spark-history-server","Python",174,64,21,"2026-06-10T18:49:04Z","MCP Server and CLI for Apache Spark History Server"),
    ("kubeflow/pipelines","Python",4153,2004,495,"2026-06-10T21:52:16Z","Machine Learning Pipelines for Kubeflow"),
    ("kubeflow/hub","Go",175,181,43,"2026-06-10T14:04:41Z","Model Registry for ML model developers"),
    ("kubeflow/website","HTML",184,923,49,"2026-06-10T13:55:27Z","Kubeflow Website"),
    ("kubeflow/trainer","Go",2112,964,129,"2026-06-10T03:16:23Z","Distributed AI Model Training on Kubernetes"),
    ("kubeflow/internal-acls","Go",19,389,1,"2026-06-09T18:22:27Z","Group ACLs for Kubeflow developers"),
    ("kubeflow/spark-operator","Python",3126,1488,97,"2026-06-09T17:15:24Z","Kubernetes operator for Apache Spark"),
    ("kubeflow/community","Jupyter Notebook",194,258,15,"2026-06-09T15:18:15Z","Kubeflow community information"),
    ("kubeflow/manifests","YAML",1022,1065,22,"2026-06-09T13:01:47Z","Kubeflow Community Distribution"),
    ("kubeflow/notebooks","",73,118,169,"2026-06-09T15:34:30Z","Kubeflow Notebooks for AI/ML workloads"),
    ("kubeflow/kale","Python",693,156,47,"2026-06-10T17:35:51Z","Kubeflow superfood for Data Scientists"),
    ("kubeflow/dashboard","TypeScript",16,59,73,"2026-06-10T04:48:30Z","Kubeflow Central Dashboard"),
    ("kubeflow/katib","Python",1685,525,119,"2026-06-05T23:23:35Z","Automated Machine Learning on Kubernetes"),
    ("kubeflow/sdk","Python",120,181,132,"2026-06-08T03:07:18Z","Universal Python SDK for AI workloads on Kubernetes"),
    ("kubeflow/mpi-operator","Go",528,236,104,"2026-06-02T14:30:58Z","Kubernetes Operator for MPI-based applications"),
    ("kubeflow/pipelines-components","Python",11,43,33,"2026-06-04T17:39:10Z","Kubeflow Pipelines"),
    ("kubeflow/blog","Jupyter Notebook",32,62,26,"2026-05-25T13:02:24Z","Kubeflow blog"),
    ("kubeflow/kubeflow","",15715,2672,3,"2026-05-24T11:31:41Z","Machine Learning Toolkit for Kubernetes"),
    ("kubeflow/mcp-server","Python",11,20,25,"2026-05-12T10:14:24Z","MCP Server for AI-Assisted Development"),
    ("kubeflow/arena","Go",812,190,46,"2026-05-07T06:46:17Z","A CLI for Kubeflow"),
    ("kubeflow/docs-agent","Python",37,94,151,"2026-04-14T03:33:15Z","Kubeflow Documentation AI Agent"),
    ("kubeflow/examples","Jsonnet",1462,756,111,"2025-04-14T01:54:52Z","Extended examples and tutorials"),
    ("kubeflow/testing","Python",60,86,33,"2025-02-14T18:33:13Z","Test infrastructure for Kubeflow"),
    ("kubeflow/kfp-tekton","TypeScript",182,123,79,"2024-11-19T12:23:51Z","Kubeflow Pipelines on Tekton"),
    ("kubeflow/kfserving-lts","Jsonnet",12,19,51,"2024-08-02T16:25:44Z",""),
    ("kubeflow/kubebench","Jsonnet",78,35,68,"2024-06-17T19:22:04Z","Repository for benchmarking"),
    ("kubeflow/fate-operator","Go",51,15,6,"2024-02-22T19:44:08Z","Fate operator"),
    ("kubeflow/kfctl","Go",182,134,94,"2023-08-15T20:19:22Z","CLI for deploying Kubeflow"),
    ("kubeflow/kfp-tekton-backend","TypeScript",8,6,46,"2023-08-14T22:05:04Z","Experimental Tekton KFP backend"),
    ("kubeflow/common","Go",53,70,40,"2023-05-28T13:16:00Z","Common APIs for Kubeflow operators"),
    ("kubeflow/.allstar","",2,0,0,"2022-12-06T23:07:59Z",""),
    ("kubeflow/fairing","Jsonnet",337,143,134,"2022-04-11T05:28:47Z","Python SDK for building ML models"),
    ("kubeflow/xgboost-operator","Python",77,53,22,"2021-12-01T18:00:10Z","xgboost operator"),
    ("kubeflow/mxnet-operator","Go",52,33,9,"2021-12-01T17:47:19Z","Kubernetes operator for mxnet jobs"),
    ("kubeflow/pytorch-operator","Jsonnet",310,143,63,"2021-12-01T17:44:48Z","PyTorch on Kubernetes"),
    ("kubeflow/frontend","JavaScript",8,18,12,"2021-12-01T17:41:37Z","kubeflow frontend"),
    ("kubeflow/metadata","TypeScript",123,63,38,"2021-12-01T17:35:27Z","Repository for Metadata assets"),
    ("kubeflow/caffe2-operator","Go",16,12,2,"2021-12-01T01:58:06Z","Experimental caffe2 operator"),
    ("kubeflow/code-intelligence","Jupyter Notebook",56,20,64,"2021-12-01T01:52:58Z","ML-Powered Developer Tools"),
    ("kubeflow/example-seldon","Jupyter Notebook",172,56,9,"2021-12-01T01:49:58Z","End-to-end ML on Kubernetes with Seldon"),
    ("kubeflow/batch-predict","Python",17,7,9,"2021-12-01T01:47:51Z","batch predict"),
    ("kubeflow/reporting","Jsonnet",2,5,1,"2021-12-01T01:42:32Z","Metrics for Kubeflow usage"),
    ("kubeflow/chainer-operator","Jsonnet",17,15,7,"2021-11-14T13:03:57Z","chainer operator"),
    ("kubeflow/crd-validation","Go",11,7,5,"2021-01-25T15:02:53Z","Validation for Kubeflow CRD"),
    ("kubeflow/community-infra","Go",3,9,4,"2021-01-25T14:49:49Z","Declarative configs for KF community infrastructure"),
    ("kubeflow/.github","",2,1,0,"2020-05-12T00:22:56Z","Org wide templates"),
    ("kubeflow/marketing-materials","",4,4,4,"2019-07-19T13:57:15Z",""),
]
for r in kubeflow_repos:
    repos.append(("org", "kubeflow") + r)

# TeglonLabs repos
teglon_repos = [
    ("TeglonLabs/jank-crane","C++",0,0,0,"2026-06-08T19:03:03Z","crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps"),
    ("TeglonLabs/mathpix-gem","Ruby",2,0,11,"2026-01-01T12:13:13Z","Transform mathematical images to LaTeX and documents to markdown"),
    ("TeglonLabs/coin-flip-mcp","JavaScript",0,2,1,"2025-09-21T08:57:27Z","MCP server for flipping coins with varying degrees of randomness"),
    ("TeglonLabs/monad-mcp-server","",0,0,0,"2025-05-14T11:36:14Z","Monad MCP Server"),
    ("TeglonLabs/topoi","Python",0,0,1,"2025-01-24T04:49:26Z",""),
]
for r in teglon_repos:
    repos.append(("org", "TeglonLabs") + r)

# bmorphism repos (50 fetched of 103)
bmorphism_repos = [
    ("bmorphism/Gay.jl","Julia",1,1,189,"2026-06-10T17:03:52Z","Wide-gamut color sampling with splittable determinism"),
    ("bmorphism/world","Python",0,0,0,"2026-06-02T06:49:06Z","Local worlds launcher for SA3, jank, and world proofs"),
    ("bmorphism/nanoclj-zig","Zig",1,0,0,"2026-06-10T16:00:16Z",""),
    ("bmorphism/zig-syrup","Zig",0,0,0,"2026-03-28T21:42:35Z","Embeddable OCapN Syrup encoder/decoder"),
    ("bmorphism/boxxy","Move",0,1,0,"2026-04-30T03:35:52Z",""),
    ("bmorphism/postweb","Go",0,0,0,"2026-04-09T10:51:55Z","postweb — evolved from prepostweb"),
    ("bmorphism/shitcoin","Python",5,0,0,"2022-04-26T18:44:46Z","gets denom for cw20 assets for permissionless degeneracy in IBC"),
    ("bmorphism/magic-world-org","Python",1,0,0,"2026-04-05T06:44:30Z","Magic World Org (Local MLX)"),
    ("bmorphism/ocaml-mcp-sdk","OCaml",61,2,0,"2026-05-08T16:50:34Z","OCaml SDK for Model Context Protocol"),
    ("bmorphism/flox-mcp-bb","Clojure",0,0,0,"2026-06-05T17:53:47Z","Open-source MCP server for Flox"),
    ("bmorphism/tapes","",0,0,0,"2026-02-04T02:23:37Z","VHS tapes for terminal recordings"),
    ("bmorphism/duck-rio-heateq","Rust",0,0,0,"2026-02-02T23:33:35Z",""),
    ("bmorphism/aella","Rascal",1,0,0,"2026-04-02T17:15:48Z",""),
    ("bmorphism/hymlx","Python",1,0,0,"2026-01-22T21:44:46Z",""),
    ("bmorphism/GeoACSets.jl","Julia",0,1,1,"2026-01-19T13:55:07Z","Categorical data structures with geospatial capabilities"),
    ("bmorphism/anti-bullshit-mcp-server","JavaScript",23,7,1,"2026-02-05T15:46:59Z","MCP server for analyzing claims and detecting manipulation"),
    ("bmorphism/vibespace-mcp-go-ternary","HTML",0,1,3,"2025-03-19T21:42:56Z","Go MCP experience for vibes and worlds with NATS streaming"),
    ("bmorphism/open-location-code-zig","Zig",3,0,0,"2026-03-24T21:54:01Z","Open Location Code for Zig"),
    ("bmorphism/bafishka","Clojure",1,0,0,"2025-11-01T06:36:06Z","Rust-native Fish shell-friendly file operations"),
    ("bmorphism/gay-color-learnable","",0,0,0,"2025-12-15T18:41:02Z","Learnable color embeddings connecting Graphistry, Ghidra, Charm"),
    ("bmorphism/gay-hy","Hy",0,0,0,"2025-12-15T15:33:02Z","Hylang MLX color bandwidth protocol"),
    ("bmorphism/multiverse-color-game","Julia",0,0,0,"2025-12-12T05:28:09Z","2+1D Holographic Color Matching Game for VisionPro"),
    ("bmorphism/signal-mcp","Rust",0,0,0,"2025-12-11T06:54:01Z","O(n)->O(1) chromatic mode collapse via Galois connection"),
    ("bmorphism/xf.jl","Julia",0,0,0,"2025-12-05T22:12:21Z","Xenofeminist color synthesis"),
    ("bmorphism/deberta-goemotions","Python",0,0,0,"2025-10-22T18:32:27Z",""),
    ("bmorphism/monero-rental-hash-war","Haskell",1,0,0,"2025-10-24T09:25:25Z","OpenGame analysis of Monero rental hash war"),
    ("bmorphism/bafishka-clean","Rust",1,0,0,"2025-10-24T09:24:58Z","Clean monadic Steel-SCI integration"),
    ("bmorphism/babashka-static-build","Dockerfile",1,0,0,"2025-10-24T09:24:12Z","Static musl babashka build for ARM64 Termux"),
    ("bmorphism/whale","MATLAB",2,0,0,"2026-04-20T15:04:09Z","omniglot + sperm whale codas = metawhaling"),
    ("bmorphism/infinity-topos","Python",1,0,0,"2025-10-24T09:24:02Z",""),
    ("bmorphism/elevenlabs-mcp-enhanced","Python",1,0,0,"2025-10-24T09:24:02Z","Enhanced ElevenLabs MCP server"),
    ("bmorphism/zeldar","Python",1,0,1,"2025-10-24T09:23:57Z","Burning Man Art Robot"),
    ("bmorphism/stellogen-quantum-operads","",1,0,0,"2026-02-02T23:59:31Z","Quantum Operads and ZX-Calculus in Stellogen"),
    ("bmorphism/apple-container-framework","Clojure",0,0,0,"2025-07-13T12:12:13Z","Apple Container Framework"),
    ("bmorphism/ezkl-ethglobal2025","Python",1,0,0,"2025-10-24T09:23:18Z",""),
    ("bmorphism/zk-haiku-nanogpt","Solidity",1,0,0,"2025-10-24T09:23:18Z","ZK-Haiku-NanoGPT: Agentic Proof-Chaining Framework"),
    ("bmorphism/rama-event-processor","Java",1,0,0,"2025-10-24T09:23:16Z","Repository for processing events with Rama"),
    ("bmorphism/oxcaml-sci-canonical","OCaml",1,0,0,"2025-10-24T09:23:08Z","Canonical OxCaml-SCI implementation"),
    ("bmorphism/oxcaml-mcp","",0,0,0,"2025-06-20T22:03:12Z","OxCaml-MCP: High-performance MCP server"),
    ("bmorphism/oxcaml-sci","",0,0,0,"2025-06-20T03:43:41Z","OxCaml-SCI: Performance-optimized Scientific Computing Interface"),
    ("bmorphism/infinity-topos-impossibility","",0,0,14,"2025-05-29T01:55:28Z","Impossibility results for automated analysis verification"),
    ("bmorphism/graphistry-mcp","Python",2,0,0,"2025-10-24T09:22:41Z","Graphistry MCP integration for graph visualization"),
    ("bmorphism/hypernym-mcp-server","JavaScript",6,5,0,"2025-10-24T09:21:53Z",""),
    ("bmorphism/vibespace-mcp-go","",0,0,0,"2025-03-19T20:30:02Z","Go MCP for vibes and worlds"),
    ("bmorphism/krep-mcp-server","JavaScript",1,1,1,"2026-02-10T11:23:43Z","High-performance string search MCP server"),
    ("bmorphism/schoenfinkel","Python",1,0,0,"2025-10-24T09:24:26Z","Post-quantum categorical gravity framework"),
    ("bmorphism/gay-spec","",1,0,0,"2025-10-24T09:25:18Z",""),
    ("bmorphism/duck-rs","Zig",0,0,0,"2025-09-23T04:10:35Z",""),
    ("bmorphism/oxgame","OCaml",0,0,0,"2026-05-15T09:55:59Z","Stellar resolution and open-game composition for OCaml"),
    ("bmorphism/vibesnipe-market","Move",0,0,9,"2026-02-05T10:23:57Z",""),
]
for r in bmorphism_repos:
    repos.append(("user", "bmorphism") + r)

# zubyul repos
zubyul_repos = [
    ("zubyul/voice-observatory","Python",0,0,0,"2026-04-24T05:56:20Z","Passive macOS TUI observing voice-download pathways"),
    ("zubyul/ghostel-emacs-worlds","GLSL",0,0,0,"2026-04-24T00:20:53Z","Ghostty config + ghostel family + emacs-mods"),
    ("zubyul/big-bad-plurigrid-quiz","Emacs Lisp",0,0,0,"2026-04-09T18:51:35Z","27 flashcards from plurigrid/bmorphism/zubyul activity"),
    ("zubyul/Gay.jl","Julia",0,0,0,"2026-03-28T11:30:07Z","Wide-gamut color sampling with splittable determinism"),
    ("zubyul/kinesis-kb360pro","Python",0,0,0,"2026-03-26T10:29:44Z","Claude Code skill for Kinesis Advantage360 Pro keyboard"),
    ("zubyul/gay-world","Python",1,1,0,"2026-04-05T06:54:03Z","Goblin world builder: each goblin is a world"),
    ("zubyul/from-possible-worlds","TeX",0,0,0,"2026-03-16T03:07:20Z",""),
    ("zubyul/tilelang-kernels","Python",0,0,0,"2026-03-16T02:24:04Z","TileLang GPU kernels for SplitMix64 color generation"),
    ("zubyul/gay-terminal-colors","Clojure",0,0,0,"2026-02-21T07:37:49Z","Gay.jl world_terminal_fingerprint"),
    ("zubyul/basin","Rust",0,0,0,"2026-02-13T10:12:20Z",""),
    ("zubyul/plurigrid-site","Svelte",0,1,11,"2026-02-03T08:42:36Z","Plurigrid world: site deployment"),
    ("zubyul/vibesnipe","Move",0,0,1,"2026-01-16T08:50:09Z",""),
    ("zubyul/zubyul.github.io","CSS",1,0,0,"2024-06-10T15:22:35Z",""),
    ("zubyul/toad-warpify-extension","Python",0,0,0,"2026-01-17T07:48:43Z","Warpify extension for Toad"),
    ("zubyul/gay-brain-world","Python",0,0,0,"2025-12-16T01:19:26Z","Gay.jl SPI colors for Moduleur Brain + OpenBCI EEG"),
    ("zubyul/multiplayer-emacs","HTML",0,0,0,"2025-12-12T08:07:30Z","Multiplayer world: Emacs split-pane Vibe Snipe"),
    ("zubyul/hue-world","JavaScript",0,0,0,"2025-12-12T08:32:58Z","Terminal Vibe Snipe puzzle game"),
    ("zubyul/multiverse-color-game","","","","","",""),
    ("zubyul/chromatic-vrf","Kotlin",0,0,0,"2025-12-12T03:22:56Z","Chromatic VRF: I Love Hue puzzle with Gay.jl MCMC"),
    ("zubyul/quantum-telephone","Jupyter Notebook",0,0,0,"2025-12-08T22:15:19Z","Quantum telephone world: entangled message passing"),
    ("zubyul/c-elegans-connectome","JavaScript",0,0,0,"2025-11-21T07:00:25Z",""),
    ("zubyul/cascade-world","Python",1,0,0,"2025-09-16T22:28:36Z","Cascade development environment"),
    ("zubyul/defcon","JavaScript",1,0,0,"2025-07-26T04:28:32Z",""),
    ("zubyul/ghostty-modifications","JavaScript",1,0,0,"2025-09-15T02:44:04Z","Ghostty terminal modifications and MCP servers"),
    ("zubyul/GoofyLifeChoices","Python",1,0,0,"2025-02-18T03:00:57Z",""),
    ("zubyul/openbci-visualizer","Zig",0,0,0,"2026-02-04T09:40:23Z",""),
    ("zubyul/jonikas_for_weronika.-annotated-code","Jupyter Notebook",1,0,0,"2023-08-16T15:35:07Z",""),
    ("zubyul/jonikas_lab_data_analysis_misc","Jupyter Notebook",2,0,0,"2023-06-15T21:54:54Z","various scripts for genetic sequence data"),
    ("zubyul/WGCNA","HTML",2,0,0,"2023-06-16T13:50:22Z","weighted gene correlation network analysis"),
    ("zubyul/Nikolova_lab_data_analysis","R",2,0,0,"2023-06-16T13:55:33Z","undergraduate thesis - cortical thickness and depression"),
    ("zubyul/lastfm_analysis_copy","Jupyter Notebook",1,0,0,"2023-06-15T22:20:33Z","lastfm data analysis"),
    ("zubyul/nash-tui","Rust",0,0,0,"2026-04-13T05:45:43Z","NASH token TUI: real-time candles via GeckoTerminal"),
    ("zubyul/nash-web","Rust",0,0,0,"2026-04-13T07:04:30Z","NASH token browser TUI via ratzilla WASM"),
    ("zubyul/instance-onboarding","Shell",0,0,0,"2026-02-02T01:13:11Z",""),
    ("zubyul/repl","Python",0,0,0,"2026-01-29T07:05:24Z",""),
    ("zubyul/GayMove","Move",0,0,0,"2025-12-18T03:49:16Z",""),
    ("zubyul/multiplayer","HTML",0,0,0,"2025-12-12T03:47:10Z",""),
    ("zubyul/vibe-snipe","Kotlin",0,0,0,"2025-12-12T03:41:50Z",""),
    ("zubyul/cat-world","TypeScript",0,0,0,"2025-12-12T05:39:50Z","Cat gaze tracker"),
    ("zubyul/fleet-bootstrap","Shell",0,0,0,"2026-02-23T08:19:56Z",""),
    ("zubyul/thread-site","Haskell",0,0,0,"2025-12-23T23:32:33Z",""),
    ("zubyul/book","HTML",0,0,0,"2025-03-05T18:24:52Z",""),
    ("zubyul/ezAR","",0,0,0,"2025-02-03T21:02:25Z",""),
    ("zubyul/obsidian","",0,0,0,"2024-05-23T17:59:11Z",""),
    ("zubyul/private","SCSS",0,0,0,"2023-10-05T21:02:13Z",""),
    ("zubyul/reddit_scraper","Python",0,0,0,"2023-06-16T14:03:55Z",""),
    ("zubyul/Python_Undergrad","Python",0,0,0,"2023-06-16T14:01:52Z",""),
    ("zubyul/Nikolova_lab_data_analysis","R",2,0,0,"2023-06-16T13:55:33Z","cortical thickness to transcription factors for depression"),
    ("zubyul/zoterobsidian","Shell",0,0,0,"2025-09-28T16:43:31Z",""),
    ("zubyul/plurigrid-playbook","",0,0,0,"2025-09-17T02:10:53Z",""),
]
for r in zubyul_repos:
    if len(r) == 7 and r[4]:  # skip empty entries
        repos.append(("user", "zubyul") + r)

# migalkin repos
migalkin_repos = [
    ("migalkin/kgcourse2021","HTML",25,9,0,"2026-02-16T05:16:08Z","Материалы к курсу по Knowledge Graphs"),
    ("migalkin/migalkin.github.io","JavaScript",0,0,0,"2025-05-20T23:58:08Z","Github Pages for academic personal websites"),
    ("migalkin/NBFNet_mlx","Python",10,1,1,"2026-03-11T01:31:21Z","Neural Bellman-Ford networks in MLX for Apple Silicon"),
    ("migalkin/StarE","Python",89,16,1,"2026-04-16T14:12:45Z","EMNLP 2020: Message Passing for Hyper-Relational Knowledge Graphs"),
    ("migalkin/rambo","Rust",3,0,1,"2023-02-28T16:37:22Z",""),
    ("migalkin/ciss2_project","Jupyter Notebook",0,0,6,"2019-06-28T23:14:33Z",""),
    ("migalkin/RWL","Python",8,1,0,"2026-05-28T20:19:20Z","Weisfeiler and Leman Go Relational (LOG 2022)"),
    ("migalkin/NodePiece","Python",144,21,0,"2026-05-07T05:40:02Z","Compositional Representations for Large Knowledge Graphs (ICLR'22)"),
    ("migalkin/SQuAD-es-mt","",0,1,0,"2020-07-14T17:18:37Z","Spanish version of SQuAD via machine translation"),
    ("migalkin/netquery_rdf","Python",0,0,0,"2019-06-01T12:49:18Z","NIPS 2018 paper fork for RDF"),
    ("migalkin/edbt-experiments","",0,0,0,"2017-11-20T10:27:28Z",""),
    ("migalkin/SMJoin-experiments","R",1,0,0,"2020-03-04T15:56:23Z","ISWC 2017 SMJoin results"),
    ("migalkin/ekgs_clustering","Python",0,0,0,"2016-08-28T16:25:19Z",""),
    ("migalkin/r_energyConsumption","R",0,0,0,"2016-05-12T21:00:17Z",""),
    ("migalkin/ontologies","Web Ontology Language",0,0,0,"2015-12-06T13:49:53Z",""),
    ("migalkin/Tables_Provider","Java",0,0,0,"2015-03-20T00:17:36Z",""),
    ("migalkin/datasciencecoursera","",0,0,0,"2015-02-12T23:57:16Z","Coursera Data Science course"),
    ("migalkin/InformationWorkbenchTestSrc","Java",0,0,0,"2014-10-15T21:42:40Z",""),
    ("migalkin/LinkedData","",0,0,0,"2014-10-15T21:42:40Z","Information Workbench + Linked Open Data"),
]
for r in migalkin_repos:
    repos.append(("user", "migalkin") + r)

# DJedamski repos
djedamski_repos = [
    ("DJedamski/Getting-and-Cleaning-Data","R",1,0,0,"2023-04-21T01:42:34Z","Coursera Project"),
    ("DJedamski/Kaggle","",1,0,0,"2023-04-21T01:42:35Z",""),
    ("DJedamski/School","R",1,1,0,"2023-04-21T01:42:33Z","Small projects from grad school"),
    ("DJedamski/Project_Euler","",0,0,0,"2015-09-05T17:13:32Z",""),
    ("DJedamski/kaggle_ncaa18","Jupyter Notebook",0,0,0,"2018-02-26T16:33:24Z","NCAA March Madness competition 2018"),
    ("DJedamski/EDA","R",0,0,0,"2014-11-09T17:00:39Z","Coursera Project"),
]
for r in djedamski_repos:
    repos.append(("user", "DJedamski") + r)

# wasita repos
wasita_repos = [
    ("wasita/magic-garden","Python",2,1,1,"2026-04-22T21:16:43Z","bot for magic garden discord auto-purchasing seeds"),
    ("wasita/wasita.github.io","Svelte",1,0,8,"2026-06-01T04:15:14Z","personal website"),
    ("wasita/wins-search","CSS",1,0,0,"2023-06-03T19:01:11Z","Women in Network Science member list website"),
    ("wasita/send2kobo","TypeScript",1,0,0,"2026-05-19T02:59:26Z","Website for sending books to your kobo e-reader"),
    ("wasita/ch3-lib","Typst",0,0,0,"2026-04-12T04:03:22Z",""),
    ("wasita/d60-keeb","",0,0,0,"2024-08-26T00:46:25Z",""),
    ("wasita/wm-cv","Svelte",0,0,0,"2026-05-13T05:29:08Z","Academic CV as single page web app"),
    ("wasita/food-diary","Svelte",0,0,0,"2025-12-13T01:06:43Z",""),
    ("wasita/proj-template","",0,0,0,"2026-01-09T20:35:44Z",""),
    ("wasita/honeycomb-demo","JavaScript",0,0,0,"2021-12-07T21:38:28Z",""),
    ("wasita/vocoder","JavaScript",0,0,0,"2026-05-06T05:14:03Z",""),
]
for r in wasita_repos:
    repos.append(("user", "wasita") + r)

# kristinezheng repos
kristinezheng_repos = [
    ("kristinezheng/Green-Machine","Python",0,0,0,"2021-09-19T05:33:04Z","HackMIT 2021: Sustainability Track"),
    ("kristinezheng/lookit-jenga","Jupyter Notebook",0,0,0,"2024-05-16T18:29:05Z","Lookit study for 9.85"),
    ("kristinezheng/auditory-illusion","CSS",0,0,0,"2022-03-07T02:57:44Z","9.35 spring 2022 auditory illusion"),
    ("kristinezheng/kristinezheng.github.io","HTML",0,0,0,"2026-06-07T22:53:10Z",""),
    ("kristinezheng/graph_example","Python",0,0,0,"2021-10-08T07:29:53Z",""),
]
for r in kristinezheng_repos:
    repos.append(("user", "kristinezheng") + r)

# M1shaaa repos
m1shaaa_repos = [
    ("M1shaaa/lab-bookshelf-","TypeScript",0,0,0,"2024-12-31T04:37:02Z",""),
    ("M1shaaa/Classes","",0,0,0,"2023-12-06T18:20:27Z",""),
    ("M1shaaa/Lookit-Demo","",0,0,0,"2023-04-10T02:44:01Z",""),
    ("M1shaaa/rosie-s-study-3-lookit-project","",0,0,0,"2024-11-04T22:15:39Z",""),
    ("M1shaaa/Python-Lookit-Uploads","Python",0,0,0,"2024-02-15T22:31:41Z","random projects"),
    ("M1shaaa/M1shaaa","",0,0,0,"2026-02-04T19:32:04Z","Config files for GitHub profile"),
    ("M1shaaa/MNIST-Classifier","",0,0,0,"2023-11-28T06:10:47Z",""),
    ("M1shaaa/Yale-Work","HTML",0,0,0,"2023-12-06T18:33:14Z",""),
]
for r in m1shaaa_repos:
    repos.append(("user", "M1shaaa") + r)

# AustinCStone repos
austincstone_repos = [
    ("AustinCStone/TextGAN","Python",92,30,5,"2025-03-03T13:26:32Z","generative adversarial network for text generation"),
    ("AustinCStone/StereoVisionMRF","Python",11,4,0,"2026-04-01T07:39:41Z","MRF with loopy belief propagation to infer depth"),
    ("AustinCStone/SpectralClustering","Python",3,2,0,"2021-04-16T08:46:36Z","spectral clustering homework"),
    ("AustinCStone/StructureFromMotion","Python",1,0,0,"2019-04-26T19:43:12Z","Recover 3D geometry from videos"),
    ("AustinCStone/logisticRegressionHaskell","Haskell",1,0,0,"2018-02-02T13:34:28Z","Logistic regression in Haskell for MNIST"),
    ("AustinCStone/TheanoStuff","Python",0,0,0,"2021-09-04T03:21:57Z","Getting acquainted with Theano"),
    ("AustinCStone/Founderati-Server","Python",0,1,0,"2015-08-25T19:17:45Z","Server for Founderati"),
    ("AustinCStone/SleepDetectionMoto360","Java",0,0,0,"2014-10-19T03:21:03Z","Sleep detection for Moto 360"),
    ("AustinCStone/TFBirds","Python",0,0,0,"2019-01-30T08:07:22Z","Bird flocking simulator in TensorFlow"),
    ("AustinCStone/bmfork","Python",0,0,1,"2025-05-09T04:09:43Z",""),
    ("AustinCStone/stuffForAlec","JavaScript",0,0,0,"2015-01-05T01:31:49Z",""),
    ("AustinCStone/Founderati-client","JavaScript",0,1,0,"2015-08-25T19:16:58Z","Founderati network for entrepreneurs"),
    ("AustinCStone/stonks","Python",0,0,0,"2020-09-04T22:54:35Z","Playing around with option calculations"),
    ("AustinCStone/statsHw2","Python",0,0,0,"2015-09-28T00:50:05Z","Simple linear regression and model selection"),
    ("AustinCStone/OptimalControl","Python",0,0,0,"2018-02-03T08:08:33Z","Concepts from control theory"),
    ("AustinCStone/Genetic-Algorithm-Sorting-Network","Python",0,0,0,"2015-05-09T03:19:37Z",""),
    ("AustinCStone/QuantumSearchAlgorithmSimulation","Java",0,0,0,"2014-11-07T02:02:29Z","Grover algorithm simulation"),
    ("AustinCStone/LensBuilder","Python",0,0,0,"2019-04-04T04:22:59Z","WIP optimize surface of focusing lens"),
    ("AustinCStone/testLogin","Python",0,0,0,"2023-02-13T20:52:27Z",""),
    ("AustinCStone/FlaskBlog","Python",0,0,0,"2014-12-17T23:41:58Z","A simple blog written with Flask"),
    ("AustinCStone/gibbs_sampling","Python",0,0,0,"2023-07-23T17:30:23Z","Gibbs sampling and ancestral rejection sampling proof"),
    ("AustinCStone/bitmind-fork","",0,0,0,"2025-01-09T06:16:50Z","forked on jan 8 2025"),
    ("AustinCStone/Royal-Road-With-Ditches-Genetic-Algorithm","Python",0,0,0,"2014-05-11T02:27:49Z","Royal Road genetic algorithm modification"),
    ("AustinCStone/Z-order-curve","Python",0,0,0,"2019-06-09T02:53:24Z","Demo implementation of z-order curve"),
    ("AustinCStone/ConvNet","Python",0,0,0,"2015-09-07T22:24:51Z","Convolutional neural network for MNIST classification"),
    ("AustinCStone/austincstone.github.io","HTML",0,0,0,"2021-10-23T22:48:49Z",""),
    ("AustinCStone/StatsModelingHw1","Python",0,0,0,"2015-09-19T04:13:22Z",""),
    ("AustinCStone/test","",0,0,0,"2021-09-21T21:15:50Z",""),
    ("AustinCStone/EpsteinSearch","Python",0,0,0,"2026-02-11T01:10:57Z",""),
    ("AustinCStone/LearningCuda","C",0,0,0,"2017-11-04T22:17:48Z","Me working through CUDA by example"),
]
for r in austincstone_repos:
    repos.append(("user", "AustinCStone") + r)

print(f"Total repos collected: {len(repos)}")

# Build SQL inserts for all repos
insert_statements = []
increment_id = 1
for (source_type, source_name, full_name, language, stars, forks, issues, pushed_at, description) in repos:
    # Compute GF3 color for this increment
    trit, color, gf3_name = gf3(increment_id)
    # Snapshot hash
    snap_hash = hashlib.md5(f"{full_name}{pushed_at}".encode()).hexdigest()[:8]
    # Escape strings for SQL
    def esc(s):
        return str(s).replace("'", "''")

    repo_name = full_name.split("/")[-1] if "/" in str(full_name) else str(full_name)

    # Insert world_increment
    sql_inc = f"""INSERT INTO world_increments VALUES (
        {increment_id}, now(), {trit}, '{esc(color)}', '{esc(gf3_name)}',
        '{esc(source_type)}', '{esc(source_name)}', 'repo_snapshot',
        '{esc(repo_name)}', '{esc(source_name)}', '{esc(snap_hash)}'
    );"""

    # Insert repo_snapshot
    stars_val = int(stars) if str(stars).isdigit() else 0
    forks_val = int(forks) if str(forks).isdigit() else 0
    issues_val = int(issues) if str(issues).isdigit() else 0

    sql_repo = f"""INSERT INTO repo_snapshots VALUES (
        {increment_id}, now(), {increment_id},
        '{esc(source_name)}', '{esc(repo_name)}', '{esc(full_name)}',
        '{esc(language)}', {stars_val}, {forks_val}, {issues_val},
        '{esc(pushed_at)}', '{esc(description)}'
    );"""

    insert_statements.append(sql_inc)
    insert_statements.append(sql_repo)
    increment_id += 1

# Write all inserts to a SQL file
sql_file = "/tmp/world_increment_inserts.sql"
with open(sql_file, "w") as f:
    f.write("\n".join(insert_statements))

print(f"Generated {len(insert_statements)} insert statements")
print("Running inserts...")
result = run_sql_file(sql_file)
print(result[:200] if result else "Done")

# Aptos snapshots - all resource_not_found = 0 APT
aptos_data = [
    ("alice", "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b", 0),
    ("bob", "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d", 0),
    ("A", "0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a", 0),
    ("B", "0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13", 0),
    ("C", "0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e", 0),
    ("D", "0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1", 0),
    ("E", "0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36", 0),
    ("F", "0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71", 0),
    ("G", "0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32", 0),
    ("H", "0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f", 0),
    ("I", "0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9", 0),
    ("J", "0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54", 0),
    ("K", "0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4", 0),
    ("L", "0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9", 0),
    ("M", "0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9", 0),
    ("N", "0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c", 0),
    ("O", "0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d", 0),
    ("P", "0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948", 0),
    ("Q", "0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9", 0),
    ("R", "0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10", 0),
    ("S", "0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386", 0),
    ("T", "0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588", 0),
    ("U", "0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956", 0),
    ("V", "0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3", 0),
    ("W", "0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0", 0),
    ("X", "0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d", 0),
    ("Y", "0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4", 0),
    ("Z", "0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c", 0),
]
print("Inserting Aptos snapshots...")
for world, addr, bal in aptos_data:
    run_sql(f"INSERT INTO aptos_snapshots VALUES (now(), '{world}', '{addr}', {bal});")

# Multisig probes (all returned 2 sigs required)
multisig_data = [
    ("A-B", "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2, True),
    ("A-G", "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2, True),
    ("Y-Z", "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2, True),
    ("S-T", "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2, True),
    ("V-W", "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2, True),
]
print("Inserting multisig probes...")
for pair, addr, sigs, healthy in multisig_data:
    run_sql(f"INSERT INTO multisig_probes VALUES (now(), '{pair}', '{addr}', {sigs}, {str(healthy).upper()});")

print("Verifying row counts...")
for table in ["world_increments", "repo_snapshots", "aptos_snapshots", "multisig_probes", "mnx_snapshots"]:
    r = subprocess.run(["duckdb", DB, "-c", f"SELECT count(*) as n FROM {table};"],
                      capture_output=True, text=True)
    print(f"  {table}: {r.stdout.strip()}")

print("Done!")
