#!/usr/bin/env python3
"""Build world-increments DuckDB from collected sweep data."""
import json, subprocess, os, hashlib, datetime

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"

# GF(3) color chain
def gf3(id_):
    t = id_ % 3
    if t == 0: return 0, "ERGODIC", "#d3869b"
    if t == 1: return 1, "PLUS", "#b8bb26"
    return -1, "MINUS", "#cc241d"

def snap_hash(*args):
    return hashlib.sha256("|".join(str(a) for a in args).encode()).hexdigest()[:16]

# ---- REPO DATA ----
# plurigrid repos from saved file
plurigrid_raw = open('/root/.claude/projects/-home-user-gorj/0aa8fa92-d3d3-583b-b25b-1939680f4f90/tool-results/mcp-github-search_repositories-1786356854983.txt').read()
plurigrid_data = json.loads(plurigrid_raw)
plurigrid_items = plurigrid_data.get('items', plurigrid_data) if isinstance(plurigrid_data, dict) else plurigrid_data

kubeflow_raw = open('/root/.claire/projects/-home-user-gorj/0aa8fa92-d3d3-583b-b25b-1939680f4f90/tool-results/mcp-github-search_repositories-1786356853390.txt').read() if False else open('/root/.claude/projects/-home-user-gorj/0aa8fa92-d3d3-583b-b25b-1939680f4f90/tool-results/mcp-github-search_repositories-1786356853390.txt').read()
kubeflow_data = json.loads(kubeflow_raw)
kubeflow_items = kubeflow_data.get('items', kubeflow_data) if isinstance(kubeflow_data, dict) else kubeflow_data

# TeglonLabs (already collected in main context)
teglon_items = [
    {"name":"jank-crane","full_name":"TeglonLabs/jank-crane","language":"C++","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-06-08T19:03:37Z","description":"crane-jank converged-IR hub"},
    {"name":"mathpix-gem","full_name":"TeglonLabs/mathpix-gem","language":"Ruby","stargazers_count":2,"forks_count":0,"open_issues_count":11,"pushed_at":"2026-01-01T12:13:16Z","description":"Transform mathematical images to LaTeX"},
    {"name":"coin-flip-mcp","full_name":"TeglonLabs/coin-flip-mcp","language":"JavaScript","stargazers_count":0,"forks_count":2,"open_issues_count":1,"pushed_at":"2025-03-16T01:31:45Z","description":"MCP server for flipping coins"},
    {"name":"monad-mcp-server","full_name":"TeglonLabs/monad-mcp-server","language":None,"stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-05-14T17:53:01Z","description":"Monad MCP Server"},
    {"name":"topoi","full_name":"TeglonLabs/topoi","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":1,"pushed_at":"2025-01-24T06:47:38Z","description":None},
]

