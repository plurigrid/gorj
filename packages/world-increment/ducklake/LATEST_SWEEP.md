# World-Increment Sweep — 2026-05-18

## GF(3) Increment

| Field | Value |
|---|---|
| ID | 13 |
| Trit | 1 |
| Color | `#b8bb26` (PLUS) |
| Snapshot Hash | `15be38e6f8427b6a` |
| Timestamp | 2026-05-18 |

## GitHub Social Graph Sweep

### Sources
| Source | Type | Repos |
|---|---|---|
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
| AustinCStone | user (zubyul social) | 30 |
| **TOTAL** | | **381** |

### Top Starred Repos
| Repo | Stars |
|---|---|
| `plurigrid/gorj` | 2026-05-18T01:20:03Z |
| `bmorphism/Gay.jl` | 2026-05-18T00:35:46Z |
| `kubeflow/pipelines` | 2026-05-17T16:25:03Z |
| `wasita/wasita.github.io` | 2026-05-17T00:36:54Z |
| `kubeflow/manifests` | 2026-05-16T16:37:54Z |
| `kubeflow/dashboard` | 2026-05-16T00:25:13Z |
| `kubeflow/mlflow-integration` | 2026-05-15T19:20:29Z |
| `kubeflow/kale` | 2026-05-15T19:04:47Z |
| `kubeflow/spark-operator` | 2026-05-15T16:31:02Z |
| `kubeflow/notebooks` | 2026-05-15T15:41:12Z |
| `kubeflow/hub` | 2026-05-15T15:36:02Z |
| `kubeflow/trainer` | 2026-05-15T15:21:03Z |
| `bmorphism/oxgame` | 2026-05-15T09:53:27Z |
| `kristinezheng/kristinezheng.github.io` | 2026-05-14T22:29:01Z |
| `kubeflow/website` | 2026-05-14T17:20:09Z |

## Hamming Swarm — Aptos Snapshot

### Wallet Balances
- **Total wallets probed:** 28 (alice, bob, A–Z)
- **Funded wallets:** 0
- **Total APT across all wallets:** 0.00000000
- **Note:** All wallets returned 0 APT (accounts not funded on Aptos mainnet or CoinStore resource not initialized)

### Multisig Contracts
| Pair | Address | Sigs Required | Healthy |
|---|---|---|---|
| A-B | `0x0da4f428a0c007…` | 2 | ✓ |
| A-G | `0xf56c4a1c090621…` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b2df4…` | 2 | ✓ |
| S-T | `0x3b1c3ae905d44c…` | 2 | ✓ |
| V-W | `0x40fad7b423a843…` | 2 | ✓ |

All 5 multisig contracts healthy — 2-of-N signatures required.

## MNX Markets (testnet.mnx.fi)

**Status:** Unavailable as REST API. `testnet.mnx.fi` is a Next.js SPA (server-side rendered) — no `/api/markets` or `/api/v1/markets` endpoint found. Market data not extractable without browser execution.

## DuckDB Ducklake

All data stored in `packages/world-increment/ducklake/world-increments.duckdb`:
- `world_increments` — GF(3) sweep events
- `repo_snapshots` — GitHub repo data
- `aptos_snapshots` — Hamming swarm wallet balances
- `multisig_probes` — Aptos multisig contract health
- `mnx_snapshots` — MNX market data (empty this sweep)
