# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-06-05T00:08 UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social | 19 |
| DJedamski | social | 6 |
| wasita | social | 11 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| AustinCStone | social | 40 |
| **TOTAL** | | **390 queried / 320 stored** |

### Top 10 Repos by Stars

| Repo | Language | Stars | Forks |
|------|----------|-------|-------|
| kubeflow/kubeflow | — | 15,706 | 2,670 |
| kubeflow/pipelines | Python | 4,152 | 2,005 |
| kubeflow/spark-operator | Python | 3,124 | 1,488 |
| kubeflow/trainer | Go | 2,111 | 964 |
| kubeflow/katib | Python | 1,684 | 525 |
| kubeflow/examples | Jsonnet | 1,462 | 756 |
| kubeflow/manifests | YAML | 1,020 | 1,065 |
| kubeflow/arena | Go | 811 | 191 |
| kubeflow/kale | Python | 690 | 155 |
| kubeflow/mpi-operator | Go | 528 | 235 |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 106 |
| 1 | #b8bb26 | PLUS | 107 |
| -1 | #cc241d | MINUS | 107 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 wallets probed on Aptos mainnet (fullnode.mainnet.aptoslabs.com).
Result: all CoinStore resources returned null — addresses exist on-chain but
0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin> resource not registered
(accounts hold zero native APT or use the Fungible Asset standard).

| World | Address | APT Balance |
|-------|---------|-------------|
| alice | 0xc793...cc7b | NULL |
| bob | 0x0a3c...2d5d | NULL |
| A-Z | 0x8699...197c | NULL (all 26) |

### Multisig Contract Probes (5 pairs)

All 5 multisig accounts respond healthy with 2-of-n threshold.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | 2 | true |
| A-G | 0xf56c...096 | 2 | true |
| Y-Z | 0xd3ff...883 | 2 | true |
| S-T | 0x3b1c...883 | 2 | true |
| V-W | 0x40fa...b6d | 2 | true |

### MNX Markets (testnet.mnx.fi)

Status: HTTP 401 Unauthorized — testnet requires authentication.
/api/markets, /api/v1/markets, /api/tickers all inaccessible without credentials.
mnx_snapshots table remains empty this sweep.

---

## DuckDB Table Summary

| Table | Rows |
|-------|------|
| world_increments | 320 |
| repo_snapshots | 320 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |
