#!/usr/bin/env python3
"""Build world-increments.duckdb with GitHub sweep + Aptos hamming snapshot."""
import duckdb
import hashlib
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "world-increments.duckdb")
con = duckdb.connect(DB_PATH)

# ── Schema ──────────────────────────────────────────────────────────────────
con.execute("""
CREATE TABLE IF NOT EXISTS world_increments (
  id INTEGER, timestamp TIMESTAMP DEFAULT now(), gf3_trit INTEGER,
  gf3_color VARCHAR, gf3_name VARCHAR, source_type VARCHAR,
  source_name VARCHAR, event_type VARCHAR, repo_name VARCHAR,
  actor VARCHAR, snapshot_hash VARCHAR
)
""")
con.execute("""
CREATE TABLE IF NOT EXISTS repo_snapshots (
  id INTEGER, timestamp TIMESTAMP DEFAULT now(), increment_id INTEGER,
  org_or_user VARCHAR, repo_name VARCHAR, full_name VARCHAR,
  language VARCHAR, stars INTEGER, forks INTEGER, open_issues INTEGER,
  pushed_at VARCHAR, description VARCHAR
)
""")
con.execute("""
CREATE TABLE IF NOT EXISTS aptos_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  world VARCHAR, address VARCHAR, balance_apt DOUBLE
)
""")
con.execute("""
CREATE TABLE IF NOT EXISTS multisig_probes (
  timestamp TIMESTAMP DEFAULT now(),
  pair VARCHAR, address VARCHAR, sigs_required INTEGER, healthy BOOLEAN
)
""")
con.execute("""
CREATE TABLE IF NOT EXISTS mnx_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  ticker VARCHAR, name VARCHAR, category VARCHAR,
  price DOUBLE, change_pct DOUBLE
)
""")

# Clear for fresh insert
for t in ["world_increments","repo_snapshots","aptos_snapshots","multisig_probes","mnx_snapshots"]:
    con.execute(f"DELETE FROM {t}")

# ── GF(3) color chain ────────────────────────────────────────────────────────
def gf3(idx):
    trit = idx % 3
    if trit == 0: return (0, "#d3869b", "ERGODIC")
    if trit == 1: return (1, "#b8bb26", "PLUS")
    return (-1, "#cc241d", "MINUS")

def snap_hash(source_name, source_type):
    return hashlib.sha256(f"{source_name}:{source_type}:2026-06-24".encode()).hexdigest()[:16]

# ── Sources ──────────────────────────────────────────────────────────────────
SOURCES = [
    ("org", "plurigrid"),
    ("org", "kubeflow"),
    ("org", "TeglonLabs"),
    ("user", "bmorphism"),
    ("user", "zubyul"),
    ("user", "migalkin"),
    ("user", "DJedamski"),
    ("user", "wasita"),
    ("user", "kristinezheng"),
    ("user", "M1shaaa"),
    ("user", "AustinCStone"),
]

inc_id = 1
for (src_type, src_name) in SOURCES:
    trit, color, name = gf3(inc_id)
    h = snap_hash(src_name, src_type)
    con.execute("""
        INSERT INTO world_increments VALUES (?,now(),?,?,?,?,?,?,?,?,?)
    """, [inc_id, trit, color, name, src_type, src_name, "repo_sweep", src_name, "agent", h])
    inc_id += 1

