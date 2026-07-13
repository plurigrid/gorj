#!/usr/bin/env python3
"""World-increment sweep + Hamming swarm snapshot builder."""
import duckdb, json, os, hashlib
from datetime import datetime, timezone

DB_PATH = os.path.join(os.path.dirname(__file__), "world-increments.duckdb")
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
con.execute("CREATE SEQUENCE IF NOT EXISTS increment_seq START 1")
con.execute("CREATE SEQUENCE IF NOT EXISTS repo_seq START 1")

TS = datetime.now(timezone.utc).isoformat()

def gf3(n):
    trit = n % 3
    if trit == 0: return (0, "#d3869b", "ERGODIC")
    if trit == 1: return (1, "#b8bb26", "PLUS")
    return (-1, "#cc241d", "MINUS")

def next_inc_id():
    return con.execute("SELECT nextval('increment_seq')").fetchone()[0]

def next_repo_id():
    return con.execute("SELECT nextval('repo_seq')").fetchone()[0]

def snap_hash(data):
    return hashlib.md5(json.dumps(data, sort_keys=True, default=str).encode()).hexdigest()[:12]

# ─── REPO DATA ────────────────────────────────────────────────────────────────

plurigrid_repos = [
  {"full_name":"plurigrid/asi","language":"HTML","stargazers_count":30,"forks_count":10,"open_issues_count":4,"pushed_at":"2026-07-10T09:47:39Z","description":"everything is topological chemputer!"},
  {"full_name":"plurigrid/gorj","language":"Clojure","stargazers_count":1,"forks_count":0,"open_issues_count":1146,"pushed_at":"2026-07-13T06:15:10Z","description":"forj + Rama topology nREPL routing + GF(3) gay trit coloring"},
  {"full_name":"plurigrid/shrimp","language":None,"stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-07-03T01:24:20Z","description":"Jank worked example: shrimp"},
  {"full_name":"plurigrid/place","language":"TeX","stargazers_count":1,"forks_count":1,"open_issues_count":12,"pushed_at":"2026-07-07T03:10:28Z","description":None},
  {"full_name":"plurigrid/eirobri","language":"Clojure","stargazers_count":0,"forks_count":0,"open_issues_count":30,"pushed_at":"2026-06-30T02:23:56Z","description":"EiRoBri replay world"},
  {"full_name":"plurigrid/nash-portal","language":"Rust","stargazers_count":2,"forks_count":3,"open_issues_count":1,"pushed_at":"2026-05-19T01:49:59Z","description":"NASH token TUI — ratzilla WASM + GeckoTerminal OHLCV candlesticks"},
  {"full_name":"plurigrid/zig-syrup","language":"Zig","stargazers_count":2,"forks_count":2,"open_issues_count":0,"pushed_at":"2026-04-30T03:52:16Z","description":"High-performance Zig implementation of OCapN Syrup"},
  {"full_name":"plurigrid/asi-skills","language":"Julia","stargazers_count":3,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-26T08:09:26Z","description":"69 skills with Galois Hole Type accessibility"},
  {"full_name":"plurigrid/bci-blue-share","language":"JavaScript","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-26T07:08:03Z","description":"BCI signal infrastructure"},
  {"full_name":"plurigrid/nanoclj-zig","language":"Zig","stargazers_count":1,"forks_count":1,"open_issues_count":20,"pushed_at":"2026-04-25T07:29:09Z","description":"NaN-boxed Clojure interpreter in Zig 0.15"},
  {"full_name":"plurigrid/spi-race","language":"Swift","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-21T19:31:56Z","description":"Splitmix Parallel Integrity"},
  {"full_name":"plurigrid/reafference","language":"HTML","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-16T05:21:49Z","description":"Reafference adaptation workspace"},
  {"full_name":"plurigrid/web-browser","language":"Rust","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-10T02:54:47Z","description":"web-browser — from prepostweb lineage"},
  {"full_name":"plurigrid/vivarium","language":"Clojure","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-08T08:38:37Z","description":None},
  {"full_name":"plurigrid/gatomic","language":"Clojure","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-30T00:54:48Z","description":"Deterministic color identity store — Gay + Datomic + Atomic"},
  {"full_name":"plurigrid/forester","language":"XSLT","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-30T01:32:26Z","description":"CatColab mathematical documentation forest"},
  {"full_name":"plurigrid/nblm-flashcards","language":"Hy","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-26T08:23:01Z","description":"NotebookLM Enterprise flashcard pipeline"},
  {"full_name":"plurigrid/graded-optic","language":"Haskell","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-02-08T16:10:16Z","description":"Semiring-graded bidirectional processes"},
  {"full_name":"plurigrid/json-canvas","language":None,"stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-02-06T06:50:57Z","description":"JSON Canvas: Real-time interaction data capture via W3C JSON-LD 1.1"},
  {"full_name":"plurigrid/shepherd","language":"Scheme","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-01-23T07:47:28Z","description":"Spritely Shepherd - Service manager"},
  {"full_name":"plurigrid/hoot","language":"Scheme","stargazers_count":0,"forks_count":0,"open_issues_count":1,"pushed_at":"2026-01-23T07:47:10Z","description":"Spritely Hoot - Scheme to WebAssembly compiler"},
  {"full_name":"plurigrid/leprechauns","language":"Racket","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-01-23T07:46:46Z","description":"Spritely Goblins + Gay.jl semantic colors"},
]

kubeflow_repos = [
  {"full_name":"kubeflow/sdk","language":"Python","stargazers_count":124,"forks_count":195,"open_issues_count":152,"pushed_at":"2026-07-13T00:57:45Z","description":"Universal Python SDK to run AI workloads on Kubernetes"},
  {"full_name":"kubeflow/mcp-server","language":"Python","stargazers_count":22,"forks_count":30,"open_issues_count":38,"pushed_at":"2026-07-12T20:36:22Z","description":"MCP Server for AI-Assisted Development with Kubeflow Tools"},
  {"full_name":"kubeflow/community-distribution","language":"YAML","stargazers_count":1029,"forks_count":1071,"open_issues_count":29,"pushed_at":"2026-07-12T16:28:39Z","description":"Kubeflow Community Distribution"},
  {"full_name":"kubeflow/pipelines","language":"Python","stargazers_count":4168,"forks_count":2031,"open_issues_count":420,"pushed_at":"2026-07-12T07:25:10Z","description":"Machine Learning Pipelines for Kubeflow"},
  {"full_name":"kubeflow/spark-operator","language":"Python","stargazers_count":3137,"forks_count":1500,"open_issues_count":109,"pushed_at":"2026-07-12T01:14:02Z","description":"Kubernetes operator for managing Apache Spark applications"},
  {"full_name":"kubeflow/docs-agent","language":"Python","stargazers_count":39,"forks_count":98,"open_issues_count":158,"pushed_at":"2026-07-11T16:56:46Z","description":"Kubeflow Documentation AI Agent"},
  {"full_name":"kubeflow/community","language":"Jupyter Notebook","stargazers_count":195,"forks_count":265,"open_issues_count":14,"pushed_at":"2026-07-11T02:36:27Z","description":"Information about the Kubeflow community"},
  {"full_name":"kubeflow/kale","language":"Python","stargazers_count":695,"forks_count":157,"open_issues_count":44,"pushed_at":"2026-07-10T22:35:31Z","description":"Kubeflow's superfood for Data Scientists"},
  {"full_name":"kubeflow/hub","language":"Go","stargazers_count":177,"forks_count":188,"open_issues_count":40,"pushed_at":"2026-07-10T22:24:45Z","description":"Model Registry for ML model developers"},
  {"full_name":"kubeflow/katib","language":"Python","stargazers_count":1690,"forks_count":533,"open_issues_count":109,"pushed_at":"2026-07-10T16:05:23Z","description":"Automated Machine Learning on Kubernetes"},
  {"full_name":"kubeflow/mpi-operator","language":"Go","stargazers_count":529,"forks_count":237,"open_issues_count":100,"pushed_at":"2026-07-10T14:12:52Z","description":"Kubernetes operator for MPI-based applications"},
  {"full_name":"kubeflow/kubeflow","language":None,"stargazers_count":15772,"forks_count":2685,"open_issues_count":0,"pushed_at":"2026-07-10T11:31:26Z","description":"Machine Learning Toolkit for Kubernetes"},
  {"full_name":"kubeflow/trainer","language":"Go","stargazers_count":2137,"forks_count":984,"open_issues_count":146,"pushed_at":"2026-07-10T10:02:33Z","description":"Distributed AI Model Training and LLM Fine-Tuning on Kubernetes"},
  {"full_name":"kubeflow/arena","language":"Go","stargazers_count":815,"forks_count":195,"open_issues_count":49,"pushed_at":"2026-07-10T13:17:48Z","description":"A CLI for Kubeflow"},
  {"full_name":"kubeflow/dashboard","language":"TypeScript","stargazers_count":16,"forks_count":60,"open_issues_count":89,"pushed_at":"2026-07-10T19:39:47Z","description":"Kubeflow Central Dashboard"},
  {"full_name":"kubeflow/mcp-apache-spark-history-server","language":"Python","stargazers_count":182,"forks_count":65,"open_issues_count":19,"pushed_at":"2026-06-25T20:28:43Z","description":"MCP Server for Apache Spark History Server"},
  {"full_name":"kubeflow/notebooks","language":None,"stargazers_count":73,"forks_count":128,"open_issues_count":178,"pushed_at":"2026-07-12T01:41:06Z","description":"Kubeflow Notebooks for AI/ML/Data workloads"},
  {"full_name":"kubeflow/mlflow-integration","language":"Python","stargazers_count":6,"forks_count":7,"open_issues_count":6,"pushed_at":"2026-07-09T14:25:31Z","description":None},
  {"full_name":"kubeflow/website","language":"HTML","stargazers_count":184,"forks_count":926,"open_issues_count":36,"pushed_at":"2026-07-10T15:30:48Z","description":"Kubeflow Website"},
  {"full_name":"kubeflow/blog","language":"Jupyter Notebook","stargazers_count":32,"forks_count":62,"open_issues_count":26,"pushed_at":"2026-06-11T16:32:01Z","description":"Kubeflow blog"},
  {"full_name":"kubeflow/internal-acls","language":"Go","stargazers_count":19,"forks_count":395,"open_issues_count":5,"pushed_at":"2026-07-12T04:56:02Z","description":"Group ACLs for Kubeflow developers"},
  {"full_name":"kubeflow/pipelines-components","language":"Python","stargazers_count":11,"forks_count":47,"open_issues_count":37,"pushed_at":"2026-07-10T21:51:03Z","description":"Kubeflow Pipelines"},
  {"full_name":"kubeflow/.project","language":None,"stargazers_count":0,"forks_count":0,"open_issues_count":1,"pushed_at":"2026-07-05T14:52:37Z","description":"Project metadata for Kubeflow"},
]

teglon_repos = [
  {"full_name":"TeglonLabs/jank-crane","language":"C++","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-06-08T19:03:03Z","description":"crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps"},
  {"full_name":"TeglonLabs/mathpix-gem","language":"Ruby","stargazers_count":2,"forks_count":0,"open_issues_count":11,"pushed_at":"2026-01-01T12:13:13Z","description":"Mathematical images to LaTeX, chemistry to SMILES, documents to markdown"},
  {"full_name":"TeglonLabs/coin-flip-mcp","language":"JavaScript","stargazers_count":0,"forks_count":2,"open_issues_count":1,"pushed_at":"2025-09-21T08:57:27Z","description":"MCP server for flipping coins with varying degrees of randomness"},
  {"full_name":"TeglonLabs/monad-mcp-server","language":None,"stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-05-14T11:36:14Z","description":"Monad MCP Server"},
  {"full_name":"TeglonLabs/topoi","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":1,"pushed_at":"2025-01-24T04:49:26Z","description":None},
]

# Social graph
migalkin_repos = [
  {"full_name":"migalkin/NodePiece","language":"Python","stargazers_count":144,"forks_count":21,"open_issues_count":0,"pushed_at":"2026-05-07T05:40:02Z","description":"Compositional and Parameter-Efficient Representations for Large Knowledge Graphs (ICLR'22)"},
  {"full_name":"migalkin/StarE","language":"Python","stargazers_count":89,"forks_count":16,"open_issues_count":1,"pushed_at":"2026-04-16T14:12:45Z","description":"EMNLP 2020: Message Passing for Hyper-Relational Knowledge Graphs"},
  {"full_name":"migalkin/kgcourse2021","language":"HTML","stargazers_count":24,"forks_count":8,"open_issues_count":0,"pushed_at":"2026-07-10T15:40:00Z","description":"Материалы к курсу по Knowledge Graphs"},
  {"full_name":"migalkin/NBFNet_mlx","language":"Python","stargazers_count":10,"forks_count":1,"open_issues_count":1,"pushed_at":"2026-03-11T01:31:21Z","description":"Neural Bellman-Ford networks in MLX for Apple Silicon"},
  {"full_name":"migalkin/RWL","language":"Python","stargazers_count":8,"forks_count":1,"open_issues_count":0,"pushed_at":"2026-05-28T20:19:20Z","description":"Weisfeiler and Leman Go Relational (LOG 2022)"},
  {"full_name":"migalkin/rambo","language":"Rust","stargazers_count":3,"forks_count":0,"open_issues_count":1,"pushed_at":"2023-02-28T16:37:22Z","description":None},
]

djedamski_repos = [
  {"full_name":"DJedamski/kaggle_ncaa18","language":"Jupyter Notebook","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2018-02-26T16:33:24Z","description":"Code for NCAA March Madness competition (2018)"},
  {"full_name":"DJedamski/Kaggle","language":None,"stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2023-04-21T01:42:35Z","description":None},
  {"full_name":"DJedamski/School","language":"R","stargazers_count":1,"forks_count":1,"open_issues_count":0,"pushed_at":"2023-04-21T01:42:33Z","description":"A couple small projects from grad school"},
]

wasita_repos = [
  {"full_name":"wasita/wasita.github.io","language":"Svelte","stargazers_count":1,"forks_count":0,"open_issues_count":8,"pushed_at":"2026-07-06T23:51:09Z","description":"personal website"},
  {"full_name":"wasita/magic-garden","language":"Python","stargazers_count":2,"forks_count":1,"open_issues_count":1,"pushed_at":"2026-04-22T21:16:43Z","description":"bot for magic garden discord activity game"},
  {"full_name":"wasita/send2kobo","language":"TypeScript","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-05-19T02:59:26Z","description":"Website for sending books to kobo e-reader"},
  {"full_name":"wasita/wm-cv","language":"Svelte","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-05-13T05:29:08Z","description":"Academic CV as single page web app"},
]

kristinezheng_repos = [
  {"full_name":"kristinezheng/kristinezheng.github.io","language":"HTML","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-07-01T20:57:48Z","description":None},
  {"full_name":"kristinezheng/lookit-jenga","language":"Jupyter Notebook","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2024-05-16T18:29:05Z","description":"Lookit study for 9.85"},
]

m1shaaa_repos = [
  {"full_name":"M1shaaa/M1shaaa","language":None,"stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-02-04T19:32:04Z","description":"Config files for GitHub profile"},
  {"full_name":"M1shaaa/lab-bookshelf-","language":"TypeScript","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2024-12-31T05:11:18Z","description":None},
]

austincstone_repos = [
  {"full_name":"AustinCStone/TextGAN","language":"Python","stargazers_count":92,"forks_count":30,"open_issues_count":5,"pushed_at":"2025-03-03T13:26:32Z","description":"A generative adversarial network for text generation, in TensorFlow"},
  {"full_name":"AustinCStone/EpsteinSearch","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-02-11T01:10:57Z","description":None},
  {"full_name":"AustinCStone/bmforkupdate","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-05-09T04:50:16Z","description":None},
  {"full_name":"AustinCStone/StructureFromMotion","language":"Python","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2019-04-26T19:43:12Z","description":"Recover 3D geometry from videos with unknown camera calibration"},
]

bmorphism_repos = [
  {"full_name":"bmorphism/Gay.jl","language":"Julia","stargazers_count":2,"forks_count":1,"open_issues_count":187,"pushed_at":"2026-07-13T00:30:18Z","description":"Wide-gamut color sampling with splittable determinism (Pigeons.jl SPI pattern) + LispSyntax"},
  {"full_name":"bmorphism/satreadout","language":"HTML","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-06-20T13:05:41Z","description":"Machine-checked saturating non-Riemannian perceptual readout — Lean 4.28 + mathlib"},
  {"full_name":"bmorphism/bci-preview","language":"HTML","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-06-20T00:20:44Z","description":"Stable redirect front for the bci.place forester preview"},
  {"full_name":"bmorphism/world","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-06-02T06:49:02Z","description":"Local worlds launcher for SA3, jank, and world proofs"},
  {"full_name":"bmorphism/oxgame","language":"OCaml","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-05-15T09:53:27Z","description":"Stellar resolution and open-game composition for OCaml"},
  {"full_name":"bmorphism/nanoclj-zig","language":"Zig","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-05-07T20:12:15Z","description":None},
  {"full_name":"bmorphism/zig-syrup","language":"Zig","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-05-07T19:49:05Z","description":"Embeddable OCapN Syrup encoder/decoder in Zig — 550 LOC, 22 tests"},
  {"full_name":"bmorphism/boxxy","language":"Move","stargazers_count":0,"forks_count":1,"open_issues_count":0,"pushed_at":"2026-04-30T03:35:47Z","description":None},
  {"full_name":"bmorphism/postweb","language":"Go","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-09T10:51:57Z","description":"postweb — evolved from prepostweb"},
  {"full_name":"bmorphism/shitcoin","language":"Python","stargazers_count":5,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-08T08:07:08Z","description":"gets denom for cw20 assets for permissionless degeneracy in IBC"},
  {"full_name":"bmorphism/magic-world-org","language":"Python","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-05T07:03:50Z","description":"Magic World Org (Local MLX)"},
  {"full_name":"bmorphism/ocaml-mcp-sdk","language":"OCaml","stargazers_count":61,"forks_count":2,"open_issues_count":0,"pushed_at":"2026-03-16T05:24:25Z","description":"OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect library"},
  {"full_name":"bmorphism/flox-mcp-bb","language":"Clojure","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-02-12T02:45:43Z","description":"Open-source MCP server for Flox — Babashka/Clojure, single file, 20 tools"},
  {"full_name":"bmorphism/vibesnipe-market","language":"Move","stargazers_count":0,"forks_count":1,"open_issues_count":9,"pushed_at":"2026-02-05T10:23:25Z","description":None},
  {"full_name":"bmorphism/anti-bullshit-mcp-server","language":"JavaScript","stargazers_count":22,"forks_count":7,"open_issues_count":1,"pushed_at":"2026-01-16T08:54:58Z","description":"MCP server for analyzing claims, validating sources, detecting manipulation"},
  {"full_name":"bmorphism/vibespace-mcp-go-ternary","language":"HTML","stargazers_count":0,"forks_count":1,"open_issues_count":3,"pushed_at":"2026-01-11T12:50:40Z","description":"Go MCP experience for vibes and worlds with NATS streaming and balanced ternary"},
  {"full_name":"bmorphism/open-location-code-zig","language":"Zig","stargazers_count":3,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-12-30T19:33:45Z","description":"Open Location Code (Plus Codes) for Zig — first Zig implementation"},
  {"full_name":"bmorphism/bafishka","language":"Clojure","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-12-19T09:38:00Z","description":"Rust-native Fish shell file operations with Steel-backed SCI Clojure"},
  {"full_name":"bmorphism/GeoACSets.jl","language":"Julia","stargazers_count":0,"forks_count":1,"open_issues_count":1,"pushed_at":"2026-01-19T13:57:13Z","description":"Categorical data structures (ACSets) with geospatial capabilities"},
  {"full_name":"bmorphism/gay-hy","language":"Hy","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-12-15T15:32:58Z","description":"Hylang MLX color bandwidth protocol — 2B+ colors/sec with SPI guarantees"},
  {"full_name":"bmorphism/multiverse-color-game","language":"Julia","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-12-12T05:28:11Z","description":"2+1D Holographic Color Matching Game — Hamkins multiverse + Gay.jl chromatic identity"},
  {"full_name":"bmorphism/monero-rental-hash-war","language":"Haskell","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-10-05T23:08:54Z","description":"Compositional OpenGame analysis of Monero rental hash war"},
]

zubyul_repos = [
  {"full_name":"zubyul/voice-observatory","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-24T05:56:17Z","description":"Passive macOS TUI observing voice-download pathways. Companion to bmorphism/say-mcp-server"},
  {"full_name":"zubyul/ghostel-emacs-worlds","language":"GLSL","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-24T00:20:56Z","description":"Ghostty config + ghostel family + alice/bob emacs-mods"},
  {"full_name":"zubyul/nash-tui","language":"Rust","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-13T07:45:16Z","description":"NASH token TUI: real-time candles, ticker, buy pressure gauge via GeckoTerminal"},
  {"full_name":"zubyul/nash-web","language":"Rust","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-13T07:08:58Z","description":"NASH token browser TUI via ratzilla WASM + GeckoTerminal OHLCV"},
  {"full_name":"zubyul/big-bad-plurigrid-quiz","language":"Emacs Lisp","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-09T18:51:31Z","description":"27 flashcards from bmorphism/plurigrid/zubyul/monaduck1069 activity + Emacs drill"},
  {"full_name":"zubyul/Gay.jl","language":"Julia","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-28T11:30:01Z","description":"Wide-gamut color sampling with splittable determinism + LispSyntax"},
  {"full_name":"zubyul/kinesis-kb360pro","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-26T10:29:40Z","description":"Claude Code skill for Kinesis Advantage360 Pro keyboard: KMonad string diagrams, GF(3) color"},
  {"full_name":"zubyul/gay-world","language":"Python","stargazers_count":1,"forks_count":1,"open_issues_count":0,"pushed_at":"2026-03-26T04:03:39Z","description":"Goblin world builder: MLX task decomposition → composable persistent worlds"},
  {"full_name":"zubyul/tilelang-kernels","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-16T02:31:13Z","description":"TileLang GPU kernels for SplitMix64 color generation, GF(3) trit classification, Sinkhorn OT"},
  {"full_name":"zubyul/fleet-bootstrap","language":"Shell","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-02-23T08:19:58Z","description":None},
  {"full_name":"zubyul/gay-terminal-colors","language":"Clojure","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-02-21T07:38:14Z","description":"SplitMix64 per-terminal color identity"},
  {"full_name":"zubyul/openbci-visualizer","language":"Zig","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-02-04T11:17:41Z","description":None},
  {"full_name":"zubyul/plurigrid-site","language":"Svelte","stargazers_count":0,"forks_count":1,"open_issues_count":11,"pushed_at":"2026-02-04T03:20:08Z","description":"Plurigrid world: site deployment"},
  {"full_name":"zubyul/vibesnipe","language":"Move","stargazers_count":0,"forks_count":0,"open_issues_count":1,"pushed_at":"2026-01-30T22:36:03Z","description":None},
  {"full_name":"zubyul/zubyul.github.io","language":"CSS","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-01-27T03:24:34Z","description":None},
  {"full_name":"zubyul/toad-warpify-extension","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-01-17T07:48:40Z","description":"Warpify extension for Toad — enables ACP agents to control terminal PTY directly"},
  {"full_name":"zubyul/GayMove","language":"Move","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-12-18T09:40:08Z","description":None},
  {"full_name":"zubyul/gay-brain-world","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-12-16T01:19:28Z","description":"Gay.jl SPI colors for Moduleur Brain (Pico) + OpenBCI EEG"},
  {"full_name":"zubyul/cat-world","language":"TypeScript","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-12-12T08:47:14Z","description":"Cat gaze tracker — tracks cat preferences for bird videos using eye detection"},
  {"full_name":"zubyul/hue-world","language":"JavaScript","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-12-12T08:32:59Z","description":"Terminal Vibe Snipe puzzle game with ANSI true color"},
  {"full_name":"zubyul/chromatic-vrf","language":"Kotlin","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-12-12T03:26:22Z","description":"Chromatic VRF: I Love Hue puzzle with Gay.jl MCMC and EG-Walker CRDT multiplayer"},
  {"full_name":"zubyul/quantum-telephone","language":"Jupyter Notebook","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-12-08T22:54:16Z","description":"Quantum telephone world: entangled message passing"},
]

SOURCES = [
  ("org",    "plurigrid",     plurigrid_repos),
  ("org",    "kubeflow",      kubeflow_repos),
  ("org",    "TeglonLabs",    teglon_repos),
  ("user",   "bmorphism",     bmorphism_repos),
  ("user",   "zubyul",        zubyul_repos),
  ("social", "migalkin",      migalkin_repos),
  ("social", "DJedamski",     djedamski_repos),
  ("social", "wasita",        wasita_repos),
  ("social", "kristinezheng", kristinezheng_repos),
  ("social", "M1shaaa",       m1shaaa_repos),
  ("social", "AustinCStone",  austincstone_repos),
]

# ─── INSERT REPOS ─────────────────────────────────────────────────────────────

for source_type, source_name, repos in SOURCES:
    for repo in repos:
        inc_id = next_inc_id()
        trit, color, name = gf3(inc_id)
        h = snap_hash(repo)
        con.execute("""
            INSERT INTO world_increments VALUES (?,?,?,?,?,?,?,?,?,?,?)
        """, [inc_id, TS, trit, color, name, source_type, source_name,
              "repo_snapshot", repo["full_name"], source_name, h])
        rid = next_repo_id()
        org = repo["full_name"].split("/")[0]
        con.execute("""
            INSERT INTO repo_snapshots VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
        """, [rid, TS, inc_id, org, repo["full_name"].split("/")[1],
              repo["full_name"], repo.get("language"),
              repo.get("stargazers_count", 0), repo.get("forks_count", 0),
              repo.get("open_issues_count", 0),
              repo.get("pushed_at"), repo.get("description")])

# ─── APTOS SNAPSHOTS ──────────────────────────────────────────────────────────

aptos_data = {
  "alice": {"address":"0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b","balance_apt":None},
  "bob":   {"address":"0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d","balance_apt":None},
  "A": {"address":"0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a","balance_apt":None},
  "B": {"address":"0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13","balance_apt":None},
  "C": {"address":"0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e","balance_apt":None},
  "D": {"address":"0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1","balance_apt":None},
  "E": {"address":"0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36","balance_apt":None},
  "F": {"address":"0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71","balance_apt":None},
  "G": {"address":"0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32","balance_apt":None},
  "H": {"address":"0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f","balance_apt":None},
  "I": {"address":"0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9","balance_apt":None},
  "J": {"address":"0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54","balance_apt":None},
  "K": {"address":"0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4","balance_apt":None},
  "L": {"address":"0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9","balance_apt":None},
  "M": {"address":"0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9","balance_apt":None},
  "N": {"address":"0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c","balance_apt":None},
  "O": {"address":"0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d","balance_apt":None},
  "P": {"address":"0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948","balance_apt":None},
  "Q": {"address":"0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9","balance_apt":None},
  "R": {"address":"0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10","balance_apt":None},
  "S": {"address":"0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386","balance_apt":None},
  "T": {"address":"0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588","balance_apt":None},
  "U": {"address":"0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956","balance_apt":None},
  "V": {"address":"0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3","balance_apt":None},
  "W": {"address":"0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0","balance_apt":None},
  "X": {"address":"0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d","balance_apt":None},
  "Y": {"address":"0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4","balance_apt":None},
  "Z": {"address":"0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c","balance_apt":None},
}

for world, info in aptos_data.items():
    con.execute("INSERT INTO aptos_snapshots VALUES (?,?,?,?)",
                [TS, world, info["address"], info["balance_apt"]])

# ─── MULTISIG PROBES ──────────────────────────────────────────────────────────

multisig_data = [
  ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2,True),
  ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2,True),
  ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2,True),
  ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2,True),
  ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2,True),
]
for pair, addr, sigs, healthy in multisig_data:
    con.execute("INSERT INTO multisig_probes VALUES (?,?,?,?,?)",
                [TS, pair, addr, sigs, healthy])

con.close()
print("DuckDB build complete:", DB_PATH)
