#!/usr/bin/env python3
"""Build world-increments.duckdb from collected GitHub + Aptos data."""

import json, subprocess, os, hashlib
from pathlib import Path

DB = str(Path(__file__).parent / "world-increments.duckdb")

def esc(s):
    if s is None: return "NULL"
    return "'" + str(s).replace("'", "''") + "'"

def run_sql(sql):
    r = subprocess.run(["duckdb", DB], input=sql, capture_output=True, text=True)
    if r.returncode != 0 and r.stderr:
        print("SQL ERR:", r.stderr[:300])
    return r.stdout

# ── Schema ───────────────────────────────────────────────────────────────────
SCHEMA = """
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
"""
run_sql(SCHEMA)
print("Schema created.")

# ── GF(3) helpers ─────────────────────────────────────────────────────────────
def gf3(n):
    m = n % 3
    if m == 0: return (0, "#d3869b", "ERGODIC")
    if m == 1: return (1, "#b8bb26", "PLUS")
    return (-1, "#cc241d", "MINUS")

# ── Load repos from files + inline ───────────────────────────────────────────
tool_dir = Path("/root/.claude/projects/-home-user-gorj/d2db5c5e-0690-4299-94af-88b61c81f41a/tool-results")

def load_repo_file(path, org_or_user):
    try:
        with open(path) as f:
            data = json.load(f)
        text = data[0]["text"]
        items = json.loads(text)["items"]
        return [
            {
                "org_or_user": org_or_user,
                "full_name": r["full_name"],
                "repo_name": r["name"],
                "language": r.get("language") or "",
                "stars": r.get("stargazers_count", 0),
                "forks": r.get("forks_count", 0),
                "open_issues": r.get("open_issues_count", 0),
                "pushed_at": r.get("pushed_at", ""),
                "description": r.get("description") or "",
            }
            for r in items
        ]
    except Exception as e:
        print(f"  Warning loading {path}: {e}")
        return []

repos = []

# From saved files
file_map = {
    "mcp-github-search_repositories-1778051156376.txt": "plurigrid",
    "mcp-github-search_repositories-1778051153542.txt": "kubeflow",
    "mcp-github-search_repositories-1778051157213.txt": "bmorphism",
    "mcp-github-search_repositories-1778051155285.txt": "zubyul",
}
for fname, org in file_map.items():
    p = tool_dir / fname
    if p.exists():
        batch = load_repo_file(p, org)
        repos.extend(batch)
        print(f"  Loaded {len(batch)} repos for {org}")

