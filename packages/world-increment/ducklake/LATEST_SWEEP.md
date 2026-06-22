# World Increment Sweep + Hamming Swarm Snapshot
**Timestamp:** 2026-06-22 UTC  
**Branch:** world-increment/sweep  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Scanned
| Source | Type | Repos | Stars |
|--------|------|-------|-------|
| plurigrid | org | 100 | 77 |
| kubeflow | org | 48 | 34,246 |
| TeglonLabs | org | 5 | 2 |
| bmorphism | user | 100 | 248 |
| zubyul | user | 49 | 14 |
| migalkin | social | 19 | 280 |
| DJedamski | social | 6 | 3 |
| wasita | social | 11 | 5 |
| kristinezheng | social | 5 | 0 |
| M1shaaa | social | 8 | 0 |
| AustinCStone | social | 40 | 108 |
| **TOTAL** | | **391** | **34,983** |

### Top Starred Repos
| Repo | Stars |
|------|-------|
| kubeflow/kubeflow | 15,740 |
| kubeflow/pipelines | 4,157 |
| kubeflow/spark-operator | 3,128 |
| kubeflow/trainer | 2,118 |
| kubeflow/katib | 1,685 |
| kubeflow/examples | 1,460 |
| kubeflow/community-distribution | 1,027 |

### Language Breakdown (Top 12)
Python(80), Rust(26), JavaScript(25), TypeScript(23), HTML(17), Go(15), Jupyter Notebook(14), Clojure(14), Julia(9), Jsonnet(7), Zig(7), R(6)

### GF(3) Color Chain (world_increments)
| ID | Trit | Color | Name | Source |
|----|------|-------|------|--------|
| 1 | 1 | #b8bb26 | PLUS | AustinCStone |
| 2 | -1 | #cc241d | MINUS | DJedamski |
| 3 | 0 | #d3869b | ERGODIC | M1shaaa |
| 4 | 1 | #b8bb26 | PLUS | TeglonLabs |
| 5 | -1 | #cc241d | MINUS | bmorphism |
| 6 | 0 | #d3869b | ERGODIC | kristinezheng |
| 7 | 1 | #b8bb26 | PLUS | kubeflow |
| 8 | -1 | #cc241d | MINUS | migalkin |
| 9 | 0 | #d3869b | ERGODIC | plurigrid |
| 10 | 1 | #b8bb26 | PLUS | wasita |
| 11 | -1 | #cc241d | MINUS | zubyul |

### Notable Recent Activity
- **M1shaaa/M1shaaa**: pushed 2026-06-22 (today)
- **wasita/proj-template**: pushed 2026-06-19
- **kristinezheng/kristinezheng.github.io**: pushed 2026-06-07
- **TeglonLabs/jank-crane**: pushed 2026-06-08 (GF3 convergence maps, loopify pass spec)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses — alice, bob, A–Z)
All 28 addresses returned 0 APT. The `CoinStore<AptosCoin>` resource was not initialized on any of these accounts (accounts exist on-chain but have not received a CoinStore deposit). This is consistent with freshly-created or placeholder accounts.

### Multisig Contract Probes (5 pairs)
| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428... | 2 | YES |
| A-G | 0xf56c4a1c... | 2 | YES |
| Y-Z | 0xd3ffe181... | 2 | YES |
| S-T | 0x3b1c3ae9... | 2 | YES |
| V-W | 0x40fad7b4... | 2 | YES |

All 5 multisig contracts are healthy, each requiring 2-of-N signatures. The on-chain quorum structure is consistent across all pairs.

### MNX Markets (testnet.mnx.fi)
**Status: Unavailable** — testnet.mnx.fi is behind Vercel deployment protection. All three probed endpoints (/api/markets, /api/v1/markets, /api/tickers) returned 401 Authentication Required. No market data captured.

---

## DuckDB Schema Summary
| Table | Rows | Description |
|-------|------|-------------|
| world_increments | 11 | GF(3) color chain per source |
| repo_snapshots | 391 | Full repo metadata snapshot |
| aptos_snapshots | 28 | Hamming swarm wallet balances |
| multisig_probes | 5 | Aptos multisig contract health |
| mnx_snapshots | 0 | MNX market data (unavailable) |
