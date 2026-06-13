# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-06-13  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos | Total Stars | Latest Push |
|--------|------|-------|------------|-------------|
| plurigrid | org | 234 | 150 | 2026-06-13 |
| bmorphism | user | 230 | 479 | 2026-06-13 |
| kubeflow | org | 118 | 101,043 | 2026-06-13 |
| TeglonLabs | org | 111 | 14 | 2026-06-08 |
| AustinCStone | user (zubyul social) | 94 | 323 | 2026-02-11 |
| zubyul | user | 78 | 32 | 2026-04-24 |
| migalkin | user (zubyul social) | 66 | 833 | 2026-05-28 |
| wasita | user (zubyul social) | 66 | 10 | 2026-06-01 |
| kristinezheng | user (zubyul social) | 40 | 0 | 2026-06-07 |
| M1shaaa | user (zubyul social) | 35 | 0 | 2026-02-04 |
| DJedamski | user (zubyul social) | 26 | 17 | 2023-04-21 |

**Total repo_snapshots:** 1,098  
**Total world_increments:** 177

### GF(3) Color Chain Distribution
| Trit | Color | Name | Increments |
|------|-------|------|------------|
| 0 | `#d3869b` | ERGODIC | 58 |
| 1 | `#b8bb26` | PLUS | 60 |
| -1 | `#cc241d` | MINUS | 59 |

*GF(3) rule: id%3==0 -> ERGODIC, id%3==1 -> PLUS, id%3==2 -> MINUS*

### Notable Recent Activity
- **plurigrid/gorj** — Pushed 2026-06-13, 539 open issues, Clojure, GF(3) gay trit coloring
- **bmorphism/Gay.jl** — Pushed 2026-06-13, 189 open issues, Wide-gamut color sampling
- **kubeflow/trainer** — 2112 stars, Distributed AI Model Training on Kubernetes
- **kubeflow/spark-operator** — 3127 stars, Kubernetes operator for Apache Spark
- **kubeflow/kubeflow** — 15720 stars, Machine Learning Toolkit for Kubernetes
- **TeglonLabs/jank-crane** — Pushed 2026-06-08, crane-jank converged-IR hub, GF3 convergence maps
- **migalkin/NodePiece** — 144 stars, Compositional KG representations (ICLR'22)
- **bmorphism/ocaml-mcp-sdk** — 61 stars, OCaml SDK for Model Context Protocol

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
**Query time:** 2026-06-13  
All 28 wallets (alice, bob, A-Z) returned **0.0 APT** — CoinStore resource not registered on these addresses at time of query.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793acd...cc7b | 0.0 |
| bob | 0x0a3c00c...512d | 0.0 |
| A-Z | 0x8699edc... - 0x7af0ef6... | 0.0 each |

### Multisig Contract Probes (5/5 healthy)
All 5 multisig contracts on Aptos mainnet responded with `num_signatures_required = 2`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...7003 | 2 | YES |
| A-G | 0xf56c4a1c...0096 | 2 | YES |
| Y-Z | 0xd3ffe181...b883 | 2 | YES |
| S-T | 0x3b1c3ae9...7883 | 2 | YES |
| V-W | 0x40fad7b4...eb6d | 2 | YES |

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — All API paths (/api/markets, /api/v1/markets, /api/tickers) return Vercel deployment protection. Market data could not be extracted. No rows inserted into mnx_snapshots.

---

## DuckDB Schema Summary
```
world_increments   — 177 rows  (GF3-tagged GitHub events)
repo_snapshots     — 1,098 rows (full repo metadata)
aptos_snapshots    — 28 rows  (A-Z + alice/bob balances)
multisig_probes    — 5 rows   (all 2-of-2, healthy)
mnx_snapshots      — 0 rows   (Vercel auth required)
```

## Increment Window
- First: 2026-04-10 23:10:18
- Last:  2026-06-13 05:14:36
