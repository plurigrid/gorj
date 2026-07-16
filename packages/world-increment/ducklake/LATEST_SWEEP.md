# World-Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-07-16 08:12 UTC  
**Sweep Date:** 2026-07-16  

---

## JOB 1: GitHub Social Graph Sweep

### Coverage
| Source | Repos Snapshotted |
|--------|------------------|
| bmorphism | 50 (115 ⭐ total) |
| plurigrid | 50 (57 ⭐ total) |
| zubyul | 49 (14 ⭐ total) |
| kubeflow | 49 (34372 ⭐ total) |
| migalkin | 5 (275 ⭐ total) |
| TeglonLabs | 5 (2 ⭐ total) |
| wasita | 4 (4 ⭐ total) |
| AustinCStone | 3 (103 ⭐ total) |
| M1shaaa | 2 (0 ⭐ total) |
| kristinezheng | 2 (0 ⭐ total) |
| DJedamski | 2 (1 ⭐ total) |

**Total repos this sweep:** 15 unique (221 new increments inserted)  
**Cumulative DB:** 244 world_increments, 1165 repo_snapshots  

### Top Repos by Stars (This Sweep)
| Org/User | Repo | Stars | Language |
|----------|------|-------|----------|
| kubeflow | kubeflow | 15778 | - |
| kubeflow | pipelines | 4167 | Python |
| kubeflow | spark-operator | 3137 | Python |
| kubeflow | trainer | 2150 | Go |
| kubeflow | katib | 1690 | Python |
| kubeflow | examples | 1460 | Jsonnet |
| kubeflow | community-distribution | 1029 | YAML |
| kubeflow | arena | 815 | Go |
| kubeflow | kale | 696 | Python |
| kubeflow | mpi-operator | 530 | Go |
| kubeflow | fairing | 337 | Jsonnet |
| kubeflow | pytorch-operator | 310 | Jsonnet |
| kubeflow | community | 195 | Jupyter Notebook |
| kubeflow | website | 184 | HTML |
| kubeflow | kfp-tekton | 183 | TypeScript |

### GF(3) Color Chain Distribution
| GF3 Name | Color | Count |
|----------|-------|-------|
| ERGODIC | `#d3869b` | 80 |
| MINUS | `#cc241d` | 82 |
| PLUS | `#b8bb26` | 82 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

**All 28 addresses (alice, bob, A–Z) returned 0.000000 APT.**  
Both `CoinStore<AptosCoin>` (v1) and `primary_fungible_store::balance` (v2) returned zero.  
These addresses are likely inactive or on testnet allocation only.

### Multisig Contract Probes
| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428a0c007da0f...` | 2 | ✓ YES |
| A-G | `0xf56c4a1c0906214f3f...` | 2 | ✓ YES |
| Y-Z | `0xd3ffe1812b2df40622...` | 2 | ✓ YES |
| S-T | `0x3b1c3ae905d44c3a49...` | 2 | ✓ YES |
| V-W | `0x40fad7b423a843650f...` | 2 | ✓ YES |

**All 5 multisig pairs report `num_signatures_required = 2`. All healthy.**

### MNX Markets (testnet.mnx.fi)
Status: **Authentication Required** (Vercel SSO gate). No market data extractable without credentials.

---

## DuckDB Schema
```
world-increments.duckdb
  ├── world_increments  (cumulative GF3-colored increment log)
  ├── repo_snapshots    (full repo metadata per sweep)
  ├── aptos_snapshots   (Hamming swarm wallet balances)
  ├── multisig_probes   (multisig sigs-required checks)
  └── mnx_snapshots     (market data; placeholder this sweep)
```
