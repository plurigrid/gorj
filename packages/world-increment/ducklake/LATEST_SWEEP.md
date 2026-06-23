# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-23T04:30 UTC  
**GF(3) chain:** id%3==0 → trit=0 ERGODIC #d3869b | id%3==1 → trit=1 PLUS #b8bb26 | id%3==2 → trit=-1 MINUS #cc241d  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 (14 stored as top-active) |
| kubeflow | org | 48 (13 stored) |
| TeglonLabs | org | 5 (all) |
| bmorphism | user | 100 (9 stored) |
| zubyul | user | 49 (5 stored) |
| migalkin | social | 19 (3 stored) |
| wasita | social | 11 (2 stored) |
| AustinCStone | social | 40 (2 stored) |
| kristinezheng | social | 5 (1 stored) |
| M1shaaa | social | 8 (1 stored) |
| DJedamski | social | 6 (1 stored) |

**Total repo_snapshots inserted:** 56  
**Total world_increments (cumulative):** 79

### Notable Activity (pushed within 7 days of 2026-06-23)

| Repo | Lang | Stars | Pushed |
|------|------|-------|--------|
| plurigrid/gorj | Clojure | 0 | 2026-06-23T04:09 |
| plurigrid/eirobri | Clojure | 0 | 2026-06-23T02:23 |
| kubeflow/sdk | Python | 120 | 2026-06-23T03:05 |
| kubeflow/pipelines | Python | 4157 | 2026-06-23T02:51 |
| kubeflow/trainer | Go | 2118 | 2026-06-22T23:34 |
| bmorphism/Gay.jl | Julia | 2 | 2026-06-23T00:40 |
| kubeflow/katib | Python | 1685 | 2026-06-22T20:07 |
| kubeflow/mpi-operator | Go | 528 | 2026-06-22T18:08 |
| kubeflow/community | Jupyter | 194 | 2026-06-22T18:12 |
| plurigrid/place | TeX | 1 | 2026-06-20T00:28 |
| wasita/proj-template | null | 0 | 2026-06-19T21:22 |
| TeglonLabs/jank-crane | C++ | 0 | 2026-06-08T19:03 |

### GF(3) Color Distribution (this sweep, 56 new increments)

- trit=1 PLUS #b8bb26: ~19 increments
- trit=-1 MINUS #cc241d: ~19 increments
- trit=0 ERGODIC #d3869b: ~18 increments

### Top Stars (all sources)

| Repo | Stars |
|------|-------|
| kubeflow/kubeflow | 15,740 |
| kubeflow/pipelines | 4,157 |
| kubeflow/spark-operator | 3,128 |
| kubeflow/trainer | 2,118 |
| kubeflow/katib | 1,685 |
| kubeflow/examples | 1,460 |
| kubeflow/community-distribution | 1,027 |
| kubeflow/arena | 813 |
| kubeflow/kale | 694 |
| migalkin/NodePiece | 144 |
| AustinCStone/TextGAN | 92 |
| migalkin/StarE | 89 |
| bmorphism/ocaml-mcp-sdk | 61 |
| plurigrid/asi | 26 |
| bmorphism/anti-bullshit-mcp-server | 23 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

Queried via `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

All 28 addresses returned **0.0 APT** — accounts either have no registered CoinStore or hold zero balance.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…512d | 0.0 |
| A | 0x8699…9d7a | 0.0 |
| B | 0x3f89…cb13 | 0.0 |
| C | 0x38b9…535e | 0.0 |
| D | 0xf776…fdd1 | 0.0 |
| E | 0xdc1d…8d36 | 0.0 |
| F | 0x18a1…cf71 | 0.0 |
| G | 0x69a3…f32 | 0.0 |
| H | 0xce67…300f | 0.0 |
| I | 0x070f…1fc9 | 0.0 |
| J | 0x4d96…7f54 | 0.0 |
| K | 0xa732…5dc4 | 0.0 |
| L | 0x7c2e…eba9 | 0.0 |
| M | 0x6fed…2e9 | 0.0 |
| N | 0xe7dd…1b2c | 0.0 |
| O | 0x7325…a89d | 0.0 |
| P | 0x6218…c948 | 0.0 |
| Q | 0xac40…89a9 | 0.0 |
| R | 0x7ce6…6e10 | 0.0 |
| S | 0xb875…0386 | 0.0 |
| T | 0x3578…4588 | 0.0 |
| U | 0x7586…9956 | 0.0 |
| V | 0xb59d…f2c3 | 0.0 |
| W | 0x5f32…c7b0 | 0.0 |
| X | 0xa95c…047d | 0.0 |
| Y | 0xd8e3…44c4 | 0.0 |
| Z | 0x7af0…197c | 0.0 |

**Total APT across swarm:** 0.0

### Multisig Contract Probes

All 5 multisig contracts are **healthy** (sigs_required=2):

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4…7003 | 2 | ✓ |
| A-G | 0xf56c…0096 | 2 | ✓ |
| Y-Z | 0xd3ff…b883 | 2 | ✓ |
| S-T | 0x3b1c…7883 | 2 | ✓ |
| V-W | 0x40fa…eb6d | 2 | ✓ |

**All multisigs require 2-of-N signatures — consistent quorum across all pairs.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` and all probed API paths (`/api/markets`, `/api/v1/markets`) are protected by Vercel Deployment Protection. Authentication required (visitor password). No market data accessible without bypass token.

---

## DuckDB Schema

```sql
world_increments  — 79 rows cumulative (GF3-colored)
repo_snapshots    — 56 rows (this sweep)
aptos_snapshots   — 28 rows (all 0.0 APT)
multisig_probes   —  5 rows (all healthy, sigs=2)
mnx_snapshots     —  1 row (unavailability record)
```

## Key Findings

1. **plurigrid/gorj** most active plurigrid repo (pushed today at 04:09Z, 757 open issues)
2. **kubeflow** ecosystem highly active — sdk, pipelines, trainer, katib, mpi-operator all pushed within 24h
3. **TeglonLabs/jank-crane** new repo (C++): GF3 convergence maps + crane-jank IR hub
4. **bmorphism/Gay.jl** updated today (00:40Z) — GF3 color library actively maintained
5. **All 5 Hamming-pair multisig contracts healthy** with uniform 2-sig requirement
6. **Hamming swarm wallets** — all 28 showing 0 APT (uninitialized CoinStore resources or zero balances)
7. **MNX testnet** behind Vercel auth — requires visitor password bypass token for market data access

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
