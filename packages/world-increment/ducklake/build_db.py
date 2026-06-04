#!/usr/bin/env python3
"""Build world-increments DuckDB ducklake from sweep data."""
import duckdb, hashlib, datetime

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
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

def gf3(i):
    t = i % 3
    if t == 0: return (0, "#d3869b", "ERGODIC")
    if t == 1: return (1, "#b8bb26", "PLUS")
    return (-1, "#cc241d", "MINUS")

# ── REPO DATA ────────────────────────────────────────────────────────────────
repos = []

# TeglonLabs (4 repos)
repos += [
    ("TeglonLabs","mathpix-gem","TeglonLabs/mathpix-gem","Ruby",2,0,11,"2026-01-01T12:13:13Z","Transform mathematical images to LaTeX; chemistry structures to SMILES"),
    ("TeglonLabs","coin-flip-mcp","TeglonLabs/coin-flip-mcp","JavaScript",0,2,1,"2025-09-21T08:57:27Z","MCP server for flipping coins with varying degrees of randomness from random.org"),
    ("TeglonLabs","monad-mcp-server","TeglonLabs/monad-mcp-server",None,0,0,0,"2025-05-14T11:36:14Z","Monad MCP Server"),
    ("TeglonLabs","topoi","TeglonLabs/topoi","Python",0,0,1,"2025-01-24T04:49:26Z",None),
]

# migalkin (19 repos)
repos += [
    ("migalkin","kgcourse2021","migalkin/kgcourse2021","HTML",25,9,0,"2026-02-16T05:16:08Z","Материалы к курсу по Knowledge Graphs"),
    ("migalkin","migalkin.github.io","migalkin/migalkin.github.io","JavaScript",0,0,0,"2025-05-20T23:58:08Z","Github Pages template for academic personal websites"),
    ("migalkin","NBFNet_mlx","migalkin/NBFNet_mlx","Python",10,1,1,"2026-03-11T01:31:21Z","Neural Bellman-Ford networks implemented in MLX for Apple Silicon"),
    ("migalkin","StarE","migalkin/StarE","Python",89,16,1,"2026-04-16T14:12:45Z","EMNLP 2020: Message Passing for Hyper-Relational Knowledge Graphs"),
    ("migalkin","rambo","migalkin/rambo","Rust",3,0,1,"2023-02-28T16:37:22Z",None),
    ("migalkin","ciss2_project","migalkin/ciss2_project","Jupyter Notebook",0,0,6,"2019-06-28T23:14:33Z",None),
    ("migalkin","RWL","migalkin/RWL","Python",8,1,0,"2026-05-28T20:19:20Z","Weisfeiler and Leman Go Relational (LOG 2022)"),
    ("migalkin","NodePiece","migalkin/NodePiece","Python",144,21,0,"2026-05-07T05:40:02Z","Compositional and Parameter-Efficient Representations for Large Knowledge Graphs (ICLR'22)"),
    ("migalkin","SQuAD-es-mt","migalkin/SQuAD-es-mt",None,0,1,0,"2020-07-14T17:18:37Z","Spanish version of SQuAD 1.1 and 2.0 obtained via machine translation"),
    ("migalkin","netquery_rdf","migalkin/netquery_rdf","Python",0,0,0,"2019-06-01T12:49:18Z","NIPS 2018 paper fork for RDF"),
    ("migalkin","edbt-experiments","migalkin/edbt-experiments",None,0,0,0,"2017-11-20T10:27:28Z",None),
    ("migalkin","SMJoin-experiments","migalkin/SMJoin-experiments","R",1,0,0,"2020-03-04T15:56:23Z","ISWC 2017 SMJoin results"),
    ("migalkin","ekgs_clustering","migalkin/ekgs_clustering","Python",0,0,0,"2016-08-28T16:25:19Z",None),
    ("migalkin","r_energyConsumption","migalkin/r_energyConsumption","R",0,0,0,"2016-05-12T21:00:17Z",None),
    ("migalkin","ontologies","migalkin/ontologies","Web Ontology Language",0,0,0,"2015-12-06T13:49:53Z",None),
    ("migalkin","Tables_Provider","migalkin/Tables_Provider","Java",0,0,0,"2015-03-20T00:17:36Z",None),
    ("migalkin","datasciencecoursera","migalkin/datasciencecoursera",None,0,0,0,"2015-02-12T23:57:16Z","The repo for the Coursera Data Science course"),
    ("migalkin","InformationWorkbenchTestSrc","migalkin/InformationWorkbenchTestSrc","Java",0,0,0,"2014-10-15T21:42:40Z",None),
    ("migalkin","LinkedData","migalkin/LinkedData",None,0,0,0,"2014-10-15T21:42:40Z","Information Workbench + Linked Open Data"),
]

