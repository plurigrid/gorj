#!/usr/bin/env python3
"""Build world-increments DuckDB from collected GitHub + Aptos data."""
import duckdb
import json
from datetime import datetime

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"

con = duckdb.connect(DB_PATH)

# --- Schema ---
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

def gf3(idx):
    trit = idx % 3
    if trit == 0:
        return (0, "#d3869b", "ERGODIC")
    elif trit == 1:
        return (1, "#b8bb26", "PLUS")
    else:
        return (-1, "#cc241d", "MINUS")

# --- Repo data ---
repos = {
    "org:plurigrid": [
        ("plurigrid", "plurigrid/asi", "HTML", 28, 8, 4, "2026-06-29T03:15:56Z", "everything is topological chemputer!"),
        ("plurigrid", "plurigrid/place", "TeX", 1, 1, 12, "2026-06-29T20:40:59Z", ""),
        ("plurigrid", "plurigrid/eirobri", "Clojure", 0, 0, 30, "2026-06-30T02:23:56Z", "EiRoBri replay world"),
        ("plurigrid", "plurigrid/nash-portal", "Rust", 2, 3, 1, "2026-05-19T01:49:59Z", "NASH token TUI in the browser"),
        ("plurigrid", "plurigrid/gorj", "Clojure", 0, 0, 926, "2026-07-02T22:16:26Z", "forj + Rama topology nREPL routing + GF(3) gay trit coloring"),
        ("plurigrid", "plurigrid/zig-syrup", "Zig", 2, 2, 0, "2026-04-30T03:52:16Z", "High-performance Zig implementation of OCapN Syrup"),
        ("plurigrid", "plurigrid/asi-skills", "Julia", 3, 0, 0, "2026-04-26T08:09:26Z", "69 skills with Galois Hole Type accessibility"),
        ("plurigrid", "plurigrid/nanoclj-zig", "Zig", 1, 1, 20, "2026-04-25T07:29:09Z", "NaN-boxed Clojure interpreter in Zig"),
        ("plurigrid", "plurigrid/vivarium", "Clojure", 1, 0, 0, "2026-04-08T08:38:37Z", ""),
        ("plurigrid", "plurigrid/ontology", "JavaScript", 8, 9, 16, "2025-05-27T18:18:34Z", "autopoietic ergodicity and embodied gradualism"),
        ("plurigrid", "plurigrid/Plurigraph", "JavaScript", 3, 5, 4, "2025-01-05T08:39:09Z", "Plurigrid knowledge base"),
        ("plurigrid", "plurigrid/gatomic", "Clojure", 0, 0, 0, "2026-03-30T00:54:48Z", "Deterministic color identity store with sonification"),
        ("plurigrid", "plurigrid/gay-rs", "Rust", 0, 0, 0, "2026-01-08T14:19:22Z", "Rust crate for Gay.jl deterministic coloring"),
        ("plurigrid", "plurigrid/lazygay", "Go", 0, 0, 0, "2026-01-08T14:19:25Z", "lazygit fork with Gay.jl deterministic commit coloring"),
        ("plurigrid", "plurigrid/agent-o-rama", "Clojure", 0, 0, 0, "2026-01-02T01:09:22Z", ""),
        ("plurigrid", "plurigrid/shepherd", "Scheme", 0, 0, 0, "2026-01-23T07:47:28Z", "Spritely Shepherd (mirror)"),
        ("plurigrid", "plurigrid/hoot", "Scheme", 0, 0, 1, "2026-01-23T07:47:10Z", "Spritely Hoot - Scheme to WebAssembly compiler"),
        ("plurigrid", "plurigrid/leprechauns", "Racket", 0, 0, 0, "2026-01-23T07:46:46Z", "Spritely Goblins + Gay.jl semantic colors"),
        ("plurigrid", "plurigrid/aptos-wallet-ruby", "Ruby", 1, 0, 0, "2025-09-30T22:47:22Z", ""),
        ("plurigrid", "plurigrid/duck-kanban", "Rust", 1, 0, 0, "2025-09-26T20:18:38Z", "Duck intelligence kanban system"),
        ("plurigrid", "plurigrid/forester", "XSLT", 0, 0, 0, "2026-03-30T01:32:26Z", "CatColab mathematical documentation forest"),
        ("plurigrid", "plurigrid/graded-optic", "Haskell", 0, 0, 0, "2026-02-08T16:10:16Z", "Semiring-graded bidirectional processes"),
        ("plurigrid", "plurigrid/reafference", "HTML", 0, 0, 0, "2026-04-16T05:21:49Z", "Reafference adaptation workspace"),
        ("plurigrid", "plurigrid/spi-race", "Swift", 0, 0, 0, "2026-04-21T19:31:56Z", "Splitmix Parallel Integrity"),
        ("plurigrid", "plurigrid/bci-blue-share", "JavaScript", 0, 0, 0, "2026-04-26T07:08:03Z", "BCI signal infrastructure"),
        ("plurigrid", "plurigrid/gay-tofu", "HTML", 0, 0, 0, "2026-01-08T15:14:34Z", "Low-discrepancy color sequences for visual TOFU"),
        ("plurigrid", "plurigrid/act", "Python", 3, 1, 4, "2024-07-26T08:27:08Z", "building blocks for cognitive category theory"),
        ("plurigrid", "plurigrid/website", "Clojure", 0, 1, 0, "2024-03-30T04:37:51Z", ""),
    ],
    "org:kubeflow": [
        ("kubeflow", "kubeflow/kubeflow", None, 15758, 2683, 0, "2026-07-02T22:11:23Z", "Machine Learning Toolkit for Kubernetes"),
        ("kubeflow", "kubeflow/pipelines", "Python", 4167, 2020, 413, "2026-07-02T19:43:31Z", "Machine Learning Pipelines for Kubeflow"),
        ("kubeflow", "kubeflow/trainer", "Go", 2129, 974, 142, "2026-07-02T19:15:37Z", "Distributed AI Model Training and LLM Fine-Tuning"),
        ("kubeflow", "kubeflow/sdk", "Python", 123, 187, 138, "2026-07-02T19:23:41Z", "Universal Python SDK for AI workloads on Kubernetes"),
        ("kubeflow", "kubeflow/spark-operator", "Python", 3130, 1496, 103, "2026-07-01T11:51:51Z", "Kubernetes operator for Apache Spark"),
        ("kubeflow", "kubeflow/katib", "Python", 1688, 529, 114, "2026-07-01T11:51:44Z", "Automated Machine Learning on Kubernetes"),
        ("kubeflow", "kubeflow/arena", "Go", 814, 194, 48, "2026-07-01T03:54:55Z", "A CLI for Kubeflow"),
        ("kubeflow", "kubeflow/kale", "Python", 694, 156, 38, "2026-07-01T16:39:54Z", "Kubeflow's superfood for Data Scientists"),
        ("kubeflow", "kubeflow/mcp-apache-spark-history-server", "Python", 179, 66, 19, "2026-07-01T21:23:15Z", "MCP Server for Apache Spark History Server"),
        ("kubeflow", "kubeflow/community-distribution", "YAML", 1028, 1067, 29, "2026-06-30T15:22:51Z", "Kubeflow Community Distribution"),
        ("kubeflow", "kubeflow/hub", "Go", 174, 183, 34, "2026-07-02T17:17:13Z", "Model Registry for ML models"),
        ("kubeflow", "kubeflow/mpi-operator", "Go", 529, 237, 102, "2026-07-02T17:00:51Z", "Kubernetes Operator for MPI-based applications"),
        ("kubeflow", "kubeflow/examples", "Jsonnet", 1460, 756, 111, "2026-06-16T17:59:01Z", "Extended examples and tutorials"),
        ("kubeflow", "kubeflow/community", "Jupyter Notebook", 194, 265, 14, "2026-07-01T21:20:26Z", "Kubeflow community"),
        ("kubeflow", "kubeflow/website", "HTML", 184, 923, 29, "2026-07-02T16:52:55Z", "Kubeflow Website"),
        ("kubeflow", "kubeflow/mcp-server", "Python", 19, 25, 32, "2026-06-29T16:55:51Z", "MCP Server for Kubeflow Tools"),
        ("kubeflow", "kubeflow/docs-agent", "Python", 39, 95, 152, "2026-06-29T10:25:33Z", "Kubeflow Documentation AI Agent"),
        ("kubeflow", "kubeflow/pipelines-components", "Python", 11, 47, 36, "2026-07-02T16:10:35Z", "Kubeflow Pipelines components"),
        ("kubeflow", "kubeflow/notebooks", None, 73, 125, 180, "2026-06-24T01:29:18Z", "Kubeflow Notebooks"),
        ("kubeflow", "kubeflow/dashboard", "TypeScript", 16, 59, 86, "2026-06-25T18:23:39Z", "Kubeflow Central Dashboard"),
        ("kubeflow", "kubeflow/fairing", "Jsonnet", 337, 143, 134, "2025-09-08T14:41:40Z", "Python SDK for building and training ML models"),
        ("kubeflow", "kubeflow/pytorch-operator", "Jsonnet", 310, 143, 63, "2026-04-29T19:38:07Z", "PyTorch on Kubernetes (archived)"),
        ("kubeflow", "kubeflow/kfctl", "Go", 182, 134, 94, "2026-04-07T18:37:47Z", "kfctl CLI (archived)"),
        ("kubeflow", "kubeflow/mlflow-integration", "Python", 6, 5, 5, "2026-06-12T19:01:14Z", "MLflow integration for Kubeflow"),
    ],
    "org:TeglonLabs": [
        ("TeglonLabs", "TeglonLabs/jank-crane", "C++", 0, 0, 0, "2026-06-08T19:03:37Z", "crane-jank converged-IR hub"),
        ("TeglonLabs", "TeglonLabs/mathpix-gem", "Ruby", 2, 0, 11, "2026-01-01T12:13:16Z", "Mathematical OCR in Ruby"),
        ("TeglonLabs", "TeglonLabs/coin-flip-mcp", "JavaScript", 0, 2, 1, "2025-03-16T01:31:45Z", "MCP server for flipping coins"),
        ("TeglonLabs", "TeglonLabs/monad-mcp-server", None, 0, 0, 0, "2025-05-14T17:53:01Z", "Monad MCP Server"),
        ("TeglonLabs", "TeglonLabs/topoi", "Python", 0, 0, 1, "2025-01-24T06:47:38Z", ""),
    ],
    "user:bmorphism": [
        ("bmorphism", "bmorphism/satreadout", "HTML", 0, 0, 0, "2026-06-20T13:05:44Z", "Machine-checked saturating non-Riemannian perceptual readout"),
        ("bmorphism", "bmorphism/Gay.jl", "Julia", 2, 1, 187, "2026-06-20T14:21:55Z", "Wide-gamut color sampling with splittable determinism"),
        ("bmorphism", "bmorphism/bci-preview", "HTML", 0, 0, 0, "2026-06-20T00:20:47Z", "Stable redirect for bci.place"),
        ("bmorphism", "bmorphism/world", "Python", 0, 0, 0, "2026-06-02T06:49:06Z", "Local worlds launcher"),
        ("bmorphism", "bmorphism/nanoclj-zig", "Zig", 1, 0, 0, "2026-06-10T16:00:16Z", ""),
        ("bmorphism", "bmorphism/flox-mcp-bb", "Clojure", 0, 0, 0, "2026-06-05T17:53:47Z", "Open-source MCP server for Flox"),
        ("bmorphism", "bmorphism/zig-syrup", "Zig", 0, 0, 0, "2026-03-28T21:42:35Z", "OCapN Syrup encoder/decoder in Zig"),
        ("bmorphism", "bmorphism/open-location-code-zig", "Zig", 3, 0, 0, "2026-03-24T21:54:01Z", "Open Location Code for Zig"),
        ("bmorphism", "bmorphism/ocaml-mcp-sdk", "OCaml", 61, 2, 0, "2026-05-08T16:50:34Z", "OCaml SDK for Model Context Protocol"),
        ("bmorphism", "bmorphism/magic-world-org", "Python", 1, 0, 0, "2026-05-01T01:06:25Z", "Magic World Org"),
        ("bmorphism", "bmorphism/whale", "MATLAB", 2, 0, 0, "2026-04-20T15:04:09Z", "omniglot + sperm whale codas"),
        ("bmorphism", "bmorphism/penrose-mcp", "JavaScript", 9, 4, 0, "2026-06-24T15:36:16Z", "Penrose server for Infinity-Topos"),
        ("bmorphism", "bmorphism/aella", "Rascal", 1, 0, 0, "2026-04-02T17:15:48Z", ""),
        ("bmorphism", "bmorphism/postweb", "Go", 0, 0, 0, "2026-04-09T10:52:07Z", "postweb"),
        ("bmorphism", "bmorphism/anti-bullshit-mcp-server", "JavaScript", 23, 7, 1, "2026-02-05T15:46:59Z", "MCP server for analyzing claims"),
        ("bmorphism", "bmorphism/manifold-mcp-server", "JavaScript", 14, 9, 5, "2026-04-15T19:54:28Z", "MCP server for Manifold Markets"),
        ("bmorphism", "bmorphism/say-mcp-server", "JavaScript", 20, 9, 3, "2026-03-19T23:11:55Z", "MCP server for macOS TTS"),
        ("bmorphism", "bmorphism/babashka-mcp-server", "JavaScript", 19, 6, 3, "2026-06-05T13:16:11Z", "MCP server for Babashka"),
        ("bmorphism", "bmorphism/risc0-cosmwasm-example", "Rust", 23, 2, 1, "2025-05-21T13:35:37Z", "CosmWasm + zkVM RISC-V EFI template"),
        ("bmorphism", "bmorphism/shitcoin", "Python", 5, 0, 0, "2026-04-08T08:07:17Z", "gets denom for cw20 assets"),
        ("bmorphism", "bmorphism/hypernym-mcp-server", "JavaScript", 6, 5, 0, "2025-10-24T09:21:53Z", ""),
        ("bmorphism", "bmorphism/boxxy", "Move", 0, 1, 0, "2026-04-30T03:35:52Z", ""),
        ("bmorphism", "bmorphism/monero-rental-hash-war", "Haskell", 1, 0, 0, "2025-10-24T09:25:25Z", "Compositional OpenGame analysis of Monero"),
        ("bmorphism", "bmorphism/GeoACSets.jl", "Julia", 0, 1, 1, "2026-01-19T13:55:07Z", "Categorical data structures with geospatial capabilities"),
        ("bmorphism", "bmorphism/duck-rio-heateq", "Rust", 0, 0, 0, "2026-02-02T23:33:35Z", ""),
        ("bmorphism", "bmorphism/vibes", "Clojure", 0, 0, 0, "2024-11-13T15:56:31Z", "Global Vibespace"),
    ],
    "user:zubyul": [
        ("zubyul", "zubyul/voice-observatory", "Python", 0, 0, 0, "2026-04-24T05:56:20Z", "Passive macOS TUI observing voice-download pathways"),
        ("zubyul", "zubyul/ghostel-emacs-worlds", "GLSL", 0, 0, 0, "2026-04-24T00:21:00Z", "Ghostty config + ghostel family"),
        ("zubyul", "zubyul/big-bad-plurigrid-quiz", "Emacs Lisp", 0, 0, 0, "2026-04-09T18:51:35Z", "27 flashcards from bmorphism/plurigrid activity"),
        ("zubyul", "zubyul/Gay.jl", "Julia", 0, 0, 0, "2026-03-28T11:30:07Z", "Wide-gamut color sampling with splittable determinism"),
        ("zubyul", "zubyul/kinesis-kb360pro", "Python", 0, 0, 0, "2026-03-26T10:29:44Z", "Claude Code skill for Kinesis Advantage360 Pro"),
        ("zubyul", "zubyul/gay-world", "Python", 1, 1, 0, "2026-04-05T06:54:03Z", "Goblin world builder"),
        ("zubyul", "zubyul/from-possible-worlds", "TeX", 0, 0, 0, "2026-03-16T03:07:20Z", ""),
        ("zubyul", "zubyul/tilelang-kernels", "Python", 0, 0, 0, "2026-03-16T02:31:16Z", "TileLang GPU kernels for SplitMix64"),
        ("zubyul", "zubyul/hue-world", "JavaScript", 0, 0, 0, "2026-03-26T09:05:56Z", "Terminal Vibe Snipe puzzle game"),
        ("zubyul", "zubyul/multiplayer-emacs", "HTML", 0, 0, 0, "2026-03-26T09:06:00Z", "Multiplayer world: Emacs split-pane Vibe Snipe"),
        ("zubyul", "zubyul/jonikas_lab_data_analysis_misc", "Jupyter Notebook", 2, 0, 0, "2026-03-26T09:05:21Z", "scripts for large genetic sequence data"),
        ("zubyul", "zubyul/WGCNA", "HTML", 2, 0, 0, "2026-03-26T09:05:26Z", "weighted gene correlation network analysis"),
        ("zubyul", "zubyul/Nikolova_lab_data_analysis", "R", 2, 0, 0, "2026-03-26T09:05:23Z", "undergraduate thesis - cortical thickness + transcription factors"),
        ("zubyul", "zubyul/lastfm_analysis_copy", "Jupyter Notebook", 1, 0, 0, "2026-03-26T09:05:23Z", "lastfm data analysis"),
    ],
    "user:migalkin": [
        ("migalkin", "migalkin/NodePiece", "Python", 144, 21, 0, "2026-05-07T05:40:02Z", "Compositional Representations for Knowledge Graphs (ICLR'22)"),
        ("migalkin", "migalkin/StarE", "Python", 89, 16, 1, "2026-04-16T14:12:45Z", "Message Passing for Hyper-Relational Knowledge Graphs"),
        ("migalkin", "migalkin/NBFNet_mlx", "Python", 10, 1, 1, "2026-03-11T01:31:21Z", "Neural Bellman-Ford networks in MLX"),
        ("migalkin", "migalkin/RWL", "Python", 8, 1, 0, "2026-05-28T20:19:20Z", "Weisfeiler and Leman Go Relational"),
        ("migalkin", "migalkin/kgcourse2021", "HTML", 25, 9, 0, "2026-02-16T05:16:08Z", "Knowledge Graphs course materials"),
        ("migalkin", "migalkin/rambo", "Rust", 3, 0, 1, "2023-02-28T16:37:22Z", ""),
        ("migalkin", "migalkin/SMJoin-experiments", "R", 1, 0, 0, "2020-03-04T15:56:23Z", "ISWC 2017 SMJoin results"),
    ],
    "user:DJedamski": [
        ("DJedamski", "DJedamski/kaggle_ncaa18", "Jupyter Notebook", 0, 0, 0, "2018-02-26T16:33:24Z", "NCAA March Madness competition 2018"),
        ("DJedamski", "DJedamski/Kaggle", None, 1, 0, 0, "2023-04-21T01:42:35Z", ""),
        ("DJedamski", "DJedamski/Getting-and-Cleaning-Data", "R", 1, 0, 0, "2023-04-21T01:42:34Z", "Coursera Project"),
        ("DJedamski", "DJedamski/School", "R", 1, 1, 0, "2023-04-21T01:42:33Z", "Projects from grad school"),
        ("DJedamski", "DJedamski/EDA", "R", 0, 0, 0, "2014-11-09T17:00:39Z", "Coursera Project"),
    ],
    "user:wasita": [
        ("wasita", "wasita/wasita.github.io", "Svelte", 1, 0, 8, "2026-07-02T01:40:18Z", "personal website"),
        ("wasita", "wasita/proj-template", None, 0, 0, 0, "2026-06-19T21:22:21Z", ""),
        ("wasita", "wasita/wm-cv", "Svelte", 0, 0, 0, "2026-05-13T05:29:08Z", "Academic CV"),
        ("wasita", "wasita/vocoder", "JavaScript", 0, 0, 0, "2026-05-06T05:14:03Z", ""),
        ("wasita", "wasita/magic-garden", "Python", 2, 1, 1, "2026-04-22T21:16:43Z", "Bot for magic garden discord game"),
        ("wasita", "wasita/send2kobo", "TypeScript", 1, 0, 0, "2026-05-19T02:59:26Z", "Website for sending books to Kobo e-reader"),
        ("wasita", "wasita/ch3-lib", "Typst", 0, 0, 0, "2026-04-12T04:03:22Z", ""),
        ("wasita", "wasita/wins-search", "CSS", 1, 0, 0, "2023-06-03T19:01:11Z", "Women in Network Science member list website"),
    ],
    "user:kristinezheng": [
        ("kristinezheng", "kristinezheng/kristinezheng.github.io", "HTML", 0, 0, 0, "2026-07-01T20:57:48Z", ""),
        ("kristinezheng", "kristinezheng/lookit-jenga", "Jupyter Notebook", 0, 0, 0, "2024-05-16T18:29:05Z", "Lookit study"),
        ("kristinezheng", "kristinezheng/auditory-illusion", "CSS", 0, 0, 0, "2022-03-07T02:57:44Z", "auditory illusion"),
        ("kristinezheng", "kristinezheng/Green-Machine", "Python", 0, 0, 0, "2021-09-19T05:33:04Z", "HackMIT 2021 Sustainability Track"),
    ],
    "user:M1shaaa": [
        ("M1shaaa", "M1shaaa/M1shaaa", None, 0, 0, 0, "2026-02-04T19:32:04Z", "Config files for GitHub profile"),
        ("M1shaaa", "M1shaaa/lab-bookshelf-", "TypeScript", 0, 0, 0, "2024-12-31T05:11:18Z", ""),
        ("M1shaaa", "M1shaaa/rosie-s-study-3-lookit-project", None, 0, 0, 0, "2024-11-04T22:15:39Z", ""),
        ("M1shaaa", "M1shaaa/Python-Lookit-Uploads", "Python", 0, 0, 0, "2024-02-15T22:59:37Z", "random projects"),
    ],
    "user:AustinCStone": [
        ("AustinCStone", "AustinCStone/TextGAN", "Python", 92, 30, 5, "2025-03-03T13:26:32Z", "GAN for text generation in TensorFlow"),
        ("AustinCStone", "AustinCStone/StereoVisionMRF", "Python", 11, 4, 0, "2026-04-01T07:39:41Z", "Infer depth from stereo images with MRF"),
        ("AustinCStone", "AustinCStone/SpectralClustering", "Python", 3, 2, 0, "2021-04-16T08:46:46Z", "Spectral clustering implementation"),
        ("AustinCStone", "AustinCStone/EpsteinSearch", "Python", 0, 0, 0, "2026-02-11T01:10:57Z", ""),
        ("AustinCStone", "AustinCStone/bmforkupdate", "Python", 0, 0, 0, "2025-05-09T04:50:16Z", ""),
        ("AustinCStone", "AustinCStone/bmfork", "Python", 0, 0, 1, "2025-05-09T04:18:54Z", ""),
        ("AustinCStone", "AustinCStone/Z-order-curve", "Python", 0, 0, 0, "2019-06-09T02:53:43Z", "Z-order curve demo"),
        ("AustinCStone", "AustinCStone/stonks", "Python", 0, 0, 0, "2020-09-04T22:54:35Z", "option calculations"),
        ("AustinCStone", "AustinCStone/StructureFromMotion", "Python", 1, 0, 0, "2019-04-26T19:43:12Z", "Recover 3D geometry from videos"),
    ],
}

