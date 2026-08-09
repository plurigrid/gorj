# World Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-08-09  
**Run:** world-increment-sweep + hamming-swarm-snapshot

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Found |
|--------|------|------------|
| plurigrid | org | 50 (top 15 stored) |
| kubeflow | org | 49 (top 15 stored) |
| TeglonLabs | org | 5 |
| bmorphism | user | 106 (top 15 stored) |
| zubyul | user | 49 (top 10 stored) |
| migalkin | user | 19 (top 8 stored) |
| DJedamski | user | 6 (top 5 stored) |
| wasita | user | 14 (top 8 stored) |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 (top 5 stored) |
| AustinCStone | user | 41 (top 8 stored) |

**Total repo snapshots this sweep:** 99 new rows (cumulative: 1,043)

### Notable Activity
- **plurigrid/gorj** pushed 2026-08-09 — 1,733 open issues, active dev
- **plurigrid/place** pushed 2026-08-09 — TeX, 3★
- **plurigrid/eirobri** pushed 2026-08-04 — EiRoBri replay world
- **kubeflow/docs-agent** pushed 2026-08-08 — 40★, AI docs agent
- **kubeflow/spark-operator** pushed 2026-08-08 — 3,145★, most starred kubeflow repo
- **kubeflow/trainer** pushed 2026-08-08 — 2,176★, distributed AI training
- **kubeflow** flagship repo — 15,807★
- **TeglonLabs/jank-crane** pushed 2026-06-08 — C++, GF3 convergence maps
- **bmorphism/Gay.jl** pushed 2026-07-21 — 188 open issues, active
- **bmorphism/ocaml-mcp-sdk** — 61★, most starred bmorphism repo
- **wasita/wm-cv** pushed 2026-08-07 — CV web app
- **wasita/xoxowasita-analysis** pushed 2026-08-06 — fresh repo

### GF(3) Color Chain (this sweep)
| Increment ID | GF3 Trit | Color | Name | Source |
|---|---|---|---|---|
| 13 | +1 | #b8bb26 | PLUS | plurigrid |
| 14 | -1 | #cc241d | MINUS | kubeflow |
| 15 | 0 | #d3869b | ERGODIC | TeglonLabs |
| 16 | +1 | #b8bb26 | PLUS | bmorphism |
| 17 | -1 | #cc241d | MINUS | zubyul |
| 18 | 0 | #d3869b | ERGODIC | migalkin |
| 19 | +1 | #b8bb26 | PLUS | DJedamski |
| 20 | -1 | #cc241d | MINUS | wasita |
| 21 | 0 | #d3869b | ERGODIC | kristinezheng |
| 22 | +1 | #b8bb26 | PLUS | M1shaaa |
| 23 | -1 | #cc241d | MINUS | AustinCStone |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
All 28 Hamming swarm addresses probed via Aptos fullnode mainnet API.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

**Status:** All addresses return 0 APT — CoinStore not registered or empty. This is consistent with Aptos accounts that hold assets in other modules or have not received APT transfers.

### Multisig Contract Probes (5/5 healthy)
| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✓ HEALTHY |

All 5 multisig contracts responding correctly — 2-of-N threshold consistent across all pairs.

### MNX Markets (testnet.mnx.fi)
**Status:** UNAVAILABLE — SPA renders HTML but no REST API endpoints responded (`/api/markets`, `/api/v1/markets`, `/api/tickers`, `/markets` all return no market data). Likely requires client-side JavaScript execution or authentication.

---

## DuckDB Ducklake State
| Table | Total Rows |
|-------|-----------|
| world_increments | 34 |
| repo_snapshots | 1,043 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

**DB path:** `packages/world-increment/ducklake/world-increments.duckdb`
