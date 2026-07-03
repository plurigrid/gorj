#!/usr/bin/env python3
import duckdb, json, hashlib

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
con = duckdb.connect(DB)

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
con.execute("CREATE SEQUENCE IF NOT EXISTS increment_seq START 1")
con.execute("CREATE SEQUENCE IF NOT EXISTS repo_seq START 1")
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

def gf3(id_val):
    t = id_val % 3
    if t == 0:
        return (0, "#d3869b", "ERGODIC")
    elif t == 1:
        return (1, "#b8bb26", "PLUS")
    else:
        return (-1, "#cc241d", "MINUS")

# All repo data collected
repos = [
  # plurigrid
  ("org", "plurigrid", "shrimp", "plurigrid/shrimp", None, 0, 0, 0, "2026-07-03", "Jank worked example: shrimp"),
  ("org", "plurigrid", "asi", "plurigrid/asi", "HTML", 28, 8, 4, "2026-07-02", "everything is topological chemputer!"),
  ("org", "plurigrid", "place", "plurigrid/place", "TeX", 1, 1, 12, "2026-06-27", None),
  ("org", "plurigrid", "gorj", "plurigrid/gorj", "Clojure", 0, 0, 945, "2026-05-08", "forj + Rama topology nREPL routing + GF(3) gay trit coloring"),
  ("org", "plurigrid", "nash-portal", "plurigrid/nash-portal", "Rust", 2, 3, 1, "2026-05-19", "NASH token TUI in the browser"),
  ("org", "plurigrid", "nanoclj-zig", "plurigrid/nanoclj-zig", "Zig", 1, 1, 20, "2026-04-25", "NaN-boxed Clojure interpreter in Zig"),
  ("org", "plurigrid", "ontology", "plurigrid/ontology", "JavaScript", 8, 9, 16, "2026-05-09", "autopoietic ergodicity and embodied gradualism"),
  ("org", "plurigrid", "vcg-auction", "plurigrid/vcg-auction", "Rust", 7, 2, 1, "2025-12-16", "simple contract that performs a VCG auction"),
  ("org", "plurigrid", "microworlds", "plurigrid/microworlds", "Rust", 3, 5, 3, "2024-03-14", None),
  ("org", "plurigrid", "agent", "plurigrid/agent", "Python", 5, 1, 6, "2024-10-16", "Framework for agency amplification"),
  # kubeflow top
  ("org", "kubeflow", "kubeflow", "kubeflow/kubeflow", None, 15760, 2682, 0, "2026-07-03", "Machine Learning Toolkit for Kubernetes"),
  ("org", "kubeflow", "pipelines", "kubeflow/pipelines", "Python", 4169, 2021, 414, "2026-07-03", "Machine Learning Pipelines for Kubeflow"),
  ("org", "kubeflow", "spark-operator", "kubeflow/spark-operator", "Python", 3132, 1496, 103, "2026-07-03", "Kubernetes operator for managing the lifecycle of Apache Spark"),
  ("org", "kubeflow", "trainer", "kubeflow/trainer", "Go", 2129, 975, 147, "2026-07-03", "Distributed AI Model Training and LLM Fine-Tuning on Kubernetes"),
  ("org", "kubeflow", "katib", "kubeflow/katib", "Python", 1689, 529, 114, "2026-07-03", "Automated Machine Learning on Kubernetes"),
  ("org", "kubeflow", "examples", "kubeflow/examples", "Jsonnet", 1460, 756, 111, "2026-06-16", "A repository to host extended examples and tutorials"),
  ("org", "kubeflow", "arena", "kubeflow/arena", "Go", 814, 194, 45, "2026-07-03", "A CLI for Kubeflow"),
  ("org", "kubeflow", "kale", "kubeflow/kale", "Python", 695, 156, 38, "2026-07-03", "Kubeflow's superfood for Data Scientists"),
  ("org", "kubeflow", "hub", "kubeflow/hub", "Go", 173, 184, 33, "2026-07-03", "Model Registry for ML model developers"),
  ("org", "kubeflow", "mcp-apache-spark-history-server", "kubeflow/mcp-apache-spark-history-server", "Python", 180, 66, 19, "2026-07-03", "MCP Server and CLI for Apache Spark History Server"),
  # TeglonLabs
  ("org", "TeglonLabs", "jank-crane", "TeglonLabs/jank-crane", "C++", 0, 0, 0, "2026-06-08", "crane-jank converged-IR hub"),
  ("org", "TeglonLabs", "mathpix-gem", "TeglonLabs/mathpix-gem", "Ruby", 2, 0, 11, "2026-01-01", "Transform mathematical images to LaTeX"),
  ("org", "TeglonLabs", "coin-flip-mcp", "TeglonLabs/coin-flip-mcp", "JavaScript", 0, 2, 1, "2025-03-16", "MCP server for flipping coins"),
  ("org", "TeglonLabs", "topoi", "TeglonLabs/topoi", "Python", 0, 0, 1, "2025-01-24", None),
  # bmorphism top
  ("user", "bmorphism", "Gay.jl", "bmorphism/Gay.jl", "Julia", 2, 1, 187, "2026-06-20", "Wide-gamut color sampling with splittable determinism"),
  ("user", "bmorphism", "satreadout", "bmorphism/satreadout", "HTML", 0, 0, 0, "2026-06-20", "Machine-checked saturating non-Riemannian perceptual readout"),
  ("user", "bmorphism", "anti-bullshit-mcp-server", "bmorphism/anti-bullshit-mcp-server", "JavaScript", 23, 7, 1, "2026-02-05", "MCP server for analyzing claims"),
  ("user", "bmorphism", "ocaml-mcp-sdk", "bmorphism/ocaml-mcp-sdk", "OCaml", 61, 2, 0, "2026-05-08", "OCaml SDK for Model Context Protocol"),
  ("user", "bmorphism", "penrose-mcp", "bmorphism/penrose-mcp", "JavaScript", 9, 4, 0, "2026-06-24", "Penrose server for the Infinity-Topos environment"),
  ("user", "bmorphism", "babashka-mcp-server", "bmorphism/babashka-mcp-server", "JavaScript", 19, 6, 3, "2026-06-05", "MCP server for interacting with Babashka"),
  ("user", "bmorphism", "risc0-cosmwasm-example", "bmorphism/risc0-cosmwasm-example", "Rust", 23, 2, 1, "2025-05-21", "CosmWasm + zkVM RISC-V EFI template"),
  ("user", "bmorphism", "say-mcp-server", "bmorphism/say-mcp-server", "JavaScript", 20, 9, 3, "2026-03-19", "MCP server for macOS text-to-speech"),
  # zubyul top
  ("user", "zubyul", "voice-observatory", "zubyul/voice-observatory", "Python", 0, 0, 0, "2026-04-24", "Passive macOS TUI observing voice-download pathways"),
  ("user", "zubyul", "Gay.jl", "zubyul/Gay.jl", "Julia", 0, 0, 0, "2026-03-28", "Wide-gamut color sampling with splittable determinism"),
  ("user", "zubyul", "gay-world", "zubyul/gay-world", "Python", 1, 1, 0, "2026-04-05", "Goblin world builder"),
  ("user", "zubyul", "big-bad-plurigrid-quiz", "zubyul/big-bad-plurigrid-quiz", "Emacs Lisp", 0, 0, 0, "2026-04-09", "27 flashcards from plurigrid activity"),
  # social graph
  ("user", "migalkin", "NodePiece", "migalkin/NodePiece", "Python", 144, 21, 0, "2026-05-07", "Compositional and Parameter-Efficient Representations (ICLR'22)"),
  ("user", "migalkin", "StarE", "migalkin/StarE", "Python", 89, 16, 1, "2026-04-16", "Message Passing for Hyper-Relational Knowledge Graphs (EMNLP 2020)"),
  ("user", "migalkin", "NBFNet_mlx", "migalkin/NBFNet_mlx", "Python", 10, 1, 1, "2026-03-11", "Neural Bellman-Ford networks in MLX"),
  ("user", "wasita", "wasita.github.io", "wasita/wasita.github.io", "Svelte", 1, 0, 8, "2026-07-02", "personal website"),
  ("user", "wasita", "send2kobo", "wasita/send2kobo", "TypeScript", 1, 0, 0, "2026-05-19", "Website for sending books to kobo"),
  ("user", "AustinCStone", "TextGAN", "AustinCStone/TextGAN", "Python", 92, 30, 5, "2025-03-03", "A generative adversarial network for text generation"),
  ("user", "AustinCStone", "StereoVisionMRF", "AustinCStone/StereoVisionMRF", "Python", 11, 4, 0, "2026-04-01", "Recover 3D geometry from videos"),
  ("user", "DJedamski", "kaggle_ncaa18", "DJedamski/kaggle_ncaa18", "Jupyter Notebook", 0, 0, 0, "2018-02-26", "NCAA March Madness competition (2018)"),
  ("user", "kristinezheng", "kristinezheng.github.io", "kristinezheng/kristinezheng.github.io", "HTML", 0, 0, 0, "2026-07-01", None),
  ("user", "M1shaaa", "M1shaaa", "M1shaaa/M1shaaa", None, 0, 0, 0, "2026-02-04", "Config files for my GitHub profile"),
]

inc_id = 1
repo_id = 1
for (src_type, src_name, repo_name, full_name, lang, stars, forks, issues, pushed_at, desc) in repos:
    trit, color, name = gf3(inc_id)
    h = hashlib.sha256(f"{src_name}/{repo_name}".encode()).hexdigest()[:12]
    con.execute("""
      INSERT INTO world_increments (id, gf3_trit, gf3_color, gf3_name, source_type, source_name, event_type, repo_name, actor, snapshot_hash)
      VALUES (?, ?, ?, ?, ?, ?, 'repo_snapshot', ?, ?, ?)
    """, [inc_id, trit, color, name, src_type, src_name, full_name, src_name, h])
    con.execute("""
      INSERT INTO repo_snapshots (id, increment_id, org_or_user, repo_name, full_name, language, stars, forks, open_issues, pushed_at, description)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [repo_id, inc_id, src_name, repo_name, full_name, lang, stars, forks, issues, pushed_at, desc])
    inc_id += 1
    repo_id += 1

# Aptos snapshots
aptos_data = [
  ("alice", "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b", 0.0),
  ("bob", "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d", 0.0),
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
    con.execute("INSERT INTO aptos_snapshots (world, address, balance_apt) VALUES (?, ?, ?)", [world, addr, bal])

# Multisig probes
multisig_data = [
    ("A-B", "0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003", 2, True),
    ("A-G", "0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096", 2, True),
    ("Y-Z", "0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883", 2, True),
    ("S-T", "0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883", 2, True),
    ("V-W", "0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d", 2, True),
]
for pair, addr, sigs, healthy in multisig_data:
    con.execute("INSERT INTO multisig_probes (pair, address, sigs_required, healthy) VALUES (?, ?, ?, ?)", [pair, addr, sigs, healthy])

con.commit()

# Summary query
print("=== world_increments ===")
print(con.execute("SELECT COUNT(*), MIN(id), MAX(id) FROM world_increments").fetchdf().to_string())
print("\n=== repo_snapshots top by stars ===")
print(con.execute("SELECT org_or_user, repo_name, stars FROM repo_snapshots ORDER BY stars DESC LIMIT 10").fetchdf().to_string())
print("\n=== aptos_snapshots ===")
print(con.execute("SELECT COUNT(*), SUM(balance_apt) FROM aptos_snapshots").fetchdf().to_string())
print("\n=== multisig_probes ===")
print(con.execute("SELECT * FROM multisig_probes").fetchdf().to_string())
print("\n=== GF3 distribution ===")
print(con.execute("SELECT gf3_name, gf3_color, COUNT(*) as cnt FROM world_increments GROUP BY gf3_name, gf3_color").fetchdf().to_string())

con.close()
print("\nDB built successfully.")
