#!/usr/bin/env python3
"""Append bmorphism and zubyul repos to world-increments DuckDB."""
import duckdb, hashlib, os

DB = os.path.join(os.path.dirname(__file__), "world-increments.duckdb")
con = duckdb.connect(DB)

def gf3(id_val):
    r = id_val % 3
    if r == 0:   return (0,  "#d3869b", "ERGODIC")
    elif r == 1: return (1,  "#b8bb26", "PLUS")
    else:        return (-1, "#cc241d", "MINUS")

def snap_hash(s):
    return hashlib.sha256(s.encode()).hexdigest()[:16]

# Get current max IDs
cur_inc = con.execute("SELECT COALESCE(MAX(id), 0) FROM world_increments").fetchone()[0]
cur_rep = con.execute("SELECT COALESCE(MAX(id), 0) FROM repo_snapshots").fetchone()[0]
inc_id = cur_inc + 1
repo_id = cur_rep + 1

repos = [
  # bmorphism (100 repos)
  ("bmorphism","bmorphism/zeldar","Python",1,0,1,"2025-08-26T15:16:21Z","Burning Man Art Robot"),
  ("bmorphism","bmorphism/matrix5","",0,0,0,"2022-05-25T06:01:57Z","glowing in public"),
  ("bmorphism","bmorphism/infinity-topos-impossibility","",0,0,14,"2025-05-29T01:55:28Z","Impossibility results for automated analysis verification"),
  ("bmorphism","bmorphism/signal-mcp","Rust",0,0,0,"2025-12-11T07:20:08Z","O(n)→O(1) chromatic mode collapse via Galois connection"),
  ("bmorphism","bmorphism/gay-color-learnable","",0,0,0,"2025-12-15T18:41:02Z","Learnable color embeddings connecting Graphistry, Ghidra, Charm via Gay.jl SPI"),
  ("bmorphism","bmorphism/manifold-mcp-server","JavaScript",14,9,5,"2025-01-11T10:36:58Z","MCP server for interacting with Manifold Markets prediction markets"),
  ("bmorphism","bmorphism/graphistry-mcp","Python",2,0,0,"2025-05-06T17:34:24Z","Graphistry MCP integration for graph visualization with LLM workflows"),
  ("bmorphism","bmorphism/whale","MATLAB",2,0,0,"2025-09-04T06:55:21Z","omniglot + sperm whale codas = metawhaling"),
  ("bmorphism","bmorphism/monero-rental-hash-war","Haskell",1,0,0,"2025-10-05T23:08:54Z","Compositional OpenGame analysis of Monero rental hash war with live network integration"),
  ("bmorphism","bmorphism/io","Handlebars",0,0,0,"2023-08-20T07:15:36Z",""),
  ("bmorphism","bmorphism/rama-event-processor","Java",1,0,0,"2025-07-02T07:01:44Z","A repository for processing events with Rama"),
  ("bmorphism","bmorphism/talks","JavaScript",3,1,0,"2017-11-14T23:07:43Z",""),
  ("bmorphism","bmorphism/minecraft-mcp-golf","",0,0,0,"2025-03-16T10:33:31Z","Minecraft server with MCP capabilities maximizing features in minimal steps"),
  ("bmorphism","bmorphism/lumon-tui","Python",1,0,0,"2025-02-02T11:24:21Z","A terminal-based parallel worlds implementation inspired by Lumon Industries"),
  ("bmorphism","bmorphism/krep-mcp-server","JavaScript",1,1,1,"2025-03-19T20:22:46Z","High-performance string search MCP server with automatic CPU core scaling"),
  ("bmorphism","bmorphism/mesocunt2001","Rust",0,0,0,"2023-08-19T07:49:43Z","A customized Telegram bot with a Claude backend."),
  ("bmorphism","bmorphism/open-location-code-zig","Zig",3,0,0,"2025-12-30T19:33:45Z","Open Location Code (Plus Codes) for Zig - First-ever Zig implementation of Google's geocoding system"),
  ("bmorphism","bmorphism/yoyo","Just",0,0,0,"2024-11-30T04:00:12Z",""),
  ("bmorphism","bmorphism/babashka-mcp-server","JavaScript",18,6,3,"2025-01-05T11:09:42Z","A Model Context Protocol server for interacting with Babashka, a native Clojure interpreter for scripting"),
  ("bmorphism","bmorphism/anti-bullshit-mcp-server","JavaScript",23,7,1,"2026-01-16T08:54:58Z","MCP server for analyzing claims, validating sources, and detecting manipulation"),
  ("bmorphism","bmorphism/MetaLab","",0,0,0,"2025-01-30T11:40:33Z","A space for learning and experimenting with cutting-edge technologies"),
  ("bmorphism","bmorphism/worlds-code-explorer","",0,0,0,"2025-03-16T05:46:58Z","A repository to explore and organize code projects from different worlds"),
  ("bmorphism","bmorphism/meso","Jupyter Notebook",1,1,0,"2023-08-09T06:04:11Z","Scripts simulating the approximation of inverse transformations of probabilistic Markov Kernels"),
  ("bmorphism","bmorphism/gists-mcp-server","JavaScript",2,0,0,"2025-01-03T03:50:54Z","An MCP server for interacting with GitHub Gists"),
  ("bmorphism","bmorphism/Gay.jl","Julia",1,0,188,"2026-05-15T12:46:39Z","Wide-gamut color sampling with splittable determinism (Pigeons.jl SPI pattern) + LispSyntax"),
  ("bmorphism","bmorphism/marginalia-mcp-server","JavaScript",8,6,0,"2025-01-06T05:47:24Z","An MCP server implementation for managing marginalia and annotations"),
  ("bmorphism","bmorphism/infinity-topos","Python",1,0,0,"2025-08-29T05:39:49Z",""),
  ("bmorphism","bmorphism/bafishka-clean","Rust",1,0,0,"2025-09-25T19:22:10Z","Clean monadic Steel-SCI integration with category theory"),
  ("bmorphism","bmorphism/banana","Python",0,0,0,"2023-02-23T15:12:07Z",""),
  ("bmorphism","bmorphism/openbci-mcp-server","",0,0,0,"2025-01-05T07:00:10Z","MCP server for interfacing with OpenBCI hardware"),
  ("bmorphism","bmorphism/oxcaml-sci-canonical","OCaml",1,0,0,"2025-06-20T06:37:12Z","Canonical OxCaml-SCI implementation with actor-critic verification"),
  ("bmorphism","bmorphism/deberta-goemotions","Python",0,0,0,"2025-10-22T18:32:24Z",""),
  ("bmorphism","bmorphism/gay-hy","Hy",0,0,0,"2025-12-15T15:32:58Z","Hylang MLX color bandwidth protocol - 2B+ colors/sec with SPI guarantees"),
  ("bmorphism","bmorphism/penumbra-mcp","JavaScript",5,6,3,"2025-01-07T01:15:23Z","MCP server for interacting with Penumbra blockchain"),
  ("bmorphism","bmorphism/say-mcp-server","JavaScript",20,9,3,"2025-01-07T03:15:18Z","MCP server for macOS text-to-speech functionality"),
  ("bmorphism","bmorphism/multiverse-color-game","Julia",0,0,0,"2025-12-12T05:28:11Z","2+1D Holographic Color Matching Game for VisionPro"),
  ("bmorphism","bmorphism/slackduck","Rust",0,0,0,"2023-08-31T09:24:05Z","A Slack bot with a ChatGPT backend."),
  ("bmorphism","bmorphism/pretopos","TeX",0,0,0,"2024-07-27T12:34:14Z",""),
  ("bmorphism","bmorphism/untime","Swift",1,0,0,"2024-09-06T23:39:08Z",""),
  ("bmorphism","bmorphism/hacker-news-alert-chatgpt-slack","Rust",0,0,0,"2023-08-31T09:56:37Z","Monitor the Hacker News post you're interested in and let ChatGPT give you a summary"),
  ("bmorphism","bmorphism/GeoACSets.jl","Julia",0,1,1,"2026-01-19T13:57:13Z","Categorical data structures (ACSets) with geospatial capabilities"),
  ("bmorphism","bmorphism/elevenlabs-mcp-enhanced","Python",1,0,0,"2025-08-29T04:41:58Z","Enhanced ElevenLabs MCP server with universal API key support and V3 features"),
  ("bmorphism","bmorphism/nanoclj-zig","Zig",0,0,0,"2026-05-07T20:12:15Z",""),
  ("bmorphism","bmorphism/vibesnipe-market","Move",0,0,9,"2026-02-05T10:23:25Z",""),
  ("bmorphism","bmorphism/duck-rio-heateq","Rust",0,0,0,"2026-02-02T23:33:32Z",""),
  ("bmorphism","bmorphism/gay-spec","",1,0,0,"2025-10-02T02:01:56Z",""),
  ("bmorphism","bmorphism/deepfakes","Python",1,0,2,"2019-04-28T22:53:40Z",""),
  ("bmorphism","bmorphism/knxwledge","",0,1,1,"2022-10-02T02:23:31Z",""),
  ("bmorphism","bmorphism/c-house-town","TypeScript",1,0,0,"2024-07-25T21:13:04Z",""),
  ("bmorphism","bmorphism/penrose-mcp","JavaScript",10,4,0,"2025-01-20T21:44:55Z","Penrose server for the Infinity-Topos environment"),
  ("bmorphism","bmorphism/boxxy","Move",0,1,0,"2026-04-30T03:35:47Z",""),
  ("bmorphism","bmorphism/hymlx","Python",1,0,0,"2026-01-22T12:20:32Z",""),
  ("bmorphism","bmorphism/apple-container-framework","Clojure",0,0,0,"2025-07-13T12:12:10Z","Apple Container Framework - High-performance Babashka library for VM snapshots"),
  ("bmorphism","bmorphism/cf","Handlebars",0,0,0,"2024-08-07T01:14:25Z","collective futures"),
  ("bmorphism","bmorphism/neural-category-diagrams","",0,0,0,"2025-01-02T05:47:22Z","A collection of diagrams exploring neural architectures through category theory"),
  ("bmorphism","bmorphism/plurigrid-celo","TypeScript",1,1,0,"2022-12-09T10:07:25Z","Celo e-app for Albany Plurigrid"),
  ("bmorphism","bmorphism/postweb","Go",0,0,0,"2026-04-09T10:51:57Z","postweb — evolved from prepostweb"),
  ("bmorphism","bmorphism/ezkl-ethglobal2025","Python",1,0,0,"2025-07-07T01:16:01Z",""),
  ("bmorphism","bmorphism/schoenfinkel","Python",1,0,0,"2025-10-04T23:31:11Z","Post-quantum categorical gravity framework"),
  ("bmorphism","bmorphism/recommenders","Python",0,0,0,"2019-09-11T07:43:03Z",""),
  ("bmorphism","bmorphism/summarize-github-issues","Rust",0,0,0,"2023-08-31T09:44:28Z","Comment the trigger phrase under a GitHub issue, ChatGPT will summarize it"),
  ("bmorphism","bmorphism/voice-fn","",0,0,0,"2025-02-24T22:28:32Z","A Clojure framework for building real-time voice-enabled AI applications"),
  ("bmorphism","bmorphism/duck-rs","Zig",0,0,0,"2025-10-05T00:21:07Z",""),
  ("bmorphism","bmorphism/vibespace-mcp-go-ternary","HTML",0,1,3,"2026-01-11T12:50:40Z","Go implementation of a MCP experience for vibes and worlds with NATS streaming and balanced ternary"),
  ("bmorphism","bmorphism/ocaml-mcp-sdk","OCaml",61,2,0,"2026-03-16T05:24:25Z","OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect library"),
  ("bmorphism","bmorphism/tapes","",0,0,0,"2026-02-04T02:23:37Z","VHS tapes for terminal recordings"),
  ("bmorphism","bmorphism/xf.jl","Julia",0,0,0,"2025-12-05T22:12:17Z","Xenofeminist color synthesis — deterministic wide-gamut colors via SplittableRandoms.jl"),
  ("bmorphism","bmorphism/open-games-agda","Agda",0,0,0,"2024-12-22T11:16:29Z","A formalization of open games in Agda, building on lenses and Markov categories"),
  ("bmorphism","bmorphism/penrose-mcp-server","",0,0,0,"2025-01-20T20:24:07Z","MCP server for Penrose system integration"),
  ("bmorphism","bmorphism/crags","Python",1,0,0,"2024-01-14T04:21:45Z","RAGs. categorically."),
  ("bmorphism","bmorphism/mesocunt","Rust",0,0,0,"2023-08-18T10:13:33Z","A customizable Discord bot with a ChatGPT backend."),
  ("bmorphism","bmorphism/telega","Rust",1,0,0,"2023-08-23T17:20:29Z","absurd wasm32-wasi flow connecting any components supported as cdylib"),
  ("bmorphism","bmorphism/test-repo-3141592","",0,0,1,"2025-01-11T15:06:57Z","Test repository for tool exploration"),
  ("bmorphism","bmorphism/flox-mcp-bb","Clojure",0,0,0,"2026-02-12T02:45:43Z","Open-source MCP server for Flox — Babashka/Clojure, single file, 20 tools"),
  ("bmorphism","bmorphism/oxcaml-sci","",0,0,0,"2025-06-20T03:48:11Z","OxCaml-SCI: Performance-optimized Scientific Computing Interface"),
  ("bmorphism","bmorphism/zk-haiku-nanogpt","Solidity",1,0,0,"2025-07-06T03:08:24Z","ZK-Haiku-NanoGPT: Agentic Proof-Chaining Framework"),
  ("bmorphism","bmorphism/goose-diagrams","",0,0,0,"2025-01-31T08:46:44Z","ASCII art diagrams representing Goose AI architecture and flows"),
  ("bmorphism","bmorphism/hypernym-mcp-server","JavaScript",6,5,0,"2025-04-02T21:21:08Z",""),
  ("bmorphism","bmorphism/galahack2024","TypeScript",2,0,0,"2024-03-21T15:48:19Z",""),
  ("bmorphism","bmorphism/monaduck69","Svelte",0,0,1,"2023-07-19T12:43:12Z","SvelteKit template for CodeSandbox Projects"),
  ("bmorphism","bmorphism/oxcaml-mcp","",0,0,0,"2025-06-20T04:04:34Z","OxCaml-MCP: High-performance Model Control Protocol server"),
  ("bmorphism","bmorphism/magic-world-org","Python",1,0,0,"2026-04-05T07:03:50Z","Magic World Org (Local MLX) - renamed from magic-todo-org"),
  ("bmorphism","bmorphism/kfsummit19","Python",0,0,0,"2019-10-28T16:40:46Z","Example of running kubeflow pipelines on Anthos"),
  ("bmorphism","bmorphism/aella","Rascal",1,0,0,"2026-02-01T02:44:30Z",""),
  ("bmorphism","bmorphism/vibespace-mcp-go","",0,0,0,"2025-03-19T20:30:02Z","Go implementation of a MCP experience for vibes and worlds with NATS streaming"),
  ("bmorphism","bmorphism/pluridrop","TypeScript",2,0,0,"2022-04-10T00:13:47Z","ETHPortland2022 hack"),
  ("bmorphism","bmorphism/babashka-static-build","Dockerfile",1,0,0,"2025-09-05T02:26:32Z","Static musl babashka build for ARM64 Termux"),
  ("bmorphism","bmorphism/stellogen-quantum-operads","",1,0,0,"2025-07-15T04:49:41Z","Quantum Operads and ZX-Calculus Implementation in Stellogen"),
  ("bmorphism","bmorphism/woodbridge-lstm","Jupyter Notebook",1,1,0,"2017-11-15T01:48:15Z","PyTorch implementation of Woodridge, Anderson, et al paper"),
  ("bmorphism","bmorphism/dotemacs","Emacs Lisp",1,0,0,"2019-03-29T22:57:59Z",""),
  ("bmorphism","bmorphism/slowtime-mcp-server","TypeScript",3,5,6,"2025-01-02T01:23:33Z","A Model Context Protocol server for secure time-based operations"),
  ("bmorphism","bmorphism/Plurigrid.jl","Julia",0,1,0,"2023-01-04T14:53:02Z",""),
  ("bmorphism","bmorphism/collective","",0,0,0,"2024-08-07T01:08:28Z",""),
  ("bmorphism","bmorphism/risc0-cosmwasm-example","Rust",23,2,1,"2022-10-20T23:50:40Z","CosmWasm + zkVM RISC-V EFI template"),
  ("bmorphism","bmorphism/uss-cogsexy","",0,0,0,"2024-11-23T20:52:30Z","Cognitive Firewall: information reflow and non-linear countermeasures"),
  ("bmorphism","bmorphism/bafishka","Clojure",1,0,0,"2025-12-19T09:38:00Z","Rust-native Fish shell-friendly file operations with Steel-backed SCI Clojure evaluation"),
  ("bmorphism","bmorphism/OTC-0","JavaScript",3,0,0,"2022-06-07T22:18:08Z",""),
  ("bmorphism","bmorphism/zig-syrup","Zig",0,0,0,"2026-05-07T19:49:05Z","Embeddable OCapN Syrup encoder/decoder in Zig — 550 LOC, 22 tests"),
  ("bmorphism","bmorphism/nats-mcp-server","",7,3,2,"2025-01-06T23:33:41Z","MCP server for NATS messaging system"),
  ("bmorphism","bmorphism/vibes","Clojure",0,0,0,"2024-11-13T15:56:28Z","Global Vibespace"),
  # zubyul (49 repos)
  ("zubyul","zubyul/repl","Python",0,0,0,"2026-02-04T01:08:15Z",""),
  ("zubyul","zubyul/ezAR","",0,0,0,"2025-02-03T21:02:26Z",""),
  ("zubyul","zubyul/toad-warpify-extension","Python",0,0,0,"2026-01-17T07:48:40Z","Warpify extension for Toad - enables ACP agents to control terminal PTY directly"),
  ("zubyul","zubyul/quantum-telephone","Jupyter Notebook",0,0,0,"2025-12-08T22:54:16Z","Quantum telephone world: entangled message passing"),
  ("zubyul","zubyul/obsidian","",0,0,0,"2024-05-24T18:26:28Z",""),
  ("zubyul","zubyul/multiplayer","HTML",0,0,0,"2025-12-12T08:56:16Z",""),
  ("zubyul","zubyul/reddit_scraper","Python",0,0,0,"2023-06-16T14:06:07Z",""),
  ("zubyul","zubyul/gay-world","Python",1,1,0,"2026-03-26T04:03:39Z","Goblin world builder: each goblin is a world. MLX task decomposition → composable persistent worlds"),
  ("zubyul","zubyul/big-bad-plurigrid-quiz","Emacs Lisp",0,0,0,"2026-04-09T18:51:31Z","27 flashcards from bmorphism/plurigrid/zubyul/monaduck1069 recent activity + Emacs drill"),
  ("zubyul","zubyul/instance-onboarding","Shell",0,0,0,"2026-02-02T11:44:07Z",""),
  ("zubyul","zubyul/cascade-world","Python",1,0,0,"2025-09-19T18:25:12Z","Cascade development environment"),
  ("zubyul","zubyul/jonikas_for_weronika.-annotated-code","Jupyter Notebook",1,0,0,"2023-08-17T02:46:42Z",""),
  ("zubyul","zubyul/thread-site","Haskell",0,0,0,"2025-12-23T23:53:27Z",""),
  ("zubyul","zubyul/chromatic-vrf","Kotlin",0,0,0,"2025-12-12T03:26:22Z","Chromatic VRF: I Love Hue puzzle with Gay.jl MCMC and EG-Walker CRDT multiplayer"),
  ("zubyul","zubyul/ghostty-modifications","JavaScript",1,0,0,"2025-09-15T02:45:21Z","Ghostty terminal modifications and MCP servers"),
  ("zubyul","zubyul/ghostel-emacs-worlds","GLSL",0,0,0,"2026-04-24T00:20:56Z","Ghostty config + ghostel family + alice/bob emacs-mods"),
  ("zubyul","zubyul/WGCNA","HTML",2,0,0,"2023-07-05T18:02:30Z","weighted gene correlation network analysis project"),
  ("zubyul","zubyul/private","SCSS",0,0,0,"2023-10-05T21:03:16Z",""),
  ("zubyul","zubyul/Gay.jl","Julia",0,0,0,"2026-03-28T11:30:01Z","Wide-gamut color sampling with splittable determinism (Pigeons.jl SPI pattern) + LispSyntax"),
  ("zubyul","zubyul/zubyul.github.io","CSS",1,0,0,"2026-01-27T03:24:34Z",""),
  ("zubyul","zubyul/openbci-visualizer","Zig",0,0,0,"2026-02-04T11:17:41Z",""),
  ("zubyul","zubyul/jonikas_lab_data_analysis_misc","Jupyter Notebook",2,0,0,"2023-08-16T20:24:40Z","various scripts used to process large genetic sequence data"),
  ("zubyul","zubyul/defcon","JavaScript",1,0,0,"2025-09-17T02:07:00Z",""),
  ("zubyul","zubyul/nash-tui","Rust",0,0,0,"2026-04-13T07:45:16Z","NASH token TUI: real-time candles, ticker, buy pressure gauge via GeckoTerminal OHLCV"),
  ("zubyul","zubyul/plurigrid-playbook","",0,0,0,"2025-09-17T02:10:35Z",""),
  ("zubyul","zubyul/fleet-bootstrap","Shell",0,0,0,"2026-02-23T08:19:58Z",""),
  ("zubyul","zubyul/kinesis-kb360pro","Python",0,0,0,"2026-03-26T10:29:40Z","Claude Code skill for Kinesis Advantage360 Pro keyboard"),
  ("zubyul","zubyul/GoofyLifeChoices","Python",1,0,0,"2025-07-30T18:48:13Z",""),
  ("zubyul","zubyul/cat-world","TypeScript",0,0,0,"2025-12-12T08:47:14Z","Cat gaze tracker - shows bird videos to cats and tracks their preferences"),
  ("zubyul","zubyul/GayMove","Move",0,0,0,"2025-12-18T09:40:08Z",""),
  ("zubyul","zubyul/Dr_Niv_Qs","Jupyter Notebook",0,0,0,"2023-06-29T04:44:01Z","Dr. Niv's Interview Questions"),
  ("zubyul","zubyul/lastfm_analysis_copy","Jupyter Notebook",1,0,0,"2023-06-15T22:20:35Z","lastfm data analysis"),
  ("zubyul","zubyul/gay-terminal-colors","Clojure",0,0,0,"2026-02-21T07:38:14Z","Gay.jl world_terminal_fingerprint: SplitMix64 per-terminal color identity"),
  ("zubyul","zubyul/voice-observatory","Python",0,0,0,"2026-04-24T05:56:17Z","Passive macOS TUI observing voice-download pathways"),
  ("zubyul","zubyul/hue-world","JavaScript",0,0,0,"2025-12-12T08:32:59Z","Terminal Vibe Snipe puzzle game with ANSI true color"),
  ("zubyul","zubyul/Python_Undergrad","Python",0,0,0,"2023-06-16T14:02:18Z",""),
  ("zubyul","zubyul/Nikolova_lab_data_analysis","R",2,0,0,"2023-06-16T13:56:58Z","undergraduate thesis - using Human Connectome Project data to study cortical thickness"),
  ("zubyul","zubyul/book","HTML",0,0,0,"2025-05-15T20:30:39Z",""),
  ("zubyul","zubyul/tilelang-kernels","Python",0,0,0,"2026-03-16T02:31:13Z","TileLang GPU kernels for SplitMix64 color generation and GF(3) trit classification"),
  ("zubyul","zubyul/from-possible-worlds","TeX",0,0,0,"2026-03-16T03:14:55Z",""),
  ("zubyul","zubyul/multiplayer-emacs","HTML",0,0,0,"2025-12-12T08:07:38Z","Multiplayer world: Emacs split-pane Vibe Snipe with Gay SPI goblin swarm"),
  ("zubyul","zubyul/nash-web","Rust",0,0,0,"2026-04-13T07:08:58Z","NASH token browser TUI via ratzilla WASM + GeckoTerminal OHLCV"),
  ("zubyul","zubyul/c-elegans-connectome","JavaScript",0,0,0,"2025-11-22T15:43:55Z",""),
  ("zubyul","zubyul/vibesnipe","Move",0,0,1,"2026-01-30T22:36:03Z",""),
  ("zubyul","zubyul/basin","Rust",0,0,0,"2026-02-13T10:31:47Z",""),
  ("zubyul","zubyul/zoterobsidian","Shell",0,0,0,"2025-09-28T16:50:50Z",""),
  ("zubyul","zubyul/gay-brain-world","Python",0,0,0,"2025-12-16T01:19:28Z","Gay.jl SPI colors for Moduleur Brain (Pico) + OpenBCI EEG"),
  ("zubyul","zubyul/vibe-snipe","Kotlin",0,0,0,"2025-12-12T03:46:26Z",""),
  ("zubyul","zubyul/plurigrid-site","Svelte",0,1,11,"2026-02-04T03:20:08Z","Plurigrid world: site deployment"),
]

for (org, full_name, lang, stars, forks, issues, pushed_at, desc) in repos:
    trit, color, name = gf3(inc_id)
    h = snap_hash(full_name + pushed_at)
    repo_short = full_name.split("/", 1)[-1]
    con.execute("""
      INSERT INTO world_increments VALUES (?, now(), ?, ?, ?, 'github_repo', ?, 'repo_push', ?, ?, ?)
    """, [inc_id, trit, color, name, org, repo_short, org, h])
    con.execute("""
      INSERT INTO repo_snapshots VALUES (?, now(), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [repo_id, inc_id, org, repo_short, full_name, lang or None,
          stars, forks, issues, pushed_at, desc or None])
    inc_id += 1
    repo_id += 1

print(f"Inserted {len(repos)} bmorphism+zubyul repos")
total = con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0]
print(f"Total world_increments now: {total}")
con.close()
print("Done.")
