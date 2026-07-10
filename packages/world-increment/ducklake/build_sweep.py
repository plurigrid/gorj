#!/usr/bin/env python3
"""world-increment sweep + hamming snapshot builder"""
import duckdb
import hashlib
import json

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
SWEEP_MD = "/home/user/gorj/packages/world-increment/ducklake/LATEST_SWEEP.md"

con = duckdb.connect(DB)

# Create tables
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
con.execute("CREATE SEQUENCE IF NOT EXISTS increment_seq START 1")
con.execute("CREATE SEQUENCE IF NOT EXISTS repo_seq START 1")
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

def gf3(id_val):
    t = id_val % 3
    if t == 0:
        return (0, "#d3869b", "ERGODIC")
    elif t == 1:
        return (1, "#b8bb26", "PLUS")
    else:
        return (-1, "#cc241d", "MINUS")

def next_increment_id():
    return con.execute("SELECT nextval('increment_seq')").fetchone()[0]

def next_repo_id():
    return con.execute("SELECT nextval('repo_seq')").fetchone()[0]

# All gathered repo data
sources = {
    "org:plurigrid": ("org", "plurigrid"),
    "org:kubeflow": ("org", "kubeflow"),
    "org:TeglonLabs": ("org", "TeglonLabs"),
    "user:bmorphism": ("user", "bmorphism"),
    "user:zubyul": ("user", "zubyul"),
    "user:migalkin": ("user", "migalkin"),
    "user:DJedamski": ("user", "DJedamski"),
    "user:wasita": ("user", "wasita"),
    "user:kristinezheng": ("user", "kristinezheng"),
    "user:M1shaaa": ("user", "M1shaaa"),
    "user:AustinCStone": ("user", "AustinCStone"),
}

