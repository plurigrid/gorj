# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-05  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) chain:** ERGODIC #d3869b (trit=0) | PLUS #b8bb26 (trit=1) | MINUS #cc241d (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social | 19 |
| DJedamski | social | 6 |
| wasita | social | 11 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| AustinCStone | social | 40 |
| **TOTAL** | | **390** |

### Top Repos by Stars

| full_name | language | stars | forks | pushed_at |
|-----------|----------|-------|-------|-----------|
| kubeflow/kubeflow | — | 15,706 | 2,670 | 2026-05-24 |
| kubeflow/pipelines | Python | 4,152 | 2,007 | 2026-06-05 |
| kubeflow/spark-operator | Python | 3,125 | 1,488 | 2026-06-04 |
| kubeflow/trainer | Go | 2,111 | 964 | 2026-06-05 |
| kubeflow/katib | Python | 1,685 | 525 | 2026-06-04 |
| kubeflow/examples | Jsonnet | 1,462 | 756 | 2025-04-14 |
| migalkin/NodePiece | Python | 144 | 21 | 2026-05-07 |
| migalkin/StarE | Python | 89 | 16 | 2026-04-16 |
| AustinCStone/TextGAN | Python | 92 | 30 | 2025-03-03 |
| plurigrid/asi | HTML | 25 | 6 | 2026-04-26 |

### Notable Plurigrid Activity
- **plurigrid/gorj** (this repo) — 381 open issues, pushed 2026-06-05
- **plurigrid/eirobri** — Clojure, 29 open issues, pushed 2026-06-03
- **plurigrid/place** — TeX, pushed 2026-06-04

### Notable bmorphism Activity
- **bmorphism/Gay.jl** — Julia, 189 open issues, pushed 2026-06-05
- **bmorphism/world** — Python, pushed 2026-06-02
- **bmorphism/ocaml-mcp-sdk** — OCaml, 61 stars, 2 forks

### Notable zubyul Activity
- **zubyul/voice-observatory** — Python, pushed 2026-04-24
- **zubyul/tilelang-kernels** — Python (GF(3)/SplitMix64 GPU kernels), 2026-03-16
- **zubyul/nash-tui** — Rust, NASH token real-time TUI

### DuckDB Tables
```
world_increments : 353 rows  (GF3 ERGODIC=117, PLUS=118, MINUS=118)
repo_snapshots   : 1274 rows
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
Queried 28 addresses (alice, bob, A–Z) via Aptos fullnode mainnet API.

**Result:** All 28 addresses returned `resource_not_found` — the CoinStore resource for `0x1::aptos_coin::AptosCoin` has not been initialized on any of these accounts. This indicates the accounts exist on-chain but have never received APT, or the addresses are newly generated and unfunded.

| world | address (truncated) | balance_apt |
|-------|---------------------|-------------|
| alice | 0xc793…cc7b | NULL |
| bob | 0x0a3c…2d5d | NULL |
| A–Z | 0x86…–0x7af0… | NULL (all) |

*Stored with `NULL` balance in `aptos_snapshots` (28 rows).*

### Multisig Contract Probes (Aptos Mainnet)
All 5 multisig contracts successfully probed via `0x1::multisig_account::num_signatures_required`.

| pair | address | sigs_required | healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428… | 2 | true |
| A-G | 0xf56c4a1c… | 2 | true |
| Y-Z | 0xd3ffe181… | 2 | true |
| S-T | 0x3b1c3ae9… | 2 | true |
| V-W | 0x40fad7b4… | 2 | true |

**All 5 multisigs healthy.** Each requires 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)
**Status: Unavailable.** `testnet.mnx.fi` is protected by Vercel deployment protection (auth required). No market data could be retrieved. `mnx_snapshots` table created but empty.

---

## GF(3) Color Chain Summary

| id % 3 | trit | name | color |
|--------|------|------|-------|
| 0 | 0 | ERGODIC | #d3869b |
| 1 | 1 | PLUS | #b8bb26 |
| 2 | -1 | MINUS | #cc241d |

Distribution across 353 world_increments: ERGODIC=117, PLUS=118, MINUS=118 (balanced).

---

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent.*  
*Sweep timestamp: 2026-06-05*
