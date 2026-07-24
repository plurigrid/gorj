#!/usr/bin/env python3
"""World-increment sweep + Hamming swarm snapshot builder."""
import duckdb, json, hashlib

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
con = duckdb.connect(DB)

# Schema
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

# GF3 color map
GF3 = {0: (0, "#d3869b", "ERGODIC"), 1: (1, "#b8bb26", "PLUS"), 2: (-1, "#cc241d", "MINUS")}

def gf3(n):
    k = n % 3
    trit, color, name = GF3[k]
    return trit, color, name

# --- REPO DATA ---
sources = [
    ("org", "plurigrid", [
        {"name":"asi","full_name":"plurigrid/asi","language":"HTML","stargazers_count":31,"forks_count":10,"open_issues_count":4,"updated_at":"2026-07-17T14:18:23Z","description":"everything is topological chemputer!"},
        {"name":"ontology","full_name":"plurigrid/ontology","language":"JavaScript","stargazers_count":8,"forks_count":9,"open_issues_count":16,"updated_at":"2026-05-09T04:20:49Z","description":"autopoietic ergodicity and embodied gradualism"},
        {"name":"vcg-auction","full_name":"plurigrid/vcg-auction","language":"Rust","stargazers_count":7,"forks_count":3,"open_issues_count":1,"updated_at":"2025-12-16T12:32:02Z","description":"a simple contract that performs a VCG auction"},
        {"name":"agent","full_name":"plurigrid/agent","language":"Python","stargazers_count":5,"forks_count":1,"open_issues_count":6,"updated_at":"2024-10-16T11:33:13Z","description":"Framework for agency amplification"},
        {"name":"gorj","full_name":"plurigrid/gorj","language":"Clojure","stargazers_count":1,"forks_count":0,"open_issues_count":1371,"updated_at":"2026-07-07T19:20:50Z","description":"forj + Rama topology nREPL routing + GF(3) gay trit coloring"},
        {"name":"nanoclj-zig","full_name":"plurigrid/nanoclj-zig","language":"Zig","stargazers_count":1,"forks_count":1,"open_issues_count":20,"updated_at":"2026-04-25T07:29:13Z","description":"NaN-boxed Clojure interpreter in Zig 0.15"},
        {"name":"nash-portal","full_name":"plurigrid/nash-portal","language":"Rust","stargazers_count":2,"forks_count":2,"open_issues_count":1,"updated_at":"2026-05-19T01:50:03Z","description":"NASH token TUI in the browser"},
        {"name":"zig-syrup","full_name":"plurigrid/zig-syrup","language":"Zig","stargazers_count":2,"forks_count":2,"open_issues_count":0,"updated_at":"2026-04-30T03:52:19Z","description":"High-performance Zig implementation of OCapN Syrup"},
        {"name":"place","full_name":"plurigrid/place","language":"TeX","stargazers_count":1,"forks_count":2,"open_issues_count":14,"updated_at":"2026-06-27T22:03:34Z","description":None},
        {"name":"asi-skills","full_name":"plurigrid/asi-skills","language":"Julia","stargazers_count":3,"forks_count":0,"open_issues_count":0,"updated_at":"2026-04-26T08:09:31Z","description":"69 skills with Galois Hole Type accessibility"},
    ]),
    ("org", "kubeflow", [
        {"name":"kubeflow","full_name":"kubeflow/kubeflow","language":"Go","stargazers_count":15792,"forks_count":2686,"open_issues_count":0,"updated_at":"2026-07-24T10:21:46Z","description":"Machine Learning Toolkit for Kubernetes"},
        {"name":"pipelines","full_name":"kubeflow/pipelines","language":"Python","stargazers_count":4169,"forks_count":2057,"open_issues_count":457,"updated_at":"2026-07-24T15:51:20Z","description":"Machine Learning Pipelines for Kubeflow"},
        {"name":"spark-operator","full_name":"kubeflow/spark-operator","language":"Python","stargazers_count":3143,"forks_count":1504,"open_issues_count":110,"updated_at":"2026-07-23T10:39:46Z","description":"Kubernetes operator for managing Apache Spark"},
        {"name":"trainer","full_name":"kubeflow/trainer","language":"Go","stargazers_count":2153,"forks_count":995,"open_issues_count":100,"updated_at":"2026-07-24T01:59:23Z","description":"Distributed AI Model Training and LLM Fine-Tuning on Kubernetes"},
        {"name":"katib","full_name":"kubeflow/katib","language":"Python","stargazers_count":1692,"forks_count":532,"open_issues_count":104,"updated_at":"2026-07-20T22:47:05Z","description":"Automated Machine Learning on Kubernetes"},
        {"name":"mcp-server","full_name":"kubeflow/mcp-server","language":"Python","stargazers_count":29,"forks_count":37,"open_issues_count":34,"updated_at":"2026-07-24T11:53:14Z","description":"MCP Server for AI-Assisted Development with Kubeflow Tools"},
        {"name":"hub","full_name":"kubeflow/hub","language":"Go","stargazers_count":178,"forks_count":188,"open_issues_count":28,"updated_at":"2026-07-24T13:07:32Z","description":"Model Registry for ML models"},
        {"name":"notebooks","full_name":"kubeflow/notebooks","language":None,"stargazers_count":74,"forks_count":132,"open_issues_count":164,"updated_at":"2026-07-23T19:24:54Z","description":"Kubeflow Notebooks"},
    ]),
    ("org", "TeglonLabs", [
        {"name":"mathpix-gem","full_name":"TeglonLabs/mathpix-gem","language":"Ruby","stargazers_count":2,"forks_count":0,"open_issues_count":11,"updated_at":"2026-01-01T12:13:16Z","description":"Transform mathematical images to LaTeX"},
        {"name":"topoi","full_name":"TeglonLabs/topoi","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":1,"updated_at":"2025-01-24T06:47:38Z","description":None},
        {"name":"jank-crane","full_name":"TeglonLabs/jank-crane","language":"C++","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-06-08T19:03:37Z","description":"crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps"},
        {"name":"monad-mcp-server","full_name":"TeglonLabs/monad-mcp-server","language":None,"stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2025-05-14T17:53:01Z","description":"Monad MCP Server"},
        {"name":"coin-flip-mcp","full_name":"TeglonLabs/coin-flip-mcp","language":"JavaScript","stargazers_count":0,"forks_count":2,"open_issues_count":1,"updated_at":"2025-03-16T01:31:45Z","description":"MCP server for flipping coins"},
    ]),
    ("user", "bmorphism", [
        {"name":"ocaml-mcp-sdk","full_name":"bmorphism/ocaml-mcp-sdk","language":"OCaml","stargazers_count":61,"forks_count":2,"open_issues_count":0,"updated_at":"2026-05-08T16:50:34Z","description":"OCaml SDK for Model Context Protocol"},
        {"name":"anti-bullshit-mcp-server","full_name":"bmorphism/anti-bullshit-mcp-server","language":"JavaScript","stargazers_count":22,"forks_count":7,"open_issues_count":1,"updated_at":"2026-07-12T19:31:54Z","description":"MCP server for analyzing claims"},
        {"name":"babashka-mcp-server","full_name":"bmorphism/babashka-mcp-server","language":"JavaScript","stargazers_count":19,"forks_count":6,"open_issues_count":3,"updated_at":"2026-06-05T13:16:11Z","description":"MCP server for Babashka Clojure"},
        {"name":"Gay.jl","full_name":"bmorphism/Gay.jl","language":"Julia","stargazers_count":2,"forks_count":1,"open_issues_count":187,"updated_at":"2026-07-21T12:57:35Z","description":"Wide-gamut color sampling with splittable determinism"},
        {"name":"nanoclj-zig","full_name":"bmorphism/nanoclj-zig","language":"Zig","stargazers_count":1,"forks_count":0,"open_issues_count":0,"updated_at":"2026-06-10T16:00:16Z","description":None},
        {"name":"manifold-mcp-server","full_name":"bmorphism/manifold-mcp-server","language":"JavaScript","stargazers_count":14,"forks_count":9,"open_issues_count":5,"updated_at":"2026-04-15T19:54:28Z","description":"MCP server for Manifold Markets prediction markets"},
        {"name":"magic-world-org","full_name":"bmorphism/magic-world-org","language":"Python","stargazers_count":1,"forks_count":0,"open_issues_count":0,"updated_at":"2026-05-01T01:06:25Z","description":"Magic World Org (Local MLX)"},
    ]),
    ("user", "zubyul", [
        {"name":"gay-world","full_name":"zubyul/gay-world","language":"Python","stargazers_count":1,"forks_count":1,"open_issues_count":0,"updated_at":"2026-04-05T06:54:03Z","description":"Goblin world builder: each goblin is a world"},
        {"name":"WGCNA","full_name":"zubyul/WGCNA","language":"HTML","stargazers_count":2,"forks_count":0,"open_issues_count":0,"updated_at":"2026-03-26T09:05:26Z","description":"weighted gene correlation network analysis project"},
        {"name":"jonikas_lab_data_analysis_misc","full_name":"zubyul/jonikas_lab_data_analysis_misc","language":"Jupyter Notebook","stargazers_count":2,"forks_count":0,"open_issues_count":0,"updated_at":"2026-03-26T09:05:21Z","description":"various scripts to process large genetic sequence data"},
        {"name":"tilelang-kernels","full_name":"zubyul/tilelang-kernels","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-03-16T02:31:16Z","description":"TileLang GPU kernels for SplitMix64 color generation"},
        {"name":"kinesis-kb360pro","full_name":"zubyul/kinesis-kb360pro","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-03-26T10:29:44Z","description":"Claude Code skill for Kinesis Advantage360 Pro keyboard"},
    ]),
    ("user", "migalkin", [
        {"name":"NodePiece","full_name":"migalkin/NodePiece","language":"Python","stargazers_count":144,"forks_count":21,"open_issues_count":0,"updated_at":"2026-05-07T05:40:02Z","description":"Compositional and Parameter-Efficient Representations for Large Knowledge Graphs (ICLR'22)"},
        {"name":"StarE","full_name":"migalkin/StarE","language":"Python","stargazers_count":89,"forks_count":16,"open_issues_count":1,"updated_at":"2026-04-16T14:12:45Z","description":"EMNLP 2020: Message Passing for Hyper-Relational Knowledge Graphs"},
        {"name":"kgcourse2021","full_name":"migalkin/kgcourse2021","language":"HTML","stargazers_count":24,"forks_count":8,"open_issues_count":0,"updated_at":"2026-07-10T15:40:00Z","description":"Материалы к курсу по Knowledge Graphs"},
        {"name":"NBFNet_mlx","full_name":"migalkin/NBFNet_mlx","language":"Python","stargazers_count":10,"forks_count":1,"open_issues_count":1,"updated_at":"2026-03-11T01:31:21Z","description":"Neural Bellman-Ford networks implemented in MLX for Apple Silicon"},
    ]),
    ("user", "DJedamski", [
        {"name":"Getting-and-Cleaning-Data","full_name":"DJedamski/Getting-and-Cleaning-Data","language":"R","stargazers_count":1,"forks_count":0,"open_issues_count":0,"updated_at":"2023-04-21T01:42:34Z","description":"Coursera Project"},
        {"name":"Kaggle","full_name":"DJedamski/Kaggle","language":None,"stargazers_count":1,"forks_count":0,"open_issues_count":0,"updated_at":"2023-04-21T01:42:35Z","description":None},
        {"name":"School","full_name":"DJedamski/School","language":"R","stargazers_count":1,"forks_count":1,"open_issues_count":0,"updated_at":"2023-04-21T01:42:33Z","description":"A couple small projects from grad school"},
    ]),
    ("user", "wasita", [
        {"name":"magic-garden","full_name":"wasita/magic-garden","language":"Python","stargazers_count":2,"forks_count":1,"open_issues_count":1,"updated_at":"2026-04-22T21:16:43Z","description":"a bot for the magic garden discord activity game"},
        {"name":"wasita.github.io","full_name":"wasita/wasita.github.io","language":"Svelte","stargazers_count":1,"forks_count":0,"open_issues_count":8,"updated_at":"2026-07-21T15:55:45Z","description":"personal website"},
        {"name":"send2kobo","full_name":"wasita/send2kobo","language":"TypeScript","stargazers_count":1,"forks_count":0,"open_issues_count":0,"updated_at":"2026-05-19T02:59:26Z","description":"Website for sending books to your kobo e-reader"},
    ]),
    ("user", "kristinezheng", [
        {"name":"Green-Machine","full_name":"kristinezheng/Green-Machine","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2021-09-19T05:33:04Z","description":"HackMIT 2021: Sustainability Track"},
        {"name":"lookit-jenga","full_name":"kristinezheng/lookit-jenga","language":"Jupyter Notebook","stargazers_count":0,"forks_count":0,"open_issues_count":1,"updated_at":"2024-05-16T18:29:05Z","description":"Lookit study for 9.85"},
        {"name":"kristinezheng.github.io","full_name":"kristinezheng/kristinezheng.github.io","language":"HTML","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-07-01T20:57:48Z","description":None},
    ]),
    ("user", "M1shaaa", [
        {"name":"lab-bookshelf-","full_name":"M1shaaa/lab-bookshelf-","language":"TypeScript","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2024-12-31T05:11:18Z","description":None},
        {"name":"M1shaaa","full_name":"M1shaaa/M1shaaa","language":None,"stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-02-04T19:32:04Z","description":"Config files for my GitHub profile."},
    ]),
    ("user", "AustinCStone", [
        {"name":"TextGAN","full_name":"AustinCStone/TextGAN","language":"Python","stargazers_count":92,"forks_count":30,"open_issues_count":5,"updated_at":"2025-03-03T13:26:32Z","description":"A generative adversarial network for text generation"},
        {"name":"StereoVisionMRF","full_name":"AustinCStone/StereoVisionMRF","language":"Python","stargazers_count":11,"forks_count":4,"open_issues_count":0,"updated_at":"2026-04-01T07:39:41Z","description":"Using MRF with loopy belief propagation to infer depth from stereo images"},
        {"name":"byteruckus","full_name":"AustinCStone/byteruckus","language":"HTML","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-07-15T05:19:33Z","description":None},
    ]),
]