# Insert world_increments and repo_snapshots
ts = "2026-07-02 23:10:00"
increment_id = 1
repo_id = 1

for source, repo_list in repos.items():
    source_type = "org" if source.startswith("org:") else "user"
    source_name = source.split(":")[1]
    for row in repo_list:
        org_or_user, full_name, language, stars, forks, open_issues, pushed_at, desc = row
        repo_name = full_name.split("/", 1)[1]
        trit, color, name = gf3(increment_id)
        snap_hash = str(hash(f"{full_name}{pushed_at}"))[:12]

        con.execute("""INSERT INTO world_increments VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            [increment_id, ts, trit, color, name, source_type, source_name,
             "repo_snapshot", repo_name, org_or_user, snap_hash])
        con.execute("""INSERT INTO repo_snapshots VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            [repo_id, ts, increment_id, org_or_user, repo_name, full_name,
             language, stars, forks, open_issues, pushed_at, desc])

        increment_id += 1
        repo_id += 1

# --- Aptos snapshots ---
aptos_addrs = [
    ("alice", "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b", None),
    ("bob",   "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d", None),
    ("A", "0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a", None),
    ("B", "0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13", None),
    ("C", "0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e", None),
    ("D", "0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1", None),
    ("E", "0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36", None),
    ("F", "0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71", None),
    ("G", "0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32", None),
    ("H", "0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f", None),
    ("I", "0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9", None),
    ("J", "0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54", None),
    ("K", "0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4", None),
    ("L", "0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9", None),
    ("M", "0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9", None),
    ("N", "0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c", None),
    ("O", "0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d", None),
    ("P", "0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948", None),
    ("Q", "0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9", None),
    ("R", "0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10", None),
    ("S", "0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386", None),
    ("T", "0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588", None),
    ("U", "0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956", None),
    ("V", "0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3", None),
    ("W", "0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0", None),
    ("X", "0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d", None),
    ("Y", "0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4", None),
    ("Z", "0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c", None),
]

