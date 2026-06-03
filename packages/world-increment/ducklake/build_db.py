#!/usr/bin/env python3
"""Build world-increments.duckdb from GitHub search result files."""

import json
import re
import duckdb
import os

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
TOOL_RESULTS = "/root/.claude/projects/-home-user-gorj/67c4b85c-06d0-497d-b97a-ccdade4a7ade/tool-results"

# Remove existing DB so we start fresh
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

def clean_desc(desc):
    if not desc:
        return ""
    desc = str(desc).replace("\n", " ").replace("|", " ").strip()
    return desc[:200]

def parse_items_from_plain_json(path):
    """Parse a plain GitHub search JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("items", [])

def parse_items_from_nested_json(path):
    """Parse a nested MCP result JSON (array of {type, text} objects)."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    # data is a list of objects with "type" and "text" keys
    for item in data:
        if item.get("type") == "text":
            inner = json.loads(item["text"])
            return inner.get("items", [])
    return []

def extract_repos(items):
    """Extract repo fields from a list of GitHub repo items."""
    repos = []
    for item in items:
        owner = item.get("owner", {})
        org_or_user = owner.get("login", "")
        name = item.get("name", "")
        full_name = item.get("full_name", "")
        language = item.get("language") or ""
        stars = item.get("stargazers_count", 0) or 0
        forks = item.get("forks_count", 0) or 0
        open_issues = item.get("open_issues_count", 0) or 0
        pushed_at = item.get("pushed_at", "") or ""
        description = clean_desc(item.get("description", ""))
        repos.append((org_or_user, name, full_name, language, stars, forks, open_issues, pushed_at, description))
    return repos

# --- Parse all files ---
migalkin_repos = extract_repos(parse_items_from_plain_json(f"{TOOL_RESULTS}/mcp-github-search_repositories-1780470716294.txt"))
austin_repos = extract_repos(parse_items_from_plain_json(f"{TOOL_RESULTS}/mcp-github-search_repositories-1780470721668.txt"))
wasita_repos = extract_repos(parse_items_from_nested_json(f"{TOOL_RESULTS}/toolu_01BQVu2QWTMqTtPQ5H1YV383.json"))
plurigrid_repos = extract_repos(parse_items_from_plain_json(f"{TOOL_RESULTS}/mcp-github-search_repositories-1780470490208.txt"))
kubeflow_repos = extract_repos(parse_items_from_plain_json(f"{TOOL_RESULTS}/mcp-github-search_repositories-1780470487169.txt"))
bmorphism_repos = extract_repos(parse_items_from_plain_json(f"{TOOL_RESULTS}/mcp-github-search_repositories-1780470490616.txt"))
zubyul_repos = extract_repos(parse_items_from_plain_json(f"{TOOL_RESULTS}/mcp-github-search_repositories-1780470489071.txt"))

print(f"migalkin: {len(migalkin_repos)} repos")
print(f"AustinCStone: {len(austin_repos)} repos")
print(f"wasita: {len(wasita_repos)} repos")
print(f"plurigrid: {len(plurigrid_repos)} repos")
print(f"kubeflow: {len(kubeflow_repos)} repos")
print(f"bmorphism: {len(bmorphism_repos)} repos")
print(f"zubyul: {len(zubyul_repos)} repos")

# --- Hard-coded repos ---
teglon_repos = [
    ("TeglonLabs", "mathpix-gem", "TeglonLabs/mathpix-gem", "Ruby", 2, 0, 11, "2026-01-01T12:13:13Z", "Transform mathematical images to LaTeX chemistry structures to SMILES and documents to markdown with security-first design."),
    ("TeglonLabs", "coin-flip-mcp", "TeglonLabs/coin-flip-mcp", "JavaScript", 0, 2, 1, "2025-09-21T08:57:27Z", "MCP server for flipping coins with varying degrees of randomness from random.org"),
    ("TeglonLabs", "monad-mcp-server", "TeglonLabs/monad-mcp-server", "", 0, 0, 0, "2025-05-14T11:36:14Z", "Monad MCP Server"),
    ("TeglonLabs", "topoi", "TeglonLabs/topoi", "Python", 0, 0, 1, "2025-01-24T04:49:26Z", ""),
]

