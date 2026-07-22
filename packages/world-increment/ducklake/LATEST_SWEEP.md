# World Increment Sweep + Hamming Swarm Snapshot
**Timestamp:** 2026-07-22T23:14:18Z  
**Run added:** 134 repo snapshots + 28 Aptos probes + 5 multisig probes  
**Cumulative DB:** 1078 repo_snapshots, 157 world_increments  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### This Run — Sources Queried
| Source | Type | Repos This Run |
|--------|------|----------------|
| AustinCStone | org/user | 86 |
| wasita | org/user | 60 |
| kristinezheng | org/user | 36 |
| M1shaaa | org/user | 32 |
| migalkin | org/user | 30 |
| DJedamski | org/user | 22 |

### GF(3) Color Chain (cumulative)
| Trit | Name | Color | Count |
|------|------|-------|-------|
| -1 | MINUS | `#cc241d` | 53 |
| 0 | ERGODIC | `#d3869b` | 51 |
| 1 | PLUS | `#b8bb26` | 53 |

### Top 10 Repos by Stars (all-time)
| Repo | Language | Stars | Forks | Last Push |
|------|----------|-------|-------|-----------|
| kubeflow/kubeflow | — | 15,788 | 2,686 | 2026-07-22 |
| kubeflow/kubeflow | — | 15,572 | 2,633 | 2026-01-05 |
| kubeflow/kubeflow | — | 15,565 | 2,626 | 2026-01-05 |
| kubeflow/pipelines | Python | 4,169 | 2,050 | 2026-07-22 |
| kubeflow/pipelines | Python | 4,119 | 1,984 | 2026-04-10 |
| kubeflow/pipelines | Python | 4,119 | 1,985 | 2026-04-14 |
| kubeflow/spark-operator | Python | 3,142 | 1,502 | 2026-07-21 |
| kubeflow/spark-operator | Python | 3,114 | 1,483 | 2026-04-13 |
| kubeflow/spark-operator | Python | 3,111 | 1,483 | 2026-04-10 |
| kubeflow/trainer | Go | 2,153 | 993 | 2026-07-22 |

### Social Graph Coverage (this run)
- **plurigrid** org: 100 repos
- **kubeflow** org: 49 repos found
- **TeglonLabs** org: 5 repos
- **bmorphism** user: 106 repos found
- **zubyul** user: 49 repos found
- **Social graph** (migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone): 91 repos found

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances — Hamming Swarm (A–Z + alice/bob)
- **28** addresses probed on Aptos mainnet (ledger v6,407,577,243)
- **All 28 addresses**: APT coin stores uninitialized (`resource_not_found`)
- Status: Accounts have not received/held APT — `0x1::coin::CoinStore<AptosCoin>` absent
- API reachable: `fullnode.mainnet.aptoslabs.com` responding correctly

### Multisig Contract Health — All 5 Healthy ✓
| Pair | Address | Threshold | Status |
|------|---------|-----------|--------|
| A-B | `0x0da4f428a0c007da0f7629...` | 2-of-N | ✓ HEALTHY |
| A-G | `0xf56c4a1c0906214f3f859c...` | 2-of-N | ✓ HEALTHY |
| Y-Z | `0xd3ffe1812b2df4062281c7...` | 2-of-N | ✓ HEALTHY |
| S-T | `0x3b1c3ae905d44c3a49f0de...` | 2-of-N | ✓ HEALTHY |
| V-W | `0x40fad7b423a843650fddca...` | 2-of-N | ✓ HEALTHY |

**All 5 multisig contracts respond correctly. 2-of-N threshold confirmed for all pairs.**

### MNX Markets (testnet.mnx.fi)
- Status: **Unavailable via REST** — Next.js SPA; no public JSON API at `/api/markets`
- `mnx_snapshots` table empty this run

---

## DuckDB Schema
```sql
world_increments   -- GF(3)-tagged event log (id%3: 0=ERGODIC #d3869b, 1=PLUS #b8bb26, -1=MINUS #cc241d)
repo_snapshots     -- GitHub repo snapshots (accumulated time-series)
aptos_snapshots    -- Hamming swarm wallet states (28 addresses)
multisig_probes    -- Multisig contract health checks (5 pairs)
mnx_snapshots      -- MNX market data (empty — SPA, no REST API)
```
