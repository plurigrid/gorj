# World Increment Sweep + Hamming Swarm Snapshot

**Sweep date:** 2026-07-20  
**Branch:** world-increment/sweep-2026-07-20

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Sampled | Notable |
|---|---|---|---|
| plurigrid | org | 50 (of 103) | gorj active today (1281 issues), asi 31★ |
| bmorphism | user | 50 | ocaml-mcp-sdk 61★, anti-bullshit-mcp-server 22★ |
| zubyul | user | 49 | from-possible-worlds pushed 2026-07-18 |
| kubeflow | org | 49 | kubeflow/kubeflow 15785★, pipelines 4169★ |
| TeglonLabs | org | 5 | jank-crane (C++), mathpix-gem (Ruby) |
| migalkin | user | 19 | NodePiece 144★ (ICLR'22 KG repr) |
| wasita | user | 12 | wasita.github.io active 2026-07-20 |
| AustinCStone | user | 20 | TextGAN 92★ |
| M1shaaa | user | 8 | lab-bookshelf- (TypeScript) |
| DJedamski | user | 6 | kaggle/R stats projects |
| kristinezheng | user | 5 | lookit-jenga (cognitive science) |

### Top Repositories by Stars

| Repo | Stars | Language | Last Push |
|---|---|---|---|
| kubeflow/kubeflow | 15785 | — | 2026-07-20 |
| kubeflow/pipelines | 4169 | Python | 2026-07-20 |
| kubeflow/spark-operator | 3140 | Python | 2026-07-20 |
| kubeflow/trainer | 2152 | Go | 2026-07-20 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/asi | 31 | HTML | 2026-07-10 |
| bmorphism/anti-bullshit-mcp-server | 22 | JavaScript | 2026-01-16 |
| migalkin/kgcourse2021 | 24 | HTML | 2026-07-10 |
| bmorphism/shitcoin | 5 | Python | 2026-04-08 |

### Most Active (pushed today 2026-07-20)

- `plurigrid/gorj` — 1281 open issues, Clojure
- `kubeflow/pipelines` — 4169★, 435 issues
- `kubeflow/trainer` — 2152★
- `kubeflow/community-distribution` — 1029★
- `kubeflow/sdk` — 126★, 177 issues
- `bmorphism/Gay.jl` — 187 issues, pushed 09:40 UTC
- `wasita/wasita.github.io` — Svelte personal site

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|---|---|---|---|
| 0 | #d3869b | ERGODIC | 25 |
| +1 | #b8bb26 | PLUS | 27 |
| -1 | #cc241d | MINUS | 26 |

**Total world increments this sweep:** 55 new (78 total in ducklake including prior sweeps)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

**Probe time:** 2026-07-20  
**Endpoint:** `https://fullnode.mainnet.aptoslabs.com/v1`  
**Result:** All 28 addresses returned HTTP 404 on `0x1::coin::CoinStore<AptosCoin>`

None of the Hamming swarm addresses have an initialized APT coin store on mainnet. Possible explanations: addresses are on devnet/testnet, have never received APT (uninitialized accounts), or hold tokens via a different resource type.

| World | Address (prefix) | Balance APT |
|---|---|---|
| alice | 0xc793ac... | 0.0 (no store) |
| bob | 0x0a3c00... | 0.0 (no store) |
| A–Z (26) | (see DuckDB) | 0.0 (no store) |

### Multisig Contract Probes

All 5 multisig contracts healthy — **2-of-2 signatures required** across the board:

| Pair | Address (prefix) | Sigs Required | Status |
|---|---|---|---|
| A-B | 0x0da4f4... | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a... | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe1... | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3a... | 2 | ✓ HEALTHY |
| V-W | 0x40fad7... | 2 | ✓ HEALTHY |

2-of-2 scheme consistent across all swarm multisig pairs.

### MNX Markets (testnet.mnx.fi)

**Status:** UNAVAILABLE — all API endpoints return HTTP 401 Unauthorized.  
Paths tried: `/api/markets`, `/api/v1/markets`, `/api/tickers`, `/markets`, `/api/v1/tickers`

---

## DuckDB Summary

**Location:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows Added This Sweep |
|---|---|
| world_increments | 55 |
| repo_snapshots | 55 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |
