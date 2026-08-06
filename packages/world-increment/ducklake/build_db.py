#!/usr/bin/env python3
"""Build world-increments DuckDB from collected sweep data."""
import json, hashlib, duckdb

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
con = duckdb.connect(DB)

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
CREATE SEQUENCE IF NOT EXISTS increment_seq START 1
""")
con.execute("""
CREATE SEQUENCE IF NOT EXISTS repo_seq START 1
""")
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

GF3 = {0: (0, "#d3869b", "ERGODIC"), 1: (1, "#b8bb26", "PLUS"), 2: (-1, "#cc241d", "MINUS")}

# Load repos from subagent-extracted JSON
with open("/home/user/gorj/packages/world-increment/ducklake/repo_data.json") as f:
    data = json.load(f)
repos = data["repos"]

# Social graph repos collected inline
social_repos = [
  # migalkin
  {"org_or_user":"migalkin","repo_name":"kgcourse2021","full_name":"migalkin/kgcourse2021","language":"HTML","stars":24,"forks":8,"open_issues":0,"pushed_at":"2026-07-10T15:40:00Z","description":"Материалы к курсу по Knowledge Graphs","source":"migalkin"},
  {"org_or_user":"migalkin","repo_name":"NBFNet_mlx","full_name":"migalkin/NBFNet_mlx","language":"Python","stars":10,"forks":1,"open_issues":1,"pushed_at":"2026-03-11T01:31:21Z","description":"Neural Bellman-Ford networks implemented in MLX for Apple Silicon","source":"migalkin"},
  {"org_or_user":"migalkin","repo_name":"StarE","full_name":"migalkin/StarE","language":"Python","stars":89,"forks":16,"open_issues":1,"pushed_at":"2026-04-16T14:12:45Z","description":"EMNLP 2020: Message Passing for Hyper-Relational Knowledge Graphs","source":"migalkin"},
  {"org_or_user":"migalkin","repo_name":"NodePiece","full_name":"migalkin/NodePiece","language":"Python","stars":144,"forks":21,"open_issues":0,"pushed_at":"2026-05-07T05:40:02Z","description":"Compositional and Parameter-Efficient Representations for Large Knowledge Graphs (ICLR'22)","source":"migalkin"},
  {"org_or_user":"migalkin","repo_name":"RWL","full_name":"migalkin/RWL","language":"Python","stars":8,"forks":1,"open_issues":0,"pushed_at":"2026-05-28T20:19:20Z","description":"Weisfeiler and Leman Go Relational (LOG 2022)","source":"migalkin"},
  # wasita
  {"org_or_user":"wasita","repo_name":"xoxowasita-analysis","full_name":"wasita/xoxowasita-analysis","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-08-06T19:06:57Z","description":None,"source":"wasita"},
  {"org_or_user":"wasita","repo_name":"wasita.github.io","full_name":"wasita/wasita.github.io","language":"Svelte","stars":1,"forks":0,"open_issues":8,"pushed_at":"2026-07-21T15:55:45Z","description":"personal website","source":"wasita"},
  {"org_or_user":"wasita","repo_name":"joint-planning-lit","full_name":"wasita/joint-planning-lit","language":None,"stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-08-04T03:30:34Z","description":None,"source":"wasita"},
  {"org_or_user":"wasita","repo_name":"magic-garden","full_name":"wasita/magic-garden","language":"Python","stars":2,"forks":1,"open_issues":1,"pushed_at":"2026-04-22T21:16:43Z","description":"a bot written for the magic garden discord activity game","source":"wasita"},
  # AustinCStone
  {"org_or_user":"AustinCStone","repo_name":"byteruckus","full_name":"AustinCStone/byteruckus","language":"HTML","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-07-15T05:19:33Z","description":None,"source":"AustinCStone"},
  {"org_or_user":"AustinCStone","repo_name":"TextGAN","full_name":"AustinCStone/TextGAN","language":"Python","stars":92,"forks":30,"open_issues":5,"pushed_at":"2025-03-03T13:26:32Z","description":"A generative adversarial network for text generation, written in TensorFlow.","source":"AustinCStone"},
  {"org_or_user":"AustinCStone","repo_name":"StereoVisionMRF","full_name":"AustinCStone/StereoVisionMRF","language":"Python","stars":11,"forks":4,"open_issues":0,"pushed_at":"2026-04-01T07:39:41Z","description":"Using a MRF with loopy belief propagation to infer depth from stereo images.","source":"AustinCStone"},
  # DJedamski
  {"org_or_user":"DJedamski","repo_name":"kaggle_ncaa18","full_name":"DJedamski/kaggle_ncaa18","language":"Jupyter Notebook","stars":0,"forks":0,"open_issues":0,"pushed_at":"2018-02-26T16:33:24Z","description":"Code for NCAA March Madness competition (2018)","source":"DJedamski"},
  {"org_or_user":"DJedamski","repo_name":"Kaggle","full_name":"DJedamski/Kaggle","language":None,"stars":1,"forks":0,"open_issues":0,"pushed_at":"2023-04-21T01:42:35Z","description":None,"source":"DJedamski"},
  # kristinezheng
  {"org_or_user":"kristinezheng","repo_name":"kristinezheng.github.io","full_name":"kristinezheng/kristinezheng.github.io","language":"HTML","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-07-01T20:57:48Z","description":None,"source":"kristinezheng"},
  {"org_or_user":"kristinezheng","repo_name":"lookit-jenga","full_name":"kristinezheng/lookit-jenga","language":"Jupyter Notebook","stars":0,"forks":0,"open_issues":0,"pushed_at":"2024-05-16T18:29:05Z","description":"Lookit study for 9.85","source":"kristinezheng"},
  # M1shaaa
  {"org_or_user":"M1shaaa","repo_name":"M1shaaa","full_name":"M1shaaa/M1shaaa","language":None,"stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-02-04T19:32:04Z","description":"Config files for my GitHub profile.","source":"M1shaaa"},
  {"org_or_user":"M1shaaa","repo_name":"lab-bookshelf-","full_name":"M1shaaa/lab-bookshelf-","language":"TypeScript","stars":0,"forks":0,"open_issues":0,"pushed_at":"2024-12-31T05:11:18Z","description":None,"source":"M1shaaa"},
  # TeglonLabs
  {"org_or_user":"TeglonLabs","repo_name":"jank-crane","full_name":"TeglonLabs/jank-crane","language":"C++","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-06-08T19:03:03Z","description":"crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow","source":"TeglonLabs"},
  {"org_or_user":"TeglonLabs","repo_name":"mathpix-gem","full_name":"TeglonLabs/mathpix-gem","language":"Ruby","stars":2,"forks":0,"open_issues":11,"pushed_at":"2026-01-01T12:13:13Z","description":"Transform mathematical images to LaTeX, chemistry structures to SMILES","source":"TeglonLabs"},
  {"org_or_user":"TeglonLabs","repo_name":"coin-flip-mcp","full_name":"TeglonLabs/coin-flip-mcp","language":"JavaScript","stars":0,"forks":2,"open_issues":1,"pushed_at":"2025-09-21T08:57:27Z","description":"MCP server for flipping coins with varying degrees of randomness from random.org","source":"TeglonLabs"},
  {"org_or_user":"TeglonLabs","repo_name":"topoi","full_name":"TeglonLabs/topoi","language":"Python","stars":0,"forks":0,"open_issues":1,"pushed_at":"2025-01-24T04:49:26Z","description":None,"source":"TeglonLabs"},
  {"org_or_user":"TeglonLabs","repo_name":"monad-mcp-server","full_name":"TeglonLabs/monad-mcp-server","language":None,"stars":0,"forks":0,"open_issues":0,"pushed_at":"2025-05-14T11:36:14Z","description":"Monad MCP Server","source":"TeglonLabs"},
]

all_repos = repos + social_repos

# Insert world_increments and repo_snapshots
inc_id = 1
snap_id = 1
for repo in all_repos:
    trit_key = inc_id % 3
    trit, color, name = GF3[trit_key]
    snap_hash = hashlib.sha256(repo["full_name"].encode()).hexdigest()[:16]
    con.execute("""
    INSERT INTO world_increments (id, gf3_trit, gf3_color, gf3_name, source_type, source_name, event_type, repo_name, actor, snapshot_hash)
    VALUES (?, ?, ?, ?, 'github', ?, 'repo_snapshot', ?, ?, ?)
    """, [inc_id, trit, color, name, repo.get("source",""), repo["repo_name"], repo.get("org_or_user",""), snap_hash])
    con.execute("""
    INSERT INTO repo_snapshots (id, increment_id, org_or_user, repo_name, full_name, language, stars, forks, open_issues, pushed_at, description)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [snap_id, inc_id, repo.get("org_or_user",""), repo["repo_name"], repo["full_name"],
          repo.get("language"), repo.get("stars",0), repo.get("forks",0), repo.get("open_issues",0),
          repo.get("pushed_at",""), repo.get("description")])
    inc_id += 1
    snap_id += 1

