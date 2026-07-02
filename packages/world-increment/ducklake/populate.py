import duckdb, json, hashlib, os

DB = os.path.join(os.path.dirname(__file__), "world-increments.duckdb")
con = duckdb.connect(DB)

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

try:
    con.execute("CREATE SEQUENCE IF NOT EXISTS increment_seq START 1")
    con.execute("CREATE SEQUENCE IF NOT EXISTS repo_seq START 1")
except: pass

def gf3(id_):
    r = id_ % 3
    if r == 0: return (0, "#d3869b", "ERGODIC")
    if r == 1: return (1, "#b8bb26", "PLUS")
    return (-1, "#cc241d", "MINUS")

def sha8(s): return hashlib.sha256(s.encode()).hexdigest()[:8]

# ── Repo data ─────────────────────────────────────────────────────────────────

plurigrid = [
    ("asi","plurigrid/asi","HTML",29,8,4,"2026-06-29T03:15:56Z","everything is topological chemputer!"),
    ("place","plurigrid/place","TeX",1,1,12,"2026-06-29T20:40:59Z",None),
    ("eirobri","plurigrid/eirobri","Clojure",0,0,30,"2026-06-30T02:23:56Z","EiRoBri replay world"),
    ("nash-portal","plurigrid/nash-portal","Rust",2,3,1,"2026-05-19T01:49:59Z","NASH token TUI in the browser"),
    ("gorj","plurigrid/gorj","Clojure",0,0,913,"2026-07-02T09:14:50Z","forj + Rama topology nREPL routing + GF(3)"),
    ("zig-syrup","plurigrid/zig-syrup","Zig",2,2,0,"2026-04-30T03:52:16Z","High-performance Zig OCapN Syrup"),
    ("asi-skills","plurigrid/asi-skills","Julia",3,0,0,"2026-04-26T08:09:26Z","69 skills with Galois Hole Type accessibility"),
    ("bci-blue-share","plurigrid/bci-blue-share","JavaScript",0,0,0,"2026-04-26T07:08:03Z","BCI signal infrastructure"),
    ("nanoclj-zig","plurigrid/nanoclj-zig","Zig",1,1,20,"2026-04-25T07:29:09Z","NaN-boxed Clojure in Zig 0.15"),
    ("spi-race","plurigrid/spi-race","Swift",0,0,0,"2026-04-21T19:31:56Z","Splitmix Parallel Integrity"),
    ("reafference","plurigrid/reafference","HTML",0,0,0,"2026-04-16T05:21:49Z","Reafference adaptation workspace"),
    ("web-browser","plurigrid/web-browser","Rust",0,0,0,"2026-04-10T02:54:47Z","web-browser from prepostweb lineage"),
    ("vivarium","plurigrid/vivarium","Clojure",1,0,0,"2026-04-08T08:38:37Z",None),
    ("graded-optic","plurigrid/graded-optic","Haskell",0,0,0,"2026-02-08T16:10:16Z","Semiring-graded bidirectional processes"),
    ("forester","plurigrid/forester","XSLT",0,0,0,"2026-03-30T01:32:26Z","CatColab mathematical documentation forest"),
    ("gatomic","plurigrid/gatomic","Clojure",0,0,0,"2026-03-30T00:54:48Z","Deterministic color identity store"),
    ("lazygay","plurigrid/lazygay","Go",0,0,0,"2026-01-08T14:19:25Z","lazygit fork with Gay.jl commit coloring"),
    ("gay-rs","plurigrid/gay-rs","Rust",0,0,0,"2026-01-08T14:19:22Z","Rust crate for Gay.jl GF(3) trits"),
    ("ontology","plurigrid/ontology","JavaScript",8,9,16,"2025-05-27T18:18:34Z","autopoietic ergodicity and embodied gradualism"),
    ("Plurigraph","plurigrid/Plurigraph","JavaScript",3,5,4,"2025-01-05T08:39:09Z","Plurigrid knowledge base for Obsidian.md"),
    ("microworlds","plurigrid/microworlds","Rust",3,5,3,"2023-05-13T03:54:56Z","👽"),
    ("agent","plurigrid/agent","Python",5,1,6,"2023-03-31T18:45:23Z","Framework for agency amplification"),
    ("vcg-auction","plurigrid/vcg-auction","Rust",7,2,1,"2023-03-16T21:53:08Z","simple VCG auction contract"),
    ("StochFlow","plurigrid/StochFlow","Python",4,1,0,"2024-03-20T23:34:57Z","stochastic interpolant models"),
    ("act","plurigrid/act","Python",3,1,4,"2024-07-26T08:27:08Z","building blocks for cognitive category theory"),
    ("aptos-wallet-ruby","plurigrid/aptos-wallet-ruby","Ruby",1,0,0,"2025-09-30T22:47:22Z",None),
    ("duck-kanban","plurigrid/duck-kanban","Rust",1,0,0,"2025-09-26T20:18:38Z","Duck intelligence kanban"),
    ("nblm-flashcards","plurigrid/nblm-flashcards","Hy",0,0,0,"2026-03-26T08:23:01Z","NotebookLM Enterprise flashcard pipeline"),
    ("gemini-agent","plurigrid/gemini-agent","Python",0,0,0,"2026-02-19T06:39:16Z",None),
    ("shepherd","plurigrid/shepherd","Scheme",0,0,0,"2026-01-23T07:47:28Z","Spritely Shepherd mirror"),
]

kubeflow = [
    ("pipelines","kubeflow/pipelines","Python",4167,2020,412,"2026-07-02T09:33:54Z","ML Pipelines for Kubeflow"),
    ("kubeflow","kubeflow/kubeflow","",15756,2684,0,"2026-07-02T02:01:18Z","Machine Learning Toolkit for Kubernetes"),
    ("trainer","kubeflow/trainer","Go",2128,974,144,"2026-07-02T07:15:09Z","Distributed AI Model Training"),
    ("spark-operator","kubeflow/spark-operator","Python",3130,1495,102,"2026-07-01T11:51:51Z","Kubernetes operator for Apache Spark"),
    ("katib","kubeflow/katib","Python",1688,529,114,"2026-07-01T11:51:44Z","Automated Machine Learning on Kubernetes"),
    ("kale","kubeflow/kale","Python",694,156,37,"2026-07-01T16:39:54Z","Kubeflow superfood for Data Scientists"),
    ("mpi-operator","kubeflow/mpi-operator","Go",529,236,102,"2026-07-01T17:34:18Z","Kubernetes Operator for MPI"),
    ("arena","kubeflow/arena","Go",814,194,48,"2026-07-01T03:54:55Z","CLI for Kubeflow"),
    ("community-distribution","kubeflow/community-distribution","YAML",1028,1067,27,"2026-06-30T15:22:51Z","Kubeflow Community Distribution"),
    ("sdk","kubeflow/sdk","Python",123,187,138,"2026-07-02T04:38:51Z","Universal Python SDK for AI workloads on Kubernetes"),
    ("hub","kubeflow/hub","Go",174,183,35,"2026-07-01T18:24:29Z","Model Registry"),
    ("mcp-apache-spark-history-server","kubeflow/mcp-apache-spark-history-server","Python",179,66,19,"2026-07-01T21:23:15Z","MCP Server for Spark History"),
    ("website","kubeflow/website","HTML",184,923,30,"2026-06-30T22:04:26Z","Kubeflow Website"),
    ("examples","kubeflow/examples","Jsonnet",1460,756,111,"2026-06-16T17:59:01Z","Extended examples and tutorials"),
    ("mcp-server","kubeflow/mcp-server","Python",19,25,32,"2026-06-29T16:55:51Z","MCP Server for Kubeflow"),
]

teglon = [
    ("jank-crane","TeglonLabs/jank-crane","C++",0,0,0,"2026-06-08T19:03:37Z","crane-jank converged-IR hub"),
    ("mathpix-gem","TeglonLabs/mathpix-gem","Ruby",2,0,11,"2026-01-01T12:13:16Z","Mathematical images to LaTeX"),
    ("coin-flip-mcp","TeglonLabs/coin-flip-mcp","JavaScript",0,2,1,"2025-03-16T01:31:45Z","MCP server for flipping coins"),
    ("monad-mcp-server","TeglonLabs/monad-mcp-server","",0,0,0,"2025-05-14T17:53:01Z","Monad MCP Server"),
    ("topoi","TeglonLabs/topoi","Python",0,0,1,"2025-01-24T06:47:38Z",None),
]

