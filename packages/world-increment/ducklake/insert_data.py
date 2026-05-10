#!/usr/bin/env python3
"""Insert GitHub sweep + Aptos snapshot data into DuckDB."""
import duckdb, hashlib, json
from datetime import datetime

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
con = duckdb.connect(DB)

NOW = datetime.utcnow().isoformat()

def gf3(id_):
    r = id_ % 3
    if r == 0:   return 0, "#d3869b", "ERGODIC"
    elif r == 1: return 1, "#b8bb26", "PLUS"
    else:        return -1, "#cc241d", "MINUS"

def snap_hash(s): return hashlib.sha256(s.encode()).hexdigest()[:16]

# ── repo data ──────────────────────────────────────────────────────────────────
# (name, full_name, language, stars, forks, open_issues, pushed_at, description)
REPOS = {
    "plurigrid": [
        ("gorj","plurigrid/gorj","Clojure",0,0,133,"2026-05-10T08:22:19Z","forj + Rama topology nREPL routing + GF(3) gay trit coloring"),
        ("zig-syrup","plurigrid/zig-syrup","Zig",2,2,0,"2026-04-30T03:52:16Z","High-performance Zig implementation of OCapN Syrup"),
        ("asi","plurigrid/asi","HTML",21,5,4,"2026-04-26T08:51:41Z","everything is topological chemputer!"),
        ("nash-portal","plurigrid/nash-portal","Rust",2,2,0,"2026-04-26T08:50:56Z","NASH token TUI in the browser"),
        ("horse","plurigrid/horse","TeX",1,1,9,"2026-05-07T04:35:12Z",""),
        ("asi-skills","plurigrid/asi-skills","Julia",3,1,0,"2026-04-26T08:09:26Z","69 skills with Galois Hole Type accessibility"),
        ("bci-blue-share","plurigrid/bci-blue-share","JavaScript",0,0,0,"2026-04-26T07:08:03Z","BCI signal infrastructure"),
        ("nanoclj-zig","plurigrid/nanoclj-zig","Zig",1,2,20,"2026-04-25T07:29:09Z","NaN-boxed Clojure interpreter in Zig"),
        ("spi-race","plurigrid/spi-race","Swift",0,0,0,"2026-04-21T19:31:56Z","Splitmix Parallel Integrity"),
        ("reafference","plurigrid/reafference","HTML",0,0,0,"2026-04-16T05:21:49Z","Reafference adaptation workspace"),
        ("web-browser","plurigrid/web-browser","Rust",0,0,0,"2026-04-10T02:54:47Z","web-browser from prepostweb lineage"),
        ("vivarium","plurigrid/vivarium","Clojure",1,0,0,"2026-04-08T08:38:37Z",""),
        ("gatomic","plurigrid/gatomic","Clojure",0,0,0,"2026-03-30T00:54:48Z","Deterministic color identity store with sonification"),
        ("nblm-flashcards","plurigrid/nblm-flashcards","Hy",0,0,0,"2026-03-26T08:23:01Z","NotebookLM Enterprise flashcard pipeline"),
        ("graded-optic","plurigrid/graded-optic","Haskell",0,0,0,"2026-02-08T16:10:16Z","Semiring-graded bidirectional processes"),
        ("lazygay","plurigrid/lazygay","Go",0,0,0,"2026-01-08T14:19:25Z","lazygit fork with Gay.jl deterministic commit coloring"),
        ("gay-rs","plurigrid/gay-rs","Rust",0,0,0,"2026-01-08T14:19:22Z","Rust crate for Gay.jl deterministic coloring"),
        ("lazybjj","plurigrid/lazybjj","Rust",0,0,0,"2026-01-08T14:19:19Z","TUI for jj with Gay.jl GF(3) coloring"),
        ("ontology","plurigrid/ontology","JavaScript",8,9,16,"2025-05-27T18:18:34Z","autopoietic ergodicity and embodied gradualism"),
        ("Plurigraph","plurigrid/Plurigraph","JavaScript",2,5,4,"2025-01-05T08:39:09Z","Plurigrid knowledge base for Obsidian.md"),
        ("act","plurigrid/act","Python",3,1,4,"2024-07-26T08:27:08Z","building blocks for cognitive category theory"),
        ("StochFlow","plurigrid/StochFlow","Python",4,1,0,"2024-03-20T23:34:57Z","stochastic interpolant models"),
        ("microworlds","plurigrid/microworlds","Rust",3,5,3,"2023-05-13T03:54:56Z",""),
        ("agent","plurigrid/agent","Python",5,1,6,"2023-03-31T18:45:23Z","Framework for agency amplification"),
        ("vcg-auction","plurigrid/vcg-auction","Rust",7,2,1,"2023-03-16T21:53:08Z","simple VCG auction contract"),
        ("grid","plurigrid/grid","TypeScript",2,1,1,"2023-01-02T11:55:55Z","Plurigrid Testnet #0"),
        ("VPP","plurigrid/VPP","Julia",0,1,0,"2023-01-11T18:41:07Z","Hyperreal Power Plant"),
        ("duck-kanban","plurigrid/duck-kanban","Rust",1,0,0,"2025-09-26T20:18:38Z","Duck intelligence kanban system"),
        ("aptos-wallet-ruby","plurigrid/aptos-wallet-ruby","Ruby",1,0,0,"2025-09-30T22:47:22Z",""),
        ("post-web","plurigrid/post-web","Svelte",0,0,0,"2023-06-18T00:24:24Z",""),
    ],
    "kubeflow": [
        ("trainer","kubeflow/trainer","Go",2097,947,111,"2026-05-09T17:39:35Z","Distributed AI Model Training on Kubernetes"),
        ("pipelines","kubeflow/pipelines","Python",4137,1990,497,"2026-05-08T21:33:13Z","Machine Learning Pipelines for Kubeflow"),
        ("kubeflow","kubeflow/kubeflow","",15628,2647,2,"2026-05-07T13:46:41Z","Machine Learning Toolkit for Kubernetes"),
        ("spark-operator","kubeflow/spark-operator","Python",3125,1480,89,"2026-05-08T16:09:29Z","Kubernetes operator for Apache Spark"),
        ("katib","kubeflow/katib","Python",1683,522,124,"2026-05-09T12:21:57Z","Automated Machine Learning on Kubernetes"),
        ("manifests","kubeflow/manifests","YAML",1015,1063,27,"2026-05-08T18:34:32Z","Kubeflow AI Reference Platform Deployment Manifests"),
        ("arena","kubeflow/arena","Go",810,190,57,"2026-05-07T06:46:17Z","A CLI for Kubeflow"),
        ("mpi-operator","kubeflow/mpi-operator","Go",524,235,100,"2026-05-05T05:00:55Z","Kubernetes Operator for MPI-based apps"),
        ("hub","kubeflow/hub","Go",175,178,41,"2026-05-09T16:20:08Z","Model Registry for ML artifacts"),
        ("kale","kubeflow/kale","Python",685,156,58,"2026-05-09T17:18:56Z","Kubeflow superfood for Data Scientists"),
        ("community","kubeflow/community","Jsonnet",196,257,13,"2026-05-09T16:41:26Z","Kubeflow community information"),
        ("website","kubeflow/website","HTML",184,919,52,"2026-05-08T20:42:29Z","Kubeflow Website"),
        ("dashboard","kubeflow/dashboard","TypeScript",17,55,75,"2026-05-09T12:48:37Z","Kubeflow Central Dashboard"),
        ("mcp-apache-spark-history-server","kubeflow/mcp-apache-spark-history-server","Python",167,58,27,"2026-05-09T02:08:36Z","MCP Server for Apache Spark History Server"),
        ("examples","kubeflow/examples","Jsonnet",1462,756,111,"2025-04-14T01:54:52Z","Extended examples and tutorials"),
        ("fairing","kubeflow/fairing","Jsonnet",337,143,134,"2022-04-11T05:28:47Z","Python SDK for building ML models"),
        ("pytorch-operator","kubeflow/pytorch-operator","Jsonnet",310,143,63,"2021-12-01T17:44:48Z","PyTorch on Kubernetes"),
        ("kfp-tekton","kubeflow/kfp-tekton","TypeScript",182,123,79,"2024-11-19T12:23:51Z","Kubeflow Pipelines on Tekton"),
        ("kfctl","kubeflow/kfctl","Go",182,134,94,"2023-08-15T20:19:22Z","CLI for deploying Kubeflow"),
        ("docs-agent","kubeflow/docs-agent","Python",36,98,159,"2026-04-14T03:33:15Z","Kubeflow Documentation AI Agent"),
        ("sdk","kubeflow/sdk","Python",114,174,129,"2026-05-07T16:14:48Z","Universal Python SDK for Kubernetes AI workloads"),
        ("notebooks","kubeflow/notebooks","",71,108,187,"2026-05-08T21:21:37Z","Kubeflow Notebooks"),
        ("internal-acls","kubeflow/internal-acls","Go",19,385,2,"2026-05-09T21:06:02Z","Group ACLs for Kubeflow developers"),
        ("testing","kubeflow/testing","Python",60,86,33,"2025-02-14T18:33:13Z","Test infrastructure for Kubeflow"),
        ("mcp-server","kubeflow/mcp-server","Python",4,6,11,"2026-04-17T14:13:49Z","MCP Server for Kubeflow"),
    ],
    "TeglonLabs": [
        ("mathpix-gem","TeglonLabs/mathpix-gem","Ruby",2,0,11,"2026-01-01T12:13:13Z","Transform mathematical images to LaTeX"),
        ("monad-mcp-server","TeglonLabs/monad-mcp-server","","",0,0,"2025-05-14T11:36:14Z","Monad MCP Server"),
        ("topoi","TeglonLabs/topoi","Python",0,0,1,"2025-01-24T04:49:26Z",""),
        ("coin-flip-mcp","TeglonLabs/coin-flip-mcp","JavaScript",0,2,1,"2025-09-21T08:57:27Z","MCP server for coin flips with random.org"),
    ],
    "bmorphism": [
        ("Gay.jl","bmorphism/Gay.jl","Julia",1,0,187,"2026-05-10T00:33:08Z","Wide-gamut color sampling with splittable determinism"),
        ("nanoclj-zig","bmorphism/nanoclj-zig","Zig",0,0,0,"2026-05-07T20:12:15Z",""),
        ("zig-syrup","bmorphism/zig-syrup","Zig",0,0,0,"2026-05-07T19:49:05Z","Embeddable OCapN Syrup encoder/decoder"),
        ("boxxy","bmorphism/boxxy","Move",0,1,0,"2026-04-30T03:35:47Z",""),
        ("postweb","bmorphism/postweb","Go",0,0,0,"2026-04-09T10:51:57Z","postweb evolved from prepostweb"),
        ("shitcoin","bmorphism/shitcoin","Python",5,0,0,"2026-04-08T08:07:08Z","gets denom for cw20 assets"),
        ("magic-world-org","bmorphism/magic-world-org","Python",1,0,0,"2026-04-05T07:03:50Z","Magic World Org - Local MLX"),
        ("ocaml-mcp-sdk","bmorphism/ocaml-mcp-sdk","OCaml",61,2,0,"2026-03-16T05:24:25Z","OCaml SDK for Model Context Protocol"),
        ("anti-bullshit-mcp-server","bmorphism/anti-bullshit-mcp-server","JavaScript",23,7,1,"2026-01-16T08:54:58Z","MCP server for analyzing claims"),
        ("vibespace-mcp-go-ternary","bmorphism/vibespace-mcp-go-ternary","HTML",0,1,3,"2026-01-11T12:50:40Z","Go MCP for vibes with NATS + balanced ternary"),
        ("flox-mcp-bb","bmorphism/flox-mcp-bb","Clojure",0,0,0,"2026-02-12T02:45:43Z","Open-source MCP server for Flox"),
        ("bafishka","bmorphism/bafishka","Clojure",1,0,0,"2025-12-19T09:38:00Z","Rust-native Fish shell Babashka library"),
        ("monero-rental-hash-war","bmorphism/monero-rental-hash-war","Haskell",1,0,0,"2025-10-05T23:08:54Z","Compositional OpenGame analysis of Monero"),
        ("whale","bmorphism/whale","MATLAB",2,0,0,"2025-09-04T06:55:21Z","omniglot + sperm whale codas"),
        ("penrose-mcp","bmorphism/penrose-mcp","JavaScript",10,4,0,"2025-01-20T21:44:55Z","Penrose server for Infinity-Topos"),
        ("manifold-mcp-server","bmorphism/manifold-mcp-server","JavaScript",14,9,5,"2025-01-11T10:36:58Z","MCP server for Manifold Markets"),
        ("say-mcp-server","bmorphism/say-mcp-server","JavaScript",20,9,3,"2025-01-07T03:15:18Z","MCP server for macOS text-to-speech"),
        ("hypernym-mcp-server","bmorphism/hypernym-mcp-server","JavaScript",6,5,0,"2025-04-02T21:21:08Z",""),
        ("graphistry-mcp","bmorphism/graphistry-mcp","Python",2,0,0,"2025-05-06T17:34:24Z","Graphistry MCP integration"),
        ("infinity-topos","bmorphism/infinity-topos","Python",1,0,0,"2025-08-29T05:39:49Z",""),
        ("open-location-code-zig","bmorphism/open-location-code-zig","Zig",3,0,0,"2025-12-30T19:33:45Z","Open Location Code for Zig"),
        ("multiverse-color-game","bmorphism/multiverse-color-game","Julia",0,0,0,"2025-12-12T05:28:11Z","2+1D Holographic Color Matching Game"),
        ("zeldar","bmorphism/zeldar","Python",1,0,1,"2025-08-26T15:16:21Z","Burning Man Art Robot"),
        ("oxcaml-sci-canonical","bmorphism/oxcaml-sci-canonical","OCaml",1,0,0,"2025-06-20T06:37:12Z","Canonical OxCaml-SCI implementation"),
        ("zk-haiku-nanogpt","bmorphism/zk-haiku-nanogpt","Solidity",1,0,0,"2025-07-06T03:08:24Z","ZK-Haiku-NanoGPT verifiable multi-agent AI"),
        ("rama-event-processor","bmorphism/rama-event-processor","Java",1,0,0,"2025-07-02T07:01:44Z","Event processing with Rama"),
        ("schoenfinkel","bmorphism/schoenfinkel","Python",1,0,0,"2025-10-04T23:31:11Z","Post-quantum categorical gravity framework"),
        ("penumbra-mcp","bmorphism/penumbra-mcp","JavaScript",5,6,3,"2025-01-07T01:15:23Z","MCP for Penumbra blockchain"),
        ("krep-mcp-server","bmorphism/krep-mcp-server","JavaScript",1,1,1,"2025-03-19T20:22:46Z","High-performance string search MCP"),
    ],
    "zubyul": [
        ("voice-observatory","zubyul/voice-observatory","Python",0,0,0,"2026-04-24T05:56:17Z","Passive macOS TUI observing voice-download pathways"),
        ("ghostel-emacs-worlds","zubyul/ghostel-emacs-worlds","GLSL",0,0,0,"2026-04-24T00:20:56Z","Ghostty config + emacs-mods"),
        ("nash-web","zubyul/nash-web","Rust",0,0,0,"2026-04-13T07:08:58Z","NASH token browser TUI via ratzilla WASM"),
        ("nash-tui","zubyul/nash-tui","Rust",0,0,0,"2026-04-13T07:45:16Z","NASH token TUI real-time candles"),
        ("big-bad-plurigrid-quiz","zubyul/big-bad-plurigrid-quiz","Emacs Lisp",0,0,0,"2026-04-09T18:51:31Z","27 flashcards from plurigrid activity"),
        ("Gay.jl","zubyul/Gay.jl","Julia",0,0,0,"2026-03-28T11:30:01Z","Wide-gamut color sampling fork"),
        ("kinesis-kb360pro","zubyul/kinesis-kb360pro","Python",0,0,0,"2026-03-26T10:29:40Z","Claude Code skill for Kinesis keyboard"),
        ("gay-world","zubyul/gay-world","Python",1,1,0,"2026-03-26T04:03:39Z","Goblin world builder with MLX task decomposition"),
        ("tilelang-kernels","zubyul/tilelang-kernels","Python",0,0,0,"2026-03-16T02:31:13Z","TileLang GPU kernels for GF(3) trit classification"),
        ("gay-terminal-colors","zubyul/gay-terminal-colors","Clojure",0,0,0,"2026-02-21T07:38:14Z","Gay.jl world_terminal_fingerprint"),
        ("openbci-visualizer","zubyul/openbci-visualizer","Zig",0,0,0,"2026-02-04T11:17:41Z",""),
        ("plurigrid-site","zubyul/plurigrid-site","Svelte",0,1,11,"2026-02-04T03:20:08Z","Plurigrid world site deployment"),
        ("vibesnipe","zubyul/vibesnipe","Move",0,0,1,"2026-01-30T22:36:03Z",""),
        ("zubyul.github.io","zubyul/zubyul.github.io","CSS",1,0,0,"2026-01-27T03:24:34Z",""),
        ("toad-warpify-extension","zubyul/toad-warpify-extension","Python",0,0,0,"2026-01-17T07:48:40Z","Warpify extension for Toad ACP agents"),
        ("cat-world","zubyul/cat-world","TypeScript",0,0,0,"2025-12-12T08:47:14Z","Cat gaze tracker bird video preferences"),
        ("chromatic-vrf","zubyul/chromatic-vrf","Kotlin",0,0,0,"2025-12-12T03:26:22Z","Chromatic VRF I Love Hue puzzle"),
        ("c-elegans-connectome","zubyul/c-elegans-connectome","JavaScript",0,0,0,"2025-11-22T15:43:55Z",""),
        ("cascade-world","zubyul/cascade-world","Python",1,0,0,"2025-09-19T18:25:12Z","Cascade development environment"),
        ("defcon","zubyul/defcon","JavaScript",1,0,0,"2025-09-17T02:07:00Z",""),
        ("jonikas_lab_data_analysis_misc","zubyul/jonikas_lab_data_analysis_misc","Jupyter Notebook",2,0,0,"2023-08-16T20:24:40Z","scripts for genetic sequence data"),
        ("WGCNA","zubyul/WGCNA","HTML",2,0,0,"2023-07-05T18:02:30Z","weighted gene correlation network analysis"),
        ("Nikolova_lab_data_analysis","zubyul/Nikolova_lab_data_analysis","R",2,0,0,"2023-06-16T13:56:58Z","undergraduate thesis cortical thickness"),
    ],
    "social_migalkin": [
        ("kgcourse2021","migalkin/kgcourse2021","HTML",25,9,0,"2026-02-16T05:16:08Z","Knowledge Graphs course materials"),
        ("NodePiece","migalkin/NodePiece","Python",144,21,0,"2026-05-07T05:40:02Z","Parameter-Efficient Representations for KGs (ICLR'22)"),
        ("StarE","migalkin/StarE","Python",89,16,1,"2026-04-16T14:12:45Z","Message Passing for Hyper-Relational Knowledge Graphs"),
        ("NBFNet_mlx","migalkin/NBFNet_mlx","Python",10,1,1,"2026-03-11T01:31:21Z","Neural Bellman-Ford networks in MLX"),
        ("RWL","migalkin/RWL","Python",7,1,0,"2025-02-10T14:12:14Z","Weisfeiler and Leman Go Relational"),
        ("rambo","migalkin/rambo","Rust",3,0,1,"2023-02-28T16:37:22Z",""),
        ("migalkin.github.io","migalkin/migalkin.github.io","JavaScript",0,0,0,"2025-05-20T23:58:08Z","Academic personal website"),
    ],
    "social_wasita": [
        ("vocoder","wasita/vocoder","JavaScript",0,0,0,"2026-05-06T05:14:03Z",""),
        ("wasita.github.io","wasita/wasita.github.io","Svelte",1,0,8,"2026-04-28T05:26:08Z","personal website"),
        ("magic-garden","wasita/magic-garden","Python",2,1,1,"2026-04-22T21:16:43Z","Discord magic garden automation bot"),
        ("wm-cv","wasita/wm-cv","Svelte",0,0,0,"2026-04-12T02:53:51Z","Academic CV web app"),
        ("send2kobo","wasita/send2kobo","TypeScript",0,0,0,"2025-12-12T19:09:16Z","Website for sending books to Kobo"),
        ("wins-search","wasita/wins-search","CSS",1,0,0,"2023-06-03T19:01:11Z","Women in Network Science member list"),
    ],
    "social_kristinezheng": [
        ("kristinezheng.github.io","kristinezheng/kristinezheng.github.io","HTML",0,0,0,"2026-04-09T17:09:47Z",""),
        ("Portfolio","kristinezheng/Portfolio","","",0,0,"2025-02-12T00:00:45Z","Portfolio July 2021"),
        ("lookit-jenga","kristinezheng/lookit-jenga","Jupyter Notebook",0,0,0,"2024-05-16T18:29:05Z","Lookit study 9.85"),
        ("Green-Machine","kristinezheng/Green-Machine","Python",0,0,0,"2021-09-19T05:33:04Z","HackMIT 2021 Sustainability Track"),
    ],
    "social_M1shaaa": [
        ("lab-bookshelf-","M1shaaa/lab-bookshelf-","TypeScript",0,0,0,"2024-12-31T05:11:18Z",""),
        ("Python-Lookit-Uploads","M1shaaa/Python-Lookit-Uploads","Python",0,0,0,"2024-02-15T22:31:41Z",""),
    ],
    "social_AustinCStone": [
        ("EpsteinSearch","AustinCStone/EpsteinSearch","Python",0,0,0,"2026-02-11T01:10:57Z",""),
        ("bmforkupdate","AustinCStone/bmforkupdate","Python",0,0,0,"2025-05-09T04:50:16Z",""),
        ("bmfork","AustinCStone/bmfork","Python",0,0,1,"2025-05-09T04:18:54Z",""),
        ("StructureFromMotion","AustinCStone/StructureFromMotion","Python",1,0,0,"2019-04-26T19:43:12Z","Recover 3D geometry from videos"),
        ("Z-order-curve","AustinCStone/Z-order-curve","Python",0,0,0,"2019-06-09T02:53:43Z","Space filling z-order curve demo"),
    ],
    "social_DJedamski": [
        ("kaggle_ncaa18","DJedamski/kaggle_ncaa18","Jupyter Notebook",0,0,0,"2018-02-26T16:33:24Z","NCAA March Madness 2018"),
    ],
}

