#!/usr/bin/env python3
"""Build world-increments DuckDB from GitHub sweep + Aptos snapshot data."""
import json, hashlib, duckdb
from pathlib import Path

DB = Path(__file__).parent / "world-increments.duckdb"
RESULTS_DIR = Path("/root/.claude/projects/-home-user-gorj/7096bb66-56ed-4c56-933a-8dd4b85d5192/tool-results")

con = duckdb.connect(str(DB))

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

GF3 = [
    (0, "#d3869b", "ERGODIC"),
    (1, "#b8bb26", "PLUS"),
    (2, "#cc241d", "MINUS"),
]

def gf3_for(n):
    t = n % 3
    _, color, name = GF3[t]
    return t if t != 2 else -1, color, name

def parse_repos(path, is_wrapper=False):
    raw = open(path).read()
    if is_wrapper:
        data = json.loads(raw)
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict) and 'text' in item:
                    return json.loads(item['text']).get('items', [])
    return json.loads(raw).get('items', [])

sources = [
    ("org", "plurigrid",     RESULTS_DIR / "mcp-github-search_repositories-1778756884976.txt", False),
    ("org", "kubeflow",      RESULTS_DIR / "mcp-github-search_repositories-1778756882444.txt", False),
    ("org", "TeglonLabs",    None, False),
    ("user", "bmorphism",    RESULTS_DIR / "mcp-github-search_repositories-1778756921131.txt", False),
    ("user", "zubyul",       RESULTS_DIR / "mcp-github-search_repositories-1778756920236.txt", False),
    ("user", "migalkin",     RESULTS_DIR / "mcp-github-search_repositories-1778756919428.txt", False),
    ("user", "DJedamski",    None, False),
    ("user", "wasita",       RESULTS_DIR / "toolu_01C4YnGfwMjqFp8W4df6w1mX.json", True),
    ("user", "kristinezheng", None, False),
    ("user", "M1shaaa",      None, False),
    ("user", "AustinCStone", RESULTS_DIR / "mcp-github-search_repositories-1778756923922.txt", False),
]

teglon_inline = [
    {"full_name": "TeglonLabs/mathpix-gem", "name": "mathpix-gem", "language": "Ruby", "stargazers_count": 2, "forks_count": 0, "open_issues_count": 11, "pushed_at": "2026-01-01T12:13:13Z", "description": "Transform mathematical images to LaTeX, chemistry structures to SMILES"},
    {"full_name": "TeglonLabs/monad-mcp-server", "name": "monad-mcp-server", "language": None, "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2025-05-14T11:36:14Z", "description": "Monad MCP Server"},
    {"full_name": "TeglonLabs/topoi", "name": "topoi", "language": "Python", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 1, "pushed_at": "2025-01-24T04:49:26Z", "description": None},
    {"full_name": "TeglonLabs/coin-flip-mcp", "name": "coin-flip-mcp", "language": "JavaScript", "stargazers_count": 0, "forks_count": 2, "open_issues_count": 1, "pushed_at": "2025-09-21T08:57:27Z", "description": "MCP server for flipping coins"},
]