bmorphism_items = [
    {"name":"nashator-h1","full_name":"bmorphism/nashator-h1","language":"Clojure","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-08-10T10:12:04Z","description":"Cech-H1 triangular-arbitrage detector"},
    {"name":"oldies-clearing","full_name":"bmorphism/oldies-clearing","language":"Agda","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-08-10T10:00:00Z","description":"Cut-elimination IS obligation clearing"},
    {"name":"attention-heat-capacity","full_name":"bmorphism/attention-heat-capacity","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-08-10T09:47:41Z","description":"Attention-row heat capacity C=Var(log alpha)"},
    {"name":"paraoptic","full_name":"bmorphism/paraoptic","language":"Lean","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-08-10T09:47:39Z","description":"Para(C) - Optic(C) - Para(Optic(C))"},
    {"name":"keywire","full_name":"bmorphism/keywire","language":"Clojure","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-08-10T09:47:38Z","description":"Key-addressed service proxy over iroh QUIC"},
    {"name":"Gay.jl","full_name":"bmorphism/Gay.jl","language":"Julia","stargazers_count":2,"forks_count":1,"open_issues_count":188,"pushed_at":"2026-07-21T12:57:35Z","description":"Wide-gamut color sampling"},
    {"name":"anti-bullshit-mcp-server","full_name":"bmorphism/anti-bullshit-mcp-server","language":"JavaScript","stargazers_count":23,"forks_count":7,"open_issues_count":1,"pushed_at":"2026-08-02T12:54:58Z","description":"MCP server for analyzing claims"},
    {"name":"penrose-mcp","full_name":"bmorphism/penrose-mcp","language":"JavaScript","stargazers_count":9,"forks_count":4,"open_issues_count":0,"pushed_at":"2026-06-24T15:36:16Z","description":"Penrose server for the Infinity-Topos environment"},
    {"name":"ocaml-mcp-sdk","full_name":"bmorphism/ocaml-mcp-sdk","language":"OCaml","stargazers_count":61,"forks_count":2,"open_issues_count":0,"pushed_at":"2026-05-08T16:50:34Z","description":"OCaml SDK for Model Context Protocol"},
    {"name":"babashka-mcp-server","full_name":"bmorphism/babashka-mcp-server","language":"JavaScript","stargazers_count":19,"forks_count":6,"open_issues_count":3,"pushed_at":"2026-06-05T13:16:11Z","description":"A Model Context Protocol server for Babashka"},
]

zubyul_items = [
    {"name":"voice-observatory","full_name":"zubyul/voice-observatory","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-24T05:56:20Z","description":"Passive macOS TUI observing voice-download pathways"},
    {"name":"ghostel-emacs-worlds","full_name":"zubyul/ghostel-emacs-worlds","language":"GLSL","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-24T00:21:00Z","description":"Ghostty config + ghostel family"},
    {"name":"big-bad-plurigrid-quiz","full_name":"zubyul/big-bad-plurigrid-quiz","language":"Emacs Lisp","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-09T18:51:35Z","description":"27 flashcards from bmorphism/plurigrid/zubyul/monaduck1069"},
    {"name":"Gay.jl","full_name":"zubyul/Gay.jl","language":"Julia","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-28T11:30:07Z","description":"Wide-gamut color sampling"},
    {"name":"tilelang-kernels","full_name":"zubyul/tilelang-kernels","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-16T02:31:16Z","description":"TileLang GPU kernels for SplitMix64 color generation"},
    {"name":"gay-world","full_name":"zubyul/gay-world","language":"Python","stargazers_count":1,"forks_count":1,"open_issues_count":0,"pushed_at":"2026-04-05T06:54:03Z","description":"Goblin world builder"},
]

migalkin_items = [
    {"name":"NodePiece","full_name":"migalkin/NodePiece","language":"Python","stargazers_count":144,"forks_count":21,"open_issues_count":0,"pushed_at":"2026-05-07T05:40:02Z","description":"Compositional and Parameter-Efficient Representations (ICLR 2022)"},
    {"name":"StarE","full_name":"migalkin/StarE","language":"Python","stargazers_count":89,"forks_count":16,"open_issues_count":1,"pushed_at":"2026-04-16T14:12:45Z","description":"Message Passing for Hyper-Relational Knowledge Graphs"},
    {"name":"kgcourse2021","full_name":"migalkin/kgcourse2021","language":"HTML","stargazers_count":24,"forks_count":8,"open_issues_count":0,"pushed_at":"2026-07-10T15:40:00Z","description":"Курс по Knowledge Graphs"},
    {"name":"NBFNet_mlx","full_name":"migalkin/NBFNet_mlx","language":"Python","stargazers_count":10,"forks_count":1,"open_issues_count":1,"pushed_at":"2026-03-11T01:31:21Z","description":"Neural Bellman-Ford networks in MLX"},
]