# ── insert world_increments + repo_snapshots ────────────────────────────────
inc_id = 1
repo_id = 1
for source, repos in REPOS.items():
    # determine source_type
    if source in ("plurigrid","kubeflow","TeglonLabs"):
        source_type = "org"
    elif source in ("bmorphism","zubyul"):
        source_type = "user"
    else:
        source_type = "social"

    trit, color, name = gf3(inc_id)
    h = snap_hash(f"{source}:{inc_id}")
    con.execute("""
        INSERT INTO world_increments VALUES (?,?,?,?,?,?,?,?,?,?,?)
    """, [inc_id, NOW, trit, color, name, source_type, source,
          "repo_sweep", f"{len(repos)} repos", "sweep-agent", h])

    for repo in repos:
        rname, full_name, lang, stars, forks, issues, pushed, desc = repo
        trit2, color2, gf3name2 = gf3(repo_id)
        con.execute("""
            INSERT INTO repo_snapshots VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
        """, [repo_id, NOW, inc_id, source, rname, full_name,
              lang if lang else None,
              int(stars) if str(stars).isdigit() else 0,
              int(forks) if str(forks).isdigit() else 0,
              int(issues) if str(issues).isdigit() else 0,
              pushed, desc])
        repo_id += 1
    inc_id += 1

