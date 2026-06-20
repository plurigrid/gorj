# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-20
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`
**GF(3) chain:** id%3==0 → ERGODIC #d3869b | id%3==1 → PLUS #b8bb26 | id%3==2 → MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 48 |
| AustinCStone | user (social) | 40 |
| migalkin | user (social) | 19 |
| wasita | user (social) | 11 |
| M1shaaa | user (social) | 8 |
| DJedamski | user (social) | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user (social) | 5 |
| **TOTAL** | | **391 unique repos** |

### Top Languages
| Language | Repos |
|----------|-------|
| Python | 80 |
| Rust | 26 |
| JavaScript | 25 |
| TypeScript | 23 |
| HTML | 17 |
| Go | 15 |
| Clojure | 14 |
| Jupyter Notebook | 14 |
| Julia | 9 |
| Jsonnet | 7 |

### Top Stars
| Repo | Stars |
|------|-------|
| kubeflow/kubeflow | 15,736 |
| kubeflow/pipelines | 4,154 |
| kubeflow/spark-operator | 3,127 |
| kubeflow/trainer | 2,117 |
| kubeflow/katib | 1,683 |

### Recent Activity Highlights
- **wasita/proj-template** pushed 2026-06-19 (yesterday)
- **M1shaaa/M1shaaa** pushed 2026-06-20 (today)
- **kristinezheng/kristinezheng.github.io** pushed 2026-06-07
- **TeglonLabs/jank-crane** pushed 2026-06-08 (crane-jank GF3 convergence maps)

### DuckDB Tables
- `world_increments`: 391 rows (GF3 color-chained)
- `repo_snapshots`: 391 rows

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
All 28 wallets probed via fullnode.mainnet.aptoslabs.com.

| World | Balance (APT) | Note |
|-------|--------------|------|
| alice | 0.00 | uninitialized CoinStore |
| bob | 0.00 | uninitialized CoinStore |
| A-Z (26 wallets) | 0.00 each | uninitialized CoinStores |

All 28 wallets return 0 APT. These appear to be uninitialized CoinStore accounts with no deposited APT on mainnet.

### Multisig Contract Probes
All 5 contracts queried via 0x1::multisig_account::num_signatures_required.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...87003 | 2 | HEALTHY |
| A-G | 0xf56c4a1c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ffe181...b883 | 2 | HEALTHY |
| S-T | 0x3b1c3ae9...7883 | 2 | HEALTHY |
| V-W | 0x40fad7b4...eb6d | 2 | HEALTHY |

All 5 multisig contracts are live and require 2-of-N signatures. No anomalies detected.

### MNX Markets
testnet.mnx.fi is protected by Vercel deployment authentication. No public API accessible. Market data unavailable this sweep.

---

## GF(3) Color Chain Summary
- ERGODIC (#d3869b, trit=0): 131 increments (id mod 3 == 0)
- PLUS (#b8bb26, trit=1): 130 increments (id mod 3 == 1)
- MINUS (#cc241d, trit=-1): 130 increments (id mod 3 == 2)
