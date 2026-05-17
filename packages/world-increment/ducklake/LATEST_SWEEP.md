# World-Increment Sweep + Hamming Snapshot
**Timestamp:** 2026-05-17T12:10 UTC  
**GF(3) Color Chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Coverage
| Source | Type | Repos | Stars |
|--------|------|------:|------:|
| plurigrid | org | 100 | 51 |
| bmorphism | user | 100 | 128 |
| AustinCStone | user | 43 | 108 |
| kubeflow | org | 30 | 32,805 |
| zubyul | user | 27 | 13 |
| migalkin | user | 19 | 279 |
| M1shaaa | user | 16 | 0 |
| DJedamski | user | 11 | 7 |
| wasita | user | 11 | 4 |
| kristinezheng | user | 6 | 0 |
| TeglonLabs | org | 4 | 2 |
| **TOTAL** | | **367** | **33,397** |

> Note: kubeflow, TeglonLabs, migalkin, wasita, and kristinezheng were rate-limited on the unauthenticated GitHub REST API (60 req/hr exhausted); data retrieved via GitHub MCP search tool.

### Events Captured
- **bmorphism**: 30 recent public events
- **zubyul**: 2 recent public events

### DuckDB Tables
- `repo_snapshots`: 1,311 rows (includes prior sweeps)
- `world_increments`: 36 rows (13 new increment entries this sweep)

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances
| World | Address (truncated) | Balance (APT) |
|-------|---------------------|-------------:|
| bob | 0x0a3c…12d5d | **12.6570** |
| F | 0x18a1…cf71 | 1.9605 |
| L | 0x7c2e…eba9 | 1.9273 |
| J | 0x4d96…f54 | 1.8951 |
| alice | 0xc793…cc7b | 0.4364 |
| O | 0x7325…89d | 0.2101 |
| K | 0xa732…dc4 | 0.1620 |
| P | 0x6218…948 | 0.1401 |
| M | 0x6fed…f2e9 | 0.1123 |
| N | 0xe7dd…b2c | 0.1061 |
| Q | 0xac40…89a9 | 0.1032 |
| S | 0xb875…386 | 0.0918 |
| R | 0x7ce6…e10 | 0.0902 |
| T | 0x3578…588 | 0.0737 |
| U | 0x7586…956 | 0.0558 |
| A | 0x8699…d7a | 0.0518 |
| V | 0xb59d…f2c3 | 0.0488 |
| Y | 0xd8e3…44c4 | 0.0444 |
| X | 0xa95c…047d | 0.0426 |
| W | 0x5f32…c7b0 | 0.0407 |
| B | 0x3f89…b13 | 0.0363 |
| Z | 0x7af0…97c | 0.0243 |
| D | 0xf776…dd1 | 0.0116 |
| C | 0x38b9…35e | 0.0102 |
| E | 0xdc1d…d36 | 0.0094 |
| H | 0xce67…00f | 0.0017 |
| I | 0x070f…fc9 | 0.0007 |
| G | 0x69a3…f32 | 0.0007 |

**Total swarm balance: 20.3448 APT**  
**Method:** `0x1::coin::balance` view function (CoinStore resource not initialized; FA balance queried via view endpoint)

### Multisig Contract Probes
| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|:-------------:|:-------:|
| A-B | 0x0da4…003 | 2 | ✅ |
| A-G | 0xf56c…096 | 2 | ✅ |
| Y-Z | 0xd3ff…883 | 2 | ✅ |
| S-T | 0x3b1c…883 | 2 | ✅ |
| V-W | 0x40fa…b6d | 2 | ✅ |

All 5 multisig contracts healthy, all require 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)
**Status: WebSocket-only SPA — REST API unavailable**  
The frontend (`testnet.mnx.fi`) is a Next.js app backed by `wss://api.testnet.mnx.fi`. No REST endpoints respond to GET requests. Market data requires WebSocket connection; not extractable via HTTP polling.

---

## DuckDB Ducklake Summary
```
world-increments.duckdb
├── world_increments:   36 rows
├── repo_snapshots:   1311 rows  
├── aptos_snapshots:    28 rows
├── multisig_probes:     5 rows
└── mnx_snapshots:       0 rows (unavailable)
```