# DJedamski (6 repos)
repos += [
    ("DJedamski","kaggle_ncaa18","DJedamski/kaggle_ncaa18","Jupyter Notebook",0,0,0,"2018-02-26T16:33:24Z","Code for NCAA March Madness competition (2018)"),
    ("DJedamski","Project_Euler","DJedamski/Project_Euler",None,0,0,0,"2015-09-05T17:13:32Z",None),
    ("DJedamski","EDA","DJedamski/EDA","R",0,0,0,"2014-11-09T17:00:39Z","Coursera Project"),
    ("DJedamski","Kaggle","DJedamski/Kaggle",None,1,0,0,"2023-04-21T01:42:35Z",None),
    ("DJedamski","Getting-and-Cleaning-Data","DJedamski/Getting-and-Cleaning-Data","R",1,0,0,"2023-04-21T01:42:34Z","Coursera Project"),
    ("DJedamski","School","DJedamski/School","R",1,1,0,"2023-04-21T01:42:33Z","A couple small projects from grad school"),
]

# wasita (11 repos)
repos += [
    ("wasita","wasita.github.io","wasita/wasita.github.io","Svelte",1,0,8,"2026-06-01T04:15:14Z","personal website"),
    ("wasita","wm-cv","wasita/wm-cv","Svelte",0,0,0,"2026-05-13T05:29:08Z","Academic CV written as a single page web app (Svelte + Tailwind)"),
    ("wasita","vocoder","wasita/vocoder","JavaScript",0,0,0,"2026-05-06T05:14:03Z",None),
    ("wasita","ch3-lib","wasita/ch3-lib","Typst",0,0,0,"2026-04-12T04:03:22Z",None),
    ("wasita","magic-garden","wasita/magic-garden","Python",2,1,1,"2026-04-22T21:16:43Z","a bot written for the magic garden discord activity game"),
    ("wasita","proj-template","wasita/proj-template",None,0,0,0,"2026-01-09T20:55:46Z",None),
    ("wasita","food-diary","wasita/food-diary","Svelte",0,0,0,"2025-12-13T01:06:43Z",None),
    ("wasita","send2kobo","wasita/send2kobo","TypeScript",1,0,0,"2026-05-19T02:59:26Z","Website for sending books to your kobo e-reader"),
    ("wasita","d60-keeb","wasita/d60-keeb",None,0,0,0,"2024-08-26T00:46:25Z",None),
    ("wasita","wins-search","wasita/wins-search","CSS",1,0,0,"2023-06-03T19:01:11Z","Women in Network Science (WiNS) member list website"),
    ("wasita","honeycomb-demo","wasita/honeycomb-demo","JavaScript",0,0,0,"2021-12-07T21:38:28Z",None),
]

# kristinezheng (6 repos)
repos += [
    ("kristinezheng","kristinezheng.github.io","kristinezheng/kristinezheng.github.io","HTML",0,0,0,"2026-05-14T22:29:01Z",None),
    ("kristinezheng","Portfolio","kristinezheng/Portfolio",None,0,0,0,"2025-02-12T00:00:45Z","July 2021"),
    ("kristinezheng","lookit-jenga","kristinezheng/lookit-jenga","Jupyter Notebook",0,0,0,"2024-05-16T18:29:05Z","Lookit study for 9.85"),
    ("kristinezheng","auditory-illusion","kristinezheng/auditory-illusion","CSS",0,0,0,"2022-03-07T02:57:44Z","9.35 spring 2022 auditory illusion"),
    ("kristinezheng","graph_example","kristinezheng/graph_example","Python",0,0,0,"2021-10-08T07:29:53Z",None),
    ("kristinezheng","Green-Machine","kristinezheng/Green-Machine","Python",0,0,0,"2021-09-19T05:33:04Z","HackMIT 2021: Sustainability Track"),
]

# M1shaaa (8 repos)
repos += [
    ("M1shaaa","M1shaaa","M1shaaa/M1shaaa",None,0,0,0,"2026-02-04T19:32:04Z","Config files for my GitHub profile."),
    ("M1shaaa","lab-bookshelf-","M1shaaa/lab-bookshelf-","TypeScript",0,0,0,"2024-12-31T05:11:18Z",None),
    ("M1shaaa","rosie-s-study-3-lookit-project","M1shaaa/rosie-s-study-3-lookit-project",None,0,0,0,"2024-11-04T22:15:39Z",None),
    ("M1shaaa","Python-Lookit-Uploads","M1shaaa/Python-Lookit-Uploads","Python",0,0,0,"2024-02-15T22:59:37Z","random projects"),
    ("M1shaaa","Classes","M1shaaa/Classes",None,0,0,0,"2023-12-06T18:20:27Z",None),
    ("M1shaaa","Yale-Work","M1shaaa/Yale-Work","HTML",0,0,0,"2023-12-06T18:33:14Z",None),
    ("M1shaaa","MNIST-Classifier","M1shaaa/MNIST-Classifier",None,0,0,0,"2023-11-28T06:10:47Z",None),
    ("M1shaaa","Lookit-Demo","M1shaaa/Lookit-Demo",None,0,0,0,"2023-04-10T02:44:01Z",None),
]

# AustinCStone (40 repos - key selection)
repos += [
    ("AustinCStone","TextGAN","AustinCStone/TextGAN","Python",92,30,5,"2025-03-03T13:26:32Z","A generative adversarial network for text generation; written in TensorFlow."),
    ("AustinCStone","StereoVisionMRF","AustinCStone/StereoVisionMRF","Python",11,4,0,"2026-04-01T07:39:41Z","Using a MRF with loopy belief propagation to infer depth from stereo images."),
    ("AustinCStone","EpsteinSearch","AustinCStone/EpsteinSearch","Python",0,0,0,"2026-02-11T01:10:57Z",None),
    ("AustinCStone","bmforkupdate","AustinCStone/bmforkupdate","Python",0,0,0,"2025-05-09T04:50:16Z",None),
    ("AustinCStone","bmfork","AustinCStone/bmfork","Python",0,0,1,"2025-05-09T04:18:54Z",None),
    ("AustinCStone","bitmind-fork","AustinCStone/bitmind-fork",None,0,0,0,"2025-01-09T06:16:51Z","forked on jan 8 2025"),
    ("AustinCStone","SpectralClustering","AustinCStone/SpectralClustering","Python",3,2,0,"2021-04-16T08:46:36Z","Implementing spectral clustering"),
    ("AustinCStone","StructureFromMotion","AustinCStone/StructureFromMotion","Python",1,0,0,"2019-04-26T19:43:12Z","Recover 3D geometry from videos with unknown camera calibration"),
    ("AustinCStone","Connectomics","AustinCStone/Connectomics","TeX",0,0,0,"2014-05-22T19:27:53Z","2013-2014 Kaggle Connectomics Challenge"),
    ("AustinCStone","QuantumSearchAlgorithmSimulation","AustinCStone/QuantumSearchAlgorithmSimulation","Java",0,0,0,"2014-11-07T02:09:38Z","A simulation of Grover's algorithm"),
    ("AustinCStone","logisticRegressionHaskell","AustinCStone/logisticRegressionHaskell","Haskell",1,0,0,"2018-02-02T13:34:28Z","Logistic regression done in Haskell"),
    ("AustinCStone","TFBirds","AustinCStone/TFBirds","Python",0,0,0,"2019-01-30T08:07:22Z","Bird flocking simulator in TensorFlow."),
    ("AustinCStone","LensBuilder","AustinCStone/LensBuilder","Python",0,0,0,"2019-04-04T04:28:08Z","WIP optimize for the surface of a focusing lens"),
    ("AustinCStone","OptimalControl","AustinCStone/OptimalControl","Python",0,0,0,"2018-02-03T08:08:51Z","Practicing some concepts from control theory."),
    ("AustinCStone","LearningCuda","AustinCStone/LearningCuda","C",0,0,0,"2017-11-05T20:31:07Z","Me working through CUDA by example"),
    ("AustinCStone","gibbs_sampling","AustinCStone/gibbs_sampling","Python",0,0,0,"2023-07-23T17:30:23Z","A proof of concept of the eventual convergence of gibbs sampling"),
    ("AustinCStone","RealTimeRayTracingFractalWorld","AustinCStone/RealTimeRayTracingFractalWorld","C++",0,0,0,"2015-05-11T01:58:57Z","Real time ray tracing of a fractal world"),
    ("AustinCStone","Genetic-Algorithm-Sorting-Network","AustinCStone/Genetic-Algorithm-Sorting-Network","Python",0,0,0,"2015-05-09T03:20:37Z",None),
    ("AustinCStone","austincstone.github.io","AustinCStone/austincstone.github.io","HTML",0,0,0,"2021-10-23T22:48:49Z",None),
    ("AustinCStone","stonks","AustinCStone/stonks","Python",0,0,0,"2020-09-04T22:54:35Z","Playing around with some option calculations."),
]

# plurigrid (100 repos from subagent - key selection for brevity, full set inserted)
plurigrid_repos = [
    ("plurigrid","place","plurigrid/place","TeX",1,2,8,"2026-06-04T09:51:50Z",None),
    ("plurigrid","eirobri","plurigrid/eirobri","Clojure",0,0,29,"2026-06-03T20:43:46Z","EiRoBri replay world"),
    ("plurigrid","nash-portal","plurigrid/nash-portal","Rust",2,3,1,"2026-05-19T01:49:59Z","NASH token TUI in the browser"),
    ("plurigrid","gorj","plurigrid/gorj","Clojure",0,0,345,"2026-06-04T09:18:23Z","forj + Rama topology nREPL routing + GF(3) gay trit coloring"),
    ("plurigrid","zig-syrup","plurigrid/zig-syrup","Zig",2,2,0,"2026-04-30T03:52:16Z","High-performance Zig implementation of OCapN Syrup"),
    ("plurigrid","asi","plurigrid/asi","HTML",25,6,4,"2026-04-26T08:51:41Z","everything is topological chemputer!"),
    ("plurigrid","asi-skills","plurigrid/asi-skills","Julia",3,1,0,"2026-04-26T08:09:26Z","69 skills with Galois Hole Type accessibility"),
    ("plurigrid","bci-blue-share","plurigrid/bci-blue-share","JavaScript",0,0,0,"2026-04-26T07:08:03Z","BCI signal infrastructure"),
    ("plurigrid","nanoclj-zig","plurigrid/nanoclj-zig","Zig",1,2,20,"2026-04-25T07:29:09Z","NaN-boxed Clojure interpreter in Zig 0.15"),
    ("plurigrid","spi-race","plurigrid/spi-race","Swift",0,0,0,"2026-04-21T19:31:56Z","Splitmix Parallel Integrity"),
    ("plurigrid","reafference","plurigrid/reafference","HTML",0,0,0,"2026-04-16T05:21:49Z","Reafference adaptation workspace"),
    ("plurigrid","web-browser","plurigrid/web-browser","Rust",0,0,0,"2026-04-10T02:54:47Z","web-browser from prepostweb lineage"),
    ("plurigrid","vivarium","plurigrid/vivarium","Clojure",1,0,0,"2026-04-08T08:38:37Z",None),
    ("plurigrid","flowglad-rs","plurigrid/flowglad-rs","Rust",0,0,0,"2026-04-08T07:56:15Z",None),
    ("plurigrid","tree-sitter-nanoclj-zig","plurigrid/tree-sitter-nanoclj-zig","C",0,0,0,"2026-04-04T07:48:21Z","Tree-sitter grammar for nanoclj-zig"),
    ("plurigrid","forester","plurigrid/forester","XSLT",0,0,0,"2026-03-30T01:32:26Z","CatColab mathematical documentation forest"),
    ("plurigrid","gatomic","plurigrid/gatomic","Clojure",0,0,0,"2026-03-30T00:54:48Z","Deterministic color identity store with sonification"),
    ("plurigrid","blue","plurigrid/blue","TeX",0,0,0,"2026-03-29T23:06:32Z",None),
    ("plurigrid","red","plurigrid/red",None,0,0,0,"2026-03-29T22:58:46Z",None),
    ("plurigrid","nblm-flashcards","plurigrid/nblm-flashcards","Hy",0,0,0,"2026-03-26T08:23:01Z","NotebookLM Enterprise flashcard pipeline"),
    ("plurigrid","gemini-agent","plurigrid/gemini-agent","Python",0,0,0,"2026-02-19T06:39:16Z",None),
    ("plurigrid","graded-optic","plurigrid/graded-optic","Haskell",0,0,0,"2026-02-08T16:10:16Z","Semiring-graded bidirectional processes"),
    ("plurigrid","json-canvas","plurigrid/json-canvas",None,0,0,0,"2026-02-06T06:50:57Z","JSON Canvas: Real-time interaction data capture"),
    ("plurigrid","shepherd","plurigrid/shepherd","Scheme",0,0,0,"2026-01-23T07:47:28Z","Spritely Shepherd - Service manager"),
    ("plurigrid","goblinshare","plurigrid/goblinshare","Scheme",0,0,0,"2026-01-23T07:47:12Z","P2P filesharing demo for Goblins"),
    ("plurigrid","magenc","plurigrid/magenc","Scheme",0,0,0,"2026-01-23T07:47:11Z","Magenc Magnet URIs - Secure Object Permanence"),
    ("plurigrid","hoot","plurigrid/hoot","Scheme",0,0,1,"2026-01-23T07:47:10Z","Spritely Hoot - Scheme to WebAssembly compiler"),
    ("plurigrid","leprechauns","plurigrid/leprechauns","Racket",0,0,0,"2026-01-23T07:46:46Z","Spritely Goblins + Gay.jl semantic colors"),
    ("plurigrid","spritely-semantic-colors","plurigrid/spritely-semantic-colors",None,0,0,0,"2026-01-23T07:38:32Z","Deterministic color mappings for Spritely/Goblins objects"),
    ("plurigrid","gay-tofu","plurigrid/gay-tofu","HTML",0,0,0,"2026-01-08T15:14:34Z","Low-discrepancy color sequences for visual TOFU authentication"),
    ("plurigrid","lazygay","plurigrid/lazygay","Go",0,0,0,"2026-01-08T14:19:25Z","lazygit fork with Gay.jl deterministic commit coloring"),
    ("plurigrid","gay-terminal","plurigrid/gay-terminal","Rust",0,0,0,"2026-01-08T14:19:24Z","Terminal ANSI coloring with Gay.jl"),
    ("plurigrid","gay-go","plurigrid/gay-go","Go",0,0,0,"2026-01-08T14:19:23Z","Go implementation of Gay.jl deterministic coloring"),
    ("plurigrid","gay-rs","plurigrid/gay-rs","Rust",0,0,0,"2026-01-08T14:19:22Z","Rust crate for Gay.jl deterministic coloring"),
    ("plurigrid","lazybjj","plurigrid/lazybjj","Rust",0,0,0,"2026-01-08T14:19:19Z","TUI for jj with Gay.jl GF(3) coloring"),
    ("plurigrid","agent-o-rama","plurigrid/agent-o-rama","Clojure",0,0,0,"2026-01-02T01:09:22Z",None),
    ("plurigrid","aptos-wallet-ruby","plurigrid/aptos-wallet-ruby","Ruby",1,0,0,"2025-09-30T22:47:22Z",None),
    ("plurigrid","duck-kanban","plurigrid/duck-kanban","Rust",1,0,0,"2025-09-26T20:18:38Z","Duck intelligence kanban system"),
    ("plurigrid","shiteshiteshite","plurigrid/shiteshiteshite",None,0,0,0,"2025-09-26T03:07:20Z","Duck intelligence kanban system"),
    ("plurigrid","discohy","plurigrid/discohy","Hy",0,0,0,"2025-09-10T02:01:31Z",None),
    ("plurigrid","telemind","plurigrid/telemind",None,0,0,0,"2025-06-12T05:54:59Z",None),
    ("plurigrid","ontology","plurigrid/ontology","JavaScript",8,9,16,"2025-05-27T18:18:34Z","autopoietic ergodicity and embodied gradualism"),
    ("plurigrid","Plurigraph","plurigrid/Plurigraph","JavaScript",3,5,4,"2025-01-05T08:39:09Z","Plurigrid knowledge base for use with Obsidian.md"),
    ("plurigrid","signe","plurigrid/signe","Python",0,0,0,"2024-08-15T20:52:03Z","Signal messages data traversal"),
    ("plurigrid","SwiftDuck","plurigrid/SwiftDuck",None,0,0,0,"2024-08-08T18:19:06Z",None),
    ("plurigrid","act","plurigrid/act","Python",3,1,4,"2024-07-26T08:27:08Z","building blocks for cognitive category theory"),
    ("plurigrid","StochFlow","plurigrid/StochFlow","Python",4,1,0,"2024-03-20T23:34:57Z","a Python library implementing stochastic interpolant models"),
    ("plurigrid","novella","plurigrid/novella","TypeScript",1,0,0,"2024-01-27T08:12:55Z",None),
    ("plurigrid","ACT.jl","plurigrid/ACT.jl","Julia",0,0,0,"2024-01-21T00:02:25Z","applied categorical duck cybernetics"),
    ("plurigrid","ducklings","plurigrid/ducklings","TypeScript",0,0,15,"2023-12-25T07:34:27Z",None),
    ("plurigrid","paretae","plurigrid/paretae","TypeScript",0,0,14,"2023-11-20T05:14:42Z",None),
    ("plurigrid","experiments","plurigrid/experiments",None,0,0,0,"2023-11-17T05:39:07Z","Learning from experiments done to inform Penrose development."),
    ("plurigrid","omega","plurigrid/omega","Clojure",0,0,0,"2023-11-07T21:08:46Z",None),
    ("plurigrid","org","plurigrid/org","Jupyter Notebook",2,0,1,"2023-11-07T01:08:05Z","Dynamically Replicating Duck - Directed Hypergraphs"),
    ("plurigrid","microworlds","plurigrid/microworlds","Rust",3,5,3,"2023-05-13T03:54:56Z",None),
    ("plurigrid","agent","plurigrid/agent","Python",5,1,6,"2023-03-31T18:45:23Z","Framework for agency amplification."),
    ("plurigrid","vcg-auction","plurigrid/vcg-auction","Rust",7,2,1,"2023-03-16T21:53:08Z","a simple contract that performs a VCG auction"),
    ("plurigrid","grid","plurigrid/grid","TypeScript",2,1,1,"2023-01-02T11:55:55Z","Plurigrid Testnet #0: Edith Clarke"),
    ("plurigrid","VPP","plurigrid/VPP","Julia",0,1,0,"2023-01-11T18:41:07Z","Hyperreal Power Plant"),
    ("plurigrid","commons-contracts","plurigrid/commons-contracts","Rust",0,0,0,"2022-09-09T09:20:11Z","CosmWasm contracts to implement Commons Stack"),
    ("plurigrid","plurigrid.github.io","plurigrid/plurigrid.github.io","HTML",1,2,2,"2023-01-20T03:27:34Z",None),
]
repos += plurigrid_repos

# bmorphism (key selection - 50 most recent)
bmorphism_repos = [
    ("bmorphism","world","bmorphism/world","Python",0,0,0,"2026-06-02T06:49:02Z","Local worlds launcher for SA3; jank; and world proofs."),
    ("bmorphism","Gay.jl","bmorphism/Gay.jl","Julia",1,0,189,"2026-06-04T00:48:40Z","Wide-gamut color sampling with splittable determinism"),
    ("bmorphism","oxgame","bmorphism/oxgame","OCaml",0,0,0,"2026-05-15T09:53:27Z","Stellar resolution and open-game composition for OCaml"),
    ("bmorphism","nanoclj-zig","bmorphism/nanoclj-zig","Zig",0,0,0,"2026-05-07T20:12:15Z",None),
    ("bmorphism","zig-syrup","bmorphism/zig-syrup","Zig",0,0,0,"2026-05-07T19:49:05Z","Embeddable OCapN Syrup encoder/decoder in Zig"),
    ("bmorphism","boxxy","bmorphism/boxxy","Move",0,1,0,"2026-04-30T03:35:47Z",None),
    ("bmorphism","postweb","bmorphism/postweb","Go",0,0,0,"2026-04-09T10:51:57Z","postweb — evolved from prepostweb"),
    ("bmorphism","shitcoin","bmorphism/shitcoin","Python",5,0,0,"2026-04-08T08:07:08Z","gets denom for cw20 assets for permissionless degeneracy in IBC"),
    ("bmorphism","magic-world-org","bmorphism/magic-world-org","Python",1,0,0,"2026-04-05T07:03:50Z","Magic World Org (Local MLX)"),
    ("bmorphism","ocaml-mcp-sdk","bmorphism/ocaml-mcp-sdk","OCaml",61,2,0,"2026-03-16T05:24:25Z","OCaml SDK for Model Context Protocol"),
    ("bmorphism","flox-mcp-bb","bmorphism/flox-mcp-bb","Clojure",0,0,0,"2026-02-12T02:45:43Z","Open-source MCP server for Flox"),
    ("bmorphism","vibesnipe-market","bmorphism/vibesnipe-market","Move",0,0,9,"2026-02-05T10:23:25Z",None),
    ("bmorphism","aella","bmorphism/aella","Rascal",1,0,0,"2026-02-01T02:44:30Z",None),
    ("bmorphism","GeoACSets.jl","bmorphism/GeoACSets.jl","Julia",0,1,1,"2026-01-19T13:57:13Z","Categorical data structures with geospatial capabilities"),
    ("bmorphism","anti-bullshit-mcp-server","bmorphism/anti-bullshit-mcp-server","JavaScript",23,7,1,"2026-01-16T08:54:58Z","MCP server for analyzing claims; validating sources"),
    ("bmorphism","vibespace-mcp-go-ternary","bmorphism/vibespace-mcp-go-ternary","HTML",0,1,3,"2026-01-11T12:50:40Z","Go MCP experience for vibes and worlds with NATS streaming"),
    ("bmorphism","open-location-code-zig","bmorphism/open-location-code-zig","Zig",3,0,0,"2025-12-30T19:33:45Z","Open Location Code (Plus Codes) for Zig"),
    ("bmorphism","bafishka","bmorphism/bafishka","Clojure",1,0,0,"2025-12-19T09:38:00Z","Rust-native Fish shell-friendly file operations"),
    ("bmorphism","multiverse-color-game","bmorphism/multiverse-color-game","Julia",0,0,0,"2025-12-12T05:28:11Z","2+1D Holographic Color Matching Game"),
    ("bmorphism","monero-rental-hash-war","bmorphism/monero-rental-hash-war","Haskell",1,0,0,"2025-10-05T23:08:54Z","Compositional OpenGame analysis of Monero rental hash war"),
    ("bmorphism","manifold-mcp-server","bmorphism/manifold-mcp-server","JavaScript",14,9,5,"2025-01-11T10:36:58Z","MCP server for interacting with Manifold Markets prediction markets"),
    ("bmorphism","say-mcp-server","bmorphism/say-mcp-server","JavaScript",20,9,3,"2025-01-07T03:15:18Z","MCP server for macOS text-to-speech functionality"),
    ("bmorphism","penumbra-mcp","bmorphism/penumbra-mcp","JavaScript",5,6,3,"2025-01-07T01:15:23Z","MCP server for interacting with Penumbra blockchain"),
    ("bmorphism","nats-mcp-server","bmorphism/nats-mcp-server",None,7,3,2,"2025-01-06T23:33:41Z","MCP server for NATS messaging system"),
    ("bmorphism","marginalia-mcp-server","bmorphism/marginalia-mcp-server","JavaScript",8,6,0,"2025-01-06T05:47:24Z","An MCP server for managing marginalia and annotations"),
    ("bmorphism","babashka-mcp-server","bmorphism/babashka-mcp-server","JavaScript",18,6,3,"2025-01-05T11:09:42Z","A Model Context Protocol server for Babashka"),
    ("bmorphism","penrose-mcp","bmorphism/penrose-mcp","JavaScript",10,4,0,"2025-01-20T21:44:55Z","Penrose server for the Infinity-Topos environment"),
    ("bmorphism","risc0-cosmwasm-example","bmorphism/risc0-cosmwasm-example","Rust",23,2,1,"2022-10-20T23:50:40Z","CosmWasm + zkVM RISC-V EFI template"),
    ("bmorphism","hypernym-mcp-server","bmorphism/hypernym-mcp-server","JavaScript",6,5,0,"2025-04-02T21:21:08Z",None),
    ("bmorphism","slowtime-mcp-server","bmorphism/slowtime-mcp-server","TypeScript",3,5,6,"2025-01-02T01:23:33Z","A Model Context Protocol server for secure time-based operations"),
]
repos += bmorphism_repos

