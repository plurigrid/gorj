# LATEST_SWEEP.md

**Generated:** 2026-06-09 04:12:50 UTC

---

## JOB 1: GitHub Social Graph Sweep

### Corpus Summary

| Source | Repos |
|--------|-------|

| plurigrid | 100 |
| bmorphism | 100 |
| zubyul | 49 |
| kubeflow | 48 |
| AustinCStone | 40 |
| migalkin | 19 |
| M1shaaa | 8 |
| DJedamski | 6 |
| TeglonLabs | 5 |
| kristinezheng | 5 |

**Total repos captured:** 380

### GF(3) Color Chain Distribution
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 126 |
| 1 | #b8bb26 | PLUS | 127 |
| 2 (−1) | #cc241d | MINUS | 127 |

### Top Languages

- **Python**: 81 repos
- **Rust**: 26 repos
- **JavaScript**: 23 repos
- **TypeScript**: 22 repos
- **HTML**: 15 repos
- **Go**: 15 repos
- **Clojure**: 14 repos
- **Jupyter Notebook**: 14 repos
- **Julia**: 9 repos
- **Zig**: 7 repos

### Notable Repos (plurigrid, recently pushed)

- `plurigrid/gorj` — Clojure — pushed 2026-06-09 — forj + Rama topology nREPL routing + GF(3) gay trit coloring for compositional o
- `plurigrid/place` — TeX — pushed 2026-06-04 — 
- `plurigrid/eirobri` — Clojure — pushed 2026-06-03 — EiRoBri replay world
- `plurigrid/nash-portal` — Rust — pushed 2026-05-19 — NASH token TUI in the browser — ratzilla WASM + GeckoTerminal OHLCV candlesticks
- `plurigrid/zig-syrup` — Zig — pushed 2026-04-30 — High-performance Zig implementation of OCapN Syrup with CapTP optimizations

### TeglonLabs Repos (5 total)

- `TeglonLabs/jank-crane` (C++) — crane-jank converged-IR hub: loopify pass spec, GF3 converge
- `TeglonLabs/mathpix-gem` (Ruby) — Transform mathematical images to LaTeX
- `TeglonLabs/coin-flip-mcp` (JavaScript) — MCP server for flipping coins
- `TeglonLabs/monad-mcp-server` () — Monad MCP Server
- `TeglonLabs/topoi` (Python) — 

### DuckDB Tables
- `world_increments`: 380 rows — GF(3) trit-colored event log
- `repo_snapshots`: 380 rows — full repo metadata per increment
- `aptos_snapshots`: 28 rows
- `multisig_probes`: 5 rows
- `mnx_snapshots`: 0 rows (MNX testnet behind Vercel auth — unavailable)

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

**Timestamp:** 2026-06-09 04:12:50 UTC

### Wallet Balances (A–Z + alice/bob)

All 28 wallets queried. All returned `resource_not_found` for `CoinStore<AptosCoin>`,
indicating zero APT balance (accounts exist on-chain but hold no APT in the standard coin store).

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...c7b | 0.0 |
| bob | 0x0a3c...d5d | 0.0 |

| A | 0x8699...d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...7b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

### Multisig Contract Probes (5 pairs)

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|

| A-B | 0x0da4f428a0c007da0f... | 2 | ✓ |
| A-G | 0xf56c4a1c0906214f3f... | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df40622... | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c3a49... | 2 | ✓ |
| V-W | 0x40fad7b423a843650f... | 2 | ✓ |

All 5 multisig contracts are **healthy** — all require **2-of-2 signatures**.

### MNX Markets (testnet.mnx.fi)

Status: **UNAVAILABLE** — testnet.mnx.fi is deployed behind Vercel deployment protection
(Vercel auth required). No market data extractable without bypass token.

---

## GF(3) Legend
- **ERGODIC** (trit=0, #d3869b): increment id mod 3 == 0 — steady state / attractor
- **PLUS** (trit=1, #b8bb26): increment id mod 3 == 1 — positive / growth
- **MINUS** (trit=−1, #cc241d): increment id mod 3 == 2 — negative / contraction
