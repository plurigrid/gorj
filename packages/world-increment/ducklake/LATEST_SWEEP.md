# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-04-01  
**Branch:** world-increment/sweep-2026-04-01  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| # | Source | Type | Repos | GF3 Trit | Color |
|---|--------|------|-------|----------|-------|
| 1 | plurigrid | org | 50 | +1 PLUS | #b8bb26 |
| 2 | kubeflow | org | 17 | -1 MINUS | #cc241d |
| 3 | TeglonLabs | org | 3 | 0 ERGODIC | #d3869b |
| 4 | bmorphism | user | 20 | +1 PLUS | #b8bb26 |
| 5 | zubyul | user | 20 | -1 MINUS | #cc241d |
| 6 | migalkin | social | 19 | 0 ERGODIC | #d3869b |
| 7 | DJedamski | social | 6 | +1 PLUS | #b8bb26 |
| 8 | wasita | social | 9 | -1 MINUS | #cc241d |
| 9 | kristinezheng | social | 6 | 0 ERGODIC | #d3869b |
| 10 | M1shaaa | social | 8 | +1 PLUS | #b8bb26 |
| 11 | AustinCStone | social | 20 | -1 MINUS | #cc241d |

**Total:** 11 sources, 130 repos captured

### Notable Repos (by stars)

| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,549 | — | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4,117 | Python | Machine Learning Pipelines for Kubeflow |
| kubeflow/spark-operator | 3,110 | Python | Kubernetes operator for Apache Spark |
| kubeflow/trainer | 2,070 | Go | Distributed AI Model Training on Kubernetes |
| kubeflow/katib | 1,674 | Python | Automated Machine Learning on Kubernetes |
| kubeflow/manifests | 1,006 | YAML | Kubeflow AI Reference Platform |
| kubeflow/arena | 809 | Go | A CLI for Kubeflow |
| kubeflow/kale | 681 | Python | Kubeflow's superfood for Data Scientists |
| kubeflow/mpi-operator | 519 | Go | Kubernetes Operator for MPI |
| AustinCStone/TextGAN | 92 | Python | GAN for text generation in TensorFlow |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml | OCaml SDK for Model Context Protocol |
| plurigrid/asi | 14 | HTML | everything is topological chemputer! |

### plurigrid Highlights (as of 2026-04-01)

- **gorj** (Clojure, 55 open issues) — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **zig-syrup** (Zig, ★2) — High-performance OCapN Syrup with CapTP optimizations
- **asi** (HTML, ★14) — everything is topological chemputer!
- **gatomic** (Clojure) — Deterministic color identity store with sonification
- **graded-optic** (Haskell) — Semiring-graded bidirectional processes

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

Queried via `https://fullnode.mainnet.aptoslabs.com` · `0x1::coin::CoinStore<AptosCoin>`

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.00000000 |
| bob | 0x0a3c...512d | 0.00000000 |
| A | 0x8699...9d7a | 0.00000000 |
| B | 0x3f89...b13 | 0.00000000 |
| C | 0x38b9...35e | 0.00000000 |
| D | 0xf776...dd1 | 0.00000000 |
| E | 0xdc1d...d36 | 0.00000000 |
| F | 0x18a1...f71 | 0.00000000 |
| G | 0x69a3...f32 | 0.00000000 |
| H | 0xce67...00f | 0.00000000 |
| I | 0x070f...fc9 | 0.00000000 |
| J | 0x4d96...f54 | 0.00000000 |
| K | 0xa732...dc4 | 0.00000000 |
| L | 0x7c2e...ba9 | 0.00000000 |
| M | 0x6fed...e9 | 0.00000000 |
| N | 0xe7dd...b2c | 0.00000000 |
| O | 0x7325...89d | 0.00000000 |
| P | 0x6218...948 | 0.00000000 |
| Q | 0xac40...9a9 | 0.00000000 |
| R | 0x7ce6...e10 | 0.00000000 |
| S | 0xb875...386 | 0.00000000 |
| T | 0x3578...588 | 0.00000000 |
| U | 0x7586...956 | 0.00000000 |
| V | 0xb59d...b3 | 0.00000000 |
| W | 0x5f32...7b0 | 0.00000000 |
| X | 0xa95c...47d | 0.00000000 |
| Y | 0xd8e3...c4 | 0.00000000 |
| Z | 0x7af0...97c | 0.00000000 |

> All 28 wallets return 0 APT — accounts may not hold the CoinStore resource or have zero balance.

### Multisig Contract Probes

`0x1::multisig_account::num_signatures_required`

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | YES |
| A-G | 0xf56c...096 | 2 | YES |
| Y-Z | 0xd3ff...883 | 2 | YES |
| S-T | 0x3b1c...883 | 2 | YES |
| V-W | 0x40fa...b6d | 2 | YES |

All 5 multisig contracts healthy — 2-of-N threshold configured.

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — All API paths return SPA HTML. No public JSON endpoints found.

---

## DuckDB Table Summary

| Table | Rows |
|-------|------|
| world_increments | 11 |
| repo_snapshots | 178 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA, no API) |

## GF(3) Color Chain

| Trit | Name | Hex |
|------|------|-----|
| 0 | ERGODIC | #d3869b |
| +1 | PLUS | #b8bb26 |
| −1 | MINUS | #cc241d |
