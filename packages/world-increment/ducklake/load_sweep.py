#!/usr/bin/env python3
"""World-increment sweep + Hamming swarm snapshot loader."""
import duckdb
import json
import hashlib
from datetime import datetime

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
con = duckdb.connect(DB_PATH)

# Create tables and sequences
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
try:
    con.execute("CREATE SEQUENCE IF NOT EXISTS increment_seq START 1")
except:
    pass
try:
    con.execute("CREATE SEQUENCE IF NOT EXISTS repo_seq START 1")
except:
    pass

# GF(3) color chain
def gf3(id_):
    t = id_ % 3
    if t == 0: return (0, "#d3869b", "ERGODIC")
    elif t == 1: return (1, "#b8bb26", "PLUS")
    else: return (-1, "#cc241d", "MINUS")

# All repo data
REPOS = {
    "org:plurigrid": [
        {"full_name":"plurigrid/asi","language":"HTML","stars":58,"forks":13,"open_issues":4,"pushed_at":"2026-07-10T09:47:39Z","description":"everything is topological chemputer!"},
        {"full_name":"plurigrid/ontology","language":"JavaScript","stars":8,"forks":9,"open_issues":16,"pushed_at":"2025-05-27T18:18:34Z","description":"autopoietic ergodicity and embodied gradualism"},
        {"full_name":"plurigrid/vcg-auction","language":"Rust","stars":7,"forks":3,"open_issues":1,"pushed_at":"2023-03-16T21:53:08Z","description":"a simple contract that performs a VCG auction"},
        {"full_name":"plurigrid/agent","language":"Python","stars":5,"forks":1,"open_issues":6,"pushed_at":"2023-03-31T18:45:23Z","description":"Framework for agency amplification"},
        {"full_name":"plurigrid/StochFlow","language":"Python","stars":4,"forks":1,"open_issues":0,"pushed_at":"2024-03-20T23:34:57Z","description":"stochastic interpolant models"},
        {"full_name":"plurigrid/microworlds","language":"Rust","stars":4,"forks":5,"open_issues":3,"pushed_at":"2023-05-13T03:54:56Z","description":None},
        {"full_name":"plurigrid/asi-skills","language":"Julia","stars":3,"forks":0,"open_issues":0,"pushed_at":"2026-04-26T08:09:26Z","description":"69 skills with Galois Hole Type accessibility"},
        {"full_name":"plurigrid/Plurigraph","language":"JavaScript","stars":3,"forks":5,"open_issues":4,"pushed_at":"2025-01-05T08:39:09Z","description":"Plurigrid knowledge base for Obsidian.md"},
        {"full_name":"plurigrid/act","language":"Python","stars":3,"forks":1,"open_issues":4,"pushed_at":"2024-07-26T08:27:08Z","description":"building blocks for cognitive category theory"},
        {"full_name":"plurigrid/zig-syrup","language":"Zig","stars":2,"forks":2,"open_issues":0,"pushed_at":"2026-07-28T13:02:13Z","description":"High-performance Zig implementation of OCapN Syrup"},
        {"full_name":"plurigrid/nash-portal","language":"Rust","stars":2,"forks":2,"open_issues":1,"pushed_at":"2026-05-19T01:49:59Z","description":"NASH token TUI in the browser"},
        {"full_name":"plurigrid/gorj","language":"Clojure","stars":1,"forks":0,"open_issues":1591,"pushed_at":"2026-08-03T03:12:45Z","description":"forj + Rama topology nREPL routing + GF(3) gay trit coloring"},
        {"full_name":"plurigrid/place","language":"TeX","stars":1,"forks":2,"open_issues":15,"pushed_at":"2026-08-02T20:00:41Z","description":None},
        {"full_name":"plurigrid/nanoclj-zig","language":"Zig","stars":1,"forks":1,"open_issues":20,"pushed_at":"2026-04-25T07:29:09Z","description":"NaN-boxed Clojure interpreter in Zig 0.15"},
        {"full_name":"plurigrid/vivarium","language":"Clojure","stars":1,"forks":0,"open_issues":0,"pushed_at":"2026-04-08T08:38:37Z","description":None},
        {"full_name":"plurigrid/aptos-wallet-ruby","language":"Ruby","stars":1,"forks":0,"open_issues":0,"pushed_at":"2025-09-30T22:47:22Z","description":None},
        {"full_name":"plurigrid/duck-kanban","language":"Rust","stars":1,"forks":0,"open_issues":0,"pushed_at":"2025-09-26T20:18:38Z","description":"Duck intelligence kanban system"},
        {"full_name":"plurigrid/eirobri","language":"Clojure","stars":0,"forks":0,"open_issues":31,"pushed_at":"2026-07-21T02:24:02Z","description":"EiRoBri replay world"},
        {"full_name":"plurigrid/bci-blue-share","language":"JavaScript","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-26T07:08:03Z","description":"BCI signal infrastructure"},
        {"full_name":"plurigrid/reafference","language":"HTML","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-16T05:21:49Z","description":"Reafference adaptation workspace"},
    ],
    "org:kubeflow": [
        {"full_name":"kubeflow/kubeflow","language":None,"stars":15803,"forks":2690,"open_issues":0,"pushed_at":"2026-07-10T11:31:26Z","description":"Machine Learning Toolkit for Kubernetes"},
        {"full_name":"kubeflow/pipelines","language":"Python","stars":4173,"forks":2074,"open_issues":510,"pushed_at":"2026-08-03T03:28:32Z","description":"Machine Learning Pipelines for Kubeflow"},
        {"full_name":"kubeflow/spark-operator","language":"Python","stars":3142,"forks":1509,"open_issues":110,"pushed_at":"2026-07-31T17:28:18Z","description":"Kubernetes operator for Apache Spark"},
        {"full_name":"kubeflow/trainer","language":"Go","stars":2165,"forks":1008,"open_issues":130,"pushed_at":"2026-07-31T03:10:01Z","description":"Distributed AI Model Training on Kubernetes"},
        {"full_name":"kubeflow/katib","language":"Python","stars":1694,"forks":534,"open_issues":105,"pushed_at":"2026-08-02T10:34:06Z","description":"Automated Machine Learning on Kubernetes"},
        {"full_name":"kubeflow/examples","language":"Jsonnet","stars":1461,"forks":755,"open_issues":111,"pushed_at":"2025-04-14T01:54:52Z","description":"Extended examples and tutorials"},
        {"full_name":"kubeflow/community-distribution","language":"YAML","stars":1029,"forks":1068,"open_issues":29,"pushed_at":"2026-07-29T12:00:24Z","description":"Kubeflow Community Distribution"},
        {"full_name":"kubeflow/arena","language":"Go","stars":816,"forks":196,"open_issues":44,"pushed_at":"2026-07-29T06:03:45Z","description":"A CLI for Kubeflow"},
        {"full_name":"kubeflow/kale","language":"Python","stars":699,"forks":158,"open_issues":55,"pushed_at":"2026-08-01T09:57:23Z","description":"Kubeflow's superfood for Data Scientists"},
        {"full_name":"kubeflow/mpi-operator","language":"Go","stars":530,"forks":238,"open_issues":102,"pushed_at":"2026-07-28T08:49:54Z","description":"Kubernetes Operator for MPI-based applications"},
        {"full_name":"kubeflow/mcp-apache-spark-history-server","language":"Python","stars":185,"forks":66,"open_issues":20,"pushed_at":"2026-07-16T20:57:58Z","description":"MCP Server for Apache Spark History Server"},
        {"full_name":"kubeflow/hub","language":"Go","stars":180,"forks":191,"open_issues":22,"pushed_at":"2026-07-31T21:11:52Z","description":"Model Registry for ML models"},
        {"full_name":"kubeflow/community","language":"Jupyter Notebook","stars":195,"forks":266,"open_issues":14,"pushed_at":"2026-07-31T16:41:48Z","description":"Kubeflow community information"},
        {"full_name":"kubeflow/website","language":"HTML","stars":185,"forks":928,"open_issues":22,"pushed_at":"2026-08-02T06:13:52Z","description":"Kubeflow Website"},
        {"full_name":"kubeflow/sdk","language":"Python","stars":131,"forks":228,"open_issues":238,"pushed_at":"2026-07-29T22:58:04Z","description":"Universal Python SDK to run AI workloads on Kubernetes"},
    ],
    "org:TeglonLabs": [
        {"full_name":"TeglonLabs/jank-crane","language":"C++","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-06-08T19:03:03Z","description":"crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps"},
        {"full_name":"TeglonLabs/mathpix-gem","language":"Ruby","stars":2,"forks":0,"open_issues":11,"pushed_at":"2026-01-01T12:13:13Z","description":"Transform mathematical images to LaTeX with security-first design"},
        {"full_name":"TeglonLabs/coin-flip-mcp","language":"JavaScript","stars":0,"forks":2,"open_issues":1,"pushed_at":"2025-09-21T08:57:27Z","description":"MCP server for flipping coins from random.org"},
        {"full_name":"TeglonLabs/monad-mcp-server","language":None,"stars":0,"forks":0,"open_issues":0,"pushed_at":"2025-05-14T11:36:14Z","description":"Monad MCP Server"},
        {"full_name":"TeglonLabs/topoi","language":"Python","stars":0,"forks":0,"open_issues":1,"pushed_at":"2025-01-24T04:49:26Z","description":None},
    ],
    "user:bmorphism": [
        {"full_name":"bmorphism/ocaml-mcp-sdk","language":"OCaml","stars":61,"forks":2,"open_issues":0,"pushed_at":"2026-03-16T05:24:25Z","description":"OCaml SDK for Model Context Protocol"},
        {"full_name":"bmorphism/anti-bullshit-mcp-server","language":"JavaScript","stars":23,"forks":7,"open_issues":1,"pushed_at":"2026-01-16T08:54:58Z","description":"MCP server for analyzing claims and detecting manipulation"},
        {"full_name":"bmorphism/shitcoin","language":"Python","stars":5,"forks":0,"open_issues":0,"pushed_at":"2026-04-08T08:07:08Z","description":"gets denom for cw20 assets for permissionless degeneracy in IBC"},
        {"full_name":"bmorphism/open-location-code-zig","language":"Zig","stars":3,"forks":0,"open_issues":0,"pushed_at":"2025-12-30T19:33:45Z","description":"Open Location Code (Plus Codes) for Zig"},
        {"full_name":"bmorphism/Gay.jl","language":"Julia","stars":2,"forks":1,"open_issues":188,"pushed_at":"2026-08-03T02:39:28Z","description":"Wide-gamut color sampling with splittable determinism"},
        {"full_name":"bmorphism/whale","language":"MATLAB","stars":2,"forks":0,"open_issues":0,"pushed_at":"2025-09-04T06:55:21Z","description":"omniglot + sperm whale codas = metawhaling"},
        {"full_name":"bmorphism/graphistry-mcp","language":"Python","stars":2,"forks":0,"open_issues":0,"pushed_at":"2025-05-06T17:34:24Z","description":"Graphistry MCP integration for graph visualization"},
        {"full_name":"bmorphism/monero-rental-hash-war","language":"Haskell","stars":1,"forks":0,"open_issues":0,"pushed_at":"2025-10-05T23:08:54Z","description":"Compositional OpenGame analysis of Monero rental hash war"},
        {"full_name":"bmorphism/schoenfinkel","language":"Python","stars":1,"forks":0,"open_issues":0,"pushed_at":"2025-10-04T23:31:11Z","description":"Post-quantum categorical gravity framework"},
        {"full_name":"bmorphism/bafishka","language":"Clojure","stars":1,"forks":0,"open_issues":0,"pushed_at":"2025-12-19T09:38:00Z","description":"Rust-native Fish shell-friendly file operations"},
    ],
    "user:zubyul": [
        {"full_name":"zubyul/jonikas_lab_data_analysis_misc","language":"Jupyter Notebook","stars":2,"forks":0,"open_issues":0,"pushed_at":"2023-08-16T20:24:40Z","description":"scripts used to process large genetic sequence data"},
        {"full_name":"zubyul/WGCNA","language":"HTML","stars":2,"forks":0,"open_issues":0,"pushed_at":"2023-07-05T18:02:30Z","description":"weighted gene correlation network analysis"},
        {"full_name":"zubyul/Nikolova_lab_data_analysis","language":"R","stars":2,"forks":0,"open_issues":0,"pushed_at":"2023-06-16T13:56:58Z","description":"undergraduate thesis - cortical thickness and transcription factors"},
        {"full_name":"zubyul/gay-world","language":"Python","stars":1,"forks":1,"open_issues":0,"pushed_at":"2026-03-26T04:03:39Z","description":"Goblin world builder: MLX task decomposition -> composable persistent worlds"},
        {"full_name":"zubyul/zubyul.github.io","language":"CSS","stars":1,"forks":0,"open_issues":0,"pushed_at":"2026-01-27T03:24:34Z","description":None},
        {"full_name":"zubyul/cascade-world","language":"Python","stars":1,"forks":0,"open_issues":0,"pushed_at":"2025-09-19T18:25:12Z","description":"Cascade development environment"},
        {"full_name":"zubyul/from-possible-worlds","language":"TeX","stars":0,"forks":1,"open_issues":1,"pushed_at":"2026-07-18T12:02:57Z","description":None},
        {"full_name":"zubyul/voice-observatory","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-24T05:56:17Z","description":"Passive macOS TUI observing voice-download pathways"},
        {"full_name":"zubyul/tilelang-kernels","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-03-16T02:31:13Z","description":"TileLang GPU kernels for SplitMix64 color generation"},
    ],
    "user:migalkin": [
        {"full_name":"migalkin/NodePiece","language":"Python","stars":144,"forks":21,"open_issues":0,"pushed_at":"2026-05-07T05:40:02Z","description":"Compositional Representations for Large Knowledge Graphs (ICLR'22)"},
        {"full_name":"migalkin/StarE","language":"Python","stars":89,"forks":16,"open_issues":1,"pushed_at":"2026-04-16T14:12:45Z","description":"Message Passing for Hyper-Relational Knowledge Graphs (EMNLP 2020)"},
        {"full_name":"migalkin/kgcourse2021","language":"HTML","stars":24,"forks":8,"open_issues":0,"pushed_at":"2026-07-10T15:40:00Z","description":"Knowledge Graphs course materials"},
        {"full_name":"migalkin/NBFNet_mlx","language":"Python","stars":10,"forks":1,"open_issues":1,"pushed_at":"2026-03-11T01:31:21Z","description":"Neural Bellman-Ford networks in MLX for Apple Silicon"},
        {"full_name":"migalkin/RWL","language":"Python","stars":8,"forks":1,"open_issues":0,"pushed_at":"2026-05-28T20:19:20Z","description":"Weisfeiler and Leman Go Relational (LOG 2022)"},
        {"full_name":"migalkin/rambo","language":"Rust","stars":3,"forks":0,"open_issues":1,"pushed_at":"2023-02-28T16:37:22Z","description":None},
        {"full_name":"migalkin/SMJoin-experiments","language":"R","stars":1,"forks":0,"open_issues":0,"pushed_at":"2020-03-04T15:56:23Z","description":"ISWC 2017 SMJoin results"},
    ],
    "user:wasita": [
        {"full_name":"wasita/wasita.github.io","language":"Svelte","stars":1,"forks":0,"open_issues":8,"pushed_at":"2026-07-21T15:55:45Z","description":"personal website"},
        {"full_name":"wasita/magic-garden","language":"Python","stars":2,"forks":1,"open_issues":1,"pushed_at":"2026-04-22T21:16:43Z","description":"bot for auto-purchasing seeds in Discord game"},
        {"full_name":"wasita/send2kobo","language":"TypeScript","stars":1,"forks":0,"open_issues":0,"pushed_at":"2026-05-19T02:59:26Z","description":"Website for sending books to kobo e-reader"},
        {"full_name":"wasita/wins-search","language":"CSS","stars":1,"forks":0,"open_issues":0,"pushed_at":"2023-06-03T19:01:11Z","description":"Women in Network Science member list website"},
    ],
    "user:DJedamski": [
        {"full_name":"DJedamski/kaggle_ncaa18","language":"Jupyter Notebook","stars":0,"forks":0,"open_issues":0,"pushed_at":"2018-02-26T16:33:24Z","description":"NCAA March Madness competition (2018)"},
        {"full_name":"DJedamski/Kaggle","language":None,"stars":1,"forks":0,"open_issues":0,"pushed_at":"2023-04-21T01:42:35Z","description":None},
        {"full_name":"DJedamski/Getting-and-Cleaning-Data","language":"R","stars":1,"forks":0,"open_issues":0,"pushed_at":"2023-04-21T01:42:34Z","description":"Coursera Project"},
        {"full_name":"DJedamski/School","language":"R","stars":1,"forks":1,"open_issues":0,"pushed_at":"2023-04-21T01:42:33Z","description":"Small projects from grad school"},
    ],
    "user:kristinezheng": [
        {"full_name":"kristinezheng/kristinezheng.github.io","language":"HTML","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-07-01T20:57:48Z","description":None},
        {"full_name":"kristinezheng/lookit-jenga","language":"Jupyter Notebook","stars":0,"forks":0,"open_issues":0,"pushed_at":"2024-05-16T18:29:05Z","description":"Lookit study for 9.85"},
    ],
    "user:M1shaaa": [
        {"full_name":"M1shaaa/lab-bookshelf-","language":"TypeScript","stars":0,"forks":0,"open_issues":0,"pushed_at":"2024-12-31T05:11:18Z","description":None},
        {"full_name":"M1shaaa/Python-Lookit-Uploads","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2024-02-15T22:59:37Z","description":"random projects"},
    ],
    "user:AustinCStone": [
        {"full_name":"AustinCStone/TextGAN","language":"Python","stars":92,"forks":30,"open_issues":5,"pushed_at":"2025-03-03T13:26:32Z","description":"A generative adversarial network for text generation in TensorFlow"},
        {"full_name":"AustinCStone/StereoVisionMRF","language":"Python","stars":11,"forks":4,"open_issues":0,"pushed_at":"2026-04-01T07:39:41Z","description":"MRF with loopy belief propagation for stereo depth"},
        {"full_name":"AustinCStone/StructureFromMotion","language":"Python","stars":1,"forks":0,"open_issues":0,"pushed_at":"2019-04-26T19:43:12Z","description":"Recover 3D geometry from videos"},
        {"full_name":"AustinCStone/SpectralClustering","language":"Python","stars":3,"forks":2,"open_issues":0,"pushed_at":"2021-04-16T08:46:36Z","description":"Spectral clustering homework"},
        {"full_name":"AustinCStone/byteruckus","language":"HTML","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-07-15T05:19:33Z","description":None},
    ],
}

