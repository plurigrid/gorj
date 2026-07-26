#!/usr/bin/env python3
"""Build world-increments.duckdb from collected GitHub and Aptos data."""
import json, subprocess, sys, os

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"

def gf3(id_):
    m = id_ % 3
    if m == 0: return (0, "#d3869b", "ERGODIC")
    if m == 1: return (1, "#b8bb26", "PLUS")
    return (-1, "#cc241d", "MINUS")

def sq(s):
    return s.replace("'", "''")

sql_parts = []

# DDL
sql_parts.append("""
CREATE TABLE IF NOT EXISTS world_increments (
  id INTEGER, timestamp TIMESTAMP DEFAULT now(), gf3_trit INTEGER,
  gf3_color VARCHAR, gf3_name VARCHAR, source_type VARCHAR,
  source_name VARCHAR, event_type VARCHAR, repo_name VARCHAR,
  actor VARCHAR, snapshot_hash VARCHAR
);
CREATE TABLE IF NOT EXISTS repo_snapshots (
  id INTEGER, timestamp TIMESTAMP DEFAULT now(), increment_id INTEGER,
  org_or_user VARCHAR, repo_name VARCHAR, full_name VARCHAR,
  language VARCHAR, stars INTEGER, forks INTEGER, open_issues INTEGER,
  pushed_at VARCHAR, description VARCHAR
);
CREATE SEQUENCE IF NOT EXISTS increment_seq START 1;
CREATE SEQUENCE IF NOT EXISTS repo_seq START 1;
CREATE TABLE IF NOT EXISTS aptos_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  world VARCHAR, address VARCHAR, balance_apt DOUBLE
);
CREATE TABLE IF NOT EXISTS multisig_probes (
  timestamp TIMESTAMP DEFAULT now(),
  pair VARCHAR, address VARCHAR, sigs_required INTEGER, healthy BOOLEAN
);
CREATE TABLE IF NOT EXISTS mnx_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  ticker VARCHAR, name VARCHAR, category VARCHAR,
  price DOUBLE, change_pct DOUBLE
);
""")

# Repo data from all sources
repo_sources = {
    "plurigrid": {
        "type": "org",
        "repos": json.loads(open('/root/.claude/projects/-home-user-gorj/df4a8971-a4d7-59ee-8916-5557f31d40a8/tool-results/mcp-github-search_repositories-1785096437351.txt').read()).get('items',[])
    },
    "kubeflow": {
        "type": "org",
        "repos": json.loads(open('/root/.claude/projects/-home-user-gorj/df4a8971-a4d7-59ee-8916-5557f31d40a8/tool-results/mcp-github-search_repositories-1785096436525.txt').read()).get('items',[])
    },
    "bmorphism": {
        "type": "user",
        "repos": json.loads(open('/root/.claude/projects/-home-user-gorj/df4a8971-a4d7-59ee-8916-5557f31d40a8/tool-results/mcp-github-search_repositories-1785096440713.txt').read()).get('items',[])
    },
    "zubyul": {
        "type": "user",
        "repos": json.loads(open('/root/.claude/projects/-home-user-gorj/df4a8971-a4d7-59ee-8916-5557f31d40a8/tool-results/mcp-github-search_repositories-1785096438759.txt').read()).get('items',[])
    },
    "migalkin": {
        "type": "user_social",
        "repos": json.loads(open('/root/.claude/projects/-home-user-gorj/df4a8971-a4d7-59ee-8916-5557f31d40a8/tool-results/mcp-github-search_repositories-1785096472020.txt').read()).get('items',[])
    },
    "AustinCStone": {
        "type": "user_social",
        "repos": json.loads(open('/root/.claude/projects/-home-user-gorj/df4a8971-a4d7-59ee-8916-5557f31d40a8/tool-results/mcp-github-search_repositories-1785096475777.txt').read()).get('items',[])
    },
}

