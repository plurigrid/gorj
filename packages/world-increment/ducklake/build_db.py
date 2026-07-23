#!/usr/bin/env python3
"""Build world-increment DuckDB ducklake from sweep data."""
import duckdb
import json

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
con = duckdb.connect(DB_PATH)

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

# GF3 color chain helper
def gf3(id_val):
    m = id_val % 3
    if m == 0:
        return (0, "#d3869b", "ERGODIC")
    elif m == 1:
        return (1, "#b8bb26", "PLUS")
    else:
        return (-1, "#cc241d", "MINUS")

# ── GITHUB REPO SNAPSHOTS ──────────────────────────────────────────────

repos_data = []

# TeglonLabs repos
teglon_repos = [
    ("TeglonLabs", "jank-crane", "TeglonLabs/jank-crane", "C++", 0, 0, 0, "2026-06-08T19:03:03Z", "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow"),
    ("TeglonLabs", "mathpix-gem", "TeglonLabs/mathpix-gem", "Ruby", 2, 0, 11, "2026-01-01T12:13:13Z", "Transform mathematical images to LaTeX, chemistry structures to SMILES"),
    ("TeglonLabs", "coin-flip-mcp", "TeglonLabs/coin-flip-mcp", "JavaScript", 0, 2, 1, "2025-09-21T08:57:27Z", "MCP server for flipping coins with varying degrees of randomness from random.org"),
    ("TeglonLabs", "monad-mcp-server", "TeglonLabs/monad-mcp-server", "", 0, 0, 0, "2025-05-14T11:36:14Z", "Monad MCP Server"),
    ("TeglonLabs", "topoi", "TeglonLabs/topoi", "Python", 0, 0, 1, "2025-01-24T04:49:26Z", ""),
]

# bmorphism repos (top 20 by recency)
bmorphism_repos = [
    ("bmorphism", "Gay.jl", "bmorphism/Gay.jl", "Julia", 2, 1, 187, "2026-07-21T12:57:35Z", "Wide-gamut color sampling with splittable determinism (Pigeons.jl SPI pattern) + LispSyntax"),
    ("bmorphism", "gay-chat", "bmorphism/gay-chat", "Scheme", 0, 0, 0, "2026-07-14T21:00:00Z", "gay://chat operationalization over Spritely Brassica Chat"),
    ("bmorphism", "satreadout", "bmorphism/satreadout", "HTML", 0, 0, 0, "2026-06-20T13:05:44Z", "Machine-checked saturating non-Riemannian perceptual readout"),
    ("bmorphism", "anti-bullshit-mcp-server", "bmorphism/anti-bullshit-mcp-server", "JavaScript", 22, 7, 1, "2026-07-12T19:31:54Z", "MCP server for analyzing claims, validating sources, and detecting manipulation"),
    ("bmorphism", "ocaml-mcp-sdk", "bmorphism/ocaml-mcp-sdk", "OCaml", 61, 2, 0, "2026-05-08T16:50:34Z", "OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect library"),
    ("bmorphism", "shitcoin", "bmorphism/shitcoin", "Python", 5, 0, 0, "2026-04-08T08:07:17Z", "gets denom for cw20 assets for permissionless degeneracy in IBC"),
    ("bmorphism", "whale", "bmorphism/whale", "MATLAB", 2, 0, 0, "2026-04-20T15:04:09Z", "omniglot + sperm whale codas = metawhaling"),
    ("bmorphism", "open-location-code-zig", "bmorphism/open-location-code-zig", "Zig", 3, 0, 0, "2026-03-24T21:54:01Z", "Open Location Code (Plus Codes) for Zig"),
    ("bmorphism", "monero-rental-hash-war", "bmorphism/monero-rental-hash-war", "Haskell", 1, 0, 0, "2025-10-24T09:25:25Z", "Compositional OpenGame analysis of Monero rental hash war"),
    ("bmorphism", "flox-mcp-bb", "bmorphism/flox-mcp-bb", "Clojure", 0, 0, 0, "2026-06-05T17:53:47Z", "Open-source MCP server for Flox - Babashka/Clojure, single file, 20 tools"),
]

# zubyul repos (top 10)
zubyul_repos = [
    ("zubyul", "voice-observatory", "zubyul/voice-observatory", "Python", 0, 0, 0, "2026-04-24T05:56:20Z", "Passive macOS TUI observing voice-download pathways"),
    ("zubyul", "ghostel-emacs-worlds", "zubyul/ghostel-emacs-worlds", "GLSL", 0, 0, 0, "2026-04-24T00:21:00Z", "Ghostty config + ghostel family + alice/bob emacs-mods"),
    ("zubyul", "Gay.jl", "zubyul/Gay.jl", "Julia", 0, 0, 0, "2026-03-28T11:30:07Z", "Wide-gamut color sampling with splittable determinism (Pigeons.jl SPI pattern)"),
    ("zubyul", "kinesis-kb360pro", "zubyul/kinesis-kb360pro", "Python", 0, 0, 0, "2026-03-26T10:29:44Z", "Claude Code skill for Kinesis Advantage360 Pro keyboard"),
    ("zubyul", "gay-world", "zubyul/gay-world", "Python", 1, 1, 0, "2026-04-05T06:54:03Z", "Goblin world builder: each goblin is a world"),
    ("zubyul", "tilelang-kernels", "zubyul/tilelang-kernels", "Python", 0, 0, 0, "2026-03-16T02:31:16Z", "TileLang GPU kernels for SplitMix64 color generation, GF(3) trit classification"),
    ("zubyul", "big-bad-plurigrid-quiz", "zubyul/big-bad-plurigrid-quiz", "Emacs Lisp", 0, 0, 0, "2026-04-09T18:51:35Z", "27 flashcards from bmorphism/plurigrid/zubyul/monaduck1069 recent activity"),
    ("zubyul", "hue-world", "zubyul/hue-world", "JavaScript", 0, 0, 0, "2026-03-26T09:05:56Z", "Terminal Vibe Snipe puzzle game with ANSI true color"),
    ("zubyul", "wasita.github.io", "wasita/wasita.github.io", "Svelte", 1, 0, 8, "2026-07-21T15:55:45Z", "personal website"),
    ("zubyul", "jonikas_lab_data_analysis_misc", "zubyul/jonikas_lab_data_analysis_misc", "Jupyter Notebook", 2, 0, 0, "2023-06-15T21:54:54Z", "various scripts used to process large genetic sequence data"),
]

# plurigrid repos (top 20 most recently pushed)
plurigrid_repos = [
    ("plurigrid", "gorj", "plurigrid/gorj", "Clojure", 1, 0, 1332, "2026-07-23T00:14:16Z", "forj + Rama topology nREPL routing + GF(3) gay trit coloring for compositional open game REPL orchestration"),
    ("plurigrid", "eirobri", "plurigrid/eirobri", "Clojure", 0, 0, 31, "2026-07-21T02:24:02Z", "EiRoBri replay world"),
    ("plurigrid", "place", "plurigrid/place", "TeX", 1, 2, 14, "2026-07-14T09:11:33Z", ""),
    ("plurigrid", "asi", "plurigrid/asi", "HTML", 31, 10, 4, "2026-07-10T09:47:39Z", "everything is topological chemputer!"),
    ("plurigrid", "shrimp", "plurigrid/shrimp", "", 0, 0, 0, "2026-07-03T01:24:20Z", "Jank worked example: shrimp"),
    ("plurigrid", "nash-portal", "plurigrid/nash-portal", "Rust", 2, 2, 1, "2026-05-19T01:49:59Z", "NASH token TUI in the browser - ratzilla WASM + GeckoTerminal OHLCV candlesticks"),
    ("plurigrid", "zig-syrup", "plurigrid/zig-syrup", "Zig", 2, 2, 0, "2026-04-30T03:52:16Z", "High-performance Zig implementation of OCapN Syrup with CapTP optimizations"),
    ("plurigrid", "asi-skills", "plurigrid/asi-skills", "Julia", 3, 0, 0, "2026-04-26T08:09:26Z", "69 skills with Galois Hole Type accessibility (Seven Sketches §1.4.1)"),
    ("plurigrid", "nanoclj-zig", "plurigrid/nanoclj-zig", "Zig", 1, 1, 20, "2026-04-25T07:29:09Z", "NaN-boxed Clojure interpreter in Zig 0.15 - interaction nets, fuel-bounded eval, GF(3) trit conservation"),
    ("plurigrid", "bci-blue-share", "plurigrid/bci-blue-share", "JavaScript", 0, 0, 0, "2026-04-26T07:08:03Z", "BCI signal infrastructure - bci.blue / bci.red / bci.horse"),
    ("plurigrid", "ontology", "plurigrid/ontology", "JavaScript", 8, 9, 16, "2025-05-27T18:18:34Z", "autopoietic ergodicity and embodied gradualism"),
    ("plurigrid", "microworlds", "plurigrid/microworlds", "Rust", 3, 5, 3, "2023-05-13T03:54:56Z", ""),
    ("plurigrid", "vcg-auction", "plurigrid/vcg-auction", "Rust", 7, 3, 1, "2023-03-16T21:53:08Z", "a simple contract that performs a VCG auction"),
    ("plurigrid", "agent", "plurigrid/agent", "Python", 5, 1, 6, "2023-03-31T18:45:23Z", "Framework for agency amplification. A conversational agent for every DAO!"),
    ("plurigrid", "StochFlow", "plurigrid/StochFlow", "Python", 4, 1, 0, "2024-03-20T23:34:57Z", "Python library implementing stochastic interpolant models"),
]

# kubeflow repos (top 15)
kubeflow_repos = [
    ("kubeflow", "sdk", "kubeflow/sdk", "Python", 127, 208, 181, "2026-07-23T00:21:14Z", "Universal Python SDK to run AI workloads on Kubernetes"),
    ("kubeflow", "trainer", "kubeflow/trainer", "Go", 2153, 993, 104, "2026-07-22T18:09:43Z", "Distributed AI Model Training and LLM Fine-Tuning on Kubernetes"),
    ("kubeflow", "pipelines", "kubeflow/pipelines", "Python", 4169, 2050, 445, "2026-07-22T11:38:06Z", "Machine Learning Pipelines for Kubeflow"),
    ("kubeflow", "kubeflow", "kubeflow/kubeflow", "", 15788, 2686, 0, "2026-07-10T11:31:26Z", "Machine Learning Toolkit for Kubernetes"),
    ("kubeflow", "spark-operator", "kubeflow/spark-operator", "Python", 3142, 1502, 107, "2026-07-17T23:31:17Z", "Kubernetes operator for managing the lifecycle of Apache Spark applications"),
    ("kubeflow", "mpi-operator", "kubeflow/mpi-operator", "Go", 530, 237, 102, "2026-07-22T23:00:11Z", "Kubernetes Operator for MPI-based applications"),
    ("kubeflow", "katib", "kubeflow/katib", "Python", 1692, 533, 104, "2026-07-22T02:20:01Z", "Automated Machine Learning on Kubernetes"),
    ("kubeflow", "kale", "kubeflow/kale", "Python", 695, 157, 49, "2026-07-22T19:55:15Z", "Kubeflow's superfood for Data Scientists"),
    ("kubeflow", "arena", "kubeflow/arena", "Go", 815, 196, 46, "2026-07-21T03:36:14Z", "A CLI for Kubeflow"),
    ("kubeflow", "community-distribution", "kubeflow/community-distribution", "YAML", 1029, 1072, 24, "2026-07-21T04:26:55Z", "Kubeflow Community Distribution"),
    ("kubeflow", "mcp-server", "kubeflow/mcp-server", "Python", 29, 36, 42, "2026-07-20T15:00:09Z", "MCP Server for AI-Assisted Development with Kubeflow Tools"),
    ("kubeflow", "hub", "kubeflow/hub", "Go", 178, 188, 29, "2026-07-22T08:20:38Z", "Model Registry for ML model developers"),
    ("kubeflow", "dashboard", "kubeflow/dashboard", "TypeScript", 16, 60, 95, "2026-07-22T20:02:27Z", "Kubeflow Central Dashboard"),
    ("kubeflow", "examples", "kubeflow/examples", "Jsonnet", 1461, 756, 111, "2025-04-14T01:54:52Z", "A repository to host extended examples and tutorials"),
    ("kubeflow", "mcp-apache-spark-history-server", "kubeflow/mcp-apache-spark-history-server", "Python", 183, 65, 20, "2026-07-16T20:57:58Z", "MCP Server and CLI for Apache Spark History Server"),
]

# Social graph repos
migalkin_repos = [
    ("migalkin", "NodePiece", "migalkin/NodePiece", "Python", 144, 21, 0, "2026-05-07T05:40:02Z", "Compositional and Parameter-Efficient Representations for Large Knowledge Graphs (ICLR'22)"),
    ("migalkin", "StarE", "migalkin/StarE", "Python", 89, 16, 1, "2026-04-16T14:12:45Z", "EMNLP 2020: Message Passing for Hyper-Relational Knowledge Graphs"),
    ("migalkin", "kgcourse2021", "migalkin/kgcourse2021", "HTML", 24, 8, 0, "2026-07-10T15:40:00Z", "Materials for Knowledge Graphs course"),
    ("migalkin", "NBFNet_mlx", "migalkin/NBFNet_mlx", "Python", 10, 1, 1, "2026-03-11T01:31:21Z", "Neural Bellman-Ford networks implemented in MLX for Apple Silicon"),
]

wasita_repos = [
    ("wasita", "wasita.github.io", "wasita/wasita.github.io", "Svelte", 1, 0, 8, "2026-07-21T15:55:45Z", "personal website"),
    ("wasita", "send2kobo", "wasita/send2kobo", "TypeScript", 1, 0, 0, "2026-05-19T02:59:26Z", "Website for sending books to your kobo e-reader"),
    ("wasita", "magic-garden", "wasita/magic-garden", "Python", 2, 1, 1, "2026-04-22T21:16:43Z", "bot for the magic garden discord activity game"),
]

austincstone_repos = [
    ("AustinCStone", "TextGAN", "AustinCStone/TextGAN", "Python", 92, 30, 5, "2025-03-03T13:26:32Z", "A generative adversarial network for text generation, written in TensorFlow"),
    ("AustinCStone", "byteruckus", "AustinCStone/byteruckus", "HTML", 0, 0, 0, "2026-07-15T05:19:33Z", ""),
    ("AustinCStone", "EpsteinSearch", "AustinCStone/EpsteinSearch", "Python", 0, 0, 0, "2026-02-11T01:10:57Z", ""),
]

djed_repos = [
    ("DJedamski", "kaggle_ncaa18", "DJedamski/kaggle_ncaa18", "Jupyter Notebook", 0, 0, 0, "2018-02-26T16:33:24Z", "Code for NCAA March Madness competition (2018)"),
]

kristine_repos = [
    ("kristinezheng", "kristinezheng.github.io", "kristinezheng/kristinezheng.github.io", "HTML", 0, 0, 0, "2026-07-01T20:57:48Z", ""),
]

m1sha_repos = [
    ("M1shaaa", "M1shaaa", "M1shaaa/M1shaaa", "", 0, 0, 0, "2026-02-04T19:32:04Z", "Config files for my GitHub profile"),
]

