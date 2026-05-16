#!/usr/bin/env python3
"""Populate world-increments DuckDB with GitHub social graph sweep + Aptos/multisig snapshot."""
import json, hashlib, duckdb
from datetime import datetime

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"

PLURIGRID_FILE = "/root/.claude/projects/-home-user-gorj/a7c53e46-8247-4925-980c-291d61525784/tool-results/mcp-github-search_repositories-1778936913213.txt"
KUBEFLOW_FILE  = "/root/.claude/projects/-home-user-gorj/a7c53e46-8247-4925-980c-291d61525784/tool-results/mcp-github-search_repositories-1778936911613.txt"
BMORPHISM_FILE = "/root/.claude/projects/-home-user-gorj/a7c53e46-8247-4925-980c-291d61525784/tool-results/mcp-github-search_repositories-1778936934381.txt"
ZUBYUL_FILE    = "/root/.claude/projects/-home-user-gorj/a7c53e46-8247-4925-980c-291d61525784/tool-results/mcp-github-search_repositories-1778936933282.txt"

def gf3(id_val):
    t = id_val % 3
    if t == 0: return (0, "#d3869b", "ERGODIC")
    if t == 1: return (1, "#b8bb26", "PLUS")
    return (-1, "#cc241d", "MINUS")

def snap_hash(src, name, pushed):
    return hashlib.sha256(f"{src}/{name}/{pushed}".encode()).hexdigest()[:16]

def load_json_repos(path):
    with open(path) as f:
        data = json.load(f)
    return data.get("items", [])

def repo_tuple(r):
    return dict(
        name=r.get("name",""),
        full_name=r.get("full_name",""),
        language=r.get("language") or "",
        stars=r.get("stargazers_count",0),
        forks=r.get("forks_count",0),
        issues=r.get("open_issues_count",0),
        pushed=r.get("pushed_at",""),
        desc=(r.get("description") or "")[:200],
    )

# ---- hardcoded data for social-graph users ----
TEGLON = [
    dict(name="mathpix-gem", full_name="TeglonLabs/mathpix-gem", language="Ruby", stars=2, forks=0, issues=11, pushed="2026-01-01T12:13:13Z", desc="Transform mathematical images to LaTeX, chemistry structures to SMILES"),
    dict(name="monad-mcp-server", full_name="TeglonLabs/monad-mcp-server", language="JavaScript", stars=0, forks=0, issues=0, pushed="2025-05-14T11:36:14Z", desc="Monad MCP Server"),
    dict(name="topoi", full_name="TeglonLabs/topoi", language="Python", stars=0, forks=0, issues=1, pushed="2025-01-24T04:49:26Z", desc=""),
    dict(name="coin-flip-mcp", full_name="TeglonLabs/coin-flip-mcp", language="JavaScript", stars=0, forks=2, issues=1, pushed="2025-09-21T08:57:27Z", desc="MCP server for flipping coins with varying degrees of randomness"),
]

