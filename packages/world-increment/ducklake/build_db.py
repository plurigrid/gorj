#!/usr/bin/env python3
"""Build world-increments DuckDB from collected GitHub + Aptos data."""
import duckdb
import json
import hashlib
from datetime import datetime

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
con = duckdb.connect(DB_PATH)

# ── Schema ────────────────────────────────────────────────────────────────────
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

con.execute("CREATE SEQUENCE IF NOT EXISTS increment_seq START 1")
con.execute("CREATE SEQUENCE IF NOT EXISTS repo_seq START 1")

# ── GF(3) color chain ─────────────────────────────────────────────────────────
GF3 = [
    (0, "#d3869b", "ERGODIC"),
    (1, "#b8bb26", "PLUS"),
    (-1, "#cc241d", "MINUS"),
]

def gf3(id_):
    t = id_ % 3
    return GF3[t]

def snap_hash(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()[:16]

# ── Repo data ──────────────────────────────────────────────────────────────────
REPOS = []

# TeglonLabs (5 repos)
teglon_repos = [
    {"org_or_user": "TeglonLabs", "repo_name": "jank-crane", "full_name": "TeglonLabs/jank-crane",
     "language": "C++", "stars": 0, "forks": 0, "open_issues": 0,
     "pushed_at": "2026-06-08T19:03:03Z",
     "description": "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow"},
    {"org_or_user": "TeglonLabs", "repo_name": "mathpix-gem", "full_name": "TeglonLabs/mathpix-gem",
     "language": "Ruby", "stars": 2, "forks": 0, "open_issues": 11,
     "pushed_at": "2026-01-01T12:13:13Z",
     "description": "Transform mathematical images to LaTeX, chemistry structures to SMILES, and documents to markdown with security-first design."},
    {"org_or_user": "TeglonLabs", "repo_name": "coin-flip-mcp", "full_name": "TeglonLabs/coin-flip-mcp",
     "language": "JavaScript", "stars": 0, "forks": 2, "open_issues": 1,
     "pushed_at": "2025-09-21T08:57:27Z",
     "description": "MCP server for flipping coins with varying degrees of randomness from random.org"},
    {"org_or_user": "TeglonLabs", "repo_name": "monad-mcp-server", "full_name": "TeglonLabs/monad-mcp-server",
     "language": None, "stars": 0, "forks": 0, "open_issues": 0,
     "pushed_at": "2025-05-14T11:36:14Z", "description": "Monad MCP Server"},
    {"org_or_user": "TeglonLabs", "repo_name": "topoi", "full_name": "TeglonLabs/topoi",
     "language": "Python", "stars": 0, "forks": 0, "open_issues": 1,
     "pushed_at": "2025-01-24T04:49:26Z", "description": None},
]
REPOS.extend(teglon_repos)

# zubyul repos
zubyul_repos = [
    {"org_or_user": "zubyul", "repo_name": "voice-observatory", "full_name": "zubyul/voice-observatory", "language": "Python", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-24T05:56:17Z", "description": "Passive macOS TUI observing voice-download pathways."},
    {"org_or_user": "zubyul", "repo_name": "ghostel-emacs-worlds", "full_name": "zubyul/ghostel-emacs-worlds", "language": "GLSL", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-24T00:20:56Z", "description": "Ghostty config + ghostel family + alice/bob emacs-mods"},
    {"org_or_user": "zubyul", "repo_name": "nash-tui", "full_name": "zubyul/nash-tui", "language": "Rust", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-13T07:45:16Z", "description": "NASH token TUI: real-time candles, ticker, buy pressure gauge via GeckoTerminal OHLCV"},
    {"org_or_user": "zubyul", "repo_name": "nash-web", "full_name": "zubyul/nash-web", "language": "Rust", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-13T07:08:58Z", "description": "NASH token browser TUI via ratzilla WASM"},
    {"org_or_user": "zubyul", "repo_name": "big-bad-plurigrid-quiz", "full_name": "zubyul/big-bad-plurigrid-quiz", "language": "Emacs Lisp", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-09T18:51:31Z", "description": "27 flashcards from bmorphism/plurigrid/zubyul/monaduck1069 recent activity"},
    {"org_or_user": "zubyul", "repo_name": "Gay.jl", "full_name": "zubyul/Gay.jl", "language": "Julia", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-03-28T11:30:01Z", "description": "Wide-gamut color sampling with splittable determinism"},
    {"org_or_user": "zubyul", "repo_name": "kinesis-kb360pro", "full_name": "zubyul/kinesis-kb360pro", "language": "Python", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-03-26T10:29:40Z", "description": "Claude Code skill for Kinesis Advantage360 Pro keyboard"},
    {"org_or_user": "zubyul", "repo_name": "gay-world", "full_name": "zubyul/gay-world", "language": "Python", "stars": 1, "forks": 1, "open_issues": 0, "pushed_at": "2026-03-26T04:03:39Z", "description": "Goblin world builder"},
    {"org_or_user": "zubyul", "repo_name": "from-possible-worlds", "full_name": "zubyul/from-possible-worlds", "language": "TeX", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-03-16T03:14:55Z", "description": None},
    {"org_or_user": "zubyul", "repo_name": "tilelang-kernels", "full_name": "zubyul/tilelang-kernels", "language": "Python", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-03-16T02:31:13Z", "description": "TileLang GPU kernels for SplitMix64 color generation, GF(3) trit classification"},
    {"org_or_user": "zubyul", "repo_name": "fleet-bootstrap", "full_name": "zubyul/fleet-bootstrap", "language": "Shell", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-02-23T08:19:58Z", "description": None},
    {"org_or_user": "zubyul", "repo_name": "gay-terminal-colors", "full_name": "zubyul/gay-terminal-colors", "language": "Clojure", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-02-21T07:38:14Z", "description": "Gay.jl world_terminal_fingerprint"},
    {"org_or_user": "zubyul", "repo_name": "basin", "full_name": "zubyul/basin", "language": "Rust", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-02-13T10:31:47Z", "description": None},
    {"org_or_user": "zubyul", "repo_name": "openbci-visualizer", "full_name": "zubyul/openbci-visualizer", "language": "Zig", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-02-04T11:17:41Z", "description": None},
    {"org_or_user": "zubyul", "repo_name": "plurigrid-site", "full_name": "zubyul/plurigrid-site", "language": "Svelte", "stars": 0, "forks": 1, "open_issues": 11, "pushed_at": "2026-02-04T03:20:08Z", "description": "Plurigrid world: site deployment"},
    {"org_or_user": "zubyul", "repo_name": "repl", "full_name": "zubyul/repl", "language": "Python", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-02-04T01:08:15Z", "description": None},
    {"org_or_user": "zubyul", "repo_name": "instance-onboarding", "full_name": "zubyul/instance-onboarding", "language": "Shell", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-02-02T11:44:07Z", "description": None},
    {"org_or_user": "zubyul", "repo_name": "vibesnipe", "full_name": "zubyul/vibesnipe", "language": "Move", "stars": 0, "forks": 0, "open_issues": 1, "pushed_at": "2026-01-30T22:36:03Z", "description": None},
    {"org_or_user": "zubyul", "repo_name": "zubyul.github.io", "full_name": "zubyul/zubyul.github.io", "language": "CSS", "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2026-01-27T03:24:34Z", "description": None},
    {"org_or_user": "zubyul", "repo_name": "toad-warpify-extension", "full_name": "zubyul/toad-warpify-extension", "language": "Python", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-01-17T07:48:40Z", "description": "Warpify extension for Toad"},
    {"org_or_user": "zubyul", "repo_name": "thread-site", "full_name": "zubyul/thread-site", "language": "Haskell", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2025-12-23T23:53:27Z", "description": None},
    {"org_or_user": "zubyul", "repo_name": "GayMove", "full_name": "zubyul/GayMove", "language": "Move", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2025-12-18T09:40:08Z", "description": None},
    {"org_or_user": "zubyul", "repo_name": "gay-brain-world", "full_name": "zubyul/gay-brain-world", "language": "Python", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2025-12-16T01:19:28Z", "description": "Gay.jl SPI colors for Moduleur Brain (Pico) + OpenBCI EEG"},
    {"org_or_user": "zubyul", "repo_name": "cat-world", "full_name": "zubyul/cat-world", "language": "TypeScript", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2025-12-12T08:47:14Z", "description": "Cat gaze tracker"},
    {"org_or_user": "zubyul", "repo_name": "hue-world", "full_name": "zubyul/hue-world", "language": "JavaScript", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2025-12-12T08:32:59Z", "description": "Terminal Vibe Snipe puzzle game with ANSI true color"},
    {"org_or_user": "zubyul", "repo_name": "chromatic-vrf", "full_name": "zubyul/chromatic-vrf", "language": "Kotlin", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2025-12-12T03:26:22Z", "description": "Chromatic VRF: I Love Hue puzzle with Gay.jl MCMC"},
    {"org_or_user": "zubyul", "repo_name": "quantum-telephone", "full_name": "zubyul/quantum-telephone", "language": "Jupyter Notebook", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2025-12-08T22:54:16Z", "description": "Quantum telephone world"},
    {"org_or_user": "zubyul", "repo_name": "c-elegans-connectome", "full_name": "zubyul/c-elegans-connectome", "language": "JavaScript", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2025-11-22T15:43:55Z", "description": None},
    {"org_or_user": "zubyul", "repo_name": "jonikas_lab_data_analysis_misc", "full_name": "zubyul/jonikas_lab_data_analysis_misc", "language": "Jupyter Notebook", "stars": 2, "forks": 0, "open_issues": 0, "pushed_at": "2023-08-16T20:24:40Z", "description": "various scripts used to process large genetic sequence data"},
    {"org_or_user": "zubyul", "repo_name": "WGCNA", "full_name": "zubyul/WGCNA", "language": "HTML", "stars": 2, "forks": 0, "open_issues": 0, "pushed_at": "2023-07-05T18:02:30Z", "description": "weighted gene correlation network analysis project"},
]
REPOS.extend(zubyul_repos)

# migalkin repos
migalkin_repos = [
    {"org_or_user": "migalkin", "repo_name": "kgcourse2021", "full_name": "migalkin/kgcourse2021", "language": "HTML", "stars": 25, "forks": 9, "open_issues": 0, "pushed_at": "2026-02-16T05:16:08Z", "description": "Materials for Knowledge Graphs course"},
    {"org_or_user": "migalkin", "repo_name": "NBFNet_mlx", "full_name": "migalkin/NBFNet_mlx", "language": "Python", "stars": 10, "forks": 1, "open_issues": 1, "pushed_at": "2026-03-11T01:31:21Z", "description": "Neural Bellman-Ford networks in MLX for Apple Silicon"},
    {"org_or_user": "migalkin", "repo_name": "StarE", "full_name": "migalkin/StarE", "language": "Python", "stars": 89, "forks": 16, "open_issues": 1, "pushed_at": "2026-04-16T14:12:45Z", "description": "EMNLP 2020: Message Passing for Hyper-Relational Knowledge Graphs"},
    {"org_or_user": "migalkin", "repo_name": "RWL", "full_name": "migalkin/RWL", "language": "Python", "stars": 8, "forks": 1, "open_issues": 0, "pushed_at": "2026-05-28T20:19:20Z", "description": "Weisfeiler and Leman Go Relational (LOG 2022)"},
    {"org_or_user": "migalkin", "repo_name": "NodePiece", "full_name": "migalkin/NodePiece", "language": "Python", "stars": 144, "forks": 21, "open_issues": 0, "pushed_at": "2026-05-07T05:40:02Z", "description": "Compositional and Parameter-Efficient Representations for Large Knowledge Graphs (ICLR'22)"},
    {"org_or_user": "migalkin", "repo_name": "rambo", "full_name": "migalkin/rambo", "language": "Rust", "stars": 3, "forks": 0, "open_issues": 1, "pushed_at": "2023-02-28T16:37:22Z", "description": None},
]
REPOS.extend(migalkin_repos)

# DJedamski repos
djedamski_repos = [
    {"org_or_user": "DJedamski", "repo_name": "kaggle_ncaa18", "full_name": "DJedamski/kaggle_ncaa18", "language": "Jupyter Notebook", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2018-02-26T16:33:24Z", "description": "Code for NCAA March Madness competition (2018)"},
    {"org_or_user": "DJedamski", "repo_name": "Kaggle", "full_name": "DJedamski/Kaggle", "language": None, "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2023-04-21T01:42:35Z", "description": None},
    {"org_or_user": "DJedamski", "repo_name": "Getting-and-Cleaning-Data", "full_name": "DJedamski/Getting-and-Cleaning-Data", "language": "R", "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2023-04-21T01:42:34Z", "description": "Coursera Project"},
    {"org_or_user": "DJedamski", "repo_name": "School", "full_name": "DJedamski/School", "language": "R", "stars": 1, "forks": 1, "open_issues": 0, "pushed_at": "2023-04-21T01:42:33Z", "description": "A couple small projects from grad school"},
]
REPOS.extend(djedamski_repos)

# wasita repos
wasita_repos = [
    {"org_or_user": "wasita", "repo_name": "wasita.github.io", "full_name": "wasita/wasita.github.io", "language": "Svelte", "stars": 1, "forks": 0, "open_issues": 8, "pushed_at": "2026-06-01T04:15:14Z", "description": "personal website"},
    {"org_or_user": "wasita", "repo_name": "wm-cv", "full_name": "wasita/wm-cv", "language": "Svelte", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-05-13T05:29:08Z", "description": "Academic CV as a single page web app"},
    {"org_or_user": "wasita", "repo_name": "vocoder", "full_name": "wasita/vocoder", "language": "JavaScript", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-05-06T05:14:03Z", "description": None},
    {"org_or_user": "wasita", "repo_name": "magic-garden", "full_name": "wasita/magic-garden", "language": "Python", "stars": 2, "forks": 1, "open_issues": 1, "pushed_at": "2026-04-22T21:16:43Z", "description": "A bot for the magic garden discord activity game"},
    {"org_or_user": "wasita", "repo_name": "send2kobo", "full_name": "wasita/send2kobo", "language": "TypeScript", "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2026-05-19T02:59:26Z", "description": "Website for sending books to your kobo e-reader"},
    {"org_or_user": "wasita", "repo_name": "ch3-lib", "full_name": "wasita/ch3-lib", "language": "Typst", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-12T04:03:22Z", "description": None},
]
REPOS.extend(wasita_repos)

# kristinezheng repos
kristinezheng_repos = [
    {"org_or_user": "kristinezheng", "repo_name": "kristinezheng.github.io", "full_name": "kristinezheng/kristinezheng.github.io", "language": "HTML", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-06-07T22:53:10Z", "description": None},
    {"org_or_user": "kristinezheng", "repo_name": "lookit-jenga", "full_name": "kristinezheng/lookit-jenga", "language": "Jupyter Notebook", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2024-05-16T18:29:05Z", "description": "Lookit study for 9.85"},
    {"org_or_user": "kristinezheng", "repo_name": "auditory-illusion", "full_name": "kristinezheng/auditory-illusion", "language": "CSS", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2022-03-07T02:57:44Z", "description": "9.35 spring 2022 auditory illusion"},
    {"org_or_user": "kristinezheng", "repo_name": "Green-Machine", "full_name": "kristinezheng/Green-Machine", "language": "Python", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2021-09-19T05:33:04Z", "description": "HackMIT 2021: Sustainability Track"},
]
REPOS.extend(kristinezheng_repos)

# M1shaaa repos
m1shaaa_repos = [
    {"org_or_user": "M1shaaa", "repo_name": "M1shaaa", "full_name": "M1shaaa/M1shaaa", "language": None, "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-02-04T19:32:04Z", "description": "Config files for my GitHub profile."},
    {"org_or_user": "M1shaaa", "repo_name": "lab-bookshelf-", "full_name": "M1shaaa/lab-bookshelf-", "language": "TypeScript", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2024-12-31T05:11:18Z", "description": None},
    {"org_or_user": "M1shaaa", "repo_name": "Python-Lookit-Uploads", "full_name": "M1shaaa/Python-Lookit-Uploads", "language": "Python", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2024-02-15T22:59:37Z", "description": "random projects"},
]
REPOS.extend(m1shaaa_repos)

# AustinCStone repos (top 15)
austincstone_repos = [
    {"org_or_user": "AustinCStone", "repo_name": "EpsteinSearch", "full_name": "AustinCStone/EpsteinSearch", "language": "Python", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-02-11T01:10:57Z", "description": None},
    {"org_or_user": "AustinCStone", "repo_name": "bmforkupdate", "full_name": "AustinCStone/bmforkupdate", "language": "Python", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2025-05-09T04:50:16Z", "description": None},
    {"org_or_user": "AustinCStone", "repo_name": "bmfork", "full_name": "AustinCStone/bmfork", "language": "Python", "stars": 0, "forks": 0, "open_issues": 1, "pushed_at": "2025-05-09T04:18:54Z", "description": None},
    {"org_or_user": "AustinCStone", "repo_name": "TextGAN", "full_name": "AustinCStone/TextGAN", "language": "Python", "stars": 92, "forks": 30, "open_issues": 5, "pushed_at": "2025-03-03T13:26:32Z", "description": "A generative adversarial network for text generation, written in TensorFlow."},
    {"org_or_user": "AustinCStone", "repo_name": "StereoVisionMRF", "full_name": "AustinCStone/StereoVisionMRF", "language": "Python", "stars": 11, "forks": 4, "open_issues": 0, "pushed_at": "2026-04-01T07:39:41Z", "description": "Using a MRF with loopy belief propagation to infer depth from stereo images."},
    {"org_or_user": "AustinCStone", "repo_name": "StructureFromMotion", "full_name": "AustinCStone/StructureFromMotion", "language": "Python", "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2019-04-26T19:43:12Z", "description": "Recover 3D geometry from videos with unknown camera calibration"},
    {"org_or_user": "AustinCStone", "repo_name": "SpectralClustering", "full_name": "AustinCStone/SpectralClustering", "language": "Python", "stars": 3, "forks": 2, "open_issues": 0, "pushed_at": "2021-04-16T08:46:36Z", "description": "Implementing spectral clustering"},
    {"org_or_user": "AustinCStone", "repo_name": "TFBirds", "full_name": "AustinCStone/TFBirds", "language": "Python", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2019-01-30T08:07:22Z", "description": "Bird flocking simulator in TensorFlow."},
]
REPOS.extend(austincstone_repos)

# ── Insert repos ───────────────────────────────────────────────────────────────
inc_id = 1
repo_id = 1

for r in REPOS:
    trit, color, name = gf3(inc_id)
    h = snap_hash(r)
    con.execute("""
        INSERT INTO world_increments VALUES (?, now(), ?, ?, ?, 'github', ?, 'repo_snapshot', ?, ?, ?)
    """, [inc_id, trit, color, name, r["org_or_user"], r["repo_name"], r["org_or_user"], h])

    con.execute("""
        INSERT INTO repo_snapshots VALUES (?, now(), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [repo_id, inc_id, r["org_or_user"], r["repo_name"], r["full_name"],
          r["language"], r["stars"], r["forks"], r["open_issues"],
          r["pushed_at"], r["description"]])

    inc_id += 1
    repo_id += 1

# ── Aptos snapshots ────────────────────────────────────────────────────────────
aptos_data = [
    ("alice", "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b", 0),
    ("bob",   "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d", 0),
    ("A", "0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a", 0),
    ("B", "0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13", 0),
    ("C", "0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e", 0),
    ("D", "0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1", 0),
    ("E", "0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36", 0),
    ("F", "0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71", 0),
    ("G", "0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32", 0),
    ("H", "0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f", 0),
    ("I", "0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9", 0),
    ("J", "0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54", 0),
    ("K", "0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4", 0),
    ("L", "0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9", 0),
    ("M", "0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9", 0),
    ("N", "0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c", 0),
    ("O", "0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d", 0),
    ("P", "0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948", 0),
    ("Q", "0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9", 0),
    ("R", "0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10", 0),
    ("S", "0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386", 0),
    ("T", "0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588", 0),
    ("U", "0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956", 0),
    ("V", "0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3", 0),
    ("W", "0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0", 0),
    ("X", "0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d", 0),
    ("Y", "0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4", 0),
    ("Z", "0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c", 0),
]

for world, addr, bal_raw in aptos_data:
    bal_apt = bal_raw / 100000000.0
    con.execute("INSERT INTO aptos_snapshots VALUES (now(), ?, ?, ?)", [world, addr, bal_apt])

# ── Multisig probes ────────────────────────────────────────────────────────────
multisig_data = [
    ("A-B", "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2, True),
    ("A-G", "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2, True),
    ("Y-Z", "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2, True),
    ("S-T", "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2, True),
    ("V-W", "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2, True),
]

for pair, addr, sigs, healthy in multisig_data:
    con.execute("INSERT INTO multisig_probes VALUES (now(), ?, ?, ?, ?)", [pair, addr, sigs, healthy])

# ── MNX snapshot (unavailable - Vercel auth) ──────────────────────────────────
# No rows inserted - MNX testnet requires Vercel authentication

print(f"Inserted {len(REPOS)} repos into repo_snapshots")
print(f"Inserted {len(aptos_data)} Aptos snapshots")
print(f"Inserted {len(multisig_data)} multisig probes")
print("MNX: unavailable (Vercel auth required)")

# ── Summary stats ──────────────────────────────────────────────────────────────
rows = con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0]
print(f"Total world_increments: {rows}")
rows = con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0]
print(f"Total repo_snapshots: {rows}")

con.close()
print("DB written to", DB_PATH)
