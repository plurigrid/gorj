# LATEST_SWEEP.md — World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-08-04 07:21 UTC  
**GF(3) color chain:** ERGODIC #d3869b / PLUS #b8bb26 / MINUS #cc241d  
**Total world increments logged:** 24

---

## JOB 1: GitHub Social Graph Sweep

### Summary
- **Total repo snapshots:** 1318 (cumulative across all sweeps)
- **Sources queried:** plurigrid, kubeflow, TeglonLabs, bmorphism, zubyul + social graph (migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone)

### Repos by Owner (cumulative)
| Owner | Count |
|-------|-------|
| plurigrid | 300 |
| bmorphism | 300 |
| kubeflow | 143 |
| TeglonLabs | 111 |
| AustinCStone | 106 |
| zubyul | 97 |
| migalkin | 79 |
| wasita | 73 |
| kristinezheng | 41 |
| M1shaaa | 40 |
| DJedamski | 28 |

### Top Repos by Stars
| Org/User | Repo | Stars |
|----------|------|-------|
| kubeflow | kubeflow | 15805 |
| kubeflow | kubeflow | 15572 |
| kubeflow | kubeflow | 15565 |
| kubeflow | pipelines | 4175 |
| kubeflow | pipelines | 4119 |
| kubeflow | pipelines | 4119 |
| kubeflow | spark-operator | 3143 |
| kubeflow | spark-operator | 3114 |
| kubeflow | spark-operator | 3111 |
| kubeflow | trainer | 2166 |
| kubeflow | trainer | 2082 |
| kubeflow | trainer | 2080 |
| kubeflow | katib | 1694 |
| kubeflow | katib | 1678 |
| kubeflow | katib | 1676 |

### Notable Findings
- **kubeflow/kubeflow**: 15,805 ⭐ — flagship ML toolkit for Kubernetes
- **kubeflow/pipelines**: 4,175 ⭐ — ML pipeline orchestration
- **kubeflow/spark-operator**: 3,143 ⭐ — Spark on Kubernetes
- **plurigrid/asi**: 58 ⭐ — topological chemputer (most starred plurigrid)
- **migalkin/NodePiece**: 144 ⭐ — knowledge graph representations (ICLR'22)
- **migalkin/StarE**: 89 ⭐ — hyper-relational KG message passing (EMNLP 2020)
- **AustinCStone/TextGAN**: 92 ⭐ — text GAN in TensorFlow

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances
| World | Address | Balance (APT) |
|-------|---------|---------------|
| Z | 0x7af0ef6e1bd706... | 0.00000000 |
| Y | 0xd8e32848f1dffa... | 0.00000000 |
| X | 0xa95cbbd116548a... | 0.00000000 |
| W | 0x5f32aef70f5ba5... | 0.00000000 |
| V | 0xb59dd8170321df... | 0.00000000 |
| U | 0x75860da47565f6... | 0.00000000 |
| T | 0x35781dc0e42fef... | 0.00000000 |
| S | 0xb8753014e4888e... | 0.00000000 |
| R | 0x7ce605cc8fda4f... | 0.00000000 |
| Q | 0xac40fa50b81b4c... | 0.00000000 |
| P | 0x6218792de4a9bc... | 0.00000000 |
| O | 0x73252b6011a751... | 0.00000000 |
| N | 0xe7dde6da0a65f5... | 0.00000000 |
| M | 0x6fed37a7553ef1... | 0.00000000 |
| L | 0x7c2eaeafad9725... | 0.00000000 |
| K | 0xa732040a6b0d55... | 0.00000000 |
| J | 0x4d964db8f53837... | 0.00000000 |
| I | 0x070fe5d74e4eda... | 0.00000000 |
| H | 0xce67c327a7844e... | 0.00000000 |
| G | 0x69a394c0b0ac84... | 0.00000000 |
| F | 0x18a14b5b4bec11... | 0.00000000 |
| E | 0xdc1d9d533bac35... | 0.00000000 |
| D | 0xf77656248f64d5... | 0.00000000 |
| C | 0x38b99e63ada9b6... | 0.00000000 |
| B | 0x3f892ebe6e4516... | 0.00000000 |
| A | 0x8699edc0960dd5... | 0.00000000 |
| bob | 0x0a3c00c58fdf90... | 0.00000000 |
| alice | 0xc793acdec12b4a... | 0.00000000 |

**Note:** All 28 wallets returned 0 APT via standard CoinStore resource. Wallets may hold APT via different account/resource types or may be unfunded.

### Multisig Probes (5 pairs)
| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| V-W | 0x40fad7b423a843... | 2 | ✅ |
| S-T | 0x3b1c3ae905d44c... | 2 | ✅ |
| Y-Z | 0xd3ffe1812b2df4... | 2 | ✅ |
| A-G | 0xf56c4a1c090621... | 2 | ✅ |
| A-B | 0x0da4f428a0c007... | 2 | ✅ |

**All 5 multisig contracts healthy** — each requires 2 signatures.
- A-B: 0x0da4f428...
- A-G: 0xf56c4a1c...
- Y-Z: 0xd3ffe181...
- S-T: 0x3b1c3ae9...
- V-W: 0x40fad7b4...

### MNX Markets
- **Status:** Unavailable — testnet.mnx.fi returns only "MNX" text (JavaScript SPA, no server-side data)

---

## DuckDB Ducklake Schema

**Location:** `packages/world-increment/ducklake/world-increments.duckdb`

Tables:
- `world_increments` — GF(3) sweep events
- `repo_snapshots` — GitHub repo metadata snapshots
- `aptos_snapshots` — Hamming swarm wallet balances
- `multisig_probes` — Multisig contract health checks
- `mnx_snapshots` — MNX market data (currently empty)
