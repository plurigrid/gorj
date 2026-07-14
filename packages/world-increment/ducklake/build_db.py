#!/usr/bin/env python3
"""Build world-increments DuckDB from sweep data."""
import duckdb
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "world-increments.duckdb")
con = duckdb.connect(DB_PATH)

# Create tables
con.execute("""
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
)
""")

con.execute("""
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
)
""")

con.execute("""
CREATE TABLE IF NOT EXISTS aptos_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  world VARCHAR,
  address VARCHAR,
  balance_apt DOUBLE
)
""")

con.execute("""
CREATE TABLE IF NOT EXISTS multisig_probes (
  timestamp TIMESTAMP DEFAULT now(),
  pair VARCHAR,
  address VARCHAR,
  sigs_required INTEGER,
  healthy BOOLEAN
)
""")

con.execute("""
CREATE TABLE IF NOT EXISTS mnx_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  ticker VARCHAR,
  name VARCHAR,
  category VARCHAR,
  price DOUBLE,
  change_pct DOUBLE
)
""")

# GF3 color chain
def gf3(id_):
    t = id_ % 3
    if t == 0:   return (0,  "#d3869b", "ERGODIC")
    elif t == 1: return (1,  "#b8bb26", "PLUS")
    else:        return (-1, "#cc241d", "MINUS")

# --- Repo data ---
# plurigrid repos (from file)
plurigrid_file = "/root/.claude/projects/-home-user-gorj/0f692518-1919-50b8-a208-057a2700a2a9/tool-results/mcp-github-search_repositories-1784009245288.txt"
plurigrid_repos = []
try:
    with open(plurigrid_file) as f:
        data = json.load(f)
    plurigrid_repos = data.get("items", [])
except Exception as e:
    print(f"Warning: {e}")

kubeflow_repos = [
  {"full_name":"kubeflow/trainer","language":"Go","stargazers_count":2139,"forks_count":985,"open_issues_count":141,"updated_at":"2026-07-14T04:08:24Z","description":"Distributed AI Model Training and LLM Fine-Tuning on Kubernetes"},
  {"full_name":"kubeflow/hub","language":"Go","stargazers_count":177,"forks_count":188,"open_issues_count":28,"updated_at":"2026-07-13T20:13:26Z","description":"Model Registry for ML lifecycle"},
  {"full_name":"kubeflow/pipelines","language":"Python","stargazers_count":4165,"forks_count":2032,"open_issues_count":422,"updated_at":"2026-07-14T01:35:20Z","description":"Machine Learning Pipelines for Kubeflow"},
  {"full_name":"kubeflow/kubeflow","language":None,"stargazers_count":15777,"forks_count":2685,"open_issues_count":0,"updated_at":"2026-07-14T00:51:22Z","description":"Machine Learning Toolkit for Kubernetes"},
  {"full_name":"kubeflow/sdk","language":"Python","stargazers_count":124,"forks_count":195,"open_issues_count":157,"updated_at":"2026-07-13T21:30:03Z","description":"Universal Python SDK for AI on Kubernetes"},
  {"full_name":"kubeflow/spark-operator","language":"Python","stargazers_count":3135,"forks_count":1500,"open_issues_count":108,"updated_at":"2026-07-13T17:22:54Z","description":"Kubernetes operator for Apache Spark"},
  {"full_name":"kubeflow/katib","language":"Python","stargazers_count":1690,"forks_count":533,"open_issues_count":106,"updated_at":"2026-07-11T16:05:34Z","description":"Automated Machine Learning on Kubernetes"},
  {"full_name":"kubeflow/mcp-server","language":"Python","stargazers_count":26,"forks_count":31,"open_issues_count":44,"updated_at":"2026-07-13T15:45:00Z","description":"MCP Server for Kubeflow Tools"},
  {"full_name":"kubeflow/mcp-apache-spark-history-server","language":"Python","stargazers_count":182,"forks_count":65,"open_issues_count":19,"updated_at":"2026-07-07T06:27:49Z","description":"MCP Server for Apache Spark History Server"},
  {"full_name":"kubeflow/community-distribution","language":"YAML","stargazers_count":1029,"forks_count":1071,"open_issues_count":24,"updated_at":"2026-07-13T15:42:00Z","description":"Kubeflow Community Distribution"},
]

