# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-08-05 UTC  
**Run type:** Scheduled autonomous sweep

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social | 19 |
| DJedamski | social | 6 |
| wasita | social | 14 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| AustinCStone | social | 41 |

**Total repos snapshotted this run:** 396  
**Total repo_snapshots in DB:** 1,340  
**Total world_increments in DB:** 419

### Most Recently Active Repos (pushed today)

| Source | Repo | Last Push |
|--------|------|-----------|
| plurigrid | gorj | 2026-08-05T20:22Z |
| kubeflow | trainer | 2026-08-05T19:01Z |
| kubeflow | pipelines | 2026-08-05T18:54Z |
| kubeflow | sdk | 2026-08-05T17:20Z |
| kubeflow | dashboard | 2026-08-05T15:44Z |
| wasita | xoxowasita-analysis | 2026-08-05T15:35Z |
| M1shaaa | M1shaaa | 2026-08-05T13:59Z |
| bmorphism | Gay.jl | 2026-08-05T02:24Z |

### Top Languages (all-time in DB)

| Language | Count |
|----------|-------|
| Python | 234 |
| Rust | 57 |
| HTML | 54 |
| JavaScript | 53 |
| Go | 51 |
| TypeScript | 46 |
| Jupyter Notebook | 40 |
| Clojure | 30 |
| Jsonnet | 23 |
| R | 22 |

### Top Starred Repos

| Repo | Stars |
|------|-------|
| kubeflow/kubeflow | 15,805 |
| kubeflow/pipelines | 4,178 |
| kubeflow/spark-operator | 3,144 |
| kubeflow/trainer | 2,171 |

### GF(3) Color Chain Distribution

| Name | Color | Count |
|------|-------|-------|
| ERGODIC (trit=0) | #d3869b | 139 |
| MINUS (trit=-1) | #cc241d | 140 |
| PLUS (trit=1) | #b8bb26 | 140 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

Queried 28 addresses (alice, bob, A–Z) via Aptos mainnet fullnode.

**Result:** All 28 wallets returned 0 APT (accounts unfunded or CoinStore resource not initialized on mainnet).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts responded successfully with 2 signatures required — healthy.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ Healthy |
| A-G | 0xf56c...0096 | 2 | ✓ Healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ Healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ Healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ Healthy |

### MNX Markets (testnet.mnx.fi)

API endpoint `https://testnet.mnx.fi/api/markets` returned **HTTP 404 — unavailable**. No market data collected this run.

---

## DuckDB Ducklake State

**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 419 |
| repo_snapshots | 1,340 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |
