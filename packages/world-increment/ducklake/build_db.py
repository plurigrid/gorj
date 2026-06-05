#!/usr/bin/env python3
"""Build world-increments DuckDB from sweep data."""
import json, hashlib, duckdb, os, sys

DB = os.path.join(os.path.dirname(__file__), "world-increments.duckdb")
RESULT_DIR = "/root/.claude/projects/-home-user-gorj/036efbd8-af43-4311-a1e0-c32a604e3b51/tool-results"

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

try:
    con.execute("CREATE SEQUENCE IF NOT EXISTS increment_seq START 1")
    con.execute("CREATE SEQUENCE IF NOT EXISTS repo_seq START 1")
except:
    pass

GF3 = {0: (0, "#d3869b", "ERGODIC"), 1: (1, "#b8bb26", "PLUS"), 2: (-1, "#cc241d", "MINUS")}

def gf3(n):
    k = n % 3
    return GF3[k]

def snap_hash(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()[:16]

# ---- Load repos from result files ----
def load_repos_from_file(filepath, source_label):
    rows = []
    try:
        raw = open(filepath).read()
        data = json.loads(raw)
        items = data.get("items", [])
        for r in items:
            rows.append({
                "source": source_label,
                "org_or_user": r.get("owner", {}).get("login", source_label),
                "repo_name": r.get("name", ""),
                "full_name": r.get("full_name", ""),
                "language": r.get("language") or "",
                "stars": r.get("stargazers_count", 0) or 0,
                "forks": r.get("forks_count", 0) or 0,
                "open_issues": r.get("open_issues_count", 0) or 0,
                "pushed_at": r.get("pushed_at") or r.get("updated_at") or "",
                "description": (r.get("description") or "")[:200],
            })
    except Exception as e:
        print(f"WARN: could not parse {filepath}: {e}", file=sys.stderr)
    return rows

# Inline social-graph repos already collected
social_graph_repos = [
    # TeglonLabs
    {"source":"org:TeglonLabs","org_or_user":"TeglonLabs","repo_name":"mathpix-gem","full_name":"TeglonLabs/mathpix-gem","language":"Ruby","stars":2,"forks":0,"open_issues":11,"pushed_at":"2026-01-01T12:13:13Z","description":"Transform mathematical images to LaTeX, chemistry structures to SMILES, and documents to markdown with security-first design."},
    {"source":"org:TeglonLabs","org_or_user":"TeglonLabs","repo_name":"coin-flip-mcp","full_name":"TeglonLabs/coin-flip-mcp","language":"JavaScript","stars":0,"forks":2,"open_issues":1,"pushed_at":"2025-09-21T08:57:27Z","description":"MCP server for flipping coins with varying degrees of randomness from random.org"},
    {"source":"org:TeglonLabs","org_or_user":"TeglonLabs","repo_name":"monad-mcp-server","full_name":"TeglonLabs/monad-mcp-server","language":"","stars":0,"forks":0,"open_issues":0,"pushed_at":"2025-05-14T11:36:14Z","description":"Monad MCP Server"},
    {"source":"org:TeglonLabs","org_or_user":"TeglonLabs","repo_name":"topoi","full_name":"TeglonLabs/topoi","language":"Python","stars":0,"forks":0,"open_issues":1,"pushed_at":"2025-01-24T04:49:26Z","description":""},
    # migalkin
    {"source":"user:migalkin","org_or_user":"migalkin","repo_name":"kgcourse2021","full_name":"migalkin/kgcourse2021","language":"HTML","stars":25,"forks":9,"open_issues":0,"pushed_at":"2026-02-16T05:16:08Z","description":"Knowledge Graphs course materials"},
    {"source":"user:migalkin","org_or_user":"migalkin","repo_name":"NBFNet_mlx","full_name":"migalkin/NBFNet_mlx","language":"Python","stars":10,"forks":1,"open_issues":1,"pushed_at":"2026-03-11T01:31:21Z","description":"Neural Bellman-Ford networks implemented in MLX for Apple Silicon"},
    {"source":"user:migalkin","org_or_user":"migalkin","repo_name":"StarE","full_name":"migalkin/StarE","language":"Python","stars":89,"forks":16,"open_issues":1,"pushed_at":"2026-04-16T14:12:45Z","description":"EMNLP 2020: Message Passing for Hyper-Relational Knowledge Graphs"},
    {"source":"user:migalkin","org_or_user":"migalkin","repo_name":"RWL","full_name":"migalkin/RWL","language":"Python","stars":8,"forks":1,"open_issues":0,"pushed_at":"2026-05-28T20:19:20Z","description":"Weisfeiler and Leman Go Relational (LOG 2022)"},
    {"source":"user:migalkin","org_or_user":"migalkin","repo_name":"NodePiece","full_name":"migalkin/NodePiece","language":"Python","stars":144,"forks":21,"open_issues":0,"pushed_at":"2026-05-07T05:40:02Z","description":"Compositional and Parameter-Efficient Representations for Large Knowledge Graphs (ICLR'22)"},
    {"source":"user:migalkin","org_or_user":"migalkin","repo_name":"rambo","full_name":"migalkin/rambo","language":"Rust","stars":3,"forks":0,"open_issues":1,"pushed_at":"2023-02-28T16:37:22Z","description":""},
    {"source":"user:migalkin","org_or_user":"migalkin","repo_name":"SMJoin-experiments","full_name":"migalkin/SMJoin-experiments","language":"R","stars":1,"forks":0,"open_issues":0,"pushed_at":"2020-03-04T15:56:23Z","description":"ISWC 2017 SMJoin results"},
    # wasita
    {"source":"user:wasita","org_or_user":"wasita","repo_name":"wasita.github.io","full_name":"wasita/wasita.github.io","language":"Svelte","stars":1,"forks":0,"open_issues":8,"pushed_at":"2026-06-01T04:15:14Z","description":"personal website"},
    {"source":"user:wasita","org_or_user":"wasita","repo_name":"wm-cv","full_name":"wasita/wm-cv","language":"Svelte","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-05-13T05:29:08Z","description":"Academic CV written as a single page web app (Svelte + Tailwind)"},
    {"source":"user:wasita","org_or_user":"wasita","repo_name":"vocoder","full_name":"wasita/vocoder","language":"JavaScript","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-05-06T05:14:03Z","description":""},
    {"source":"user:wasita","org_or_user":"wasita","repo_name":"magic-garden","full_name":"wasita/magic-garden","language":"Python","stars":2,"forks":1,"open_issues":1,"pushed_at":"2026-04-22T21:16:43Z","description":"Discord bot for magic garden auto-purchasing seeds"},
    {"source":"user:wasita","org_or_user":"wasita","repo_name":"send2kobo","full_name":"wasita/send2kobo","language":"TypeScript","stars":1,"forks":0,"open_issues":0,"pushed_at":"2026-05-19T02:59:26Z","description":"Website for sending books to your kobo e-reader"},
    # AustinCStone
    {"source":"user:AustinCStone","org_or_user":"AustinCStone","repo_name":"TextGAN","full_name":"AustinCStone/TextGAN","language":"Python","stars":92,"forks":30,"open_issues":5,"pushed_at":"2025-03-03T13:26:32Z","description":"A generative adversarial network for text generation, written in TensorFlow."},
    {"source":"user:AustinCStone","org_or_user":"AustinCStone","repo_name":"StereoVisionMRF","full_name":"AustinCStone/StereoVisionMRF","language":"Python","stars":11,"forks":4,"open_issues":0,"pushed_at":"2026-04-01T07:39:41Z","description":"Using a MRF with loopy belief propagation to infer depth from stereo images."},
    {"source":"user:AustinCStone","org_or_user":"AustinCStone","repo_name":"EpsteinSearch","full_name":"AustinCStone/EpsteinSearch","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-02-11T01:10:57Z","description":""},
    {"source":"user:AustinCStone","org_or_user":"AustinCStone","repo_name":"bmforkupdate","full_name":"AustinCStone/bmforkupdate","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2025-05-09T04:50:16Z","description":""},
    {"source":"user:AustinCStone","org_or_user":"AustinCStone","repo_name":"Z-order-curve","full_name":"AustinCStone/Z-order-curve","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2019-06-09T02:53:43Z","description":"Demo implementation of things related to space filling z-order curve"},
    {"source":"user:AustinCStone","org_or_user":"AustinCStone","repo_name":"StructureFromMotion","full_name":"AustinCStone/StructureFromMotion","language":"Python","stars":1,"forks":0,"open_issues":0,"pushed_at":"2019-04-26T19:43:12Z","description":"Recover 3D geometry from videos with unknown camera calibration"},
    # DJedamski
    {"source":"user:DJedamski","org_or_user":"DJedamski","repo_name":"kaggle_ncaa18","full_name":"DJedamski/kaggle_ncaa18","language":"Jupyter Notebook","stars":0,"forks":0,"open_issues":0,"pushed_at":"2018-02-26T16:33:24Z","description":"Code for NCAA March Madness competition (2018)"},
    {"source":"user:DJedamski","org_or_user":"DJedamski","repo_name":"Kaggle","full_name":"DJedamski/Kaggle","language":"","stars":1,"forks":0,"open_issues":0,"pushed_at":"2023-04-21T01:42:35Z","description":""},
    {"source":"user:DJedamski","org_or_user":"DJedamski","repo_name":"Getting-and-Cleaning-Data","full_name":"DJedamski/Getting-and-Cleaning-Data","language":"R","stars":1,"forks":0,"open_issues":0,"pushed_at":"2023-04-21T01:42:34Z","description":"Coursera Project"},
    {"source":"user:DJedamski","org_or_user":"DJedamski","repo_name":"School","full_name":"DJedamski/School","language":"R","stars":1,"forks":1,"open_issues":0,"pushed_at":"2023-04-21T01:42:33Z","description":"A couple small projects from grad school"},
    {"source":"user:DJedamski","org_or_user":"DJedamski","repo_name":"EDA","full_name":"DJedamski/EDA","language":"R","stars":0,"forks":0,"open_issues":0,"pushed_at":"2014-11-09T17:00:39Z","description":"Coursera Project"},
    # kristinezheng
    {"source":"user:kristinezheng","org_or_user":"kristinezheng","repo_name":"kristinezheng.github.io","full_name":"kristinezheng/kristinezheng.github.io","language":"HTML","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-05-14T22:29:01Z","description":""},
    {"source":"user:kristinezheng","org_or_user":"kristinezheng","repo_name":"lookit-jenga","full_name":"kristinezheng/lookit-jenga","language":"Jupyter Notebook","stars":0,"forks":0,"open_issues":0,"pushed_at":"2024-05-16T18:29:05Z","description":"Lookit study for 9.85"},
    {"source":"user:kristinezheng","org_or_user":"kristinezheng","repo_name":"Green-Machine","full_name":"kristinezheng/Green-Machine","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2021-09-19T05:33:04Z","description":"HackMIT 2021: Sustainability Track"},
    # M1shaaa
    {"source":"user:M1shaaa","org_or_user":"M1shaaa","repo_name":"M1shaaa","full_name":"M1shaaa/M1shaaa","language":"","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-02-04T19:32:04Z","description":"Config files for my GitHub profile."},
    {"source":"user:M1shaaa","org_or_user":"M1shaaa","repo_name":"lab-bookshelf-","full_name":"M1shaaa/lab-bookshelf-","language":"TypeScript","stars":0,"forks":0,"open_issues":0,"pushed_at":"2024-12-31T05:11:18Z","description":""},
    {"source":"user:M1shaaa","org_or_user":"M1shaaa","repo_name":"Python-Lookit-Uploads","full_name":"M1shaaa/Python-Lookit-Uploads","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2024-02-15T22:59:37Z","description":"random projects"},
]

# Load from files
file_sources = [
    (f"{RESULT_DIR}/mcp-github-search_repositories-1780653889927.txt", "org:plurigrid"),
    (f"{RESULT_DIR}/mcp-github-search_repositories-1780653888516.txt", "org:kubeflow"),
    (f"{RESULT_DIR}/mcp-github-search_repositories-1780653892726.txt", "user:bmorphism"),
    (f"{RESULT_DIR}/mcp-github-search_repositories-1780653890698.txt", "user:zubyul"),
]

all_repos = list(social_graph_repos)
for filepath, label in file_sources:
    loaded = load_repos_from_file(filepath, label)
    print(f"Loaded {len(loaded)} repos from {label}")
    all_repos.extend(loaded)

print(f"Total repos: {len(all_repos)}")

# Insert repos
increment_id = 1
repo_id = 1
for i, r in enumerate(all_repos):
    trit, color, name = gf3(increment_id)
    h = snap_hash(r)
    con.execute("""
        INSERT INTO world_increments (id, gf3_trit, gf3_color, gf3_name, source_type, source_name,
            event_type, repo_name, actor, snapshot_hash)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [increment_id, trit, color, name, "github_repo", r["source"],
          "push", r["repo_name"], r["org_or_user"], h])

    con.execute("""
        INSERT INTO repo_snapshots (id, increment_id, org_or_user, repo_name, full_name,
            language, stars, forks, open_issues, pushed_at, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [repo_id, increment_id, r["org_or_user"], r["repo_name"], r["full_name"],
          r["language"], r["stars"], r["forks"], r["open_issues"], r["pushed_at"], r["description"]])

    increment_id += 1
    repo_id += 1

# ---- Aptos snapshots ----
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
    con.execute("INSERT INTO aptos_snapshots (world, address, balance_apt) VALUES (?, ?, ?)",
                [world, addr, bal])

# ---- Multisig probes ----
multisig_data = [
    ("A-B", "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2),
    ("A-G", "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2),
    ("Y-Z", "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2),
    ("S-T", "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2),
    ("V-W", "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2),
]

for pair, addr, sigs in multisig_data:
    con.execute("INSERT INTO multisig_probes (pair, address, sigs_required, healthy) VALUES (?, ?, ?, ?)",
                [pair, addr, sigs, sigs > 0])

# ---- MNX - auth wall, record unavailable ----
con.execute("INSERT INTO mnx_snapshots (ticker, name, category, price, change_pct) VALUES (?, ?, ?, ?, ?)",
            ["UNAVAILABLE", "testnet.mnx.fi behind Vercel auth", "exchange", 0.0, 0.0])

# Print summary
print("\n=== DuckDB Summary ===")
print("world_increments:", con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0])
print("repo_snapshots:", con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0])
print("aptos_snapshots:", con.execute("SELECT COUNT(*) FROM aptos_snapshots").fetchone()[0])
print("multisig_probes:", con.execute("SELECT COUNT(*) FROM multisig_probes").fetchone()[0])
print("mnx_snapshots:", con.execute("SELECT COUNT(*) FROM mnx_snapshots").fetchone()[0])

# GF3 distribution
print("\n=== GF3 color chain distribution ===")
for row in con.execute("SELECT gf3_name, gf3_color, COUNT(*) FROM world_increments GROUP BY gf3_name, gf3_color ORDER BY gf3_name").fetchall():
    print(f"  {row[0]} {row[1]}: {row[2]}")

# Top starred repos
print("\n=== Top repos by stars ===")
for row in con.execute("SELECT org_or_user, repo_name, stars, language FROM repo_snapshots ORDER BY stars DESC LIMIT 10").fetchall():
    print(f"  {row[0]}/{row[1]} ★{row[2]} [{row[3]}]")

con.close()
print("\nDone. DB written to:", DB)
