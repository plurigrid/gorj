#!/usr/bin/env python3
"""Populate world-increments DuckDB with GitHub sweep + Hamming swarm snapshot."""

import duckdb
import datetime

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"

def gf3(id_val):
    trit = id_val % 3
    if trit == 0:
        return (0, "ERGODIC", "#d3869b")
    elif trit == 1:
        return (1, "PLUS", "#b8bb26")
    else:
        return (-1, "MINUS", "#cc241d")

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
CREATE SEQUENCE IF NOT EXISTS increment_seq START 1
""")

con.execute("""
CREATE SEQUENCE IF NOT EXISTS repo_seq START 1
""")

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

ts = datetime.datetime.utcnow()

# --- Repo snapshot data ---
repo_rows = []

# TeglonLabs repos
teglon_repos = [
    ("TeglonLabs", "jank-crane", "TeglonLabs/jank-crane", "C++", 0, 0, 0, "2026-06-08T19:03:03Z", "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps"),
    ("TeglonLabs", "mathpix-gem", "TeglonLabs/mathpix-gem", "Ruby", 2, 0, 11, "2026-01-01T12:13:13Z", "Transform mathematical images to LaTeX with security-first design"),
    ("TeglonLabs", "coin-flip-mcp", "TeglonLabs/coin-flip-mcp", "JavaScript", 0, 2, 1, "2025-09-21T08:57:27Z", "MCP server for flipping coins with varying degrees of randomness"),
    ("TeglonLabs", "monad-mcp-server", "TeglonLabs/monad-mcp-server", "", 0, 0, 0, "2025-05-14T11:36:14Z", "Monad MCP Server"),
    ("TeglonLabs", "topoi", "TeglonLabs/topoi", "Python", 0, 0, 1, "2025-01-24T04:49:26Z", ""),
]
repo_rows.extend(teglon_repos)

# plurigrid repos (top 30 by pushed)
plurigrid_repos = [
    ("plurigrid", "gorj", "plurigrid/gorj", "Clojure", 1, 0, 1439, "2026-07-27T12:15:18Z", "forj + Rama topology nREPL routing + GF(3) gay trit coloring"),
    ("plurigrid", "place", "plurigrid/place", "TeX", 1, 2, 14, "2026-07-14T09:11:33Z", ""),
    ("plurigrid", "eirobri", "plurigrid/eirobri", "Clojure", 0, 0, 31, "2026-07-21T02:24:02Z", "EiRoBri replay world"),
    ("plurigrid", "asi", "plurigrid/asi", "HTML", 51, 11, 4, "2026-07-10T09:47:39Z", "everything is topological chemputer!"),
    ("plurigrid", "shrimp", "plurigrid/shrimp", "", 0, 0, 0, "2026-07-03T01:24:20Z", "Jank worked example: shrimp"),
    ("plurigrid", "nash-portal", "plurigrid/nash-portal", "Rust", 2, 2, 1, "2026-05-19T01:49:59Z", "NASH token TUI in the browser — ratzilla WASM + GeckoTerminal OHLCV candlesticks"),
    ("plurigrid", "zig-syrup", "plurigrid/zig-syrup", "Zig", 2, 2, 0, "2026-04-30T03:52:16Z", "High-performance Zig implementation of OCapN Syrup"),
    ("plurigrid", "asi-skills", "plurigrid/asi-skills", "Julia", 3, 0, 0, "2026-04-26T08:09:26Z", "69 skills with Galois Hole Type accessibility"),
    ("plurigrid", "nanoclj-zig", "plurigrid/nanoclj-zig", "Zig", 1, 1, 20, "2026-04-25T07:29:09Z", "NaN-boxed Clojure interpreter in Zig 0.15"),
    ("plurigrid", "bci-blue-share", "plurigrid/bci-blue-share", "JavaScript", 0, 0, 0, "2026-04-26T07:08:03Z", "BCI signal infrastructure"),
    ("plurigrid", "spi-race", "plurigrid/spi-race", "Swift", 0, 0, 0, "2026-04-21T19:31:56Z", "Splitmix Parallel Integrity"),
    ("plurigrid", "reafference", "plurigrid/reafference", "HTML", 0, 0, 0, "2026-04-16T05:21:49Z", "Reafference adaptation workspace"),
    ("plurigrid", "web-browser", "plurigrid/web-browser", "Rust", 0, 0, 0, "2026-04-10T02:54:47Z", "web-browser from prepostweb lineage"),
    ("plurigrid", "vivarium", "plurigrid/vivarium", "Clojure", 1, 0, 0, "2026-04-08T08:38:37Z", ""),
    ("plurigrid", "ontology", "plurigrid/ontology", "JavaScript", 8, 9, 16, "2025-05-27T18:18:34Z", "autopoietic ergodicity and embodied gradualism"),
    ("plurigrid", "microworlds", "plurigrid/microworlds", "Rust", 3, 5, 3, "2023-05-13T03:54:56Z", ""),
    ("plurigrid", "agent", "plurigrid/agent", "Python", 5, 1, 6, "2023-03-31T18:45:23Z", "Framework for agency amplification"),
    ("plurigrid", "vcg-auction", "plurigrid/vcg-auction", "Rust", 7, 3, 1, "2023-03-16T21:53:08Z", "a simple contract that performs a VCG auction"),
]
repo_rows.extend(plurigrid_repos)

# kubeflow repos (top active)
kubeflow_repos = [
    ("kubeflow", "dashboard", "kubeflow/dashboard", "TypeScript", 16, 61, 96, "2026-07-27T12:59:09Z", "Kubeflow Central Dashboard"),
    ("kubeflow", "mcp-server", "kubeflow/mcp-server", "Python", 29, 38, 33, "2026-07-27T12:56:52Z", "MCP Server for AI-Assisted Development"),
    ("kubeflow", "community", "kubeflow/community", "Jupyter Notebook", 195, 264, 14, "2026-07-27T12:12:01Z", "Information about the Kubeflow community"),
    ("kubeflow", "mpi-operator", "kubeflow/mpi-operator", "Go", 530, 238, 101, "2026-07-27T13:02:54Z", "Kubernetes Operator for MPI-based applications"),
    ("kubeflow", "pipelines", "kubeflow/pipelines", "Python", 4171, 2067, 465, "2026-07-27T03:53:12Z", "Machine Learning Pipelines for Kubeflow"),
    ("kubeflow", "trainer", "kubeflow/trainer", "Go", 2155, 997, 112, "2026-07-27T03:12:06Z", "Distributed AI Model Training"),
    ("kubeflow", "kubeflow", "kubeflow/kubeflow", "", 15792, 2687, 0, "2026-07-10T11:31:26Z", "Machine Learning Toolkit for Kubernetes"),
    ("kubeflow", "spark-operator", "kubeflow/spark-operator", "Python", 3142, 1506, 111, "2026-07-25T03:02:55Z", "Kubernetes operator for Apache Spark"),
    ("kubeflow", "katib", "kubeflow/katib", "Python", 1692, 531, 107, "2026-07-26T16:12:12Z", "Automated Machine Learning on Kubernetes"),
    ("kubeflow", "arena", "kubeflow/arena", "Go", 815, 196, 46, "2026-07-24T18:18:51Z", "A CLI for Kubeflow"),
]
repo_rows.extend(kubeflow_repos)

# bmorphism repos (top active)
bmorphism_repos = [
    ("bmorphism", "Gay.jl", "bmorphism/Gay.jl", "Julia", 2, 1, 188, "2026-07-27T02:46:40Z", "Wide-gamut color sampling with splittable determinism"),
    ("bmorphism", "gay-chat", "bmorphism/gay-chat", "Scheme", 0, 0, 0, "2026-07-14T20:59:56Z", "gay://chat operationalization over Spritely Brassica Chat"),
    ("bmorphism", "satreadout", "bmorphism/satreadout", "HTML", 0, 0, 0, "2026-06-20T13:05:41Z", "Machine-checked saturating non-Riemannian perceptual readout"),
    ("bmorphism", "ocaml-mcp-sdk", "bmorphism/ocaml-mcp-sdk", "OCaml", 61, 2, 0, "2026-03-16T05:24:25Z", "OCaml SDK for Model Context Protocol"),
    ("bmorphism", "anti-bullshit-mcp-server", "bmorphism/anti-bullshit-mcp-server", "JavaScript", 22, 7, 1, "2026-01-16T08:54:58Z", "MCP server for analyzing claims"),
    ("bmorphism", "say-mcp-server", "bmorphism/say-mcp-server", "JavaScript", 20, 9, 3, "2025-01-07T03:15:18Z", "MCP server for macOS text-to-speech"),
    ("bmorphism", "babashka-mcp-server", "bmorphism/babashka-mcp-server", "JavaScript", 19, 6, 3, "2025-01-05T11:09:42Z", "MCP server for Babashka"),
    ("bmorphism", "vibespace-mcp-go-ternary", "bmorphism/vibespace-mcp-go-ternary", "HTML", 0, 1, 3, "2026-01-11T12:50:40Z", "Go MCP experience for vibes with balanced ternary"),
    ("bmorphism", "manifold-mcp-server", "bmorphism/manifold-mcp-server", "JavaScript", 14, 9, 5, "2025-01-11T10:36:58Z", "MCP server for Manifold Markets prediction markets"),
    ("bmorphism", "penrose-mcp", "bmorphism/penrose-mcp", "JavaScript", 9, 4, 0, "2025-01-20T21:44:55Z", "Penrose server for Infinity-Topos"),
    ("bmorphism", "risc0-cosmwasm-example", "bmorphism/risc0-cosmwasm-example", "Rust", 23, 2, 1, "2022-10-20T23:50:40Z", "CosmWasm + zkVM RISC-V EFI template"),
]
repo_rows.extend(bmorphism_repos)

# zubyul repos
zubyul_repos = [
    ("zubyul", "voice-observatory", "zubyul/voice-observatory", "Python", 0, 0, 0, "2026-04-24T05:56:17Z", "Passive macOS TUI observing voice-download pathways"),
    ("zubyul", "ghostel-emacs-worlds", "zubyul/ghostel-emacs-worlds", "GLSL", 0, 0, 0, "2026-04-24T00:20:56Z", "Ghostty config + ghostel family + alice/bob emacs-mods"),
    ("zubyul", "from-possible-worlds", "zubyul/from-possible-worlds", "TeX", 0, 0, 1, "2026-07-18T12:02:57Z", ""),
    ("zubyul", "nash-tui", "zubyul/nash-tui", "Rust", 0, 0, 0, "2026-04-13T07:45:16Z", "NASH token TUI"),
    ("zubyul", "gay-world", "zubyul/gay-world", "Python", 1, 1, 0, "2026-03-26T04:03:39Z", "Goblin world builder"),
    ("zubyul", "Gay.jl", "zubyul/Gay.jl", "Julia", 0, 0, 0, "2026-03-28T11:30:01Z", "Wide-gamut color sampling with splittable determinism"),
    ("zubyul", "kinesis-kb360pro", "zubyul/kinesis-kb360pro", "Python", 0, 0, 0, "2026-03-26T10:29:40Z", "Claude Code skill for Kinesis Advantage360 Pro"),
]
repo_rows.extend(zubyul_repos)

# Social graph repos
social_repos = [
    ("migalkin", "NodePiece", "migalkin/NodePiece", "Python", 144, 21, 0, "2022-02-02T03:34:04Z", "Compositional Representations for Knowledge Graphs ICLR22"),
    ("migalkin", "StarE", "migalkin/StarE", "Python", 89, 16, 1, "2023-12-01T20:12:24Z", "Message Passing for Hyper-Relational Knowledge Graphs"),
    ("migalkin", "kgcourse2021", "migalkin/kgcourse2021", "HTML", 24, 8, 0, "2025-08-04T03:01:46Z", "Knowledge Graphs course materials"),
    ("migalkin", "NBFNet_mlx", "migalkin/NBFNet_mlx", "Python", 10, 1, 1, "2024-03-02T00:15:23Z", "Neural Bellman-Ford networks in MLX for Apple Silicon"),
    ("wasita", "wasita.github.io", "wasita/wasita.github.io", "Svelte", 1, 0, 8, "2026-07-21T15:52:20Z", "personal website"),
    ("wasita", "magic-garden", "wasita/magic-garden", "Python", 2, 1, 1, "2026-01-13T23:51:32Z", "discord bot for magic garden game"),
    ("wasita", "wm-cv", "wasita/wm-cv", "Svelte", 0, 0, 0, "2026-07-14T03:53:15Z", "Academic CV as single page web app"),
    ("AustinCStone", "TextGAN", "AustinCStone/TextGAN", "Python", 92, 30, 5, "2016-10-04T03:19:12Z", "Generative adversarial network for text generation"),
    ("AustinCStone", "byteruckus", "AustinCStone/byteruckus", "HTML", 0, 0, 0, "2026-07-15T05:19:30Z", ""),
    ("AustinCStone", "EpsteinSearch", "AustinCStone/EpsteinSearch", "Python", 0, 0, 0, "2026-02-11T01:10:54Z", ""),
]
repo_rows.extend(social_repos)

# Insert repo snapshots + world increments
print(f"Inserting {len(repo_rows)} repo snapshots...")
for i, row in enumerate(repo_rows):
    inc_id = con.execute("SELECT nextval('increment_seq')").fetchone()[0]
    repo_id = con.execute("SELECT nextval('repo_seq')").fetchone()[0]
    trit, color, name = gf3(inc_id)
    org, repo_name, full_name, lang, stars, forks, issues, pushed, desc = row

    # Insert world increment
    con.execute("""
        INSERT INTO world_increments (id, timestamp, gf3_trit, gf3_color, gf3_name,
            source_type, source_name, event_type, repo_name, actor, snapshot_hash)
        VALUES (?, ?, ?, ?, ?, 'github_repo', ?, 'repo_snapshot', ?, ?, ?)
    """, [inc_id, ts, trit, color, name, org, full_name, org,
          f"sweep-{ts.strftime('%Y%m%d')}-{inc_id}"])

    # Insert repo snapshot
    con.execute("""
        INSERT INTO repo_snapshots (id, timestamp, increment_id, org_or_user, repo_name,
            full_name, language, stars, forks, open_issues, pushed_at, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [repo_id, ts, inc_id, org, repo_name, full_name, lang or "", stars, forks, issues,
          pushed or "", desc or ""])

