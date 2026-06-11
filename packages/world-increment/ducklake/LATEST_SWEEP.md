# World Increment Sweep + Hamming Swarm Snapshot
**Timestamp:** 2026-06-11  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured | Total Stars |
|--------|------|---------------|-------------|
| bmorphism | user | 100 | 247 |
| plurigrid | org | 100 | 76 |
| zubyul | user | 49 | 14 |
| kubeflow | org | 48 | 34,188 |
| AustinCStone | user | 40 | 108 |
| migalkin | user | 19 | 280 |
| wasita | user | 11 | 5 |
| M1shaaa | user | 8 | 0 |
| DJedamski | user | 6 | 3 |
| TeglonLabs | org | 5 | 2 |
| kristinezheng | user | 5 | 0 |
| **TOTAL** | | **391** | **34,923** |

### Top Repos by Stars
| Repo | Language | Stars |
|------|----------|-------|
| kubeflow/kubeflow | — | 15,713 |
| kubeflow/pipelines | Python | 4,152 |
| kubeflow/spark-operator | Python | 3,126 |
| kubeflow/trainer | Go | 2,111 |
| kubeflow/katib | Python | 1,683 |

### GF(3) Color Chain Distribution
| Trit | Color | Name | Count |
|------|-------|------|-------|
| -1 | `#cc241d` | MINUS | 130 |
| 0 | `#d3869b` | ERGODIC | 130 |
| +1 | `#b8bb26` | PLUS | 131 |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (28 addresses)
All 28 Hamming swarm wallets (alice, bob, A-Z) returned **0.0 APT**.

### Multisig Probes (5 contracts) - ALL HEALTHY
| Pair | Contract Address | Sigs Required |
|------|-----------------|---------------|
| A-B | 0x0da4...7003 | 2 |
| A-G | 0xf56c...0096 | 2 |
| Y-Z | 0xd3ff...b883 | 2 |
| S-T | 0x3b1c...7883 | 2 |
| V-W | 0x40fa...eb6d | 2 |

### MNX Markets
**Status: UNAVAILABLE** - testnet.mnx.fi requires Vercel auth on all API endpoints.

---

## Database Summary
```
world-increments.duckdb
  world_increments  391 rows  (GF3-tagged increment events)
  repo_snapshots    391 rows  (GitHub repo metadata)
  aptos_snapshots    28 rows  (Hamming wallet balances)
  multisig_probes     5 rows  (Aptos multisig health)
  mnx_snapshots       1 row   (MNX unavailable sentinel)
```
