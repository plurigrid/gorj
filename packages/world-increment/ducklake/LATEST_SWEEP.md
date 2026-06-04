# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-04

## Sweep Metadata
- **Date:** 2026-06-04
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 48 |
| kubeflow | org | 19 |
| TeglonLabs | org | 4 |
| bmorphism | user | 30 |
| zubyul | user | 12 |
| migalkin | user (social) | 5 |
| DJedamski | user (social) | 3 |
| wasita | user (social) | 5 |
| kristinezheng | user (social) | 3 |
| M1shaaa | user (social) | 3 |
| AustinCStone | user (social) | 5 |
| **TOTAL** | | **135** |

### Top Repos by Stars

| Stars | Repo | Language |
|------:|------|----------|
| 15705 | kubeflow/kubeflow | — |
| 4152 | kubeflow/pipelines | Python |
| 3124 | kubeflow/spark-operator | Python |
| 2111 | kubeflow/trainer | Go |
| 1685 | kubeflow/katib | Python |
| 1462 | kubeflow/examples | Jsonnet |
| 1020 | kubeflow/manifests | YAML |
| 811 | kubeflow/arena | Go |
| 690 | kubeflow/kale | Python |
| 528 | kubeflow/mpi-operator | Go |
| 144 | migalkin/NodePiece | Python |
| 92 | AustinCStone/TextGAN | Python |
| 61 | bmorphism/ocaml-mcp-sdk | OCaml |
| 48 | plurigrid/gorj | Clojure |
| 25 | plurigrid/asi | HTML |
| 23 | bmorphism/anti-bullshit-mcp-server | JavaScript |
| 23 | bmorphism/risc0-cosmwasm-example | Rust |
| 20 | bmorphism/say-mcp-server | JavaScript |

### Notable Activity (pushed 2026-06-04)
- **plurigrid/gorj** — forj + Rama topology nREPL routing + GF(3) gay trit coloring (349 open issues)
- **plurigrid/place** — most recently pushed in plurigrid org (TeX)
- **plurigrid/eirobri** — EiRoBri replay world (Clojure)
- **kubeflow/hub** — Model Registry pushed 13:14 UTC
- **kubeflow/pipelines** — 4152★, pushed 12:45 UTC
- **bmorphism/Gay.jl** — 189 open issues, wide-gamut color sampling (Julia)

### Plurigrid Org Highlights
Active multi-language ecosystem: Clojure · Zig · Rust · Julia · Scheme · Haskell · Go · Swift · OCaml — themes: GF(3) trit coloring, OCapN Syrup, Gay.jl deterministic colors, nanoclj-zig NaN-boxed interpreter, Spritely Goblins mirrors, open games, categorical computing, BCI signal infrastructure.

### bmorphism Highlights
Heavy MCP server portfolio (OCaml SDK, say, babashka, manifold, penrose, NATS, marginalia, anti-bullshit), open games in OCaml/Agda, Gay.jl Julia, Zig Plus Codes, Clojure world launchers.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-06-04)

All 28 addresses queried via `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. All returned **0 APT** — coin store resources not initialized on these addresses.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...4cc7b | 0.0 |
| bob | 0x0a3c...512d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...cfdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...3cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...5300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...7f2e9 | 0.0 |
| N | 0xe7dd...51b2c | 0.0 |
| O | 0x7325...5a89d | 0.0 |
| P | 0x6218...ec948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...d0386 | 0.0 |
| T | 0x3578...f4588 | 0.0 |
| U | 0x7586...f9956 | 0.0 |
| V | 0xb59d...af2c3 | 0.0 |
| W | 0x5f32...cc7b0 | 0.0 |
| X | 0xa95c...3047d | 0.0 |
| Y | 0xd8e3...444c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

> All 28 balances are 0.0 APT. The `CoinStore<AptosCoin>` resource is not registered on these addresses, indicating they have not been initialized with APT or have zero balance.

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|:-------------:|:-------:|
| A-B | 0x0da4...87003 | **2** | ✓ |
| A-G | 0xf56c...c0096 | **2** | ✓ |
| Y-Z | 0xd3ff...5b883 | **2** | ✓ |
| S-T | 0x3b1c...d7883 | **2** | ✓ |
| V-W | 0x40fa...0eb6d | **2** | ✓ |

All 5 multisigs require 2-of-N signatures. All healthy.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA — all probed paths (`/api/markets`, `/api/tickers`, `/api/v1/markets`) return the HTML shell. No public REST API is exposed from this endpoint. **mnx_snapshots: 0 rows.**

---

## DuckDB Schema Summary

```
world_increments   135 rows   — GF(3)-tagged repo push events
repo_snapshots     135 rows   — full repo metadata snapshot  
aptos_snapshots     28 rows   — Hamming swarm wallet balances
multisig_probes      5 rows   — 2-of-N multisig health checks
mnx_snapshots        0 rows   — SPA, no REST API available
```

## GF(3) Color Assignment Rule

| id % 3 | Trit | Color | Name |
|--------|------|-------|------|
| 0 | 0 | `#d3869b` | **ERGODIC** |
| 1 | +1 | `#b8bb26` | **PLUS** |
| 2 | -1 | `#cc241d` | **MINUS** |

Color chain over 135 increments: 45 ERGODIC · 45 PLUS · 45 MINUS