# Aptos wallets
APTOS_WALLETS = [
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

MULTISIGS = [
    ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2,True),
    ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2,True),
    ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2,True),
    ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2,True),
    ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2,True),
]

# Get current max id
try:
    row = con.execute("SELECT COALESCE(MAX(id), 0) FROM world_increments").fetchone()
    current_id = row[0] if row else 0
except:
    current_id = 0

increment_rows = []
repo_rows = []
inc_id = current_id + 1

ts = "2026-08-03 00:00:00"

for source_key, repos in REPOS.items():
    source_type, source_name = source_key.split(":", 1)
    for repo in repos:
        trit, color, name = gf3(inc_id)
        h = hashlib.sha256(f"{repo['full_name']}{repo['pushed_at']}".encode()).hexdigest()[:16]
        increment_rows.append((
            inc_id, ts, trit, color, name,
            source_type, source_name, "repo_snapshot",
            repo["full_name"], source_name, h
        ))
        org_user = repo["full_name"].split("/")[0]
        repo_rows.append((
            inc_id, ts, inc_id,
            org_user, repo["full_name"].split("/")[1], repo["full_name"],
            repo.get("language"), repo.get("stars", 0), repo.get("forks", 0),
            repo.get("open_issues", 0), repo.get("pushed_at"), repo.get("description")
        ))
        inc_id += 1