bmorphism_repos = [
    ("satreadout","bmorphism/satreadout","HTML",0,0,0,"2026-06-20T13:05:44Z","Machine-checked saturating non-Riemannian perceptual readout"),
    ("Gay.jl","bmorphism/Gay.jl","Julia",2,1,187,"2026-06-20T14:21:55Z","Wide-gamut color sampling with splittable determinism"),
    ("bci-preview","bmorphism/bci-preview","HTML",0,0,0,"2026-06-20T00:20:47Z","Stable redirect front for bci.place"),
    ("world","bmorphism/world","Python",0,0,0,"2026-06-02T06:49:06Z","Local worlds launcher for SA3"),
    ("nanoclj-zig","bmorphism/nanoclj-zig","Zig",1,0,0,"2026-06-10T16:00:16Z","nanoclj-zig"),
    ("ocaml-mcp-sdk","bmorphism/ocaml-mcp-sdk","OCaml",61,2,0,"2026-05-08T16:50:34Z","OCaml SDK for Model Context Protocol"),
    ("flox-mcp-bb","bmorphism/flox-mcp-bb","Clojure",0,0,0,"2026-06-05T17:53:47Z","Open-source MCP server for Flox"),
    ("anti-bullshit-mcp-server","bmorphism/anti-bullshit-mcp-server","JavaScript",23,7,1,"2026-02-05T15:46:59Z","MCP server for analyzing claims"),
    ("babashka-mcp-server","bmorphism/babashka-mcp-server","JavaScript",19,6,3,"2026-06-05T13:16:11Z","MCP server for Babashka"),
    ("say-mcp-server","bmorphism/say-mcp-server","JavaScript",20,9,3,"2026-03-19T23:11:59Z","MCP server for macOS TTS"),
    ("manifold-mcp-server","bmorphism/manifold-mcp-server","JavaScript",14,9,5,"2026-04-15T19:54:28Z","MCP server for Manifold Markets"),
    ("penrose-mcp","bmorphism/penrose-mcp","JavaScript",9,4,0,"2026-06-24T15:36:16Z","Penrose server for Infinity-Topos"),
    ("whale","bmorphism/whale","MATLAB",2,0,0,"2026-04-20T15:04:09Z","omniglot + sperm whale codas"),
    ("risc0-cosmwasm-example","bmorphism/risc0-cosmwasm-example","Rust",23,2,1,"2025-05-21T13:35:37Z","CosmWasm + zkVM RISC-V EFI"),
    ("shitcoin","bmorphism/shitcoin","Python",5,0,0,"2026-04-08T08:07:17Z","denom for cw20 assets IBC"),
    ("marginalia-mcp-server","bmorphism/marginalia-mcp-server","JavaScript",8,6,0,"2026-03-27T16:55:55Z","MCP server for marginalia"),
    ("zig-syrup","bmorphism/zig-syrup","Zig",0,0,0,"2026-03-28T21:42:35Z","OCapN Syrup encoder/decoder in Zig"),
    ("hypernym-mcp-server","bmorphism/hypernym-mcp-server","JavaScript",6,5,0,"2025-10-24T09:21:53Z","hypernym MCP server"),
]

zubyul_repos = [
    ("voice-observatory","zubyul/voice-observatory","Python",0,0,0,"2026-04-24T05:56:20Z","Passive macOS TUI for voice-download pathways"),
    ("ghostel-emacs-worlds","zubyul/ghostel-emacs-worlds","GLSL",0,0,0,"2026-04-24T00:21:00Z","Ghostty config + ghostel family"),
    ("Gay.jl","zubyul/Gay.jl","Julia",0,0,0,"2026-03-28T11:30:07Z","Wide-gamut color sampling fork"),
    ("kinesis-kb360pro","zubyul/kinesis-kb360pro","Python",0,0,0,"2026-03-26T10:29:44Z","Kinesis Advantage360 Pro keyboard skill"),
    ("tilelang-kernels","zubyul/tilelang-kernels","Python",0,0,0,"2026-03-16T02:31:16Z","TileLang GPU kernels for GF(3)"),
    ("gay-world","zubyul/gay-world","Python",1,1,0,"2026-04-05T06:54:03Z","Goblin world builder"),
    ("big-bad-plurigrid-quiz","zubyul/big-bad-plurigrid-quiz","Emacs Lisp",0,0,0,"2026-04-09T18:51:35Z","27 flashcards from plurigrid activity"),
    ("hue-world","zubyul/hue-world","JavaScript",0,0,0,"2026-01-08T00:00:00Z","Terminal Vibe Snipe puzzle game"),
    ("multiplayer-emacs","zubyul/multiplayer-emacs","HTML",0,0,0,"2026-01-01T00:00:00Z","Multiplayer world: Emacs split-pane"),
    ("jonikas_lab_data_analysis_misc","zubyul/jonikas_lab_data_analysis_misc","Jupyter Notebook",2,0,0,"2026-03-26T09:05:21Z","scripts for large genetic sequence data"),
    ("Nikolova_lab_data_analysis","zubyul/Nikolova_lab_data_analysis","R",2,0,0,"2026-03-26T09:05:23Z","undergraduate thesis - Human Connectome Project"),
    ("WGCNA","zubyul/WGCNA","HTML",2,0,0,"2026-03-26T09:05:26Z","weighted gene correlation network analysis"),
]

