# World Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-06-15  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| DJedamski | user | 6 |
| wasita | user | 11 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| AustinCStone | user | 40 |
| **TOTAL** | | **391** |

### DuckDB GF(3) Color Chain Distribution
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 130 |
| 1 | `#b8bb26` | PLUS | 131 |
| -1 | `#cc241d` | MINUS | 130 |

### Top Languages Across All Repos
| Language | Repos |
|----------|-------|
| Python | 81 |
| Rust | 26 |
| JavaScript | 25 |
| TypeScript | 23 |
| Go | 15 |
| HTML | 15 |
| Clojure | 14 |
| Jupyter Notebook | 14 |
| Julia | 9 |
| Zig | 7 |

### Most Recently Pushed Repos
| Repo | Pushed At |
|------|-----------|
| plurigrid/gorj | 2026-06-15T05:17:04Z |
| M1shaaa/M1shaaa | 2026-06-15T03:55:00Z |
| bmorphism/Gay.jl | 2026-06-15T00:44:40Z |
| kubeflow/community | 2026-06-14T21:03:42Z |
| kubeflow/spark-operator | 2026-06-14T16:43:38Z |
| kubeflow/pipelines | 2026-06-14T11:54:36Z |
| kubeflow/website | 2026-06-13T16:50:04Z |
| kubeflow/trainer | 2026-06-13T03:19:28Z |
| kubeflow/notebooks | 2026-06-13T00:38:04Z |
| kubeflow/hub | 2026-06-12T22:39:56Z |

### Star Leaders
| Repo | Stars |
|------|-------|
| kubeflow/kubeflow | 15722 |
| kubeflow/pipelines | 4154 |
| kubeflow/spark-operator | 3127 |
| kubeflow/trainer | 2115 |
| kubeflow/katib | 1683 |
| kubeflow/examples | 1461 |
| kubeflow/community-distribution | 1023 |
| kubeflow/arena | 812 |
| kubeflow/kale | 694 |
| kubeflow/mpi-operator | 528 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
All 28 wallets queried against fullnode.mainnet.aptoslabs.com. Every address returned 0.0 APT — these are unfunded or zero-balance accounts on mainnet (CoinStore resource not yet initialized).

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793...c7b | 0.0 |
| bob | 0x0a3c...d5d | 0.0 |
| A-Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes (Aptos Mainnet)
All 5 multisig contracts are healthy, requiring 2-of-N signatures.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | YES |
| A-G | 0xf56c...096 | 2 | YES |
| Y-Z | 0xd3ff...883 | 2 | YES |
| S-T | 0x3b1c...883 | 2 | YES |
| V-W | 0x40fa...b6d | 2 | YES |

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** - testnet.mnx.fi requires Vercel authentication for all API paths (/api/markets, /api/v1/markets, /api/tickers). Returns 401 authentication wall. No market data captured this sweep.

---

## DuckDB Schema Summary
| Table | Rows | Description |
|-------|------|-------------|
| world_increments | 391 | GF(3) color-chained event log |
| repo_snapshots | 391 | GitHub repo metadata per increment |
| aptos_snapshots | 28 | Hamming swarm wallet balances |
| multisig_probes | 5 | Multisig contract signature requirements |
| mnx_snapshots | 0 | MNX market data (unavailable this run) |
