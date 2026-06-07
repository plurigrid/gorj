#!/usr/bin/env python3
"""Append bmorphism repos to world-increments DuckDB."""
import duckdb

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
con = duckdb.connect(DB)

def gf3(i):
    t = i % 3
    if t == 0: return (0, "#d3869b", "ERGODIC")
    if t == 1: return (1, "#b8bb26", "PLUS")
    return (-1, "#cc241d", "MINUS")

inc = con.execute("SELECT id FROM world_increments WHERE source_name='bmorphism' LIMIT 1").fetchone()
inc_id = inc[0] if inc else 4

start_id = (con.execute("SELECT COALESCE(MAX(id),0) FROM repo_snapshots").fetchone()[0] or 0) + 1

BMORPHISM = [
{"rn":"Gay.jl","fn":"bmorphism/Gay.jl","lang":"Julia","s":1,"f":0,"oi":189,"pa":"2026-06-07T00:41:16Z","d":"Wide-gamut color sampling with splittable determinism"},
{"rn":"ocaml-mcp-sdk","fn":"bmorphism/ocaml-mcp-sdk","lang":"OCaml","s":61,"f":2,"oi":0,"pa":"2026-03-16T05:24:25Z","d":"OCaml SDK for Model Context Protocol"},
{"rn":"anti-bullshit-mcp-server","fn":"bmorphism/anti-bullshit-mcp-server","lang":"JavaScript","s":23,"f":7,"oi":1,"pa":"2026-01-16T08:54:58Z","d":"Analyzing claims and detecting manipulation"},
{"rn":"risc0-cosmwasm-example","fn":"bmorphism/risc0-cosmwasm-example","lang":"Rust","s":23,"f":2,"oi":1,"pa":"2022-10-20T23:50:40Z","d":"CosmWasm + zkVM RISC-V EFI template"},
{"rn":"say-mcp-server","fn":"bmorphism/say-mcp-server","lang":"JavaScript","s":20,"f":9,"oi":3,"pa":"2025-01-07T03:15:18Z","d":"MCP server for macOS text-to-speech"},
{"rn":"babashka-mcp-server","fn":"bmorphism/babashka-mcp-server","lang":"JavaScript","s":19,"f":6,"oi":3,"pa":"2025-01-05T11:09:42Z","d":"MCP server for Babashka Clojure"},
{"rn":"manifold-mcp-server","fn":"bmorphism/manifold-mcp-server","lang":"JavaScript","s":14,"f":9,"oi":5,"pa":"2025-01-11T10:36:58Z","d":"MCP server for Manifold Markets"},
{"rn":"marginalia-mcp-server","fn":"bmorphism/marginalia-mcp-server","lang":"JavaScript","s":8,"f":6,"oi":0,"pa":"2025-01-06T05:47:24Z","d":"MCP server for marginalia and annotations"},
{"rn":"nats-mcp-server","fn":"bmorphism/nats-mcp-server","lang":None,"s":7,"f":3,"oi":2,"pa":"2025-01-06T23:33:41Z","d":"MCP server for NATS messaging"},
{"rn":"hypernym-mcp-server","fn":"bmorphism/hypernym-mcp-server","lang":"JavaScript","s":6,"f":5,"oi":0,"pa":"2025-04-02T21:21:08Z","d":None},
{"rn":"shitcoin","fn":"bmorphism/shitcoin","lang":"Python","s":5,"f":0,"oi":0,"pa":"2026-04-08T08:07:08Z","d":"denom for cw20 assets for permissionless degeneracy"},
{"rn":"penumbra-mcp","fn":"bmorphism/penumbra-mcp","lang":"JavaScript","s":5,"f":6,"oi":3,"pa":"2025-01-07T01:15:23Z","d":"MCP server for Penumbra blockchain"},
{"rn":"penrose-mcp","fn":"bmorphism/penrose-mcp","lang":"JavaScript","s":10,"f":4,"oi":0,"pa":"2025-01-20T21:44:55Z","d":"Penrose server for Infinity-Topos"},
{"rn":"world","fn":"bmorphism/world","lang":"Python","s":0,"f":0,"oi":0,"pa":"2026-06-02T06:49:02Z","d":"Local worlds launcher for SA3"},
{"rn":"oxgame","fn":"bmorphism/oxgame","lang":"OCaml","s":0,"f":0,"oi":0,"pa":"2026-05-15T09:53:27Z","d":"Stellar resolution and open-game composition"},
{"rn":"nanoclj-zig","fn":"bmorphism/nanoclj-zig","lang":"Zig","s":0,"f":0,"oi":0,"pa":"2026-05-07T20:12:15Z","d":None},
{"rn":"zig-syrup","fn":"bmorphism/zig-syrup","lang":"Zig","s":0,"f":0,"oi":0,"pa":"2026-05-07T19:49:05Z","d":"Embeddable OCapN Syrup in Zig"},
{"rn":"postweb","fn":"bmorphism/postweb","lang":"Go","s":0,"f":0,"oi":0,"pa":"2026-04-09T10:51:57Z","d":"postweb — evolved from prepostweb"},
{"rn":"magic-world-org","fn":"bmorphism/magic-world-org","lang":"Python","s":1,"f":0,"oi":0,"pa":"2026-04-05T07:03:50Z","d":"Magic World Org (Local MLX)"},
{"rn":"flox-mcp-bb","fn":"bmorphism/flox-mcp-bb","lang":"Clojure","s":0,"f":0,"oi":0,"pa":"2026-02-12T02:45:43Z","d":"Open-source MCP server for Flox"},
{"rn":"vibesnipe-market","fn":"bmorphism/vibesnipe-market","lang":"Move","s":0,"f":0,"oi":9,"pa":"2026-02-05T10:23:25Z","d":None},
{"rn":"aella","fn":"bmorphism/aella","lang":"Rascal","s":1,"f":0,"oi":0,"pa":"2026-02-01T02:44:30Z","d":None},
{"rn":"vibespace-mcp-go-ternary","fn":"bmorphism/vibespace-mcp-go-ternary","lang":"HTML","s":0,"f":1,"oi":3,"pa":"2026-01-11T12:50:40Z","d":"MCP experience with NATS and balanced ternary"},
{"rn":"open-location-code-zig","fn":"bmorphism/open-location-code-zig","lang":"Zig","s":3,"f":0,"oi":0,"pa":"2025-12-30T19:33:45Z","d":"Open Location Code in Zig"},
{"rn":"bafishka","fn":"bmorphism/bafishka","lang":"Clojure","s":1,"f":0,"oi":0,"pa":"2025-12-19T09:38:00Z","d":"Rust-native Fish shell file operations with Steel"},
{"rn":"multiverse-color-game","fn":"bmorphism/multiverse-color-game","lang":"Julia","s":0,"f":0,"oi":0,"pa":"2025-12-12T05:28:11Z","d":"2+1D Holographic Color Matching for VisionPro"},
{"rn":"signal-mcp","fn":"bmorphism/signal-mcp","lang":"Rust","s":0,"f":0,"oi":0,"pa":"2025-12-11T07:20:08Z","d":"O(n)->O(1) chromatic mode collapse"},
{"rn":"monero-rental-hash-war","fn":"bmorphism/monero-rental-hash-war","lang":"Haskell","s":1,"f":0,"oi":0,"pa":"2025-10-05T23:08:54Z","d":"OpenGame analysis of Monero rental hash war"},
{"rn":"schoenfinkel","fn":"bmorphism/schoenfinkel","lang":"Python","s":1,"f":0,"oi":0,"pa":"2025-10-04T23:31:11Z","d":"Post-quantum categorical gravity framework"},
{"rn":"bafishka-clean","fn":"bmorphism/bafishka-clean","lang":"Rust","s":1,"f":0,"oi":0,"pa":"2025-09-25T19:22:10Z","d":"Clean monadic Steel-SCI with category theory"},
{"rn":"babashka-static-build","fn":"bmorphism/babashka-static-build","lang":"Dockerfile","s":1,"f":0,"oi":0,"pa":"2025-09-05T02:26:32Z","d":"Static musl babashka for ARM64 Termux"},
{"rn":"whale","fn":"bmorphism/whale","lang":"MATLAB","s":2,"f":0,"oi":0,"pa":"2025-09-04T06:55:21Z","d":"omniglot + sperm whale codas = metawhaling"},
{"rn":"infinity-topos","fn":"bmorphism/infinity-topos","lang":"Python","s":1,"f":0,"oi":0,"pa":"2025-08-29T05:39:49Z","d":None},
{"rn":"elevenlabs-mcp-enhanced","fn":"bmorphism/elevenlabs-mcp-enhanced","lang":"Python","s":1,"f":0,"oi":0,"pa":"2025-08-29T04:41:58Z","d":"Enhanced ElevenLabs MCP server"},
{"rn":"zeldar","fn":"bmorphism/zeldar","lang":"Python","s":1,"f":0,"oi":1,"pa":"2025-08-26T15:16:21Z","d":"Burning Man Art Robot"},
{"rn":"stellogen-quantum-operads","fn":"bmorphism/stellogen-quantum-operads","lang":None,"s":1,"f":0,"oi":0,"pa":"2025-07-15T04:49:41Z","d":"Quantum Operads in Stellogen"},
{"rn":"ezkl-ethglobal2025","fn":"bmorphism/ezkl-ethglobal2025","lang":"Python","s":1,"f":0,"oi":0,"pa":"2025-07-07T01:16:01Z","d":None},
{"rn":"zk-haiku-nanogpt","fn":"bmorphism/zk-haiku-nanogpt","lang":"Solidity","s":1,"f":0,"oi":0,"pa":"2025-07-06T03:08:24Z","d":"ZK-Haiku-NanoGPT verifiable multi-agent AI"},
{"rn":"rama-event-processor","fn":"bmorphism/rama-event-processor","lang":"Java","s":1,"f":0,"oi":0,"pa":"2025-07-02T07:01:44Z","d":"Processing events with Rama"},
{"rn":"oxcaml-sci-canonical","fn":"bmorphism/oxcaml-sci-canonical","lang":"OCaml","s":1,"f":0,"oi":0,"pa":"2025-06-20T06:37:12Z","d":"Canonical OxCaml-SCI implementation"},
{"rn":"graphistry-mcp","fn":"bmorphism/graphistry-mcp","lang":"Python","s":2,"f":0,"oi":0,"pa":"2025-05-06T17:34:24Z","d":"Graphistry MCP for graph visualization"},
{"rn":"slowtime-mcp-server","fn":"bmorphism/slowtime-mcp-server","lang":"TypeScript","s":3,"f":5,"oi":6,"pa":"2025-01-02T01:23:33Z","d":"MCP server for time-based operations"},
{"rn":"krep-mcp-server","fn":"bmorphism/krep-mcp-server","lang":"JavaScript","s":1,"f":1,"oi":1,"pa":"2025-03-19T20:22:46Z","d":"High-performance string search MCP server"},
{"rn":"gists-mcp-server","fn":"bmorphism/gists-mcp-server","lang":"JavaScript","s":2,"f":0,"oi":0,"pa":"2025-01-03T03:50:54Z","d":"MCP server for GitHub Gists"},
{"rn":"deberta-goemotions","fn":"bmorphism/deberta-goemotions","lang":"Python","s":0,"f":0,"oi":0,"pa":"2025-10-22T18:32:24Z","d":None},
{"rn":"lumon-tui","fn":"bmorphism/lumon-tui","lang":"Python","s":1,"f":0,"oi":0,"pa":"2025-02-02T11:24:21Z","d":"Parallel worlds TUI inspired by Lumon"},
{"rn":"GeoACSets.jl","fn":"bmorphism/GeoACSets.jl","lang":"Julia","s":0,"f":1,"oi":1,"pa":"2026-01-19T13:57:13Z","d":"Categorical data structures with geospatial"},
{"rn":"galahack2024","fn":"bmorphism/galahack2024","lang":"TypeScript","s":2,"f":0,"oi":0,"pa":"2024-03-21T15:48:19Z","d":None},
{"rn":"crags","fn":"bmorphism/crags","lang":"Python","s":1,"f":0,"oi":0,"pa":"2024-01-14T04:21:45Z","d":"RAGs. categorically."},
{"rn":"untime","fn":"bmorphism/untime","lang":"Swift","s":1,"f":0,"oi":0,"pa":"2024-09-06T23:39:08Z","d":None},
{"rn":"c-house-town","fn":"bmorphism/c-house-town","lang":"TypeScript","s":1,"f":0,"oi":0,"pa":"2024-07-25T21:13:04Z","d":None},
{"rn":"telega","fn":"bmorphism/telega","lang":"Rust","s":1,"f":0,"oi":0,"pa":"2023-08-23T17:20:29Z","d":"absurd wasm32-wasi flow"},
{"rn":"meso","fn":"bmorphism/meso","lang":"Jupyter Notebook","s":1,"f":1,"oi":0,"pa":"2023-08-09T06:04:11Z","d":"Markov Kernel inference simulations"},
{"rn":"OTC-0","fn":"bmorphism/OTC-0","lang":"JavaScript","s":3,"f":0,"oi":0,"pa":"2022-06-07T22:18:08Z","d":None},
{"rn":"pluridrop","fn":"bmorphism/pluridrop","lang":"TypeScript","s":2,"f":0,"oi":0,"pa":"2022-04-10T00:13:47Z","d":"ETHPortland2022 hack"},
{"rn":"plurigrid-celo","fn":"bmorphism/plurigrid-celo","lang":"TypeScript","s":1,"f":1,"oi":0,"pa":"2022-12-09T10:07:25Z","d":"Celo e-app for Albany Plurigrid"},
{"rn":"deepfakes","fn":"bmorphism/deepfakes","lang":"Python","s":1,"f":0,"oi":2,"pa":"2019-04-28T22:53:40Z","d":None},
]

for i, r in enumerate(BMORPHISM, start=start_id):
    trit, color, name = gf3(i)
    con.execute("INSERT INTO repo_snapshots VALUES (?,now(),?,?,?,?,?,?,?,?,?,?)",
                [i, inc_id, "bmorphism", r["rn"], r["fn"], r["lang"],
                 r["s"], r["f"], r["oi"], r["pa"], r["d"]])

print(f"Inserted {len(BMORPHISM)} bmorphism repos starting at id {start_id}.")
con.close()
