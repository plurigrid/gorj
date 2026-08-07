#!/usr/bin/env python3
"""Build world-increments DuckDB from collected GitHub + Aptos data."""

import duckdb
import json
import hashlib
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "world-increments.duckdb")

con = duckdb.connect(DB_PATH)

# --- Schema ---
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

def gf3(id_):
    m = id_ % 3
    if m == 0: return 0, "#d3869b", "ERGODIC"
    if m == 1: return 1, "#b8bb26", "PLUS"
    return -1, "#cc241d", "MINUS"

def snap_hash(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True, default=str).encode()).hexdigest()[:16]

# --- Repo data ---
# Sources: (source_type, source_name, list_of_repos)
sources = []

# plurigrid repos from saved file
with open("/root/.claude/projects/-home-user-gorj/09e99d12-8c5e-5e35-b9b4-d517b12ce4a1/tool-results/mcp-github-search_repositories-1786105735257.txt") as f:
    data = json.load(f)
repos = data if isinstance(data, list) else data.get("items", [])
sources.append(("org", "plurigrid", repos))

# Inline data from other sources (collected during sweep)
kubeflow_repos = [
  {"full_name":"kubeflow/hub","language":"Go","stargazers_count":181,"forks_count":191,"open_issues_count":28,"updated_at":"2026-08-07T12:21:12Z","description":"Model Registry"},
  {"full_name":"kubeflow/sdk","language":"Python","stargazers_count":135,"forks_count":235,"open_issues_count":230,"updated_at":"2026-08-07T12:18:42Z","description":"Universal Python SDK for AI workloads on Kubernetes"},
  {"full_name":"kubeflow/trainer","language":"Go","stargazers_count":2173,"forks_count":1016,"open_issues_count":146,"updated_at":"2026-08-07T06:11:03Z","description":"Distributed AI Model Training and LLM Fine-Tuning"},
  {"full_name":"kubeflow/pipelines","language":"Python","stargazers_count":4181,"forks_count":2082,"open_issues_count":512,"updated_at":"2026-08-07T06:27:55Z","description":"Machine Learning Pipelines for Kubeflow"},
  {"full_name":"kubeflow/mcp-apache-spark-history-server","language":"Python","stargazers_count":188,"forks_count":67,"open_issues_count":19,"updated_at":"2026-08-07T06:53:59Z","description":"MCP Server for Apache Spark"},
  {"full_name":"kubeflow/spark-operator","language":"Python","stargazers_count":3145,"forks_count":1511,"open_issues_count":111,"updated_at":"2026-08-07T07:25:22Z","description":"K8s operator for Apache Spark"},
  {"full_name":"kubeflow/kubeflow","language":None,"stargazers_count":15805,"forks_count":2691,"open_issues_count":0,"updated_at":"2026-08-04T06:45:35Z","description":"Machine Learning Toolkit for Kubernetes"},
  {"full_name":"kubeflow/community-distribution","language":"YAML","stargazers_count":1030,"forks_count":1070,"open_issues_count":29,"updated_at":"2026-08-07T03:32:38Z","description":"Kubeflow Community Distribution"},
  {"full_name":"kubeflow/katib","language":"Python","stargazers_count":1694,"forks_count":534,"open_issues_count":105,"updated_at":"2026-08-01T18:43:37Z","description":"Automated Machine Learning on Kubernetes"},
  {"full_name":"kubeflow/notebooks","language":None,"stargazers_count":75,"forks_count":138,"open_issues_count":170,"updated_at":"2026-08-07T06:11:36Z","description":"Kubeflow Notebooks"},
]
sources.append(("org", "kubeflow", kubeflow_repos))

teglon_repos = [
  {"full_name":"TeglonLabs/jank-crane","language":"C++","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-06-08T19:03:37Z","description":"crane-jank converged-IR hub"},
  {"full_name":"TeglonLabs/mathpix-gem","language":"Ruby","stargazers_count":2,"forks_count":0,"open_issues_count":11,"updated_at":"2026-01-01T12:13:16Z","description":"Mathematical OCR in Ruby"},
  {"full_name":"TeglonLabs/coin-flip-mcp","language":"JavaScript","stargazers_count":0,"forks_count":2,"open_issues_count":1,"updated_at":"2025-03-16T01:31:45Z","description":"MCP server for flipping coins"},
  {"full_name":"TeglonLabs/monad-mcp-server","language":None,"stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2025-05-14T17:53:01Z","description":"Monad MCP Server"},
  {"full_name":"TeglonLabs/topoi","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":1,"updated_at":"2025-01-24T06:47:38Z","description":None},
]
sources.append(("org", "TeglonLabs", teglon_repos))