djedamski_repos = [
    ("DJedamski", "kaggle_ncaa18", "DJedamski/kaggle_ncaa18", "Jupyter Notebook", 0, 0, 0, "2018-03-07T12:36:09Z", "Code for NCAA March Madness competition (2018)"),
    ("DJedamski", "Project_Euler", "DJedamski/Project_Euler", "", 0, 0, 0, "2015-10-14T02:10:45Z", ""),
    ("DJedamski", "EDA", "DJedamski/EDA", "R", 0, 0, 0, "2014-11-09T16:51:34Z", "Coursera Project"),
    ("DJedamski", "Kaggle", "DJedamski/Kaggle", "", 1, 0, 0, "2014-11-03T02:22:01Z", ""),
    ("DJedamski", "Getting-and-Cleaning-Data", "DJedamski/Getting-and-Cleaning-Data", "R", 1, 0, 0, "2014-10-26T20:53:14Z", "Coursera Project"),
    ("DJedamski", "School", "DJedamski/School", "R", 1, 1, 0, "2014-10-09T02:55:13Z", "A couple small projects from grad school"),
]

kristinezheng_repos = [
    ("kristinezheng", "kristinezheng.github.io", "kristinezheng/kristinezheng.github.io", "HTML", 0, 0, 0, "2026-05-14T22:28:57Z", ""),
    ("kristinezheng", "Portfolio", "kristinezheng/Portfolio", "", 0, 0, 0, "2025-02-12T00:00:42Z", "July 2021"),
    ("kristinezheng", "lookit-jenga", "kristinezheng/lookit-jenga", "Jupyter Notebook", 0, 0, 0, "2024-05-16T18:29:01Z", "Lookit study for 9.85"),
    ("kristinezheng", "auditory-illusion", "kristinezheng/auditory-illusion", "CSS", 0, 0, 0, "2022-03-11T19:22:33Z", "9.35 spring 2022 auditory illusion"),
    ("kristinezheng", "graph_example", "kristinezheng/graph_example", "Python", 0, 0, 0, "2021-10-08T07:29:51Z", ""),
    ("kristinezheng", "Green-Machine", "kristinezheng/Green-Machine", "Python", 0, 0, 0, "2021-09-19T05:33:01Z", "HackMIT 2021: Sustainability Track"),
]

m1shaaa_repos = [
    ("M1shaaa", "M1shaaa", "M1shaaa/M1shaaa", "", 0, 0, 0, "2026-06-03T03:43:49Z", "Config files for my GitHub profile."),
    ("M1shaaa", "lab-bookshelf-", "M1shaaa/lab-bookshelf-", "TypeScript", 0, 0, 0, "2024-12-31T05:11:14Z", ""),
    ("M1shaaa", "rosie-s-study-3-lookit-project", "M1shaaa/rosie-s-study-3-lookit-project", "", 0, 0, 0, "2024-11-04T22:15:35Z", ""),
    ("M1shaaa", "Python-Lookit-Uploads", "M1shaaa/Python-Lookit-Uploads", "Python", 0, 0, 0, "2024-02-16T15:20:50Z", "random projects"),
    ("M1shaaa", "Classes", "M1shaaa/Classes", "", 0, 0, 0, "2023-12-07T08:16:20Z", ""),
    ("M1shaaa", "Yale-Work", "M1shaaa/Yale-Work", "HTML", 0, 0, 0, "2023-12-06T18:33:10Z", ""),
    ("M1shaaa", "MNIST-Classifier", "M1shaaa/MNIST-Classifier", "", 0, 0, 0, "2023-11-28T06:12:13Z", ""),
    ("M1shaaa", "Lookit-Demo", "M1shaaa/Lookit-Demo", "", 0, 0, 0, "2023-04-10T02:50:03Z", ""),
]

# --- All sources grouped ---
all_sources = {
    "plurigrid": plurigrid_repos,
    "kubeflow": kubeflow_repos,
    "TeglonLabs": teglon_repos,
    "bmorphism": bmorphism_repos,
    "zubyul": zubyul_repos,
    "migalkin": migalkin_repos,
    "DJedamski": djedamski_repos,
    "wasita": wasita_repos,
    "kristinezheng": kristinezheng_repos,
    "M1shaaa": m1shaaa_repos,
    "AustinCStone": austin_repos,
}

# --- GF(3) helper ---
def gf3_for_id(n):
    r = n % 3
    if r == 0:
        return (0, "#d3869b", "ERGODIC")
    elif r == 1:
        return (1, "#b8bb26", "PLUS")
    else:
        return (-1, "#cc241d", "MINUS")

# --- Connect DuckDB ---
con = duckdb.connect(DB_PATH)

# --- Create tables ---
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

con.execute("CREATE SEQUENCE IF NOT EXISTS increment_seq START 1")
con.execute("CREATE SEQUENCE IF NOT EXISTS repo_seq START 1")

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

