# World Increment Sweep + Hamming Snapshot

**Date:** 2026-08-10  
**Run:** world-increment-sweep + hamming-swarm-snapshot

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | GF3 Trit | Color | Repos (top 30) |
|--------|------|----------|-------|----------------|
| plurigrid | org | +1 PLUS #b8bb26 | most recently pushed 2026-08-09 (`place`) |
| kubeflow | org | -1 MINUS #cc241d | most recently pushed 2026-08-09 (`pipelines`) |
| TeglonLabs | org | 0 ERGODIC #d3869b | 5 repos, latest `jank-crane` 2026-06-08 |
| bmorphism | user | +1 PLUS #b8bb26 | most recently pushed 2026-08-07 (`Gay.jl`) |
| zubyul | user | -1 MINUS #cc241d | most recently pushed 2026-07-18 (`from-possible-worlds`) |
| migalkin | user | 0 ERGODIC #d3869b | social graph (no public access) |
| DJedamski | user | +1 PLUS #b8bb26 | social graph (no public access) |
| wasita | user | -1 MINUS #cc241d | social graph (no public access) |
| kristinezheng | user | 0 ERGODIC #d3869b | social graph (no public access) |
| M1shaaa | user | +1 PLUS #b8bb26 | social graph (no public access) |
| AustinCStone | user | -1 MINUS #cc241d | social graph (no public access) |

### Top Repos by Stars (this sweep)

| Org/User | Repo | Stars | Last Pushed |
|----------|------|-------|-------------|
| kubeflow | kubeflow | 15,808 | 2026-07-10 |
| kubeflow | pipelines | 4,180 | 2026-08-09 |
| kubeflow | spark-operator | 3,146 | 2026-08-09 |
| kubeflow | trainer | 2,177 | 2026-08-08 |

### Most Recently Active Repos

| Source | Repo | Pushed |
|--------|------|--------|
| plurigrid | place | 2026-08-09 |
| kubeflow | pipelines | 2026-08-09 |
| kubeflow | spark-operator | 2026-08-09 |
| bmorphism | Gay.jl | 2026-08-07 |
| TeglonLabs | jank-crane | 2026-06-08 |
| zubyul | from-possible-worlds | 2026-07-18 |

### DuckDB Tables Updated

- `world_increments`: 34 total records (11 added this sweep)
- `repo_snapshots`: 1,069 total rows (125 added this sweep: 30×plurigrid + 30×kubeflow + 5×TeglonLabs + 30×bmorphism + 30×zubyul)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (2026-08-10)

**Total swarm APT: 20.3448 APT across 28 wallets**

| World | Address (short) | Balance (APT) |
|-------|----------------|---------------|
| bob | 0x0a3c...512d | **12.6570** |
| F | 0x18a1...cf71 | 1.9605 |
| L | 0x7c2e...ba9 | 1.9273 |
| J | 0x4d96...7f54 | 1.8951 |
| alice | 0xc793...cc7b | 0.4364 |
| O | 0x7325...89d | 0.2101 |
| K | 0xa732...dc4 | 0.1620 |
| P | 0x6218...948 | 0.1401 |
| M | 0x6fed...2e9 | 0.1123 |
| N | 0xe7dd...b2c | 0.1061 |
| Q | 0xac40...89a9 | 0.1032 |
| R | 0x7ce6...6e10 | 0.0902 |
| S | 0xb875...386 | 0.0918 |
| T | 0x3578...588 | 0.0737 |
| U | 0x7586...956 | 0.0558 |
| A | 0x8699...d7a | 0.0518 |
| X | 0xa95c...047d | 0.0426 |
| Y | 0xd8e3...44c4 | 0.0444 |
| V | 0xb59d...f2c3 | 0.0488 |
| W | 0x5f32...7b0 | 0.0407 |
| B | 0x3f89...b13 | 0.0363 |
| Z | 0x7af0...97c | 0.0243 |
| D | 0xf776...dd1 | 0.0116 |
| C | 0x38b9...35e | 0.0102 |
| E | 0xdc1d...d36 | 0.0094 |
| H | 0xce67...00f | 0.0017 |
| G | 0x69a3...f32 | 0.0007 |
| I | 0x070f...fc9 | 0.0007 |

> Note: All balances fetched via `0x1::coin::balance` view function on Aptos mainnet.

### Multisig Contract Probes

All 5 multisig pairs probed healthy (2-of-N threshold):

| Pair | Contract Address | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c...096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ff...883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c...883 | 2 | ✅ HEALTHY |
| V-W | 0x40fa...b6d | 2 | ✅ HEALTHY |

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — Next.js SPA with no public REST API endpoints. `/api/markets` and `/api/v1/markets` return no data. Market data requires client-side JavaScript rendering.

---

## DuckDB Summary

Database: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 34 |
| repo_snapshots | 1,069 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |
