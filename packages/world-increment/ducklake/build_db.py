#!/usr/bin/env python3
"""Build world-increments DuckDB from collected sweep data."""
import duckdb
import hashlib
import os
from datetime import datetime, timezone

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"

def gf3(id_val):
    trit = id_val % 3
    if trit == 0:
        return (0, "#d3869b", "ERGODIC")
    elif trit == 1:
        return (1, "#b8bb26", "PLUS")
    else:
        return (-1, "#cc241d", "MINUS")

def sha8(s):
    return hashlib.sha256(s.encode()).hexdigest()[:8]

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

NOW = datetime.now(timezone.utc).isoformat()

# ─── REPO DATA ────────────────────────────────────────────────────────────────
sources = {
    "plurigrid": ("org", [
        ('plurigrid/place','TeX',1,2,8,'2026-06-04T09:51:50Z',''),
        ('plurigrid/eirobri','Clojure',0,0,29,'2026-06-03T20:43:46Z','EiRoBri replay world'),
        ('plurigrid/nash-portal','Rust',2,3,1,'2026-05-19T01:49:59Z','NASH token TUI in the browser'),
        ('plurigrid/gorj','Clojure',0,0,417,'2026-06-07T11:20:48Z','forj + Rama topology nREPL routing + GF(3)'),
        ('plurigrid/zig-syrup','Zig',2,2,0,'2026-04-30T03:52:16Z','High-performance Zig OCapN Syrup'),
        ('plurigrid/asi','HTML',25,7,4,'2026-04-26T08:51:41Z','everything is topological chemputer!'),
        ('plurigrid/asi-skills','Julia',3,1,0,'2026-04-26T08:09:26Z','69 skills with Galois Hole Type'),
        ('plurigrid/bci-blue-share','JavaScript',0,0,0,'2026-04-26T07:08:03Z','BCI signal infrastructure'),
        ('plurigrid/nanoclj-zig','Zig',1,2,20,'2026-04-25T07:29:09Z','NaN-boxed Clojure interpreter in Zig 0.15'),
        ('plurigrid/spi-race','Swift',0,0,0,'2026-04-21T19:31:56Z','Splitmix Parallel Integrity'),
        ('plurigrid/reafference','HTML',0,0,0,'2026-04-16T05:21:49Z','Reafference adaptation workspace'),
        ('plurigrid/web-browser','Rust',0,0,0,'2026-04-10T02:54:47Z','web-browser from prepostweb lineage'),
        ('plurigrid/vivarium','Clojure',1,0,0,'2026-04-08T08:38:37Z',''),
        ('plurigrid/flowglad-rs','Rust',0,0,0,'2026-04-08T07:56:15Z',''),
        ('plurigrid/tree-sitter-nanoclj-zig','C',0,0,0,'2026-04-04T07:48:21Z','Tree-sitter grammar for nanoclj-zig'),
        ('plurigrid/forester','XSLT',0,0,0,'2026-03-30T01:32:26Z','CatColab mathematical documentation forest'),
        ('plurigrid/gatomic','Clojure',0,0,0,'2026-03-30T00:54:48Z','Deterministic color identity store'),
        ('plurigrid/blue','TeX',0,0,0,'2026-03-29T23:06:32Z',''),
        ('plurigrid/red',None,0,0,0,'2026-03-29T22:58:46Z',''),
        ('plurigrid/nblm-flashcards','Hy',0,0,0,'2026-03-26T08:23:01Z','NotebookLM Enterprise flashcard pipeline'),
        ('plurigrid/gemini-agent','Python',0,0,0,'2026-02-19T06:39:16Z',''),
        ('plurigrid/graded-optic','Haskell',0,0,0,'2026-02-08T16:10:16Z','Semiring-graded bidirectional processes'),
        ('plurigrid/json-canvas',None,0,0,0,'2026-02-06T06:50:57Z','JSON Canvas: Real-time interaction data capture'),
        ('plurigrid/shepherd','Scheme',0,0,0,'2026-01-23T07:47:28Z','Spritely Shepherd - Service manager'),
        ('plurigrid/goblinshare','Scheme',0,0,0,'2026-01-23T07:47:12Z','P2P filesharing demo for Goblins'),
        ('plurigrid/magenc','Scheme',0,0,0,'2026-01-23T07:47:11Z','Magenc Magnet URIs'),
        ('plurigrid/hoot','Scheme',0,0,1,'2026-01-23T07:47:10Z','Spritely Hoot - Scheme to WebAssembly compiler'),
        ('plurigrid/leprechauns','Racket',0,0,0,'2026-01-23T07:46:46Z','Spritely Goblins + Gay.jl semantic colors'),
        ('plurigrid/spritely-semantic-colors',None,0,0,0,'2026-01-23T07:38:32Z','Deterministic color mappings for Spritely/Goblins'),
        ('plurigrid/gay-tofu','HTML',0,0,0,'2026-01-08T15:14:34Z','Low-discrepancy color sequences for visual TOFU'),
        ('plurigrid/lazygay','Go',0,0,0,'2026-01-08T14:19:25Z','lazygit fork with Gay.jl deterministic commit coloring'),
        ('plurigrid/gay-terminal','Rust',0,0,0,'2026-01-08T14:19:24Z','Terminal ANSI coloring with Gay.jl'),
        ('plurigrid/gay-go','Go',0,0,0,'2026-01-08T14:19:23Z','Go implementation of Gay.jl deterministic coloring'),
        ('plurigrid/gay-rs','Rust',0,0,0,'2026-01-08T14:19:22Z','Rust crate for Gay.jl deterministic coloring GF(3)'),
        ('plurigrid/lazybjj','Rust',0,0,0,'2026-01-08T14:19:19Z','TUI for jj with Gay.jl GF(3) coloring'),
        ('plurigrid/agent-o-rama','Clojure',0,0,0,'2026-01-02T01:09:22Z',''),
        ('plurigrid/aptos-wallet-ruby','Ruby',1,0,0,'2025-09-30T22:47:22Z',''),
        ('plurigrid/duck-kanban','Rust',1,0,0,'2025-09-26T20:18:38Z','Duck intelligence kanban system'),
        ('plurigrid/shiteshiteshite',None,0,0,0,'2025-09-26T03:07:20Z','Duck intelligence kanban system'),
        ('plurigrid/discohy','Hy',0,0,0,'2025-09-10T02:01:31Z',''),
        ('plurigrid/telemind',None,0,0,0,'2025-06-12T05:54:59Z',''),
        ('plurigrid/ontology','JavaScript',8,9,16,'2025-05-27T18:18:34Z','autopoietic ergodicity and embodied gradualism'),
        ('plurigrid/Plurigraph','JavaScript',3,5,4,'2025-01-05T08:39:09Z','Plurigrid knowledge base for Obsidian.md'),
        ('plurigrid/signe','Python',0,0,0,'2024-08-15T20:52:03Z','Signal messages data traversal'),
        ('plurigrid/SwiftDuck',None,0,0,0,'2024-08-08T18:19:06Z',''),
        ('plurigrid/act','Python',3,1,4,'2024-07-26T08:27:08Z','building blocks for cognitive category theory'),
        ('plurigrid/xenomorphic',None,0,0,0,'2024-04-09T03:24:55Z',''),
        ('plurigrid/metamorphic',None,0,0,0,'2024-04-09T03:22:41Z',''),
        ('plurigrid/DiffusionVoiceDemo','Clojure',0,0,0,'2024-04-02T18:09:01Z',''),
        ('plurigrid/website','Clojure',0,1,0,'2024-03-30T04:37:51Z',''),
        ('plurigrid/StochFlow','Python',4,1,0,'2024-03-20T23:34:57Z','stochastic interpolant models and algorithms'),
        ('plurigrid/intent',None,0,0,0,'2024-03-04T04:53:38Z','Simulations for An Analysis of Intent Markets'),
        ('plurigrid/novella','TypeScript',1,0,0,'2024-01-27T08:12:55Z',''),
        ('plurigrid/ACT.jl','Julia',0,0,0,'2024-01-21T00:02:25Z','applied categorical duck cybernetics'),
        ('plurigrid/ducklings','TypeScript',0,0,15,'2023-12-25T07:34:27Z',''),
        ('plurigrid/paretae','TypeScript',0,0,14,'2023-11-20T05:14:42Z',''),
        ('plurigrid/experiments',None,0,0,0,'2023-11-17T05:39:07Z','Learning from Penrose development archive'),
        ('plurigrid/fuckit','Clojure',0,0,0,'2023-11-14T21:26:14Z',''),
        ('plurigrid/omega','Clojure',0,0,0,'2023-11-07T21:08:46Z',''),
        ('plurigrid/org','Jupyter Notebook',2,0,1,'2023-11-07T01:08:05Z','Dynamically Replicating Duck'),
        ('plurigrid/CVAE-Flows',None,0,0,0,'2023-10-24T14:41:32Z','Leveraging dihypergraphs and latent spaces'),
        ('plurigrid/morph-prover-cli',None,0,1,0,'2023-10-18T03:49:03Z','Lean4 in'),
        ('plurigrid/uncharacter','TypeScript',0,0,0,'2023-09-19T20:17:46Z',''),
        ('plurigrid/chateau','TypeScript',0,0,0,'2023-08-30T20:11:12Z',''),
        ('plurigrid/gmgm',None,0,0,1,'2023-08-25T13:54:00Z',''),
        ('plurigrid/tuttle','TypeScript',0,0,0,'2023-08-09T17:40:44Z',''),
        ('plurigrid/mesoplay',None,0,0,0,'2023-08-09T06:19:03Z',''),
        ('plurigrid/am','Python',0,0,0,'2023-08-05T12:46:33Z',''),
        ('plurigrid/compose',None,0,0,2,'2023-07-24T06:18:48Z',''),
        ('plurigrid/flussi',None,0,0,1,'2023-07-15T06:40:11Z',''),
        ('plurigrid/cf',None,0,0,0,'2023-07-11T08:11:29Z',''),
        ('plurigrid/poepoe',None,0,0,1,'2023-07-09T22:20:50Z',''),
        ('plurigrid/marketplace',None,0,0,1,'2023-07-09T05:52:30Z',''),
        ('plurigrid/smoller',None,0,0,1,'2023-07-06T07:38:04Z',''),
        ('plurigrid/liquidity',None,0,0,1,'2023-07-06T02:07:28Z',''),
        ('plurigrid/solid-rs',None,0,0,1,'2023-07-05T21:58:05Z',''),
        ('plurigrid/solid','Python',0,0,0,'2023-07-05T21:52:25Z',''),
        ('plurigrid/ipegrafo','Python',0,0,0,'2023-07-03T07:29:40Z',''),
        ('plurigrid/plurigrid-v4','TypeScript',0,0,0,'2023-07-03T06:31:59Z',''),
        ('plurigrid/novella-v3',None,0,0,0,'2023-07-03T06:29:40Z',''),
        ('plurigrid/polyglottal','TypeScript',0,0,0,'2023-07-03T06:23:45Z',''),
        ('plurigrid/novella-v2',None,0,0,0,'2023-07-03T06:22:38Z',''),
        ('plurigrid/cocreation-ui',None,0,0,2,'2023-07-03T04:45:53Z',''),
        ('plurigrid/smol',None,0,0,1,'2023-07-02T08:45:32Z',''),
        ('plurigrid/commons','TypeScript',0,0,0,'2023-06-27T05:46:24Z',''),
        ('plurigrid/post-web','Svelte',0,0,0,'2023-06-18T00:24:24Z',''),
        ('plurigrid/microworlds','Rust',3,5,3,'2023-05-13T03:54:56Z',''),
        ('plurigrid/pills',None,0,0,0,'2023-05-02T10:03:03Z','metaphors for embodied gradualism'),
        ('plurigrid/plurigrid-rs','Rust',0,0,0,'2023-04-21T01:02:56Z',''),
        ('plurigrid/plurigrid-game.github.io','HTML',0,0,1,'2023-04-20T00:17:55Z',''),
        ('plurigrid/synth','Rust',0,0,0,'2023-04-15T01:56:45Z',''),
        ('plurigrid/birbs','C++',0,0,0,'2023-04-15T01:56:32Z','Build native CosmWasm apps with Dart and Flutter'),
        ('plurigrid/agent','Python',5,1,6,'2023-03-31T18:45:23Z','Framework for agency amplification'),
        ('plurigrid/vcg-auction','Rust',7,2,1,'2023-03-16T21:53:08Z','simple contract that performs a VCG auction'),
        ('plurigrid/bidder','Dart',0,0,1,'2023-03-15T15:23:22Z','flutter app for bidding in vcg auction'),
        ('plurigrid/plurigrid.github.io','HTML',1,2,2,'2023-01-20T03:27:34Z',''),
        ('plurigrid/VPP','Julia',0,1,0,'2023-01-11T18:41:07Z','Hyperreal Power Plant'),
        ('plurigrid/grid','TypeScript',2,1,1,'2023-01-02T11:55:55Z','Plurigrid Testnet #0: Edith Clarke'),
        ('plurigrid/commons-contracts','Rust',0,0,0,'2022-09-09T09:20:11Z','CosmWasm contracts to implement Commons Stack'),
        ('plurigrid/plurigrid.xyz','TypeScript',0,0,1,'2022-08-31T05:26:14Z',''),
    ]),
    "kubeflow": ("org", [
        ('kubeflow/pipelines','Python',4153,2006,494,'2026-06-06T11:07:54Z','Machine Learning Pipelines for Kubeflow'),
        ('kubeflow/notebooks',None,73,118,182,'2026-06-06T01:03:23Z','Kubeflow Notebooks interactive development environments'),
        ('kubeflow/community','Jupyter Notebook',194,257,15,'2026-06-05T17:29:18Z','Information about the Kubeflow community'),
        ('kubeflow/manifests','YAML',1020,1065,22,'2026-06-05T14:42:22Z','Kubeflow Community Distribution'),
        ('kubeflow/hub','Go',175,182,44,'2026-06-05T15:39:48Z','Model Registry for ML model developers'),
        ('kubeflow/trainer','Go',2112,964,123,'2026-06-05T03:17:48Z','Distributed AI Model Training and LLM Fine-Tuning'),
        ('kubeflow/website','HTML',184,921,46,'2026-06-05T02:01:44Z','Kubeflow Website'),
        ('kubeflow/kale','Python',691,155,48,'2026-06-05T21:02:41Z','Kubeflow superfood for Data Scientists'),
        ('kubeflow/spark-operator','Python',3125,1488,99,'2026-06-04T17:55:40Z','Kubernetes operator for Apache Spark'),
        ('kubeflow/mcp-apache-spark-history-server','Python',174,62,22,'2026-06-04T17:24:33Z','MCP Server and CLI for Apache Spark History Server'),
        ('kubeflow/dashboard','TypeScript',16,57,73,'2026-06-05T19:15:56Z','Kubeflow Central Dashboard'),
        ('kubeflow/katib','Python',1685,526,120,'2026-06-05T23:23:35Z','Automated Machine Learning on Kubernetes'),
        ('kubeflow/sdk','Python',120,181,137,'2026-06-04T03:07:45Z','Universal Python SDK for AI workloads on Kubernetes'),
        ('kubeflow/internal-acls','Go',19,388,2,'2026-06-01T16:22:32Z','Repository for group ACLs'),
        ('kubeflow/mpi-operator','Go',528,235,103,'2026-06-02T14:30:58Z','Kubernetes Operator for MPI-based applications'),
        ('kubeflow/pipelines-components','Python',11,43,33,'2026-06-04T17:39:10Z','Kubeflow Pipelines'),
        ('kubeflow/mlflow-integration','Python',6,4,2,'2026-05-27T15:42:37Z',''),
        ('kubeflow/blog','Jupyter Notebook',32,62,26,'2026-05-25T13:02:24Z','Kubeflow blog based on fastpages'),
        ('kubeflow/kubeflow',None,15706,2671,3,'2026-05-24T11:31:41Z','Machine Learning Toolkit for Kubernetes'),
        ('kubeflow/mcp-server','Python',10,19,25,'2026-05-12T10:14:24Z','MCP Server for AI-Assisted Development with Kubeflow'),
        ('kubeflow/arena','Go',811,191,46,'2026-05-07T06:46:17Z','A CLI for Kubeflow'),
        ('kubeflow/docs-agent','Python',37,94,151,'2026-04-14T03:33:15Z','Kubeflow Documentation AI Agent'),
        ('kubeflow/examples','Jsonnet',1462,756,111,'2025-04-14T01:54:52Z','Extended examples and tutorials'),
        ('kubeflow/testing','Python',60,86,33,'2025-02-14T18:33:13Z','Test infrastructure and tooling'),
        ('kubeflow/kfp-tekton','TypeScript',182,123,79,'2024-11-19T12:23:51Z','Kubeflow Pipelines on Tekton'),
        ('kubeflow/kfserving-lts','Jsonnet',12,19,51,'2024-08-02T16:25:44Z',''),
        ('kubeflow/kubebench','Jsonnet',78,35,68,'2024-06-17T19:22:04Z','Repository for benchmarking'),
        ('kubeflow/fate-operator','Go',51,15,6,'2024-02-22T19:44:08Z','Fate operator'),
        ('kubeflow/kfctl','Go',182,134,94,'2023-08-15T20:19:22Z','CLI for deploying and managing Kubeflow'),
        ('kubeflow/kfp-tekton-backend','TypeScript',8,6,46,'2023-08-14T22:05:04Z','Experimental Tekton yaml behind KFP API'),
        ('kubeflow/common','Go',53,70,40,'2023-05-28T13:16:00Z','Common APIs and libraries for Kubeflow operators'),
        ('kubeflow/fairing','Jsonnet',337,143,134,'2022-04-11T05:28:47Z','Python SDK for building, training, and deploying ML'),
        ('kubeflow/xgboost-operator','Python',77,53,22,'2021-12-01T18:00:10Z','Incubating project for xgboost operator'),
        ('kubeflow/mxnet-operator','Go',52,33,9,'2021-12-01T17:47:19Z','Kubernetes operator for mxnet jobs'),
        ('kubeflow/pytorch-operator','Jsonnet',310,143,63,'2021-12-01T17:44:48Z','PyTorch on Kubernetes'),
        ('kubeflow/frontend','JavaScript',8,18,12,'2021-12-01T17:41:37Z','Repository for kubeflow frontend'),
        ('kubeflow/metadata','TypeScript',123,63,38,'2021-12-01T17:35:27Z','Repository for assets related to Metadata'),
        ('kubeflow/caffe2-operator','Go',16,12,2,'2021-12-01T01:58:06Z','Experimental repository for a caffe2 operator'),
        ('kubeflow/code-intelligence','Jupyter Notebook',56,20,64,'2021-12-01T01:52:58Z','ML-Powered Developer Tools using Kubeflow'),
        ('kubeflow/example-seldon','Jupyter Notebook',172,56,9,'2021-12-01T01:49:58Z','Example for end-to-end ML on Kubernetes'),
        ('kubeflow/batch-predict','Python',17,7,9,'2021-12-01T01:47:51Z','Repository for batch predict'),
        ('kubeflow/reporting','Jsonnet',2,5,1,'2021-12-01T01:42:32Z','Collecting and analyzing metrics about Kubeflow'),
        ('kubeflow/chainer-operator','Jsonnet',17,15,7,'2021-11-14T13:03:57Z','Repository for chainer operator'),
        ('kubeflow/crd-validation','Go',11,7,5,'2021-01-25T15:02:53Z','Validation Generation for Kubeflow CRD'),
        ('kubeflow/community-infra','Go',3,9,4,'2021-01-25T14:49:49Z','Declarative configurations for KF community infra'),
        ('kubeflow/.github',None,2,1,0,'2020-05-12T00:22:56Z','Org wide templates'),
        ('kubeflow/marketing-materials',None,4,4,4,'2019-07-19T13:57:15Z',''),
    ]),
    "TeglonLabs": ("org", [
        ('TeglonLabs/mathpix-gem','Ruby',2,0,11,'2026-01-01T12:13:13Z','Transform math images to LaTeX, chemistry to SMILES'),
        ('TeglonLabs/coin-flip-mcp','JavaScript',0,2,1,'2025-09-21T08:57:27Z','MCP server for flipping coins with random.org'),
        ('TeglonLabs/monad-mcp-server',None,0,0,0,'2025-05-14T11:36:14Z','Monad MCP Server'),
        ('TeglonLabs/topoi','Python',0,0,1,'2025-01-24T04:49:26Z',''),
    ]),
    "migalkin": ("user", [
        ('migalkin/kgcourse2021','HTML',25,9,0,'2025-08-04T03:01:46Z','Materials for Knowledge Graphs course'),
        ('migalkin/migalkin.github.io','JavaScript',0,0,0,'2025-01-22T04:53:51Z','Github Pages for academic personal website'),
        ('migalkin/NBFNet_mlx','Python',10,1,1,'2024-03-02T00:15:23Z','Neural Bellman-Ford networks in MLX for Apple Silicon'),
        ('migalkin/StarE','Python',89,16,1,'2023-12-01T20:12:24Z','EMNLP 2020: Message Passing for Hyper-Relational KGs'),
        ('migalkin/rambo','Rust',3,0,1,'2023-02-08T14:27:03Z',''),
        ('migalkin/ciss2_project','Jupyter Notebook',0,0,6,'2022-12-08T05:50:27Z',''),
        ('migalkin/RWL','Python',8,1,0,'2022-12-01T15:58:59Z','Weisfeiler and Leman Go Relational (LOG 2022)'),
        ('migalkin/NodePiece','Python',144,21,0,'2022-02-02T03:34:04Z','Compositional representations for Large KGs'),
        ('migalkin/SQuAD-es-mt',None,0,1,0,'2020-07-14T17:13:08Z','Spanish SQuAD via machine translation'),
        ('migalkin/netquery_rdf','Python',0,0,0,'2019-06-01T12:49:16Z','NIPS 2018 paper fork for RDF'),
        ('migalkin/edbt-experiments',None,0,0,0,'2017-11-23T15:27:49Z',''),
        ('migalkin/SMJoin-experiments','R',1,0,0,'2017-06-06T12:20:23Z','ISWC 2017 SMJoin results'),
        ('migalkin/ekgs_clustering','Python',0,0,0,'2016-08-28T16:28:02Z',''),
        ('migalkin/r_energyConsumption','R',0,0,0,'2016-05-12T21:00:16Z',''),
        ('migalkin/ontologies','Web Ontology Language',0,0,0,'2015-12-06T13:49:53Z',''),
        ('migalkin/Tables_Provider','Java',0,0,0,'2015-03-20T00:17:35Z',''),
        ('migalkin/datasciencecoursera',None,0,0,0,'2015-02-13T00:04:31Z','Coursera Data Science course'),
        ('migalkin/InformationWorkbenchTestSrc','Java',0,0,0,'2013-06-22T15:46:54Z',''),
        ('migalkin/LinkedData',None,0,0,0,'2013-05-20T07:43:46Z','Information Workbench + Linked Open Data'),
    ]),
    "DJedamski": ("user", [
        ('DJedamski/kaggle_ncaa18','Jupyter Notebook',0,0,0,'2018-03-07T12:36:09Z','NCAA March Madness competition (2018)'),
        ('DJedamski/Project_Euler',None,0,0,0,'2015-10-14T02:10:45Z',''),
        ('DJedamski/EDA','R',0,0,0,'2014-11-09T16:51:34Z','Coursera Project'),
        ('DJedamski/Kaggle',None,1,0,0,'2014-11-03T02:22:01Z',''),
        ('DJedamski/Getting-and-Cleaning-Data','R',1,0,0,'2014-10-26T20:53:14Z','Coursera Project'),
        ('DJedamski/School','R',1,1,0,'2014-10-09T02:55:13Z','Small projects from grad school'),
    ]),
    "wasita": ("user", [
        ('wasita/wasita.github.io','Svelte',1,0,8,'2026-06-01T04:15:56Z','personal website'),
        ('wasita/wm-cv','Svelte',0,0,0,'2026-05-13T05:29:04Z','Academic CV as single page web app'),
        ('wasita/vocoder','JavaScript',0,0,0,'2026-05-06T05:14:00Z',''),
        ('wasita/ch3-lib','Typst',0,0,0,'2026-04-12T04:03:19Z',''),
        ('wasita/magic-garden','Python',2,1,1,'2026-01-13T23:51:32Z','bot for magic garden discord activity game'),
        ('wasita/proj-template',None,0,0,0,'2026-01-09T20:55:42Z',''),
        ('wasita/food-diary','Svelte',0,0,0,'2025-12-13T01:06:39Z',''),
        ('wasita/send2kobo','TypeScript',1,0,0,'2025-12-12T19:09:12Z','Website for sending books to kobo e-reader'),
        ('wasita/d60-keeb',None,0,0,0,'2024-08-26T00:46:22Z',''),
        ('wasita/wins-search','CSS',1,0,0,'2022-12-14T22:17:32Z','Women in Network Science member list website'),
        ('wasita/honeycomb-demo','JavaScript',0,0,0,'2021-12-07T21:38:28Z',''),
    ]),
    "kristinezheng": ("user", [
        ('kristinezheng/kristinezheng.github.io','HTML',0,0,0,'2026-05-14T22:28:57Z',''),
        ('kristinezheng/lookit-jenga','Jupyter Notebook',0,0,0,'2024-05-16T18:29:01Z','Lookit study for 9.85'),
        ('kristinezheng/auditory-illusion','CSS',0,0,0,'2022-03-11T19:22:33Z','9.35 spring 2022 auditory illusion'),
        ('kristinezheng/graph_example','Python',0,0,0,'2021-10-08T07:29:51Z',''),
        ('kristinezheng/Green-Machine','Python',0,0,0,'2021-09-19T05:33:01Z','HackMIT 2021: Sustainability Track'),
    ]),
    "M1shaaa": ("user", [
        ('M1shaaa/M1shaaa',None,0,0,0,'2026-06-07T03:33:05Z','Config files for GitHub profile'),
        ('M1shaaa/lab-bookshelf-','TypeScript',0,0,0,'2024-12-31T05:11:14Z',''),
        ('M1shaaa/rosie-s-study-3-lookit-project',None,0,0,0,'2024-11-04T22:15:35Z',''),
        ('M1shaaa/Python-Lookit-Uploads','Python',0,0,0,'2024-02-16T15:20:50Z','random projects'),
        ('M1shaaa/Classes',None,0,0,0,'2023-12-07T08:16:20Z',''),
        ('M1shaaa/Yale-Work','HTML',0,0,0,'2023-12-06T18:33:10Z',''),
        ('M1shaaa/MNIST-Classifier',None,0,0,0,'2023-11-28T06:12:13Z',''),
        ('M1shaaa/Lookit-Demo',None,0,0,0,'2023-04-10T02:50:03Z',''),
    ]),
    "AustinCStone": ("user", [
        ('AustinCStone/EpsteinSearch','Python',0,0,0,'2026-02-11T01:10:54Z',''),
        ('AustinCStone/bmforkupdate','Python',0,0,0,'2025-05-09T04:49:24Z',''),
        ('AustinCStone/bmfork','Python',0,0,1,'2025-05-09T04:17:17Z',''),
        ('AustinCStone/bitmind-fork',None,0,0,0,'2025-01-09T06:16:51Z','forked on jan 8 2025'),
        ('AustinCStone/testLogin','Python',0,0,0,'2023-02-13T20:52:23Z',''),
        ('AustinCStone/austincstone.github.io','HTML',0,0,0,'2021-10-23T22:48:46Z',''),
        ('AustinCStone/test',None,0,0,0,'2021-09-21T21:15:51Z',''),
        ('AustinCStone/stonks','Python',0,0,0,'2020-09-04T22:54:33Z','Playing around with option calculations'),
        ('AustinCStone/Z-order-curve','Python',0,0,0,'2019-06-09T02:53:41Z','Demo implementation of space filling z-order curve'),
        ('AustinCStone/LensBuilder','Python',0,0,0,'2019-04-04T04:28:05Z','WIP optimize for surface of a focusing lens'),
        ('AustinCStone/TFBirds','Python',0,0,0,'2019-01-30T08:07:21Z','Bird flocking simulator in TensorFlow'),
        ('AustinCStone/StructureFromMotion','Python',1,0,0,'2018-06-10T18:56:16Z','Recover 3D geometry from videos'),
        ('AustinCStone/OptimalControl','Python',0,0,0,'2018-02-19T23:13:55Z','Practicing concepts from control theory'),
        ('AustinCStone/LearningCuda','C',0,0,0,'2017-11-05T23:48:04Z','Working through CUDA by example'),
        ('AustinCStone/TextGAN','Python',92,30,5,'2016-10-04T03:19:12Z','GAN for text generation in TensorFlow'),
        ('AustinCStone/StereoVisionMRF','Python',11,4,0,'2016-01-10T08:34:29Z','MRF with loopy belief propagation for stereo depth'),
        ('AustinCStone/SpectralClustering','Python',3,2,0,'2015-11-09T03:27:15Z','Implementing spectral clustering for grad school'),
        ('AustinCStone/statsHw2','Python',0,0,0,'2015-09-28T15:56:31Z','Simple linear regression and model selection'),
        ('AustinCStone/StatsModelingHw1','Python',0,0,0,'2015-09-19T04:13:52Z','First homework for statistical modeling'),
        ('AustinCStone/ConvNet','Python',0,0,0,'2015-09-08T00:43:12Z','Deep CNN for MNIST classification'),
        ('AustinCStone/TheanoStuff','Python',0,0,0,'2015-09-04T02:14:00Z','Getting acquainted with Theano'),
        ('AustinCStone/bash_profile',None,0,0,0,'2015-08-26T17:59:50Z','bash profile'),
        ('AustinCStone/Founderati-Server','Python',0,1,0,'2015-08-25T19:17:44Z','Server for Founderati'),
        ('AustinCStone/Founderati-client','JavaScript',0,1,0,'2015-08-25T19:16:57Z','AngelList/LinkedIn-inspired network'),
        ('AustinCStone/logisticRegressionHaskell','Haskell',1,0,0,'2015-06-07T19:37:42Z','Logistic regression in Haskell for MNIST'),
        ('AustinCStone/Genetic-Algorithm-Sorting-Network','Python',0,0,0,'2015-05-12T19:30:48Z',''),
        ('AustinCStone/RealTimeRayTracingFractalWorld','C++',0,0,0,'2015-05-11T02:03:41Z','Real time ray tracing of fractal world'),
        ('AustinCStone/gibbs_sampling','Python',0,0,0,'2015-04-09T03:27:15Z','Proof of concept of gibbs sampling convergence'),
        ('AustinCStone/lexer','C',0,0,0,'2015-02-09T22:45:55Z','A lexer for prolog'),
        ('AustinCStone/HTTPCache','Java',0,0,0,'2015-02-05T22:04:01Z','URL response caching for GET requests'),
    ]),
}