# Inline small repos
teglon_repos = [
    {"name":"jank-crane","full_name":"TeglonLabs/jank-crane","language":"C++","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-06-08T19:03:03Z","description":"crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow"},
    {"name":"mathpix-gem","full_name":"TeglonLabs/mathpix-gem","language":"Ruby","stargazers_count":2,"forks_count":0,"open_issues_count":11,"pushed_at":"2026-01-01T12:13:13Z","description":"Transform mathematical images to LaTeX"},
    {"name":"coin-flip-mcp","full_name":"TeglonLabs/coin-flip-mcp","language":"JavaScript","stargazers_count":0,"forks_count":2,"open_issues_count":1,"pushed_at":"2025-09-21T08:57:27Z","description":"MCP server for flipping coins with varying degrees of randomness"},
    {"name":"monad-mcp-server","full_name":"TeglonLabs/monad-mcp-server","language":"","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-05-14T11:36:14Z","description":"Monad MCP Server"},
    {"name":"topoi","full_name":"TeglonLabs/topoi","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":1,"pushed_at":"2025-01-24T04:49:26Z","description":""},
]
repo_sources["TeglonLabs"] = {"type": "org", "repos": teglon_repos}

djedamski_repos = [
    {"name":"kaggle_ncaa18","full_name":"DJedamski/kaggle_ncaa18","language":"Jupyter Notebook","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2018-03-07T12:36:09Z","description":"Code for NCAA March Madness competition (2018)"},
    {"name":"Project_Euler","full_name":"DJedamski/Project_Euler","language":"","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2015-10-14T02:10:45Z","description":""},
    {"name":"EDA","full_name":"DJedamski/EDA","language":"R","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2014-11-09T16:51:34Z","description":"Coursera Project"},
    {"name":"Kaggle","full_name":"DJedamski/Kaggle","language":"","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2014-11-03T02:22:01Z","description":""},
    {"name":"Getting-and-Cleaning-Data","full_name":"DJedamski/Getting-and-Cleaning-Data","language":"R","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2014-10-26T20:53:14Z","description":"Coursera Project"},
    {"name":"School","full_name":"DJedamski/School","language":"R","stargazers_count":1,"forks_count":1,"open_issues_count":0,"pushed_at":"2014-10-09T02:55:13Z","description":"A couple small projects from grad school"},
]
repo_sources["DJedamski"] = {"type": "user_social", "repos": djedamski_repos}

