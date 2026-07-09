# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-09  **Time:** 15:12 UTC

## GitHub Social Graph Sweep

### Coverage

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| TeglonLabs | org | 5 |
| migalkin | user | 5 |
| wasita | user | 3 |
| AustinCStone | user | 3 |
| DJedamski | user | 2 |
| kristinezheng | user | 2 |
| M1shaaa | user | 2 |

**This sweep:** 320 repos from 11 sources
**Cumulative DB:** 1264 repo snapshots across 34 world-increment entries

### Top Repos by Stars (This Sweep)

| Repo | Language | Stars | Last Push | Description |
|------|----------|-------|-----------|-------------|
| kubeflow/kubeflow | - | 15769 | 2026-07-08 | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | Python | 4169 | 2026-07-09 | Machine Learning Pipelines for Kubeflow |
| kubeflow/spark-operator | Python | 3136 | 2026-07-08 | Kubernetes operator for managing the lifecycle of Apache Spa |
| kubeflow/trainer | Go | 2134 | 2026-07-08 | Distributed AI Model Training and LLM Fine-Tuning on Kuberne |
| kubeflow/katib | Python | 1689 | 2026-07-09 | Automated Machine Learning on Kubernetes |
| kubeflow/examples | Jsonnet | 1460 | 2025-04-14 | A repository to host extended examples and tutorials |
| kubeflow/community-distribution | YAML | 1029 | 2026-07-09 | Kubeflow Community Distribution |
| kubeflow/arena | Go | 815 | 2026-07-09 | A CLI for Kubeflow.  |
| kubeflow/kale | Python | 695 | 2026-07-01 | Kubeflow’s superfood for Data Scientists |
| kubeflow/mpi-operator | Go | 529 | 2026-07-07 | Kubernetes Operator for MPI-based applications (distributed  |

### GF(3) Color Chain

- trit=0 (id%3==0): ERGODIC #d3869b
- trit=1 (id%3==1): PLUS #b8bb26
- trit=-1 (id%3==2): MINUS #cc241d

## Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances

- **Addresses probed:** 28
- **Resource not found (inactive accounts):** 28/28
- **Status:** All 28 Hamming-swarm addresses (alice, bob, A–Z) return `Resource not found`
  on `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — accounts not active on mainnet.

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| V-W | 0x40fad7b4...80eb6d | 2 | ✓ |
| S-T | 0x3b1c3ae9...ed7883 | 2 | ✓ |
| Y-Z | 0xd3ffe181...75b883 | 2 | ✓ |
| A-G | 0xf56c4a1c...bc0096 | 2 | ✓ |
| A-B | 0x0da4f428...987003 | 2 | ✓ |

**All 5 multisig contracts healthy** — each requires 2 signatures.

### MNX Markets (testnet.mnx.fi)

- **Status:** Unavailable — `https://testnet.mnx.fi` and `/api/markets` both return HTTP 401 Unauthorized.
  Market data requires authentication token not available in this sweep context.

## DuckDB Schema

Tables: `world_increments`, `repo_snapshots`, `aptos_snapshots`, `multisig_probes`, `mnx_snapshots`

Path: `packages/world-increment/ducklake/world-increments.duckdb`
