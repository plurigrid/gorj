# World-Increment Sweep + Hamming Snapshot
**Date:** 2026-07-25  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured | Total Known |
|--------|------|---------------|-------------|
| plurigrid | org | 50 | 103 |
| kubeflow | org | 49 | 49 |
| TeglonLabs | org | 5 | 5 |
| bmorphism | user | 8 | 106 |
| zubyul | user | 5 | 49 |
| migalkin | social | 3 | 19 |
| wasita | social | 2 | 12 |
| kristinezheng | social | 1 | 5 |
| M1shaaa | social | 1 | 8 |
| AustinCStone | social | 1 | 41 |
| DJedamski | social | 1 | 6 |

### Top Repos by Stars (this sweep)
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15793 | — |
| kubeflow/pipelines | 4170 | Python |
| kubeflow/spark-operator | 3143 | Python |
| kubeflow/trainer | 2153 | Go |
| kubeflow/katib | 1692 | Python |
| kubeflow/community-distribution | 1029 | YAML |
| kubeflow/arena | 815 | Go |
| kubeflow/kale | 697 | Python |
| kubeflow/mpi-operator | 530 | Go |
| migalkin/NodePiece | 144 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| bmorphism/anti-bullshit-mcp-server | 22 | JavaScript |
| plurigrid/asi | 31 | HTML |

### Most Active (recent push 2026-07-25)
| Repo | Pushed At |
|------|-----------|
| kubeflow/pipelines | 2026-07-25 |
| kubeflow/kale | 2026-07-25 |
| kubeflow/sdk | 2026-07-25 |
| plurigrid/gorj | 2026-07-25 (1397 open issues) |
| wasita/wasita.github.io | 2026-07-21 |
| bmorphism/Gay.jl | 2026-07-21 (188 open issues) |

### GF(3) World-Increment Color Chain
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 49 |
| +1 | #b8bb26 | PLUS | 50 |
| -1 | #cc241d | MINUS | 50 |

**Total world-increments this session:** 126  
**Cumulative world-increments in DB:** 149

### Notable Observations
- `plurigrid/gorj` (this repo) has 1397 open issues — most active in the graph
- `bmorphism/Gay.jl` has 188 open issues — active development
- TeglonLabs newest repo `jank-crane` (C++, GF3 convergence maps) pushed June 2026
- `kubeflow/mcp-server` (29 stars) — Kubeflow now has an MCP integration
- `bmorphism/ocaml-mcp-sdk` (61 stars) — highest-starred bmorphism repo

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances
**Sweep time:** 2026-07-25  
**Method:** Aptos fullnode REST API v1, CoinStore resource, 1s sleep between calls

All 28 wallets (alice, bob, A-Z) returned **0.0 APT** via the CoinStore resource query.
Accounts may hold APT in fungible asset stores (Aptos v2 API) rather than legacy coin stores,
or are initialized but unfunded on mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
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
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...f956 | 0.0 |
| V | 0xb59d...af2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...444c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

### Multisig Contract Probes — ALL HEALTHY
| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | healthy |
| A-G | 0xf56c...0096 | 2 | healthy |
| Y-Z | 0xd3ff...b883 | 2 | healthy |
| S-T | 0x3b1c...7883 | 2 | healthy |
| V-W | 0x40fa...eb6d | 2 | healthy |

All 5 multisig contracts require 2-of-N signatures and responded successfully to view calls.

### MNX Markets
`https://testnet.mnx.fi` — UNAVAILABLE  
`https://testnet.mnx.fi/api/markets` — 404 Not Found  
The testnet frontend is a SPA shell that yields no market data via static fetch.
`mnx_snapshots` table remains empty this sweep.

---

## DuckDB Table Summary
| Table | Rows |
|-------|------|
| world_increments | 149 (cumulative) |
| repo_snapshots | 1070 (cumulative) |
| aptos_snapshots | 28 (this sweep) |
| multisig_probes | 5 (this sweep) |
| mnx_snapshots | 0 (unavailable) |
