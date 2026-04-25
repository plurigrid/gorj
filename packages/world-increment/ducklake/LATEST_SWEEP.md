# World Increment Sweep + Hamming Snapshot

**Timestamp:** 2026-04-25  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
- **Orgs:** plurigrid, kubeflow, TeglonLabs
- **Users:** bmorphism, zubyul
- **Zubyul social graph:** migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone

### Repo Snapshot Highlights

| Source | Notable Repos | Top Stars |
|--------|--------------|-----------|
| kubeflow | kubeflow/kubeflow, pipelines, trainer, spark-operator | 15599, 4125, 2091, 3120 |
| plurigrid | asi (17★), ontology (7★), vcg-auction (7★), agent (5★) | 17 |
| bmorphism | ocaml-mcp-sdk (60★), anti-bullshit-mcp-server (23★) | 60 |
| migalkin | NodePiece (143★), StarE (89★) — KG research | 143 |
| TeglonLabs | mathpix-gem (2★), coin-flip-mcp (0★) | 2 |
| zubyul | gay-world (1★), voice-observatory, tilelang-kernels | 1 |
| wasita | magic-garden (2★), wasita.github.io (1★) | 2 |
| kristinezheng | kristinezheng.github.io, lookit-jenga | 0 |
| M1shaaa | M1shaaa profile, lab-bookshelf- | 0 |
| AustinCStone | EpsteinSearch, bmforkupdate | 0 |
| DJedamski | kaggle_ncaa18 | 0 |

### Recently Active (pushed 2026-04-24)
- `plurigrid/nanoclj-zig` — NaN-boxed Clojure in Zig 0.15, GF(3) trit conservation
- `plurigrid/asi` — topological chemputer  
- `plurigrid/gorj` — this repo! forj + Rama topology + GF(3) coloring (270 open issues)
- `kubeflow/trainer` — Distributed AI Model Training on Kubernetes
- `kubeflow/pipelines` — ML Pipelines
- `bmorphism/Gay.jl` — Wide-gamut color sampling (187 open issues)
- `zubyul/voice-observatory` — passive macOS TUI
- `M1shaaa/M1shaaa` — profile

### GF(3) Color Chain Distribution (this sweep: 51 new increments)
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 17 |
| +1 | `#b8bb26` | PLUS | 17 |
| -1 | `#cc241d` | MINUS | 17 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-04-25)
> Method: `0x1::coin::balance` view function (FA standard)

| World | Balance (APT) | Address (short) |
|-------|--------------|-----------------|
| bob | 12.6570 | 0x0a3c...512d |
| F | 1.9605 | 0x18a1...3cf71 |
| L | 1.9273 | 0x7c2e...eba9 |
| J | 1.8951 | 0x4d96...7f54 |
| alice | 0.4364 | 0xc793...cc7b |
| K | 0.1619 | 0xa732...5dc4 |
| O | 0.2101 | 0x7325...89d |
| P | 0.1401 | 0x6218...948 |
| M | 0.1123 | 0x6fed...f2e9 |
| N | 0.1061 | 0xe7dd...b2c |
| Q | 0.1032 | 0xac40...89a9 |
| S | 0.0918 | 0xb875...0386 |
| R | 0.0902 | 0x7ce6...6e10 |
| T | 0.0737 | 0x3578...4588 |
| U | 0.0558 | 0x7586...9956 |
| A | 0.0518 | 0x8699...9d7a |
| V | 0.0488 | 0xb59d...f2c3 |
| Y | 0.0444 | 0xd8e3...444c4 |
| X | 0.0426 | 0xa95c...047d |
| W | 0.0407 | 0x5f32...7b0 |
| B | 0.0363 | 0x3f89...cb13 |
| Z | 0.0243 | 0x7af0...197c |
| D | 0.0116 | 0xf776...cdd1 |
| C | 0.0102 | 0x38b9...535e |
| E | 0.0094 | 0xdc1d...8d36 |
| H | 0.0017 | 0xce67...300f |
| G | 0.0007 | 0x69a3...7f32 |
| I | 0.0007 | 0x070f...1fc9 |

**Total swarm balance:** ~20.63 APT

> Note: Legacy `0x1::coin::CoinStore` resource not found for all addresses —
> all balances retrieved via FA `coin::balance` view function.

### Multisig Contract Probes (All 5 healthy)

| Pair | Address (short) | Sigs Required | Status |
|------|----------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ healthy |
| A-G | 0xf56c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

All 5 multisig contracts require 2-of-N signatures. All probes returned healthy.

### MNX Markets (testnet.mnx.fi)
Status: **SPA unavailable** — `testnet.mnx.fi` serves a Next.js SPA with no accessible REST API endpoint at `/api/markets` or `/api/v1/markets`. Market data could not be extracted.

---

## Database State

```
world_increments: 74 rows total (51 new this sweep)
repo_snapshots:   995 rows total (51 new this sweep)
aptos_snapshots:  28 rows (alice, bob, A-Z)
multisig_probes:  5 rows
mnx_snapshots:    1 row (unavailable marker)
```