# ── Repo snapshots ───────────────────────────────────────────────────────────
REPOS = [
    # (increment_id, org_or_user, repo_name, full_name, language, stars, forks, open_issues, pushed_at, description)
    # plurigrid (id=1)
    (1,"plurigrid","asi","plurigrid/asi","HTML",26,8,4,"2026-06-10T12:51:42Z","everything is topological chemputer!"),
    (1,"plurigrid","place","plurigrid/place","TeX",1,1,9,"2026-06-24T00:41:15Z",""),
    (1,"plurigrid","eirobri","plurigrid/eirobri","Clojure",0,0,30,"2026-06-23T02:23:36Z","EiRoBri replay world"),
    (1,"plurigrid","nash-portal","plurigrid/nash-portal","Rust",2,3,1,"2026-05-19T01:49:59Z","NASH token TUI in the browser"),
    (1,"plurigrid","gorj","plurigrid/gorj","Clojure",0,0,787,"2026-06-24T11:12:05Z","forj + Rama topology nREPL routing + GF(3) gay trit coloring"),
    (1,"plurigrid","zig-syrup","plurigrid/zig-syrup","Zig",2,2,0,"2026-04-30T03:52:16Z","High-performance Zig OCapN Syrup implementation"),
    (1,"plurigrid","asi-skills","plurigrid/asi-skills","Julia",3,0,0,"2026-04-26T08:09:26Z","69 skills with Galois Hole Type accessibility"),
    (1,"plurigrid","nanoclj-zig","plurigrid/nanoclj-zig","Zig",1,1,20,"2026-04-25T07:29:09Z","NaN-boxed Clojure interpreter in Zig 0.15"),
    (1,"plurigrid","ontology","plurigrid/ontology","JavaScript",8,9,16,"2025-05-27T18:18:34Z","autopoietic ergodicity and embodied gradualism"),
    (1,"plurigrid","Plurigraph","plurigrid/Plurigraph","JavaScript",3,5,4,"2025-01-05T08:39:09Z","Plurigrid knowledge base for Obsidian.md"),
    (1,"plurigrid","act","plurigrid/act","Python",3,1,4,"2024-07-26T08:27:08Z","building blocks for cognitive category theory"),
    (1,"plurigrid","StochFlow","plurigrid/StochFlow","Python",4,1,0,"2024-03-20T23:34:57Z","stochastic interpolant models"),
    (1,"plurigrid","microworlds","plurigrid/microworlds","Rust",3,5,3,"2023-05-13T03:54:56Z","microworlds"),
    (1,"plurigrid","agent","plurigrid/agent","Python",5,1,6,"2023-03-31T18:45:23Z","Framework for agency amplification"),
    (1,"plurigrid","vcg-auction","plurigrid/vcg-auction","Rust",7,2,1,"2023-03-16T21:53:08Z","VCG auction contract"),
    (1,"plurigrid","vivarium","plurigrid/vivarium","Clojure",1,0,0,"2026-04-08T08:38:37Z",""),
    (1,"plurigrid","bci-blue-share","plurigrid/bci-blue-share","JavaScript",0,0,0,"2026-04-26T07:08:03Z","BCI signal infrastructure"),
    (1,"plurigrid","gatomic","plurigrid/gatomic","Clojure",0,0,0,"2026-03-30T00:54:48Z","Deterministic color identity store with sonification"),
    (1,"plurigrid","web-browser","plurigrid/web-browser","Rust",0,0,0,"2026-04-10T02:54:47Z","web-browser from prepostweb lineage"),
    (1,"plurigrid","gay-rs","plurigrid/gay-rs","Rust",0,0,0,"2026-01-08T14:19:22Z","Rust crate for Gay.jl deterministic coloring"),
    # kubeflow (id=2)
    (2,"kubeflow","kubeflow","kubeflow/kubeflow","",15742,2680,0,"2026-06-18T11:45:16Z","Machine Learning Toolkit for Kubernetes"),
    (2,"kubeflow","pipelines","kubeflow/pipelines","Python",4157,2009,456,"2026-06-23T11:58:41Z","Machine Learning Pipelines for Kubeflow"),
    (2,"kubeflow","spark-operator","kubeflow/spark-operator","Python",3128,1491,108,"2026-06-24T03:15:09Z","Kubernetes operator for Apache Spark"),
    (2,"kubeflow","trainer","kubeflow/trainer","Go",2119,972,129,"2026-06-24T10:40:35Z","Distributed AI Model Training and LLM Fine-Tuning"),
    (2,"kubeflow","katib","kubeflow/katib","Python",1685,527,112,"2026-06-23T11:07:55Z","Automated Machine Learning on Kubernetes"),
    (2,"kubeflow","community-distribution","kubeflow/community-distribution","YAML",1028,1065,22,"2026-06-18T19:10:25Z","Kubeflow Community Distribution"),
    (2,"kubeflow","arena","kubeflow/arena","Go",813,191,45,"2026-05-07T06:46:17Z","A CLI for Kubeflow"),
    (2,"kubeflow","kale","kubeflow/kale","Python",694,156,53,"2026-06-22T11:11:44Z","Kubeflow's superfood for Data Scientists"),
    (2,"kubeflow","community","kubeflow/community","Jupyter Notebook",194,264,14,"2026-06-22T18:11:52Z","Kubeflow community proposals and governance"),
    (2,"kubeflow","website","kubeflow/website","HTML",184,922,40,"2026-06-19T15:39:26Z","Kubeflow Website"),
    (2,"kubeflow","hub","kubeflow/hub","Go",173,183,45,"2026-06-23T10:35:10Z","Model Registry for ML developers"),
    (2,"kubeflow","kfp-tekton","kubeflow/kfp-tekton","TypeScript",183,123,79,"2024-11-19T12:23:51Z","Kubeflow Pipelines on Tekton"),
    (2,"kubeflow","mcp-apache-spark-history-server","kubeflow/mcp-apache-spark-history-server","Python",178,65,20,"2026-06-23T23:14:00Z","MCP Server for Apache Spark History Server"),
    (2,"kubeflow","notebooks","kubeflow/notebooks","",73,125,179,"2026-06-23T18:13:30Z","Kubeflow Notebooks for AI/ML workloads"),
    (2,"kubeflow","mcp-server","kubeflow/mcp-server","Python",17,23,26,"2026-06-24T11:09:23Z","MCP Server for AI-Assisted Development"),
    (2,"kubeflow","dashboard","kubeflow/dashboard","TypeScript",16,59,83,"2026-06-24T00:51:39Z","Kubeflow Central Dashboard"),
    (2,"kubeflow","mpi-operator","kubeflow/mpi-operator","Go",528,236,103,"2026-06-23T17:30:35Z","Kubernetes Operator for MPI-based applications"),
    (2,"kubeflow","internal-acls","kubeflow/internal-acls","Go",19,390,1,"2026-06-19T19:50:08Z","Group ACLs for Kubeflow developers"),
    (2,"kubeflow","docs-agent","kubeflow/docs-agent","Python",39,95,153,"2026-06-11T18:43:15Z","Kubeflow Documentation AI Agent"),
    (2,"kubeflow","blog","kubeflow/blog","Jupyter Notebook",32,62,26,"2026-06-11T16:32:01Z","Kubeflow blog"),
    # TeglonLabs (id=3)
    (3,"TeglonLabs","jank-crane","TeglonLabs/jank-crane","C++",0,0,0,"2026-06-08T19:03:03Z","crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps"),
    (3,"TeglonLabs","mathpix-gem","TeglonLabs/mathpix-gem","Ruby",2,0,11,"2026-01-01T12:13:13Z","Transform mathematical images to LaTeX"),
    (3,"TeglonLabs","coin-flip-mcp","TeglonLabs/coin-flip-mcp","JavaScript",0,2,1,"2025-09-21T08:57:27Z","MCP server for flipping coins from random.org"),
    (3,"TeglonLabs","monad-mcp-server","TeglonLabs/monad-mcp-server","",0,0,0,"2025-05-14T11:36:14Z","Monad MCP Server"),
    (3,"TeglonLabs","topoi","TeglonLabs/topoi","Python",0,0,1,"2025-01-24T04:49:26Z",""),
    # bmorphism (id=4)
    (4,"bmorphism","Gay.jl","bmorphism/Gay.jl","Julia",2,1,187,"2026-06-24T00:35:11Z","Wide-gamut color sampling with splittable determinism"),
    (4,"bmorphism","satreadout","bmorphism/satreadout","HTML",0,0,0,"2026-06-20T13:05:41Z","Machine-checked saturating non-Riemannian perceptual readout"),
    (4,"bmorphism","ocaml-mcp-sdk","bmorphism/ocaml-mcp-sdk","OCaml",61,2,0,"2026-03-16T05:24:25Z","OCaml SDK for Model Context Protocol"),
    (4,"bmorphism","anti-bullshit-mcp-server","bmorphism/anti-bullshit-mcp-server","JavaScript",23,7,1,"2026-01-16T08:54:58Z","MCP server for analyzing claims and detecting manipulation"),
    (4,"bmorphism","shitcoin","bmorphism/shitcoin","Python",5,0,0,"2026-04-08T08:07:08Z","CW20 asset denom for IBC"),
    (4,"bmorphism","say-mcp-server","bmorphism/say-mcp-server","JavaScript",20,9,3,"2025-01-07T03:15:18Z","MCP server for macOS text-to-speech"),
    (4,"bmorphism","babashka-mcp-server","bmorphism/babashka-mcp-server","JavaScript",19,6,3,"2025-01-05T11:09:42Z","MCP server for Babashka Clojure"),
    (4,"bmorphism","manifold-mcp-server","bmorphism/manifold-mcp-server","JavaScript",14,9,5,"2025-01-11T10:36:58Z","MCP server for Manifold Markets"),
    (4,"bmorphism","penrose-mcp","bmorphism/penrose-mcp","JavaScript",10,4,0,"2025-01-20T21:44:55Z","Penrose MCP server"),
    (4,"bmorphism","risc0-cosmwasm-example","bmorphism/risc0-cosmwasm-example","Rust",23,2,1,"2022-10-20T23:50:40Z","CosmWasm + zkVM RISC-V EFI template"),
    (4,"bmorphism","world","bmorphism/world","Python",0,0,0,"2026-06-02T06:49:02Z","Local worlds launcher for SA3, jank, and world proofs"),
    (4,"bmorphism","oxgame","bmorphism/oxgame","OCaml",0,0,0,"2026-05-15T09:53:27Z","Stellar resolution and open-game composition for OCaml"),
    (4,"bmorphism","graphistry-mcp","bmorphism/graphistry-mcp","Python",2,0,0,"2025-05-06T17:34:24Z","Graphistry MCP integration"),
    (4,"bmorphism","monero-rental-hash-war","bmorphism/monero-rental-hash-war","Haskell",1,0,0,"2025-10-05T23:08:54Z","Compositional OpenGame analysis of Monero rental hash war"),
    (4,"bmorphism","magic-world-org","bmorphism/magic-world-org","Python",1,0,0,"2026-04-05T07:03:50Z","Magic World Org (Local MLX)"),
    (4,"bmorphism","bafishka","bmorphism/bafishka","Clojure",1,0,0,"2025-12-19T09:38:00Z","Rust-native Fish shell file operations with SCI Clojure"),
    # zubyul (id=5)
    (5,"zubyul","voice-observatory","zubyul/voice-observatory","Python",0,0,0,"2026-04-24T05:56:17Z","Passive macOS TUI observing voice-download pathways"),
    (5,"zubyul","nash-tui","zubyul/nash-tui","Rust",0,0,0,"2026-04-13T07:45:16Z","NASH token TUI: real-time candles, ticker"),
    (5,"zubyul","nash-web","zubyul/nash-web","Rust",0,0,0,"2026-04-13T07:08:58Z","NASH token browser TUI via ratzilla WASM"),
    (5,"zubyul","big-bad-plurigrid-quiz","zubyul/big-bad-plurigrid-quiz","Emacs Lisp",0,0,0,"2026-04-09T18:51:31Z","27 flashcards from plurigrid activity"),
    (5,"zubyul","Gay.jl","zubyul/Gay.jl","Julia",0,0,0,"2026-03-28T11:30:01Z","Wide-gamut color sampling fork"),
    (5,"zubyul","gay-world","zubyul/gay-world","Python",1,1,0,"2026-03-26T04:03:39Z","Goblin world builder: composable persistent worlds"),
    (5,"zubyul","kinesis-kb360pro","zubyul/kinesis-kb360pro","Python",0,0,0,"2026-03-26T10:29:40Z","Claude Code skill for Kinesis Advantage360 Pro keyboard"),
    (5,"zubyul","tilelang-kernels","zubyul/tilelang-kernels","Python",0,0,0,"2026-03-16T02:31:13Z","TileLang GPU kernels for SplitMix64 color generation"),
    (5,"zubyul","plurigrid-site","zubyul/plurigrid-site","Svelte",0,1,11,"2026-02-04T03:20:08Z","Plurigrid world: site deployment"),
    (5,"zubyul","zubyul.github.io","zubyul/zubyul.github.io","CSS",1,0,0,"2026-01-27T03:24:34Z","Personal site"),
    # migalkin (id=6)
    (6,"migalkin","NodePiece","migalkin/NodePiece","Python",144,21,0,"2026-05-07T05:40:02Z","Compositional and Parameter-Efficient Representations for Large KGs (ICLR 22)"),
    (6,"migalkin","StarE","migalkin/StarE","Python",89,16,1,"2026-04-16T14:12:45Z","Message Passing for Hyper-Relational Knowledge Graphs (EMNLP 2020)"),
    (6,"migalkin","kgcourse2021","migalkin/kgcourse2021","HTML",25,9,0,"2026-02-16T05:16:08Z","Materials for Knowledge Graphs course"),
    (6,"migalkin","NBFNet_mlx","migalkin/NBFNet_mlx","Python",10,1,1,"2026-03-11T01:31:21Z","Neural Bellman-Ford networks in MLX for Apple Silicon"),
    (6,"migalkin","RWL","migalkin/RWL","Python",8,1,0,"2026-05-28T20:19:20Z","Weisfeiler and Leman Go Relational (LOG 2022)"),
    (6,"migalkin","rambo","migalkin/rambo","Rust",3,0,1,"2023-02-28T16:37:22Z",""),
    # DJedamski (id=7)
    (7,"DJedamski","kaggle_ncaa18","DJedamski/kaggle_ncaa18","Jupyter Notebook",0,0,0,"2018-02-26T16:33:24Z","NCAA March Madness competition 2018"),
    (7,"DJedamski","Kaggle","DJedamski/Kaggle","",1,0,0,"2023-04-21T01:42:35Z",""),
    (7,"DJedamski","Getting-and-Cleaning-Data","DJedamski/Getting-and-Cleaning-Data","R",1,0,0,"2023-04-21T01:42:34Z","Coursera Project"),
    (7,"DJedamski","School","DJedamski/School","R",1,1,0,"2023-04-21T01:42:33Z","Small projects from grad school"),
    (7,"DJedamski","EDA","DJedamski/EDA","R",0,0,0,"2014-11-09T17:00:39Z","Coursera Project"),
    # wasita (id=8)
    (8,"wasita","wasita.github.io","wasita/wasita.github.io","Svelte",1,0,8,"2026-06-15T20:14:23Z","Personal website"),
    (8,"wasita","proj-template","wasita/proj-template","",0,0,0,"2026-06-19T21:22:21Z",""),
    (8,"wasita","vocoder","wasita/vocoder","JavaScript",0,0,0,"2026-05-06T05:14:03Z",""),
    (8,"wasita","wm-cv","wasita/wm-cv","Svelte",0,0,0,"2026-05-13T05:29:08Z","Academic CV web app"),
    (8,"wasita","magic-garden","wasita/magic-garden","Python",2,1,1,"2026-04-22T21:16:43Z","Bot for magic garden discord game"),
    (8,"wasita","send2kobo","wasita/send2kobo","TypeScript",1,0,0,"2026-05-19T02:59:26Z","Website for sending books to kobo"),
    (8,"wasita","food-diary","wasita/food-diary","Svelte",0,0,0,"2025-12-13T01:06:43Z",""),
    (8,"wasita","wins-search","wasita/wins-search","CSS",1,0,0,"2023-06-03T19:01:11Z","Women in Network Science member list"),
    # kristinezheng (id=9)
    (9,"kristinezheng","kristinezheng.github.io","kristinezheng/kristinezheng.github.io","HTML",0,0,0,"2026-06-07T22:53:10Z",""),
    (9,"kristinezheng","lookit-jenga","kristinezheng/lookit-jenga","Jupyter Notebook",0,0,0,"2024-05-16T18:29:05Z","Lookit study for 9.85"),
    (9,"kristinezheng","auditory-illusion","kristinezheng/auditory-illusion","CSS",0,0,0,"2022-03-07T02:57:44Z","9.35 auditory illusion project"),
    (9,"kristinezheng","Green-Machine","kristinezheng/Green-Machine","Python",0,0,0,"2021-09-19T05:33:04Z","HackMIT 2021 Sustainability Track"),
    (9,"kristinezheng","graph_example","kristinezheng/graph_example","Python",0,0,0,"2021-10-08T07:29:53Z",""),
    # M1shaaa (id=10)
    (10,"M1shaaa","M1shaaa","M1shaaa/M1shaaa","",0,0,0,"2026-02-04T19:32:04Z","Config files for GitHub profile"),
    (10,"M1shaaa","lab-bookshelf-","M1shaaa/lab-bookshelf-","TypeScript",0,0,0,"2024-12-31T05:11:18Z",""),
    (10,"M1shaaa","Python-Lookit-Uploads","M1shaaa/Python-Lookit-Uploads","Python",0,0,0,"2024-02-15T22:59:37Z","Random Python projects"),
    (10,"M1shaaa","Yale-Work","M1shaaa/Yale-Work","HTML",0,0,0,"2023-12-06T18:33:14Z","Yale work"),
    (10,"M1shaaa","MNIST-Classifier","M1shaaa/MNIST-Classifier","",0,0,0,"2023-11-28T06:10:47Z",""),
    # AustinCStone (id=11)
    (11,"AustinCStone","TextGAN","AustinCStone/TextGAN","Python",92,30,5,"2025-03-03T13:26:32Z","Generative adversarial network for text generation in TensorFlow"),
    (11,"AustinCStone","StereoVisionMRF","AustinCStone/StereoVisionMRF","Python",11,4,0,"2026-04-01T07:39:41Z","Recover 3D geometry from stereo videos"),
    (11,"AustinCStone","SpectralClustering","AustinCStone/SpectralClustering","Python",3,2,0,"2021-04-16T08:46:36Z","Implementing spectral clustering"),
    (11,"AustinCStone","EpsteinSearch","AustinCStone/EpsteinSearch","Python",0,0,0,"2026-02-11T01:10:57Z",""),
    (11,"AustinCStone","bmforkupdate","AustinCStone/bmforkupdate","Python",0,0,0,"2025-05-09T04:50:16Z",""),
    (11,"AustinCStone","bmfork","AustinCStone/bmfork","Python",0,0,1,"2025-05-09T04:18:54Z",""),
    (11,"AustinCStone","RealTimeRayTracingFractalWorld","AustinCStone/RealTimeRayTracingFractalWorld","C++",0,0,0,"2015-05-11T01:58:57Z","Real time ray tracing fractal world"),
    (11,"AustinCStone","logisticRegressionHaskell","AustinCStone/logisticRegressionHaskell","Haskell",1,0,0,"2018-02-02T13:34:28Z","Logistic regression in Haskell"),
]

repo_id = 1
for r in REPOS:
    con.execute("""
        INSERT INTO repo_snapshots VALUES (?,now(),?,?,?,?,?,?,?,?,?,?)
    """, [repo_id, r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9]])
    repo_id += 1

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
for world, addr, bal in APTOS:
    con.execute("INSERT INTO aptos_snapshots VALUES (now(),?,?,?)", [world, addr, bal])

# ── Multisig probes ──────────────────────────────────────────────────────────
MULTISIGS = [
    ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2),
    ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2),
    ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2),
    ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2),
    ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2),
]
for pair, addr, sigs in MULTISIGS:
    con.execute("INSERT INTO multisig_probes VALUES (now(),?,?,?,?)", [pair, addr, sigs, True])

# MNX snapshots: unavailable (Vercel auth required)
# No rows inserted

con.close()

# ── Verification ─────────────────────────────────────────────────────────────
con2 = duckdb.connect(DB_PATH, read_only=True)
tables = ["world_increments","repo_snapshots","aptos_snapshots","multisig_probes","mnx_snapshots"]
for t in tables:
    cnt = con2.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
    print(f"{t}: {cnt} rows")
con2.close()
print("DuckDB built OK:", DB_PATH)