repo_data = [
    # plurigrid repos (top 20 by push date)
    ("plurigrid","asi","plurigrid/asi","HTML",30,9,4,"2026-07-10T09:48:02Z","everything is topological chemputer!"),
    ("plurigrid","gorj","plurigrid/gorj","Clojure",1,0,1104,"2026-07-07T19:20:50Z","forj + Rama topology nREPL routing"),
    ("plurigrid","shrimp","plurigrid/shrimp",None,0,0,0,"2026-07-03T01:24:20Z","Jank worked example: shrimp"),
    ("plurigrid","place","plurigrid/place","TeX",1,1,12,"2026-06-27T22:03:34Z",None),
    ("plurigrid","ontology","plurigrid/ontology","JavaScript",8,9,16,"2026-05-09T04:20:49Z","autopoietic ergodicity"),
    ("plurigrid","Plurigraph","plurigrid/Plurigraph","JavaScript",3,5,4,"2026-05-12T03:19:41Z","knowledge base"),
    ("plurigrid","nash-portal","plurigrid/nash-portal","Rust",2,3,1,"2026-05-19T01:50:03Z","NASH token TUI in the browser"),
    ("plurigrid","zig-syrup","plurigrid/zig-syrup","Zig",2,2,0,"2026-04-30T03:52:19Z","OCapN Syrup Zig implementation"),
    ("plurigrid","nanoclj-zig","plurigrid/nanoclj-zig","Zig",1,1,20,"2026-04-25T07:29:13Z","NaN-boxed Clojure interpreter in Zig"),
    ("plurigrid","vcg-auction","plurigrid/vcg-auction","Rust",7,3,1,"2025-12-16T12:32:02Z","VCG auction contract"),
    # kubeflow repos (top 10)
    ("kubeflow","kubeflow","kubeflow/kubeflow",None,15772,2685,0,"2026-07-10T17:30:20Z","Machine Learning Toolkit for Kubernetes"),
    ("kubeflow","trainer","kubeflow/trainer","Go",2134,983,145,"2026-07-10T12:20:17Z","Distributed AI Model Training"),
    ("kubeflow","pipelines","kubeflow/pipelines","Python",4169,2030,421,"2026-07-09T18:36:07Z","ML Pipelines for Kubeflow"),
    ("kubeflow","spark-operator","kubeflow/spark-operator","Python",3136,1500,110,"2026-07-09T08:56:50Z","Kubernetes operator for Apache Spark"),
    ("kubeflow","katib","kubeflow/katib","Python",1689,532,112,"2026-07-09T13:35:36Z","Automated ML on Kubernetes"),
    ("kubeflow","mcp-server","kubeflow/mcp-server","Python",20,28,25,"2026-07-10T13:10:56Z","MCP Server for Kubeflow Tools"),
    ("kubeflow","hub","kubeflow/hub","Go",177,188,36,"2026-07-10T14:54:47Z","Model Registry"),
    ("kubeflow","sdk","kubeflow/sdk","Python",123,193,150,"2026-07-10T11:34:13Z","Universal Python SDK for AI workloads"),
    ("kubeflow","mcp-apache-spark-history-server","kubeflow/mcp-apache-spark-history-server","Python",182,65,19,"2026-07-07T06:27:43Z","MCP Server for Apache Spark"),
    ("kubeflow","docs-agent","kubeflow/docs-agent","Python",39,96,155,"2026-07-05T02:25:56Z","Kubeflow Documentation AI Agent"),
    # TeglonLabs repos (all 5)
    ("TeglonLabs","jank-crane","TeglonLabs/jank-crane","C++",0,0,0,"2026-06-08T19:03:37Z","crane-jank converged-IR hub"),
    ("TeglonLabs","mathpix-gem","TeglonLabs/mathpix-gem","Ruby",2,0,11,"2026-01-01T12:13:16Z","Mathematical image to LaTeX"),
    ("TeglonLabs","topoi","TeglonLabs/topoi","Python",0,0,1,"2025-01-24T06:47:38Z",None),
    ("TeglonLabs","coin-flip-mcp","TeglonLabs/coin-flip-mcp","JavaScript",0,2,1,"2025-03-16T01:31:45Z","MCP coin flip server"),
    ("TeglonLabs","monad-mcp-server","TeglonLabs/monad-mcp-server",None,0,0,0,"2025-05-14T17:53:01Z","Monad MCP Server"),
    # bmorphism repos (top 15)
    ("bmorphism","Gay.jl","bmorphism/Gay.jl","Julia",2,1,187,"2026-06-20T14:21:55Z","Wide-gamut color sampling"),
    ("bmorphism","satreadout","bmorphism/satreadout","HTML",0,0,0,"2026-06-20T13:05:44Z","Machine-checked saturating readout"),
    ("bmorphism","bci-preview","bmorphism/bci-preview","HTML",0,0,0,"2026-06-20T00:20:47Z","bci.place forester preview"),
    ("bmorphism","penrose-mcp","bmorphism/penrose-mcp","JavaScript",9,4,0,"2026-06-24T15:36:16Z","Penrose server for Infinity-Topos"),
    ("bmorphism","babashka-mcp-server","bmorphism/babashka-mcp-server","JavaScript",19,6,3,"2026-06-05T13:16:11Z","MCP server for Babashka"),
    ("bmorphism","ocaml-mcp-sdk","bmorphism/ocaml-mcp-sdk","OCaml",61,2,0,"2026-05-08T16:50:34Z","OCaml SDK for MCP"),
    ("bmorphism","anti-bullshit-mcp-server","bmorphism/anti-bullshit-mcp-server","JavaScript",23,7,1,"2026-02-05T15:46:59Z","MCP server for claim analysis"),
    ("bmorphism","manifold-mcp-server","bmorphism/manifold-mcp-server","JavaScript",14,9,5,"2026-04-15T19:54:28Z","Manifold Markets MCP server"),
    ("bmorphism","say-mcp-server","bmorphism/say-mcp-server","JavaScript",20,9,3,"2026-03-19T23:11:59Z","macOS text-to-speech MCP"),
    ("bmorphism","risc0-cosmwasm-example","bmorphism/risc0-cosmwasm-example","Rust",23,2,1,"2025-05-21T13:35:37Z","CosmWasm + zkVM RISC-V"),
    # zubyul repos (top 10)
    ("zubyul","voice-observatory","zubyul/voice-observatory","Python",0,0,0,"2026-04-24T05:56:20Z","Passive macOS TUI for voice-download"),
    ("zubyul","ghostel-emacs-worlds","zubyul/ghostel-emacs-worlds","GLSL",0,0,0,"2026-04-24T00:21:00Z","Ghostty config + emacs-mods"),
    ("zubyul","gay-world","zubyul/gay-world","Python",1,1,0,"2026-04-05T06:54:03Z","Goblin world builder"),
    ("zubyul","Gay.jl","zubyul/Gay.jl","Julia",0,0,0,"2026-03-28T11:30:07Z","Wide-gamut color sampling"),
    ("zubyul","kinesis-kb360pro","zubyul/kinesis-kb360pro","Python",0,0,0,"2026-03-26T10:29:44Z","Kinesis Advantage360 Pro skill"),
    ("zubyul","tilelang-kernels","zubyul/tilelang-kernels","Python",0,0,0,"2026-03-16T02:31:16Z","TileLang GPU kernels GF(3)"),
    ("zubyul","big-bad-plurigrid-quiz","zubyul/big-bad-plurigrid-quiz","Emacs Lisp",0,0,0,"2026-04-09T18:51:35Z","27 flashcards plurigrid activity"),
    # migalkin repos (top 5)
    ("migalkin","NodePiece","migalkin/NodePiece","Python",144,21,0,"2026-05-07T05:40:02Z","Compositional KG representations"),
    ("migalkin","StarE","migalkin/StarE","Python",89,16,1,"2026-04-16T14:12:45Z","Hyper-relational KG message passing"),
    ("migalkin","kgcourse2021","migalkin/kgcourse2021","HTML",24,9,0,"2026-07-10T15:40:00Z","Knowledge Graphs course"),
    ("migalkin","NBFNet_mlx","migalkin/NBFNet_mlx","Python",10,1,1,"2026-03-11T01:31:21Z","Neural Bellman-Ford networks MLX"),
    ("migalkin","RWL","migalkin/RWL","Python",8,1,0,"2026-05-28T20:19:20Z","Weisfeiler Leman Relational"),
    # DJedamski repos (top 3)
    ("DJedamski","kaggle_ncaa18","DJedamski/kaggle_ncaa18","Jupyter Notebook",0,0,0,"2018-02-26T16:33:24Z","NCAA March Madness 2018"),
    ("DJedamski","Kaggle","DJedamski/Kaggle",None,1,0,0,"2023-04-21T01:42:35Z",None),
    ("DJedamski","School","DJedamski/School","R",1,1,0,"2023-04-21T01:42:33Z","Grad school projects"),
    # wasita repos (top 5)
    ("wasita","wasita.github.io","wasita/wasita.github.io","Svelte",1,0,8,"2026-07-06T23:51:09Z","personal website"),
    ("wasita","magic-garden","wasita/magic-garden","Python",2,1,1,"2026-04-22T21:16:43Z","Discord magic garden bot"),
    ("wasita","send2kobo","wasita/send2kobo","TypeScript",1,0,0,"2026-05-19T02:59:26Z","Send books to Kobo"),
    ("wasita","proj-template","wasita/proj-template",None,0,0,0,"2026-06-19T21:22:21Z",None),
    ("wasita","wm-cv","wasita/wm-cv","Svelte",0,0,0,"2026-05-13T05:29:08Z","Academic CV as web app"),
    # kristinezheng repos
    ("kristinezheng","kristinezheng.github.io","kristinezheng/kristinezheng.github.io","HTML",0,0,0,"2026-07-01T20:57:48Z",None),
    ("kristinezheng","lookit-jenga","kristinezheng/lookit-jenga","Jupyter Notebook",0,0,0,"2024-05-16T18:29:05Z","Lookit study"),
    ("kristinezheng","Green-Machine","kristinezheng/Green-Machine","Python",0,0,0,"2021-09-19T05:33:04Z","HackMIT 2021 Sustainability"),
    # M1shaaa repos
    ("M1shaaa","M1shaaa","M1shaaa/M1shaaa",None,0,0,0,"2026-02-04T19:32:04Z","Config files"),
    ("M1shaaa","lab-bookshelf-","M1shaaa/lab-bookshelf-","TypeScript",0,0,0,"2024-12-31T05:11:18Z",None),
    ("M1shaaa","Python-Lookit-Uploads","M1shaaa/Python-Lookit-Uploads","Python",0,0,0,"2024-02-15T22:59:37Z","Random projects"),
    # AustinCStone repos (top 5)
    ("AustinCStone","TextGAN","AustinCStone/TextGAN","Python",92,30,5,"2025-03-03T13:26:32Z","GAN for text generation in TensorFlow"),
    ("AustinCStone","StereoVisionMRF","AustinCStone/StereoVisionMRF","Python",11,4,0,"2026-04-01T07:39:41Z","3D geometry from stereo MRF"),
    ("AustinCStone","EpsteinSearch","AustinCStone/EpsteinSearch","Python",0,0,0,"2026-02-11T01:10:57Z",None),
    ("AustinCStone","SpectralClustering","AustinCStone/SpectralClustering","Python",3,2,0,"2021-04-16T08:46:38Z","Spectral clustering"),
    ("AustinCStone","StructureFromMotion","AustinCStone/StructureFromMotion","Python",1,0,0,"2019-04-26T19:43:12Z","Recover 3D geometry from videos"),
]

