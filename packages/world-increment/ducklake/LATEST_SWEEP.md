# World-Increment Sweep + Hamming Swarm Snapshot
**Timestamp:** 2026-07-02 ~21:14 UTC  
**Branch:** world-increment/sweep-2026-07-02

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 50 (of 102 total) |
| kubeflow | org | 10 top by stars (of 48 total) |
| TeglonLabs | org | 5 |
| bmorphism | user | 30 (of 105 total) |
| zubyul | user | 30 (of 49 total) |
| migalkin | social graph | 4 top |
| wasita | social graph | 3 |
| kristinezheng | social graph | 2 |
| AustinCStone | social graph | 3 top |
| M1shaaa | social graph | 2 |
| DJedamski | social graph | 3 |

### Most Active Repos (pushed today, 2026-07-02)
- `plurigrid/gorj` — Clojure, 924 open issues, GF(3) trit orchestration REPL
- `kubeflow/pipelines` — Python, 4167 stars, ML Pipelines for Kubeflow
- `kubeflow/sdk` — Python, Universal AI workloads on Kubernetes
- `wasita/wasita.github.io` — Svelte, personal site updated today
- `bmorphism/Gay.jl` — Julia, 187 open issues, wide-gamut deterministic color sampling

### Top Repos by Stars (this sweep)
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,757 | — |
| kubeflow/pipelines | 4,167 | Python |
| kubeflow/spark-operator | 3,130 | Python |
| kubeflow/trainer | 2,129 | Go |
| kubeflow/katib | 1,688 | Python |
| kubeflow/examples | 1,460 | Jsonnet |
| kubeflow/community-distribution | 1,028 | YAML |
| migalkin/NodePiece | 144 | Python |
| migalkin/StarE | 89 | Python |
| AustinCStone/TextGAN | 92 | Python |
| plurigrid/asi | 28 | HTML |
| migalkin/kgcourse2021 | 25 | HTML |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |

### GF(3) Color Chain (51 new world_increments)
- **ERGODIC** #d3869b (trit=0): 17 events
- **PLUS** #b8bb26 (trit=1): 17 events
- **MINUS** #cc241d (trit=-1): 17 events

### Notable Observations
- `plurigrid/gorj` has **924 open issues** — most active org repo by issue volume
- `plurigrid/eirobri` has 30 open issues, pushed 2026-06-30 (EiRoBri replay world)
- `bmorphism/ocaml-mcp-sdk` (61 stars) — OCaml SDK for MCP using Jane Street's effect library
- TeglonLabs emerging with GF3-themed repos (jank-crane: crane-jank converged-IR hub)
- zubyul/migalkin/wasita/kristinezheng/AustinCStone/M1shaaa/DJedamski all mapped

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, 2026-07-02)
All 28 addresses (alice, bob, A-Z) queried against Aptos mainnet fullnode.
**Result: All wallets returned 0.0 APT.**
The `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource was not found on any address, indicating these are either unfunded/empty accounts or the addresses have not initialized an AptosCoin store on mainnet.

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
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K-Z | (see aptos_snapshots table) | 0.0 each |

### Multisig Contract Probes (5 pairs)
All 5 multisig contracts returned `num_signatures_required = 2`. All **HEALTHY**.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | HEALTHY |
| A-G | 0xf56c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY |
| S-T | 0x3b1c...7883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — `testnet.mnx.fi` and `/api/markets` both returned HTTP 401 Unauthorized. No market data could be extracted. The SPA appears to require authentication. `mnx_snapshots` table left empty this sweep.

---

## DuckDB Ducklake State
**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Total Rows |
|-------|-----------|
| world_increments | 74 |
| repo_snapshots | 995 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

*Note: repo_snapshots and world_increments include cumulative data from previous sweep (2026-06-29) plus this run (51 new repo entries, 28 Aptos wallets, 5 multisig probes).*

---

## Next Steps / Signals
- MNX testnet requires auth — obtain API key or use websocket endpoint
- All Aptos wallets at 0 APT — confirm addresses are correct for mainnet vs testnet
- `plurigrid/gorj` 924 open issues warrants attention
- kubeflow/pipelines actively maintained (pushed today), good signal for ML pipeline community health
