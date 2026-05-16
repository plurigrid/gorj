#!/usr/bin/env python3
"""Build DuckDB ducklake from GitHub and Aptos snapshot data."""
import duckdb
import json
import hashlib
import sys
from datetime import datetime

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
con = duckdb.connect(DB_PATH)

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

con.execute("""
CREATE SEQUENCE IF NOT EXISTS increment_seq START 1""")

con.execute("""
CREATE SEQUENCE IF NOT EXISTS repo_seq START 1""")

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

print("Tables created.")

# GF3 color chain
def gf3_info(n):
    t = n % 3
    if t == 0:
        return (0, '#d3869b', 'ERGODIC')
    elif t == 1:
        return (1, '#b8bb26', 'PLUS')
    else:
        return (-1, '#cc241d', 'MINUS')

# Repo data collected inline (already-parsed sources)
repos = []

# TeglonLabs (4 repos)
teglon_data = [
    {"org": "TeglonLabs", "name": "topoi", "full_name": "TeglonLabs/topoi", "lang": "Python", "stars": 0, "forks": 0, "issues": 1, "pushed": "2025-01-24T04:49:26Z", "desc": ""},
    {"org": "TeglonLabs", "name": "mathpix-gem", "full_name": "TeglonLabs/mathpix-gem", "lang": "Ruby", "stars": 2, "forks": 0, "issues": 11, "pushed": "2026-01-01T12:13:13Z", "desc": "Transform mathematical images to LaTeX"},
    {"org": "TeglonLabs", "name": "monad-mcp-server", "full_name": "TeglonLabs/monad-mcp-server", "lang": None, "stars": 0, "forks": 0, "issues": 0, "pushed": "2025-05-14T11:36:14Z", "desc": "Monad MCP Server"},
    {"org": "TeglonLabs", "name": "coin-flip-mcp", "full_name": "TeglonLabs/coin-flip-mcp", "lang": "JavaScript", "stars": 0, "forks": 2, "issues": 1, "pushed": "2025-09-21T08:57:27Z", "desc": "MCP server for flipping coins"},
]
for r in teglon_data:
    repos.append(("TeglonLabs", r["org"], r["name"], r["full_name"], r["lang"] or "", r["stars"], r["forks"], r["issues"], r["pushed"], r["desc"]))

# migalkin (19 repos)
migalkin_data = [
    {"name": "NodePiece", "full_name": "migalkin/NodePiece", "lang": "Python", "stars": 144, "forks": 21, "issues": 0, "pushed": "2021-06-14", "desc": "Compositional and Parameter-Efficient Representations for Large Knowledge Graphs"},
    {"name": "StarE", "full_name": "migalkin/StarE", "lang": "Python", "stars": 89, "forks": 16, "issues": 1, "pushed": "2020-09-17", "desc": "EMNLP 2020: Message Passing for Hyper-Relational Knowledge Graphs"},
    {"name": "NBFNet_mlx", "full_name": "migalkin/NBFNet_mlx", "lang": "Python", "stars": 10, "forks": 1, "issues": 1, "pushed": "2024-03-01", "desc": "Neural Bellman-Ford networks implemented in MLX for Apple Silicon"},
    {"name": "kgcourse2021", "full_name": "migalkin/kgcourse2021", "lang": "HTML", "stars": 25, "forks": 9, "issues": 0, "pushed": "2020-09-01", "desc": "Knowledge Graphs course materials"},
    {"name": "RWL", "full_name": "migalkin/RWL", "lang": "Python", "stars": 7, "forks": 1, "issues": 0, "pushed": "2022-11-30", "desc": "Weisfeiler and Leman Go Relational"},
    {"name": "rambo", "full_name": "migalkin/rambo", "lang": "Rust", "stars": 3, "forks": 0, "issues": 1, "pushed": "2019-08-13", "desc": ""},
    {"name": "migalkin.github.io", "full_name": "migalkin/migalkin.github.io", "lang": "JavaScript", "stars": 0, "forks": 0, "issues": 0, "pushed": "2019-07-02", "desc": "Github Pages template"},
    {"name": "SMJoin-experiments", "full_name": "migalkin/SMJoin-experiments", "lang": "R", "stars": 1, "forks": 0, "issues": 0, "pushed": "2017-05-11", "desc": "ISWC 2017 SMJoin results"},
]
for r in migalkin_data:
    repos.append(("migalkin", "migalkin", r["name"], r["full_name"], r["lang"] or "", r["stars"], r["forks"], r["issues"], r["pushed"], r["desc"]))

