# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-25 16:13 UTC
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Fetched |
|--------|------|--------------|
| plurigrid | org | 100 (103 total) |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 50 (106 total) |
| zubyul | user | 49 |
| migalkin | user (social graph) | 19 |
| DJedamski | user (social graph) | 6 |
| wasita | user (social graph) | 12 |
| kristinezheng | user (social graph) | 5 |
| M1shaaa | user (social graph) | 8 |
| AustinCStone | user (social graph) | 41 |

**Total new repo_snapshots inserted this run:** 276
**Total world_increments in DB:** 299

### GF(3) Color Chain Distribution (this run)
| Color | Trit | Name | Count |
|-------|------|------|-------|
| PLUS | #b8bb26 | PLUS | 92 |
| MINUS | #cc241d | MINUS | 92 |
| ERGODIC | #d3869b | ERGODIC | 92 |
| #d3869b | ERGODIC | #d3869b | 7 |
| #cc241d | MINUS | #cc241d | 8 |
| #b8bb26 | PLUS | #b8bb26 | 8 |

### Top plurigrid Repos (by stars)
| Repo | Language | Stars | Forks | Issues | Pushed |
|------|----------|-------|-------|--------|--------|
| [plurigrid/asi](https://github.com/plurigrid/asi) | HTML | 31 | 10 | 4 | 2026-07-10 |
| [plurigrid/asi](https://github.com/plurigrid/asi) | HTML | 16 | 5 | 3 | 2026-04-10 |
| [plurigrid/asi](https://github.com/plurigrid/asi) | HTML | 16 | 5 | 6 | 2026-04-13 |
| [plurigrid/ontology](https://github.com/plurigrid/ontology) | JavaScript | 8 | 9 | 16 | 2025-05-27 |
| [plurigrid/ontology](https://github.com/plurigrid/ontology) | JavaScript | 7 | 9 | 16 | 2025-05-27 |
| [plurigrid/ontology](https://github.com/plurigrid/ontology) | JavaScript | 7 | 9 | 16 | 2025-05-27 |
| [plurigrid/vcg-auction](https://github.com/plurigrid/vcg-auction) | Rust | 7 | 3 | 1 | 2023-03-16 |
| [plurigrid/agent](https://github.com/plurigrid/agent) | Python | 5 | 1 | 6 | 2023-03-31 |
| [plurigrid/StochFlow](https://github.com/plurigrid/StochFlow) | Python | 4 | 1 | 0 | 2024-03-20 |
| [plurigrid/asi-skills](https://github.com/plurigrid/asi-skills) | Julia | 3 | 1 | 2 | 2026-04-09 |

### Top kubeflow Repos (by stars)
| Repo | Language | Stars | Forks | Issues | Pushed |
|------|----------|-------|-------|--------|--------|
| [kubeflow/kubeflow](https://github.com/kubeflow/kubeflow) |  | 15793 | 2685 | 1 | 2026-07-10 |
| [kubeflow/kubeflow](https://github.com/kubeflow/kubeflow) |  | 15572 | 2633 | 0 | 2026-01-05 |
| [kubeflow/kubeflow](https://github.com/kubeflow/kubeflow) |  | 15565 | 2626 | 0 | 2026-01-05 |
| [kubeflow/pipelines](https://github.com/kubeflow/pipelines) | Python | 4170 | 2063 | 475 | 2026-07-25 |
| [kubeflow/pipelines](https://github.com/kubeflow/pipelines) | Python | 4119 | 1984 | 469 | 2026-04-10 |
| [kubeflow/pipelines](https://github.com/kubeflow/pipelines) | Python | 4119 | 1985 | 471 | 2026-04-14 |
| [kubeflow/spark-operator](https://github.com/kubeflow/spark-operator) | Python | 3143 | 1506 | 111 | 2026-07-25 |
| [kubeflow/spark-operator](https://github.com/kubeflow/spark-operator) | Python | 3114 | 1483 | 86 | 2026-04-13 |

### Top bmorphism Repos (by stars)
| Repo | Language | Stars | Forks | Issues |
|------|----------|-------|-------|--------|
| [bmorphism/ocaml-mcp-sdk](https://github.com/bmorphism/ocaml-mcp-sdk) | OCaml | 61 | 2 | 0 |
| [bmorphism/ocaml-mcp-sdk](https://github.com/bmorphism/ocaml-mcp-sdk) | OCaml | 60 | 2 | 0 |
| [bmorphism/ocaml-mcp-sdk](https://github.com/bmorphism/ocaml-mcp-sdk) | OCaml | 60 | 2 | 0 |
| [bmorphism/anti-bullshit-mcp-server](https://github.com/bmorphism/anti-bullshit-mcp-server) | JavaScript | 23 | 7 | 1 |
| [bmorphism/anti-bullshit-mcp-server](https://github.com/bmorphism/anti-bullshit-mcp-server) | JavaScript | 23 | 7 | 1 |
| [bmorphism/anti-bullshit-mcp-server](https://github.com/bmorphism/anti-bullshit-mcp-server) | JavaScript | 22 | 7 | 1 |
| [bmorphism/shitcoin](https://github.com/bmorphism/shitcoin) | Python | 5 | 0 | 0 |
| [bmorphism/shitcoin](https://github.com/bmorphism/shitcoin) | Python | 5 | 0 | 0 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice..Z, 28 addresses)
**Status:** All 28 wallets returned HTTP 404 — `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
This indicates the addresses do not have initialized APT coin stores on mainnet (accounts may be unregistered or use FA-based coin stores instead of legacy CoinStore).  
All entries recorded in `aptos_snapshots` with `balance_apt = NULL`.

Ledger version at query time: **6,449,770,005** (epoch 16667, block 924,794,919)

### Multisig Contract Probes
All 5 multisig contracts are **healthy** (2-of-N signatures required):

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | `0x0da4f428a0c007da0f...` | 2 | ✓ |
| A-G | `0xf56c4a1c0906214f3f...` | 2 | ✓ |
| S-T | `0x3b1c3ae905d44c3a49...` | 2 | ✓ |
| V-W | `0x40fad7b423a843650f...` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b2df40622...` | 2 | ✓ |

### MNX Testnet Markets
**Status:** `https://testnet.mnx.fi` serves a Next.js SPA — no public REST JSON API endpoints found at `/api/markets` or `/api/v1/markets`. Market data not available without authenticated client-side calls. Recorded as **unavailable** (no rows in `mnx_snapshots`).

---

## DuckDB Table Row Counts (current)

```sql
SELECT 'world_increments' as t, count(*) FROM world_increments
UNION ALL SELECT 'repo_snapshots', count(*) FROM repo_snapshots
UNION ALL SELECT 'aptos_snapshots', count(*) FROM aptos_snapshots
UNION ALL SELECT 'multisig_probes', count(*) FROM multisig_probes
UNION ALL SELECT 'mnx_snapshots', count(*) FROM mnx_snapshots;
```

| Table | Rows |
|-------|------|
| world_increments | 299 |
| repo_snapshots | 1220 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

---
*Generated by world-increment-sweep + hamming-swarm-snapshot agent*
