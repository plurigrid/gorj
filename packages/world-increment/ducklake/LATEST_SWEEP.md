# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-10  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 25 |
| TeglonLabs | org | 5 |
| kubeflow | org | 15 |
| bmorphism | user | 15 |
| zubyul | user | 10 |
| migalkin | user (social) | 5 |
| DJedamski | user (social) | 4 |
| wasita | user (social) | 5 |
| kristinezheng | user (social) | 4 |
| M1shaaa | user (social) | 3 |
| AustinCStone | user (social) | 5 |
| **Total** | | **96** |

### Notable Repos

| Repo | Stars | Lang | Description |
|------|-------|------|-------------|
| kubeflow/kubeflow | 15,714 | — | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4,153 | Python | ML Pipelines |
| kubeflow/spark-operator | 3,126 | Python | Kubernetes operator for Apache Spark |
| kubeflow/trainer | 2,112 | Go | Distributed AI Model Training & LLM Fine-Tuning |
| kubeflow/katib | 1,685 | Python | Automated ML on Kubernetes |
| kubeflow/examples | 1,462 | Jsonnet | Extended examples and tutorials |
| AustinCStone/TextGAN | 92 | Python | GAN for text generation in TensorFlow |
| migalkin/NodePiece | 144 | Python | Compositional Representations for Knowledge Graphs (ICLR'22) |
| migalkin/StarE | 89 | Python | Message Passing for Hyper-Relational KGs (EMNLP'20) |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | OCaml SDK for Model Context Protocol |
| plurigrid/asi | 25 | HTML | everything is topological chemputer! |
| plurigrid/gorj | 0 | Clojure | **480 open issues** — forj + Rama topology + GF(3) |
| bmorphism/Gay.jl | 1 | Julia | **189 open issues** — Wide-gamut splittable color sampling |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 32 |
| 1 | `#b8bb26` | PLUS | 32 |
| -1 | `#cc241d` | MINUS | 32 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

All 28 addresses (alice, bob, A–Z) queried against `fullnode.mainnet.aptoslabs.com`.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...3cf71 | 0.0 |
| G | 0x69a3...c7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...d386 | 0.0 |
| T | 0x3578...f4588 | 0.0 |
| U | 0x7586...f9956 | 0.0 |
| V | 0xb59d...af2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...444c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

> All wallets returned 0.0 APT — addresses appear unfunded on mainnet (CoinStore resource absent for these accounts).

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All 5 multisig contracts are live and require 2-of-N signatures. **All healthy.**

### MNX Markets (testnet.mnx.fi)

Status: **UNAVAILABLE** — endpoint protected by Vercel deployment authentication. The SPA returns an auth challenge. No market data extractable without a Vercel bypass token or Trusted Sources OIDC config.

---

## DuckDB Schema Summary

```
world_increments   96 rows  — GF(3) trit-colored increment log
repo_snapshots     96 rows  — GitHub repo metadata
aptos_snapshots    28 rows  — Hamming swarm wallet balances
multisig_probes     5 rows  — Multisig health probes
mnx_snapshots       0 rows  — MNX markets (unavailable)
```

**GF(3) color chain:** id%3==0 → trit=0 ERGODIC `#d3869b` | id%3==1 → trit=1 PLUS `#b8bb26` | id%3==2 → trit=-1 MINUS `#cc241d`
