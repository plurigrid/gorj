# World-Increment Sweep + Hamming Snapshot — 2026-07-25

## Sweep Metadata
- **Date:** 2026-07-25
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried (11 increments, GF3 color chain)

| ID | Source | Type | Repos | GF3 Trit | Color | Name |
|----|--------|------|-------|-----------|-------|------|
| 1 | plurigrid | org | 100 | +1 | `#b8bb26` | **PLUS** |
| 2 | kubeflow | org | 49 | -1 | `#cc241d` | **MINUS** |
| 3 | bmorphism | user | 100 | 0 | `#d3869b` | **ERGODIC** |
| 4 | zubyul | user | 49 | +1 | `#b8bb26` | **PLUS** |
| 5 | TeglonLabs | org | 5 | -1 | `#cc241d` | **MINUS** |
| 6 | migalkin | user (social) | 19 | 0 | `#d3869b` | **ERGODIC** |
| 7 | DJedamski | user (social) | 6 | +1 | `#b8bb26` | **PLUS** |
| 8 | wasita | user (social) | 12 | -1 | `#cc241d` | **MINUS** |
| 9 | kristinezheng | user (social) | 5 | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user (social) | 8 | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user (social) | 20 | -1 | `#cc241d` | **MINUS** |

**GF(3) chain:** `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

**This sweep:** 313 repo snapshots, 11 world increments  
**DB cumulative:** 1257 repo snapshots, 34 world increments

### Top Repos by Stars (This Sweep)
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,793 | — | 2026-07-10 |
| kubeflow/pipelines | 4,170 | Python | 2026-07-25 |
| kubeflow/spark-operator | 3,143 | Python | 2026-07-25 |
| kubeflow/trainer | 2,153 | Go | 2026-07-25 |
| kubeflow/katib | 1,692 | Python | 2026-07-22 |
| kubeflow/examples | 1,461 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1,029 | YAML | 2026-07-24 |
| migalkin/NodePiece | 144 | Python | 2021-06-14 |
| AustinCStone/TextGAN | 92 | Python | 2019-01-30 |
| migalkin/StarE | 89 | Python | 2020-09-17 |

### Notable Observations
- **kubeflow/pipelines** pushed 2026-07-25 (active today) — star count up from 4119 → 4170 vs April sweep
- **TeglonLabs/jank-crane** (C++) — new since April sweep: "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps"
- **wasita/pnas-typst-template** — new repo (2026-07-16), likely recent academic work
- **AustinCStone/byteruckus** — new repo (2026-07-15)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 28 wallets)

All 28 wallets queried at 1-second intervals. All return 0.0 APT — accounts may lack initialized CoinStore resources or hold zero balance.

| World | Balance (APT) |
|-------|---------------|
| alice, bob, A–Z (all) | **0.0** |

> API endpoint: `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

### Multisig Contract Probes — 5/5 HEALTHY ✓

All 5 probed multisig contracts responded correctly with `num_signatures_required = 2`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...987003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a1c...c0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — testnet.mnx.fi is a Next.js SPA (dpl_var6UYTwReYK9tifCBPZSQQcg1fZ). All paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`, `/markets`) return the SPA HTML shell — no JSON data endpoints exposed publicly.

---

## DuckDB Table Counts
| Table | Rows (cumulative) |
|-------|-------------------|
| world_increments | 34 |
| repo_snapshots | 1257 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (unavailable marker) |

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