all_repo_groups = [
    teglon_repos, bmorphism_repos, zubyul_repos, plurigrid_repos,
    kubeflow_repos, migalkin_repos, wasita_repos, austincstone_repos,
    djed_repos, kristine_repos, m1sha_repos
]

inc_id = 1
repo_id = 1
snap_hash_base = "sweep_2026_07_23"

for group in all_repo_groups:
    for r in group:
        (org, repo_name, full_name, lang, stars, forks, issues, pushed, desc) = r
        trit, color, gf3_name = gf3(inc_id)
        # Insert world_increment
        con.execute("""
            INSERT INTO world_increments VALUES (?, now(), ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, [inc_id, trit, color, gf3_name, "github", org, "repo_snapshot", repo_name, org, f"{snap_hash_base}_{inc_id}"])
        # Insert repo_snapshot
        con.execute("""
            INSERT INTO repo_snapshots VALUES (?, now(), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, [repo_id, inc_id, org, repo_name, full_name, lang, stars, forks, issues, pushed, desc])
        inc_id += 1
        repo_id += 1

# ── APTOS SNAPSHOTS ──────────────────────────────────────────────────

aptos_data = [
    ("alice", "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b", 0.43643352),
    ("bob", "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d", 12.657007),
    ("A", "0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a", 0.051767),
    ("B", "0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13", 0.036256),
    ("C", "0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e", 0.010185),
    ("D", "0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1", 0.011629),
    ("E", "0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36", 0.009372),
    ("F", "0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71", 1.960516),
    ("G", "0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32", 0.000681),
    ("H", "0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f", 0.001681),
    ("I", "0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9", 0.000681),
    ("J", "0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54", 1.895093),
    ("K", "0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4", 0.161961),
    ("L", "0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9", 1.927269),
    ("M", "0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9", 0.112285),
    ("N", "0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c", 0.106121),
    ("O", "0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d", 0.210136),
    ("P", "0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948", 0.140136),
    ("Q", "0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9", 0.10324),
    ("R", "0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10", 0.090217),
    ("S", "0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386", 0.091788),
    ("T", "0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588", 0.073713),
    ("U", "0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956", 0.055773),
    ("V", "0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3", 0.04883299),
    ("W", "0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0", 0.040705),
    ("X", "0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d", 0.042577),
    ("Y", "0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4", 0.044449),
    ("Z", "0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c", 0.024268),
]

for world, addr, bal in aptos_data:
    con.execute("INSERT INTO aptos_snapshots VALUES (now(), ?, ?, ?)", [world, addr, bal])

# ── MULTISIG PROBES ──────────────────────────────────────────────────

multisig_data = [
    ("A-B", "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2, True),
    ("A-G", "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2, True),
    ("Y-Z", "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2, True),
    ("S-T", "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2, True),
    ("V-W", "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2, True),
]

for pair, addr, sigs, healthy in multisig_data:
    con.execute("INSERT INTO multisig_probes VALUES (now(), ?, ?, ?, ?)", [pair, addr, sigs, healthy])

# MNX unavailable - note it with a marker row
con.execute("INSERT INTO mnx_snapshots VALUES (now(), 'N/A', 'SPA_ONLY_NO_API', 'unavailable', 0.0, 0.0)")

# Verify counts
print("world_increments:", con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0])
print("repo_snapshots:", con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0])
print("aptos_snapshots:", con.execute("SELECT COUNT(*) FROM aptos_snapshots").fetchone()[0])
print("multisig_probes:", con.execute("SELECT COUNT(*) FROM multisig_probes").fetchone()[0])
print("mnx_snapshots:", con.execute("SELECT COUNT(*) FROM mnx_snapshots").fetchone()[0])

# Total APT
total_apt = con.execute("SELECT SUM(balance_apt) FROM aptos_snapshots").fetchone()[0]
print(f"Total APT across swarm: {total_apt:.6f}")

con.close()
print("DuckDB built successfully.")
