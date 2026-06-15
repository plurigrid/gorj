# LATEST_SWEEP.md — World-Increment + Hamming Swarm Snapshot

**Generated:** 2026-06-15 21:12:50 UTC  
**Run date:** 2026-06-15

---

## JOB 1: GitHub Social Graph Sweep

### Summary
| Metric | Value |
|--------|-------|
| World increments recorded | 363 |
| Repo snapshots | 1284 |
| Total stars across graph | 103,842 |
| Sources swept | 11 |

### GF(3) Color Chain Distribution
| GF(3) Name | Trit | Color | Count |
|-----------|------|-------|-------|
| ERGODIC | 0 | `#d3869b` | 121 |
| MINUS | -1 | `#cc241d` | 121 |
| PLUS | 1 | `#b8bb26` | 121 |

### Repos by Source
| Source | Type | Repos | Stars |
|--------|------|-------|-------|
| plurigrid | org | 501 | 263 |
| bmorphism | user | 500 | 771 |
| kubeflow | org | 236 | 169,660 |
| TeglonLabs | org | 217 | 26 |
| AustinCStone | user | 182 | 540 |
| zubyul | user | 145 | 66 |
| migalkin | user | 127 | 1,388 |
| wasita | user | 127 | 17 |
| kristinezheng | user | 77 | 0 |
| M1shaaa | user | 69 | 0 |
| DJedamski | user | 48 | 30 |

### Top 15 Repos by Stars
| Repo | Language | Stars | Forks | Description |
|------|----------|-------|-------|-------------|
| kubeflow/kubeflow | - | 15726 | 2673 | Machine Learning Toolkit for Kubernetes |
| kubeflow/kubeflow | - | 15572 | 2633 | Machine Learning Toolkit for Kubernetes |
| kubeflow/kubeflow | - | 15565 | 2626 | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | Python | 4154 | 2008 | Machine Learning Pipelines for Kubeflow |
| kubeflow/pipelines | Python | 4119 | 1984 | Machine Learning Pipelines for Kubeflow |
| kubeflow/pipelines | Python | 4119 | 1985 | Machine Learning Pipelines for Kubeflow |
| kubeflow/spark-operator | Python | 3127 | 1490 | Kubernetes operator for managing the lifecycle of Apache Spa |
| kubeflow/spark-operator | Python | 3114 | 1483 | Kubernetes operator for managing the lifecycle of Apache Spa |
| kubeflow/spark-operator | Python | 3111 | 1483 | Kubernetes operator for managing the lifecycle of Apache Spa |
| kubeflow/trainer | Go | 2115 | 969 | Distributed AI Model Training and LLM Fine-Tuning on Kuberne |
| kubeflow/trainer | Go | 2082 | 945 | Distributed AI Model Training and LLM Fine-Tuning on Kuberne |
| kubeflow/trainer | Go | 2080 | 944 | Distributed AI Model Training and LLM Fine-Tuning on Kuberne |
| kubeflow/katib | Python | 1683 | 527 | Automated Machine Learning on Kubernetes |
| kubeflow/katib | Python | 1678 | 521 | Automated Machine Learning on Kubernetes |
| kubeflow/katib | Python | 1676 | 521 | Automated Machine Learning on Kubernetes |

### Top Languages
| Language | Repo Count |
|----------|------------|
| Python | 218 |
| Rust | 57 |
| Go | 51 |
| JavaScript | 49 |
| HTML | 49 |
| TypeScript | 47 |
| Jupyter Notebook | 39 |
| Clojure | 30 |
| Jsonnet | 23 |
| R | 20 |

### Social Graph Coverage
- **Orgs:** plurigrid, kubeflow, TeglonLabs
- **Users (core):** bmorphism, zubyul
- **Zubyul social graph:** migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances
- **Queried:** 28 addresses (Alice, Bob, A-Z)
- **Result:** 28/28 wallets have no CoinStore resource (unfunded on mainnet)

All 28 Hamming-swarm addresses queried via the Aptos fullnode mainnet API returned missing coin data.
These addresses exist on-chain but hold zero APT and have no registered CoinStore.

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428...987003` | 2 | yes |
| A-G | `0xf56c4a1c...bc0096` | 2 | yes |
| Y-Z | `0xd3ffe181...75b883` | 2 | yes |
| S-T | `0x3b1c3ae9...ed7883` | 2 | yes |
| V-W | `0x40fad7b4...80eb6d` | 2 | yes |

All 5 multisig contracts responded with `sigs_required=2`. All are healthy.

### MNX Markets (testnet.mnx.fi)
**Status:** UNAVAILABLE — Vercel deployment-protection auth-gates all endpoints.
No market data could be extracted. `mnx_snapshots` table is empty this sweep.

---

## DuckDB Tables
| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 363 | GF(3)-colored increment log per repo event |
| `repo_snapshots` | 1284 | GitHub repo metadata (name, stars, forks, language) |
| `aptos_snapshots` | 28 | Hamming swarm wallet APT balances |
| `multisig_probes` | 5 | Aptos multisig sig-threshold probes |
| `mnx_snapshots` | 0 | MNX market data (empty — auth-gated this run) |

**DB path:** `packages/world-increment/ducklake/world-increments.duckdb`