print(f"Inserted {inc_id-1} world_increments, {repo_id-1} repo_snapshots")

# ── Aptos balances ─────────────────────────────────────────────────────────
WALLETS = [
    ("alice", "0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b"),
    ("bob",   "0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d"),
    ("A","0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a"),
    ("B","0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13"),
    ("C","0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e"),
    ("D","0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1"),
    ("E","0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36"),
    ("F","0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71"),
    ("G","0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32"),
    ("H","0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f"),
    ("I","0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9"),
    ("J","0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54"),
    ("K","0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4"),
    ("L","0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9"),
    ("M","0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9"),
    ("N","0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c"),
    ("O","0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d"),
    ("P","0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948"),
    ("Q","0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9"),
    ("R","0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10"),
    ("S","0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386"),
    ("T","0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588"),
    ("U","0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956"),
    ("V","0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3"),
    ("W","0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0"),
    ("X","0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d"),
    ("Y","0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4"),
    ("Z","0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c"),
]
for world, addr in WALLETS:
    # All returned NULL (no CoinStore resource — empty accounts)
    con.execute("INSERT INTO aptos_snapshots VALUES (?,?,?,?)",
                [NOW, world, addr, None])
print(f"Inserted {len(WALLETS)} aptos_snapshots (all NULL — no CoinStore)")

# ── Multisig probes ────────────────────────────────────────────────────────
MULTISIG = [
    ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2,True),
    ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2,True),
    ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2,True),
    ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2,True),
    ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2,True),
]
for pair, addr, sigs, healthy in MULTISIG:
    con.execute("INSERT INTO multisig_probes VALUES (?,?,?,?,?)",
                [NOW, pair, addr, sigs, healthy])
print(f"Inserted {len(MULTISIG)} multisig_probes (all 2-of-2 healthy)")

# ── MNX snapshot (SPA — no JSON API) ──────────────────────────────────────
# testnet.mnx.fi is a Next.js SPA; no /api/markets endpoint available
# Record sentinel indicating unavailability
con.execute("INSERT INTO mnx_snapshots VALUES (?,?,?,?,?,?)",
            [NOW, "N/A", "MNX_TESTNET_UNAVAILABLE", "SPA_NO_API", None, None])
print("Inserted MNX sentinel (SPA, no JSON API found)")

con.close()
print("Done.")
