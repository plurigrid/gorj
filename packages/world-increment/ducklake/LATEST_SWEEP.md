# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-05-18 UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 25 |
| kubeflow | org | 10 |
| TeglonLabs | org | 4 |
| bmorphism | user | 12 |
| zubyul | user | 8 |
| migalkin | social | 4 |
| DJedamski | social | 1 |
| wasita | social | 3 |
| kristinezheng | social | 1 |
| M1shaaa | social | 2 |
| AustinCStone | social | 2 |
| **Total** | | **71** |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 23 |
| +1 | `#b8bb26` | PLUS | 24 |
| -1 | `#cc241d` | MINUS | 24 |

### Top Repos by Stars

| Org/User | Repo | Stars | Language |
|----------|------|-------|----------|
| kubeflow | kubeflow | 15,647 | — |
| kubeflow | pipelines | 4,140 | Python |
| kubeflow | spark-operator | 3,126 | Python |
| kubeflow | trainer | 2,100 | Go |
| kubeflow | katib | 1,682 | Python |
| migalkin | NodePiece | 144 | Python |
| AustinCStone | TextGAN | 92 | Python |
| migalkin | StarE | 89 | Python |
| bmorphism | anti-bullshit-mcp-server | 23 | JavaScript |
| bmorphism | risc0-cosmwasm-example | 23 | Rust |
| plurigrid | vcg-auction | 7 | Rust |

### Notable Activity (plurigrid)
- **gorj** (Clojure) — 248 open issues, pushed 2026-05-08: forj + Rama topology nREPL routing + GF(3)
- **asi** (HTML) — 23 stars, pushed 2026-05-17: everything is topological chemputer!
- **Plurigraph** (JS) — pushed 2026-05-12: Plurigrid knowledge base
- **nanoclj-zig** (Zig) — 20 open issues: NaN-boxed Clojure interpreter in Zig

### Notable Activity (bmorphism)
- **Gay.jl** (Julia) — 189 open issues, active gay GF(3) color library
- **ocaml-mcp-sdk** — 61 stars: OCaml SDK for Model Context Protocol
- **say-mcp-server** — 20 stars; **babashka-mcp-server** — 18 stars

### Notable Activity (zubyul)
- **voice-observatory** — Passive macOS TUI observing voice-download pathways
- **tilelang-kernels** — TileLang GPU kernels for GF(3) trit classification + Sinkhorn OT
- **gay-world** — Goblin world builder via Gay.jl SPI

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 worlds)

All 28 wallets (alice, bob, A-Z) queried via Aptos mainnet fullnode.
All accounts returned **0.0 APT** — no `CoinStore<AptosCoin>` resource registered (fresh/empty accounts).

| World | Address | APT Balance |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...9a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...7b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

### Multisig Contract Probes (5/5 healthy)

All 5 multisig accounts confirmed **2-of-2 signature requirement** on Aptos mainnet.

| Pair | Address | Sigs Required | Healthy |
|------|---------|:-------------:|:-------:|
| A-B | 0x0da4...003 | 2 | true |
| A-G | 0xf56c...096 | 2 | true |
| Y-Z | 0xd3ff...883 | 2 | true |
| S-T | 0x3b1c...883 | 2 | true |
| V-W | 0x40fa...b6d | 2 | true |

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a **Next.js SPA** — the frontend loads (HTTP 200) but all market data is client-side rendered with no accessible REST API endpoints (`/api/markets`, `/api/v1/markets`, `/api/tickers` all return 404/SPA HTML). Market data recorded as **unavailable** in `mnx_snapshots` table.

---

## DuckDB Schema Summary

```
world_increments  -- 71 rows  (GF3 trit-colored increment events)
repo_snapshots    -- 71 rows  (GitHub repo metadata)
aptos_snapshots   -- 28 rows  (Aptos wallet balances)
multisig_probes   --  5 rows  (2-of-2 multisig health checks)
mnx_snapshots     --  1 row   (MNX market status: unavailable)
```

### GF(3) Encoding Key

| id%3 | Trit | Color | Name | Semantic |
|------|------|-------|------|----------|
| 0 | 0 | #d3869b | ERGODIC | neutral / fixed-point |
| 1 | +1 | #b8bb26 | PLUS | forward / constructive |
| 2 | -1 | #cc241d | MINUS | backward / destructive |
