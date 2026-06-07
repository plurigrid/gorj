#!/usr/bin/env python3
"""Supplement world-increments DuckDB with bmorphism and zubyul repos."""
import duckdb
import hashlib
from datetime import datetime, timezone

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"

def gf3(id_val):
    trit = id_val % 3
    if trit == 0: return (0, "#d3869b", "ERGODIC")
    elif trit == 1: return (1, "#b8bb26", "PLUS")
    else: return (-1, "#cc241d", "MINUS")

def sha8(s):
    return hashlib.sha256(s.encode()).hexdigest()[:8]

con = duckdb.connect(DB_PATH)
NOW = datetime.now(timezone.utc).isoformat()

# Get current max IDs
max_inc = con.execute("SELECT COALESCE(MAX(id), 0) FROM world_increments").fetchone()[0]
max_repo = con.execute("SELECT COALESCE(MAX(id), 0) FROM repo_snapshots").fetchone()[0]
inc_id = max_inc + 1
repo_id = max_repo + 1

sources = {
    "bmorphism": ("user", [
        ('bmorphism/world','Python',0,0,0,'2026-06-02T06:49:02Z','Local worlds launcher for SA3, jank, and world proofs'),
        ('bmorphism/Gay.jl','Julia',1,0,189,'2026-06-07T00:41:16Z','Wide-gamut color sampling with splittable determinism'),
        ('bmorphism/oxgame','OCaml',0,0,0,'2026-05-15T09:53:27Z','Stellar resolution and open-game composition for OCaml'),
        ('bmorphism/nanoclj-zig','Zig',0,0,0,'2026-05-07T20:12:15Z',''),
        ('bmorphism/zig-syrup','Zig',0,0,0,'2026-05-07T19:49:05Z','Embeddable OCapN Syrup encoder/decoder in Zig'),
        ('bmorphism/boxxy','Move',0,1,0,'2026-04-30T03:35:47Z',''),
        ('bmorphism/postweb','Go',0,0,0,'2026-04-09T10:51:57Z','postweb — evolved from prepostweb'),
        ('bmorphism/shitcoin','Python',5,0,0,'2026-04-08T08:07:08Z','gets denom for cw20 assets for permissionless degeneracy'),
        ('bmorphism/magic-world-org','Python',1,0,0,'2026-04-05T07:03:50Z','Magic World Org (Local MLX)'),
        ('bmorphism/ocaml-mcp-sdk','OCaml',61,2,0,'2026-03-16T05:24:25Z','OCaml SDK for Model Context Protocol'),
        ('bmorphism/flox-mcp-bb','Clojure',0,0,0,'2026-02-12T02:45:43Z','Open-source MCP server for Flox in Babashka/Clojure'),
        ('bmorphism/vibesnipe-market','Move',0,0,9,'2026-02-05T10:23:25Z',''),
        ('bmorphism/tapes',None,0,0,0,'2026-02-04T02:23:37Z','VHS tapes for terminal recordings'),
        ('bmorphism/duck-rio-heateq','Rust',0,0,0,'2026-02-02T23:33:32Z',''),
        ('bmorphism/aella','Rascal',1,0,0,'2026-02-01T02:44:30Z',''),
        ('bmorphism/hymlx','Python',1,0,0,'2026-01-22T12:20:32Z',''),
        ('bmorphism/GeoACSets.jl','Julia',0,1,1,'2026-01-19T13:57:13Z','Categorical data structures with geospatial capabilities'),
        ('bmorphism/anti-bullshit-mcp-server','JavaScript',23,7,1,'2026-01-16T08:54:58Z','MCP server for analyzing claims and detecting manipulation'),
        ('bmorphism/vibespace-mcp-go-ternary','HTML',0,1,3,'2026-01-11T12:50:40Z','Go MCP experience for vibes and worlds with NATS'),
        ('bmorphism/open-location-code-zig','Zig',3,0,0,'2025-12-30T19:33:45Z','Open Location Code (Plus Codes) for Zig'),
        ('bmorphism/bafishka','Clojure',1,0,0,'2025-12-19T09:38:00Z','Rust-native Fish shell-friendly file operations'),
        ('bmorphism/gay-color-learnable',None,0,0,0,'2025-12-15T18:41:02Z','Learnable color embeddings via Gay.jl SPI'),
        ('bmorphism/gay-hy','Hy',0,0,0,'2025-12-15T15:32:58Z','Hylang MLX color bandwidth protocol'),
        ('bmorphism/multiverse-color-game','Julia',0,0,0,'2025-12-12T05:28:11Z','2+1D Holographic Color Matching Game for VisionPro'),
        ('bmorphism/signal-mcp','Rust',0,0,0,'2025-12-11T07:20:08Z','O(n) to O(1) chromatic mode collapse via Galois connection'),
        ('bmorphism/xf.jl','Julia',0,0,0,'2025-12-05T22:12:17Z','Xenofeminist color synthesis via SplittableRandom'),
        ('bmorphism/deberta-goemotions','Python',0,0,0,'2025-10-22T18:32:24Z',''),
        ('bmorphism/monero-rental-hash-war','Haskell',1,0,0,'2025-10-05T23:08:54Z','Compositional OpenGame analysis of Monero rental hash war'),
        ('bmorphism/duck-rs','Zig',0,0,0,'2025-10-05T00:21:07Z',''),
        ('bmorphism/schoenfinkel','Python',1,0,0,'2025-10-04T23:31:11Z','Post-quantum categorical gravity framework'),
        ('bmorphism/gay-spec',None,1,0,0,'2025-10-02T02:01:56Z',''),
        ('bmorphism/bafishka-clean','Rust',1,0,0,'2025-09-25T19:22:10Z','Clean monadic Steel-SCI integration with category theory'),
        ('bmorphism/babashka-static-build','Dockerfile',1,0,0,'2025-09-05T02:26:32Z','Static musl babashka build for ARM64 Termux'),
        ('bmorphism/whale','MATLAB',2,0,0,'2025-09-04T06:55:21Z','omniglot + sperm whale codas = metawhaling'),
        ('bmorphism/infinity-topos','Python',1,0,0,'2025-08-29T05:39:49Z',''),
        ('bmorphism/elevenlabs-mcp-enhanced','Python',1,0,0,'2025-08-29T04:41:58Z','Enhanced ElevenLabs MCP server with universal API key'),
        ('bmorphism/zeldar','Python',1,0,1,'2025-08-26T15:16:21Z','Burning Man Art Robot'),
        ('bmorphism/stellogen-quantum-operads',None,1,0,0,'2025-07-15T04:49:41Z','Quantum Operads and ZX-Calculus in Stellogen'),
        ('bmorphism/apple-container-framework','Clojure',0,0,0,'2025-07-13T12:12:10Z','Apple Container Framework - High-performance Babashka library'),
        ('bmorphism/ezkl-ethglobal2025','Python',1,0,0,'2025-07-07T01:16:01Z',''),
        ('bmorphism/zk-haiku-nanogpt','Solidity',1,0,0,'2025-07-06T03:08:24Z','ZK-Haiku-NanoGPT Agentic Proof-Chaining Framework'),
        ('bmorphism/rama-event-processor','Java',1,0,0,'2025-07-02T07:01:44Z','A repository for processing events with Rama'),
        ('bmorphism/oxcaml-sci-canonical','OCaml',1,0,0,'2025-06-20T06:37:12Z','Canonical OxCaml-SCI implementation'),
        ('bmorphism/oxcaml-mcp',None,0,0,0,'2025-06-20T04:04:34Z','OxCaml-MCP: High-performance MCP server'),
        ('bmorphism/oxcaml-sci',None,0,0,0,'2025-06-20T03:48:11Z','OxCaml-SCI: Performance-optimized Scientific Computing'),
        ('bmorphism/infinity-topos-impossibility',None,0,0,14,'2025-05-29T01:55:28Z','Impossibility results for automated analysis verification'),
        ('bmorphism/graphistry-mcp','Python',2,0,0,'2025-05-06T17:34:24Z','Graphistry MCP integration for graph visualization'),
        ('bmorphism/hypernym-mcp-server','JavaScript',6,5,0,'2025-04-02T21:21:08Z',''),
        ('bmorphism/vibespace-mcp-go',None,0,0,0,'2025-03-19T20:30:02Z','Go MCP experience for vibes and worlds with NATS'),
        ('bmorphism/krep-mcp-server','JavaScript',1,1,1,'2025-03-19T20:22:46Z','High-performance string search MCP server'),
        ('bmorphism/minecraft-mcp-golf',None,0,0,0,'2025-03-16T10:33:31Z','Minecraft server with MCP capabilities'),
        ('bmorphism/worlds-code-explorer',None,0,0,0,'2025-03-16T05:46:58Z','Repository to explore code projects from different worlds'),
        ('bmorphism/voice-fn',None,0,0,0,'2025-02-24T22:28:32Z','Clojure framework for real-time voice-enabled AI'),
        ('bmorphism/lumon-tui','Python',1,0,0,'2025-02-02T11:24:21Z','Terminal parallel worlds inspired by Lumon Industries'),
        ('bmorphism/goose-diagrams',None,0,0,0,'2025-01-31T08:46:44Z','ASCII art diagrams for Goose AI architecture'),
        ('bmorphism/MetaLab',None,0,0,0,'2025-01-30T11:40:33Z','Space for learning cutting-edge technologies'),
        ('bmorphism/penrose-mcp','JavaScript',10,4,0,'2025-01-20T21:44:55Z','Penrose server for the Infinity-Topos environment'),
        ('bmorphism/penrose-mcp-server',None,0,0,0,'2025-01-20T20:24:07Z','MCP server for Penrose system integration'),
        ('bmorphism/test-repo-3141592',None,0,0,1,'2025-01-11T15:06:57Z','Test repository for tool exploration'),
        ('bmorphism/manifold-mcp-server','JavaScript',14,9,5,'2025-01-11T10:36:58Z','MCP server for Manifold Markets prediction markets'),
        ('bmorphism/say-mcp-server','JavaScript',20,9,3,'2025-01-07T03:15:18Z','MCP server for macOS text-to-speech'),
        ('bmorphism/penumbra-mcp','JavaScript',5,6,3,'2025-01-07T01:15:23Z','MCP server for Penumbra blockchain privacy-preserving'),
        ('bmorphism/nats-mcp-server',None,7,3,2,'2025-01-06T23:33:41Z','MCP server for NATS messaging system'),
        ('bmorphism/marginalia-mcp-server','JavaScript',8,6,0,'2025-01-06T05:47:24Z','MCP server for managing marginalia and annotations'),
        ('bmorphism/babashka-mcp-server','JavaScript',19,6,3,'2025-01-05T11:09:42Z','MCP server for interacting with Babashka'),
        ('bmorphism/openbci-mcp-server',None,0,0,0,'2025-01-05T07:00:10Z','MCP server for interfacing with OpenBCI hardware'),
        ('bmorphism/gists-mcp-server','JavaScript',2,0,0,'2025-01-03T03:50:54Z','MCP server for interacting with GitHub Gists'),
        ('bmorphism/neural-category-diagrams',None,0,0,0,'2025-01-02T05:47:22Z','Diagrams exploring neural architectures via category theory'),
        ('bmorphism/slowtime-mcp-server','TypeScript',3,5,6,'2025-01-02T01:23:33Z','MCP server for secure time-based operations'),
        ('bmorphism/open-games-agda','Agda',0,0,0,'2024-12-22T11:16:29Z','Formalization of open games in Agda'),
        ('bmorphism/yoyo','Just',0,0,0,'2024-11-30T04:00:12Z',''),
        ('bmorphism/uss-cogsexy',None,0,0,0,'2024-11-23T20:52:30Z','Cognitive Firewall: information reflow countermeasures'),
        ('bmorphism/vibes','Clojure',0,0,0,'2024-11-13T15:56:28Z','Global Vibespace'),
        ('bmorphism/untime','Swift',1,0,0,'2024-09-06T23:39:08Z',''),
        ('bmorphism/cf','Handlebars',0,0,0,'2024-08-07T01:14:25Z','collective futures'),
        ('bmorphism/collective',None,0,0,0,'2024-08-07T01:08:28Z',''),
        ('bmorphism/pretopos','TeX',0,0,0,'2024-07-27T12:34:14Z',''),
        ('bmorphism/c-house-town','TypeScript',1,0,0,'2024-07-25T21:13:04Z',''),
        ('bmorphism/galahack2024','TypeScript',2,0,0,'2024-03-21T15:48:19Z',''),
        ('bmorphism/crags','Python',1,0,0,'2024-01-14T04:21:45Z','RAGs. categorically.'),
        ('bmorphism/hacker-news-alert-chatgpt-slack','Rust',0,0,0,'2023-08-31T09:56:37Z','Monitor Hacker News posts with ChatGPT summaries'),
        ('bmorphism/summarize-github-issues','Rust',0,0,0,'2023-08-31T09:44:28Z','ChatGPT summarizes GitHub issues'),
        ('bmorphism/slackduck','Rust',0,0,0,'2023-08-31T09:24:05Z','Slack bot with ChatGPT backend'),
        ('bmorphism/telega','Rust',1,0,0,'2023-08-23T17:20:29Z','absurd wasm32-wasi flow connecting components as cdylib'),
        ('bmorphism/io','Handlebars',0,0,0,'2023-08-20T07:15:36Z',''),
        ('bmorphism/mesocunt2001','Rust',0,0,0,'2023-08-19T07:49:43Z','Customized Telegram bot with Claude backend'),
        ('bmorphism/mesocunt','Rust',0,0,0,'2023-08-18T10:13:33Z','Customizable Discord bot with ChatGPT backend'),
        ('bmorphism/meso','Jupyter Notebook',1,1,0,'2023-08-09T06:04:11Z','Scripts simulating inverse transformations of probabilistic'),
        ('bmorphism/monaduck69','Svelte',0,0,1,'2023-07-19T12:43:12Z','SvelteKit template for CodeSandbox Projects'),
        ('bmorphism/banana','Python',0,0,0,'2023-02-23T15:12:07Z',''),
        ('bmorphism/Plurigrid.jl','Julia',0,1,0,'2023-01-04T14:53:02Z',''),
        ('bmorphism/plurigrid-celo','TypeScript',1,1,0,'2022-12-09T10:07:25Z','Celo e-app for Albany Plurigrid'),
        ('bmorphism/risc0-cosmwasm-example','Rust',23,2,1,'2022-10-20T23:50:40Z','CosmWasm + zkVM RISC-V EFI template'),
        ('bmorphism/knxwledge',None,0,1,1,'2022-10-02T02:23:31Z',''),
        ('bmorphism/OTC-0','JavaScript',3,0,0,'2022-06-07T22:18:08Z',''),
        ('bmorphism/matrix5',None,0,0,0,'2022-05-25T06:01:57Z','glowing in public'),
        ('bmorphism/pluridrop','TypeScript',2,0,0,'2022-04-10T00:13:47Z','ETHPortland2022 hack'),
        ('bmorphism/kfsummit19','Python',0,0,0,'2019-10-28T16:40:46Z','Running kubeflow pipelines on Anthos demo'),
        ('bmorphism/recommenders','Python',0,0,0,'2019-09-11T07:43:03Z',''),
        ('bmorphism/deepfakes','Python',1,0,2,'2019-04-28T22:53:40Z',''),
    ]),
    "zubyul": ("user", [
        ('zubyul/voice-observatory','Python',0,0,0,'2026-04-24T05:56:17Z','Passive macOS TUI observing voice-download pathways'),
        ('zubyul/ghostel-emacs-worlds','GLSL',0,0,0,'2026-04-24T00:20:56Z','Ghostty config + ghostel family + alice/bob emacs-mods'),
        ('zubyul/nash-tui','Rust',0,0,0,'2026-04-13T07:45:16Z','NASH token TUI: real-time candles via GeckoTerminal'),
        ('zubyul/nash-web','Rust',0,0,0,'2026-04-13T07:08:58Z','NASH token browser TUI via ratzilla WASM'),
        ('zubyul/big-bad-plurigrid-quiz','Emacs Lisp',0,0,0,'2026-04-09T18:51:31Z','27 flashcards from bmorphism/plurigrid/zubyul activity'),
        ('zubyul/Gay.jl','Julia',0,0,0,'2026-03-28T11:30:01Z','Wide-gamut color sampling with splittable determinism'),
        ('zubyul/kinesis-kb360pro','Python',0,0,0,'2026-03-26T10:29:40Z','Claude Code skill for Kinesis Advantage360 Pro keyboard'),
        ('zubyul/gay-world','Python',1,1,0,'2026-03-26T04:03:39Z','Goblin world builder: MLX task decomposition'),
        ('zubyul/from-possible-worlds','TeX',0,0,0,'2026-03-16T03:14:55Z',''),
        ('zubyul/tilelang-kernels','Python',0,0,0,'2026-03-16T02:31:13Z','TileLang GPU kernels for SplitMix64 color generation'),
        ('zubyul/fleet-bootstrap','Shell',0,0,0,'2026-02-23T08:19:58Z',''),
        ('zubyul/gay-terminal-colors','Clojure',0,0,0,'2026-02-21T07:38:14Z','Gay.jl world_terminal_fingerprint: SplitMix64 color identity'),
        ('zubyul/basin','Rust',0,0,0,'2026-02-13T10:31:47Z',''),
        ('zubyul/openbci-visualizer','Zig',0,0,0,'2026-02-04T11:17:41Z',''),
        ('zubyul/plurigrid-site','Svelte',0,1,11,'2026-02-04T03:20:08Z','Plurigrid world: site deployment'),
        ('zubyul/repl','Python',0,0,0,'2026-02-04T01:08:15Z',''),
        ('zubyul/instance-onboarding','Shell',0,0,0,'2026-02-02T11:44:07Z',''),
        ('zubyul/vibesnipe','Move',0,0,1,'2026-01-30T22:36:03Z',''),
        ('zubyul/zubyul.github.io','CSS',1,0,0,'2026-01-27T03:24:34Z',''),
        ('zubyul/toad-warpify-extension','Python',0,0,0,'2026-01-17T07:48:40Z','Warpify extension for Toad - ACP agents control terminal PTY'),
        ('zubyul/thread-site','Haskell',0,0,0,'2025-12-23T23:53:27Z',''),
        ('zubyul/GayMove','Move',0,0,0,'2025-12-18T09:40:08Z',''),
        ('zubyul/gay-brain-world','Python',0,0,0,'2025-12-16T01:19:28Z','Gay.jl SPI colors for Moduleur Brain (Pico) + OpenBCI EEG'),
        ('zubyul/multiplayer','HTML',0,0,0,'2025-12-12T08:56:16Z',''),
        ('zubyul/cat-world','TypeScript',0,0,0,'2025-12-12T08:47:14Z','Cat gaze tracker - shows bird videos to cats'),
        ('zubyul/hue-world','JavaScript',0,0,0,'2025-12-12T08:32:59Z','Terminal Vibe Snipe puzzle game with ANSI true color'),
        ('zubyul/multiplayer-emacs','HTML',0,0,0,'2025-12-12T08:07:38Z','Multiplayer world: Emacs split-pane Vibe Snipe'),
        ('zubyul/vibe-snipe','Kotlin',0,0,0,'2025-12-12T03:46:26Z',''),
        ('zubyul/chromatic-vrf','Kotlin',0,0,0,'2025-12-12T03:26:22Z','Chromatic VRF: I Love Hue puzzle with Gay.jl MCMC'),
        ('zubyul/quantum-telephone','Jupyter Notebook',0,0,0,'2025-12-08T22:54:16Z','Quantum telephone world: entangled message passing'),
        ('zubyul/c-elegans-connectome','JavaScript',0,0,0,'2025-11-22T15:43:55Z',''),
        ('zubyul/zoterobsidian','Shell',0,0,0,'2025-09-28T16:50:50Z',''),
        ('zubyul/cascade-world','Python',1,0,0,'2025-09-19T18:25:12Z','Cascade development environment'),
        ('zubyul/plurigrid-playbook',None,0,0,0,'2025-09-17T02:10:35Z',''),
        ('zubyul/defcon','JavaScript',1,0,0,'2025-09-17T02:07:00Z',''),
        ('zubyul/ghostty-modifications','JavaScript',1,0,0,'2025-09-15T02:45:21Z','Ghostty terminal modifications and MCP servers'),
        ('zubyul/GoofyLifeChoices','Python',1,0,0,'2025-07-30T18:48:13Z',''),
        ('zubyul/book','HTML',0,0,0,'2025-05-15T20:30:39Z',''),
        ('zubyul/ezAR',None,0,0,0,'2025-02-03T21:02:26Z',''),
        ('zubyul/obsidian',None,0,0,0,'2024-05-24T18:26:28Z',''),
        ('zubyul/private','SCSS',0,0,0,'2023-10-05T21:03:16Z',''),
        ('zubyul/jonikas_for_weronika.-annotated-code','Jupyter Notebook',1,0,0,'2023-08-17T02:46:42Z',''),
        ('zubyul/jonikas_lab_data_analysis_misc','Jupyter Notebook',2,0,0,'2023-08-16T20:24:40Z','Various scripts for large genetic sequence data'),
        ('zubyul/WGCNA','HTML',2,0,0,'2023-07-05T18:02:30Z','Weighted gene correlation network analysis project'),
        ('zubyul/Dr_Niv_Qs','Jupyter Notebook',0,0,0,'2023-06-29T04:46:41Z',"Dr. Niv's Interview Questions"),
        ('zubyul/reddit_scraper','Python',0,0,0,'2023-06-16T14:06:07Z',''),
        ('zubyul/Python_Undergrad','Python',0,0,0,'2023-06-16T14:02:18Z',''),
        ('zubyul/Nikolova_lab_data_analysis','R',2,0,0,'2023-06-16T13:56:58Z','Undergraduate thesis - Human Connectome Project data'),
        ('zubyul/lastfm_analysis_copy','Jupyter Notebook',1,0,0,'2023-06-15T22:20:35Z','lastfm data analysis'),
    ]),
}

for source_name, (source_type, repos) in sources.items():
    trit, color, name = gf3(inc_id)
    snap_hash = sha8(f"{source_name}:{NOW}")
    con.execute("""
        INSERT INTO world_increments VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [inc_id, NOW, trit, color, name, source_type, source_name,
          "repo_sweep", None, None, snap_hash])

    for repo in repos:
        full_name, language, stars, forks, issues, pushed_at, desc = repo
        org_or_user = full_name.split('/')[0]
        repo_name = full_name.split('/')[1]
        con.execute("""
            INSERT INTO repo_snapshots VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, [repo_id, NOW, inc_id, org_or_user, repo_name, full_name,
              language, stars, forks, issues, pushed_at, desc])
        repo_id += 1

    print(f"  {source_name}: {len(repos)} repos inserted (inc_id={inc_id}, gf3={name} {color})")
    inc_id += 1

total_repos = con.execute("SELECT COUNT(*) FROM repo_snapshots").fetchone()[0]
total_incs  = con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0]
print(f"\nDB totals: {total_incs} world_increments, {total_repos} repo_snapshots")
con.close()
print("Supplement done.")
