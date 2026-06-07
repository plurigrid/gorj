# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-07  
**DuckDB:** `world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted (GF3 Color Chain)

| Inc# | Source | Type | Repos | GF3 Trit | Color | Name |
|------|--------|------|-------|----------|-------|------|
| 1 | plurigrid | org | 100 (capped) | +1 | `#b8bb26` | PLUS |
| 2 | kubeflow | org | 48 | -1 | `#cc241d` | MINUS |
| 3 | TeglonLabs | org | 4 | 0 | `#d3869b` | ERGODIC |
| 4 | bmorphism | user | 100 (capped) | +1 | `#b8bb26` | PLUS |
| 5 | zubyul | user | 49 | -1 | `#cc241d` | MINUS |
| 6 | migalkin | user | 19 | 0 | `#d3869b` | ERGODIC |
| 7 | DJedamski | user | 6 | +1 | `#b8bb26` | PLUS |
| 8 | wasita | user | 11 | -1 | `#cc241d` | MINUS |
| 9 | kristinezheng | user | 5 | 0 | `#d3869b` | ERGODIC |
| 10 | M1shaaa | user | 8 | +1 | `#b8bb26` | PLUS |
| 11 | AustinCStone | user | 40 | -1 | `#cc241d` | MINUS |

**Total repo snapshots:** 390

### Top Repos by Stars

| Repository | Stars |
|-----------|-------|
| kubeflow/kubeflow | 15,705 |
| kubeflow/pipelines | 4,152 |
| kubeflow/spark-operator | 3,126 |
| kubeflow/trainer | 2,112 |
| kubeflow/katib | 1,685 |
| kubeflow/examples | 1,462 |
| kubeflow/manifests | 1,020 |
| kubeflow/arena | 811 |

### Language Distribution (Top 10)

| Language | Repos |
|----------|-------|
| Python | 82 |
| Rust | 26 |
| JavaScript | 25 |
| TypeScript | 23 |
| Go | 15 |
| HTML | 15 |
| Jupyter Notebook | 14 |
| Clojure | 14 |
| Julia | 9 |
| Zig | 7 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 Hamming-swarm addresses (alice, bob, A-Z) probed against
fullnode.mainnet.aptoslabs.com. All returned 0 APT — no active
0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin> resource found.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A-Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes

All 5 multisig accounts healthy (num_signatures_required = 2):

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | YES |
| A-G | 0xf56c...0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

### MNX Markets (testnet.mnx.fi)

Status: UNAVAILABLE — testnet.mnx.fi is a client-side SPA with no
accessible JSON API endpoints (/api/markets, /api/v1/markets, /api/tickers
all returned empty). No market data recorded.

---

## DuckDB Tables

| Table | Rows |
|-------|------|
| world_increments | 11 |
| repo_snapshots | 390 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |
