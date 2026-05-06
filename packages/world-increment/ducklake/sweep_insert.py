#!/usr/bin/env python3
import duckdb
from datetime import datetime, timezone

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

def gf3(id_):
    t = id_ % 3
    if t == 0:
        return 0, "#d3869b", "ERGODIC"
    elif t == 1:
        return 1, "#b8bb26", "PLUS"
    else:
        return -1, "#cc241d", "MINUS"

con = duckdb.connect(DB)

# Ensure tables exist
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

# ── World increment sources ──────────────────────────────────────────────────
sources = [
    ("org",  "plurigrid",     "repo_sweep", None),
    ("org",  "kubeflow",      "repo_sweep", None),
    ("org",  "TeglonLabs",    "repo_sweep", None),
    ("user", "bmorphism",     "repo_sweep", None),
    ("user", "zubyul",        "repo_sweep", None),
    ("user", "migalkin",      "repo_sweep", None),
    ("user", "DJedamski",     "repo_sweep", None),
    ("user", "wasita",        "repo_sweep", None),
    ("user", "kristinezheng", "repo_sweep", None),
    ("user", "M1shaaa",       "repo_sweep", None),
    ("user", "AustinCStone",  "repo_sweep", None),
    ("event","hamming_swarm", "aptos_snapshot", None),
    ("event","hamming_swarm", "multisig_probe", None),
]

wi_start = con.execute("SELECT COALESCE(MAX(id),0)+1 FROM world_increments").fetchone()[0]
wi_ids = {}
for i, (src_type, src_name, ev_type, _) in enumerate(sources):
    wid = wi_start + i
    trit, color, name = gf3(wid)
    con.execute(
        "INSERT INTO world_increments VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        [wid, NOW, trit, color, name, src_type, src_name, ev_type, None, None, None]
    )
    wi_ids[(src_type, src_name, ev_type)] = wid

print(f"Inserted {len(sources)} world_increments starting at id={wi_start}")

