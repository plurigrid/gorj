# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-06-15  
**Run:** world-increment-sweep + hamming-swarm-snapshot agent

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos | Stars | Most Recent Push |
|--------|------|-------|-------|-----------------|
| plurigrid | org | 100 | 77 | 2026-06-15 (gorj) |
| kubeflow | org | 48 | ~103K+ | 2026-06-15 (pipelines, trainer, katib) |
| TeglonLabs | org | 5 | 2 | 2026-06-08 (jank-crane) |
| bmorphism | user | 100 | 273 | 2026-06-15 |
| zubyul | user | 49 | 230 | 2026-06-15 |
| migalkin | user | 19 | 281 | 2025-08-04 (kgcourse2021) |
| DJedamski | user | 6 | 4 | 2018-03-07 |
| wasita | user | 11 | 5 | 2026-06-15 (wasita.github.io) |
| kristinezheng | user | 5 | 0 | 2026-06-07 |
| M1shaaa | user | 8 | 0 | 2026-06-15 (profile) |
| AustinCStone | user | 40 | 188 | recent |

**Total unique repos: 391**

### Notable Repos (by stars)

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,726 | 2026-06-11 |
| kubeflow/pipelines | Python | 4,154 | 2026-06-15 |
| kubeflow/spark-operator | Python | 3,127 | 2026-06-15 |
| kubeflow/trainer | Go | 2,115 | 2026-06-15 |
| migalkin/NodePiece | Python | 144 | 2022-02-02 |
| migalkin/StarE | Python | 89 | 2023-12-01 |
| plurigrid/asi | HTML | 26 | 2026-06-10 |
| migalkin/kgcourse2021 | HTML | 25 | 2025-08-04 |
| TeglonLabs/jank-crane | C++ | 0 | 2026-06-08 |
| plurigrid/gorj | Clojure | 0 | 2026-06-15 |

### GF(3) Color Chain (world_increments this sweep)

| ID | Source | Trit | Color | Name |
|----|--------|------|-------|------|
| 1 | AustinCStone | +1 | #b8bb26 | PLUS |
| 2 | DJedamski | -1 | #cc241d | MINUS |
| 3 | M1shaaa | 0 | #d3869b | ERGODIC |
| 4 | TeglonLabs | +1 | #b8bb26 | PLUS |
| 5 | bmorphism | -1 | #cc241d | MINUS |
| 6 | kristinezheng | 0 | #d3869b | ERGODIC |
| 7 | kubeflow | +1 | #b8bb26 | PLUS |
| 8 | migalkin | -1 | #cc241d | MINUS |
| 9 | plurigrid | 0 | #d3869b | ERGODIC |
| 10 | wasita | +1 | #b8bb26 | PLUS |
| 11 | zubyul | -1 | #cc241d | MINUS |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (28 addresses)

All addresses queried via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
No address returned an active CoinStore resource — all balances reported as 0 APT.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793acdec12b4a...cc7b | 0.0 |
| bob | 0x0a3c00c58fdf90...2d5d | 0.0 |
| A | 0x8699edc0960dd5...9d7a | 0.0 |
| B | 0x3f892ebe6e4516...b13 | 0.0 |
| C | 0x38b99e63ada9b6...35e | 0.0 |
| D | 0xf77656248f64d5...dd1 | 0.0 |
| E | 0xdc1d9d533bac35...d36 | 0.0 |
| F | 0x18a14b5b4bec11...f71 | 0.0 |
| G | 0x69a394c0b0ac84...f32 | 0.0 |
| H | 0xce67c327a7844e...00f | 0.0 |
| I | 0x070fe5d74e4eda...fc9 | 0.0 |
| J | 0x4d964db8f53837...f54 | 0.0 |
| K | 0xa732040a6b0d55...dc4 | 0.0 |
| L | 0x7c2eaeafad9725...ba9 | 0.0 |
| M | 0x6fed37a7553ef1...2e9 | 0.0 |
| N | 0xe7dde6da0a65f5...b2c | 0.0 |
| O | 0x73252b6011a751...89d | 0.0 |
| P | 0x6218792de4a9bc...948 | 0.0 |
| Q | 0xac40fa50b81b4c...89a9 | 0.0 |
| R | 0x7ce605cc8fda4f...e10 | 0.0 |
| S | 0xb8753014e4888e...386 | 0.0 |
| T | 0x35781dc0e42fef...588 | 0.0 |
| U | 0x75860da47565f6...956 | 0.0 |
| V | 0xb59dd8170321df...2c3 | 0.0 |
| W | 0x5f32aef70f5ba5...7b0 | 0.0 |
| X | 0xa95cbbd1165489...47d | 0.0 |
| Y | 0xd8e32848f1dffa...44c4 | 0.0 |
| Z | 0x7af0ef6e1bd706...97c | 0.0 |

**Interpretation:** None of these addresses have active APT holdings on mainnet via the standard coin module as of this sweep.

### Multisig Contract Probes

All 5 multisig contracts responded successfully via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...7003 | 2 | HEALTHY |
| A-G | 0xf56c4a1c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ffe181...b883 | 2 | HEALTHY |
| S-T | 0x3b1c3ae9...7883 | 2 | HEALTHY |
| V-W | 0x40fad7b4...eb6d | 2 | HEALTHY |

**5/5 multisig contracts healthy. All require 2-of-N signatures.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Vercel deployment protection active on all API paths (`/`, `/api/markets`, `/api/v1/markets`). Returns 401 auth challenge requiring bypass token or trusted OIDC source. No market data captured.

---

## DuckDB Ducklake State

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Cumulative Rows | This Sweep |
|-------|----------------|------------|
| world_increments | 34 | +11 |
| repo_snapshots | 1335+ | +391 |
| aptos_snapshots | 28 | +28 |
| multisig_probes | 5 | +5 |
| mnx_snapshots | 0 | 0 (unavailable) |

Historical data present from 2026-04-10 sweep.

---

## Key Findings

1. **kubeflow org very active** — pipelines, spark-operator, trainer, and katib all pushed today (2026-06-15)
2. **wasita and M1shaaa** — both pushed today, active social graph nodes
3. **TeglonLabs/jank-crane** — new C++ repo with GF3 convergence maps (pushed 2026-06-08), most recent TeglonLabs activity
4. **Hamming swarm wallets** — all 28 addresses at 0 APT; no active mainnet holdings
5. **All 5 multisig contracts** — healthy, each requiring 2 signatures
6. **MNX testnet** — inaccessible (Vercel-protected deployment)
