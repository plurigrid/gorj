# World-Increment Sweep + Hamming Snapshot

**Date:** 2026-07-08  
**GF(3) Color Chain:** ERGODIC #d3869b | PLUS #b8bb26 | MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Found |
|--------|------|-------------|
| plurigrid | org | 103 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 105 |
| zubyul | user | 49 |
| migalkin | social graph | 19 |
| DJedamski | social graph | 6 |
| wasita | social graph | 11 |
| kristinezheng | social graph | 5 |
| M1shaaa | social graph | 8 |
| AustinCStone | social graph | 40 |

**Total:** ~400 repos across social graph

### Notable Repos (Top Stars)

| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,769 | — | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4,170 | Python | ML Pipelines for Kubeflow |
| kubeflow/spark-operator | 3,133 | Python | Kubernetes operator for Apache Spark |
| kubeflow/trainer | 2,130 | Go | Distributed AI Training + LLM Fine-Tuning |
| kubeflow/katib | 1,690 | Python | Automated ML on Kubernetes |
| AustinCStone/TextGAN | 92 | Python | GAN for text generation in TensorFlow |
| migalkin/NodePiece | 144 | Python | Parameter-Efficient KG Representations (ICLR'22) |
| plurigrid/asi | 30 | HTML | everything is topological chemputer! |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | OCaml SDK for Model Context Protocol |

### Most Active (Recent Push)

| Repo | Last Push |
|------|-----------|
| kubeflow/pipelines | 2026-07-08T02:46:48Z |
| plurigrid/gorj | 2026-07-08T02:12:56Z |
| bmorphism/Gay.jl | 2026-07-08T00:29:55Z |
| kubeflow/trainer | 2026-07-08T00:12:32Z |
| kubeflow/website | 2026-07-07T19:56:24Z |

### GF(3) World-Increment Distribution (this sweep)

| Name | Trit | Color | Count |
|------|------|-------|-------|
| ERGODIC | 0 | #d3869b | 25 |
| PLUS | +1 | #b8bb26 | 26 |
| MINUS | -1 | #cc241d | 26 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A–Z) queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result:** All wallets returned **0.0 APT** — CoinStore resource not registered on mainnet (addresses may hold FA tokens or be unfunded).

| World | Address | APT Balance |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D–Z | (24 more) | 0.0 each |

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

All 5 multisig contracts healthy: **2-of-2 signatures required**.

### MNX Markets

`https://testnet.mnx.fi` — **UNAVAILABLE** (Vercel deployment protection requires visitor password authentication; no market data could be extracted).

---

## DuckDB Summary

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows (cumulative) |
|-------|-------------------|
| world_increments | 77 |
| repo_snapshots | 998 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

---

*Sweep generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent on 2026-07-08.*
