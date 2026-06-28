# World Increment Sweep + Hamming Snapshot
**Date:** 2026-06-28  
**GF(3) Chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d → ...

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 11 |
| kubeflow | org | 10 |
| TeglonLabs | org | 5 |
| bmorphism | user | 11 |
| zubyul | user | 6 |
| migalkin | social graph | 2 |
| DJedamski | social graph | 1 |
| wasita | social graph | 2 |
| kristinezheng | social graph | 1 |
| M1shaaa | social graph | 2 |
| AustinCStone | social graph | 2 |

**Total: 48 repo snapshots across 11 sources**

### Notable Activity (sorted by most recently pushed)
| Repo | Stars | Pushed | Language |
|------|-------|--------|----------|
| plurigrid/gorj | 0 | 2026-06-28 | Clojure (877 open issues!) |
| bmorphism/Gay.jl | 2 | 2026-06-28 | Julia (187 open issues) |
| M1shaaa/M1shaaa | 0 | 2026-06-28 | — |
| plurigrid/asi | 26 | 2026-06-28 | HTML |
| zubyul/voice-observatory | 0 | 2026-04-24 | Python |
| TeglonLabs/jank-crane | 0 | 2026-06-08 | C++ |
| kubeflow/kubeflow | 15750 | 2026-06-18 | — |
| kubeflow/pipelines | 4158 | 2026-06-27 | Python |

### GF(3) World Increment Chain (11 increments)
| id | GF3 | Color | Name | Source |
|----|-----|-------|------|--------|
| 1 | 1 | #b8bb26 | PLUS | plurigrid |
| 2 | -1 | #cc241d | MINUS | kubeflow |
| 3 | 0 | #d3869b | ERGODIC | TeglonLabs |
| 4 | 1 | #b8bb26 | PLUS | bmorphism |
| 5 | -1 | #cc241d | MINUS | zubyul |
| 6 | 0 | #d3869b | ERGODIC | migalkin |
| 7 | 1 | #b8bb26 | PLUS | DJedamski |
| 8 | -1 | #cc241d | MINUS | wasita |
| 9 | 0 | #d3869b | ERGODIC | kristinezheng |
| 10 | 1 | #b8bb26 | PLUS | M1shaaa |
| 11 | -1 | #cc241d | MINUS | AustinCStone |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Balances (28 addresses, via `0x1::coin::balance` view function)

**Note:** Legacy `CoinStore` resource not present on these accounts; used fungible asset view function.

| World | Balance (APT) | Address (truncated) |
|-------|--------------|---------------------|
| bob | **12.657007** | 0x0a3c...12d5d |
| F | **1.960516** | 0x18a1...3cf71 |
| L | **1.927269** | 0x7c2e...7eba9 |
| J | **1.895093** | 0x4d96...7f54 |
| alice | 0.436434 | 0xc793...cc7b |
| O | 0.210136 | 0x7325...a89d |
| K | 0.161961 | 0xa732...5dc4 |
| P | 0.140136 | 0x6218...c948 |
| M | 0.112285 | 0x6fed...f2e9 |
| N | 0.106121 | 0xe7dd...1b2c |
| Q | 0.103240 | 0xac40...c89a9 |
| S | 0.091788 | 0xb875...0386 |
| R | 0.090217 | 0x7ce6...6e10 |
| T | 0.073713 | 0x3578...4588 |
| U | 0.055773 | 0x7586...f9956 |
| A | 0.051767 | 0x8699...cc7b |
| V | 0.048833 | 0xb59d...af2c3 |
| Y | 0.044449 | 0xd8e3...444c4 |
| X | 0.042577 | 0xa95c...3047d |
| W | 0.040705 | 0x5f32...cc7b0 |
| B | 0.036256 | 0x3f89...cb13 |
| Z | 0.024268 | 0x7af0...197c |
| D | 0.011629 | 0xf776...cfdd1 |
| C | 0.010185 | 0x38b9...535e |
| E | 0.009372 | 0xdc1d...8d36 |
| H | 0.001681 | 0xce67...5300f |
| I | 0.000681 | 0x070f...1fc9 |
| G | 0.000681 | 0x69a3...c7f32 |

**Total swarm APT: ~21.61 APT**  
**Top holder:** bob (12.657 APT, ~59% of swarm)

### Multisig Contract Probes (5 pairs)

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2/2 | Y |
| A-G | 0xf56c...0096 | 2/2 | Y |
| Y-Z | 0xd3ff...b883 | 2/2 | Y |
| S-T | 0x3b1c...7883 | 2/2 | Y |
| V-W | 0x40fa...eb6d | 2/2 | Y |

**All 5 multisig contracts healthy — 2-of-2 threshold on all pairs.**

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — testnet.mnx.fi is behind Vercel deployment protection (auth required). No market data could be extracted. Manual access via Vercel CLI or bypass token required.

---

## DuckDB Ducklake Summary
- **File:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Tables:** `world_increments` (11 rows), `repo_snapshots` (48 rows), `aptos_snapshots` (28 rows), `multisig_probes` (5 rows), `mnx_snapshots` (1 row — unavailable marker)
- **Sequences:** `increment_seq`, `repo_seq`
- **Snapshot timestamp:** 2026-06-28