wasita_repos = [
    {"name":"wasita.github.io","full_name":"wasita/wasita.github.io","language":"Svelte","stargazers_count":1,"forks_count":0,"open_issues_count":8,"pushed_at":"2026-07-21T15:52:20Z","description":"personal website"},
    {"name":"pnas-typst-template","full_name":"wasita/pnas-typst-template","language":"","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-07-16T00:00:00Z","description":""},
    {"name":"wm-cv","full_name":"wasita/wm-cv","language":"Svelte","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-07-14T00:00:00Z","description":""},
    {"name":"proj-template","full_name":"wasita/proj-template","language":"","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-06-19T00:00:00Z","description":""},
    {"name":"vocoder","full_name":"wasita/vocoder","language":"JavaScript","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-05-06T00:00:00Z","description":""},
    {"name":"magic-garden","full_name":"wasita/magic-garden","language":"Python","stargazers_count":2,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-01-13T00:00:00Z","description":""},
]
repo_sources["wasita"] = {"type": "user_social", "repos": wasita_repos}

kristinezheng_repos = [
    {"name":"kristinezheng.github.io","full_name":"kristinezheng/kristinezheng.github.io","language":"HTML","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-07-01T20:57:44Z","description":""},
    {"name":"lookit-jenga","full_name":"kristinezheng/lookit-jenga","language":"Jupyter Notebook","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2024-05-16T18:29:01Z","description":"Lookit study for 9.85"},
    {"name":"auditory-illusion","full_name":"kristinezheng/auditory-illusion","language":"CSS","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2022-03-11T19:22:33Z","description":"9.35 spring 2022 auditory illusion"},
    {"name":"graph_example","full_name":"kristinezheng/graph_example","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2021-10-08T07:29:51Z","description":""},
    {"name":"Green-Machine","full_name":"kristinezheng/Green-Machine","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2021-09-19T05:33:01Z","description":"HackMIT 2021: Sustainability Track"},
]
repo_sources["kristinezheng"] = {"type": "user_social", "repos": kristinezheng_repos}

m1shaaa_repos = [
    {"name":"M1shaaa","full_name":"M1shaaa/M1shaaa","language":"","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-07-26T13:12:12Z","description":"Config files for my GitHub profile"},
    {"name":"lab-bookshelf-","full_name":"M1shaaa/lab-bookshelf-","language":"TypeScript","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2024-12-31T05:11:14Z","description":""},
    {"name":"rosie-s-study-3-lookit-project","full_name":"M1shaaa/rosie-s-study-3-lookit-project","language":"","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2024-11-04T22:15:35Z","description":""},
    {"name":"Python-Lookit-Uploads","full_name":"M1shaaa/Python-Lookit-Uploads","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2024-02-16T15:20:50Z","description":"random projects"},
    {"name":"Classes","full_name":"M1shaaa/Classes","language":"HTML","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2023-12-07T08:16:20Z","description":""},
    {"name":"Yale-Work","full_name":"M1shaaa/Yale-Work","language":"HTML","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2023-12-06T18:33:10Z","description":""},
    {"name":"MNIST-Classifier","full_name":"M1shaaa/MNIST-Classifier","language":"","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2023-11-28T06:12:13Z","description":""},
    {"name":"Lookit-Demo","full_name":"M1shaaa/Lookit-Demo","language":"","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2023-04-10T02:50:03Z","description":""},
]
repo_sources["M1shaaa"] = {"type": "user_social", "repos": m1shaaa_repos}

# Build INSERT statements
inc_id = 1
repo_id = 1

for source_name, source_data in repo_sources.items():
    source_type = source_data["type"]
    repos = source_data["repos"][:30]  # cap at 30 per source

    trit, color, name = gf3(inc_id)
    sql_parts.append(f"""
INSERT INTO world_increments VALUES (
  {inc_id}, now(), {trit}, '{color}', '{name}',
  '{source_type}', '{source_name}', 'repo_snapshot',
  '{sq(source_name)}', NULL, NULL
);""")

    for r in repos:
        desc = sq((r.get('description') or '')[:200])
        lang = sq(r.get('language') or '')
        repo_name = sq(r.get('name',''))
        full_name = sq(r.get('full_name',''))
        pushed = r.get('pushed_at','')
        stars = r.get('stargazers_count', 0)
        forks = r.get('forks_count', 0)
        issues = r.get('open_issues_count', 0)

        sql_parts.append(f"""
INSERT INTO repo_snapshots VALUES (
  {repo_id}, now(), {inc_id},
  '{source_name}', '{repo_name}', '{full_name}',
  '{lang}', {stars}, {forks}, {issues},
  '{pushed}', '{desc}'
);""")
        repo_id += 1

    inc_id += 1

# Aptos balances - all addresses
aptos_worlds = {
    "alice": "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b",
    "bob": "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d",
    "A": "0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a",
    "B": "0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13",
    "C": "0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e",
    "D": "0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1",
    "E": "0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36",
    "F": "0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71",
    "G": "0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32",
    "H": "0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f",
    "I": "0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9",
    "J": "0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54",
    "K": "0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4",
    "L": "0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9",
    "M": "0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9",
    "N": "0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c",
    "O": "0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d",
    "P": "0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948",
    "Q": "0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9",
    "R": "0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10",
    "S": "0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386",
    "T": "0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588",
    "U": "0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956",
    "V": "0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3",
    "W": "0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0",
    "X": "0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d",
    "Y": "0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4",
    "Z": "0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c",
}

for world, addr in aptos_worlds.items():
    # All returned resource_not_found (no legacy CoinStore<AptosCoin>)
    sql_parts.append(f"INSERT INTO aptos_snapshots VALUES (now(), '{world}', '{addr}', 0.0);")

# Multisig probes - all returned sigs_required=2
multisig_data = [
    ("A-B", "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2),
    ("A-G", "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2),
    ("Y-Z", "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2),
    ("S-T", "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2),
    ("V-W", "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2),
]
for pair, addr, sigs in multisig_data:
    healthy = "true" if sigs is not None else "false"
    sigs_val = sigs if sigs is not None else 0
    sql_parts.append(f"INSERT INTO multisig_probes VALUES (now(), '{pair}', '{addr}', {sigs_val}, {healthy});")

# MNX - SPA only, no public REST API
sql_parts.append("INSERT INTO mnx_snapshots VALUES (now(), 'N/A', 'MNX testnet SPA - no public REST API', 'unavailable', 0.0, 0.0);")

full_sql = "\n".join(sql_parts)
with open("/tmp/build_world.sql", "w") as f:
    f.write(full_sql)

print(f"Generated SQL: {len(full_sql)} chars")
print(f"Sources: {len(repo_sources)}")
total_repos = sum(len(s['repos'][:30]) for s in repo_sources.values())
print(f"Total repos: {total_repos}")