wasita_items = [
    {"name":"xoxowasita-analysis","full_name":"wasita/xoxowasita-analysis","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-08-10T03:48:50Z","description":None},
    {"name":"wasita.github.io","full_name":"wasita/wasita.github.io","language":"Svelte","stargazers_count":1,"forks_count":0,"open_issues_count":8,"pushed_at":"2026-08-10T02:27:08Z","description":"personal website"},
    {"name":"wm-cv","full_name":"wasita/wm-cv","language":"Svelte","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-08-07T20:46:15Z","description":"Academic CV"},
    {"name":"magic-garden","full_name":"wasita/magic-garden","language":"Python","stargazers_count":2,"forks_count":1,"open_issues_count":1,"pushed_at":"2026-04-22T21:16:43Z","description":"Magic garden discord bot"},
]

kristinezheng_items = [
    {"name":"kristinezheng.github.io","full_name":"kristinezheng/kristinezheng.github.io","language":"HTML","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-07-01T20:57:48Z","description":None},
    {"name":"lookit-jenga","full_name":"kristinezheng/lookit-jenga","language":"Jupyter Notebook","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2024-05-16T18:29:05Z","description":"Lookit study"},
]

DJedamski_items = [
    {"name":"kaggle_ncaa18","full_name":"DJedamski/kaggle_ncaa18","language":"Jupyter Notebook","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2018-02-26T16:33:24Z","description":"NCAA March Madness competition"},
    {"name":"Kaggle","full_name":"DJedamski/Kaggle","language":None,"stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2023-04-21T01:42:35Z","description":None},
]

AustinCStone_items = [
    {"name":"byteruckus","full_name":"AustinCStone/byteruckus","language":"HTML","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-07-15T05:19:33Z","description":None},
    {"name":"TextGAN","full_name":"AustinCStone/TextGAN","language":"Python","stargazers_count":92,"forks_count":30,"open_issues_count":5,"pushed_at":"2025-03-03T13:26:32Z","description":"GAN for text generation"},
    {"name":"StereoVisionMRF","full_name":"AustinCStone/StereoVisionMRF","language":"Python","stargazers_count":11,"forks_count":4,"open_issues_count":0,"pushed_at":"2026-04-01T07:39:41Z","description":"MRF with loopy belief propagation"},
]

M1shaaa_items = [
    {"name":"M1shaaa","full_name":"M1shaaa/M1shaaa","language":None,"stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-02-04T19:32:04Z","description":"Config files for GitHub profile"},
    {"name":"lab-bookshelf-","full_name":"M1shaaa/lab-bookshelf-","language":"TypeScript","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2024-12-31T05:11:18Z","description":None},
]

all_sources = [
    ("org", "plurigrid", plurigrid_items[:30]),
    ("org", "kubeflow", kubeflow_items[:30]),
    ("org", "TeglonLabs", teglon_items),
    ("user", "bmorphism", bmorphism_items),
    ("user", "zubyul", zubyul_items),
    ("social", "migalkin", migalkin_items),
    ("social", "DJedamski", DJedamski_items),
    ("social", "wasita", wasita_items),
    ("social", "kristinezheng", kristinezheng_items),
    ("social", "M1shaaa", M1shaaa_items),
    ("social", "AustinCStone", AustinCStone_items),
]