# ── Repo snapshots ───────────────────────────────────────────────────────────
repos = [
    # (org_or_user, repo_name, full_name, language, stars, forks, open_issues, pushed_at, description)
    # plurigrid
    ("plurigrid","gorj","plurigrid/gorj","Clojure",0,0,88,"2026-05-06T16:08:56Z","forj + Rama topology nREPL routing + GF(3) gay trit coloring"),
    ("plurigrid","zig-syrup","plurigrid/zig-syrup","Zig",2,2,0,"2026-04-30T03:52:16Z","High-performance Zig implementation of OCapN Syrup with CapTP optimizations"),
    ("plurigrid","horse","plurigrid/horse","TeX",1,1,8,"2026-04-29T20:35:13Z",None),
    ("plurigrid","asi","plurigrid/asi","HTML",19,5,4,"2026-04-26T08:51:41Z","everything is topological chemputer!"),
    ("plurigrid","nash-portal","plurigrid/nash-portal","Rust",2,2,0,"2026-04-26T08:50:56Z","NASH token TUI in the browser - ratzilla WASM + GeckoTerminal"),
    ("plurigrid","asi-skills","plurigrid/asi-skills","Julia",3,1,0,"2026-04-26T08:09:26Z","69 skills with Galois Hole Type accessibility"),
    ("plurigrid","bci-blue-share","plurigrid/bci-blue-share","JavaScript",0,0,0,"2026-04-26T07:08:03Z","BCI signal infrastructure"),
    ("plurigrid","nanoclj-zig","plurigrid/nanoclj-zig","Zig",1,1,20,"2026-04-25T07:29:09Z","NaN-boxed Clojure interpreter in Zig 0.15"),
    ("plurigrid","spi-race","plurigrid/spi-race","Swift",0,0,0,"2026-04-21T19:31:56Z","Splitmix Parallel Integrity"),
    ("plurigrid","reafference","plurigrid/reafference","HTML",0,0,0,"2026-04-16T05:21:49Z","Reafference adaptation workspace"),
    ("plurigrid","web-browser","plurigrid/web-browser","Rust",0,0,0,"2026-04-10T02:54:47Z","web-browser - from prepostweb lineage"),
    ("plurigrid","vivarium","plurigrid/vivarium","Clojure",1,0,0,"2026-04-08T08:38:37Z",None),
    ("plurigrid","flowglad-rs","plurigrid/flowglad-rs","Rust",0,0,0,"2026-04-08T07:56:15Z",None),
    ("plurigrid","tree-sitter-nanoclj-zig","plurigrid/tree-sitter-nanoclj-zig","C",0,0,0,"2026-04-04T07:48:21Z","Tree-sitter grammar for nanoclj-zig"),
    ("plurigrid","forester","plurigrid/forester","XSLT",0,0,0,"2026-03-30T01:32:26Z","CatColab mathematical documentation forest"),
    ("plurigrid","gatomic","plurigrid/gatomic","Clojure",0,0,0,"2026-03-28T00:00:00Z",None),
    # kubeflow
    ("kubeflow","hub","kubeflow/hub","Go",175,178,44,"2026-05-06T16:21:38Z","Model Registry for ML model developers"),
    ("kubeflow","trainer","kubeflow/trainer","Go",2095,948,120,"2026-05-06T14:28:41Z","Distributed AI Model Training and LLM Fine-Tuning on Kubernetes"),
    ("kubeflow","kale","kubeflow/kale","Python",684,156,58,"2026-05-06T10:29:41Z","Kubeflow superfood for Data Scientists"),
    ("kubeflow","pipelines","kubeflow/pipelines","Python",4134,1988,488,"2026-05-05T20:48:37Z","Machine Learning Pipelines for Kubeflow"),
    ("kubeflow","mcp-apache-spark-history-server","kubeflow/mcp-apache-spark-history-server","Python",164,56,24,"2026-05-05T19:43:08Z","MCP Server and CLI for Apache Spark History Server"),
    # TeglonLabs
    ("TeglonLabs","mathpix-gem","TeglonLabs/mathpix-gem","Ruby",2,0,11,"2026-01-01T12:13:13Z","Transform mathematical images to LaTeX"),
    ("TeglonLabs","coin-flip-mcp","TeglonLabs/coin-flip-mcp","JavaScript",0,2,1,"2025-09-21T08:57:27Z","MCP server for flipping coins with varying degrees of randomness"),
    ("TeglonLabs","monad-mcp-server","TeglonLabs/monad-mcp-server",None,0,0,0,"2025-05-14T11:36:14Z","Monad MCP Server"),
    ("TeglonLabs","topoi","TeglonLabs/topoi","Python",0,0,1,"2025-01-24T04:49:26Z",None),
    # bmorphism
    ("bmorphism","Gay.jl","bmorphism/Gay.jl","Julia",1,0,187,"2026-05-06T00:31:13Z","Wide-gamut color sampling with splittable determinism"),
    ("bmorphism","boxxy","bmorphism/boxxy","Move",0,1,0,"2026-04-30T03:35:47Z",None),
    ("bmorphism","nanoclj-zig","bmorphism/nanoclj-zig","Zig",0,0,0,"2026-04-25T07:29:15Z",None),
    ("bmorphism","postweb","bmorphism/postweb","Go",0,0,0,"2026-04-09T10:51:57Z","postweb - evolved from prepostweb"),
    ("bmorphism","shitcoin","bmorphism/shitcoin","Python",5,0,0,"2026-04-08T08:07:08Z","gets denom for cw20 assets for permissionless degeneracy in IBC"),
    ("bmorphism","magic-world-org","bmorphism/magic-world-org","Python",1,0,0,"2026-04-05T07:03:50Z","Magic World Org (Local MLX)"),
    ("bmorphism","zig-syrup","bmorphism/zig-syrup","Zig",0,0,0,"2026-03-28T21:42:32Z","Embeddable OCapN Syrup encoder/decoder in Zig"),
    ("bmorphism","ocaml-mcp-sdk","bmorphism/ocaml-mcp-sdk","OCaml",60,2,0,"2026-03-16T05:24:25Z","OCaml SDK for Model Context Protocol"),
    ("bmorphism","flox-mcp-bb","bmorphism/flox-mcp-bb","Clojure",0,0,0,"2026-02-12T02:45:43Z","Open-source MCP server for Flox"),
    ("bmorphism","vibesnipe-market","bmorphism/vibesnipe-market","Move",0,0,9,"2026-02-05T10:23:25Z",None),
    # zubyul
    ("zubyul","voice-observatory","zubyul/voice-observatory","Python",0,0,0,"2026-04-24T05:56:17Z","Passive macOS TUI observing voice-download pathways"),
    ("zubyul","ghostel-emacs-worlds","zubyul/ghostel-emacs-worlds","GLSL",0,0,0,"2026-04-24T00:20:56Z","Ghostty config + ghostel family + alice/bob emacs-mods"),
    ("zubyul","nash-tui","zubyul/nash-tui","Rust",0,0,0,"2026-04-13T07:45:16Z","NASH token TUI: real-time candles, ticker, buy pressure gauge"),
    ("zubyul","nash-web","zubyul/nash-web","Rust",0,0,0,"2026-04-13T07:08:58Z","NASH token browser TUI via ratzilla WASM"),
    ("zubyul","big-bad-plurigrid-quiz","zubyul/big-bad-plurigrid-quiz","Emacs Lisp",0,0,0,"2026-04-09T18:51:31Z","27 flashcards from bmorphism/plurigrid/zubyul/monaduck1069 activity"),
    ("zubyul","Gay.jl","zubyul/Gay.jl","Julia",0,1,0,"2026-03-28T11:30:01Z","Wide-gamut color sampling with splittable determinism"),
    ("zubyul","kinesis-kb360pro","zubyul/kinesis-kb360pro","Python",0,0,0,"2026-03-26T10:29:40Z","Claude Code skill for Kinesis Advantage360 Pro keyboard"),
    ("zubyul","gay-world","zubyul/gay-world","Python",1,1,0,"2026-03-26T04:03:39Z","Goblin world builder: each goblin is a world"),
    ("zubyul","from-possible-worlds","zubyul/from-possible-worlds","TeX",0,0,0,"2026-03-16T03:14:55Z",None),
    ("zubyul","tilelang-kernels","zubyul/tilelang-kernels","Python",0,0,0,"2026-03-16T02:31:13Z","TileLang GPU kernels for SplitMix64 color generation, GF(3)"),
    # migalkin
    ("migalkin","kgcourse2021","migalkin/kgcourse2021","HTML",25,9,0,"2025-08-04T03:01:46Z","Материалы к курсу по Knowledge Graphs"),
    ("migalkin","migalkin.github.io","migalkin/migalkin.github.io","JavaScript",0,0,0,"2025-01-22T04:53:51Z","Github Pages template for academic personal websites"),
    ("migalkin","NBFNet_mlx","migalkin/NBFNet_mlx","Python",10,1,1,"2024-03-02T00:15:23Z","Neural Bellman-Ford networks implemented in MLX for Apple Silicon"),
    ("migalkin","StarE","migalkin/StarE","Python",89,16,1,"2023-12-01T20:12:24Z","EMNLP 2020: Message Passing for Hyper-Relational Knowledge Graphs"),
    ("migalkin","rambo","migalkin/rambo","Rust",3,0,1,"2023-02-08T14:27:03Z",None),
    # DJedamski
    ("DJedamski","kaggle_ncaa18","DJedamski/kaggle_ncaa18","Jupyter Notebook",0,0,0,"2018-02-26T16:33:24Z","Code for NCAA March Madness competition (2018)"),
    ("DJedamski","Kaggle","DJedamski/Kaggle",None,1,0,0,"2023-04-21T01:42:35Z",None),
    ("DJedamski","Getting-and-Cleaning-Data","DJedamski/Getting-and-Cleaning-Data","R",1,0,0,"2023-04-21T01:42:34Z","Coursera Project"),
    ("DJedamski","EDA","DJedamski/EDA","R",0,0,0,"2014-11-09T17:00:39Z","Coursera Project"),
    ("DJedamski","Project_Euler","DJedamski/Project_Euler",None,0,0,0,"2015-09-05T17:13:32Z",None),
    # wasita
    ("wasita","vocoder","wasita/vocoder","JavaScript",0,0,0,"2026-05-06T05:14:03Z",None),
    ("wasita","wasita.github.io","wasita/wasita.github.io","Svelte",1,0,8,"2026-04-28T05:26:08Z","personal website"),
    ("wasita","magic-garden","wasita/magic-garden","Python",2,1,1,"2026-04-22T21:16:43Z","bot for magic garden discord activity game"),
    ("wasita","ch3-lib","wasita/ch3-lib","Typst",0,0,0,"2026-04-12T04:03:22Z",None),
    ("wasita","wm-cv","wasita/wm-cv","Svelte",0,0,0,"2026-04-12T02:53:51Z","Academic CV written as a single page web app"),
    # kristinezheng
    ("kristinezheng","kristinezheng.github.io","kristinezheng/kristinezheng.github.io","HTML",0,0,0,"2026-04-09T17:09:47Z",None),
    ("kristinezheng","Portfolio","kristinezheng/Portfolio",None,0,0,0,"2025-02-12T00:00:45Z","July 2021"),
    ("kristinezheng","lookit-jenga","kristinezheng/lookit-jenga","Jupyter Notebook",0,0,0,"2024-05-16T18:29:05Z","Lookit study for 9.85"),
    ("kristinezheng","auditory-illusion","kristinezheng/auditory-illusion","CSS",0,0,0,"2022-03-07T02:57:44Z","9.35 spring 2022 auditory illusion"),
    ("kristinezheng","graph_example","kristinezheng/graph_example","Python",0,0,0,"2021-10-08T07:29:53Z",None),
    # M1shaaa
    ("M1shaaa","M1shaaa","M1shaaa/M1shaaa",None,0,0,0,"2026-02-04T19:32:04Z","Config files for my GitHub profile."),
    ("M1shaaa","lab-bookshelf-","M1shaaa/lab-bookshelf-","TypeScript",0,0,0,"2024-12-31T05:11:18Z",None),
    ("M1shaaa","rosie-s-study-3-lookit-project","M1shaaa/rosie-s-study-3-lookit-project",None,0,0,0,"2024-11-04T22:15:39Z",None),
    ("M1shaaa","Python-Lookit-Uploads","M1shaaa/Python-Lookit-Uploads","Python",0,0,0,"2024-02-15T22:59:37Z","random projects"),
    ("M1shaaa","Classes","M1shaaa/Classes",None,0,0,0,"2023-12-06T18:20:27Z",None),
    # AustinCStone
    ("AustinCStone","EpsteinSearch","AustinCStone/EpsteinSearch","Python",0,0,0,"2026-02-11T01:10:57Z",None),
    ("AustinCStone","bmforkupdate","AustinCStone/bmforkupdate","Python",0,0,0,"2025-05-09T04:50:16Z",None),
    ("AustinCStone","bmfork","AustinCStone/bmfork","Python",0,0,1,"2025-05-09T04:18:54Z",None),
    ("AustinCStone","bitmind-fork","AustinCStone/bitmind-fork",None,0,0,0,"2025-01-09T06:16:51Z","forked on jan 8 2025"),
    ("AustinCStone","testLogin","AustinCStone/testLogin","Python",0,0,0,"2023-02-13T20:52:27Z",None),
]

# Map org_or_user to increment_id
ou_to_wi = {
    "plurigrid":     wi_ids[("org",  "plurigrid",     "repo_sweep")],
    "kubeflow":      wi_ids[("org",  "kubeflow",      "repo_sweep")],
    "TeglonLabs":    wi_ids[("org",  "TeglonLabs",    "repo_sweep")],
    "bmorphism":     wi_ids[("user", "bmorphism",     "repo_sweep")],
    "zubyul":        wi_ids[("user", "zubyul",        "repo_sweep")],
    "migalkin":      wi_ids[("user", "migalkin",      "repo_sweep")],
    "DJedamski":     wi_ids[("user", "DJedamski",     "repo_sweep")],
    "wasita":        wi_ids[("user", "wasita",        "repo_sweep")],
    "kristinezheng": wi_ids[("user", "kristinezheng", "repo_sweep")],
    "M1shaaa":       wi_ids[("user", "M1shaaa",       "repo_sweep")],
    "AustinCStone":  wi_ids[("user", "AustinCStone",  "repo_sweep")],
}

rs_start = con.execute("SELECT COALESCE(MAX(id),0)+1 FROM repo_snapshots").fetchone()[0]
for i, (ou, repo, full, lang, stars, forks, issues, pushed, desc) in enumerate(repos):
    rid = rs_start + i
    wid = ou_to_wi[ou]
    con.execute(
        "INSERT INTO repo_snapshots VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
        [rid, NOW, wid, ou, repo, full, lang, stars, forks, issues, pushed, desc]
    )

