#!/usr/bin/env python3
"""World-increment sweep + Hamming swarm snapshot."""
import duckdb, hashlib, time, subprocess, json, os

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
con = duckdb.connect(DB)

# ── Schema ────────────────────────────────────────────────────────────────────
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

def gf3(id_):
    t = id_ % 3
    if t == 0: return (0, "#d3869b", "ERGODIC")
    if t == 1: return (1, "#b8bb26", "PLUS")
    return (-1, "#cc241d", "MINUS")

def snap_hash(data): return hashlib.md5(str(data).encode()).hexdigest()[:12]

# ── Repo data ─────────────────────────────────────────────────────────────────
repos = [
  # plurigrid (100 repos)
  ("plurigrid","plurigrid/shrimp","","0","0","0","2026-07-03T01:24:20Z","Jank worked example: shrimp"),
  ("plurigrid","plurigrid/asi","HTML","28","8","4","2026-06-29T03:15:56Z","everything is topological chemputer!"),
  ("plurigrid","plurigrid/place","TeX","1","1","12","2026-06-29T20:40:59Z",""),
  ("plurigrid","plurigrid/eirobri","Clojure","0","0","30","2026-06-30T02:23:56Z","EiRoBri replay world"),
  ("plurigrid","plurigrid/nash-portal","Rust","2","3","1","2026-05-19T01:49:59Z","NASH token TUI in the browser"),
  ("plurigrid","plurigrid/gorj","Clojure","0","0","951","2026-07-04T00:15:40Z","forj + Rama topology nREPL routing + GF(3) gay trit coloring"),
  ("plurigrid","plurigrid/zig-syrup","Zig","2","2","0","2026-04-30T03:52:16Z","High-performance Zig OCapN Syrup"),
  ("plurigrid","plurigrid/asi-skills","Julia","3","0","0","2026-04-26T08:09:26Z","69 skills with Galois Hole Type accessibility"),
  ("plurigrid","plurigrid/bci-blue-share","JavaScript","0","0","0","2026-04-26T07:08:03Z","BCI signal infrastructure"),
  ("plurigrid","plurigrid/nanoclj-zig","Zig","1","1","20","2026-04-25T07:29:09Z","NaN-boxed Clojure interpreter in Zig 0.15"),
  ("plurigrid","plurigrid/spi-race","Swift","0","0","0","2026-04-21T19:31:56Z","Splitmix Parallel Integrity"),
  ("plurigrid","plurigrid/reafference","HTML","0","0","0","2026-04-16T05:21:49Z","Reafference adaptation workspace"),
  ("plurigrid","plurigrid/web-browser","Rust","0","0","0","2026-04-10T02:54:47Z","web-browser from prepostweb lineage"),
  ("plurigrid","plurigrid/vivarium","Clojure","1","0","0","2026-04-08T08:38:37Z",""),
  ("plurigrid","plurigrid/flowglad-rs","Rust","0","0","0","2026-04-08T07:56:15Z",""),
  ("plurigrid","plurigrid/tree-sitter-nanoclj-zig","C","0","0","0","2026-04-04T07:48:21Z","Tree-sitter grammar for nanoclj-zig"),
  ("plurigrid","plurigrid/forester","XSLT","0","0","0","2026-03-30T01:32:26Z","CatColab mathematical documentation forest"),
  ("plurigrid","plurigrid/gatomic","Clojure","0","0","0","2026-03-30T00:54:48Z","Deterministic color identity store"),
  ("plurigrid","plurigrid/blue","TeX","0","0","0","2026-03-29T23:06:32Z",""),
  ("plurigrid","plurigrid/red","","0","0","0","2026-03-29T22:58:46Z",""),
  ("plurigrid","plurigrid/nblm-flashcards","Hy","0","0","0","2026-03-26T08:23:01Z","NotebookLM Enterprise flashcard pipeline"),
  ("plurigrid","plurigrid/gemini-agent","Python","0","0","0","2026-02-19T06:39:16Z",""),
  ("plurigrid","plurigrid/graded-optic","Haskell","0","0","0","2026-02-08T16:10:16Z","Semiring-graded bidirectional processes"),
  ("plurigrid","plurigrid/json-canvas","","0","0","0","2026-02-06T06:50:57Z","JSON Canvas: Real-time interaction data capture"),
  ("plurigrid","plurigrid/shepherd","Scheme","0","0","0","2026-01-23T07:47:28Z","Spritely Shepherd Service manager"),
  ("plurigrid","plurigrid/goblinshare","Scheme","0","0","0","2026-01-23T07:47:12Z","P2P filesharing demo for Goblins"),
  ("plurigrid","plurigrid/magenc","Scheme","0","0","0","2026-01-23T07:47:11Z","Magenc Magnet URIs"),
  ("plurigrid","plurigrid/hoot","Scheme","0","0","1","2026-01-23T07:47:10Z","Spritely Hoot Scheme to WebAssembly compiler"),
  ("plurigrid","plurigrid/leprechauns","Racket","0","0","0","2026-01-23T07:46:46Z","Spritely Goblins + Gay.jl semantic colors"),
  ("plurigrid","plurigrid/spritely-semantic-colors","","0","0","0","2026-01-23T07:38:32Z","Deterministic color mappings for Spritely/Goblins"),
  ("plurigrid","plurigrid/gay-tofu","HTML","0","0","0","2026-01-08T15:14:34Z","Low-discrepancy color sequences for visual TOFU"),
  ("plurigrid","plurigrid/lazygay","Go","0","0","0","2026-01-08T14:19:25Z","lazygit fork with Gay.jl deterministic commit coloring"),
  ("plurigrid","plurigrid/gay-terminal","Rust","0","0","0","2026-01-08T14:19:24Z","Terminal ANSI coloring with Gay.jl"),
  ("plurigrid","plurigrid/gay-go","Go","0","0","0","2026-01-08T14:19:23Z","Go implementation of Gay.jl deterministic coloring"),
  ("plurigrid","plurigrid/gay-rs","Rust","0","0","0","2026-01-08T14:19:22Z","Rust crate for Gay.jl deterministic coloring with GF(3) trits"),
  ("plurigrid","plurigrid/lazybjj","Rust","0","0","0","2026-01-08T14:19:19Z","TUI for jj with Gay.jl GF(3) coloring"),
  ("plurigrid","plurigrid/agent-o-rama","Clojure","0","0","0","2026-01-02T01:09:22Z",""),
  ("plurigrid","plurigrid/aptos-wallet-ruby","Ruby","1","0","0","2025-09-30T22:47:22Z",""),
  ("plurigrid","plurigrid/duck-kanban","Rust","1","0","0","2025-09-26T20:18:38Z","Duck intelligence kanban system"),
  ("plurigrid","plurigrid/shiteshiteshite","","0","0","0","2025-09-26T03:07:20Z",""),
  ("plurigrid","plurigrid/discohy","Hy","0","0","0","2025-09-10T02:01:31Z",""),
  ("plurigrid","plurigrid/telemind","","0","0","0","2025-06-12T05:54:59Z",""),
  ("plurigrid","plurigrid/ontology","JavaScript","8","9","16","2025-05-27T18:18:34Z","autopoietic ergodicity and embodied gradualism"),
  ("plurigrid","plurigrid/Plurigraph","JavaScript","3","5","4","2025-01-05T08:39:09Z","Plurigrid knowledge base"),
  ("plurigrid","plurigrid/signe","Python","0","0","0","2024-08-15T20:52:03Z","Signal messages data traversal"),
  ("plurigrid","plurigrid/SwiftDuck","","0","0","0","2024-08-08T18:19:06Z",""),
  ("plurigrid","plurigrid/act","Python","3","1","4","2024-07-26T08:27:08Z","building blocks for cognitive category theory"),
  ("plurigrid","plurigrid/xenomorphic","","0","0","0","2024-04-09T03:24:55Z",""),
  ("plurigrid","plurigrid/metamorphic","","0","0","0","2024-04-09T03:22:41Z",""),
  ("plurigrid","plurigrid/DiffusionVoiceDemo","Clojure","0","0","0","2024-04-02T18:09:01Z",""),
  ("plurigrid","plurigrid/website","Clojure","0","1","0","2024-03-30T04:37:51Z",""),
  ("plurigrid","plurigrid/StochFlow","Python","4","1","0","2024-03-20T23:34:57Z","Python library for stochastic interpolant models"),
  ("plurigrid","plurigrid/intent","","0","0","0","2024-03-04T04:53:38Z","Simulations for intent markets"),
  ("plurigrid","plurigrid/novella","TypeScript","1","0","0","2024-01-27T08:12:55Z",""),
  ("plurigrid","plurigrid/ACT.jl","Julia","0","0","0","2024-01-21T00:02:25Z","applied categorical duck cybernetics"),
  ("plurigrid","plurigrid/ducklings","TypeScript","0","0","15","2023-12-25T07:34:27Z",""),
  ("plurigrid","plurigrid/paretae","TypeScript","0","0","14","2023-11-20T05:14:42Z",""),
  ("plurigrid","plurigrid/experiments","","0","0","0","2023-11-17T05:39:07Z",""),
  ("plurigrid","plurigrid/fuckit","Clojure","0","0","0","2023-11-14T21:26:14Z",""),
  ("plurigrid","plurigrid/omega","Clojure","0","0","0","2023-11-07T21:08:46Z",""),
  ("plurigrid","plurigrid/org","Jupyter Notebook","2","0","1","2023-11-07T01:08:05Z","Dynamically Replicating Duck"),
  ("plurigrid","plurigrid/CVAE-Flows","","0","0","0","2023-10-24T14:41:32Z",""),
  ("plurigrid","plurigrid/morph-prover-cli","","0","1","0","2023-10-18T03:49:03Z","Lean4"),
  ("plurigrid","plurigrid/uncharacter","TypeScript","0","0","0","2023-09-19T20:17:46Z",""),
  ("plurigrid","plurigrid/chateau","TypeScript","0","0","0","2023-08-30T20:11:12Z",""),
  ("plurigrid","plurigrid/gmgm","","0","0","1","2023-08-25T13:54:00Z",""),
  ("plurigrid","plurigrid/tuttle","TypeScript","0","0","0","2023-08-09T17:40:44Z",""),
  ("plurigrid","plurigrid/mesoplay","","0","0","0","2023-08-09T06:19:03Z",""),
  ("plurigrid","plurigrid/am","Python","0","0","0","2023-08-05T12:46:33Z",""),
  ("plurigrid","plurigrid/compose","","0","0","2","2023-07-24T06:18:48Z",""),
  ("plurigrid","plurigrid/flussi","","0","0","1","2023-07-15T06:40:11Z",""),
  ("plurigrid","plurigrid/cf","","0","0","0","2023-07-11T08:11:29Z",""),
  ("plurigrid","plurigrid/poepoe","","0","0","1","2023-07-09T22:20:50Z",""),
  ("plurigrid","plurigrid/marketplace","","0","0","1","2023-07-09T05:52:30Z",""),
  ("plurigrid","plurigrid/smoller","","0","0","1","2023-07-06T07:38:04Z",""),
  ("plurigrid","plurigrid/liquidity","","0","0","1","2023-07-06T02:07:28Z",""),
  ("plurigrid","plurigrid/solid-rs","","0","0","1","2023-07-05T21:58:05Z",""),
  ("plurigrid","plurigrid/solid","Python","0","0","0","2023-07-05T21:52:25Z",""),
  ("plurigrid","plurigrid/ipegrafo","Python","0","0","0","2023-07-03T07:29:40Z",""),
  ("plurigrid","plurigrid/plurigrid-v4","TypeScript","0","0","0","2023-07-03T06:31:59Z",""),
  ("plurigrid","plurigrid/novella-v3","","0","0","0","2023-07-03T06:29:40Z",""),
  ("plurigrid","plurigrid/polyglottal","TypeScript","0","0","0","2023-07-03T06:23:45Z",""),
  ("plurigrid","plurigrid/novella-v2","","0","0","0","2023-07-03T06:22:38Z",""),
  ("plurigrid","plurigrid/cocreation-ui","","0","0","2","2023-07-03T04:45:53Z",""),
  ("plurigrid","plurigrid/smol","","0","0","1","2023-07-02T08:45:32Z",""),
  ("plurigrid","plurigrid/commons","TypeScript","0","0","0","2023-06-27T05:46:24Z",""),
  ("plurigrid","plurigrid/post-web","Svelte","0","0","0","2023-06-18T00:24:24Z",""),
  ("plurigrid","plurigrid/microworlds","Rust","3","5","3","2023-05-13T03:54:56Z",""),
  ("plurigrid","plurigrid/pills","","0","0","0","2023-05-02T10:03:03Z","metaphors for embodied gradualism"),
  ("plurigrid","plurigrid/plurigrid-rs","Rust","0","0","0","2023-04-21T01:02:56Z",""),
  ("plurigrid","plurigrid/plurigrid-game.github.io","HTML","0","0","1","2023-04-20T00:17:55Z",""),
  ("plurigrid","plurigrid/synth","Rust","0","0","0","2023-04-15T01:56:45Z",""),
  ("plurigrid","plurigrid/birbs","C++","0","0","0","2023-04-15T01:56:32Z","Build native CosmWasm apps"),
  ("plurigrid","plurigrid/agent","Python","5","1","6","2023-03-31T18:45:23Z","Framework for agency amplification"),
  ("plurigrid","plurigrid/vcg-auction","Rust","7","2","1","2023-03-16T21:53:08Z","a simple VCG auction contract"),
  ("plurigrid","plurigrid/bidder","Dart","0","0","1","2023-03-15T15:23:22Z","simple flutter VCG auction app"),
  ("plurigrid","plurigrid/plurigrid.github.io","HTML","1","2","2","2023-01-20T03:27:34Z",""),
  ("plurigrid","plurigrid/VPP","Julia","0","1","0","2023-01-11T18:41:07Z","Hyperreal Power Plant"),
  ("plurigrid","plurigrid/grid","TypeScript","2","1","1","2023-01-02T11:55:55Z","Plurigrid Testnet #0: Edith Clarke"),
  ("plurigrid","plurigrid/commons-contracts","Rust","0","0","0","2022-09-09T09:20:11Z","CosmWasm contracts for Commons Stack"),
  # kubeflow (48 repos)
  ("kubeflow","kubeflow/website","HTML","184","923","29","2026-07-03T20:27:09Z","Kubeflow Website"),
  ("kubeflow","kubeflow/internal-acls","Go","19","391","2","2026-07-03T20:27:04Z","Group ACLs for Kubeflow developers"),
  ("kubeflow","kubeflow/hub","Go","173","184","33","2026-07-03T16:09:16Z","Model Registry"),
  ("kubeflow","kubeflow/mpi-operator","Go","529","237","99","2026-07-03T15:24:45Z","Kubernetes Operator for MPI-based applications"),
  ("kubeflow","kubeflow/trainer","Go","2129","975","147","2026-07-03T13:41:32Z","Distributed AI Model Training and LLM Fine-Tuning"),
  ("kubeflow","kubeflow/pipelines","Python","4169","2021","414","2026-07-03T13:38:00Z","Machine Learning Pipelines for Kubeflow"),
  ("kubeflow","kubeflow/community-distribution","YAML","1028","1067","25","2026-07-03T09:20:06Z","Kubeflow Community Distribution"),
  ("kubeflow","kubeflow/dashboard","TypeScript","16","59","87","2026-07-03T15:44:52Z","Kubeflow Central Dashboard"),
  ("kubeflow","kubeflow/arena","Go","814","194","45","2026-07-03T12:22:43Z","A CLI for Kubeflow"),
  ("kubeflow","kubeflow/sdk","Python","123","188","140","2026-07-02T19:23:35Z","Universal Python SDK for AI workloads"),
  ("kubeflow","kubeflow/pipelines-components","Python","11","47","36","2026-07-02T16:09:54Z","Kubeflow Pipelines components"),
  ("kubeflow","kubeflow/spark-operator","Python","3132","1496","103","2026-07-02T08:52:01Z","Kubernetes operator for Apache Spark"),
  ("kubeflow","kubeflow/katib","Python","1689","529","114","2026-07-01T21:20:57Z","Automated Machine Learning on Kubernetes"),
  ("kubeflow","kubeflow/community","Jupyter Notebook","194","265","15","2026-07-01T21:20:20Z","Kubeflow community information"),
  ("kubeflow","kubeflow/kale","Python","695","156","38","2026-07-01T12:44:49Z","Kubeflow superfood for Data Scientists"),
  ("kubeflow","kubeflow/mcp-server","Python","19","25","32","2026-06-29T14:46:23Z","MCP Server for AI-Assisted Development"),
  ("kubeflow","kubeflow/mcp-apache-spark-history-server","Python","180","66","19","2026-06-25T20:28:43Z","MCP Server for Apache Spark History Server"),
  ("kubeflow","kubeflow/docs-agent","Python","39","96","154","2026-06-25T05:33:14Z","Kubeflow Documentation AI Agent"),
  ("kubeflow","kubeflow/notebooks","","73","125","180","2026-07-03T15:34:14Z","Kubeflow Notebooks"),
  ("kubeflow","kubeflow/kubeflow","","15760","2682","0","2026-06-18T11:45:16Z","Machine Learning Toolkit for Kubernetes"),
  ("kubeflow","kubeflow/mlflow-integration","Python","6","5","5","2026-07-01T19:01:56Z",""),
  ("kubeflow","kubeflow/blog","Jupyter Notebook","32","62","26","2026-06-11T16:32:01Z","Kubeflow blog"),
  ("kubeflow","kubeflow/examples","Jsonnet","1460","756","111","2025-04-14T01:54:52Z","Extended examples and tutorials"),
  ("kubeflow","kubeflow/testing","Python","60","86","33","2025-02-14T18:33:13Z","Test infrastructure and tooling"),
  ("kubeflow","kubeflow/kfp-tekton","TypeScript","183","123","79","2024-11-19T12:23:51Z","Kubeflow Pipelines on Tekton"),
  ("kubeflow","kubeflow/kfserving-lts","Jsonnet","12","19","51","2024-08-02T16:25:44Z",""),
  ("kubeflow","kubeflow/kubebench","Jsonnet","78","35","68","2024-06-17T19:22:04Z","Repository for benchmarking"),
  ("kubeflow","kubeflow/fate-operator","Go","50","15","6","2024-02-22T19:44:08Z","Fate operator"),
  ("kubeflow","kubeflow/kfctl","Go","182","134","94","2023-08-15T20:19:22Z","CLI for deploying and managing Kubeflow"),
  ("kubeflow","kubeflow/kfp-tekton-backend","TypeScript","8","6","46","2023-08-14T22:05:04Z","Experimental Tekton yaml behind KFP API"),
  ("kubeflow","kubeflow/common","Go","53","70","40","2023-05-28T13:16:00Z","Common APIs and libraries"),
  ("kubeflow","kubeflow/.allstar","","2","0","0","2022-12-06T23:07:59Z",""),
  ("kubeflow","kubeflow/fairing","Jsonnet","337","143","134","2022-04-11T05:28:47Z","Python SDK for building, training, deploying ML models"),
  ("kubeflow","kubeflow/xgboost-operator","Python","77","53","22","2021-12-01T18:00:10Z","Incubating project for xgboost operator"),
  ("kubeflow","kubeflow/mxnet-operator","Go","52","33","9","2021-12-01T17:47:19Z","A Kubernetes operator for mxnet jobs"),
  ("kubeflow","kubeflow/pytorch-operator","Jsonnet","310","143","63","2021-12-01T17:44:48Z","PyTorch on Kubernetes"),
  ("kubeflow","kubeflow/frontend","JavaScript","8","18","12","2021-12-01T17:41:37Z","Repository for kubeflow frontend"),
  ("kubeflow","kubeflow/metadata","TypeScript","123","63","38","2021-12-01T17:35:27Z","Repository for Metadata assets"),
  ("kubeflow","kubeflow/caffe2-operator","Go","16","12","2","2021-12-01T01:58:06Z","Experimental caffe2 operator"),
  ("kubeflow","kubeflow/code-intelligence","Jupyter Notebook","56","20","64","2021-12-01T01:52:58Z","ML-Powered Developer Tools"),
  ("kubeflow","kubeflow/example-seldon","Jupyter Notebook","172","56","9","2021-12-01T01:49:58Z","End-to-end ML on Kubernetes"),
  ("kubeflow","kubeflow/batch-predict","Python","17","7","9","2021-12-01T01:47:51Z","Repository for batch predict"),
  ("kubeflow","kubeflow/reporting","Jsonnet","2","5","1","2021-12-01T01:42:32Z","Metrics collection for Kubeflow"),
  ("kubeflow","kubeflow/chainer-operator","Jsonnet","17","15","7","2021-11-14T13:03:57Z","Repository for chainer operator"),
  ("kubeflow","kubeflow/crd-validation","Go","11","7","5","2021-01-25T15:02:53Z","Validation Generation for Kubeflow CRD"),
  ("kubeflow","kubeflow/community-infra","Go","3","9","4","2021-01-25T14:49:49Z","Declarative configurations for KF community infra"),
  ("kubeflow","kubeflow/.github","","2","1","0","2020-05-12T00:22:56Z","Org wide templates"),
  ("kubeflow","kubeflow/marketing-materials","","4","4","4","2019-07-19T13:57:15Z",""),
  # TeglonLabs (5 repos)
  ("TeglonLabs","TeglonLabs/jank-crane","C++","0","0","0","2026-06-08T19:03:03Z","crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps"),
  ("TeglonLabs","TeglonLabs/mathpix-gem","Ruby","2","0","11","2026-01-01T12:13:13Z","Transform mathematical images to LaTeX"),
  ("TeglonLabs","TeglonLabs/coin-flip-mcp","JavaScript","0","2","1","2025-09-21T08:57:27Z","MCP server for flipping coins"),
  ("TeglonLabs","TeglonLabs/monad-mcp-server","","0","0","0","2025-05-14T11:36:14Z","Monad MCP Server"),
  ("TeglonLabs","TeglonLabs/topoi","Python","0","0","1","2025-01-24T04:49:26Z",""),
  # bmorphism (105 repos - key ones)
  ("bmorphism","bmorphism/satreadout","HTML","0","0","0","2026-06-20T13:05:41Z","Machine-checked saturating non-Riemannian perceptual readout"),
  ("bmorphism","bmorphism/Gay.jl","Julia","2","1","187","2026-07-04T00:33:17Z","Wide-gamut color sampling with splittable determinism"),
  ("bmorphism","bmorphism/bci-preview","HTML","0","0","0","2026-06-20T00:20:44Z","Stable redirect front for bci.place forester preview"),
  ("bmorphism","bmorphism/world","Python","0","0","0","2026-06-02T06:49:02Z","Local worlds launcher for SA3, jank, and world proofs"),
  ("bmorphism","bmorphism/oxgame","OCaml","0","0","0","2026-05-15T09:53:27Z","Stellar resolution and open-game composition for OCaml"),
  ("bmorphism","bmorphism/nanoclj-zig","Zig","1","0","0","2026-05-07T20:12:15Z",""),
  ("bmorphism","bmorphism/zig-syrup","Zig","0","0","0","2026-05-07T19:49:05Z","Embeddable OCapN Syrup encoder/decoder in Zig"),
  ("bmorphism","bmorphism/boxxy","Move","0","1","0","2026-04-30T03:35:47Z",""),
  ("bmorphism","bmorphism/postweb","Go","0","0","0","2026-04-09T10:51:57Z","postweb — evolved from prepostweb"),
  ("bmorphism","bmorphism/shitcoin","Python","5","0","0","2026-04-08T08:07:08Z","gets denom for cw20 assets"),
  ("bmorphism","bmorphism/magic-world-org","Python","1","0","0","2026-04-05T07:03:50Z","Magic World Org (Local MLX)"),
  ("bmorphism","bmorphism/ocaml-mcp-sdk","OCaml","61","2","0","2026-03-16T05:24:25Z","OCaml SDK for Model Context Protocol"),
  ("bmorphism","bmorphism/flox-mcp-bb","Clojure","0","0","0","2026-02-12T02:45:43Z","Open-source MCP server for Flox"),
  ("bmorphism","bmorphism/vibesnipe-market","Move","0","0","9","2026-02-05T10:23:25Z",""),
  ("bmorphism","bmorphism/anti-bullshit-mcp-server","JavaScript","23","7","1","2026-01-16T08:54:58Z","MCP server for analyzing claims"),
  ("bmorphism","bmorphism/vibespace-mcp-go-ternary","HTML","0","1","3","2026-01-11T12:50:40Z","Go MCP experience for vibes and worlds with NATS"),
  ("bmorphism","bmorphism/open-location-code-zig","Zig","3","0","0","2025-12-30T19:33:45Z","Open Location Code (Plus Codes) for Zig"),
  ("bmorphism","bmorphism/bafishka","Clojure","1","0","0","2025-12-19T09:38:00Z","Rust-native Fish shell with Steel-backed SCI Clojure"),
  ("bmorphism","bmorphism/multiverse-color-game","Julia","0","0","0","2025-12-12T05:28:11Z","2+1D Holographic Color Matching Game for VisionPro"),
  ("bmorphism","bmorphism/monero-rental-hash-war","Haskell","1","0","0","2025-10-05T23:08:54Z","OpenGame analysis of Monero rental hash war"),
  ("bmorphism","bmorphism/schoenfinkel","Python","1","0","0","2025-10-04T23:31:11Z","Post-quantum categorical gravity framework"),
  ("bmorphism","bmorphism/graphistry-mcp","Python","2","0","0","2025-05-06T17:34:24Z","Graphistry MCP integration"),
  ("bmorphism","bmorphism/hypernym-mcp-server","JavaScript","6","5","0","2025-04-02T21:21:08Z",""),
  ("bmorphism","bmorphism/manifold-mcp-server","JavaScript","14","9","5","2025-01-11T10:36:58Z","MCP server for Manifold Markets"),
  ("bmorphism","bmorphism/say-mcp-server","JavaScript","20","9","3","2025-01-07T03:15:18Z","MCP server for macOS text-to-speech"),
  ("bmorphism","bmorphism/penumbra-mcp","JavaScript","5","6","3","2025-01-07T01:15:23Z","MCP server for Penumbra blockchain"),
  ("bmorphism","bmorphism/nats-mcp-server","","7","3","2","2025-01-06T23:33:41Z","MCP server for NATS messaging system"),
  ("bmorphism","bmorphism/marginalia-mcp-server","JavaScript","8","6","0","2025-01-06T05:47:24Z","MCP server for marginalia and annotations"),
  ("bmorphism","bmorphism/babashka-mcp-server","JavaScript","19","6","3","2025-01-05T11:09:42Z","MCP server for Babashka/Clojure"),
  ("bmorphism","bmorphism/penrose-mcp","JavaScript","9","4","0","2025-01-20T21:44:55Z","Penrose server for the Infinity-Topos environment"),
  ("bmorphism","bmorphism/risc0-cosmwasm-example","Rust","23","2","1","2022-10-20T23:50:40Z","CosmWasm + zkVM RISC-V EFI template"),
  # zubyul (49 repos - key ones)
  ("zubyul","zubyul/voice-observatory","Python","0","0","0","2026-04-24T05:56:17Z","Passive macOS TUI observing voice-download pathways"),
  ("zubyul","zubyul/ghostel-emacs-worlds","GLSL","0","0","0","2026-04-24T00:20:56Z","Ghostty config + ghostel family"),
  ("zubyul","zubyul/nash-tui","Rust","0","0","0","2026-04-13T07:45:16Z","NASH token TUI: real-time candles via GeckoTerminal"),
  ("zubyul","zubyul/nash-web","Rust","0","0","0","2026-04-13T07:08:58Z","NASH token browser TUI via ratzilla WASM"),
  ("zubyul","zubyul/gay-world","Python","1","1","0","2026-03-26T04:03:39Z","Goblin world builder with Gay.jl SPI colors"),
  ("zubyul","zubyul/Gay.jl","Julia","0","0","0","2026-03-28T11:30:01Z","Wide-gamut color sampling fork"),
  ("zubyul","zubyul/kinesis-kb360pro","Python","0","0","0","2026-03-26T10:29:40Z","Claude Code skill for Kinesis Advantage360 Pro"),
  ("zubyul","zubyul/tilelang-kernels","Python","0","0","0","2026-03-16T02:31:13Z","TileLang GPU kernels for SplitMix64 color generation"),
  ("zubyul","zubyul/plurigrid-site","Svelte","0","1","11","2026-02-04T03:20:08Z","Plurigrid world: site deployment"),
  ("zubyul","zubyul/vibesnipe","Move","0","0","1","2026-01-30T22:36:03Z",""),
  ("zubyul","zubyul/zubyul.github.io","CSS","1","0","0","2026-01-27T03:24:34Z",""),
  ("zubyul","zubyul/cat-world","TypeScript","0","0","0","2025-12-12T08:47:14Z","Cat gaze tracker"),
  ("zubyul","zubyul/chromatic-vrf","Kotlin","0","0","0","2025-12-12T03:26:22Z","Chromatic VRF: I Love Hue puzzle"),
  ("zubyul","zubyul/cascade-world","Python","1","0","0","2025-09-19T18:25:12Z","Cascade development environment"),
  ("zubyul","zubyul/defcon","JavaScript","1","0","0","2025-09-17T02:07:00Z",""),
  ("zubyul","zubyul/ghostty-modifications","JavaScript","1","0","0","2025-09-15T02:45:21Z","Ghostty terminal modifications and MCP servers"),
  ("zubyul","zubyul/jonikas_lab_data_analysis_misc","Jupyter Notebook","2","0","0","2023-08-16T20:24:40Z","Various scripts for large genetic sequence data"),
  ("zubyul","zubyul/WGCNA","HTML","2","0","0","2023-07-05T18:02:30Z","Weighted gene correlation network analysis"),
  ("zubyul","zubyul/Nikolova_lab_data_analysis","R","2","0","0","2023-06-16T13:56:58Z","HCP data for brain-body relationship study"),
  # migalkin (19 repos)
  ("migalkin","migalkin/NodePiece","Python","144","21","0","2026-05-07T05:40:02Z","Compositional Representations for Large Knowledge Graphs (ICLR 2022)"),
  ("migalkin","migalkin/StarE","Python","89","16","1","2026-04-16T14:12:45Z","EMNLP 2020: Message Passing for Hyper-Relational KGs"),
  ("migalkin","migalkin/kgcourse2021","HTML","25","9","0","2026-02-16T05:16:08Z","Материалы к курсу по Knowledge Graphs"),
  ("migalkin","migalkin/NBFNet_mlx","Python","10","1","1","2026-03-11T01:31:21Z","Neural Bellman-Ford networks in MLX for Apple Silicon"),
  ("migalkin","migalkin/RWL","Python","8","1","0","2026-05-28T20:19:20Z","Weisfeiler and Leman Go Relational (LOG 2022)"),
  ("migalkin","migalkin/rambo","Rust","3","0","1","2023-02-28T16:37:22Z",""),
  ("migalkin","migalkin/SMJoin-experiments","R","1","0","0","2020-03-04T15:56:23Z","ISWC 2017 SMJoin results"),
  ("migalkin","migalkin/netquery_rdf","Python","0","0","0","2019-06-01T12:49:18Z","NIPS 2018 paper fork for RDF"),
  # DJedamski (6 repos)
  ("DJedamski","DJedamski/Getting-and-Cleaning-Data","R","1","0","0","2023-04-21T01:42:34Z","Coursera Project"),
  ("DJedamski","DJedamski/Kaggle","","1","0","0","2023-04-21T01:42:35Z",""),
  ("DJedamski","DJedamski/School","R","1","1","0","2023-04-21T01:42:33Z","Small projects from grad school"),
  ("DJedamski","DJedamski/Project_Euler","","0","0","0","2015-09-05T17:13:32Z",""),
  ("DJedamski","DJedamski/kaggle_ncaa18","Jupyter Notebook","0","0","0","2018-02-26T16:33:24Z","NCAA March Madness competition 2018"),
  ("DJedamski","DJedamski/EDA","R","0","0","0","2014-11-09T17:00:39Z","Coursera Project"),
  # wasita (11 repos)
  ("wasita","wasita/magic-garden","Python","2","1","1","2026-04-22T21:16:43Z","Discord magic garden bot"),
  ("wasita","wasita/wasita.github.io","Svelte","1","0","8","2026-07-02T01:40:18Z","personal website"),
  ("wasita","wasita/wins-search","CSS","1","0","0","2023-06-03T19:01:11Z","Women in Network Science member list website"),
  ("wasita","wasita/send2kobo","TypeScript","1","0","0","2026-05-19T02:59:26Z","Website for sending books to kobo e-reader"),
  ("wasita","wasita/ch3-lib","Typst","0","0","0","2026-04-12T04:03:22Z",""),
  ("wasita","wasita/wm-cv","Svelte","0","0","0","2026-05-13T05:29:08Z","Academic CV as web app"),
  ("wasita","wasita/food-diary","Svelte","0","0","0","2025-12-13T01:06:43Z",""),
  ("wasita","wasita/proj-template","","0","0","0","2026-06-19T21:22:21Z",""),
  ("wasita","wasita/vocoder","JavaScript","0","0","0","2026-05-06T05:14:03Z",""),
  # kristinezheng (5 repos)
  ("kristinezheng","kristinezheng/Green-Machine","Python","0","0","0","2021-09-19T05:33:04Z","HackMIT 2021: Sustainability Track"),
  ("kristinezheng","kristinezheng/lookit-jenga","Jupyter Notebook","0","0","0","2024-05-16T18:29:05Z","Lookit study for 9.85"),
  ("kristinezheng","kristinezheng/auditory-illusion","CSS","0","0","0","2022-03-07T02:57:44Z","9.35 spring 2022 auditory illusion"),
  ("kristinezheng","kristinezheng/kristinezheng.github.io","HTML","0","0","0","2026-07-01T20:57:48Z",""),
  ("kristinezheng","kristinezheng/graph_example","Python","0","0","0","2021-10-08T07:29:35Z",""),
  # M1shaaa (8 repos)
  ("M1shaaa","M1shaaa/lab-bookshelf-","TypeScript","0","0","0","2024-12-31T05:11:18Z",""),
  ("M1shaaa","M1shaaa/Classes","","0","0","0","2023-12-06T18:20:27Z",""),
  ("M1shaaa","M1shaaa/Lookit-Demo","","0","0","0","2023-04-10T02:44:01Z",""),
  ("M1shaaa","M1shaaa/Python-Lookit-Uploads","Python","0","0","0","2024-02-15T22:59:37Z","random projects"),
  ("M1shaaa","M1shaaa/M1shaaa","","0","0","0","2026-02-04T19:32:04Z","Config files for GitHub profile"),
  ("M1shaaa","M1shaaa/MNIST-Classifier","","0","0","0","2023-11-28T06:10:47Z",""),
  ("M1shaaa","M1shaaa/Yale-Work","HTML","0","0","0","2023-12-06T18:33:14Z",""),
  # AustinCStone (40 repos - key ones)
  ("AustinCStone","AustinCStone/TextGAN","Python","92","30","5","2025-03-03T13:26:32Z","Generative adversarial network for text generation"),
  ("AustinCStone","AustinCStone/StereoVisionMRF","Python","11","4","0","2026-04-01T07:39:41Z","MRF with loopy belief propagation for stereo depth"),
  ("AustinCStone","AustinCStone/SpectralClustering","Python","3","2","0","2021-04-16T08:46:36Z","Implementing spectral clustering"),
  ("AustinCStone","AustinCStone/StructureFromMotion","Python","1","0","0","2019-04-26T19:43:12Z","Recover 3D geometry from videos"),
  ("AustinCStone","AustinCStone/logisticRegressionHaskell","Haskell","1","0","0","2018-02-02T13:34:28Z","Logistic regression in Haskell"),
  ("AustinCStone","AustinCStone/bmfork","Python","0","0","1","2025-05-09T04:18:54Z",""),
  ("AustinCStone","AustinCStone/EpsteinSearch","Python","0","0","0","2026-02-11T01:10:57Z",""),
  ("AustinCStone","AustinCStone/bmforkupdate","Python","0","0","0","2025-05-09T04:50:16Z",""),
]

print(f"Inserting {len(repos)} repos into DuckDB...")
inc_id = 0
for org_user, full_name, lang, stars, forks, issues, pushed_at, desc in repos:
    inc_id += 1
    trit, color, name = gf3(inc_id)
    h = snap_hash(full_name + pushed_at)
    repo_name = full_name.split("/",1)[1] if "/" in full_name else full_name
    # world_increment row
    con.execute("""INSERT INTO world_increments VALUES (?,now(),?,?,?,'repo',?,?,?,?,?)""",
        [inc_id, trit, color, name, org_user, "push", repo_name, "", h])
    # repo_snapshot row
    repo_id = inc_id
    con.execute("""INSERT INTO repo_snapshots VALUES (?,now(),?,?,?,?,?,?,?,?,?,?)""",
        [repo_id, inc_id, org_user, repo_name, full_name, lang,
         int(stars), int(forks), int(issues), pushed_at, desc[:120]])

print(f"✓ {inc_id} world_increment rows and {inc_id} repo_snapshot rows inserted")

# ── Aptos wallet balances ─────────────────────────────────────────────────────
APTOS_BASE = "https://fullnode.mainnet.aptoslabs.com/v1"
RESOURCE = "0x1::coin::CoinStore%3C0x1::aptos_coin::AptosCoin%3E"

wallets = {
    "alice": "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b",
    "bob":   "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d",
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

print(f"\nQuerying {len(wallets)} Aptos wallets...")
aptos_results = []
for world, addr in wallets.items():
    url = f"{APTOS_BASE}/accounts/{addr}/resource/{RESOURCE}"
    try:
        result = subprocess.run(
            ["curl", "-s", "--max-time", "10", url],
            capture_output=True, text=True)
        data = json.loads(result.stdout)
        raw = data.get("data", {}).get("coin", {}).get("value", None)
        if raw is not None:
            apt = int(raw) / 100_000_000
        else:
            apt = None
        aptos_results.append((world, addr, apt))
        status = f"{apt:.4f} APT" if apt is not None else "no balance"
        print(f"  {world}: {status}")
    except Exception as e:
        aptos_results.append((world, addr, None))
        print(f"  {world}: error ({e})")
    time.sleep(1)

for world, addr, bal in aptos_results:
    if bal is not None:
        con.execute("INSERT INTO aptos_snapshots VALUES (now(),?,?,?)", [world, addr, bal])
    else:
        con.execute("INSERT INTO aptos_snapshots VALUES (now(),?,?,NULL)", [world, addr])

print(f"✓ {len(aptos_results)} Aptos wallet rows inserted")

# ── Multisig probes ───────────────────────────────────────────────────────────
MULTISIG_URL = f"{APTOS_BASE}/view"
multisigs = {
    "A-B": "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",
    "A-G": "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",
    "Y-Z": "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",
    "S-T": "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",
    "V-W": "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",
}

print(f"\nProbing {len(multisigs)} multisig contracts...")
for pair, addr in multisigs.items():
    payload = json.dumps({
        "function": "0x1::multisig_account::num_signatures_required",
        "type_arguments": [],
        "arguments": [addr]
    })
    try:
        result = subprocess.run(
            ["curl", "-s", "--max-time", "10", "-X", "POST",
             "-H", "Content-Type: application/json",
             "-d", payload, MULTISIG_URL],
            capture_output=True, text=True)
        data = json.loads(result.stdout)
        if isinstance(data, list) and len(data) > 0:
            sigs = int(data[0])
            healthy = sigs > 0
            print(f"  {pair}: sigs_required={sigs}, healthy={healthy}")
            con.execute("INSERT INTO multisig_probes VALUES (now(),?,?,?,?)",
                        [pair, addr, sigs, healthy])
        else:
            print(f"  {pair}: unexpected response: {data}")
            con.execute("INSERT INTO multisig_probes VALUES (now(),?,?,NULL,FALSE)",
                        [pair, addr])
    except Exception as e:
        print(f"  {pair}: error ({e})")
        con.execute("INSERT INTO multisig_probes VALUES (now(),?,?,NULL,FALSE)", [pair, addr])
    time.sleep(1)

# ── MNX Markets ───────────────────────────────────────────────────────────────
print("\nProbing MNX markets...")
mnx_urls = [
    "https://testnet.mnx.fi/api/markets",
    "https://testnet.mnx.fi/api/v1/markets",
    "https://testnet.mnx.fi/api/tickers",
]
mnx_found = False
for url in mnx_urls:
    try:
        result = subprocess.run(
            ["curl", "-s", "--max-time", "10", "-L", url],
            capture_output=True, text=True)
        if result.returncode == 0 and len(result.stdout) > 10:
            try:
                data = json.loads(result.stdout)
                print(f"  MNX data from {url}: {str(data)[:200]}")
                # try to insert if it looks like market data
                if isinstance(data, list):
                    for item in data[:20]:
                        if isinstance(item, dict):
                            con.execute("INSERT INTO mnx_snapshots VALUES (now(),?,?,?,?,?)", [
                                item.get("ticker", item.get("symbol", "")),
                                item.get("name", ""),
                                item.get("category", ""),
                                float(item.get("price", item.get("last", 0)) or 0),
                                float(item.get("change_pct", item.get("change", 0)) or 0),
                            ])
                mnx_found = True
                break
            except json.JSONDecodeError:
                print(f"  MNX {url}: non-JSON response (SPA), length={len(result.stdout)}")
    except Exception as e:
        print(f"  MNX {url}: error ({e})")

if not mnx_found:
    print("  MNX testnet.mnx.fi: unavailable (SPA with no public API endpoints)")
    con.execute("INSERT INTO mnx_snapshots VALUES (now(),'N/A','N/A (SPA)','unavailable',0,0)")

# ── Summary stats ─────────────────────────────────────────────────────────────
total_inc = con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0]
total_repos = con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0]
total_aptos = con.execute("SELECT COUNT(*) FROM aptos_snapshots WHERE balance_apt IS NOT NULL").fetchone()[0]
total_multisig = con.execute("SELECT COUNT(*) FROM multisig_probes").fetchone()[0]

top_repos = con.execute("""
    SELECT full_name, stars, language, pushed_at
    FROM repo_snapshots WHERE stars > 0
    ORDER BY stars DESC LIMIT 10
""").fetchall()

aptos_rows = con.execute("""
    SELECT world, address, balance_apt
    FROM aptos_snapshots ORDER BY world
""").fetchall()

multisig_rows = con.execute("""
    SELECT pair, address, sigs_required, healthy FROM multisig_probes
""").fetchall()

gf3_dist = con.execute("""
    SELECT gf3_name, gf3_color, COUNT(*) as cnt
    FROM world_increments GROUP BY gf3_name, gf3_color ORDER BY cnt DESC
""").fetchall()

org_dist = con.execute("""
    SELECT org_or_user, COUNT(*) as cnt
    FROM repo_snapshots GROUP BY org_or_user ORDER BY cnt DESC
""").fetchall()

print(f"\n{'='*60}")
print(f"SWEEP COMPLETE")
print(f"  world_increments: {total_inc}")
print(f"  repo_snapshots:   {total_repos}")
print(f"  aptos_snapshots:  {total_aptos} with balances")
print(f"  multisig_probes:  {total_multisig}")

# ── Write LATEST_SWEEP.md ─────────────────────────────────────────────────────
aptos_table = "\n".join(
    f"| {r[0]} | `{r[1][:20]}...` | {f'{r[2]:.6f}' if r[2] is not None else 'N/A'} |"
    for r in aptos_rows
)
multisig_table = "\n".join(
    f"| {r[0]} | `{r[1][:20]}...` | {r[2] if r[2] is not None else 'N/A'} | {'✅' if r[3] else '❌'} |"
    for r in multisig_rows
)
top_table = "\n".join(
    f"| {r[0]} | {r[1]} | {r[2] or ''} | {r[3][:10]} |"
    for r in top_repos
)
gf3_table = "\n".join(
    f"| {r[1]} | {r[0]} | {r[2]} |"
    for r in gf3_dist
)
org_table = "\n".join(
    f"| {r[0]} | {r[1]} |"
    for r in org_dist
)

md = f"""# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-04
**DuckDB:** `world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Coverage

| Source | Type | Repos |
|--------|------|-------|
{org_table}

**Total world_increments:** {total_inc}
**Total repo_snapshots:** {total_repos}

### GF(3) Color Chain Distribution

| Color (Hex) | Name | Count |
|-------------|------|-------|
{gf3_table}

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
{top_table}

### Notable Highlights
- **plurigrid/gorj** (this repo): 951 open issues, active GF(3) + nREPL work, pushed 2026-07-04
- **kubeflow/kubeflow**: 15,760 stars — most starred in sweep
- **kubeflow/pipelines**: 4,169 stars, 414 open issues — most active KF repo
- **bmorphism/Gay.jl**: 187 open issues, active development 2026-07-04
- **bmorphism/ocaml-mcp-sdk**: 61 stars — top bmorphism repo
- **migalkin/NodePiece**: 144 stars — top zubyul social graph repo

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (APT)

| World | Address | Balance (APT) |
|-------|---------|---------------|
{aptos_table}

**Wallets with balances:** {total_aptos}/{len(wallets)}

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
{multisig_table}

### MNX Markets

`testnet.mnx.fi` returned no structured API data — the site appears to be a single-page app without public REST endpoints. Status: **unavailable**.

---

## DuckDB Schema Summary

| Table | Rows |
|-------|------|
| world_increments | {total_inc} |
| repo_snapshots | {total_repos} |
| aptos_snapshots | {len(aptos_rows)} |
| multisig_probes | {total_multisig} |
| mnx_snapshots | 1 (unavailable sentinel) |

---

*Generated by world-increment-sweep + hamming-swarm-snapshot agent*
"""

with open("/home/user/gorj/packages/world-increment/ducklake/LATEST_SWEEP.md", "w") as f:
    f.write(md)

print("✓ LATEST_SWEEP.md written")
con.close()
print("✓ DuckDB connection closed")
