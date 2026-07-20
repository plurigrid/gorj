# World Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-07-20T22:14:25Z  
**Run Date:** 2026-07-20

---

## Job 1: GitHub Social Graph Sweep

### Sources Queried
| Org/User | Type | Repos Snapshotted | Total Stars |
|----------|------|-------------------|-------------|
| plurigrid | org | 250 | 138 |
| bmorphism | user | 250 | 377 |
| kubeflow | org | 143 | 102116 |
| AustinCStone | user | 127 | 324 |
| TeglonLabs | org | 111 | 14 |
| zubyul | user | 97 | 40 |
| migalkin | user | 79 | 833 |
| wasita | user | 72 | 11 |
| kristinezheng | user | 41 | 0 |
| M1shaaa | user | 40 | 0 |
| DJedamski | user | 28 | 17 |

**Total repo snapshots:** 1238  
**Sources:** plurigrid, kubeflow, TeglonLabs (orgs) + bmorphism, zubyul, migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone (users)

### Top Repos by Stars
| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | n/a | 15785 | 2026-07-10 |
| kubeflow/kubeflow | n/a | 15572 | 2026-01-05 |
| kubeflow/kubeflow | n/a | 15565 | 2026-01-05 |
| kubeflow/pipelines | Python | 4169 | 2026-07-20 |
| kubeflow/pipelines | Python | 4119 | 2026-04-10 |
| kubeflow/pipelines | Python | 4119 | 2026-04-14 |
| kubeflow/spark-operator | Python | 3140 | 2026-07-17 |
| kubeflow/spark-operator | Python | 3114 | 2026-04-13 |
| kubeflow/spark-operator | Python | 3111 | 2026-04-10 |
| kubeflow/trainer | Go | 2152 | 2026-07-20 |

### GF(3) Color Chain Distribution
| GF3 Name | Color | Count |
|----------|-------|-------|
| PLUS (trit=1) | #b8bb26 | 106 |
| MINUS (trit=-1) | #cc241d | 106 |
| ERGODIC (trit=0) | #d3869b | 105 |

### DuckDB Ducklake Tables
| Table | Rows |
|-------|------|
| world_increments | 317 |
| repo_snapshots | 1238 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

---

## Job 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances
Queried 28 addresses from `fullnode.mainnet.aptoslabs.com`.

| World | Address (truncated) | Balance (APT) | Status |
|-------|---------------------|---------------|--------|
| A | `...A` | resource_not_found | unfunded |
| B | `...B` | resource_not_found | unfunded |
| C | `...C` | resource_not_found | unfunded |
| D | `...D` | resource_not_found | unfunded |
| E | `...E` | resource_not_found | unfunded |
| F | `...F` | resource_not_found | unfunded |
| G | `...G` | resource_not_found | unfunded |
| H | `...H` | resource_not_found | unfunded |
| I | `...I` | resource_not_found | unfunded |
| J | `...J` | resource_not_found | unfunded |
| K | `...K` | resource_not_found | unfunded |
| L | `...L` | resource_not_found | unfunded |
| M | `...M` | resource_not_found | unfunded |
| N | `...N` | resource_not_found | unfunded |
| O | `...O` | resource_not_found | unfunded |
| P | `...P` | resource_not_found | unfunded |
| Q | `...Q` | resource_not_found | unfunded |
| R | `...R` | resource_not_found | unfunded |
| S | `...S` | resource_not_found | unfunded |
| T | `...T` | resource_not_found | unfunded |
| U | `...U` | resource_not_found | unfunded |
| V | `...V` | resource_not_found | unfunded |
| W | `...W` | resource_not_found | unfunded |
| X | `...X` | resource_not_found | unfunded |
| Y | `...Y` | resource_not_found | unfunded |
| Z | `...Z` | resource_not_found | unfunded |
| alice | `...lice` | resource_not_found | unfunded |
| bob | `...bob` | resource_not_found | unfunded |

> All 28 addresses returned `resource_not_found` — accounts are not yet funded/initialized on Aptos mainnet (CoinStore not registered).

### Multisig Contract Probes
All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4f428...987003` | 2 | HEALTHY |
| A-G | `0xf56c4a1c...bc0096` | 2 | HEALTHY |
| S-T | `0x3b1c3ae9...ed7883` | 2 | HEALTHY |
| V-W | `0x40fad7b4...80eb6d` | 2 | HEALTHY |
| Y-Z | `0xd3ffe181...75b883` | 2 | HEALTHY |

**All 5 multisig contracts are healthy** — each requires 2-of-2 signatures.

### MNX Markets (testnet.mnx.fi)
**Status:** Password-protected deployment (HTTP 401 — Vercel auth guard active).  
Market data is unavailable without authentication credentials. No data captured.

---

## Summary

| Job | Status | Notes |
|-----|--------|-------|
| GitHub social graph sweep | COMPLETE | 294 repos across 11 sources |
| Aptos wallet balances | COMPLETE | 28 queried; all unfunded (resource_not_found) |
| Multisig probes | COMPLETE | 5/5 healthy, all 2-of-2 |
| MNX markets | UNAVAILABLE | 401 password-protected |

GF(3) color chain applied to all world_increment IDs:  
- `id%3==0` → trit=0, ERGODIC `#d3869b`  
- `id%3==1` → trit=1, PLUS `#b8bb26`  
- `id%3==2` → trit=-1, MINUS `#cc241d`