print(f"Inserted {len(repos)} repo_snapshots starting at id={rs_start}")

# ── Aptos snapshots ──────────────────────────────────────────────────────────
aptos_data = [
    ("alice","0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b",0.0),
    ("bob",  "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d",0.0),
    ("A",    "0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a",0.0),
    ("B",    "0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13",0.0),
    ("C",    "0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e",0.0),
    ("D",    "0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1",0.0),
    ("E",    "0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36",0.0),
    ("F",    "0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71",0.0),
    ("G",    "0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32",0.0),
    ("H",    "0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f",0.0),
    ("I",    "0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9",0.0),
    ("J",    "0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54",0.0),
    ("K",    "0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4",0.0),
    ("L",    "0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9",0.0),
    ("M",    "0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9",0.0),
    ("N",    "0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c",0.0),
    ("O",    "0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d",0.0),
    ("P",    "0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948",0.0),
    ("Q",    "0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9",0.0),
    ("R",    "0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10",0.0),
    ("S",    "0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386",0.0),
    ("T",    "0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588",0.0),
    ("U",    "0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956",0.0),
    ("V",    "0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3",0.0),
    ("W",    "0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0",0.0),
    ("X",    "0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d",0.0),
    ("Y",    "0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4",0.0),
    ("Z",    "0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c",0.0),
]

for world, addr, bal in aptos_data:
    con.execute("INSERT INTO aptos_snapshots VALUES (?,?,?,?)", [NOW, world, addr, bal])

print(f"Inserted {len(aptos_data)} aptos_snapshots")

# ── Multisig probes ──────────────────────────────────────────────────────────
multisig_data = [
    ("A-B", "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2, True),
    ("A-G", "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2, True),
    ("Y-Z", "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2, True),
    ("S-T", "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2, True),
    ("V-W", "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2, True),
]

for pair, addr, sigs, healthy in multisig_data:
    con.execute("INSERT INTO multisig_probes VALUES (?,?,?,?,?)", [NOW, pair, addr, sigs, healthy])

print(f"Inserted {len(multisig_data)} multisig_probes")

# MNX Markets - SPA, no JSON API available
print("MNX Markets: SPA (Next.js) - no JSON API endpoint found, skipping")

con.close()
print("Done.")