inc_id = 1
repo_id = 1

for source_name, (source_type, repos) in sources.items():
    trit, color, name = gf3(inc_id)
    snap_hash = sha8(f"{source_name}:{NOW}")
    con.execute("""
        INSERT INTO world_increments VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [inc_id, NOW, trit, color, name, source_type, source_name,
          "repo_sweep", None, None, snap_hash])

    for repo in repos:
        full_name, language, stars, forks, issues, pushed_at, desc = repo
        org_or_user = full_name.split('/')[0]
        repo_name = full_name.split('/')[1]
        con.execute("""
            INSERT INTO repo_snapshots VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, [repo_id, NOW, inc_id, org_or_user, repo_name, full_name,
              language, stars, forks, issues, pushed_at, desc])
        repo_id += 1

    inc_id += 1

print(f"Inserted {inc_id-1} world_increments, {repo_id-1} repo_snapshots")

# ─── APTOS SNAPSHOTS ─────────────────────────────────────────────────────────
aptos_data = [
    ("alice", "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b", 0.0),
    ("bob",   "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d", 0.0),
    ("A",     "0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a", 0.0),
    ("B",     "0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13", 0.0),
    ("C",     "0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e", 0.0),
    ("D",     "0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1", 0.0),
    ("E",     "0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36", 0.0),
    ("F",     "0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71", 0.0),
    ("G",     "0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32", 0.0),
    ("H",     "0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f", 0.0),
    ("I",     "0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9", 0.0),
    ("J",     "0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54", 0.0),
    ("K",     "0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4", 0.0),
    ("L",     "0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9", 0.0),
    ("M",     "0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9", 0.0),
    ("N",     "0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c", 0.0),
    ("O",     "0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d", 0.0),
    ("P",     "0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948", 0.0),
    ("Q",     "0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9", 0.0),
    ("R",     "0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10", 0.0),
    ("S",     "0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386", 0.0),
    ("T",     "0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588", 0.0),
    ("U",     "0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956", 0.0),
    ("V",     "0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3", 0.0),
    ("W",     "0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0", 0.0),
    ("X",     "0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d", 0.0),
    ("Y",     "0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4", 0.0),
    ("Z",     "0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c", 0.0),
]
for world, addr, bal in aptos_data:
    con.execute("INSERT INTO aptos_snapshots VALUES (?, ?, ?, ?)",
                [NOW, world, addr, bal])
print(f"Inserted {len(aptos_data)} aptos_snapshots")

# ─── MULTISIG PROBES ─────────────────────────────────────────────────────────
multisigs = [
    ("A-B",  "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2, True),
    ("A-G",  "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2, True),
    ("Y-Z",  "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2, True),
    ("S-T",  "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2, True),
    ("V-W",  "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2, True),
]
for pair, addr, sigs, healthy in multisigs:
    con.execute("INSERT INTO multisig_probes VALUES (?, ?, ?, ?, ?)",
                [NOW, pair, addr, sigs, healthy])
print(f"Inserted {len(multisigs)} multisig_probes (all healthy, 2-of-2)")

# ─── MNX (unavailable) ───────────────────────────────────────────────────────
print("MNX testnet.mnx.fi: Vercel authentication wall — no data inserted")

# ─── VERIFY ──────────────────────────────────────────────────────────────────
total_repos = con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0]
total_incs  = con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0]
total_aptos = con.execute("SELECT COUNT(*) FROM aptos_snapshots").fetchone()[0]
total_multi = con.execute("SELECT COUNT(*) FROM multisig_probes").fetchone()[0]

print(f"\nDB Summary:")
print(f"  world_increments: {total_incs}")
print(f"  repo_snapshots:   {total_repos}")
print(f"  aptos_snapshots:  {total_aptos}")
print(f"  multisig_probes:  {total_multi}")

# GF3 chain distribution
gf3_dist = con.execute("""
    SELECT gf3_name, gf3_color, COUNT(*) as cnt
    FROM world_increments GROUP BY gf3_name, gf3_color ORDER BY gf3_name
""").fetchall()
print("\nGF(3) chain distribution:")
for row in gf3_dist:
    print(f"  {row[0]} {row[1]}: {row[2]}")

con.close()
print("\nDuckDB written successfully.")