# ---- APTOS DATA ----
aptos_data = [
    ("alice", "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b", 0.0),
    ("bob", "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d", 0.0),
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

multisig_data = [
    ("A-B", "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2, True),
    ("A-G", "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2, True),
    ("Y-Z", "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2, True),
    ("S-T", "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2, True),
    ("V-W", "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2, True),
]

# Build SQL script
lines = []
lines.append("CREATE TABLE IF NOT EXISTS world_increments (")
lines.append("  id INTEGER, timestamp TIMESTAMP DEFAULT now(), gf3_trit INTEGER,")
lines.append("  gf3_color VARCHAR, gf3_name VARCHAR, source_type VARCHAR,")
lines.append("  source_name VARCHAR, event_type VARCHAR, repo_name VARCHAR,")
lines.append("  actor VARCHAR, snapshot_hash VARCHAR")
lines.append(");")
lines.append("CREATE TABLE IF NOT EXISTS repo_snapshots (")
lines.append("  id INTEGER, timestamp TIMESTAMP DEFAULT now(), increment_id INTEGER,")
lines.append("  org_or_user VARCHAR, repo_name VARCHAR, full_name VARCHAR,")
lines.append("  language VARCHAR, stars INTEGER, forks INTEGER, open_issues INTEGER,")
lines.append("  pushed_at VARCHAR, description VARCHAR")
lines.append(");")
lines.append("CREATE TABLE IF NOT EXISTS aptos_snapshots (")
lines.append("  timestamp TIMESTAMP DEFAULT now(),")
lines.append("  world VARCHAR, address VARCHAR, balance_apt DOUBLE")
lines.append(");")
lines.append("CREATE TABLE IF NOT EXISTS multisig_probes (")
lines.append("  timestamp TIMESTAMP DEFAULT now(),")
lines.append("  pair VARCHAR, address VARCHAR, sigs_required INTEGER, healthy BOOLEAN")
lines.append(");")
lines.append("CREATE TABLE IF NOT EXISTS mnx_snapshots (")
lines.append("  timestamp TIMESTAMP DEFAULT now(),")
lines.append("  ticker VARCHAR, name VARCHAR, category VARCHAR,")
lines.append("  price DOUBLE, change_pct DOUBLE")
lines.append(");")
lines.append("CREATE SEQUENCE IF NOT EXISTS increment_seq START 1;")
lines.append("CREATE SEQUENCE IF NOT EXISTS repo_seq START 1;")

# Build increment and repo inserts
inc_id = 1
repo_id = 1
for src_type, src_name, items in all_sources:
    trit, color, gf3_name = gf3(inc_id)
    h = snap_hash(src_type, src_name, inc_id)
    desc_safe = src_name.replace("'","''")
    lines.append(f"INSERT INTO world_increments VALUES ({inc_id}, now(), {trit}, '{color}', '{gf3_name}', '{src_type}', '{desc_safe}', 'repo_sweep', '', 'sweep-agent', '{h}');")
    for r in items:
        rname = (r.get('name','') or '').replace("'","''")
        fname = (r.get('full_name','') or '').replace("'","''")
        lang = (r.get('language') or '').replace("'","''")
        stars = r.get('stargazers_count', 0) or 0
        forks = r.get('forks_count', 0) or 0
        issues = r.get('open_issues_count', 0) or 0
        pushed = (r.get('pushed_at') or r.get('updated_at','') or '').replace("'","''")
        desc = (r.get('description') or '').replace("'","''")[:200]
        ou = src_name.replace("'","''")
        trit2, color2, gf3_name2 = gf3(repo_id)
        lines.append(f"INSERT INTO repo_snapshots VALUES ({repo_id}, now(), {inc_id}, '{ou}', '{rname}', '{fname}', '{lang}', {stars}, {forks}, {issues}, '{pushed}', '{desc}');")
        repo_id += 1
    inc_id += 1

# Aptos snapshots
for world, addr, bal in aptos_data:
    lines.append(f"INSERT INTO aptos_snapshots VALUES (now(), '{world}', '{addr}', {bal});")

# Multisig probes
for pair, addr, sigs, healthy in multisig_data:
    lines.append(f"INSERT INTO multisig_probes VALUES (now(), '{pair}', '{addr}', {sigs}, {str(healthy).upper()});")

# MNX snapshot - SPA only, no data available
lines.append("-- MNX testnet: SPA only (Next.js), no JSON API endpoint accessible (HTTP 404 on all /api/* paths)")
lines.append("INSERT INTO mnx_snapshots VALUES (now(), 'N/A', 'mnx.fi testnet', 'unavailable', NULL, NULL);")

sql = "\n".join(lines)
sql_file = "/tmp/build_world_increments.sql"
with open(sql_file, "w") as f:
    f.write(sql)

print(f"SQL written to {sql_file} ({len(lines)} statements)")
print(f"Increments: {inc_id-1}, Repos: {repo_id-1}, Aptos: {len(aptos_data)}, Multisig: {len(multisig_data)}")
