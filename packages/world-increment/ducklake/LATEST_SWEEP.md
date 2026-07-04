# World-Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-07-04 07:11:13 UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | Org | 168 |
| bmorphism | User | 165 |
| zubyul | User | 59 |
| TeglonLabs | Org | 54 |
| kubeflow | Org | 50 |
| AustinCStone | User | 43 |
| wasita | User | 31 |
| migalkin | User | 30 |
| kristinezheng | User | 18 |
| M1shaaa | User | 16 |
| DJedamski | User | 11 |

**Total unique repos:** 645

### Top 15 Repos by Stars

| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| [kubeflow/kubeflow](https://github.com/kubeflow/kubeflow) | 15761 | — | Machine Learning Toolkit for Kubernetes |
| [kubeflow/pipelines](https://github.com/kubeflow/pipelines) | 4169 | Python | Machine Learning Pipelines for Kubeflow |
| [kubeflow/spark-operator](https://github.com/kubeflow/spark-operator) | 3132 | Python | Kubernetes operator for managing the lifecycle of Apache Spa |
| [kubeflow/trainer](https://github.com/kubeflow/trainer) | 2129 | Go | Distributed AI Model Training and LLM Fine-Tuning on Kuberne |
| [kubeflow/katib](https://github.com/kubeflow/katib) | 1689 | Python | Automated Machine Learning on Kubernetes |
| [kubeflow/examples](https://github.com/kubeflow/examples) | 1460 | Jsonnet | A repository to host extended examples and tutorials |
| [kubeflow/community-distribution](https://github.com/kubeflow/community-distribution) | 1028 | YAML | Kubeflow Community Distribution |
| [kubeflow/manifests](https://github.com/kubeflow/manifests) | 1010 | YAML | Kubeflow AI Reference Platform Deployment Manifests |
| [kubeflow/arena](https://github.com/kubeflow/arena) | 814 | Go | A CLI for Kubeflow.  |
| [kubeflow/kale](https://github.com/kubeflow/kale) | 695 | Python | Kubeflow’s superfood for Data Scientists |
| [kubeflow/mpi-operator](https://github.com/kubeflow/mpi-operator) | 529 | Go | Kubernetes Operator for MPI-based applications (distributed  |
| [kubeflow/fairing](https://github.com/kubeflow/fairing) | 337 | Jsonnet | Python SDK for building, training, and deploying ML models |
| [kubeflow/pytorch-operator](https://github.com/kubeflow/pytorch-operator) | 310 | Jsonnet | PyTorch on Kubernetes |
| [kubeflow/community](https://github.com/kubeflow/community) | 194 | Jupyter Notebook | Information about the Kubeflow community including proposals |
| [kubeflow/website](https://github.com/kubeflow/website) | 184 | HTML | Kubeflow Website |

### GF(3) World Increment Chain

| Source | GF3 Color | GF3 Name | Trit | Hash |
|--------|-----------|----------|------|------|
| migalkin | `#cc241d` | MINUS | -1 | `25236d94a378cd6e` |
| plurigrid | `#d3869b` | ERGODIC | 0 | `4f3baa2346d66bf3` |
| kristinezheng | `#d3869b` | ERGODIC | 0 | `575bdf58c288` |
| kristinezheng | `#d3869b` | ERGODIC | 0 | `` |
| wasita | `#b8bb26` | PLUS | 1 | `c016f3b1ab100efe` |
| M1shaaa | `#b8bb26` | PLUS | 1 | `af0122c87aab` |
| M1shaaa | `#b8bb26` | PLUS | 1 | `` |
| zubyul | `#cc241d` | MINUS | -1 | `e240ee4455e86756` |
| AustinCStone | `#cc241d` | MINUS | -1 | `138f69dd62d2` |
| AustinCStone | `#cc241d` | MINUS | -1 | `` |
| bmorphism | `#d3869b` | ERGODIC | 0 | `sweep-2026-04-12` |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 worlds)

- **Total addresses probed:** 28
- **Non-zero balances:** 0
- **Zero/empty (resource_not_found):** 28

> All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<AptosCoin>` — accounts exist but hold no APT on mainnet (ledger v6093393599).

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428a0c007da0f7629...` | 2 | ✓ |
| A-G | `0xf56c4a1c0906214f3f859c...` | 2 | ✓ |
| S-T | `0x3b1c3ae905d44c3a49f0de...` | 2 | ✓ |
| V-W | `0x40fad7b423a843650fddca...` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b2df4062281c7...` | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

> **Status: UNAVAILABLE** — All endpoints (`/`, `/api/markets`, `/api/v1/markets`, `/api`) returned HTTP 401. Site requires Vercel authentication. No market data extracted.

---

## DuckDB Table Summary

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 34 | GF(3) color-coded source sweep events |
| `repo_snapshots` | 1275 | Full repo snapshots with stars/forks/issues |
| `aptos_snapshots` | 28 | 28 Hamming swarm wallet balances (APT) |
| `multisig_probes` | 5 | 5 multisig contract threshold probes |
| `mnx_snapshots` | 1 | MNX market data (unavailable this sweep) |

---
*Sweep completed 2026-07-04 07:11:13 UTC*