# zubyul (key selection - 30 repos)
zubyul_repos = [
    ("zubyul","voice-observatory","zubyul/voice-observatory","Python",0,0,0,"2026-04-24T05:56:17Z","Passive macOS TUI observing voice-download pathways"),
    ("zubyul","ghostel-emacs-worlds","zubyul/ghostel-emacs-worlds","GLSL",0,0,0,"2026-04-24T00:20:56Z","Ghostty config + ghostel family + alice/bob emacs-mods"),
    ("zubyul","nash-tui","zubyul/nash-tui","Rust",0,0,0,"2026-04-13T07:45:16Z","NASH token TUI: real-time candles; ticker; buy pressure gauge"),
    ("zubyul","nash-web","zubyul/nash-web","Rust",0,0,0,"2026-04-13T07:08:58Z","NASH token browser TUI via ratzilla WASM"),
    ("zubyul","big-bad-plurigrid-quiz","zubyul/big-bad-plurigrid-quiz","Emacs Lisp",0,0,0,"2026-04-09T18:51:31Z","27 flashcards from bmorphism/plurigrid/zubyul recent activity"),
    ("zubyul","Gay.jl","zubyul/Gay.jl","Julia",0,0,0,"2026-03-28T11:30:01Z","Wide-gamut color sampling with splittable determinism"),
    ("zubyul","kinesis-kb360pro","zubyul/kinesis-kb360pro","Python",0,0,0,"2026-03-26T10:29:40Z","Claude Code skill for Kinesis Advantage360 Pro keyboard"),
    ("zubyul","gay-world","zubyul/gay-world","Python",1,1,0,"2026-03-26T04:03:39Z","Goblin world builder: each goblin is a world"),
    ("zubyul","tilelang-kernels","zubyul/tilelang-kernels","Python",0,0,0,"2026-03-16T02:31:13Z","TileLang GPU kernels for SplitMix64 color generation"),
    ("zubyul","gay-terminal-colors","zubyul/gay-terminal-colors","Clojure",0,0,0,"2026-02-21T07:38:14Z","Gay.jl world_terminal_fingerprint: SplitMix64 per-terminal color identity"),
    ("zubyul","plurigrid-site","zubyul/plurigrid-site","Svelte",0,1,11,"2026-02-04T03:20:08Z","Plurigrid world: site deployment"),
    ("zubyul","vibesnipe","zubyul/vibesnipe","Move",0,0,1,"2026-01-30T22:36:03Z",None),
    ("zubyul","zubyul.github.io","zubyul/zubyul.github.io","CSS",1,0,0,"2026-01-27T03:24:34Z",None),
    ("zubyul","toad-warpify-extension","zubyul/toad-warpify-extension","Python",0,0,0,"2026-01-17T07:48:40Z","Warpify extension for Toad"),
    ("zubyul","gay-brain-world","zubyul/gay-brain-world","Python",0,0,0,"2025-12-16T01:19:28Z","Gay.jl SPI colors for Moduleur Brain (Pico) + OpenBCI EEG"),
    ("zubyul","cascade-world","zubyul/cascade-world","Python",1,0,0,"2025-09-19T18:25:12Z","Cascade development environment"),
    ("zubyul","defcon","zubyul/defcon","JavaScript",1,0,0,"2025-09-17T02:07:00Z",None),
    ("zubyul","ghostty-modifications","zubyul/ghostty-modifications","JavaScript",1,0,0,"2025-09-15T02:45:21Z","Ghostty terminal modifications and MCP servers"),
    ("zubyul","jonikas_lab_data_analysis_misc","zubyul/jonikas_lab_data_analysis_misc","Jupyter Notebook",2,0,0,"2023-08-16T20:24:40Z","various scripts used to process large genetic sequence data"),
    ("zubyul","WGCNA","zubyul/WGCNA","HTML",2,0,0,"2023-07-05T18:02:30Z","weighted gene correlation network analysis project"),
]
repos += zubyul_repos

# kubeflow (key selection - 25 repos)
kubeflow_repos = [
    ("kubeflow","kubeflow","kubeflow/kubeflow",None,15704,2669,3,"2026-05-24T11:31:41Z","Machine Learning Toolkit for Kubernetes"),
    ("kubeflow","pipelines","kubeflow/pipelines","Python",4152,2004,490,"2026-06-04T06:43:08Z","Machine Learning Pipelines for Kubeflow"),
    ("kubeflow","spark-operator","kubeflow/spark-operator","Python",3124,1488,101,"2026-06-03T17:01:00Z","Kubernetes operator for managing Apache Spark applications"),
    ("kubeflow","trainer","kubeflow/trainer","Go",2110,964,123,"2026-06-04T04:42:57Z","Distributed AI Model Training and LLM Fine-Tuning on Kubernetes"),
    ("kubeflow","katib","kubeflow/katib","Python",1685,525,121,"2026-06-04T01:14:59Z","Automated Machine Learning on Kubernetes"),
    ("kubeflow","kale","kubeflow/kale","Python",690,155,48,"2026-06-01T23:05:01Z","Kubeflow's superfood for Data Scientists"),
    ("kubeflow","arena","kubeflow/arena","Go",811,191,49,"2026-05-07T06:46:17Z","A CLI for Kubeflow."),
    ("kubeflow","manifests","kubeflow/manifests","YAML",1020,1065,23,"2026-06-04T09:08:05Z","Kubeflow AI Reference Platform Deployment Manifests"),
    ("kubeflow","hub","kubeflow/hub","Go",175,182,41,"2026-06-04T07:43:18Z","Model Registry for ML model developers"),
    ("kubeflow","examples","kubeflow/examples","Jsonnet",1462,756,111,"2025-04-14T01:54:52Z","Extended examples and tutorials"),
    ("kubeflow","community","kubeflow/community","Jupyter Notebook",195,257,17,"2026-06-02T15:52:13Z","Information about the Kubeflow community"),
    ("kubeflow","mpi-operator","kubeflow/mpi-operator","Go",528,235,103,"2026-06-02T14:30:58Z","Kubernetes Operator for MPI-based applications"),
    ("kubeflow","website","kubeflow/website","HTML",184,921,50,"2026-05-28T14:05:25Z","Kubeflow Website"),
    ("kubeflow","mcp-apache-spark-history-server","kubeflow/mcp-apache-spark-history-server","Python",173,61,21,"2026-06-01T19:56:25Z","MCP Server and CLI for Apache Spark History Server"),
    ("kubeflow","notebooks","kubeflow/notebooks",None,73,118,186,"2026-06-04T02:11:40Z","Kubeflow Notebooks for AI/ML workloads"),
    ("kubeflow","sdk","kubeflow/sdk","Python",120,181,136,"2026-06-04T03:07:45Z","Universal Python SDK to run AI workloads on Kubernetes"),
    ("kubeflow","kfp-tekton","kubeflow/kfp-tekton","TypeScript",182,123,79,"2024-11-19T12:23:51Z","Kubeflow Pipelines on Tekton"),
    ("kubeflow","fairing","kubeflow/fairing","Jsonnet",337,143,134,"2022-04-11T05:28:47Z","Python SDK for building; training; and deploying ML models"),
    ("kubeflow","pytorch-operator","kubeflow/pytorch-operator","Jsonnet",310,143,63,"2021-12-01T17:44:48Z","PyTorch on Kubernetes"),
    ("kubeflow","dashboard","kubeflow/dashboard","TypeScript",16,57,84,"2026-06-04T02:16:43Z","Kubeflow Central Dashboard"),
    ("kubeflow","kfctl","kubeflow/kfctl","Go",182,134,94,"2023-08-15T20:19:22Z","kfctl is a CLI for deploying and managing Kubeflow"),
    ("kubeflow","mcp-server","kubeflow/mcp-server","Python",10,19,22,"2026-05-12T10:14:24Z","MCP Server for AI-Assisted Development with Kubeflow"),
    ("kubeflow","docs-agent","kubeflow/docs-agent","Python",37,95,151,"2026-04-14T03:33:15Z","Kubeflow Documentation AI Agent"),
    ("kubeflow","internal-acls","kubeflow/internal-acls","Go",19,388,2,"2026-06-01T16:22:32Z","Repository for group ACLs for Kubeflow developers"),
    ("kubeflow","common","kubeflow/common","Go",53,70,40,"2023-05-28T13:16:00Z","Common APIs and libraries for Kubeflow operators"),
]
repos += kubeflow_repos

