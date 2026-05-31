# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-05-31  
**GF(3) Color Chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 36 |
| kubeflow | org | 17 |
| TeglonLabs | org | 4 |
| bmorphism | user | 14 |
| zubyul | user | 10 |
| migalkin | social-graph | 5 |
| DJedamski | social-graph | 2 |
| wasita | social-graph | 5 |
| kristinezheng | social-graph | 2 |
| M1shaaa | social-graph | 3 |
| AustinCStone | social-graph | 6 |
| **Total** | | **104** |

### GF(3) World-Increment Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 34 |
| 1 | #b8bb26 | PLUS | 35 |
| -1 | #cc241d | MINUS | 35 |

### Notable Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15693 | — | 2026-05-24 |
| kubeflow/pipelines | 4149 | Python | 2026-05-30 |
| kubeflow/spark-operator | 3124 | Python | 2026-05-29 |
| kubeflow/trainer | 2106 | Go | 2026-05-30 |
| kubeflow/katib | 1685 | Python | 2026-05-29 |
| kubeflow/examples | 1463 | Jsonnet | 2025-04-14 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| plurigrid/asi | 23 | HTML | 2026-04-26 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| bmorphism/Gay.jl | 1 | Julia | 2026-05-31 (active!) |
| plurigrid/gorj | 0 | Clojure | 2026-05-31 (active!) |

### Most Active Repos (pushed 2026-05)

- `plurigrid/eirobri` — EiRoBri replay world (Clojure, 28 open issues)
- `plurigrid/gorj` — forj + Rama + GF(3) trit coloring (Clojure, 270 open issues)
- `bmorphism/Gay.jl` — Wide-gamut color sampling (Julia, 189 open issues)
- `kubeflow/pipelines` — ML Pipelines for Kubernetes (Python, 488 open issues)
- `kubeflow/trainer` — Distributed AI Training on Kubernetes (Go, 127 open issues)
- `migalkin/RWL` — Weisfeiler and Leman Go Relational (Python)

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (alice…Z, 28 addresses)

All 28 addresses queried via Aptos mainnet fullnode API  
(`GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…2d5d | 0.0 |
| A | 0x8699…9d7a | 0.0 |
| B | 0x3f89…b13 | 0.0 |
| C | 0x38b9…535e | 0.0 |
| D | 0xf776…fdd1 | 0.0 |
| E | 0xdc1d…8d36 | 0.0 |
| F | 0x18a1…cf71 | 0.0 |
| G | 0x69a3…7f32 | 0.0 |
| H | 0xce67…300f | 0.0 |
| I | 0x070f…1fc9 | 0.0 |
| J | 0x4d96…7f54 | 0.0 |
| K | 0xa732…5dc4 | 0.0 |
| L | 0x7c2e…ba9 | 0.0 |
| M | 0x6fed…f2e9 | 0.0 |
| N | 0xe7dd…1b2c | 0.0 |
| O | 0x7325…a89d | 0.0 |
| P | 0x6218…c948 | 0.0 |
| Q | 0xac40…c89a9 | 0.0 |
| R | 0x7ce6…6e10 | 0.0 |
| S | 0xb875…0386 | 0.0 |
| T | 0x3578…4588 | 0.0 |
| U | 0x7586…9956 | 0.0 |
| V | 0xb59d…f2c3 | 0.0 |
| W | 0x5f32…c7b0 | 0.0 |
| X | 0xa95c…047d | 0.0 |
| Y | 0xd8e3…44c4 | 0.0 |
| Z | 0x7af0…197c | 0.0 |

> All 28 addresses resolved on Aptos mainnet. CoinStore resources return 0 — addresses may hold fungible assets via other resource types or are unfunded in the standard APT coin store.

### Multisig Contract Probes

Probed via `POST /v1/view` with `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4…7003 | 2 | ✅ |
| A-G | 0xf56c…0096 | 2 | ✅ |
| Y-Z | 0xd3ff…b883 | 2 | ✅ |
| S-T | 0x3b1c…7883 | 2 | ✅ |
| V-W | 0x40fa…eb6d | 2 | ✅ |

All 5 multisig contracts respond and require 2 signatures. All probes healthy.

### MNX Markets (testnet.mnx.fi)

The MNX testnet ("The AI Exchange") is a Next.js SPA. The `/api/markets` endpoint returns 404 and no market data is embedded server-side. Market data loads client-side via JavaScript bundles.  
**Status: data unavailable in server-side scrape — logged as 0 mnx_snapshots rows.**

---

## DuckDB Schema & Counts

```
packages/world-increment/ducklake/world-increments.duckdb
├── world_increments     104 rows — per-repo GF(3) colored event log
├── repo_snapshots       104 rows — repo metadata (stars, forks, lang, desc)
├── aptos_snapshots       28 rows — hamming swarm wallet balances (APT)
├── multisig_probes        5 rows — 2-of-N threshold health probes
└── mnx_snapshots          0 rows — MNX market data (SPA, unavailable)
```

### GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC  
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS  
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS  