# wasita (11 repos)
wasita_data = [
    {"name": "wasita.github.io", "full_name": "wasita/wasita.github.io", "lang": "Svelte", "stars": 1, "forks": 0, "issues": 8, "pushed": "2026-05-14", "desc": "personal website"},
    {"name": "magic-garden", "full_name": "wasita/magic-garden", "lang": "Python", "stars": 2, "forks": 1, "issues": 1, "pushed": "2026-04-22", "desc": "a bot for magic garden discord game"},
    {"name": "wm-cv", "full_name": "wasita/wm-cv", "lang": "Svelte", "stars": 0, "forks": 0, "issues": 0, "pushed": "2026-05-13", "desc": "Academic CV"},
    {"name": "vocoder", "full_name": "wasita/vocoder", "lang": "JavaScript", "stars": 0, "forks": 0, "issues": 0, "pushed": "2026-05-06", "desc": ""},
    {"name": "wins-search", "full_name": "wasita/wins-search", "lang": "CSS", "stars": 1, "forks": 0, "issues": 0, "pushed": "2022-09-26", "desc": "Women in Network Science member list website"},
    {"name": "send2kobo", "full_name": "wasita/send2kobo", "lang": "TypeScript", "stars": 0, "forks": 0, "issues": 0, "pushed": "2025-12-10", "desc": "Website for sending books to kobo"},
    {"name": "ch3-lib", "full_name": "wasita/ch3-lib", "lang": "Typst", "stars": 0, "forks": 0, "issues": 0, "pushed": "2026-04-12", "desc": ""},
]
for r in wasita_data:
    repos.append(("wasita", "wasita", r["name"], r["full_name"], r["lang"] or "", r["stars"], r["forks"], r["issues"], r["pushed"], r["desc"]))

# AustinCStone (top repos)
austin_data = [
    {"name": "TextGAN", "full_name": "AustinCStone/TextGAN", "lang": "Python", "stars": 92, "forks": 30, "issues": 5, "pushed": "2016-09-19", "desc": "A generative adversarial network for text generation"},
    {"name": "StereoVisionMRF", "full_name": "AustinCStone/StereoVisionMRF", "lang": "Python", "stars": 11, "forks": 4, "issues": 0, "pushed": "2016-01-10", "desc": "Using a MRF with loopy belief propagation"},
    {"name": "SpectralClustering", "full_name": "AustinCStone/SpectralClustering", "lang": "Python", "stars": 3, "forks": 2, "issues": 0, "pushed": "2015-11-09", "desc": "Implementing spectral clustering"},
    {"name": "bmfork", "full_name": "AustinCStone/bmfork", "lang": "Python", "stars": 0, "forks": 0, "issues": 1, "pushed": "2025-05-09", "desc": ""},
    {"name": "EpsteinSearch", "full_name": "AustinCStone/EpsteinSearch", "lang": "Python", "stars": 0, "forks": 0, "issues": 0, "pushed": "2026-02-08", "desc": ""},
    {"name": "TFBirds", "full_name": "AustinCStone/TFBirds", "lang": "Python", "stars": 0, "forks": 0, "issues": 0, "pushed": "2019-01-20", "desc": "Bird flocking simulator in TensorFlow"},
]
for r in austin_data:
    repos.append(("AustinCStone", "AustinCStone", r["name"], r["full_name"], r["lang"] or "", r["stars"], r["forks"], r["issues"], r["pushed"], r["desc"]))

