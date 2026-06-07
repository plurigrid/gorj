# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-07  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| # | GF3 | Color | Source | Type | Repos |
|---|-----|-------|--------|------|-------|
| 1 | PLUS +1 | `#b8bb26` | plurigrid | org | 100 |
| 2 | MINUS -1 | `#cc241d` | kubeflow | org | 48 |
| 3 | ERGODIC 0 | `#d3869b` | TeglonLabs | org | 4 |
| 4 | PLUS +1 | `#b8bb26` | bmorphism | user | 100 |
| 5 | MINUS -1 | `#cc241d` | zubyul | user | 49 |
| 6 | ERGODIC 0 | `#d3869b` | migalkin | user | 19 |
| 7 | PLUS +1 | `#b8bb26` | DJedamski | user | 6 |
| 8 | MINUS -1 | `#cc241d` | wasita | user | 11 |
| 9 | ERGODIC 0 | `#d3869b` | kristinezheng | user | 5 |
| 10 | PLUS +1 | `#b8bb26` | M1shaaa | user | 8 |
| 11 | MINUS -1 | `#cc241d` | AustinCStone | user | 40 |

**Total repo snapshots: 390**

### Top Starred Repos

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,706 | — |
| kubeflow/pipelines | 4,153 | Python |
| kubeflow/spark-operator | 3,125 | Python |
| kubeflow/trainer | 2,112 | Go |
| kubeflow/katib | 1,685 | Python |
| kubeflow/examples | 1,462 | Jsonnet |
| kubeflow/manifests | 1,020 | YAML |
| kubeflow/arena | 811 | Go |
| kubeflow/kale | 691 | Python |
| kubeflow/mpi-operator | 528 | Go |

### Language Distribution (top 15)

| Language | Repos |
|----------|-------|
| Python | 82 |
| Rust | 26 |
| JavaScript | 25 |
| TypeScript | 23 |
| Go | 15 |
| HTML | 15 |
| Clojure | 14 |
| Jupyter Notebook | 14 |
| Julia | 9 |
| Zig | 7 |
| Jsonnet | 7 |
| Svelte | 6 |
| R | 6 |
| Java | 6 |
| TeX | 5 |

Notable: plurigrid/bmorphism social graph shows strong Clojure (14 repos) and Rust (26 repos) presence.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (A–Z + alice + bob)

All 28 Hamming-swarm addresses were probed against `fullnode.mainnet.aptoslabs.com`.  
Result: **all balances NULL** — none of the queried accounts have an initialized  
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource on mainnet at time of sweep.  
This may indicate accounts holding APT via a different resource type, or unfunded accounts.

### Multisig Contract Probes

All 5 multisig pairs returned `2` signatures required — **all healthy (2-of-2)**.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4…7003 | 2 | ✓ |
| A-G | 0xf56c…0096 | 2 | ✓ |
| Y-Z | 0xd3ff…b883 | 2 | ✓ |
| S-T | 0x3b1c…7883 | 2 | ✓ |
| V-W | 0x40fa…eb6d | 2 | ✓ |

### MNX Markets

`testnet.mnx.fi` — **unavailable** at time of sweep. No API endpoints responded  
(`/api/markets`, `/api/v1/markets`, `/api/tickers`, root). Recorded as no data.

---

## DuckDB Schema Summary

```
world_increments:  11 rows  (GF3 color chain: 3 orgs + 8 users)
repo_snapshots:   390 rows  (11 sources: plurigrid, kubeflow, TeglonLabs,
                             bmorphism, zubyul, migalkin, DJedamski, wasita,
                             kristinezheng, M1shaaa, AustinCStone)
aptos_snapshots:   28 rows  (alice, bob, A-Z; all NULL - no CoinStore found)
multisig_probes:    5 rows  (A-B, A-G, Y-Z, S-T, V-W; all 2-of-2 healthy)
mnx_snapshots:      0 rows  (testnet.mnx.fi unavailable)
```