# Inline data for remaining sources
inline_repos = [
    # TeglonLabs
    {"org_or_user":"TeglonLabs","full_name":"TeglonLabs/mathpix-gem","repo_name":"mathpix-gem","language":"Ruby","stars":2,"forks":0,"open_issues":11,"pushed_at":"2026-01-01T12:13:13Z","description":"Transform mathematical images to LaTeX, chemistry structures to SMILES"},
    {"org_or_user":"TeglonLabs","full_name":"TeglonLabs/monad-mcp-server","repo_name":"monad-mcp-server","language":"JavaScript","stars":0,"forks":0,"open_issues":0,"pushed_at":"2025-05-14T11:36:14Z","description":"Monad MCP Server"},
    {"org_or_user":"TeglonLabs","full_name":"TeglonLabs/topoi","repo_name":"topoi","language":"Python","stars":0,"forks":0,"open_issues":1,"pushed_at":"2025-01-24T04:49:26Z","description":""},
    {"org_or_user":"TeglonLabs","full_name":"TeglonLabs/coin-flip-mcp","repo_name":"coin-flip-mcp","language":"JavaScript","stars":0,"forks":2,"open_issues":1,"pushed_at":"2025-09-21T08:57:27Z","description":"MCP server for flipping coins with varying degrees of randomness"},
    # migalkin
    {"org_or_user":"migalkin","full_name":"migalkin/kgcourse2021","repo_name":"kgcourse2021","language":"HTML","stars":25,"forks":9,"open_issues":0,"pushed_at":"2026-02-16T05:16:08Z","description":"Knowledge Graphs course materials"},
    {"org_or_user":"migalkin","full_name":"migalkin/NBFNet_mlx","repo_name":"NBFNet_mlx","language":"Python","stars":10,"forks":1,"open_issues":1,"pushed_at":"2026-03-11T01:31:21Z","description":"Neural Bellman-Ford networks in MLX for Apple Silicon"},
    {"org_or_user":"migalkin","full_name":"migalkin/StarE","repo_name":"StarE","language":"Python","stars":89,"forks":16,"open_issues":1,"pushed_at":"2026-04-16T14:12:45Z","description":"EMNLP 2020: Message Passing for Hyper-Relational Knowledge Graphs"},
    {"org_or_user":"migalkin","full_name":"migalkin/NodePiece","repo_name":"NodePiece","language":"Python","stars":143,"forks":21,"open_issues":0,"pushed_at":"2026-03-02T09:39:45Z","description":"Compositional Parameter-Efficient Representations for Large KGs (ICLR 2022)"},
    {"org_or_user":"migalkin","full_name":"migalkin/RWL","repo_name":"RWL","language":"Python","stars":7,"forks":1,"open_issues":0,"pushed_at":"2025-02-10T14:12:14Z","description":"Weisfeiler and Leman Go Relational (LOG 2022)"},
    {"org_or_user":"migalkin","full_name":"migalkin/rambo","repo_name":"rambo","language":"Rust","stars":3,"forks":0,"open_issues":1,"pushed_at":"2023-02-28T16:37:22Z","description":""},
    # DJedamski
    {"org_or_user":"DJedamski","full_name":"DJedamski/kaggle_ncaa18","repo_name":"kaggle_ncaa18","language":"Jupyter Notebook","stars":0,"forks":0,"open_issues":0,"pushed_at":"2018-02-26T16:33:24Z","description":"Code for NCAA March Madness competition 2018"},
    {"org_or_user":"DJedamski","full_name":"DJedamski/Kaggle","repo_name":"Kaggle","language":"","stars":1,"forks":0,"open_issues":0,"pushed_at":"2023-04-21T01:42:35Z","description":""},
    {"org_or_user":"DJedamski","full_name":"DJedamski/Getting-and-Cleaning-Data","repo_name":"Getting-and-Cleaning-Data","language":"R","stars":1,"forks":0,"open_issues":0,"pushed_at":"2023-04-21T01:42:34Z","description":"Coursera Project"},
    {"org_or_user":"DJedamski","full_name":"DJedamski/School","repo_name":"School","language":"R","stars":1,"forks":1,"open_issues":0,"pushed_at":"2023-04-21T01:42:33Z","description":"A couple small projects from grad school"},
    {"org_or_user":"DJedamski","full_name":"DJedamski/EDA","repo_name":"EDA","language":"R","stars":0,"forks":0,"open_issues":0,"pushed_at":"2014-11-09T17:00:39Z","description":"Coursera Project"},
    # wasita
    {"org_or_user":"wasita","full_name":"wasita/vocoder","repo_name":"vocoder","language":"JavaScript","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-05-06T05:14:03Z","description":""},
    {"org_or_user":"wasita","full_name":"wasita/wasita.github.io","repo_name":"wasita.github.io","language":"Svelte","stars":1,"forks":0,"open_issues":8,"pushed_at":"2026-04-28T05:26:08Z","description":"personal website"},
    {"org_or_user":"wasita","full_name":"wasita/ch3-lib","repo_name":"ch3-lib","language":"Typst","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-12T04:03:22Z","description":""},
    {"org_or_user":"wasita","full_name":"wasita/wm-cv","repo_name":"wm-cv","language":"Svelte","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-12T02:53:51Z","description":"Academic CV as single page web app"},
    {"org_or_user":"wasita","full_name":"wasita/magic-garden","repo_name":"magic-garden","language":"Python","stars":2,"forks":1,"open_issues":1,"pushed_at":"2026-04-22T21:16:43Z","description":"Discord game bot"},
    {"org_or_user":"wasita","full_name":"wasita/send2kobo","repo_name":"send2kobo","language":"TypeScript","stars":0,"forks":0,"open_issues":0,"pushed_at":"2025-12-12T19:09:16Z","description":"Website for sending books to kobo e-reader"},
    {"org_or_user":"wasita","full_name":"wasita/wins-search","repo_name":"wins-search","language":"CSS","stars":1,"forks":0,"open_issues":0,"pushed_at":"2023-06-03T19:01:11Z","description":"Women in Network Science member list website"},
    # kristinezheng
    {"org_or_user":"kristinezheng","full_name":"kristinezheng/kristinezheng.github.io","repo_name":"kristinezheng.github.io","language":"HTML","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-04-09T17:09:47Z","description":""},
    {"org_or_user":"kristinezheng","full_name":"kristinezheng/lookit-jenga","repo_name":"lookit-jenga","language":"Jupyter Notebook","stars":0,"forks":0,"open_issues":0,"pushed_at":"2024-05-16T18:29:05Z","description":"Lookit study for 9.85"},
    {"org_or_user":"kristinezheng","full_name":"kristinezheng/Portfolio","repo_name":"Portfolio","language":"","stars":0,"forks":0,"open_issues":0,"pushed_at":"2025-02-12T00:00:45Z","description":"July 2021"},
    {"org_or_user":"kristinezheng","full_name":"kristinezheng/auditory-illusion","repo_name":"auditory-illusion","language":"CSS","stars":0,"forks":0,"open_issues":0,"pushed_at":"2022-03-07T02:57:44Z","description":"9.35 spring 2022 auditory illusion"},
    {"org_or_user":"kristinezheng","full_name":"kristinezheng/Green-Machine","repo_name":"Green-Machine","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2021-09-19T05:33:04Z","description":"HackMIT 2021: Sustainability Track"},
    # M1shaaa
    {"org_or_user":"M1shaaa","full_name":"M1shaaa/M1shaaa","repo_name":"M1shaaa","language":"","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-02-04T19:32:04Z","description":"Config files for GitHub profile"},
    {"org_or_user":"M1shaaa","full_name":"M1shaaa/lab-bookshelf-","repo_name":"lab-bookshelf-","language":"TypeScript","stars":0,"forks":0,"open_issues":0,"pushed_at":"2024-12-31T05:11:18Z","description":""},
    {"org_or_user":"M1shaaa","full_name":"M1shaaa/Python-Lookit-Uploads","repo_name":"Python-Lookit-Uploads","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2024-02-15T22:59:37Z","description":"random projects"},
    {"org_or_user":"M1shaaa","full_name":"M1shaaa/Classes","repo_name":"Classes","language":"","stars":0,"forks":0,"open_issues":0,"pushed_at":"2023-12-06T18:20:27Z","description":""},
    {"org_or_user":"M1shaaa","full_name":"M1shaaa/MNIST-Classifier","repo_name":"MNIST-Classifier","language":"","stars":0,"forks":0,"open_issues":0,"pushed_at":"2023-11-28T06:10:47Z","description":""},
    # AustinCStone
    {"org_or_user":"AustinCStone","full_name":"AustinCStone/EpsteinSearch","repo_name":"EpsteinSearch","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2026-02-11T01:10:57Z","description":""},
    {"org_or_user":"AustinCStone","full_name":"AustinCStone/TextGAN","repo_name":"TextGAN","language":"Python","stars":92,"forks":30,"open_issues":5,"pushed_at":"2025-03-03T13:26:32Z","description":"Generative adversarial network for text generation in TensorFlow"},
    {"org_or_user":"AustinCStone","full_name":"AustinCStone/StereoVisionMRF","repo_name":"StereoVisionMRF","language":"Python","stars":11,"forks":4,"open_issues":0,"pushed_at":"2026-04-01T07:39:41Z","description":"MRF-based depth inference from stereo images"},
    {"org_or_user":"AustinCStone","full_name":"AustinCStone/SpectralClustering","repo_name":"SpectralClustering","language":"Python","stars":3,"forks":2,"open_issues":0,"pushed_at":"2021-04-16T08:46:36Z","description":"Implementing spectral clustering"},
    {"org_or_user":"AustinCStone","full_name":"AustinCStone/TFBirds","repo_name":"TFBirds","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2019-01-30T08:07:22Z","description":"Bird flocking simulator in TensorFlow"},
    {"org_or_user":"AustinCStone","full_name":"AustinCStone/StructureFromMotion","repo_name":"StructureFromMotion","language":"Python","stars":1,"forks":0,"open_issues":0,"pushed_at":"2019-04-26T19:43:12Z","description":"Recover 3D geometry from videos"},
    {"org_or_user":"AustinCStone","full_name":"AustinCStone/bmforkupdate","repo_name":"bmforkupdate","language":"Python","stars":0,"forks":0,"open_issues":0,"pushed_at":"2025-05-09T04:50:16Z","description":""},
    {"org_or_user":"AustinCStone","full_name":"AustinCStone/bitmind-fork","repo_name":"bitmind-fork","language":"","stars":0,"forks":0,"open_issues":0,"pushed_at":"2025-01-09T06:16:51Z","description":"forked on jan 8 2025"},
    {"org_or_user":"AustinCStone","full_name":"AustinCStone/RealTimeRayTracingFractalWorld","repo_name":"RealTimeRayTracingFractalWorld","language":"C++","stars":0,"forks":0,"open_issues":0,"pushed_at":"2015-05-11T01:58:57Z","description":"Real time ray tracing of fractal world"},
]
repos.extend(inline_repos)
print(f"Total repos: {len(repos)}")