# --- Insert world_increments (one per source) ---
increment_id = 1
source_to_increment = {}
for source_name, repos in all_sources.items():
    trit, color, gf3name = gf3_for_id(increment_id)
    con.execute("""
        INSERT INTO world_increments (id, gf3_trit, gf3_color, gf3_name, source_type, source_name, event_type, repo_name, actor, snapshot_hash)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (increment_id, trit, color, gf3name, "github", source_name, "repo_sweep", "", source_name, ""))
    source_to_increment[source_name] = increment_id
    increment_id += 1

print(f"Inserted {increment_id - 1} world_increment rows")

# --- Insert repo_snapshots ---
repo_id = 1
for source_name, repos in all_sources.items():
    inc_id = source_to_increment[source_name]
    for r in repos:
        org_or_user, repo_name, full_name, language, stars, forks, open_issues, pushed_at, description = r
        con.execute("""
            INSERT INTO repo_snapshots (id, timestamp, increment_id, org_or_user, repo_name, full_name, language, stars, forks, open_issues, pushed_at, description)
            VALUES (?, now(), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (repo_id, inc_id, org_or_user, repo_name, full_name, language, stars, forks, open_issues, pushed_at, description))
        repo_id += 1

print(f"Inserted {repo_id - 1} repo_snapshot rows")

# --- Insert Aptos snapshots ---
aptos_data = [
    ("alice", "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b"),
    ("bob",   "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d"),
    ("A",     "0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a"),
    ("B",     "0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13"),
    ("C",     "0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e"),
    ("D",     "0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1"),
    ("E",     "0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36"),
    ("F",     "0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71"),
    ("G",     "0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32"),
    ("H",     "0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f"),
    ("I",     "0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9"),
    ("J",     "0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54"),
    ("K",     "0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4"),
    ("L",     "0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9"),
    ("M",     "0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9"),
    ("N",     "0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c"),
    ("O",     "0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d"),
    ("P",     "0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948"),
    ("Q",     "0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9"),
    ("R",     "0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10"),
    ("S",     "0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386"),
    ("T",     "0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588"),
    ("U",     "0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956"),
    ("V",     "0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3"),
    ("W",     "0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0"),
    ("X",     "0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d"),
    ("Y",     "0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4"),
    ("Z",     "0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c"),
]

for world, address in aptos_data:
    con.execute("""
        INSERT INTO aptos_snapshots (timestamp, world, address, balance_apt)
        VALUES (now(), ?, ?, 0.0)
    """, (world, address))

print(f"Inserted {len(aptos_data)} aptos_snapshot rows")

# --- Insert multisig probes ---
multisig_data = [
    ("A-B", "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2, True),
    ("A-G", "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2, True),
    ("Y-Z", "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2, True),
    ("S-T", "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2, True),
    ("V-W", "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2, True),
]

for pair, address, sigs_required, healthy in multisig_data:
    con.execute("""
        INSERT INTO multisig_probes (timestamp, pair, address, sigs_required, healthy)
        VALUES (now(), ?, ?, ?, ?)
    """, (pair, address, sigs_required, healthy))

print(f"Inserted {len(multisig_data)} multisig_probe rows")

# --- Verify counts ---
print("\n--- Row counts ---")
result = con.execute("""
    SELECT 'world_increments' as tbl, COUNT(*) as n FROM world_increments
    UNION ALL SELECT 'repo_snapshots', COUNT(*) FROM repo_snapshots
    UNION ALL SELECT 'aptos_snapshots', COUNT(*) FROM aptos_snapshots
    UNION ALL SELECT 'multisig_probes', COUNT(*) FROM multisig_probes
    UNION ALL SELECT 'mnx_snapshots', COUNT(*) FROM mnx_snapshots
""").fetchall()
for row in result:
    print(f"  {row[0]}: {row[1]}")

# --- Gather stats for LATEST_SWEEP.md ---
print("\n--- Source stats ---")
source_stats = con.execute("""
    SELECT
        org_or_user,
        COUNT(*) as repo_count,
        MAX(language) as top_lang,
        MAX(stars) as max_stars,
        MAX(pushed_at) as last_pushed
    FROM repo_snapshots
    GROUP BY org_or_user
    ORDER BY org_or_user
""").fetchall()

for row in source_stats:
    print(row)

print("\n--- Language by stars per source ---")
lang_stats = con.execute("""
    SELECT org_or_user, language, SUM(stars) as total_stars
    FROM repo_snapshots
    WHERE language != ''
    GROUP BY org_or_user, language
    ORDER BY org_or_user, total_stars DESC
""").fetchall()
for row in lang_stats:
    print(row)

# --- Get increment info ---
print("\n--- world_increments ---")
increments = con.execute("""
    SELECT id, gf3_trit, gf3_color, gf3_name, source_name
    FROM world_increments
    ORDER BY id
""").fetchall()
for row in increments:
    print(row)

con.close()
print("\nDone.")