# Insert world_increments
con.executemany("""
INSERT INTO world_increments (id, timestamp, gf3_trit, gf3_color, gf3_name, source_type, source_name, event_type, repo_name, actor, snapshot_hash)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", increment_rows)

# Insert repo_snapshots
con.executemany("""
INSERT INTO repo_snapshots (id, timestamp, increment_id, org_or_user, repo_name, full_name, language, stars, forks, open_issues, pushed_at, description)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", repo_rows)

# Insert Aptos snapshots
con.executemany("""
INSERT INTO aptos_snapshots (timestamp, world, address, balance_apt)
VALUES (?, ?, ?, ?)
""", [(ts, w, a, b) for w, a, b in APTOS_WALLETS])

# Insert multisig probes
con.executemany("""
INSERT INTO multisig_probes (timestamp, pair, address, sigs_required, healthy)
VALUES (?, ?, ?, ?, ?)
""", [(ts, p, a, s, h) for p, a, s, h in MULTISIGS])

# Verification counts
r1 = con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0]
r2 = con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0]
r3 = con.execute("SELECT COUNT(*) FROM aptos_snapshots").fetchone()[0]
r4 = con.execute("SELECT COUNT(*) FROM multisig_probes").fetchone()[0]

# GF3 distribution
gf3_dist = con.execute("""
SELECT gf3_name, gf3_color, COUNT(*) as cnt
FROM world_increments
GROUP BY gf3_name, gf3_color
ORDER BY gf3_name
""").fetchall()

# Top repos by stars
top_repos = con.execute("""
SELECT full_name, stars, language, org_or_user
FROM repo_snapshots
ORDER BY stars DESC
LIMIT 10
""").fetchall()

print(f"world_increments: {r1} rows")
print(f"repo_snapshots: {r2} rows")
print(f"aptos_snapshots: {r3} rows")
print(f"multisig_probes: {r4} rows")
print(f"GF3 distribution: {gf3_dist}")
print(f"Top repos: {top_repos}")

con.close()
print("Done.")