# Insert repo snapshots
increment_id = 0
repo_id = 0
for source_type, source_name, repos in sources:
    for repo in repos:
        increment_id += 1
        repo_id += 1
        trit, color, gf3_name = gf3(increment_id)
        snap_hash = hashlib.sha256(f"{source_name}/{repo['full_name']}/{repo.get('updated_at','')}".encode()).hexdigest()[:16]
        con.execute("""
            INSERT INTO world_increments VALUES (?, now(), ?, ?, ?, ?, ?, 'repo_push', ?, ?, ?)
        """, [increment_id, trit, color, gf3_name, source_type, source_name, repo['name'], source_name, snap_hash])
        con.execute("""
            INSERT INTO repo_snapshots VALUES (?, now(), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, [repo_id, increment_id, source_name, repo['name'], repo['full_name'],
              repo.get('language'), repo.get('stargazers_count',0), repo.get('forks_count',0),
              repo.get('open_issues_count',0), repo.get('updated_at',''), repo.get('description')])

print(f"Inserted {increment_id} world_increments, {repo_id} repo_snapshots")

# --- APTOS SNAPSHOTS ---
aptos_data = [
    ("alice","0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b",0),
    ("bob","0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d",0),
    ("A","0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a",0),
    ("B","0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13",0),
    ("C","0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e",0),
    ("D","0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1",0),
    ("E","0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36",0),
    ("F","0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71",0),
    ("G","0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32",0),
    ("H","0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f",0),
    ("I","0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9",0),
    ("J","0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54",0),
    ("K","0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4",0),
    ("L","0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9",0),
    ("M","0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9",0),
    ("N","0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c",0),
    ("O","0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d",0),
    ("P","0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948",0),
    ("Q","0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9",0),
    ("R","0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10",0),
    ("S","0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386",0),
    ("T","0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588",0),
    ("U","0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956",0),
    ("V","0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3",0),
    ("W","0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0",0),
    ("X","0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d",0),
    ("Y","0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4",0),
    ("Z","0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c",0),
]
for world, addr, bal in aptos_data:
    con.execute("INSERT INTO aptos_snapshots VALUES (now(), ?, ?, ?)", [world, addr, bal/100000000])
print(f"Inserted {len(aptos_data)} aptos_snapshots")

# --- MULTISIG PROBES ---
multisig_data = [
    ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2),
    ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2),
    ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2),
    ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2),
    ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2),
]
for pair, addr, sigs in multisig_data:
    con.execute("INSERT INTO multisig_probes VALUES (now(), ?, ?, ?, ?)", [pair, addr, sigs, True])
print(f"Inserted {len(multisig_data)} multisig_probes")

# --- MNX SNAPSHOTS: unavailable ---
# testnet.mnx.fi returns SPA shell with no data; no rows inserted

con.close()
print("DB build complete.")
