#!/usr/bin/env python3
"""Build world-increment ducklake: GitHub social graph + Aptos hamming swarm snapshot."""

import duckdb
import hashlib
import json
from datetime import datetime

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
con = duckdb.connect(DB_PATH)

# Create tables
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

# GF(3) color chain
def gf3(idx):
    t = idx % 3
    if t == 0:   return (0, "#d3869b", "ERGODIC")
    elif t == 1: return (1, "#b8bb26", "PLUS")
    else:        return (-1, "#cc241d", "MINUS")

def snap_hash(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()[:16]

# All repo data collected
repos = [
    # plurigrid (50 repos from agent)
    {"org_or_user":"plurigrid","repo_name":"asi","full_name":"plurigrid/asi","language":"HTML","stars":28,"forks":8,"open_issues":4,"pushed_at":"2026-06-29T03:15:56Z","description":"everything is topological chemputer!"},
    {"org_or_user":"plurigrid","repo_name":"place","full_name":"plurigrid/place","language":"TeX","stars":1,"forks":1,"open_issues":12,"pushed_at":"2026-06-29T20:40:59Z","description":None},
    {"org_or_user":"plurigrid","repo_name":"eirobri","full_name":"plurigrid/eirobri","language":"Clojure","stars":0,"forks":0,"open_issues":30,"pushed_at":"2026-06-30T02:23:56Z","description":"EiRoBri replay world"},
    {"org_or_user":"plurigrid","repo_name":"nash-portal","full_name":"plurigrid/nash-portal","language":"Rust","stars":2,"forks":3,"open_issues":1,"pushed_at":"2026-05-19T01:49:59Z","description":"NASH token TUI in the browser"},
    {"org_or_user":"plurigrid","repo_name":"gorj","full_name":"plurigrid/gorj","language":"Clojure","stars":0,"forks":0,"open_issues":924,"pushed_at":"2026-07-02T20:15:27Z","description":"forj + Rama topology nREPL routing + GF(3) gay trit coloring"},
    {"org_or_user":"plurigrid","repo_name":"zig-syrup","full_name":"plurigrid/zig-syrup","language":"Zig","stars":2,"forks":2,"open_issues":0,"pushed_at":"2026-04-30T03:52:16Z","description":"High-performance Zig OCapN Syrup"},
    {"org_or_user":"plurigrid","repo_name":"asi-skills","full_name":"plurigrid/asi-skills","language":"Julia","stars":3,"forks":0,"open_issues":0,"pushed_at":"2026-04-26T08:09:26Z","description":"69 skills with Galois Hole Type accessibility"},
    {"org_or_user":"plurigrid","repo_name":"nanoclj-zig","full_name":"plurigrid/nanoclj-zig","language":"Zig","stars":1,"forks":1,"open_issues":20,"pushed_at":"2026-04-25T07:29:01Z","description":"NaN-boxed Clojure interpreter in Zig 0.15"},
    {"org_or_user":"plurigrid","repo_name":"ontology","full_name":"plurigrid/ontology","language":"JavaScript","stars":8,"forks":9,"open_issues":16,"pushed_at":"2025-05-27T18:18:34Z","description":"autopoietic ergodicity and embodied gradualism"},
    {"org_or_user":"plurigrid","repo_name":"Plurigraph","full_name":"plurigrid/Plurigraph","language":"JavaScript","stars":3,"forks":5,"open_issues":4,"pushed_at":"2025-01-05T08:39:09Z","description":"Plurigrid knowledge base for use with Obsidian.md"},
    # TeglonLabs (5 repos)
    {"org_or_user":"TeglonLabs","repo_name":"jank-crane","full_name":"TeglonLabs/jank-crane","language":"C++","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-06-08T19:03:03Z","description":"crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps"},
    {"org_or_user":"TeglonLabs","repo_name":"mathpix-gem","full_name":"TeglonLabs/mathpix-gem","language":"Ruby","stars":2,"forks":0,"open_issues":11,"pushed_at":"2026-01-01T12:13:13Z","description":"Transform mathematical images to LaTeX"},
    {"org_or_user":"TeglonLabs","repo_name":"coin-flip-mcp","full_name":"TeglonLabs/coin-flip-mcp","language":"JavaScript","stars":0,"forks":2,"open_issues":1,"pushed_at":"2025-09-21T08:57:27Z","description":"MCP server for flipping coins"},
    {"org_or_user":"TeglonLabs","repo_name":"monad-mcp-server","full_name":"TeglonLabs/monad-mcp-server","language":None,"stars":0,"forks":0,"open_issues":0,"pushed_at":"2025-05-14T11:36:14Z","description":"Monad MCP Server"},
    {"org_or_user":"TeglonLabs","repo_name":"topoi","full_name":"TeglonLabs/topoi","language":"Python","stars":0,"forks":0,"open_issues":1,"pushed_at":"2025-01-24T04:49:26Z","description":None},
    # kubeflow (top 10 by stars)
    {"org_or_user":"kubeflow","repo_name":"kubeflow","full_name":"kubeflow/kubeflow","language":None,"stars":15757,"forks":2683,"open_issues":0,"pushed_at":"2026-06-18T11:45:16Z","description":"Machine Learning Toolkit for Kubernetes"},
    {"org_or_user":"kubeflow","repo_name":"pipelines","full_name":"kubeflow/pipelines","language":"Python","stars":4167,"forks":2020,"open_issues":413,"pushed_at":"2026-07-02T19:45:12Z","description":"Machine Learning Pipelines for Kubeflow"},
    {"org_or_user":"kubeflow","repo_name":"spark-operator","full_name":"kubeflow/spark-operator","language":"Python","stars":3130,"forks":1496,"open_issues":103,"pushed_at":"2026-07-02T08:52:01Z","description":"Kubernetes operator for Apache Spark"},
    {"org_or_user":"kubeflow","repo_name":"trainer","full_name":"kubeflow/trainer","language":"Go","stars":2129,"forks":974,"open_issues":142,"pushed_at":"2026-07-02T15:21:32Z","description":"Distributed AI Model Training on Kubernetes"},
    {"org_or_user":"kubeflow","repo_name":"katib","full_name":"kubeflow/katib","language":"Python","stars":1688,"forks":529,"open_issues":114,"pushed_at":"2026-07-01T21:20:57Z","description":"Automated Machine Learning on Kubernetes"},
    {"org_or_user":"kubeflow","repo_name":"examples","full_name":"kubeflow/examples","language":"Jsonnet","stars":1460,"forks":756,"open_issues":111,"pushed_at":"2025-04-14T01:54:52Z","description":"Extended examples and tutorials"},
    {"org_or_user":"kubeflow","repo_name":"community-distribution","full_name":"kubeflow/community-distribution","language":"YAML","stars":1028,"forks":1067,"open_issues":27,"pushed_at":"2026-06-30T15:20:24Z","description":"Kubeflow Community Distribution"},
    {"org_or_user":"kubeflow","repo_name":"arena","full_name":"kubeflow/arena","language":"Go","stars":814,"forks":194,"open_issues":48,"pushed_at":"2026-07-02T08:52:11Z","description":"A CLI for Kubeflow"},
    {"org_or_user":"kubeflow","repo_name":"kale","full_name":"kubeflow/kale","language":"Python","stars":694,"forks":156,"open_issues":38,"pushed_at":"2026-07-01T12:44:49Z","description":"Kubeflow superfood for Data Scientists"},
    {"org_or_user":"kubeflow","repo_name":"sdk","full_name":"kubeflow/sdk","language":"Python","stars":123,"forks":187,"open_issues":138,"pushed_at":"2026-07-02T19:23:35Z","description":"Universal Python SDK for AI workloads on Kubernetes"},
    # bmorphism (top repos)
    {"org_or_user":"bmorphism","repo_name":"Gay.jl","full_name":"bmorphism/Gay.jl","language":"Julia","stars":2,"forks":1,"open_issues":187,"pushed_at":"2026-07-02T00:40:16Z","description":"Wide-gamut color sampling with splittable determinism"},
    {"org_or_user":"bmorphism","repo_name":"ocaml-mcp-sdk","full_name":"bmorphism/ocaml-mcp-sdk","language":"OCaml","stars":61,"forks":2,"open_issues":0,"pushed_at":"2026-03-16T05:24:25Z","description":"OCaml SDK for Model Context Protocol"},
    {"org_or_user":"bmorphism","repo_name":"anti-bullshit-mcp-server","full_name":"bmorphism/anti-bullshit-mcp-server","language":"JavaScript","stars":23,"forks":7,"open_issues":1,"pushed_at":"2026-01-16T08:54:58Z","description":"MCP server for analyzing claims and detecting manipulation"},
    {"org_or_user":"bmorphism","repo_name":"satreadout","full_name":"bmorphism/satreadout","language":"HTML","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-06-20T13:05:41Z","description":"Machine-checked saturating non-Riemannian perceptual readout"},
    {"org_or_user":"bmorphism","repo_name":"vibespace-mcp-go-ternary","full_name":"bmorphism/vibespace-mcp-go-ternary","language":"HTML","stars":0,"forks":1,"open_issues":3,"pushed_at":"2026-01-11T12:50:40Z","description":"Go MCP for vibes and worlds with balanced ternary support"},
    # zubyul (top repos)
    {"org_or_user":"zubyul","repo_name":"gay-world","full_name":"zubyul/gay-world","language":"Python","stars":1,"forks":1,"open_issues":0,"pushed_at":"2026-03-26T04:03:39Z","description":"Goblin world builder: each goblin is a world"},
    {"org_or_user":"zubyul","repo_name":"nash-tui","full_name":"zubyul/nash-tui","language":"Rust","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-13T07:45:16Z","description":"NASH token TUI: real-time candles"},
    {"org_or_user":"zubyul","repo_name":"voice-observatory","full_name":"zubyul/voice-observatory","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-24T05:56:17Z","description":"Passive macOS TUI observing voice-download pathways"},
    {"org_or_user":"zubyul","repo_name":"tilelang-kernels","full_name":"zubyul/tilelang-kernels","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-03-16T02:31:13Z","description":"TileLang GPU kernels for SplitMix64 color generation"},
    # migalkin (top repos)
    {"org_or_user":"migalkin","repo_name":"NodePiece","full_name":"migalkin/NodePiece","language":"Python","stars":144,"forks":21,"open_issues":0,"pushed_at":"2026-05-07T05:40:02Z","description":"Compositional Representations for Large Knowledge Graphs (ICLR'22)"},
    {"org_or_user":"migalkin","repo_name":"StarE","full_name":"migalkin/StarE","language":"Python","stars":89,"forks":16,"open_issues":1,"pushed_at":"2026-04-16T14:12:45Z","description":"EMNLP 2020: Message Passing for Hyper-Relational Knowledge Graphs"},
    {"org_or_user":"migalkin","repo_name":"kgcourse2021","full_name":"migalkin/kgcourse2021","language":"HTML","stars":25,"forks":9,"open_issues":0,"pushed_at":"2026-02-16T05:16:08Z","description":"Knowledge Graphs course materials"},
    {"org_or_user":"migalkin","repo_name":"NBFNet_mlx","full_name":"migalkin/NBFNet_mlx","language":"Python","stars":10,"forks":1,"open_issues":1,"pushed_at":"2026-03-11T01:31:21Z","description":"Neural Bellman-Ford networks in MLX for Apple Silicon"},
    # wasita
    {"org_or_user":"wasita","repo_name":"wasita.github.io","full_name":"wasita/wasita.github.io","language":"Svelte","stars":1,"forks":0,"open_issues":8,"pushed_at":"2026-07-02T01:40:18Z","description":"personal website"},
    {"org_or_user":"wasita","repo_name":"magic-garden","full_name":"wasita/magic-garden","language":"Python","stars":2,"forks":1,"open_issues":1,"pushed_at":"2026-04-22T21:16:43Z","description":"Magic Garden Discord bot for auto-purchasing seeds"},
    {"org_or_user":"wasita","repo_name":"send2kobo","full_name":"wasita/send2kobo","language":"TypeScript","stars":1,"forks":0,"open_issues":0,"pushed_at":"2026-05-19T02:59:26Z","description":"Website for sending books to Kobo e-reader"},
    # kristinezheng
    {"org_or_user":"kristinezheng","repo_name":"kristinezheng.github.io","full_name":"kristinezheng/kristinezheng.github.io","language":"HTML","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-07-01T20:57:48Z","description":None},
    {"org_or_user":"kristinezheng","repo_name":"lookit-jenga","full_name":"kristinezheng/lookit-jenga","language":"Jupyter Notebook","stars":0,"forks":0,"open_issues":0,"pushed_at":"2024-05-16T18:29:05Z","description":"Lookit study for 9.85"},
    # AustinCStone (top repos)
    {"org_or_user":"AustinCStone","repo_name":"TextGAN","full_name":"AustinCStone/TextGAN","language":"Python","stars":92,"forks":30,"open_issues":5,"pushed_at":"2025-03-03T13:26:32Z","description":"Generative adversarial network for text generation"},
    {"org_or_user":"AustinCStone","repo_name":"StereoVisionMRF","full_name":"AustinCStone/StereoVisionMRF","language":"Python","stars":11,"forks":4,"open_issues":0,"pushed_at":"2026-04-01T07:39:41Z","description":"MRF with loopy belief propagation for stereo depth"},
    {"org_or_user":"AustinCStone","repo_name":"EpsteinSearch","full_name":"AustinCStone/EpsteinSearch","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-02-11T01:10:57Z","description":None},
    # M1shaaa
    {"org_or_user":"M1shaaa","repo_name":"lab-bookshelf-","full_name":"M1shaaa/lab-bookshelf-","language":"TypeScript","stars":0,"forks":0,"open_issues":0,"pushed_at":"2024-12-31T05:11:18Z","description":None},
    {"org_or_user":"M1shaaa","repo_name":"Python-Lookit-Uploads","full_name":"M1shaaa/Python-Lookit-Uploads","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2024-02-15T22:59:37Z","description":"random projects"},
    # DJedamski
    {"org_or_user":"DJedamski","repo_name":"kaggle_ncaa18","full_name":"DJedamski/kaggle_ncaa18","language":"Jupyter Notebook","stars":0,"forks":0,"open_issues":0,"pushed_at":"2018-02-26T16:33:24Z","description":"NCAA March Madness competition (2018)"},
    {"org_or_user":"DJedamski","repo_name":"Kaggle","full_name":"DJedamski/Kaggle","language":None,"stars":1,"forks":0,"open_issues":0,"pushed_at":"2023-04-21T01:42:35Z","description":None},
    {"org_or_user":"DJedamski","repo_name":"School","full_name":"DJedamski/School","language":"R","stars":1,"forks":1,"open_issues":0,"pushed_at":"2023-04-21T01:42:33Z","description":"Projects from grad school"},
]

# Insert repo snapshots and world increments
increment_id = 1
for i, r in enumerate(repos):
    trit, color, name = gf3(increment_id)
    h = snap_hash(r)
    con.execute("""
        INSERT INTO world_increments VALUES (?, now(), ?, ?, ?, 'repo', ?, 'push', ?, ?, ?)
    """, [increment_id, trit, color, name, r["org_or_user"], r["repo_name"], r["org_or_user"], h])
    con.execute("""
        INSERT INTO repo_snapshots VALUES (?, now(), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [i+1, increment_id, r["org_or_user"], r["repo_name"], r["full_name"],
          r.get("language"), r["stars"], r["forks"], r["open_issues"],
          r["pushed_at"], r.get("description")])
    increment_id += 1

print(f"Inserted {len(repos)} repo snapshots")

# Aptos wallet data (all read 0.0 from API - CoinStore resource not found = zero balance)
aptos_wallets = [
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

for world, addr, bal in aptos_wallets:
    con.execute("INSERT INTO aptos_snapshots VALUES (now(), ?, ?, ?)", [world, addr, bal])
print(f"Inserted {len(aptos_wallets)} Aptos wallet snapshots")

# Multisig probes (all returned sigs_required=2)
multisigs = [
    ("A-B", "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2),
    ("A-G", "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2),
    ("Y-Z", "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2),
    ("S-T", "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2),
    ("V-W", "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2),
]
for pair, addr, sigs in multisigs:
    con.execute("INSERT INTO multisig_probes VALUES (now(), ?, ?, ?, ?)", [pair, addr, sigs, True])
print(f"Inserted {len(multisigs)} multisig probes (all healthy, sigs=2)")

# MNX markets - unavailable (401 Unauthorized on testnet.mnx.fi)
print("MNX markets: unavailable (401 Unauthorized on testnet.mnx.fi/api/markets)")

# Verify
print("\n=== DB Summary ===")
print(f"world_increments: {con.execute('SELECT COUNT(*) FROM world_increments').fetchone()[0]} rows")
print(f"repo_snapshots:   {con.execute('SELECT COUNT(*) FROM repo_snapshots').fetchone()[0]} rows")
print(f"aptos_snapshots:  {con.execute('SELECT COUNT(*) FROM aptos_snapshots').fetchone()[0]} rows")
print(f"multisig_probes:  {con.execute('SELECT COUNT(*) FROM multisig_probes').fetchone()[0]} rows")
print(f"mnx_snapshots:    {con.execute('SELECT COUNT(*) FROM mnx_snapshots').fetchone()[0]} rows")

print("\n=== GF(3) Distribution ===")
for row in con.execute("SELECT gf3_trit, gf3_name, gf3_color, COUNT(*) as cnt FROM world_increments GROUP BY 1,2,3 ORDER BY 1").fetchall():
    print(f"  trit={row[0]} {row[1]} ({row[2]}): {row[3]} events")

print("\n=== Top Repos by Stars ===")
for row in con.execute("SELECT full_name, stars, language FROM repo_snapshots ORDER BY stars DESC LIMIT 10").fetchall():
    print(f"  {row[0]}: {row[1]}* ({row[2]})")

con.close()
print("\nDone.")
