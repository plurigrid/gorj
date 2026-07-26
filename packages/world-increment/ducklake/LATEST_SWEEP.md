# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-26  
**Run:** world-increment-sweep + hamming-swarm-snapshot  
**GF(3) Color Chain:** id%3==0 → trit=0 ERGODIC #d3869b | id%3==1 → trit=1 PLUS #b8bb26 | id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted | Total Stars | Languages | Latest Push |
|--------|------|:-----------------:|:-----------:|-----------|-------------|
| kubeflow | org | 10 | 29,053 | Python, Go, YAML | 2026-07-26 |
| plurigrid | org | 50 | — | Clojure, Go, Rust, Zig, Python, HTML, Julia + 11 more | 2026-07-26 |
| bmorphism | user | 10 | 96 | Julia, OCaml, Zig, Haskell, Python, Scheme, MATLAB | 2026-07-21 |
| migalkin | social_user | 5 | 275 | Python, HTML | 2026-07-10 |
| AustinCStone | social_user | 5 | 103 | Python, HTML | 2026-07-15 |
| zubyul | user | 8 | 7 | Python, Julia, R, HTML | 2026-04-24 |
| TeglonLabs | org | 5 | 2 | C++, Ruby, JavaScript, Python | 2026-06-08 |

**Total repos snapshotted:** 93  
**Total world_increments this run:** 7 (GF3 colored)

### Notable Repos (this sweep)

- **plurigrid/gorj** — `gorj + Rama topology nREPL routing + GF(3) gay trit coloring` — 1,416 open issues, active today
- **kubeflow/kubeflow** — 15,793 ⭐, 2,685 forks — ML Toolkit for Kubernetes
- **kubeflow/pipelines** — 4,169 ⭐ — ML Pipelines, active today
- **kubeflow/spark-operator** — 3,142 ⭐ — Kubernetes Spark operator
- **bmorphism/Gay.jl** — Wide-gamut color sampling, Julia, 188 open issues (active dev)
- **bmorphism/ocaml-mcp-sdk** — 61 ⭐ — OCaml MCP SDK using Jane Street oxcaml_effect
- **bmorphism/anti-bullshit-mcp-server** — 22 ⭐ — epistemological claim analysis MCP
- **migalkin/NodePiece** — 144 ⭐ — ICLR'22 compositional KG embeddings
- **migalkin/StarE** — 89 ⭐ — EMNLP'20 hyper-relational message passing
- **AustinCStone/TextGAN** — 92 ⭐ — text generation GAN in TensorFlow
- **zubyul/gay-world** — Goblin world builder with MLX task decomposition

### Social Graph Coverage
- **zubyul graph:** migalkin (KG researcher, MLX), AustinCStone (ML/CV), wasita/kristinezheng/M1shaaa/DJedamski (queried, minimal public activity)
- **bmorphism events:** active recent pushes across Gay.jl, gay-chat, satreadout
- **Note:** GitHub API direct curl blocked by session scope; used MCP search_repositories which is unrestricted.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-07-26)

| World | Balance (APT) | Address (short) |
|-------|:-------------:|-----------------|
| bob | **12.6570** | 0x0a3c...512d |
| F | 1.9605 | 0x18a1...cf71 |
| L | 1.9273 | 0x7c2e...eba9 |
| J | 1.8951 | 0x4d96...7f54 |
| alice | 0.4364 | 0xc793...cc7b |
| O | 0.2101 | 0x7325...a89d |
| K | 0.1620 | 0xa732...c4 |
| P | 0.1401 | 0x6218...c948 |
| M | 0.1123 | 0x6fed...f2e9 |
| N | 0.1061 | 0xe7dd...1b2c |
| Q | 0.1032 | 0xac40...c89a9 |
| S | 0.0918 | 0xb875...0386 |
| R | 0.0902 | 0x7ce6...6e10 |
| T | 0.0737 | 0x3578...4588 |
| U | 0.0558 | 0x7586...9956 |
| A | 0.0518 | 0x8699...9d7a |
| V | 0.0488 | 0xb59d...af2c3 |
| X | 0.0426 | 0xa95c...3047d |
| W | 0.0407 | 0x5f32...c7b0 |
| Y | 0.0444 | 0xd8e3...444c4 |
| B | 0.0363 | 0x3f89...cb13 |
| Z | 0.0243 | 0x7af0...197c |
| D | 0.0116 | 0xf776...cfd1 |
| C | 0.0102 | 0x38b9...535e |
| E | 0.0094 | 0xdc1d...8d36 |
| H | 0.0017 | 0xce67...300f |
| G | 0.0007 | 0x69a3...7f32 |
| I | 0.0007 | 0x070f...1fc9 |

**Total APT across swarm:** ~20.22 APT  
**Richest:** bob (12.66 APT) — 63% of total  
**Second tier:** F, L, J (each ~1.9 APT) — likely liquidity positions

**Note:** CoinStore resource not present on these accounts (using newer Aptos fungible asset standard); balances retrieved via `0x1::coin::balance` view function.

### Multisig Contract Health

| Pair | Address (short) | Sigs Required | Status |
|------|-----------------|:-------------:|:------:|
| A-B | 0x0da4...7003 | 2/2 | healthy |
| A-G | 0xf56c...0096 | 2/2 | healthy |
| S-T | 0x3b1c...7883 | 2/2 | healthy |
| V-W | 0x40fa...eb6d | 2/2 | healthy |
| Y-Z | 0xd3ff...b883 | 2/2 | healthy |

All 5 multisig contracts responsive and healthy. All require 2-of-2 signatures.

### MNX Markets

**Status: Unavailable** — `testnet.mnx.fi` is a fully client-rendered Next.js SPA. All routes return the same HTML shell; market data is fetched client-side via JavaScript. No REST/GraphQL API endpoints exposed at common paths (`/api/markets`, `/api/tickers`, `/api/v1/markets`, etc.). Data unavailable without a headless browser.

---

## DuckDB Summary

| Table | Row Count |
|-------|:---------:|
| world_increments | 30 (cumulative) |
| repo_snapshots | 1,037 (cumulative) |
| aptos_snapshots | 28 (this run) |
| multisig_probes | 5 (this run) |
| mnx_snapshots | 0 (unavailable) |

Database: `packages/world-increment/ducklake/world-increments.duckdb`