for world, addr, bal in aptos_addrs:
    con.execute("INSERT INTO aptos_snapshots VALUES (?, ?, ?, ?)",
        [ts, world, addr, bal])

# --- Multisig probes ---
multisigs = [
    ("A-B", "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2),
    ("A-G", "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2),
    ("Y-Z", "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2),
    ("S-T", "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2),
    ("V-W", "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2),
]
for pair, addr, sigs in multisigs:
    con.execute("INSERT INTO multisig_probes VALUES (?, ?, ?, ?, ?)",
        [ts, pair, addr, sigs, True])

# Verify
print("=== world_increments:", con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0])
print("=== repo_snapshots:", con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0])
print("=== aptos_snapshots:", con.execute("SELECT COUNT(*) FROM aptos_snapshots").fetchone()[0])
print("=== multisig_probes:", con.execute("SELECT COUNT(*) FROM multisig_probes").fetchone()[0])
print("=== mnx_snapshots:", con.execute("SELECT COUNT(*) FROM mnx_snapshots").fetchone()[0])

# Sample GF3 color chain
print("\n=== GF3 color sample (first 9):")
rows = con.execute("SELECT wi.id, gf3_trit, gf3_color, gf3_name, full_name FROM world_increments wi JOIN repo_snapshots rs ON wi.id = rs.increment_id ORDER BY wi.id LIMIT 9").fetchall()
for r in rows:
    print(f"  id={r[0]} trit={r[1]} {r[2]} {r[3]:8} -> {r[4]}")

# Stars summary
print("\n=== Top starred repos:")
rows = con.execute("SELECT full_name, stars, language FROM repo_snapshots ORDER BY stars DESC LIMIT 10").fetchall()
for r in rows:
    print(f"  {r[0]}: {r[1]} stars ({r[2]})")

con.close()
print("\nDone.")
