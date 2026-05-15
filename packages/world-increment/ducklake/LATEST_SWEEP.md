# LATEST_SWEEP — 2026-05-07 06:15:44 UTC

## JOB 1: GitHub Social Graph Sweep

### Coverage
| Source | Type | Repos Sampled |
|--------|------|--------------|
| plurigrid | org | 212 |
| bmorphism | user | 210 |
| TeglonLabs | org | 110 |
| kubeflow | org | 106 |
| AustinCStone | user | 92 |
| migalkin | user | 66 |
| wasita | user | 61 |
| zubyul | user | 56 |
| kristinezheng | user | 42 |
| M1shaaa | user | 38 |
| DJedamski | user | 26 |

**Total world_increments:** 98  
**Total repo_snapshots (all runs):** 1019

### GF(3) Color Chain Distribution
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 32 |
| -1 | `#cc241d` | MINUS | 33 |
| 1 | `#b8bb26` | PLUS | 33 |

### Top Repos by Stars
| Repo | Language | Stars | Forks | Last Push |
|------|----------|-------|-------|-----------|
| kubeflow/kubeflow | - | 15624 | 2647 | 2026-04-29 |
| kubeflow/kubeflow | - | 15572 | 2633 | 2026-01-05 |
| kubeflow/kubeflow | - | 15565 | 2626 | 2026-01-05 |
| kubeflow/pipelines | Python | 4135 | 1988 | 2026-05-07 |
| kubeflow/pipelines | Python | 4119 | 1984 | 2026-04-10 |
| kubeflow/pipelines | Python | 4119 | 1985 | 2026-04-14 |
| kubeflow/spark-operator | Python | 3124 | 1482 | 2026-05-05 |
| kubeflow/spark-operator | Python | 3114 | 1483 | 2026-04-13 |
| kubeflow/spark-operator | Python | 3111 | 1483 | 2026-04-10 |
| kubeflow/trainer | Go | 2095 | 948 | 2026-05-06 |
| kubeflow/trainer | Go | 2082 | 945 | 2026-04-13 |
| kubeflow/trainer | Go | 2080 | 944 | 2026-04-10 |
| kubeflow/katib | Python | 1683 | 522 | 2026-05-06 |
| kubeflow/katib | Python | 1678 | 521 | 2026-04-14 |
| kubeflow/katib | Python | 1676 | 521 | 2026-04-02 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
All 28 Hamming swarm addresses (alice, bob, A–Z) probed via  
`https://fullnode.mainnet.aptoslabs.com/v1/`.  
**Result:** All addresses return `resource_not_found` for  
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — wallets not yet  
initialized on mainnet (no APT CoinStore registered).  
Balance: **0.0 APT** for all 28 worlds.

### Multisig Contract Probes
| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428a0...` | 2 | ✓ |
| A-G | `0xf56c4a1c09...` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b...` | 2 | ✓ |
| S-T | `0x3b1c3ae905...` | 2 | ✓ |
| V-W | `0x40fad7b423...` | 2 | ✓ |

**All 5 multisig contracts healthy** — each requires 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)
MNX testnet frontend is a Next.js SPA; no public JSON API endpoint  
found at `/api/markets` or `/api/v1/markets`. Market data **unavailable**  
from server-side scraping.

---

## DuckDB Schema (ducklake/world-increments.duckdb)

| Table | Purpose |
|-------|---------|
| `world_increments` | GF(3)-colored event log |
| `repo_snapshots` | GitHub repo metadata snapshots |
| `aptos_snapshots` | Aptos mainnet wallet balances |
| `multisig_probes` | Multisig contract health checks |
| `mnx_snapshots` | MNX market data (empty — SPA) |

GF(3) chain: `id%3==0` → trit=0 ERGODIC `#d3869b` |  
`id%3==1` → trit=1 PLUS `#b8bb26` |  
`id%3==2` → trit=-1 MINUS `#cc241d`