print("Repo snapshots inserted.")

# --- Aptos snapshots ---
aptos_data = [
    ("alice", "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b", 0.0),
    ("bob",   "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d", 0.0),
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

for world, addr, bal in aptos_data:
    con.execute("INSERT INTO aptos_snapshots (timestamp, world, address, balance_apt) VALUES (?, ?, ?, ?)",
                [ts, world, addr, bal])
print(f"Aptos snapshots inserted: {len(aptos_data)} accounts (all 0 APT — no CoinStore registered).")

# --- Multisig probes ---
multisig_data = [
    ("A-B", "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2, True),
    ("A-G", "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2, True),
    ("Y-Z", "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2, True),
    ("S-T", "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2, True),
    ("V-W", "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2, True),
]

for pair, addr, sigs, healthy in multisig_data:
    con.execute("INSERT INTO multisig_probes (timestamp, pair, address, sigs_required, healthy) VALUES (?, ?, ?, ?, ?)",
                [ts, pair, addr, sigs, healthy])
print("Multisig probes inserted: 5 probes (all healthy, 2-of-2).")

# Verify counts
world_count = con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0]
repo_count = con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0]
aptos_count = con.execute("SELECT COUNT(*) FROM aptos_snapshots").fetchone()[0]
multi_count = con.execute("SELECT COUNT(*) FROM multisig_probes").fetchone()[0]

print(f"\nDB summary:")
print(f"  world_increments: {world_count}")
print(f"  repo_snapshots: {repo_count}")
print(f"  aptos_snapshots: {aptos_count}")
print(f"  multisig_probes: {multi_count}")

con.close()
print("\nDone!")
