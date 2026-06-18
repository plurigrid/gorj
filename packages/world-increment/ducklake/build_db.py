#!/usr/bin/env python3
"""Build world-increments DuckDB from GitHub sweep and Aptos snapshot data."""
import json, hashlib, duckdb
from datetime import datetime

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
con = duckdb.connect(DB)

# ---------- Schema ----------
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

# ---------- GF(3) helpers ----------
GF3 = [
    (0, '#d3869b', 'ERGODIC'),
    (1, '#b8bb26', 'PLUS'),
    (-1, '#cc241d', 'MINUS'),
]

def gf3(i):
    t = GF3[i % 3]
    return t[0], t[1], t[2]

# ---------- Load repo data from saved files ----------
TOOL_RESULTS = "/root/.claude/projects/-home-user-gorj/96f70894-d669-588d-8863-1b53a9f1092f/tool-results"

def load_search(fname, source_name):
    try:
        data = json.load(open(fname))
        return [(source_name, r.get('name',''), r.get('full_name',''),
                 r.get('language') or '', r.get('stargazers_count',0),
                 r.get('forks_count',0), r.get('open_issues_count',0),
                 r.get('pushed_at','') or '', (r.get('description') or '')[:200])
                for r in data.get('items',[])]
    except Exception as e:
        print(f"WARN loading {fname}: {e}")
        return []

# File map: source_name -> filename suffix
file_map = {
    'plurigrid':  'mcp-github-search_repositories-1781766246707.txt',
    'kubeflow':   'mcp-github-search_repositories-1781766244736.txt',
    'bmorphism':  'mcp-github-search_repositories-1781766247844.txt',
    'zubyul':     'mcp-github-search_repositories-1781766247051.txt',
}

all_repos = []
for src, fname in file_map.items():
    all_repos.extend(load_search(f"{TOOL_RESULTS}/{fname}", src))

# TeglonLabs repos (inline from search results)
teglon_repos = [
    ('TeglonLabs','jank-crane','TeglonLabs/jank-crane','C++',0,0,0,'2026-06-08T19:03:03Z','crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow'),
    ('TeglonLabs','mathpix-gem','TeglonLabs/mathpix-gem','Ruby',2,0,11,'2026-01-01T12:13:13Z','Transform mathematical images to LaTeX, chemistry structures to SMILES, and documents to markdown'),
    ('TeglonLabs','coin-flip-mcp','TeglonLabs/coin-flip-mcp','JavaScript',0,2,1,'2025-09-21T08:57:27Z','MCP server for flipping coins with varying degrees of randomness from random.org'),
    ('TeglonLabs','monad-mcp-server','TeglonLabs/monad-mcp-server','',0,0,0,'2025-05-14T11:36:14Z','Monad MCP Server'),
    ('TeglonLabs','topoi','TeglonLabs/topoi','Python',0,0,1,'2025-01-24T04:49:26Z',''),
]
all_repos.extend(teglon_repos)

# Social graph repos (inline from search results)
social_repos = [
    ('migalkin','kgcourse2021','migalkin/kgcourse2021','HTML',25,9,0,'2026-02-16T05:16:08Z','Материалы к курсу по Knowledge Graphs'),
    ('migalkin','NBFNet_mlx','migalkin/NBFNet_mlx','Python',10,1,1,'2026-03-11T01:31:21Z','Neural Bellman-Ford networks implemented in MLX for Apple Silicon'),
    ('migalkin','StarE','migalkin/StarE','Python',89,16,1,'2026-04-16T14:12:45Z','EMNLP 2020: Message Passing for Hyper-Relational Knowledge Graphs'),
    ('migalkin','NodePiece','migalkin/NodePiece','Python',144,21,0,'2026-05-07T05:40:02Z','Compositional and Parameter-Efficient Representations for Large Knowledge Graphs (ICLR22)'),
    ('migalkin','RWL','migalkin/RWL','Python',8,1,0,'2026-05-28T20:19:20Z','Weisfeiler and Leman Go Relational (LOG 2022)'),
    ('migalkin','rambo','migalkin/rambo','Rust',3,0,1,'2023-02-28T16:37:22Z',''),
    ('migalkin','migalkin.github.io','migalkin/migalkin.github.io','JavaScript',0,0,0,'2025-05-20T23:58:08Z','Github Pages template for academic personal websites'),
    ('DJedamski','kaggle_ncaa18','DJedamski/kaggle_ncaa18','Jupyter Notebook',0,0,0,'2018-02-26T16:33:24Z','Code for NCAA March Madness competition (2018)'),
    ('DJedamski','Kaggle','DJedamski/Kaggle','',1,0,0,'2023-04-21T01:42:35Z',''),
    ('DJedamski','Getting-and-Cleaning-Data','DJedamski/Getting-and-Cleaning-Data','R',1,0,0,'2023-04-21T01:42:34Z','Coursera Project'),
    ('DJedamski','School','DJedamski/School','R',1,1,0,'2023-04-21T01:42:33Z','A couple small projects from grad school'),
    ('DJedamski','EDA','DJedamski/EDA','R',0,0,0,'2014-11-09T17:00:39Z','Coursera Project'),
    ('DJedamski','Project_Euler','DJedamski/Project_Euler','',0,0,0,'2015-09-05T17:13:32Z',''),
    ('wasita','wasita.github.io','wasita/wasita.github.io','Svelte',1,0,8,'2026-06-15T20:14:23Z','personal website'),
    ('wasita','wm-cv','wasita/wm-cv','Svelte',0,0,0,'2026-05-13T05:29:08Z','Academic CV written as a single page web app'),
    ('wasita','vocoder','wasita/vocoder','JavaScript',0,0,0,'2026-05-06T05:14:03Z',''),
    ('wasita','send2kobo','wasita/send2kobo','TypeScript',1,0,0,'2026-05-19T02:59:26Z','Website for sending books to your kobo e-reader'),
    ('wasita','magic-garden','wasita/magic-garden','Python',2,1,1,'2026-04-22T21:16:43Z','a bot written for the magic garden discord activity game'),
    ('wasita','ch3-lib','wasita/ch3-lib','Typst',0,0,0,'2026-04-12T04:03:22Z',''),
    ('wasita','food-diary','wasita/food-diary','Svelte',0,0,0,'2025-12-13T01:06:43Z',''),
    ('wasita','d60-keeb','wasita/d60-keeb','',0,0,0,'2024-08-26T00:46:25Z',''),
    ('wasita','wins-search','wasita/wins-search','CSS',1,0,0,'2023-06-03T19:01:11Z','Women in Network Science (WiNS) member list website'),
    ('wasita','honeycomb-demo','wasita/honeycomb-demo','JavaScript',0,0,0,'2021-12-07T21:38:28Z',''),
    ('kristinezheng','kristinezheng.github.io','kristinezheng/kristinezheng.github.io','HTML',0,0,0,'2026-06-07T22:53:10Z',''),
    ('kristinezheng','lookit-jenga','kristinezheng/lookit-jenga','Jupyter Notebook',0,0,0,'2024-05-16T18:29:05Z','Lookit study for 9.85'),
    ('kristinezheng','auditory-illusion','kristinezheng/auditory-illusion','CSS',0,0,0,'2022-03-07T02:57:44Z','9.35 spring 2022 auditory illusion'),
    ('kristinezheng','graph_example','kristinezheng/graph_example','Python',0,0,0,'2021-10-08T07:29:53Z',''),
    ('kristinezheng','Green-Machine','kristinezheng/Green-Machine','Python',0,0,0,'2021-09-19T05:33:04Z','HackMIT 2021: Sustainability Track'),
    ('M1shaaa','M1shaaa','M1shaaa/M1shaaa','',0,0,0,'2026-02-04T19:32:04Z','Config files for my GitHub profile.'),
    ('M1shaaa','lab-bookshelf-','M1shaaa/lab-bookshelf-','TypeScript',0,0,0,'2024-12-31T05:11:18Z',''),
    ('M1shaaa','rosie-s-study-3-lookit-project','M1shaaa/rosie-s-study-3-lookit-project','',0,0,0,'2024-11-04T22:15:39Z',''),
    ('M1shaaa','Python-Lookit-Uploads','M1shaaa/Python-Lookit-Uploads','Python',0,0,0,'2024-02-15T22:59:37Z','random projects'),
    ('M1shaaa','Classes','M1shaaa/Classes','',0,0,0,'2023-12-06T18:20:27Z',''),
    ('M1shaaa','Yale-Work','M1shaaa/Yale-Work','HTML',0,0,0,'2023-12-06T18:33:14Z',''),
    ('M1shaaa','MNIST-Classifier','M1shaaa/MNIST-Classifier','',0,0,0,'2023-11-28T06:10:47Z',''),
    ('M1shaaa','Lookit-Demo','M1shaaa/Lookit-Demo','',0,0,0,'2023-04-10T02:44:01Z',''),
    ('AustinCStone','EpsteinSearch','AustinCStone/EpsteinSearch','Python',0,0,0,'2026-02-11T01:10:57Z',''),
    ('AustinCStone','bmforkupdate','AustinCStone/bmforkupdate','Python',0,0,0,'2025-05-09T04:50:16Z',''),
    ('AustinCStone','TextGAN','AustinCStone/TextGAN','Python',92,30,5,'2025-03-03T13:26:32Z','A generative adversarial network for text generation, written in TensorFlow.'),
    ('AustinCStone','StereoVisionMRF','AustinCStone/StereoVisionMRF','Python',11,4,0,'2026-04-01T07:39:41Z','Using a MRF with loopy belief propagation to infer depth from stereo images.'),
    ('AustinCStone','StructureFromMotion','AustinCStone/StructureFromMotion','Python',1,0,0,'2019-04-26T19:43:12Z','Recover 3D geometry from videos with unknown camera calibration'),
    ('AustinCStone','SpectralClustering','AustinCStone/SpectralClustering','Python',3,2,0,'2021-04-16T08:46:36Z','Implementing spectral clustering'),
    ('AustinCStone','logisticRegressionHaskell','AustinCStone/logisticRegressionHaskell','Haskell',1,0,0,'2018-02-02T13:34:28Z','Logistic regression done in Haskell.'),
    ('AustinCStone','RealTimeRayTracingFractalWorld','AustinCStone/RealTimeRayTracingFractalWorld','C++',0,0,0,'2015-05-11T01:58:57Z','Real time ray tracing of a fractal world'),
    ('AustinCStone','TFBirds','AustinCStone/TFBirds','Python',0,0,0,'2019-01-30T08:07:22Z','Bird flocking simulator in TensorFlow.'),
]
all_repos.extend(social_repos)

print(f"Total repos to insert: {len(all_repos)}")

# ---------- Insert world_increments + repo_snapshots ----------
now = datetime.utcnow().isoformat()
inc_id = 1
rep_id = 1

for i, (src, name, full_name, lang, stars, forks, issues, pushed_at, desc) in enumerate(all_repos):
    trit, color, gf3_name = gf3(inc_id)
    snap_hash = hashlib.sha256(f"{full_name}{pushed_at}".encode()).hexdigest()[:16]
    con.execute("""
        INSERT INTO world_increments VALUES (?, ?, ?, ?, ?, 'github_repo', ?, 'push', ?, ?, ?)
    """, [inc_id, now, trit, color, gf3_name, src, name, src, snap_hash])
    con.execute("""
        INSERT INTO repo_snapshots VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [rep_id, now, inc_id, src, name, full_name, lang, stars, forks, issues, pushed_at, desc[:200]])
    inc_id += 1
    rep_id += 1

print(f"Inserted {inc_id-1} world_increments and repo_snapshots")

# ---------- Aptos snapshots ----------
aptos_data = [
    ("alice","0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b",0.0),
    ("bob",  "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d",0.0),
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
for world, addr, bal in aptos_data:
    con.execute("INSERT INTO aptos_snapshots VALUES (?, ?, ?, ?)", [now, world, addr, bal])
print(f"Inserted {len(aptos_data)} aptos_snapshots")

# ---------- Multisig probes ----------
multisig_data = [
    ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2,True),
    ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2,True),
    ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2,True),
    ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2,True),
    ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2,True),
]
for pair, addr, sigs, healthy in multisig_data:
    con.execute("INSERT INTO multisig_probes VALUES (?, ?, ?, ?, ?)", [now, pair, addr, sigs, healthy])
print(f"Inserted {len(multisig_data)} multisig_probes (all healthy)")

# ---------- MNX snapshot (unavailable) ----------
# testnet.mnx.fi requires Vercel authentication - no public data accessible
print("MNX: Vercel auth required, no data inserted")

# ---------- Summary queries ----------
print("\n=== Summary ===")
r = con.execute("SELECT COUNT(*) FROM world_increments").fetchone()
print(f"world_increments: {r[0]}")
r = con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()
print(f"repo_snapshots: {r[0]}")
r = con.execute("SELECT org_or_user, COUNT(*) as cnt FROM repo_snapshots GROUP BY org_or_user ORDER BY cnt DESC").fetchall()
print("repos by source:")
for row in r:
    print(f"  {row[0]}: {row[1]}")
r = con.execute("SELECT gf3_name, COUNT(*) FROM world_increments GROUP BY gf3_name ORDER BY gf3_name").fetchall()
print("GF3 distribution:")
for row in r:
    print(f"  {row[0]}: {row[1]}")

con.close()
print("\nDatabase built successfully.")