djedamski_inline = [
    {"full_name": "DJedamski/kaggle_ncaa18", "name": "kaggle_ncaa18", "language": "Jupyter Notebook", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2018-03-07T12:36:09Z", "description": "Code for NCAA March Madness competition (2018)"},
    {"full_name": "DJedamski/Project_Euler", "name": "Project_Euler", "language": None, "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2015-10-14T02:10:45Z", "description": None},
    {"full_name": "DJedamski/EDA", "name": "EDA", "language": "R", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2014-11-09T16:51:34Z", "description": "Coursera Project"},
    {"full_name": "DJedamski/Kaggle", "name": "Kaggle", "language": None, "stargazers_count": 1, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2014-11-03T02:22:01Z", "description": None},
    {"full_name": "DJedamski/Getting-and-Cleaning-Data", "name": "Getting-and-Cleaning-Data", "language": "R", "stargazers_count": 1, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2014-10-26T20:53:14Z", "description": "Coursera Project"},
    {"full_name": "DJedamski/School", "name": "School", "language": "R", "stargazers_count": 1, "forks_count": 1, "open_issues_count": 0, "pushed_at": "2014-10-09T02:55:13Z", "description": "A couple small projects from grad school"},
]

kristinezheng_inline = [
    {"full_name": "kristinezheng/kristinezheng.github.io", "name": "kristinezheng.github.io", "language": "HTML", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2026-04-09T17:09:42Z", "description": None},
    {"full_name": "kristinezheng/Portfolio", "name": "Portfolio", "language": None, "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2025-02-12T00:00:42Z", "description": "July 2021"},
    {"full_name": "kristinezheng/lookit-jenga", "name": "lookit-jenga", "language": "Jupyter Notebook", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2024-05-16T18:29:01Z", "description": "Lookit study for 9.85"},
    {"full_name": "kristinezheng/auditory-illusion", "name": "auditory-illusion", "language": "CSS", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2022-03-11T19:22:33Z", "description": "9.35 spring 2022 auditory illusion"},
    {"full_name": "kristinezheng/graph_example", "name": "graph_example", "language": "Python", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2021-10-08T07:29:51Z", "description": None},
    {"full_name": "kristinezheng/Green-Machine", "name": "Green-Machine", "language": "Python", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2021-09-19T05:33:01Z", "description": "HackMIT 2021: Sustainability Track"},
]

m1shaaa_inline = [
    {"full_name": "M1shaaa/M1shaaa", "name": "M1shaaa", "language": None, "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2026-05-14T02:49:12Z", "description": "Config files for GitHub profile"},
    {"full_name": "M1shaaa/lab-bookshelf-", "name": "lab-bookshelf-", "language": "TypeScript", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2024-12-31T05:11:14Z", "description": None},
    {"full_name": "M1shaaa/rosie-s-study-3-lookit-project", "name": "rosie-s-study-3-lookit-project", "language": None, "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2024-11-04T22:15:35Z", "description": None},
    {"full_name": "M1shaaa/Python-Lookit-Uploads", "name": "Python-Lookit-Uploads", "language": "Python", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2024-02-16T15:20:50Z", "description": "random projects"},
    {"full_name": "M1shaaa/Classes", "name": "Classes", "language": None, "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2023-12-07T08:16:20Z", "description": None},
    {"full_name": "M1shaaa/Yale-Work", "name": "Yale-Work", "language": "HTML", "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2023-12-06T18:33:10Z", "description": None},
    {"full_name": "M1shaaa/MNIST-Classifier", "name": "MNIST-Classifier", "language": None, "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2023-11-28T06:12:13Z", "description": None},
    {"full_name": "M1shaaa/Lookit-Demo", "name": "Lookit-Demo", "language": None, "stargazers_count": 0, "forks_count": 0, "open_issues_count": 0, "pushed_at": "2023-04-10T02:50:03Z", "description": None},
]

inline_repos = {
    "TeglonLabs": teglon_inline,
    "DJedamski": djedamski_inline,
    "kristinezheng": kristinezheng_inline,
    "M1shaaa": m1shaaa_inline,
}

increment_id = 1
repo_id = 1

for src_type, src_name, path, is_wrapper in sources:
    if path is not None:
        repos = parse_repos(path, is_wrapper)
    else:
        repos = inline_repos.get(src_name, [])

    for repo in repos:
        trit, color, name = gf3_for(increment_id)
        full_name = repo.get("full_name", "")
        snap_hash = hashlib.md5(f"{full_name}{repo.get('pushed_at','')}".encode()).hexdigest()[:8]

        con.execute("""
        INSERT INTO world_increments VALUES (?, now(), ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, [increment_id, trit, color, name, src_type, src_name, "repo_snapshot",
              repo.get("name", ""), repo.get("owner", {}).get("login", src_name) if isinstance(repo.get("owner"), dict) else src_name,
              snap_hash])

        con.execute("""
        INSERT INTO repo_snapshots VALUES (?, now(), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, [repo_id, increment_id, src_name, repo.get("name", ""), full_name,
              repo.get("language") or "", repo.get("stargazers_count", 0),
              repo.get("forks_count", 0), repo.get("open_issues_count", 0),
              repo.get("pushed_at", "")[:10], (repo.get("description") or "")[:200]])

        increment_id += 1
        repo_id += 1

# Aptos snapshots - all null (no CoinStore resource)
aptos_data = [
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
for world, addr, bal in aptos_data:
    con.execute("INSERT INTO aptos_snapshots VALUES (now(), ?, ?, ?)", [world, addr, bal])

# Multisig probes - all healthy, 2 sigs required
multisig_data = [
    ("A-B", "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2, True),
    ("A-G", "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2, True),
    ("Y-Z", "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2, True),
    ("S-T", "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2, True),
    ("V-W", "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2, True),
]
for pair, addr, sigs, healthy in multisig_data:
    con.execute("INSERT INTO multisig_probes VALUES (now(), ?, ?, ?, ?)", [pair, addr, sigs, healthy])

# MNX - SPA unavailable
# No rows inserted

# Summary query
total_increments = con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0]
total_repos = con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0]
top_langs = con.execute("""
  SELECT language, COUNT(*) as cnt FROM repo_snapshots
  WHERE language != '' GROUP BY language ORDER BY cnt DESC LIMIT 10
""").fetchall()
gf3_dist = con.execute("""
  SELECT gf3_name, gf3_color, COUNT(*) FROM world_increments GROUP BY gf3_name, gf3_color ORDER BY gf3_name
""").fetchall()

print(f"total_increments={total_increments} total_repos={total_repos}")
for lang, cnt in top_langs:
    print(f"  lang: {lang} = {cnt}")
for name, color, cnt in gf3_dist:
    print(f"  gf3: {name} {color} = {cnt}")

con.close()
print("DB built OK:", DB)
