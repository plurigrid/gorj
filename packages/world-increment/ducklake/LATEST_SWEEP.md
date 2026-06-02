# LATEST_SWEEP

**Timestamp:** 2026-06-02 03:14:25 UTC  
**Run:** world-increment-sweep + hamming-swarm-snapshot

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept
| Source | Type | Repos | Stars | Latest Push |
|--------|------|-------|-------|-------------|
| bmorphism | user | 100 | 247 | 2026-06-02 |
| plurigrid | org | 100 | 75 | 2026-06-02 |
| zubyul | user | 49 | 14 | 2026-04-24 |
| kubeflow | org | 48 | 34167 | 2026-06-01 |
| AustinCStone | user | 40 | 108 | 2026-02-11 |
| migalkin | user | 19 | 280 | 2025-08-04 |
| wasita | user | 11 | 5 | 2026-06-01 |
| M1shaaa | user | 8 | 0 | 2026-06-01 |
| kristinezheng | user | 6 | 0 | 2026-05-14 |
| DJedamski | user | 6 | 3 | 2018-03-07 |
| TeglonLabs | org | 4 | 2 | 2026-01-01 |

**Total repos captured:** 391  
**Total stars across all repos:** 34901

### GF(3) Color Chain
| Name | Color | Count |
|------|-------|-------|
| PLUS | `#b8bb26` | 4 |
| MINUS | `#cc241d` | 4 |
| ERGODIC | `#d3869b` | 3 |

### Top Repos by Stars
| Repo | Stars | Language | Last Push | Description |
|------|-------|----------|-----------|-------------|
| kubeflow/kubeflow | 15700 | N/A | 2026-05-24 | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4151 | Python | 2026-06-01 | Machine Learning Pipelines for Kubeflow |
| kubeflow/spark-operator | 3125 | Python | 2026-06-01 | Kubernetes operator for managing the lifecycle of Apache Spa |
| kubeflow/trainer | 2109 | Go | 2026-05-30 | Distributed AI Model Training and LLM Fine-Tuning on Kuberne |
| kubeflow/katib | 1685 | Python | 2026-05-29 | Automated Machine Learning on Kubernetes |
| kubeflow/examples | 1462 | Jsonnet | 2025-04-14 | A repository to host extended examples and tutorials |
| kubeflow/manifests | 1020 | YAML | 2026-05-29 | Kubeflow AI Reference Platform Deployment Manifests |
| kubeflow/arena | 811 | Go | 2026-05-07 | A CLI for Kubeflow.  |
| kubeflow/kale | 691 | Python | 2026-06-01 | Kubeflow’s superfood for Data Scientists |
| kubeflow/mpi-operator | 528 | Go | 2026-05-29 | Kubernetes Operator for MPI-based applications (distributed  |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
**Query method:** `0x1::coin::balance` view function  
**Total APT across swarm:** 20.34477 APT

| World | Address (short) | Balance (APT) |
|-------|-----------------|----------------|
| bob | `0x0a3c00...512d5d` | 12.65701 |
| F | `0x18a14b...c3cf71` | 1.96052 |
| L | `0x7c2eae...37eba9` | 1.92727 |
| J | `0x4d964d...e87f54` | 1.89509 |
| alice | `0xc793ac...24cc7b` | 0.43643 |
| O | `0x73252b...25a89d` | 0.21014 |
| K | `0xa73204...425dc4` | 0.16196 |
| P | `0x621879...1ec948` | 0.14014 |
| M | `0x6fed37...b7f2e9` | 0.11228 |
| N | `0xe7dde6...551b2c` | 0.10612 |
| Q | `0xac40fa...5c89a9` | 0.10324 |
| S | `0xb87530...9d0386` | 0.09179 |
| R | `0x7ce605...d76e10` | 0.09022 |
| T | `0x35781d...3f4588` | 0.07371 |
| U | `0x75860d...ef9956` | 0.05577 |
| A | `0x8699ed...be9d7a` | 0.05177 |
| V | `0xb59dd8...9af2c3` | 0.04883 |
| Y | `0xd8e328...2444c4` | 0.04445 |
| X | `0xa95cbb...33047d` | 0.04258 |
| W | `0x5f32ae...ccc7b0` | 0.04070 |
| B | `0x3f892e...77cb13` | 0.03626 |
| Z | `0x7af0ef...4e197c` | 0.02427 |
| D | `0xf77656...fcfdd1` | 0.01163 |
| C | `0x38b99e...91535e` | 0.01018 |
| E | `0xdc1d9d...958d36` | 0.00937 |
| H | `0xce67c3...e5300f` | 0.00168 |
| I | `0x070fe5...0c1fc9` | 0.00068 |
| G | `0x69a394...cc7f32` | 0.00068 |

### Multisig Contract Probes
All probes use `0x1::multisig_account::num_signatures_required`

| Pair | Address (short) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | `0x0da4f428...` | 2 | ✓ HEALTHY |
| A-G | `0xf56c4a1c...` | 2 | ✓ HEALTHY |
| Y-Z | `0xd3ffe181...` | 2 | ✓ HEALTHY |
| S-T | `0x3b1c3ae9...` | 2 | ✓ HEALTHY |
| V-W | `0x40fad7b4...` | 2 | ✓ HEALTHY |

**All 5 multisig contracts require 2 signatures — all healthy.**

### MNX Markets (testnet.mnx.fi)
Status: **UNAVAILABLE** — endpoint serves a Next.js SPA with no accessible REST API.  
No market data could be extracted at this time.

---

## DuckDB Schema (ducklake)
- `world_increments` — GF(3) trit-colored sweep events
- `repo_snapshots` — Full GitHub repo metadata  
- `aptos_snapshots` — Hamming swarm wallet balances
- `multisig_probes` — Multisig account health checks
- `mnx_snapshots` — MNX market snapshots (unavailable this run)

**Database:** `packages/world-increment/ducklake/world-increments.duckdb`