# ── INSERT world_increments ───────────────────────────────────────────────────
sources = [
    ("org", "plurigrid", "repo_sweep"),
    ("org", "kubeflow", "repo_sweep"),
    ("org", "TeglonLabs", "repo_sweep"),
    ("user", "bmorphism", "repo_sweep"),
    ("user", "zubyul", "repo_sweep"),
    ("user", "migalkin", "social_graph"),
    ("user", "DJedamski", "social_graph"),
    ("user", "wasita", "social_graph"),
    ("user", "kristinezheng", "social_graph"),
    ("user", "M1shaaa", "social_graph"),
    ("user", "AustinCStone", "social_graph"),
]

now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
increment_id = 1
for src_type, src_name, evt in sources:
    trit, color, name = gf3(increment_id)
    h = hashlib.sha256(f"{src_type}:{src_name}:{now}".encode()).hexdigest()[:16]
    con.execute("""
        INSERT INTO world_increments VALUES (?,?,?,?,?,?,?,?,?,?,?)
    """, [increment_id, now, trit, color, name, src_type, src_name, evt, None, None, h])
    increment_id += 1

# ── INSERT repo_snapshots ─────────────────────────────────────────────────────
repo_id = 1
inc_map = {s[1]: i+1 for i, s in enumerate(sources)}
for r in repos:
    org_or_user, repo_name, full_name, language, stars, forks, open_issues, pushed_at, description = r
    inc_id = inc_map.get(org_or_user, 1)
    trit, color, name = gf3(repo_id)
    con.execute("""
        INSERT INTO repo_snapshots VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
    """, [repo_id, now, inc_id, org_or_user, repo_name, full_name,
          language, stars, forks, open_issues, pushed_at, description])
    repo_id += 1

# ── INSERT aptos_snapshots ────────────────────────────────────────────────────
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
    con.execute("INSERT INTO aptos_snapshots VALUES (?,?,?,?)", [now, world, addr, bal])

# ── INSERT multisig_probes ────────────────────────────────────────────────────
multisig_data = [
    ("A-B","0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003",2,True),
    ("A-G","0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096",2,True),
    ("Y-Z","0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883",2,True),
    ("S-T","0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883",2,True),
    ("V-W","0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d",2,True),
]
for pair, addr, sigs, healthy in multisig_data:
    con.execute("INSERT INTO multisig_probes VALUES (?,?,?,?,?)", [now, pair, addr, sigs, healthy])

# ── VERIFY ────────────────────────────────────────────────────────────────────
print("world_increments:", con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0])
print("repo_snapshots:", con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0])
print("aptos_snapshots:", con.execute("SELECT COUNT(*) FROM aptos_snapshots").fetchone()[0])
print("multisig_probes:", con.execute("SELECT COUNT(*) FROM multisig_probes").fetchone()[0])
print("mnx_snapshots:", con.execute("SELECT COUNT(*) FROM mnx_snapshots").fetchone()[0])

# Top repos by stars
print("\nTop 10 repos by stars:")
for row in con.execute("""
    SELECT org_or_user, repo_name, stars, language
    FROM repo_snapshots ORDER BY stars DESC LIMIT 10
""").fetchall():
    print(f"  {row[0]}/{row[1]}: {row[2]} stars ({row[3]})")

con.close()
print("\nDone — world-increments.duckdb written.")
