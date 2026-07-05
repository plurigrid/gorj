# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-05  
**Run:** world-increment-sweep + hamming-swarm-snapshot agent  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 (103 total, GitHub page limit) |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 105 |
| zubyul | user | 49 |
| migalkin | user (social) | 19 |
| wasita | user (social) | 11 |
| kristinezheng | user (social) | 5 |
| M1shaaa | user (social) | 8 |
| AustinCStone | user (social) | 40 |
| DJedamski | user (social) | 6 |

**Total unique repos in ducklake:** 497  
**World increments this run:** 109  

### Top Repos by Stars

| Repo | Stars | Forks | Language |
|------|-------|-------|----------|
| kubeflow/kubeflow | 15,762 | 2,683 | — |
| kubeflow/pipelines | 4,169 | 2,023 | Python |
| kubeflow/spark-operator | 3,132 | 1,496 | Python |
| kubeflow/trainer | 2,129 | 978 | Go |
| kubeflow/katib | 1,689 | 530 | Python |
| kubeflow/examples | 1,460 | 756 | Jsonnet |
| kubeflow/community-distribution | 1,028 | 1,067 | YAML |
| migalkin/NodePiece | 144 | 21 | Python |
| AustinCStone/TextGAN | 92 | 30 | Python |
| migalkin/StarE | 89 | 16 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | 2 | OCaml |
| plurigrid/asi | 28 | 8 | HTML |

### Notable Repos

- **plurigrid/gorj** (this repo): 982 open issues, pushed 2026-07-05 — very active
- **plurigrid/eirobri**: 30 open issues, EiRoBri replay world
- **kubeflow/docs-agent**: 155 open issues, AI-powered docs agent
- **bmorphism/Gay.jl**: 187 open issues, wide-gamut color sampling with GF(3)
- **TeglonLabs/jank-crane**: crane-jank converged-IR hub with GF(3) convergence maps
- **zubyul/tilelang-kernels**: TileLang GPU kernels for GF(3) trit classification

### GF(3) Color Chain Distribution (world_increments)

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 35 |
| 1 | PLUS | #b8bb26 | 37 |
| -1 | MINUS | #cc241d | 37 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A-Z)

**Status:** All 28 addresses returned `no_account` — no CoinStore resource on Aptos mainnet. These Hamming swarm wallets are not yet initialized on mainnet (likely test addresses).

| World | Status | Balance (APT) |
|-------|--------|--------------|
| alice-Z (all 28) | no_account | 0.0 |

### Multisig Contract Probes

All 5 multisig contracts are **healthy** and require **2-of-2 signatures**:

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | healthy |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | healthy |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | healthy |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | healthy |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

**Status:** All endpoints return `Authentication Required` (SPA gated behind login). No market data extractable without credentials. Recorded as unavailable in `mnx_snapshots` (0 rows).

---

## DuckDB Schema Summary

| Table | Rows |
|-------|------|
| world_increments | 109 (this run) |
| repo_snapshots | 497 unique repos (cumulative) |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (auth required) |
