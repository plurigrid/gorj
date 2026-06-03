# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-06-03 12:16:01 UTC
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (zubyul social) | 19 |
| DJedamski | user (zubyul social) | 6 |
| wasita | user (zubyul social) | 11 |
| kristinezheng | user (zubyul social) | 6 |
| M1shaaa | user (zubyul social) | 8 |
| AustinCStone | user (zubyul social) | 40 |
| **TOTAL** | | **391** |

### GF(3) Color Chain Distribution
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 (id%3=0) | #d3869b | ERGODIC | 130 |
| 1 (id%3=1) | #b8bb26 | PLUS | 131 |
| -1 (id%3=2) | #cc241d | MINUS | 130 |

### Top 15 Repos by Stars
| Owner | Repo | Stars | Language |
|-------|------|-------|----------|
| kubeflow | kubeflow | 15705 |  |
| kubeflow | pipelines | 4151 | Python |
| kubeflow | spark-operator | 3125 | Python |
| kubeflow | trainer | 2110 | Go |
| kubeflow | katib | 1685 | Python |
| kubeflow | examples | 1462 | Jsonnet |
| kubeflow | manifests | 1020 | YAML |
| kubeflow | arena | 811 | Go |
| kubeflow | kale | 691 | Python |
| kubeflow | mpi-operator | 528 | Go |
| kubeflow | fairing | 337 | Jsonnet |
| kubeflow | pytorch-operator | 310 | Jsonnet |
| kubeflow | community | 195 | Jupyter Notebook |
| kubeflow | website | 184 | HTML |
| kubeflow | kfctl | 182 | Go |

### DuckDB Tables
- `world_increments`: 391 rows (one per repo, GF3 color tagged)
- `repo_snapshots`: 391 rows (full metadata)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

**Result:** All 28 wallets returned no CoinStore resource.  
The `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource was not found for any of the queried addresses on Aptos mainnet, indicating these accounts either have zero APT under the legacy coin module or haven't been registered with the classic coin store. Balance recorded as NULL for all.

| World | Address (truncated) |
|-------|---------------------|
| alice | 0xc793...4cc7b |
| bob | 0x0a3c...512d5d |
| A | 0x8699...e9d7a |
| B–Z | (see aptos_snapshots table) |

### Multisig Contract Probes

All 5 multisig contracts are **healthy** with 2-of-N signatures required.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

MNX testnet is a Next.js SPA — all API path probes returned HTML, not JSON.  
No structured market data was extractable. Status: **unavailable via static API** (requires JS execution).  
`mnx_snapshots` table is empty.

---

## DuckDB Schema Summary

```
world_increments (391 rows)   — GF3 color-tagged repo events
repo_snapshots   (391 rows)   — Full repo metadata from social graph
aptos_snapshots  (28 rows)    — Hamming swarm wallet balances (all NULL)
multisig_probes  (5 rows)     — All healthy, 2 sigs required
mnx_snapshots    (0 rows)     — SPA, data unavailable
```