# Aptos wallets - all returned resource_not_found (unfunded accounts on mainnet)
WALLETS = [
  ("alice","0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b"),
  ("bob","0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d"),
  ("A","0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a"),
  ("B","0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13"),
  ("C","0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e"),
  ("D","0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1"),
  ("E","0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36"),
  ("F","0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71"),
  ("G","0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32"),
  ("H","0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f"),
  ("I","0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9"),
  ("J","0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54"),
  ("K","0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4"),
  ("L","0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9"),
  ("M","0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9"),
  ("N","0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c"),
  ("O","0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d"),
  ("P","0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948"),
  ("Q","0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9"),
  ("R","0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10"),
  ("S","0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386"),
  ("T","0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588"),
  ("U","0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956"),
  ("V","0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3"),
  ("W","0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0"),
  ("X","0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d"),
  ("Y","0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4"),
  ("Z","0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c"),
]
for world, addr in WALLETS:
    con.execute("INSERT INTO aptos_snapshots (world, address, balance_apt) VALUES (?, ?, ?)",
                [world, addr, 0.0])

# Multisig probes - all returned ["2"] (2 sigs required)
MULTISIGS = [
  ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2),
  ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2),
  ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2),
  ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2),
  ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2),
]
for pair, addr, sigs in MULTISIGS:
    con.execute("INSERT INTO multisig_probes (pair, address, sigs_required, healthy) VALUES (?, ?, ?, ?)",
                [pair, addr, sigs, True])

con.close()

# Print summary
con2 = duckdb.connect(DB, read_only=True)
wi = con2.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0]
rs = con2.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0]
at = con2.execute("SELECT COUNT(*) FROM aptos_snapshots").fetchone()[0]
mp = con2.execute("SELECT COUNT(*) FROM multisig_probes").fetchone()[0]
top = con2.execute("SELECT org_or_user, COUNT(*) as n FROM repo_snapshots GROUP BY org_or_user ORDER BY n DESC LIMIT 10").fetchall()
con2.close()

print(f"world_increments: {wi}")
print(f"repo_snapshots: {rs}")
print(f"aptos_snapshots: {at}")
print(f"multisig_probes: {mp}")
print("Top sources:", top)