social_repos = [
    # migalkin
    ("NodePiece","migalkin/NodePiece","Python",144,21,0,"2026-05-07T05:40:02Z","Compositional Representations for Large KGs (ICLR22)"),
    ("StarE","migalkin/StarE","Python",89,16,1,"2026-04-16T14:12:45Z","Message Passing for Hyper-Relational KGs (EMNLP20)"),
    ("NBFNet_mlx","migalkin/NBFNet_mlx","Python",10,1,1,"2026-03-11T01:31:21Z","Neural Bellman-Ford networks in MLX"),
    ("kgcourse2021","migalkin/kgcourse2021","HTML",25,9,0,"2026-02-16T05:16:08Z","Knowledge Graphs course materials"),
    ("RWL","migalkin/RWL","Python",8,1,0,"2026-05-28T20:19:20Z","Weisfeiler and Leman Go Relational"),
    # DJedamski
    ("kaggle_ncaa18","DJedamski/kaggle_ncaa18","Jupyter Notebook",0,0,0,"2018-02-26T16:33:24Z","NCAA March Madness 2018"),
    ("Kaggle","DJedamski/Kaggle","",1,0,0,"2023-04-21T01:42:35Z","Kaggle projects"),
    # wasita
    ("wasita.github.io","wasita/wasita.github.io","Svelte",1,0,8,"2026-07-02T01:40:18Z","personal website"),
    ("magic-garden","wasita/magic-garden","Python",2,1,1,"2026-04-22T21:16:43Z","Discord magic garden auto-bot"),
    ("wm-cv","wasita/wm-cv","Svelte",0,0,0,"2026-05-13T05:29:08Z","Academic CV as single page web app"),
    ("send2kobo","wasita/send2kobo","TypeScript",1,0,0,"2026-05-19T02:59:26Z","Website for sending books to kobo"),
    # kristinezheng
    ("kristinezheng.github.io","kristinezheng/kristinezheng.github.io","HTML",0,0,0,"2026-07-01T20:57:48Z","personal site"),
    ("lookit-jenga","kristinezheng/lookit-jenga","Jupyter Notebook",0,0,0,"2024-05-16T18:29:05Z","Lookit study for 9.85"),
    # M1shaaa
    ("M1shaaa","M1shaaa/M1shaaa","",0,0,0,"2026-02-04T19:32:04Z","GitHub profile config"),
    ("lab-bookshelf-","M1shaaa/lab-bookshelf-","TypeScript",0,0,0,"2024-12-31T05:11:18Z","lab bookshelf"),
    # AustinCStone
    ("TextGAN","AustinCStone/TextGAN","Python",92,30,5,"2025-03-03T13:26:32Z","GAN for text generation in TensorFlow"),
    ("StereoVisionMRF","AustinCStone/StereoVisionMRF","Python",11,4,0,"2026-04-01T07:39:41Z","Stereo vision depth inference with MRF"),
    ("EpsteinSearch","AustinCStone/EpsteinSearch","Python",0,0,0,"2026-02-11T01:10:57Z","Epstein search tool"),
]

all_source_groups = [
    ("plurigrid", "org", plurigrid),
    ("kubeflow", "org", kubeflow),
    ("TeglonLabs", "org", teglon),
    ("bmorphism", "user", bmorphism_repos),
    ("zubyul", "user", zubyul_repos),
    ("social_graph", "users", social_repos),
]

increment_id = 1
repo_id = 1

for source_name, source_type, repos in all_source_groups:
    for r in repos:
        name, full_name, lang, stars, forks, issues, pushed_at, desc = r
        trit, color, gf3name = gf3(increment_id)
        snap_hash = sha8(full_name + pushed_at)
        con.execute("""INSERT INTO world_increments VALUES (?,now(),?,?,?,?,?,?,?,?,?)""",
            [increment_id, trit, color, gf3name, source_type, source_name,
             "repo_push", name, None, snap_hash])
        con.execute("""INSERT INTO repo_snapshots VALUES (?,now(),?,?,?,?,?,?,?,?,?,?)""",
            [repo_id, increment_id, source_name, name, full_name, lang or "",
             stars, forks, issues, pushed_at, desc or ""])
        increment_id += 1
        repo_id += 1

print(f"Inserted {increment_id-1} increments, {repo_id-1} repo snapshots")

# ── Aptos snapshots ────────────────────────────────────────────────────────────

aptos_data = [
    ("alice","0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b",0.0),
    ("bob","0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d",0.0),
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
print(f"Inserted {len(aptos_data)} aptos snapshots")

# ── Multisig probes ────────────────────────────────────────────────────────────

multisig_data = [
    ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2,True),
    ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2,True),
    ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2,True),
    ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2,True),
    ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2,True),
]
for pair, addr, sigs, healthy in multisig_data:
    con.execute("INSERT INTO multisig_probes VALUES (now(),?,?,?,?)", [pair, addr, sigs, healthy])
print(f"Inserted {len(multisig_data)} multisig probes")

# MNX unavailable - no rows inserted (Vercel auth protected)

con.close()
print("Done. DB:", DB)
