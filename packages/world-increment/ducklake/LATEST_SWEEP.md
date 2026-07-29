# World-Increment Sweep + Hamming Snapshot

**Generated:** 2026-07-29 17:15 UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 10 |
| kubeflow | org | 10 |
| TeglonLabs | org | 5 |
| bmorphism | user | 10 |
| zubyul | user | 5 |
| migalkin | user (social) | 5 |
| DJedamski | user (social) | 0 (no public repos) |
| wasita | user (social) | 5 |
| kristinezheng | user (social) | 2 |
| M1shaaa | user (social) | 2 |
| AustinCStone | user (social) | 3 |

**Total new repo_snapshots this run:** 57  
**Cumulative repo_snapshots in DB:** 1,001  
**Cumulative world_increments in DB:** 33  

### GF(3) Color Chain (this run)

| Increment | Source | Trit | Color | Name |
|-----------|--------|------|-------|------|
| 1 | plurigrid | 1 | #b8bb26 | PLUS |
| 2 | kubeflow | -1 | #cc241d | MINUS |
| 3 | TeglonLabs | 0 | #d3869b | ERGODIC |
| 4 | bmorphism | 1 | #b8bb26 | PLUS |
| 5 | zubyul | -1 | #cc241d | MINUS |
| 6 | migalkin | 0 | #d3869b | ERGODIC |
| 7 | wasita | 1 | #b8bb26 | PLUS |
| 8 | kristinezheng | -1 | #cc241d | MINUS |
| 9 | M1shaaa | 0 | #d3869b | ERGODIC |
| 10 | AustinCStone | 1 | #b8bb26 | PLUS |

### Notable GitHub Activity

- **plurigrid/gorj** — pushed today (2026-07-29), 1491 open issues, active
- **plurigrid/zig-syrup** — pushed yesterday (2026-07-28)
- **kubeflow/kubeflow** — 15,796 stars, pushed today
- **kubeflow/pipelines** — 4,170 stars, 498 open issues, pushed today
- **kubeflow/sdk** — 131 stars, pushed today (universal Python SDK)
- **bmorphism/Gay.jl** — pushed 2026-07-21, 188 open issues
- **wasita/wasita.github.io** — pushed 2026-07-21
- **TeglonLabs/jank-crane** — C++ crane-jank converged-IR hub with GF3 convergence maps

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances

| World | APT Balance | Address (truncated) |
|-------|-------------|---------------------|
| alice | 0.43643352 | 0xc793...cc7b |
| **bob** | **12.657007** | 0x0a3c...512d |
| A | 0.051767 | 0x8699...9d7a |
| B | 0.036256 | 0x3f89...b13 |
| C | 0.010185 | 0x38b9...35e |
| D | 0.011629 | 0xf776...fdd1 |
| E | 0.009372 | 0xdc1d...d36 |
| **F** | **1.960516** | 0x18a1...cf71 |
| G | 0.000681 | 0x69a3...f32 |
| H | 0.001681 | 0xce67...300f |
| I | 0.000681 | 0x070f...1fc9 |
| **J** | **1.895093** | 0x4d96...f54 |
| K | 0.161961 | 0xa732...dc4 |
| **L** | **1.927269** | 0x7c2e...ba9 |
| M | 0.112285 | 0x6fed...f2e9 |
| N | 0.106121 | 0xe7dd...1b2c |
| O | 0.210136 | 0x7325...89d |
| P | 0.140136 | 0x6218...948 |
| Q | 0.103240 | 0xac40...89a9 |
| R | 0.090217 | 0x7ce6...6e10 |
| S | 0.091788 | 0xb875...386 |
| T | 0.073713 | 0x3578...588 |
| U | 0.055773 | 0x7586...956 |
| V | 0.048833 | 0xb59d...f2c3 |
| W | 0.040705 | 0x5f32...c7b0 |
| X | 0.042577 | 0xa95c...047d |
| Y | 0.044449 | 0xd8e3...44c4 |
| Z | 0.024268 | 0x7af0...97c |

**Total APT in swarm:** 20.344773 APT  
**Note:** CoinStore resource not exposed; balances queried via `0x1::coin::balance` view function.  
**Heaviest wallets:** bob (12.66), F (1.96), L (1.93), J (1.90)

### Multisig Contract Probes

All 5 multisig contracts are **HEALTHY** (2-of-N signatures required):

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)

Status: **SPA — API unavailable.** The site is a Next.js SPA (HTTP 200 on root/markets), all API path probes (/api/v1/markets, /api/tickers, /v1/markets) return 404 or the SPA shell. No structured market data extractable via HTTP.

---

## DuckDB State

```
world_increments : 33 rows (cumulative)
repo_snapshots   : 1,001 rows (cumulative)  
aptos_snapshots  : 28 rows (this run)
multisig_probes  : 5 rows (this run)
mnx_snapshots    : 0 rows (unavailable)
```