MIGALKIN = [
    dict(name="NodePiece", full_name="migalkin/NodePiece", language="Python", stars=144, forks=21, issues=0, pushed="2026-05-07T05:40:02Z", desc="Compositional and Parameter-Efficient Representations for Large Knowledge Graphs (ICLR'22)"),
    dict(name="StarE", full_name="migalkin/StarE", language="Python", stars=89, forks=16, issues=1, pushed="2026-04-16T14:12:45Z", desc="EMNLP 2020: Message Passing for Hyper-Relational Knowledge Graphs"),
    dict(name="kgcourse2021", full_name="migalkin/kgcourse2021", language="HTML", stars=25, forks=9, issues=0, pushed="2026-02-16T05:16:08Z", desc="Материалы к курсу по Knowledge Graphs"),
    dict(name="NBFNet_mlx", full_name="migalkin/NBFNet_mlx", language="Python", stars=10, forks=1, issues=1, pushed="2026-03-11T01:31:21Z", desc="Neural Bellman-Ford networks implemented in MLX for Apple Silicon"),
    dict(name="RWL", full_name="migalkin/RWL", language="Python", stars=7, forks=1, issues=0, pushed="2025-02-10T14:12:14Z", desc="Weisfeiler and Leman Go Relational (LOG 2022)"),
    dict(name="rambo", full_name="migalkin/rambo", language="Rust", stars=3, forks=0, issues=1, pushed="2023-02-28T16:37:22Z", desc=""),
    dict(name="SMJoin-experiments", full_name="migalkin/SMJoin-experiments", language="R", stars=1, forks=0, issues=0, pushed="2020-03-04T15:56:23Z", desc="ISWC 2017 SMJoin results"),
    dict(name="migalkin.github.io", full_name="migalkin/migalkin.github.io", language="JavaScript", stars=0, forks=0, issues=0, pushed="2025-05-20T23:58:08Z", desc="Github Pages template for academic personal websites"),
    dict(name="ciss2_project", full_name="migalkin/ciss2_project", language="Jupyter Notebook", stars=0, forks=0, issues=6, pushed="2019-06-28T23:14:33Z", desc=""),
    dict(name="SQuAD-es-mt", full_name="migalkin/SQuAD-es-mt", language="", stars=0, forks=1, issues=0, pushed="2020-07-14T17:18:37Z", desc="Spanish version of SQuAD 1.1 and 2.0 obtained via machine translation"),
    dict(name="netquery_rdf", full_name="migalkin/netquery_rdf", language="Python", stars=0, forks=0, issues=0, pushed="2019-06-01T12:49:18Z", desc="NIPS 2018 paper fork for RDF"),
    dict(name="edbt-experiments", full_name="migalkin/edbt-experiments", language="", stars=0, forks=0, issues=0, pushed="2017-11-20T10:27:28Z", desc=""),
    dict(name="ekgs_clustering", full_name="migalkin/ekgs_clustering", language="Python", stars=0, forks=0, issues=0, pushed="2016-08-28T16:25:19Z", desc=""),
    dict(name="r_energyConsumption", full_name="migalkin/r_energyConsumption", language="R", stars=0, forks=0, issues=0, pushed="2016-05-12T21:00:17Z", desc=""),
    dict(name="ontologies", full_name="migalkin/ontologies", language="Web Ontology Language", stars=0, forks=0, issues=0, pushed="2015-12-06T13:49:53Z", desc=""),
    dict(name="Tables_Provider", full_name="migalkin/Tables_Provider", language="Java", stars=0, forks=0, issues=0, pushed="2015-03-20T00:17:36Z", desc=""),
    dict(name="datasciencecoursera", full_name="migalkin/datasciencecoursera", language="", stars=0, forks=0, issues=0, pushed="2015-02-12T23:57:16Z", desc="The repo for the Coursera Data Science course"),
    dict(name="InformationWorkbenchTestSrc", full_name="migalkin/InformationWorkbenchTestSrc", language="Java", stars=0, forks=0, issues=0, pushed="2014-10-15T21:42:40Z", desc=""),
    dict(name="LinkedData", full_name="migalkin/LinkedData", language="", stars=0, forks=0, issues=0, pushed="2014-10-15T21:42:40Z", desc="Information Workbench + Linked Open Data"),
]

DJEDAMSKI = [
    dict(name="kaggle_ncaa18", full_name="DJedamski/kaggle_ncaa18", language="Jupyter Notebook", stars=0, forks=0, issues=0, pushed="2018-02-26T16:33:24Z", desc="Code for NCAA March Madness competition (2018)"),
    dict(name="Project_Euler", full_name="DJedamski/Project_Euler", language="", stars=0, forks=0, issues=0, pushed="2015-09-05T17:13:32Z", desc=""),
    dict(name="EDA", full_name="DJedamski/EDA", language="R", stars=0, forks=0, issues=0, pushed="2014-11-09T17:00:39Z", desc="Coursera Project"),
    dict(name="Kaggle", full_name="DJedamski/Kaggle", language="", stars=1, forks=0, issues=0, pushed="2023-04-21T01:42:35Z", desc=""),
    dict(name="Getting-and-Cleaning-Data", full_name="DJedamski/Getting-and-Cleaning-Data", language="R", stars=1, forks=0, issues=0, pushed="2023-04-21T01:42:34Z", desc="Coursera Project"),
    dict(name="School", full_name="DJedamski/School", language="R", stars=1, forks=1, issues=0, pushed="2023-04-21T01:42:33Z", desc="A couple small projects from grad school"),
]