teglon_repos = [
  {"full_name":"TeglonLabs/jank-crane","language":"C++","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-06-08T19:03:37Z","description":"crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps"},
  {"full_name":"TeglonLabs/mathpix-gem","language":"Ruby","stargazers_count":2,"forks_count":0,"open_issues_count":11,"updated_at":"2026-01-01T12:13:16Z","description":"Transform mathematical images to LaTeX"},
  {"full_name":"TeglonLabs/coin-flip-mcp","language":"JavaScript","stargazers_count":0,"forks_count":2,"open_issues_count":1,"updated_at":"2025-03-16T01:31:45Z","description":"MCP server for flipping coins"},
  {"full_name":"TeglonLabs/monad-mcp-server","language":None,"stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2025-05-14T17:53:01Z","description":"Monad MCP Server"},
  {"full_name":"TeglonLabs/topoi","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":1,"updated_at":"2025-01-24T06:47:38Z","description":None},
]

bmorphism_repos = [
  {"full_name":"bmorphism/Gay.jl","language":"Julia","stargazers_count":2,"forks_count":1,"open_issues_count":187,"updated_at":"2026-07-14T04:33:04Z","description":"Wide-gamut color sampling with splittable determinism"},
  {"full_name":"bmorphism/anti-bullshit-mcp-server","language":"JavaScript","stargazers_count":22,"forks_count":7,"open_issues_count":1,"updated_at":"2026-07-12T19:31:54Z","description":"MCP server for analyzing claims and detecting manipulation"},
  {"full_name":"bmorphism/ocaml-mcp-sdk","language":"OCaml","stargazers_count":61,"forks_count":2,"open_issues_count":0,"updated_at":"2026-05-08T16:50:34Z","description":"OCaml SDK for Model Context Protocol"},
  {"full_name":"bmorphism/shitcoin","language":"Python","stargazers_count":5,"forks_count":0,"open_issues_count":0,"updated_at":"2026-04-08T08:07:17Z","description":"IBC permissionless degeneracy tool"},
  {"full_name":"bmorphism/open-location-code-zig","language":"Zig","stargazers_count":3,"forks_count":0,"open_issues_count":0,"updated_at":"2026-03-24T21:54:01Z","description":"Open Location Code for Zig"},
  {"full_name":"bmorphism/nanoclj-zig","language":"Zig","stargazers_count":1,"forks_count":0,"open_issues_count":0,"updated_at":"2026-06-10T16:00:16Z","description":None},
  {"full_name":"bmorphism/satreadout","language":"HTML","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-06-20T13:05:44Z","description":"Machine-checked saturating non-Riemannian perceptual readout"},
]

zubyul_repos = [
  {"full_name":"zubyul/voice-observatory","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-04-24T05:56:20Z","description":"Passive macOS TUI observing voice-download pathways"},
  {"full_name":"zubyul/ghostel-emacs-worlds","language":"GLSL","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-04-24T00:21:00Z","description":"Ghostty config + alice/bob emacs-mods"},
  {"full_name":"zubyul/gay-world","language":"Python","stargazers_count":1,"forks_count":1,"open_issues_count":0,"updated_at":"2026-04-05T06:54:03Z","description":"Goblin world builder: each goblin is a world"},
  {"full_name":"zubyul/big-bad-plurigrid-quiz","language":"Emacs Lisp","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-04-09T18:51:35Z","description":"27 flashcards from plurigrid recent activity"},
  {"full_name":"zubyul/tilelang-kernels","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-03-16T02:31:16Z","description":"TileLang GPU kernels for GF(3) trit classification"},
]

social_graph_repos = [
  {"full_name":"wasita/wm-cv","language":"Svelte","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-07-14T03:53:19Z","description":"Academic CV as single page web app"},
  {"full_name":"wasita/wasita.github.io","language":"Svelte","stargazers_count":1,"forks_count":0,"open_issues_count":8,"updated_at":"2026-07-14T03:31:01Z","description":"personal website"},
  {"full_name":"migalkin/kgcourse2021","language":"HTML","stargazers_count":24,"forks_count":8,"open_issues_count":0,"updated_at":"2026-07-10T15:40:00Z","description":"Knowledge Graphs course materials"},
  {"full_name":"migalkin/NodePiece","language":"Python","stargazers_count":144,"forks_count":21,"open_issues_count":0,"updated_at":"2026-05-07T05:40:02Z","description":"Compositional Representations for Large Knowledge Graphs (ICLR'22)"},
  {"full_name":"migalkin/StarE","language":"Python","stargazers_count":89,"forks_count":16,"open_issues_count":1,"updated_at":"2026-04-16T14:12:45Z","description":"Message Passing for Hyper-Relational Knowledge Graphs (EMNLP'20)"},
  {"full_name":"migalkin/NBFNet_mlx","language":"Python","stargazers_count":10,"forks_count":1,"open_issues_count":1,"updated_at":"2026-03-11T01:31:21Z","description":"Neural Bellman-Ford networks in MLX"},
  {"full_name":"AustinCStone/EpsteinSearch","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-02-11T01:10:57Z","description":None},
]