bmorphism_repos = [
  {"full_name":"bmorphism/Gay.jl","language":"Julia","stargazers_count":2,"forks_count":1,"open_issues_count":188,"updated_at":"2026-07-21T12:57:35Z","description":"Wide-gamut color sampling"},
  {"full_name":"bmorphism/anti-bullshit-mcp-server","language":"JavaScript","stargazers_count":23,"forks_count":7,"open_issues_count":1,"updated_at":"2026-08-02T12:54:58Z","description":"MCP server for analyzing claims"},
  {"full_name":"bmorphism/ocaml-mcp-sdk","language":"OCaml","stargazers_count":61,"forks_count":2,"open_issues_count":0,"updated_at":"2026-05-08T16:50:34Z","description":"OCaml SDK for MCP"},
  {"full_name":"bmorphism/gay-chat","language":"Scheme","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-07-14T21:00:00Z","description":"gay://chat over Spritely Brassica"},
  {"full_name":"bmorphism/satreadout","language":"HTML","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-06-20T13:05:44Z","description":"Machine-checked saturating perceptual readout"},
  {"full_name":"bmorphism/whale","language":"MATLAB","stargazers_count":2,"forks_count":0,"open_issues_count":0,"updated_at":"2026-04-20T15:04:09Z","description":"omniglot + sperm whale codas"},
  {"full_name":"bmorphism/shitcoin","language":"Python","stargazers_count":5,"forks_count":0,"open_issues_count":0,"updated_at":"2026-04-08T08:07:17Z","description":"IBC degen tools"},
  {"full_name":"bmorphism/open-location-code-zig","language":"Zig","stargazers_count":3,"forks_count":0,"open_issues_count":0,"updated_at":"2026-03-24T21:54:01Z","description":"Open Location Code for Zig"},
  {"full_name":"bmorphism/nanoclj-zig","language":"Zig","stargazers_count":1,"forks_count":0,"open_issues_count":0,"updated_at":"2026-06-10T16:00:16Z","description":"nanoclj-zig fork"},
  {"full_name":"bmorphism/world","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-06-02T06:49:06Z","description":"Local worlds launcher"},
]
sources.append(("user", "bmorphism", bmorphism_repos))

zubyul_repos = [
  {"full_name":"zubyul/voice-observatory","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-04-24T05:56:20Z","description":"Passive macOS TUI for voice-download pathways"},
  {"full_name":"zubyul/ghostel-emacs-worlds","language":"GLSL","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-04-24T00:21:00Z","description":"Ghostty config + ghostel family"},
  {"full_name":"zubyul/big-bad-plurigrid-quiz","language":"Emacs Lisp","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-04-09T18:51:35Z","description":"27 flashcards from activity"},
  {"full_name":"zubyul/Gay.jl","language":"Julia","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-03-28T11:30:07Z","description":"Gay.jl fork"},
  {"full_name":"zubyul/gay-world","language":"Python","stargazers_count":1,"forks_count":1,"open_issues_count":0,"updated_at":"2026-04-05T06:54:03Z","description":"Goblin world builder"},
  {"full_name":"zubyul/tilelang-kernels","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-03-16T02:31:16Z","description":"TileLang GPU kernels for GF(3)"},
  {"full_name":"zubyul/kinesis-kb360pro","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-03-26T10:29:44Z","description":"Kinesis Advantage360 Pro keyboard skill"},
]
sources.append(("user", "zubyul", zubyul_repos))

