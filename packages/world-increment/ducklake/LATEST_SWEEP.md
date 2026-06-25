# LATEST_SWEEP — 2026-06-25

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted
| Source | Repos Captured | Notable |
|--------|---------------|---------|
| plurigrid | 100 | plurigrid/duck-kanban(1★), plurigrid/nanoclj-zig(1★), plurigrid/Plurigraph(3★),  |
| bmorphism | 100 | bmorphism/manifold-mcp-server(14★), bmorphism/zeldar(1★), bmorphism/graphistry-m |
| zubyul | 49 | zubyul/gay-world(1★), zubyul/cascade-world(1★), zubyul/jonikas_for_weronika.-ann |
| kubeflow | 48 | kubeflow/xgboost-operator(77★), kubeflow/testing(60★), kubeflow/spark-operator(3 |
| migalkin | 19 | migalkin/RWL(8★), migalkin/SMJoin-experiments(1★), migalkin/rambo(3★), migalkin/ |
| wasita | 11 | wasita/wasita.github.io(1★), wasita/magic-garden(2★), wasita/wins-search(1★), wa |
| AustinCStone | 9 | AustinCStone/TextGAN(92★), AustinCStone/StereoVisionMRF(11★), AustinCStone/Spect |
| M1shaaa | 8 |  |
| DJedamski | 6 | DJedamski/Getting-and-Cleaning-Data(1★), DJedamski/Kaggle(1★), DJedamski/School( |
| TeglonLabs | 5 | TeglonLabs/mathpix-gem(2★) |
| kristinezheng | 5 |  |

**Total repos indexed:** 360

### Top Repos by Stars
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15743 | — |
| kubeflow/pipelines | 4157 | Python |
| kubeflow/spark-operator | 3128 | Python |
| kubeflow/trainer | 2121 | Go |
| kubeflow/katib | 1685 | Python |
| kubeflow/examples | 1460 | Jsonnet |
| kubeflow/community-distribution | 1028 | YAML |
| kubeflow/arena | 813 | Go |
| kubeflow/kale | 694 | Python |
| kubeflow/mpi-operator | 528 | Go |
| kubeflow/fairing | 337 | Jsonnet |
| kubeflow/pytorch-operator | 310 | Jsonnet |
| kubeflow/community | 194 | Jupyter Notebook |
| kubeflow/website | 184 | HTML |
| kubeflow/kfp-tekton | 183 | TypeScript |

### GF(3) Color Chain Distribution
| Name | Color | Count |
|------|-------|-------|
| PLUS | `#b8bb26` | 120 |
| MINUS | `#cc241d` | 120 |
| ERGODIC | `#d3869b` | 120 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
- **Addresses probed:** 28
- **Total APT across swarm:** 0.0000 APT
- **Status:** All 28 wallets (alice, bob, A–Z) return 0 balance — CoinStore resource absent, accounts unfunded/inactive on mainnet

### Multisig Contract Probes
| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | `0x0da4f428a0c007da0f…` | 2 | ✓ |
| A-G | `0xf56c4a1c0906214f3f…` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b2df40622…` | 2 | ✓ |
| S-T | `0x3b1c3ae905d44c3a49…` | 2 | ✓ |
| V-W | `0x40fad7b423a843650f…` | 2 | ✓ |

All 5 multisig contracts respond with **2-of-N threshold** — operational.

### MNX Markets (testnet.mnx.fi)
- **Status:** Unavailable — Vercel deployment protection active (auth required)
- Market data could not be extracted from SPA

---

## DuckDB Ducklake Schema
Location: `packages/world-increment/ducklake/world-increments.duckdb`

Tables:
- `world_increments` — GF(3) color-chained event log
- `repo_snapshots` — GitHub repo metadata
- `aptos_snapshots` — Hamming swarm wallet balances
- `multisig_probes` — Multisig threshold probes
- `mnx_snapshots` — MNX market data (unavailable this sweep)

GF(3) trit key: `0=ERGODIC #d3869b` · `1=PLUS #b8bb26` · `-1=MINUS #cc241d`