WASITA = [
    dict(name="wasita.github.io", full_name="wasita/wasita.github.io", language="Svelte", stars=1, forks=0, issues=8, pushed="2026-05-14T02:10:55Z", desc="personal website"),
    dict(name="wm-cv", full_name="wasita/wm-cv", language="Svelte", stars=0, forks=0, issues=0, pushed="2026-05-13T05:29:08Z", desc="Academic CV written as a single page web app (Svelte + Tailwind)"),
    dict(name="vocoder", full_name="wasita/vocoder", language="JavaScript", stars=0, forks=0, issues=0, pushed="2026-05-06T05:14:03Z", desc=""),
    dict(name="ch3-lib", full_name="wasita/ch3-lib", language="Typst", stars=0, forks=0, issues=0, pushed="2026-04-12T04:03:22Z", desc=""),
    dict(name="magic-garden", full_name="wasita/magic-garden", language="Python", stars=2, forks=1, issues=1, pushed="2026-04-22T21:16:43Z", desc="a bot for the magic garden discord activity game"),
    dict(name="proj-template", full_name="wasita/proj-template", language="", stars=0, forks=0, issues=0, pushed="2026-01-09T20:55:46Z", desc=""),
    dict(name="food-diary", full_name="wasita/food-diary", language="Svelte", stars=0, forks=0, issues=0, pushed="2025-12-13T01:06:43Z", desc=""),
    dict(name="send2kobo", full_name="wasita/send2kobo", language="TypeScript", stars=0, forks=0, issues=0, pushed="2025-12-12T19:09:16Z", desc="Website for sending books to your kobo e-reader"),
    dict(name="d60-keeb", full_name="wasita/d60-keeb", language="", stars=0, forks=0, issues=0, pushed="2024-08-26T00:46:25Z", desc=""),
    dict(name="wins-search", full_name="wasita/wins-search", language="CSS", stars=1, forks=0, issues=0, pushed="2023-06-03T19:01:11Z", desc="Women in Network Science (WiNS) member list website"),
    dict(name="honeycomb-demo", full_name="wasita/honeycomb-demo", language="JavaScript", stars=0, forks=0, issues=0, pushed="2021-12-07T21:38:28Z", desc=""),
]

KRISTINEZHENG = [
    dict(name="kristinezheng.github.io", full_name="kristinezheng/kristinezheng.github.io", language="HTML", stars=0, forks=0, issues=0, pushed="2026-05-14T22:29:01Z", desc=""),
    dict(name="Portfolio", full_name="kristinezheng/Portfolio", language="", stars=0, forks=0, issues=0, pushed="2025-02-12T00:00:45Z", desc="July 2021"),
    dict(name="lookit-jenga", full_name="kristinezheng/lookit-jenga", language="Jupyter Notebook", stars=0, forks=0, issues=0, pushed="2024-05-16T18:29:05Z", desc="Lookit study for 9.85"),
    dict(name="auditory-illusion", full_name="kristinezheng/auditory-illusion", language="CSS", stars=0, forks=0, issues=0, pushed="2022-03-07T02:57:44Z", desc="9.35 spring 2022 auditory illusion"),
    dict(name="graph_example", full_name="kristinezheng/graph_example", language="Python", stars=0, forks=0, issues=0, pushed="2021-10-08T07:29:53Z", desc=""),
    dict(name="Green-Machine", full_name="kristinezheng/Green-Machine", language="Python", stars=0, forks=0, issues=0, pushed="2021-09-19T05:33:04Z", desc="HackMIT 2021: Sustainability Track"),
]

M1SHAAA = [
    dict(name="M1shaaa", full_name="M1shaaa/M1shaaa", language="", stars=0, forks=0, issues=0, pushed="2026-02-04T19:32:04Z", desc="Config files for my GitHub profile."),
    dict(name="lab-bookshelf-", full_name="M1shaaa/lab-bookshelf-", language="TypeScript", stars=0, forks=0, issues=0, pushed="2024-12-31T05:11:18Z", desc=""),
    dict(name="rosie-s-study-3-lookit-project", full_name="M1shaaa/rosie-s-study-3-lookit-project", language="", stars=0, forks=0, issues=0, pushed="2024-11-04T22:15:39Z", desc=""),
    dict(name="Python-Lookit-Uploads", full_name="M1shaaa/Python-Lookit-Uploads", language="Python", stars=0, forks=0, issues=0, pushed="2024-02-15T22:59:37Z", desc="random projects"),
    dict(name="Classes", full_name="M1shaaa/Classes", language="", stars=0, forks=0, issues=0, pushed="2023-12-06T18:20:27Z", desc=""),
    dict(name="Yale-Work", full_name="M1shaaa/Yale-Work", language="HTML", stars=0, forks=0, issues=0, pushed="2023-12-06T18:33:14Z", desc=""),
    dict(name="MNIST-Classifier", full_name="M1shaaa/MNIST-Classifier", language="", stars=0, forks=0, issues=0, pushed="2023-11-28T06:10:47Z", desc=""),
    dict(name="Lookit-Demo", full_name="M1shaaa/Lookit-Demo", language="", stars=0, forks=0, issues=0, pushed="2023-04-10T02:44:01Z", desc=""),
]