# ── Build increment + repo inserts ────────────────────────────────────────────
inc_inserts = []
repo_inserts = []

for i, repo in enumerate(repos, start=1):
    trit, color, gf3_name = gf3(i)
    snap_hash = hashlib.sha256(repo["full_name"].encode()).hexdigest()[:12]
    inc_inserts.append(
        f"INSERT INTO world_increments VALUES ({i}, now(), {trit}, "
        f"{esc(color)}, {esc(gf3_name)}, 'github_repo', "
        f"{esc(repo['org_or_user'])}, 'repo_snapshot', "
        f"{esc(repo['repo_name'])}, {esc(repo['org_or_user'])}, {esc(snap_hash)});"
    )
    repo_inserts.append(
        f"INSERT INTO repo_snapshots VALUES ({i}, now(), {i}, "
        f"{esc(repo['org_or_user'])}, {esc(repo['repo_name'])}, "
        f"{esc(repo['full_name'])}, {esc(repo['language'])}, "
        f"{repo['stars']}, {repo['forks']}, {repo['open_issues']}, "
        f"{esc(repo['pushed_at'])}, {esc(repo['description'][:200])});"
    )

# ── Aptos snapshots (balances null - accounts use FA module, not legacy CoinStore) ──
aptos_addrs = {
    "alice": "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b",
    "bob":   "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d",
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
aptos_inserts = [
    f"INSERT INTO aptos_snapshots VALUES (now(), {esc(name)}, {esc(addr)}, NULL);"
    for name, addr in aptos_addrs.items()
]

# ── Multisig probes (all returned sigs_required=2) ─────────────────────────────
multisig_data = [
    ("A-B", "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2, True),
    ("A-G", "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2, True),
    ("Y-Z", "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2, True),
    ("S-T", "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2, True),
    ("V-W", "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2, True),
]
multisig_inserts = [
    f"INSERT INTO multisig_probes VALUES (now(), {esc(p)}, {esc(a)}, {s}, {str(h).upper()});"
    for p, a, s, h in multisig_data
]

# ── Execute all inserts ────────────────────────────────────────────────────────
all_sql = "\n".join(inc_inserts + repo_inserts + aptos_inserts + multisig_inserts)
run_sql(all_sql)
print("Data inserted.")

# ── Verify ────────────────────────────────────────────────────────────────────
verify = run_sql("""
SELECT 'world_increments' AS tbl, COUNT(*) AS n FROM world_increments
UNION ALL SELECT 'repo_snapshots', COUNT(*) FROM repo_snapshots
UNION ALL SELECT 'aptos_snapshots', COUNT(*) FROM aptos_snapshots
UNION ALL SELECT 'multisig_probes', COUNT(*) FROM multisig_probes
UNION ALL SELECT 'mnx_snapshots', COUNT(*) FROM mnx_snapshots;
""")
print("Table counts:\n", verify)

# ── GF(3) distribution ────────────────────────────────────────────────────────
gf3_dist = run_sql("SELECT gf3_name, gf3_color, COUNT(*) AS n FROM world_increments GROUP BY 1,2 ORDER BY 1;")
print("GF(3) distribution:\n", gf3_dist)
