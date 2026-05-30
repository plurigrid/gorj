# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep Date:** 2026-05-30  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured | Max Stars |
|--------|------|---------------|-----------|
| plurigrid | org | 100 | 23 |
| kubeflow | org | 48 | 15,687 |
| TeglonLabs | org | 4 | 2 |
| bmorphism | user | 19 | 144 |
| zubyul | user | 100 | 61 |
| migalkin | user (social) | 40 | 92 |
| DJedamski | user (social) | 6 | 1 |
| wasita | user (social) | 11 | 2 |
| kristinezheng | user (social) | 6 | 0 |
| M1shaaa | user (social) | 8 | 0 |

**Total this run:** 342 repo snapshots → 365 world_increments total in DB.

### Top Repos by Stars (this sweep)
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,687 | — | 2026-05-24 |
| kubeflow/pipelines | 4,150 | Python | 2026-05-29 |
| kubeflow/spark-operator | 3,124 | Python | 2026-05-29 |
| kubeflow/trainer | 2,107 | Go | 2026-05-30 |
| kubeflow/katib | 1,685 | Python | 2026-05-29 |
| bmorphism/* | 144 max | — | — |
| migalkin/* | 92 max | — | — |
| plurigrid/asi | 23 | HTML | 2026-04-26 |
| plurigrid/gorj | 0 | Clojure | 2026-05-30 |

### GF(3) Color Chain (this sweep)
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 114 |
| +1 | `#b8bb26` | PLUS | 114 |
| −1 | `#cc241d` | MINUS | 114 |

342 increments perfectly balanced across the trinary field (114 each).

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)
All 28 addresses queried (alice, bob, A–Z). All returned **0 APT** — accounts have no APT CoinStore resource on mainnet (unfunded or non-existent).

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...4cc7b | 0 |
| bob | 0x0a3c...512d5d | 0 |
| A–Z | (26 addresses) | 0 each |

### Multisig Contract Probes
All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All multisig contracts healthy — 2-of-N threshold confirmed on all 5 pairs.

### MNX Markets (testnet.mnx.fi)
- `GET /api/markets` → empty (SPA serves no REST JSON)
- `GET /api/v1/markets` → empty
- Root HTML returned (client-rendered SPA)
- **Status:** unavailable via server-side fetch; no market data captured.

---

## DuckDB Tables Summary

```sql
SELECT count(*) FROM world_increments;   -- 365
SELECT count(*) FROM repo_snapshots;     -- 1286
SELECT count(*) FROM aptos_snapshots;    --  28
SELECT count(*) FROM multisig_probes;    --   5
SELECT count(*) FROM mnx_snapshots;      --   0
```