AUSTINCSTONE = [
    dict(name="EpsteinSearch", full_name="AustinCStone/EpsteinSearch", language="Python", stars=0, forks=0, issues=0, pushed="2026-02-11T01:10:57Z", desc=""),
    dict(name="bmforkupdate", full_name="AustinCStone/bmforkupdate", language="Python", stars=0, forks=0, issues=0, pushed="2025-05-09T04:50:16Z", desc=""),
    dict(name="bmfork", full_name="AustinCStone/bmfork", language="Python", stars=0, forks=0, issues=1, pushed="2025-05-09T04:18:54Z", desc=""),
    dict(name="bitmind-fork", full_name="AustinCStone/bitmind-fork", language="", stars=0, forks=0, issues=0, pushed="2025-01-09T06:16:51Z", desc="forked on jan 8 2025"),
    dict(name="testLogin", full_name="AustinCStone/testLogin", language="Python", stars=0, forks=0, issues=0, pushed="2023-02-13T20:52:27Z", desc=""),
    dict(name="austincstone.github.io", full_name="AustinCStone/austincstone.github.io", language="HTML", stars=0, forks=0, issues=0, pushed="2021-10-23T22:48:49Z", desc=""),
    dict(name="test", full_name="AustinCStone/test", language="", stars=0, forks=0, issues=0, pushed="2021-09-21T21:15:50Z", desc=""),
    dict(name="stonks", full_name="AustinCStone/stonks", language="Python", stars=0, forks=0, issues=0, pushed="2020-09-04T22:54:35Z", desc="Playing around with some option calculations."),
    dict(name="Z-order-curve", full_name="AustinCStone/Z-order-curve", language="Python", stars=0, forks=0, issues=0, pushed="2019-06-09T02:53:43Z", desc="Demo implementation of things related to space filling z-order curve"),
    dict(name="LensBuilder", full_name="AustinCStone/LensBuilder", language="Python", stars=0, forks=0, issues=0, pushed="2019-04-04T04:28:08Z", desc="WIP optimize for the surface of a focusing lens by casting rays"),
    dict(name="TFBirds", full_name="AustinCStone/TFBirds", language="Python", stars=0, forks=0, issues=0, pushed="2019-01-30T08:07:18Z", desc="Bird flocking simulator in TensorFlow."),
    dict(name="StructureFromMotion", full_name="AustinCStone/StructureFromMotion", language="Python", stars=1, forks=0, issues=0, pushed="2019-04-26T19:43:12Z", desc="Recover 3D geometry from videos with unknown camera calibration"),
    dict(name="OptimalControl", full_name="AustinCStone/OptimalControl", language="Python", stars=0, forks=0, issues=0, pushed="2018-02-03T08:08:51Z", desc="Practicing some concepts from control theory."),
    dict(name="LearningCuda", full_name="AustinCStone/LearningCuda", language="C", stars=0, forks=0, issues=0, pushed="2017-11-05T20:31:07Z", desc="Me working through CUDA by example"),
    dict(name="TextGAN", full_name="AustinCStone/TextGAN", language="Python", stars=92, forks=30, issues=5, pushed="2025-03-03T13:26:32Z", desc="A generative adversarial network for text generation, written in TensorFlow."),
    dict(name="StereoVisionMRF", full_name="AustinCStone/StereoVisionMRF", language="Python", stars=11, forks=4, issues=0, pushed="2026-04-01T07:39:41Z", desc="Using a MRF with loopy belief propagation to infer depth from stereo images."),
    dict(name="SpectralClustering", full_name="AustinCStone/SpectralClustering", language="Python", stars=3, forks=2, issues=0, pushed="2021-04-16T08:46:36Z", desc="Implementing spectral clustering as part of a homework assignment"),
    dict(name="statsHw2", full_name="AustinCStone/statsHw2", language="Python", stars=0, forks=0, issues=0, pushed="2015-09-28T00:50:31Z", desc="Simple linear regression and model selection stuff"),
    dict(name="StatsModelingHw1", full_name="AustinCStone/StatsModelingHw1", language="Python", stars=0, forks=0, issues=0, pushed="2015-09-19T04:13:53Z", desc="My first homework for statistical modeling"),
    dict(name="ConvNet", full_name="AustinCStone/ConvNet", language="Python", stars=0, forks=0, issues=0, pushed="2015-09-07T22:25:29Z", desc="A 'deep' convolutional neural network for classifying the MNIST database"),
]