social_graph_repos = [
  # migalkin
  {"full_name":"migalkin/NodePiece","language":"Python","stargazers_count":144,"forks_count":21,"open_issues_count":0,"updated_at":"2026-05-07T05:40:02Z","description":"Compositional representations for large KGs"},
  {"full_name":"migalkin/StarE","language":"Python","stargazers_count":89,"forks_count":16,"open_issues_count":1,"updated_at":"2026-04-16T14:12:45Z","description":"Message Passing for Hyper-Relational KGs"},
  {"full_name":"migalkin/NBFNet_mlx","language":"Python","stargazers_count":10,"forks_count":1,"open_issues_count":1,"updated_at":"2026-03-11T01:31:21Z","description":"Neural Bellman-Ford networks in MLX"},
  {"full_name":"migalkin/kgcourse2021","language":"HTML","stargazers_count":24,"forks_count":8,"open_issues_count":0,"updated_at":"2026-07-10T15:40:00Z","description":"Knowledge Graphs course"},
  # wasita
  {"full_name":"wasita/xoxowasita-analysis","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-08-06T19:06:57Z","description":None},
  {"full_name":"wasita/joint-planning-lit","language":None,"stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-08-04T03:30:34Z","description":None},
  {"full_name":"wasita/wasita.github.io","language":"Svelte","stargazers_count":1,"forks_count":0,"open_issues_count":8,"updated_at":"2026-07-21T15:55:45Z","description":"personal website"},
  {"full_name":"wasita/magic-garden","language":"Python","stargazers_count":2,"forks_count":1,"open_issues_count":1,"updated_at":"2026-04-22T21:16:43Z","description":"Discord bot for magic garden"},
  # kristinezheng
  {"full_name":"kristinezheng/kristinezheng.github.io","language":"HTML","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-07-01T20:57:48Z","description":None},
  {"full_name":"kristinezheng/lookit-jenga","language":"Jupyter Notebook","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2024-05-16T18:29:05Z","description":"Lookit study"},
  # AustinCStone
  {"full_name":"AustinCStone/byteruckus","language":"HTML","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-07-15T05:19:33Z","description":None},
  {"full_name":"AustinCStone/TextGAN","language":"Python","stargazers_count":92,"forks_count":30,"open_issues_count":5,"updated_at":"2025-03-03T13:26:32Z","description":"GAN for text generation"},
  # M1shaaa
  {"full_name":"M1shaaa/M1shaaa","language":None,"stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-02-04T19:32:04Z","description":"GitHub profile config"},
  {"full_name":"M1shaaa/lab-bookshelf-","language":"TypeScript","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2024-12-31T05:11:18Z","description":None},
  # DJedamski
  {"full_name":"DJedamski/kaggle_ncaa18","language":"Jupyter Notebook","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2018-02-26T16:33:24Z","description":"NCAA March Madness 2018"},
  {"full_name":"DJedamski/Kaggle","language":None,"stargazers_count":1,"forks_count":0,"open_issues_count":0,"updated_at":"2023-04-21T01:42:35Z","description":None},
]
sources.append(("social_graph", "zubyul_graph", social_graph_repos))

# --- Insert repo snapshots ---
inc_id = 0
repo_id = 0

for source_type, source_name, repo_list in sources:
    for r in repo_list:
        inc_id += 1
        repo_id += 1
        trit, color, name = gf3(inc_id)
        full_name = r.get("full_name", "")
        repo_name_only = full_name.split("/")[-1] if "/" in full_name else full_name
        org_or_user = full_name.split("/")[0] if "/" in full_name else source_name
        h = snap_hash({"full_name": full_name, "stars": r.get("stargazers_count", 0), "pushed": r.get("updated_at","")})

        con.execute("""
            INSERT INTO world_increments VALUES (?, now(), ?, ?, ?, ?, ?, 'repo_snapshot', ?, ?, ?)
        """, [inc_id, trit, color, name, source_type, source_name, repo_name_only, org_or_user, h])

        con.execute("""
            INSERT INTO repo_snapshots VALUES (?, now(), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, [
            repo_id, inc_id, org_or_user,
            repo_name_only, full_name,
            r.get("language") or "unknown",
            r.get("stargazers_count", 0),
            r.get("forks_count", 0),
            r.get("open_issues_count", 0),
            r.get("updated_at") or r.get("pushed_at", ""),
            (r.get("description") or "")[:200]
        ])

print(f"Inserted {inc_id} world_increments and {repo_id} repo_snapshots")

# --- Aptos balances ---
aptos_addresses = [
    ("alice", "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b"),
    ("bob", "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d"),
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

for world, addr in aptos_addresses:
    # All returned resource_not_found -> 0.0 APT
    con.execute("INSERT INTO aptos_snapshots VALUES (now(), ?, ?, ?)", [world, addr, 0.0])

print(f"Inserted {len(aptos_addresses)} aptos_snapshots (all 0.0 APT - resource_not_found)")

# --- Multisig probes ---
multisigs = [
    ("A-B", "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2),
    ("A-G", "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2),
    ("Y-Z", "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2),
    ("S-T", "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2),
    ("V-W", "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2),
]

for pair, addr, sigs in multisigs:
    con.execute("INSERT INTO multisig_probes VALUES (now(), ?, ?, ?, ?)",
                [pair, addr, sigs, True])

print(f"Inserted {len(multisigs)} multisig_probes (all 2-of-n, healthy)")

# --- MNX (SPA, no public API) ---
# testnet.mnx.fi is a Next.js SPA; /api/markets returns 404; data not accessible via HTTP
print("MNX: testnet.mnx.fi is a Next.js SPA - no public REST API available")

con.close()
print(f"Database written to {DB_PATH}")
