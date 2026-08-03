# World Increment + Hamming Swarm Snapshot
**Generated:** 2026-08-03 14:11:55 UTC  
**GF(3) Color Chain:** ERGODIC #d3869b | PLUS #b8bb26 | MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Summary
- **Total repositories indexed:** 394
- **Sources:** plurigrid (org), kubeflow (org), TeglonLabs (org), bmorphism (user), zubyul (user)
- **Social graph:** migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone

### Repository Counts by Source
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | user | 41 |
| migalkin | user | 19 |
| wasita | user | 12 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| kristinezheng | user | 5 |
| TeglonLabs | org | 5 |

### GF(3) Color Distribution
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 131 |
| 1 | #b8bb26 | PLUS | 132 |
| -1 | #cc241d | MINUS | 131 |

### Top Languages
- **Python**: 79 repos
- **Rust**: 26 repos
- **JavaScript**: 25 repos
- **TypeScript**: 22 repos
- **HTML**: 18 repos
- **Go**: 15 repos
- **Clojure**: 14 repos
- **Jupyter Notebook**: 14 repos
- **Julia**: 9 repos
- **Zig**: 7 repos

### Most Recently Pushed
| Repo | Source | Pushed At | Stars |
|------|--------|-----------|-------|
| plurigrid/gorj | plurigrid | 2026-08-03 | 1 |
| kubeflow/mpi-operator | kubeflow | 2026-08-03 | 530 |
| kubeflow/hub | kubeflow | 2026-08-03 | 180 |
| kubeflow/community-distribution | kubeflow | 2026-08-03 | 1029 |
| kubeflow/mcp-server | kubeflow | 2026-08-03 | 31 |
| kubeflow/pipelines | kubeflow | 2026-08-03 | 4173 |
| bmorphism/Gay.jl | bmorphism | 2026-08-03 | 2 |
| M1shaaa/M1shaaa | M1shaaa | 2026-08-03 | 0 |
| kubeflow/internal-acls | kubeflow | 2026-08-03 | 19 |
| kubeflow/notebooks | kubeflow | 2026-08-02 | 73 |

### Top Starred Repos
| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15805 |  | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4173 | Python | Machine Learning Pipelines for Kubeflow |
| kubeflow/spark-operator | 3143 | Python | Kubernetes operator for managing the lifecycle of Apache Spa |
| kubeflow/trainer | 2165 | Go | Distributed AI Model Training and LLM Fine-Tuning on Kuberne |
| kubeflow/katib | 1694 | Python | Automated Machine Learning on Kubernetes |
| kubeflow/examples | 1461 | Jsonnet | A repository to host extended examples and tutorials |
| kubeflow/community-distribution | 1029 | YAML | Kubeflow Community Distribution |
| kubeflow/arena | 816 | Go | A CLI for Kubeflow.  |
| kubeflow/kale | 699 | Python | Kubeflow’s superfood for Data Scientists |
| kubeflow/mpi-operator | 530 | Go | Kubernetes Operator for MPI-based applications (distributed  |
| kubeflow/fairing | 337 | Jsonnet | Python SDK for building, training, and deploying ML models |
| kubeflow/pytorch-operator | 311 | Jsonnet | PyTorch on Kubernetes |
| kubeflow/community | 195 | Jupyter Notebook | Information about the Kubeflow community including proposals |
| kubeflow/website | 185 | HTML | Kubeflow Website |
| kubeflow/mcp-apache-spark-history-server | 185 | Python | MCP Server and CLI for Apache Spark History Server. Debug Sp |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
- **Wallets queried:** 28
- **Funded wallets:** 0
- **Empty/unfunded wallets:** 28 (CoinStore resource not initialized)

> All 28 Hamming swarm addresses returned `Resource not found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at Ledger version ~6592878122–6592886468. These accounts exist on-chain but have not initialized an APT coin store (likely new accounts or using FA balance instead).

### Multisig Contract Probes
| Pair | Address (short) | Sigs Required | Healthy |
|------|----------------|---------------|---------|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

**Result:** All 5 multisig contracts probed successfully — each requires **2 signatures**.

### MNX Markets (testnet.mnx.fi)
- **Status:** SPA (Next.js) — no public REST API found at `/api/markets` or `/api/v1/markets`
- The frontend returns a full Next.js HTML bundle; market data is loaded client-side via internal RPC
- **Verdict:** Unavailable via headless curl; recorded as `unavailable` in `mnx_snapshots` table

---

## DuckDB Schema (ducklake/world-increments.duckdb)
| Table | Rows (this run) |
|-------|-----------------|
| world_increments | 394 |
| repo_snapshots | 394 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

---
*Sweep by world-increment-sweep + hamming-swarm-snapshot agent*
