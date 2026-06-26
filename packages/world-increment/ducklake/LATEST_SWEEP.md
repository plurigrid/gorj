# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-06-26  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 44 |
| bmorphism | user | 28 |
| kubeflow | org | 25 |
| zubyul | user | 17 |
| AustinCStone | social graph | 12 |
| wasita | social graph | 8 |
| migalkin | social graph | 7 |
| M1shaaa | social graph | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | social graph | 4 |
| DJedamski | social graph | 4 |
| **TOTAL** | | **160 repos** |

### GF(3) Trit Color Chain Distribution
| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 53 |
| 1 | PLUS | `#b8bb26` | 54 |
| -1 | MINUS | `#cc241d` | 53 |

### Top Repos by Stars
| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,744 | — | 2026-06-18 |
| kubeflow/pipelines | 4,156 | Python | 2026-06-25 |
| kubeflow/spark-operator | 3,128 | Python | 2026-06-26 |
| kubeflow/trainer | 2,121 | Go | 2026-06-25 |
| kubeflow/katib | 1,685 | Python | 2026-06-23 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/asi | 26 | HTML | 2026-06-10 |

### Most Recently Active
- `plurigrid/gorj` — pushed 2026-06-25 (this repo! 823 open issues)
- `kubeflow/spark-operator` — pushed 2026-06-26
- `wasita/wasita.github.io` — pushed 2026-06-25
- `bmorphism/Gay.jl` — pushed 2026-06-25 (187 open issues)
- `M1shaaa/M1shaaa` — pushed 2026-06-25

### Notable Plurigrid Activity
- **gorj** (`plurigrid/gorj`): forj + Rama topology nREPL routing + GF(3) gay trit coloring — 823 open issues, pushed 2026-06-25
- **eirobri** (`plurigrid/eirobri`): EiRoBri replay world — 30 open issues, pushed 2026-06-23
- **asi** (`plurigrid/asi`): everything is topological chemputer! — 26 stars
- **nanoclj-zig** (`plurigrid/nanoclj-zig`): NaN-boxed Clojure interpreter in Zig 0.15 — 20 open issues

### Notable TeglonLabs Activity
- **jank-crane** (`TeglonLabs/jank-crane`): crane-jank converged-IR hub — pushed 2026-06-08

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)

All 28 Hamming swarm addresses (alice, bob, A-Z) returned **0.0 APT**.
Aptos mainnet returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` on all addresses — accounts exist on-chain but have never received native APT.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...f4588 | 0.0 |
| U | 0x7586...f9956 | 0.0 |
| V | 0xb59d...af2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...444c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

### Multisig Contract Probes (5 contracts)

All 5 multisig contracts responded successfully. All require **2-of-2 signatures** and are **HEALTHY**.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | HEALTHY |
| A-G | 0xf56c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY |
| S-T | 0x3b1c...7883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `https://testnet.mnx.fi/api/markets` returned HTTP 401 Unauthorized. The testnet requires authentication; no market data could be extracted.

---

## DuckDB Schema Summary

```
world_increments  160 rows  -- GF(3) colored world events
repo_snapshots    160 rows  -- GitHub repo metadata
aptos_snapshots    28 rows  -- Hamming swarm wallet balances
multisig_probes     5 rows  -- Multisig contract health
mnx_snapshots       1 row   -- MNX market (unavailable marker)
```

**GF(3) color chain:** ERGODIC #d3869b (trit=0) -> PLUS #b8bb26 (trit=1) -> MINUS #cc241d (trit=-1) -> repeat