# Insert all repo snapshots with increment records
for i, (org, repo, full, lang, stars, forks, issues, pushed, desc) in enumerate(repo_data):
    incr_id = next_increment_id()
    trit, color, name = gf3(incr_id)
    snap_hash = hashlib.sha256(full.encode()).hexdigest()[:16]
    con.execute("""
        INSERT INTO world_increments VALUES (?, now(), ?, ?, ?, 'github_snapshot', ?, 'repo_push', ?, ?, ?)
    """, [incr_id, trit, color, name, org, repo, org, snap_hash])
    repo_id = next_repo_id()
    con.execute("""
        INSERT INTO repo_snapshots VALUES (?, now(), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [repo_id, incr_id, org, repo, full, lang, stars, forks, issues, pushed, desc])

# Aptos wallets (all 0 APT - resource_not_found on mainnet)
APTOS_ADDRS = [
    ("alice","0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b",0.0),
    ("bob","0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d",0.0),
    ("A","0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a",0.0),
    ("B","0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13",0.0),
    ("C","0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e",0.0),
    ("D","0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1",0.0),
    ("E","0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36",0.0),
    ("F","0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71",0.0),
    ("G","0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32",0.0),
    ("H","0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f",0.0),
    ("I","0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9",0.0),
    ("J","0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54",0.0),
    ("K","0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4",0.0),
    ("L","0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9",0.0),
    ("M","0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9",0.0),
    ("N","0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c",0.0),
    ("O","0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d",0.0),
    ("P","0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948",0.0),
    ("Q","0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9",0.0),
    ("R","0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10",0.0),
    ("S","0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386",0.0),
    ("T","0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588",0.0),
    ("U","0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956",0.0),
    ("V","0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3",0.0),
    ("W","0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0",0.0),
    ("X","0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d",0.0),
    ("Y","0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4",0.0),
    ("Z","0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c",0.0),
]
for world, addr, bal in APTOS_ADDRS:
    con.execute("INSERT INTO aptos_snapshots VALUES (now(), ?, ?, ?)", [world, addr, bal])

# Multisig probes (all healthy, 2 sigs required)
MULTISIGS = [
    ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2),
    ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2),
    ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2),
    ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2),
    ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2),
]
for pair, addr, sigs in MULTISIGS:
    con.execute("INSERT INTO multisig_probes VALUES (now(), ?, ?, ?, ?)", [pair, addr, sigs, True])

# Query summary stats
repo_count = con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0]
incr_count = con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0]
aptos_count = con.execute("SELECT COUNT(*) FROM aptos_snapshots").fetchone()[0]
multisig_count = con.execute("SELECT COUNT(*) FROM multisig_probes").fetchone()[0]

# GF3 color distribution
gf3_dist = con.execute("""
    SELECT gf3_name, gf3_color, COUNT(*) as cnt
    FROM world_increments GROUP BY gf3_name, gf3_color ORDER BY cnt DESC
""").fetchall()

# Top repos by stars
top_repos = con.execute("""
    SELECT org_or_user, repo_name, stars, language
    FROM repo_snapshots WHERE stars > 0 ORDER BY stars DESC LIMIT 15
""").fetchall()

# Source breakdown
source_breakdown = con.execute("""
    SELECT source_name, COUNT(*) as cnt FROM world_increments GROUP BY source_name ORDER BY cnt DESC
""").fetchall()

con.close()

# Write LATEST_SWEEP.md
md = f"""# World Increment Sweep — 2026-07-10

## Summary

| Metric | Value |
|--------|-------|
| World increments recorded | {incr_count} |
| Repo snapshots | {repo_count} |
| Aptos wallet probes | {aptos_count} |
| Multisig contract probes | {multisig_count} |
| MNX testnet | Unavailable (Vercel auth required) |

---

## Job 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type |
|--------|------|
| plurigrid | org |
| kubeflow | org |
| TeglonLabs | org |
| bmorphism | user |
| zubyul | user |
| migalkin | user (zubyul social) |
| DJedamski | user (zubyul social) |
| wasita | user (zubyul social) |
| kristinezheng | user (zubyul social) |
| M1shaaa | user (zubyul social) |
| AustinCStone | user (zubyul social) |

### Top Repos by Stars

| Org/User | Repo | Stars | Language |
|----------|------|-------|----------|
"""
for org, repo, stars, lang in top_repos:
    md += f"| {org} | {repo} | {stars} | {lang or 'N/A'} |\n"

md += f"""
### GF(3) Color Chain Distribution

| Trit Name | Color | Count |
|-----------|-------|-------|
"""
for name, color, cnt in gf3_dist:
    md += f"| {name} | `{color}` | {cnt} |\n"

md += f"""
### Increment Source Breakdown

| Source | Increments |
|--------|-----------|
"""
for src, cnt in source_breakdown:
    md += f"| {src} | {cnt} |\n"

md += """
---

## Job 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (A–Z + alice/bob)

All 28 Hamming swarm addresses probed on Aptos mainnet.
Result: All addresses return `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
This indicates the addresses are registered on-chain but hold **0 APT** (no CoinStore initialized).

| World | Balance (APT) | Status |
|-------|---------------|--------|
"""
for world, addr, bal in APTOS_ADDRS:
    status = "resource_not_found (0 APT)"
    md += f"| {world} | {bal} | {status} |\n"

md += """
### Multisig Contract Probes

All 5 multisig pairs probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
"""
for pair, addr, sigs in MULTISIGS:
    md += f"| {pair} | `{addr[:16]}…` | {sigs} | ✓ |\n"

md += """
### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — Vercel deployment protection requires authentication.
The testnet.mnx.fi endpoint returns HTTP 200 with an authentication challenge page.
No market data could be extracted.

---

*Generated by world-increment-sweep + hamming-swarm-snapshot agent*
*Ledger version probed: 6216957827 (Aptos mainnet)*
"""

with open(SWEEP_MD, "w") as f:
    f.write(md)

print(f"Done: {incr_count} increments, {repo_count} repos, {aptos_count} Aptos probes, {multisig_count} multisig probes")
print(f"Wrote {SWEEP_MD}")
