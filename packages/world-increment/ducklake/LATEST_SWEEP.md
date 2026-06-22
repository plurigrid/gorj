# World Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-06-22  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| # | Source | Type | GF3 Trit | GF3 Color | GF3 Name |
|---|--------|------|----------|-----------|----------|
| 1 | plurigrid | org | +1 | #b8bb26 | PLUS |
| 2 | kubeflow | org | -1 | #cc241d | MINUS |
| 3 | bmorphism | user | 0 | #d3869b | ERGODIC |
| 4 | zubyul | user | +1 | #b8bb26 | PLUS |
| 5 | migalkin | social-graph | -1 | #cc241d | MINUS |
| 6 | DJedamski | social-graph | 0 | #d3869b | ERGODIC |
| 7 | wasita | social-graph | +1 | #b8bb26 | PLUS |
| 8 | kristinezheng | social-graph | -1 | #cc241d | MINUS |
| 9 | M1shaaa | social-graph | 0 | #d3869b | ERGODIC |
| 10 | AustinCStone | social-graph | +1 | #b8bb26 | PLUS |
| 11 | TeglonLabs | org | -1 | #cc241d | MINUS |

### Repo Counts

| Source | Repos |
|--------|-------|
| plurigrid | 100 |
| kubeflow | 48 |
| bmorphism | 100 |
| zubyul | 49 |
| migalkin | 19 |
| DJedamski | 6 |
| wasita | 11 |
| kristinezheng | 5 |
| M1shaaa | 8 |
| AustinCStone | 40 |
| TeglonLabs | 5 |
| **Total** | **391** |

### Most Recently Pushed (Top 8)

| Repo | Pushed At |
|------|-----------|
| kubeflow/mpi-operator | 2026-06-22T17:55:37Z |
| plurigrid/gorj | 2026-06-22T17:18:30Z |
| kubeflow/mcp-apache-spark-history-server | 2026-06-22T16:51:05Z |
| kubeflow/spark-operator | 2026-06-22T15:42:54Z |
| kubeflow/dashboard | 2026-06-22T14:41:45Z |
| kubeflow/hub | 2026-06-22T14:15:36Z |
| kubeflow/trainer | 2026-06-22T11:34:59Z |
| kubeflow/sdk | 2026-06-22T11:33:29Z |

### Stars Leaderboard (Top 10)

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15740 | - |
| kubeflow/pipelines | 4157 | Python |
| kubeflow/spark-operator | 3128 | Python |
| kubeflow/trainer | 2118 | Go |
| kubeflow/katib | 1685 | Python |
| kubeflow/examples | 1460 | Jsonnet |
| kubeflow/community-distribution | 1027 | YAML |
| kubeflow/arena | 813 | Go |
| kubeflow/kale | 694 | Python |
| kubeflow/mpi-operator | 528 | Go |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All 28 Hamming-swarm addresses returned **0.0 APT** -- accounts either unfunded on mainnet or CoinStore resource not initialized.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...12d5 | 0.0 |
| A-Z (26) | 0x8699...to 0x7af0... | 0.0 each |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **healthy** with `num_signatures_required = 2`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...987003 | 2 | YES |
| A-G | 0xf56c4a1c...0096 | 2 | YES |
| Y-Z | 0xd3ffe181...b883 | 2 | YES |
| S-T | 0x3b1c3ae9...7883 | 2 | YES |
| V-W | 0x40fad7b4...eb6d | 2 | YES |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** -- testnet.mnx.fi is behind Vercel deployment protection (authentication required). All API paths (/, /api/markets, /api/v1/markets, /markets) return 401 Authentication Required. No market data could be extracted. mnx_snapshots table is empty.

---

## DuckDB Schema Summary

| Table | Rows |
|-------|------|
| world_increments | 11 |
| repo_snapshots | 344 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |
