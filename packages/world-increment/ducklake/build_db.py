#!/usr/bin/env python3
"""Build world-increment DuckDB from sweep data."""
import duckdb
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "world-increments.duckdb")
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

# ── GF(3) helper ─────────────────────────────────────────────────────────────
GF3 = {
    0: (0,  "#d3869b", "ERGODIC"),
    1: (1,  "#b8bb26", "PLUS"),
    2: (-1, "#cc241d", "MINUS"),
}

def gf3(i):
    t, c, n = GF3[i % 3]
    return t, c, n

# ── Parse plurigrid & kubeflow from saved MCP result files ───────────────────
RESULT_DIR = "/root/.claude/projects/-home-user-gorj/dfd856f5-1b00-5a71-9451-ac32ef15fce2/tool-results"
PG_FILE = os.path.join(RESULT_DIR, "mcp-github-search_repositories-1783019205591.txt")
KF_FILE = os.path.join(RESULT_DIR, "mcp-github-search_repositories-1783019204061.txt")

def parse_repo_file(path):
    try:
        with open(path) as f:
            data = json.load(f)
        items = data.get("items", data) if isinstance(data, dict) else data
        return items
    except Exception as e:
        print(f"Error parsing {path}: {e}")
        return []

pg_repos = parse_repo_file(PG_FILE)
kf_repos = parse_repo_file(KF_FILE)
print(f"Parsed plurigrid: {len(pg_repos)} repos, kubeflow: {len(kf_repos)} repos")

# ── Inline repo data from MCP queries ────────────────────────────────────────
teglon_repos = [
  {"name":"jank-crane","full_name":"TeglonLabs/jank-crane","language":"C++","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-06-08T19:03:37Z","description":"crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow"},
  {"name":"mathpix-gem","full_name":"TeglonLabs/mathpix-gem","language":"Ruby","stargazers_count":2,"forks_count":0,"open_issues_count":11,"pushed_at":"2026-01-01T12:13:16Z","description":"Transform mathematical images to LaTeX, chemistry structures to SMILES"},
  {"name":"coin-flip-mcp","full_name":"TeglonLabs/coin-flip-mcp","language":"JavaScript","stargazers_count":0,"forks_count":2,"open_issues_count":1,"pushed_at":"2025-03-16T01:31:45Z","description":"MCP server for flipping coins with varying degrees of randomness from random.org"},
  {"name":"monad-mcp-server","full_name":"TeglonLabs/monad-mcp-server","language":None,"stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2025-05-14T17:53:01Z","description":"Monad MCP Server"},
  {"name":"topoi","full_name":"TeglonLabs/topoi","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":1,"pushed_at":"2025-01-24T06:47:38Z","description":None},
]

bmorphism_repos = [
  {"name":"satreadout","full_name":"bmorphism/satreadout","language":"HTML","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-06-20T13:05:44Z","description":"Machine-checked saturating non-Riemannian perceptual readout"},
  {"name":"Gay.jl","full_name":"bmorphism/Gay.jl","language":"Julia","stargazers_count":2,"forks_count":1,"open_issues_count":187,"pushed_at":"2026-06-20T14:21:55Z","description":"Wide-gamut color sampling with splittable determinism (Pigeons.jl SPI pattern)"},
  {"name":"bci-preview","full_name":"bmorphism/bci-preview","language":"HTML","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-06-20T00:20:47Z","description":"Stable redirect front for the bci.place forester preview"},
  {"name":"world","full_name":"bmorphism/world","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-06-02T06:49:06Z","description":"Local worlds launcher for SA3, jank, and world proofs."},
  {"name":"oxgame","full_name":"bmorphism/oxgame","language":"OCaml","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-05-15T09:55:59Z","description":"Stellar resolution and open-game composition for OCaml"},
  {"name":"nanoclj-zig","full_name":"bmorphism/nanoclj-zig","language":"Zig","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-06-10T16:00:16Z","description":None},
  {"name":"zig-syrup","full_name":"bmorphism/zig-syrup","language":"Zig","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-28T21:42:35Z","description":"Embeddable OCapN Syrup encoder/decoder in Zig — 550 LOC"},
  {"name":"ocaml-mcp-sdk","full_name":"bmorphism/ocaml-mcp-sdk","language":"OCaml","stargazers_count":61,"forks_count":2,"open_issues_count":0,"pushed_at":"2026-05-08T16:50:34Z","description":"OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect library"},
  {"name":"anti-bullshit-mcp-server","full_name":"bmorphism/anti-bullshit-mcp-server","language":"JavaScript","stargazers_count":23,"forks_count":7,"open_issues_count":1,"pushed_at":"2026-02-05T15:46:59Z","description":"MCP server for analyzing claims, validating sources"},
  {"name":"penrose-mcp","full_name":"bmorphism/penrose-mcp","language":"JavaScript","stargazers_count":9,"forks_count":4,"open_issues_count":0,"pushed_at":"2026-06-24T15:36:16Z","description":"Penrose server for the Infinity-Topos environment"},
  {"name":"manifold-mcp-server","full_name":"bmorphism/manifold-mcp-server","language":"JavaScript","stargazers_count":14,"forks_count":9,"open_issues_count":5,"pushed_at":"2026-04-15T19:54:28Z","description":"MCP server for interacting with Manifold Markets prediction markets"},
  {"name":"babashka-mcp-server","full_name":"bmorphism/babashka-mcp-server","language":"JavaScript","stargazers_count":19,"forks_count":6,"open_issues_count":3,"pushed_at":"2026-06-05T13:16:11Z","description":"A MCP server for interacting with Babashka, a native Clojure interpreter"},
  {"name":"say-mcp-server","full_name":"bmorphism/say-mcp-server","language":"JavaScript","stargazers_count":20,"forks_count":9,"open_issues_count":3,"pushed_at":"2026-03-19T23:11:59Z","description":"MCP server for macOS text-to-speech functionality"},
  {"name":"risc0-cosmwasm-example","full_name":"bmorphism/risc0-cosmwasm-example","language":"Rust","stargazers_count":23,"forks_count":2,"open_issues_count":1,"pushed_at":"2025-05-21T13:35:37Z","description":"CosmWasm + zkVM RISC-V EFI template"},
  {"name":"hypernym-mcp-server","full_name":"bmorphism/hypernym-mcp-server","language":"JavaScript","stargazers_count":6,"forks_count":5,"open_issues_count":0,"pushed_at":"2025-10-24T09:21:53Z","description":None},
  {"name":"marginalia-mcp-server","full_name":"bmorphism/marginalia-mcp-server","language":"JavaScript","stargazers_count":8,"forks_count":6,"open_issues_count":0,"pushed_at":"2026-03-27T16:55:55Z","description":"An MCP server implementation for managing marginalia and annotations"},
  {"name":"nats-mcp-server","full_name":"bmorphism/nats-mcp-server","language":None,"stargazers_count":7,"forks_count":3,"open_issues_count":2,"pushed_at":"2025-12-20T23:56:36Z","description":"MCP server for NATS messaging system"},
  {"name":"whale","full_name":"bmorphism/whale","language":"MATLAB","stargazers_count":2,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-20T15:04:09Z","description":"omniglot + sperm whale codas = metawhaling"},
  {"name":"shitcoin","full_name":"bmorphism/shitcoin","language":"Python","stargazers_count":5,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-08T08:07:17Z","description":"gets denom for cw20 assets for permissionless degeneracy in IBC"},
  {"name":"flox-mcp-bb","full_name":"bmorphism/flox-mcp-bb","language":"Clojure","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-06-05T17:53:47Z","description":"Open-source MCP server for Flox — Babashka/Clojure, single file, 20 tools"},
]

zubyul_repos = [
  {"name":"voice-observatory","full_name":"zubyul/voice-observatory","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-24T05:56:20Z","description":"Passive macOS TUI observing voice-download pathways"},
  {"name":"ghostel-emacs-worlds","full_name":"zubyul/ghostel-emacs-worlds","language":"GLSL","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-24T00:21:00Z","description":"Ghostty config + ghostel family + alice/bob emacs-mods"},
  {"name":"big-bad-plurigrid-quiz","full_name":"zubyul/big-bad-plurigrid-quiz","language":"Emacs Lisp","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-04-09T18:51:35Z","description":"27 flashcards from bmorphism/plurigrid/zubyul activity"},
  {"name":"Gay.jl","full_name":"zubyul/Gay.jl","language":"Julia","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-28T11:30:07Z","description":"Wide-gamut color sampling with splittable determinism"},
  {"name":"kinesis-kb360pro","full_name":"zubyul/kinesis-kb360pro","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-26T10:29:44Z","description":"Claude Code skill for Kinesis Advantage360 Pro keyboard"},
  {"name":"gay-world","full_name":"zubyul/gay-world","language":"Python","stargazers_count":1,"forks_count":1,"open_issues_count":0,"pushed_at":"2026-04-05T06:54:03Z","description":"Goblin world builder: each goblin is a world"},
  {"name":"tilelang-kernels","full_name":"zubyul/tilelang-kernels","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-16T02:31:16Z","description":"TileLang GPU kernels for GF(3) trit classification, Sinkhorn OT"},
  {"name":"plurigrid-site","full_name":"zubyul/plurigrid-site","language":"Svelte","stargazers_count":0,"forks_count":1,"open_issues_count":11,"pushed_at":"2026-03-26T09:06:31Z","description":"Plurigrid world: site deployment"},
  {"name":"hue-world","full_name":"zubyul/hue-world","language":"JavaScript","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-26T09:05:56Z","description":"Terminal Vibe Snipe puzzle game with ANSI true color"},
  {"name":"cascade-world","full_name":"zubyul/cascade-world","language":"Python","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-26T09:06:01Z","description":"Cascade development environment"},
  {"name":"jonikas_lab_data_analysis_misc","full_name":"zubyul/jonikas_lab_data_analysis_misc","language":"Jupyter Notebook","stargazers_count":2,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-26T09:05:21Z","description":"various scripts to process large genetic sequence data"},
  {"name":"WGCNA","full_name":"zubyul/WGCNA","language":"HTML","stargazers_count":2,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-03-26T09:05:26Z","description":"weighted gene correlation network analysis project"},
]

migalkin_repos = [
  {"name":"NodePiece","full_name":"migalkin/NodePiece","language":"Python","stargazers_count":144,"forks_count":21,"open_issues_count":0,"pushed_at":"2026-05-07T05:40:02Z","description":"Compositional and Parameter-Efficient Representations for Large Knowledge Graphs"},
  {"name":"StarE","full_name":"migalkin/StarE","language":"Python","stargazers_count":89,"forks_count":16,"open_issues_count":1,"pushed_at":"2026-04-16T14:12:45Z","description":"EMNLP 2020: Message Passing for Hyper-Relational Knowledge Graphs"},
  {"name":"NBFNet_mlx","full_name":"migalkin/NBFNet_mlx","language":"Python","stargazers_count":10,"forks_count":1,"open_issues_count":1,"pushed_at":"2026-03-11T01:31:21Z","description":"Neural Bellman-Ford networks implemented in MLX for Apple Silicon"},
  {"name":"RWL","full_name":"migalkin/RWL","language":"Python","stargazers_count":8,"forks_count":1,"open_issues_count":0,"pushed_at":"2026-05-28T20:19:20Z","description":"Weisfeiler and Leman Go Relational (LOG 2022)"},
  {"name":"kgcourse2021","full_name":"migalkin/kgcourse2021","language":"HTML","stargazers_count":25,"forks_count":9,"open_issues_count":0,"pushed_at":"2026-02-16T05:16:08Z","description":"Материалы к курсу по Knowledge Graphs"},
]

wasita_repos = [
  {"name":"wasita.github.io","full_name":"wasita/wasita.github.io","language":"Svelte","stargazers_count":1,"forks_count":0,"open_issues_count":8,"pushed_at":"2026-07-02T01:40:18Z","description":"personal website"},
  {"name":"proj-template","full_name":"wasita/proj-template","language":None,"stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-06-19T21:22:21Z","description":None},
  {"name":"wm-cv","full_name":"wasita/wm-cv","language":"Svelte","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-05-13T05:29:08Z","description":"Academic CV written as a single page web app"},
  {"name":"send2kobo","full_name":"wasita/send2kobo","language":"TypeScript","stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-05-19T02:59:26Z","description":"Website for sending books to your kobo e-reader"},
  {"name":"magic-garden","full_name":"wasita/magic-garden","language":"Python","stargazers_count":2,"forks_count":1,"open_issues_count":1,"pushed_at":"2026-04-22T21:16:43Z","description":"a bot for the magic garden discord activity game"},
]

kristinezheng_repos = [
  {"name":"kristinezheng.github.io","full_name":"kristinezheng/kristinezheng.github.io","language":"HTML","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-07-01T20:57:48Z","description":None},
  {"name":"lookit-jenga","full_name":"kristinezheng/lookit-jenga","language":"Jupyter Notebook","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2024-05-16T18:29:05Z","description":"Lookit study for 9.85"},
  {"name":"Green-Machine","full_name":"kristinezheng/Green-Machine","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2021-09-19T05:33:04Z","description":"HackMIT 2021: Sustainability Track"},
]

m1shaaa_repos = [
  {"name":"lab-bookshelf-","full_name":"M1shaaa/lab-bookshelf-","language":"TypeScript","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2024-12-31T05:11:18Z","description":None},
  {"name":"Python-Lookit-Uploads","full_name":"M1shaaa/Python-Lookit-Uploads","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2024-02-15T22:59:37Z","description":"random projects"},
]

austinc_repos = [
  {"name":"TextGAN","full_name":"AustinCStone/TextGAN","language":"Python","stargazers_count":92,"forks_count":30,"open_issues_count":5,"pushed_at":"2025-03-03T13:26:32Z","description":"A generative adversarial network for text generation, written in TensorFlow."},
  {"name":"EpsteinSearch","full_name":"AustinCStone/EpsteinSearch","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2026-02-11T01:10:57Z","description":None},
  {"name":"StereoVisionMRF","full_name":"AustinCStone/StereoVisionMRF","language":"Python","stargazers_count":11,"forks_count":4,"open_issues_count":0,"pushed_at":"2026-04-01T07:39:41Z","description":"Using a MRF with loopy belief propagation to infer depth from stereo images."},
  {"name":"bmfork","full_name":"AustinCStone/bmfork","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":1,"pushed_at":"2025-05-09T04:18:54Z","description":None},
]

djedamski_repos = [
  {"name":"kaggle_ncaa18","full_name":"DJedamski/kaggle_ncaa18","language":"Jupyter Notebook","stargazers_count":0,"forks_count":0,"open_issues_count":0,"pushed_at":"2018-02-26T16:33:24Z","description":"Code for NCAA March Madness competition (2018)"},
  {"name":"Kaggle","full_name":"DJedamski/Kaggle","language":None,"stargazers_count":1,"forks_count":0,"open_issues_count":0,"pushed_at":"2023-04-21T01:42:35Z","description":None},
  {"name":"School","full_name":"DJedamski/School","language":"R","stargazers_count":1,"forks_count":1,"open_issues_count":0,"pushed_at":"2023-04-21T01:42:33Z","description":"A couple small projects from grad school"},
]

# Source mapping
SOURCES = [
    ("org",  "plurigrid",    pg_repos),
    ("org",  "kubeflow",     kf_repos),
    ("org",  "TeglonLabs",   teglon_repos),
    ("user", "bmorphism",    bmorphism_repos),
    ("user", "zubyul",       zubyul_repos),
    ("user", "migalkin",     migalkin_repos),
    ("user", "wasita",       wasita_repos),
    ("user", "kristinezheng",kristinezheng_repos),
    ("user", "M1shaaa",      m1shaaa_repos),
    ("user", "AustinCStone", austinc_repos),
    ("user", "DJedamski",    djedamski_repos),
]

# ── Insert repo_snapshots + world_increments ──────────────────────────────────
inc_id = 1
repo_id = 1
for src_type, src_name, repos in SOURCES:
    for repo in repos:
        trit, color, name = gf3(inc_id)
        rname = repo.get("name", "")
        full  = repo.get("full_name", "")
        lang  = repo.get("language") or ""
        stars = repo.get("stargazers_count", 0) or 0
        forks = repo.get("forks_count", 0) or 0
        issues= repo.get("open_issues_count", 0) or 0
        pushed= repo.get("pushed_at") or repo.get("updated_at") or ""
        desc  = (repo.get("description") or "")[:120]
        snap_hash = hex(hash(full + pushed))[2:10]

        con.execute("""
            INSERT INTO world_increments
              (id, timestamp, gf3_trit, gf3_color, gf3_name, source_type, source_name,
               event_type, repo_name, actor, snapshot_hash)
            VALUES (?,now(),?,?,?,'repo_snapshot',?,?,?,?,?)
        """, [inc_id, trit, color, name, src_name, "push", rname, src_name, snap_hash])

        con.execute("""
            INSERT INTO repo_snapshots
              (id, timestamp, increment_id, org_or_user, repo_name, full_name,
               language, stars, forks, open_issues, pushed_at, description)
            VALUES (?,now(),?,?,?,?,?,?,?,?,?,?)
        """, [repo_id, inc_id, src_name, rname, full, lang, stars, forks, issues, pushed, desc])

        inc_id += 1
        repo_id += 1

print(f"Inserted {inc_id-1} increments, {repo_id-1} repo snapshots")

# ── Aptos snapshots ───────────────────────────────────────────────────────────
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
    con.execute("INSERT INTO aptos_snapshots(world,address,balance_apt) VALUES (?,?,?)", [world, addr, bal])
print(f"Inserted {len(aptos_data)} aptos snapshots")

# ── Multisig probes ───────────────────────────────────────────────────────────
multisig_data = [
    ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2),
    ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2),
    ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2),
    ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2),
    ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2),
]
for pair, addr, sigs in multisig_data:
    con.execute("INSERT INTO multisig_probes(pair,address,sigs_required,healthy) VALUES (?,?,?,?)",
                [pair, addr, sigs, True])
print(f"Inserted {len(multisig_data)} multisig probes (all healthy, 2-of-2)")

# ── MNX — unavailable (Vercel auth required) ─────────────────────────────────
# No rows inserted; noted in LATEST_SWEEP.md

# ── Summary stats ─────────────────────────────────────────────────────────────
res = con.execute("SELECT COUNT(*) FROM world_increments").fetchone()
print(f"world_increments total: {res[0]}")
res = con.execute("SELECT org_or_user, COUNT(*) FROM repo_snapshots GROUP BY org_or_user ORDER BY 2 DESC").fetchall()
print("repo_snapshots by source:")
for r in res:
    print(f"  {r[0]:20s} {r[1]}")

res = con.execute("SELECT gf3_color, gf3_name, COUNT(*) FROM world_increments GROUP BY 1,2").fetchall()
print("GF(3) distribution:")
for r in res:
    print(f"  {r[1]:10s} {r[0]}  count={r[2]}")

con.close()
print("DB written to:", DB_PATH)