# ---- source registry ----
SOURCES = [
    ("org",  "plurigrid",     PLURIGRID_FILE),
    ("org",  "kubeflow",      KUBEFLOW_FILE),
    ("org",  "TeglonLabs",    TEGLON),
    ("user", "bmorphism",     BMORPHISM_FILE),
    ("user", "zubyul",        ZUBYUL_FILE),
    ("user", "migalkin",      MIGALKIN),
    ("user", "DJedamski",     DJEDAMSKI),
    ("user", "wasita",        WASITA),
    ("user", "kristinezheng", KRISTINEZHENG),
    ("user", "M1shaaa",       M1SHAAA),
    ("user", "AustinCStone",  AUSTINCSTONE),
]

con = duckdb.connect(DB_PATH)
con.execute("""CREATE TABLE IF NOT EXISTS world_increments (
  id INTEGER, timestamp TIMESTAMP DEFAULT now(), gf3_trit INTEGER,
  gf3_color VARCHAR, gf3_name VARCHAR, source_type VARCHAR,
  source_name VARCHAR, event_type VARCHAR, repo_name VARCHAR,
  actor VARCHAR, snapshot_hash VARCHAR)""")
con.execute("""CREATE TABLE IF NOT EXISTS repo_snapshots (
  id INTEGER, timestamp TIMESTAMP DEFAULT now(), increment_id INTEGER,
  org_or_user VARCHAR, repo_name VARCHAR, full_name VARCHAR,
  language VARCHAR, stars INTEGER, forks INTEGER, open_issues INTEGER,
  pushed_at VARCHAR, description VARCHAR)""")
con.execute("""CREATE TABLE IF NOT EXISTS aptos_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  world VARCHAR, address VARCHAR, balance_apt DOUBLE)""")
con.execute("""CREATE TABLE IF NOT EXISTS multisig_probes (
  timestamp TIMESTAMP DEFAULT now(),
  pair VARCHAR, address VARCHAR, sigs_required INTEGER, healthy BOOLEAN)""")
con.execute("""CREATE TABLE IF NOT EXISTS mnx_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  ticker VARCHAR, name VARCHAR, category VARCHAR,
  price DOUBLE, change_pct DOUBLE)""")
con.execute("CREATE SEQUENCE IF NOT EXISTS increment_seq START 1")
con.execute("CREATE SEQUENCE IF NOT EXISTS repo_seq START 1")

inc_id = 0
repo_id = 0

for src_type, src_name, data_or_file in SOURCES:
    if isinstance(data_or_file, str):
        repos = [repo_tuple(r) for r in load_json_repos(data_or_file)]
    else:
        repos = data_or_file

    for r in repos:
        inc_id += 1
        trit, color, gname = gf3(inc_id)
        h = snap_hash(src_name, r["name"], r.get("pushed",""))
        con.execute(
            "INSERT INTO world_increments VALUES (?,now(),?,?,?,?,?,?,?,?,?)",
            [inc_id, trit, color, gname, src_type, src_name,
             "repo_snapshot", r["name"], src_name, h])
        repo_id += 1
        con.execute(
            "INSERT INTO repo_snapshots VALUES (?,now(),?,?,?,?,?,?,?,?,?,?)",
            [repo_id, inc_id, src_name, r["name"], r.get("full_name",""),
             r.get("language",""), r.get("stars",0), r.get("forks",0),
             r.get("issues",0), r.get("pushed",""), r.get("desc","")])

print(f"Inserted {inc_id} world_increments / {repo_id} repo_snapshots")

# ---- Aptos snapshots ----
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
    con.execute("INSERT INTO aptos_snapshots VALUES (now(),?,?,?)", [world, addr, bal])
print(f"Inserted {len(aptos_data)} aptos_snapshots")

# ---- Multisig probes ----
multisig_data = [
    ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2,True),
    ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2,True),
    ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2,True),
    ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2,True),
    ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2,True),
]
for pair, addr, sigs, healthy in multisig_data:
    con.execute("INSERT INTO multisig_probes VALUES (now(),?,?,?,?)", [pair, addr, sigs, healthy])
print(f"Inserted {len(multisig_data)} multisig_probes")

# MNX: SPA (Next.js), no REST API endpoint accessible — noted as unavailable
print("MNX Markets: SPA — no market data rows inserted (endpoint not accessible)")

con.close()
print("Done.")