# Collect all repos by source
all_sources = [
    ("org", "plurigrid",   plurigrid_repos),
    ("org", "kubeflow",    kubeflow_repos),
    ("org", "TeglonLabs", teglon_repos),
    ("user","bmorphism",   bmorphism_repos),
    ("user","zubyul",      zubyul_repos),
    ("social","social_graph", social_graph_repos),
]

# Clear existing data for this run (idempotent)
con.execute("DELETE FROM world_increments WHERE source_type IN ('org','user','social')")
con.execute("DELETE FROM repo_snapshots")
con.execute("DELETE FROM aptos_snapshots")
con.execute("DELETE FROM multisig_probes")
con.execute("DELETE FROM mnx_snapshots")

increment_id = 1
repo_id = 1

for source_type, source_name, repos in all_sources:
    for r in repos:
        trit, color, name = gf3(increment_id)
        full_name = r.get("full_name","")
        repo_short = full_name.split("/")[-1] if "/" in full_name else full_name
        org = full_name.split("/")[0] if "/" in full_name else source_name

        con.execute("""
          INSERT INTO world_increments VALUES (?,now(),?,?,?,?,?,?,?,?,?)
        """, [
            increment_id, trit, color, name,
            source_type, source_name, "repo_push",
            repo_short, org,
            str(hash(full_name + r.get("updated_at","")))[:16]
        ])

        con.execute("""
          INSERT INTO repo_snapshots VALUES (?,now(),?,?,?,?,?,?,?,?,?,?)
        """, [
            repo_id, increment_id,
            org, repo_short, full_name,
            r.get("language") or "",
            r.get("stargazers_count", 0),
            r.get("forks_count", 0),
            r.get("open_issues_count", 0),
            r.get("updated_at") or r.get("pushed_at",""),
            r.get("description") or ""
        ])

        increment_id += 1
        repo_id += 1

# Aptos wallets
aptos_data = [
  ("alice", "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b", 0.0),
  ("bob",   "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d", 0.0),
  ("A", "0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a", 0.0),
  ("B", "0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13", 0.0),
  ("C", "0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e", 0.0),
  ("D", "0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1", 0.0),
  ("E", "0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36", 0.0),
  ("F", "0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71", 0.0),
  ("G", "0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32", 0.0),
  ("H", "0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f", 0.0),
  ("I", "0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9", 0.0),
  ("J", "0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54", 0.0),
  ("K", "0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4", 0.0),
  ("L", "0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9", 0.0),
  ("M", "0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9", 0.0),
  ("N", "0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c", 0.0),
  ("O", "0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d", 0.0),
  ("P", "0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948", 0.0),
  ("Q", "0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9", 0.0),
  ("R", "0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10", 0.0),
  ("S", "0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386", 0.0),
  ("T", "0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588", 0.0),
  ("U", "0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956", 0.0),
  ("V", "0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3", 0.0),
  ("W", "0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0", 0.0),
  ("X", "0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d", 0.0),
  ("Y", "0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4", 0.0),
  ("Z", "0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c", 0.0),
]
for world, addr, bal in aptos_data:
    con.execute("INSERT INTO aptos_snapshots VALUES (now(),?,?,?)", [world, addr, bal])

# Multisig probes - all returned ["2"]
multisig_data = [
  ("A-B", "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2, True),
  ("A-G", "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2, True),
  ("Y-Z", "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2, True),
  ("S-T", "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2, True),
  ("V-W", "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2, True),
]
for pair, addr, sigs, healthy in multisig_data:
    con.execute("INSERT INTO multisig_probes VALUES (now(),?,?,?,?)", [pair, addr, sigs, healthy])

# MNX - unavailable (Vercel auth required)
# No rows inserted for mnx_snapshots

con.close()
print("DB built successfully.")

# Print summary stats
con2 = duckdb.connect(DB_PATH, read_only=True)
print(con2.execute("SELECT COUNT(*) as increments FROM world_increments").fetchone())
print(con2.execute("SELECT COUNT(*) as repos FROM repo_snapshots").fetchone())
print(con2.execute("SELECT COUNT(*) as wallets FROM aptos_snapshots").fetchone())
print(con2.execute("SELECT COUNT(*) as multisig FROM multisig_probes").fetchone())
print(con2.execute("SELECT source_name, COUNT(*) as cnt FROM repo_snapshots GROUP BY source_name ORDER BY cnt DESC").fetchall())
con2.close()
