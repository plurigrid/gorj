# World Increment Sweep + Hamming Snapshot

**Timestamp:** 2026-06-05T02:04 UTC  
**Branch:** world-increment/sweep-2026-06-05-0204  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 48 |
| AustinCStone | zubyul social graph | 30 |
| migalkin | zubyul social graph | 19 |
| wasita | zubyul social graph | 11 |
| M1shaaa | zubyul social graph | 8 |
| DJedamski | zubyul social graph | 6 |
| kristinezheng | zubyul social graph | 5 |
| TeglonLabs | org | 4 |
| **TOTAL** | | **380** |

### Top Repos by Stars
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,706 | — |
| kubeflow/pipelines | 4,152 | Python |
| kubeflow/spark-operator | 3,124 | Python |
| kubeflow/trainer | 2,111 | Go |
| kubeflow/katib | 1,684 | Python |
| kubeflow/manifests | 1,020 | YAML |

### GF(3) Color Chain Distribution
| Trit | Color | Name | Count |
|------|-------|------|-------|
| +1 | `#b8bb26` | PLUS | 127 |
| -1 | `#cc241d` | MINUS | 127 |
| 0 | `#d3869b` | ERGODIC | 126 |

Color chain: `id % 3 == 0` → trit=0 ERGODIC `#d3869b`, `id % 3 == 1` → trit=1 PLUS `#b8bb26`, `id % 3 == 2` → trit=-1 MINUS `#cc241d`.

### DuckDB Tables
- **world_increments**: 380 rows — one per repo with GF3 color, source metadata, snapshot hash
- **repo_snapshots**: 380 rows — full repo metadata (language, stars, forks, open_issues, pushed_at, description)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
28 addresses queried (alice, bob, A-Z).  
**All wallets returned 0 APT** — none of the addresses have a funded `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource on mainnet at time of sweep.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A-Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes
5 contracts probed via `0x1::multisig_account::num_signatures_required`.  
**All 5 healthy — 2-of-N threshold.**

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | yes |
| A-G | 0xf56c...0096 | 2 | yes |
| Y-Z | 0xd3ff...b883 | 2 | yes |
| S-T | 0x3b1c...7883 | 2 | yes |
| V-W | 0x40fa...eb6d | 2 | yes |

### MNX Markets (testnet.mnx.fi)
**Status: Unavailable** — `https://testnet.mnx.fi` returns HTTP 401 (Vercel authentication required). All API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`) similarly auth-gated. No market data captured; `mnx_snapshots` table is empty.

---

## DuckDB Schema Summary

```sql
world_increments   -- 380 rows: GF3 color chain over all repo events
repo_snapshots     -- 380 rows: org/user, repo, language, stars, forks, issues, pushed_at
aptos_snapshots    --  28 rows: hamming swarm A-Z + alice/bob, all 0 APT
multisig_probes    --   5 rows: A-B, A-G, Y-Z, S-T, V-W all 2-of-N healthy
mnx_snapshots      --   0 rows: Vercel auth blocked
```
