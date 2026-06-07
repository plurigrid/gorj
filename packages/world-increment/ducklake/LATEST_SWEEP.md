# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-07  
**Sweep ID:** world-increment/sweep-2026-06-07  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 52 |
| kubeflow | org | 31 |
| TeglonLabs | org | 4 |
| bmorphism | user | 64 |
| zubyul | user | 27 |
| migalkin | social | 7 |
| wasita | social | 6 |
| AustinCStone | social | 7 |
| kristinezheng | social | 4 |
| M1shaaa | social | 4 |
| DJedamski | social | 4 |
| **Total** | | **210 repos** |

### Notable Repos (by stars)

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15706 | 2026-05-24 |
| kubeflow/pipelines | Python | 4153 | 2026-06-06 |
| kubeflow/spark-operator | Python | 3125 | 2026-06-04 |
| kubeflow/trainer | Go | 2112 | 2026-06-05 |
| kubeflow/katib | Python | 1685 | 2026-06-05 |
| kubeflow/examples | Jsonnet | 1462 | 2025-04-14 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| plurigrid/asi | HTML | 25 | 2026-04-26 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |

### Active Repos (pushed 2026-06)

- `plurigrid/gorj` — forj + Rama nREPL routing + GF(3) coloring (416 open issues)
- `plurigrid/eirobri` — EiRoBri replay world (29 open issues)
- `kubeflow/pipelines` — ML Pipelines (494 open issues)
- `kubeflow/notebooks` — Kubeflow Notebooks (182 open issues)
- `bmorphism/Gay.jl` — Wide-gamut color sampling, 189 open issues

### GF(3) Color Chain (this sweep)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 64 |
| 1 | `#b8bb26` | PLUS | 64 |
| -1 | `#cc241d` | MINUS | 64 |

GF(3) cycle perfectly balanced at 64 per trit (192 total increments).

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

**Status:** All 28 wallets returned `resource_not_found` from the Aptos mainnet fullnode.  
The accounts exist on-chain but have not been initialized with an APT `CoinStore` resource.  
**Total APT across swarm: 0.000000 APT**

| World | Address (truncated) | Balance (APT) | Status |
|-------|---------------------|---------------|--------|
| alice | 0xc793…cc7b | 0.0 | resource_not_found |
| bob | 0x0a3c…2d5d | 0.0 | resource_not_found |
| A | 0x8699…9d7a | 0.0 | resource_not_found |
| B | 0x3f89…b13 | 0.0 | resource_not_found |
| C | 0x38b9…535e | 0.0 | resource_not_found |
| D | 0xf776…fdd1 | 0.0 | resource_not_found |
| E | 0xdc1d…d36 | 0.0 | resource_not_found |
| F | 0x18a1…f71 | 0.0 | resource_not_found |
| G | 0x69a3…f32 | 0.0 | resource_not_found |
| H | 0xce67…300f | 0.0 | resource_not_found |
| I | 0x070f…1fc9 | 0.0 | resource_not_found |
| J | 0x4d96…7f54 | 0.0 | resource_not_found |
| K | 0xa732…5dc4 | 0.0 | resource_not_found |
| L | 0x7c2e…eba9 | 0.0 | resource_not_found |
| M | 0x6fed…7f2e9 | 0.0 | resource_not_found |
| N | 0xe7dd…51b2c | 0.0 | resource_not_found |
| O | 0x7325…5a89d | 0.0 | resource_not_found |
| P | 0x6218…ec948 | 0.0 | resource_not_found |
| Q | 0xac40…5c89a9 | 0.0 | resource_not_found |
| R | 0x7ce6…76e10 | 0.0 | resource_not_found |
| S | 0xb875…9d0386 | 0.0 | resource_not_found |
| T | 0x3578…3f4588 | 0.0 | resource_not_found |
| U | 0x7586…ef9956 | 0.0 | resource_not_found |
| V | 0xb59d…9af2c3 | 0.0 | resource_not_found |
| W | 0x5f32…6ccc7b0 | 0.0 | resource_not_found |
| X | 0xa95c…e33047d | 0.0 | resource_not_found |
| Y | 0xd8e3…fa2444c4 | 0.0 | resource_not_found |
| Z | 0x7af0…4e197c | 0.0 | resource_not_found |

### Multisig Contract Probes (5 pairs)

All contracts healthy — all require 2-of-2 signatures.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4…7003 | 2 | yes |
| A-G | 0xf56c…0096 | 2 | yes |
| Y-Z | 0xd3ff…b883 | 2 | yes |
| S-T | 0x3b1c…7883 | 2 | yes |
| V-W | 0x40fa…eb6d | 2 | yes |

### MNX Markets (testnet.mnx.fi)

**Status:** `testnet.mnx.fi` is protected by Vercel deployment authentication.  
Both `/api/markets` and the root return a Vercel password-protection page.  
No market data is accessible without a visitor password or bypass token.

---

## DuckDB Schema Summary

```
world_increments   -- 216 rows total (192 this sweep + 24 historical)
repo_snapshots     -- 1136 rows total (192 this sweep + 944 historical)
aptos_snapshots    -- 28 rows (this sweep)
multisig_probes    -- 5 rows (this sweep)
mnx_snapshots      -- 1 row (unavailable note)
```

### GF(3) Color Legend

| Color | Hex | Trit | Rule |
|-------|-----|------|------|
| ERGODIC | `#d3869b` | 0 | id % 3 == 0 |
| PLUS | `#b8bb26` | 1 | id % 3 == 1 |
| MINUS | `#cc241d` | -1 | id % 3 == 2 |