# DJedamski (6 repos)
djed_data = [
    {"name": "kaggle_ncaa18", "full_name": "DJedamski/kaggle_ncaa18", "lang": "Jupyter Notebook", "stars": 0, "forks": 0, "issues": 0, "pushed": "2018-02-26", "desc": "NCAA March Madness competition"},
    {"name": "Getting-and-Cleaning-Data", "full_name": "DJedamski/Getting-and-Cleaning-Data", "lang": "R", "stars": 1, "forks": 0, "issues": 0, "pushed": "2014-10-26", "desc": "Coursera Project"},
    {"name": "Kaggle", "full_name": "DJedamski/Kaggle", "lang": None, "stars": 1, "forks": 0, "issues": 0, "pushed": "2014-11-03", "desc": ""},
    {"name": "School", "full_name": "DJedamski/School", "lang": "R", "stars": 1, "forks": 1, "issues": 0, "pushed": "2014-10-09", "desc": "Projects from grad school"},
]
for r in djed_data:
    repos.append(("DJedamski", "DJedamski", r["name"], r["full_name"], r["lang"] or "", r["stars"], r["forks"], r["issues"], r["pushed"], r["desc"]))

# kristinezheng (6 repos)
kzheng_data = [
    {"name": "kristinezheng.github.io", "full_name": "kristinezheng/kristinezheng.github.io", "lang": "HTML", "stars": 0, "forks": 0, "issues": 0, "pushed": "2022-07-26", "desc": ""},
    {"name": "lookit-jenga", "full_name": "kristinezheng/lookit-jenga", "lang": "Jupyter Notebook", "stars": 0, "forks": 0, "issues": 0, "pushed": "2023-10-31", "desc": "Lookit study for 9.85"},
    {"name": "Portfolio", "full_name": "kristinezheng/Portfolio", "lang": None, "stars": 0, "forks": 0, "issues": 0, "pushed": "2021-07-24", "desc": "July 2021"},
    {"name": "Green-Machine", "full_name": "kristinezheng/Green-Machine", "lang": "Python", "stars": 0, "forks": 0, "issues": 0, "pushed": "2021-09-19", "desc": "HackMIT 2021: Sustainability Track"},
]
for r in kzheng_data:
    repos.append(("kristinezheng", "kristinezheng", r["name"], r["full_name"], r["lang"] or "", r["stars"], r["forks"], r["issues"], r["pushed"], r["desc"]))

# M1shaaa (8 repos)
m1sha_data = [
    {"name": "lab-bookshelf-", "full_name": "M1shaaa/lab-bookshelf-", "lang": "TypeScript", "stars": 0, "forks": 0, "issues": 0, "pushed": "2024-12-31", "desc": ""},
    {"name": "M1shaaa", "full_name": "M1shaaa/M1shaaa", "lang": None, "stars": 0, "forks": 0, "issues": 0, "pushed": "2024-11-30", "desc": "Config files for GitHub profile"},
    {"name": "Python-Lookit-Uploads", "full_name": "M1shaaa/Python-Lookit-Uploads", "lang": "Python", "stars": 0, "forks": 0, "issues": 0, "pushed": "2024-02-15", "desc": "random projects"},
    {"name": "Yale-Work", "full_name": "M1shaaa/Yale-Work", "lang": "HTML", "stars": 0, "forks": 0, "issues": 0, "pushed": "2023-12-06", "desc": ""},
    {"name": "MNIST-Classifier", "full_name": "M1shaaa/MNIST-Classifier", "lang": None, "stars": 0, "forks": 0, "issues": 0, "pushed": "2023-11-28", "desc": ""},
]
for r in m1sha_data:
    repos.append(("M1shaaa", "M1shaaa", r["name"], r["full_name"], r["lang"] or "", r["stars"], r["forks"], r["issues"], r["pushed"], r["desc"]))

print(f"Inline repos collected: {len(repos)}")
# Save for later use
with open("/tmp/inline_repos.json", "w") as f:
    json.dump(repos, f)
print("Saved inline repos to /tmp/inline_repos.json")
con.close()
