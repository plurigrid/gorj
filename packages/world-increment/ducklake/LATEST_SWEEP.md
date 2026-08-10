# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-08-10  
**Run:** world-increment-sweep + hamming-swarm-snapshot  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 50 (of 100+) |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 50 (of 100+) |
| zubyul | user | 49 |
| migalkin | social graph | 5 |
| wasita | social graph | 5 |
| DJedamski | social graph | 3 |
| kristinezheng | social graph | 4 |
| M1shaaa | social graph | 3 |
| AustinCStone | social graph | 5 |

**Total repo snapshots this run:** 228  
**Cumulative in DB:** 1,172 (across sweeps)

### Top Repos by Stars (Cumulative)

| Org/User | Repo | Language | Stars | Last Pushed |
|----------|------|----------|-------|-------------|
| kubeflow | kubeflow | — | 15,809 | 2026-07-10 |
| kubeflow | pipelines | Python | 4,180 | 2026-08-10 |
| kubeflow | spark-operator | Python | 3,146 | 2026-08-09 |
| kubeflow | trainer | Go | 2,177 | 2026-08-10 |
| kubeflow | katib | Python | 1,694 | 2026-08-06 |

### Language Distribution (Cumulative Snapshots)

| Language | Repos |
|----------|-------|
| Python | 205 |
| Go | 51 |
| HTML | 50 |
| Rust | 44 |
| JavaScript | 38 |
| Jupyter Notebook | 37 |
| TypeScript | 31 |
| Clojure | 29 |
| Jsonnet | 23 |
| R | 18 |

### GF(3) World-Increment Color Chain

| GF3 Name | Color | Count |
|----------|-------|-------|
| ERGODIC | #d3869b (trit=0) | 10 |
| PLUS | #b8bb26 (trit=1) | 12 |
| MINUS | #cc241d (trit=-1) | 12 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 wallets probed via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

**Status:** All 28 accounts returned 0 APT. Accounts appear to be unfunded on mainnet (CoinStore resource not initialized or zero balance). This is consistent with prior sweeps.

### Multisig Contract Probes

All 5 multisig contracts queried via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

**Status:** All 5 multisig contracts are live and require 2-of-N signatures. All healthy.

### MNX Markets (testnet.mnx.fi)

**Status:** `testnet.mnx.fi` is a Next.js SPA. No REST API endpoints (`/api/markets`, `/api/v1/markets`) returned JSON data — the server serves the SPA shell for all paths. Market data unavailable via scraping. No records inserted into `mnx_snapshots`.

---

## DuckDB Table Summary

| Table | Rows |
|-------|------|
| world_increments | 34 |
| repo_snapshots | 1,172 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA, unavailable) |

---

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent*
