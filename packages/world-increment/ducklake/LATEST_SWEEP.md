# World Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-07-05 16:10 UTC  
**GF(3) Color Chain:** id%3==0 → trit=0 ERGODIC #d3869b | id%3==1 → trit=1 PLUS #b8bb26 | id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Found | Top Star |
|--------|------|-------------|----------|
| plurigrid | org | 20 | asi (28★) |
| kubeflow | org | 12 | kubeflow/kubeflow (15,763★) |
| TeglonLabs | org | 5 | jank-crane, mathpix-gem |
| bmorphism | user | 10 | ocaml-mcp-sdk (61★) |
| zubyul | user | 14 | jonikas_lab_data_analysis_misc (2★) |
| migalkin | social | 6 | NodePiece (144★) |
| wasita | social | 3 | magic-garden (2★) |
| AustinCStone | social | 4 | TextGAN (92★) |
| DJedamski | social | 2 | Kaggle (1★) |
| kristinezheng | social | 2 | (all 0★) |
| M1shaaa | social | 2 | (all 0★) |

### Notable Repos (by stars)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,763 | — | 2026-06-18 |
| kubeflow/pipelines | 4,169 | Python | 2026-07-05 |
| kubeflow/spark-operator | 3,132 | Python | 2026-07-02 |
| kubeflow/trainer | 2,129 | Go | 2026-07-03 |
| kubeflow/katib | 1,689 | Python | 2026-07-01 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/asi | 28 | HTML | 2026-06-29 |
| migalkin/kgcourse2021 | 25 | HTML | 2026-02-16 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| bmorphism/risc0-cosmwasm-example | 23 | Rust | 2022-10-20 |
| bmorphism/say-mcp-server | 20 | JavaScript | 2025-01-07 |
| bmorphism/babashka-mcp-server | 19 | JavaScript | 2025-01-05 |

### Hot Repos (pushed today or yesterday)

| Repo | Pushed | Stars | Issues |
|------|--------|-------|--------|
| kubeflow/community-distribution | 2026-07-05 | 1,028 | 27 |
| kubeflow/pipelines | 2026-07-05 | 4,169 | 413 |
| bmorphism/Gay.jl | 2026-07-05 | 2 | 187 |
| plurigrid/gorj | 2026-07-05 | 0 | 990 |
| wasita/wasita.github.io | 2026-07-05 | 1 | 8 |

### GF(3) Distribution

73 new increments inserted this sweep:
- trit=0 ERGODIC (#d3869b): 25 repos (ids: 3,6,9,…)
- trit=1 PLUS (#b8bb26): 24 repos (ids: 1,4,7,…)
- trit=-1 MINUS (#cc241d): 24 repos (ids: 2,5,8,…)

Total cumulative in DB: **96 world_increments**, **1017 repo_snapshots**

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet — Wallet Balances (28 addresses)

**Status:** All 28 addresses probed. APT CoinStore resource not found on any address (accounts have no registered APT holding). Ledger at block 6,119,383,777, epoch 16,426.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793…cc7b | null (unregistered) |
| bob | 0x0a3c…512d | null (unregistered) |
| A | 0x8699…9d7a | null (unregistered) |
| B | 0x3f89…b13 | null (unregistered) |
| C | 0x38b9…35e | null (unregistered) |
| D | 0xf776…dd1 | null (unregistered) |
| E | 0xdc1d…d36 | null (unregistered) |
| F | 0x18a1…f71 | null (unregistered) |
| G | 0x69a3…f32 | null (unregistered) |
| H | 0xce67…00f | null (unregistered) |
| I | 0x070f…c9 | null (unregistered) |
| J | 0x4d96…f54 | null (unregistered) |
| K | 0xa732…dc4 | null (unregistered) |
| L | 0x7c2e…ba9 | null (unregistered) |
| M | 0x6fed…e9 | null (unregistered) |
| N | 0xe7dd…b2c | null (unregistered) |
| O | 0x7325…89d | null (unregistered) |
| P | 0x6218…948 | null (unregistered) |
| Q | 0xac40…a9 | null (unregistered) |
| R | 0x7ce6…e10 | null (unregistered) |
| S | 0xb875…386 | null (unregistered) |
| T | 0x3578…588 | null (unregistered) |
| U | 0x7586…956 | null (unregistered) |
| V | 0xb59d…c3 | null (unregistered) |
| W | 0x5f32…b0 | null (unregistered) |
| X | 0xa95c…47d | null (unregistered) |
| Y | 0xd8e3…4c4 | null (unregistered) |
| Z | 0x7af0…97c | null (unregistered) |

> Diagnostic: Aptos API reachable, ledger live at epoch 16426. All addresses return `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — these hamming swarm addresses hold no on-chain APT balance.

### Multisig Probes (5 pairs)

All 5 probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4…003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c…096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ff…883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c…883 | 2 | ✅ HEALTHY |
| V-W | 0x40fa…b6d | 2 | ✅ HEALTHY |

**All 5 multisigs require 2/N signatures — all contracts responding normally.**

### MNX Markets (testnet.mnx.fi)

**Status:** UNAVAILABLE — testnet.mnx.fi API paths did not yield data. SPA returns no parseable market data via `/api/markets` or root path.

---

## DuckDB State

```
world_increments:  96 rows
repo_snapshots:  1017 rows
aptos_snapshots:    28 rows
multisig_probes:     5 rows
mnx_snapshots:       0 rows (MNX unavailable)
```

Database: `packages/world-increment/ducklake/world-increments.duckdb`

---

*Sweep by world-increment-sweep + hamming-swarm-snapshot agent — GF(3) color chain active*
