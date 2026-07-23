# World Increment + Hamming Swarm Snapshot

**Sweep date:** 2026-07-23  
**Engine:** DuckDB 1.5.5 ducklake  

---

## JOB 1: GitHub Social Graph Sweep

**Repo snapshots:** 394  
**World increments:** 394  
**Sources:** plurigrid (org), kubeflow (org), TeglonLabs (org), bmorphism (user), zubyul (user), migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone  

### GF(3) Color Chain

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 131 |
| -1 | `#cc241d` | MINUS | 131 |
| 1 | `#b8bb26` | PLUS | 132 |

### Source Breakdown

| Source | Repos Snapshotted | Total Stars |
|--------|-------------------|-------------|
| plurigrid | 100 | 83 |
| bmorphism | 100 | 246 |
| zubyul | 49 | 14 |
| kubeflow | 49 | 34404 |
| AustinCStone | 41 | 108 |
| migalkin | 19 | 279 |
| wasita | 12 | 5 |
| M1shaaa | 8 | 0 |
| DJedamski | 6 | 3 |
| TeglonLabs | 5 | 2 |
| kristinezheng | 5 | 0 |

### Top Starred Repos (>100 stars)

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | N/A | 15789 | 2026-07-10 |
| kubeflow/pipelines | Python | 4169 | 2026-07-23 |
| kubeflow/spark-operator | Python | 3142 | 2026-07-17 |
| kubeflow/trainer | Go | 2153 | 2026-07-23 |
| kubeflow/katib | Python | 1692 | 2026-07-22 |
| kubeflow/examples | Jsonnet | 1461 | 2025-04-14 |
| kubeflow/community-distribution | YAML | 1029 | 2026-07-21 |
| kubeflow/arena | Go | 815 | 2026-07-21 |
| kubeflow/kale | Python | 695 | 2026-07-23 |
| kubeflow/mpi-operator | Go | 530 | 2026-07-22 |
| kubeflow/fairing | Jsonnet | 337 | 2022-04-11 |
| kubeflow/pytorch-operator | Jsonnet | 310 | 2021-12-01 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (A–Z + alice/bob)

- **Wallets queried:** 28
- **Status:** All `resource_not_found` — CoinStore not initialized (accounts not yet on-chain or no APT received)
- **Network:** Aptos mainnet fullnode (`fullnode.mainnet.aptoslabs.com`)

### Multisig Contract Probes

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4f428a0c007da0f...` | 2 | HEALTHY |
| A-G | `0xf56c4a1c0906214f3f...` | 2 | HEALTHY |
| S-T | `0x3b1c3ae905d44c3a49...` | 2 | HEALTHY |
| V-W | `0x40fad7b423a843650f...` | 2 | HEALTHY |
| Y-Z | `0xd3ffe1812b2df40622...` | 2 | HEALTHY |

**All 5 multisig contracts responding and require 2-of-N signatures.**

### MNX Markets (testnet.mnx.fi)

- **Status:** UNAVAILABLE — Next.js SPA, no public REST API endpoints accessible
- **Probed:** `/api/markets`, `/api/v1/markets`, root HTML

---

## DuckDB Schema (`world-increments.duckdb`)

```
TABLE world_increments   — GF(3) color-coded event log (394 rows)
TABLE repo_snapshots     — GitHub repo metadata (394 rows)
TABLE aptos_snapshots    — Hamming swarm wallet states (28 rows, all uninit)
TABLE multisig_probes    — Aptos 2-of-N multisig health (5 rows, all healthy)
TABLE mnx_snapshots      — MNX market data (1 row, unavailable)
```