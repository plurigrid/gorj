# World Increment Sweep + Hamming Snapshot
**Date:** 2026-06-23  
**GF(3) Color Chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos | Total Stars | Latest Push |
|--------|------|-------|-------------|-------------|
| kubeflow | org | 48 | 34,249 | 2026-06-23 |
| migalkin | user | 19 | 280 | 2025-08-04 |
| bmorphism | user | 100 | 248 | 2026-06-23 |
| AustinCStone | user (zubyul graph) | 30 | 108 | 2026-02-11 |
| plurigrid | org | 100 | 77 | 2026-06-23 |
| zubyul | user | 49 | 14 | 2026-04-24 |
| wasita | user (zubyul graph) | 11 | 5 | 2026-06-19 |
| DJedamski | user (zubyul graph) | 6 | 3 | 2018-03-07 |
| TeglonLabs | org | 5 | 2 | 2026-06-08 |
| kristinezheng | user (zubyul graph) | 5 | 0 | 2026-06-07 |
| M1shaaa | user (zubyul graph) | 8 | 0 | 2026-06-23 |
| **TOTAL** | | **381** | **35,986** | |

### Top 10 Repos by Stars
| Repo | Stars |
|------|-------|
| kubeflow/kubeflow | 15,741 |
| kubeflow/pipelines | 4,157 |
| kubeflow/spark-operator | 3,128 |
| kubeflow/trainer | 2,119 |
| kubeflow/katib | 1,685 |
| kubeflow/examples | 1,460 |
| kubeflow/community-distribution | 1,028 |
| kubeflow/arena | 813 |
| kubeflow/kale | 694 |
| kubeflow/mpi-operator | 528 |

### Notable Non-Kubeflow Repos
- `migalkin/NodePiece` — 144 stars — Compositional KG representations (ICLR'22)
- `migalkin/StarE` — 89 stars — Message passing for hyper-relational KGs (EMNLP 2020)
- `AustinCStone/TextGAN` — 92 stars — GAN for text generation (TensorFlow)
- `bmorphism/ocaml-mcp-sdk` — 61 stars — OCaml MCP SDK
- `bmorphism/anti-bullshit-mcp-server` — 23 stars
- `bmorphism/risc0-cosmwasm-example` — 23 stars
- `plurigrid/asi` — 26 stars
- `TeglonLabs/jank-crane` — C++ — crane-jank converged-IR hub with GF3 convergence maps

### Active Social Graph (bmorphism/zubyul cluster, 2026)
- `bmorphism`: 100 repos pushed through 2026-06-23 (say-mcp-server, ocaml-mcp-sdk, Gay.jl)
- `zubyul`: 49 repos — terminal/emacs worlds, Nash TUI, Gay.jl worlds, Aptos Move
- `M1shaaa`: pushed profile today (2026-06-23)
- `kristinezheng`: personal site updated 2026-06-07
- `wasita`: personal site + proj-template active through June 2026
- `plurigrid`: 100 repos, very active (pushed today), Clojure/Rust/TypeScript core

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-06-23)
All 28 hamming-swarm wallets queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Balance (APT) | Status |
|-------|---------------|--------|
| alice | 0.0 | Empty |
| bob | 0.0 | Empty |
| A–Z (26 wallets) | 0.0 each | Empty |

**Result:** All 28 swarm wallets show 0 APT balance. The CoinStore resource is present but holds no funds.

### Multisig Contract Probes
All 5 multisig contracts queried via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428... | **2** | YES |
| A-G | 0xf56c4a1c... | **2** | YES |
| Y-Z | 0xd3ffe181... | **2** | YES |
| S-T | 0x3b1c3ae9... | **2** | YES |
| V-W | 0x40fad7b4... | **2** | YES |

**Result:** All 5 multisig accounts require 2-of-N signatures. All respond as healthy.

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — testnet.mnx.fi requires Vercel authentication for all endpoints
(/, /api/markets, /api/v1/markets). No market data could be extracted without credentials.

---

## DuckDB Schema Summary
File: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows | Description |
|-------|------|-------------|
| world_increments | 381 | GF(3) color-coded event log |
| repo_snapshots | 381 | GitHub repo metadata snapshots |
| aptos_snapshots | 28 | Hamming swarm APT balances |
| multisig_probes | 5 | Multisig contract health checks |
| mnx_snapshots | 0 | MNX market data (auth-gated, unavailable) |

## GF(3) Distribution
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 127 |
| 1 | #b8bb26 | PLUS | 127 |
| -1 | #cc241d | MINUS | 127 |
