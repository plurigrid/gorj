# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-25  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Scanned

| Source | Type | Repos | Stars | Forks |
|--------|------|-------|-------|-------|
| kubeflow | org | 48 | 34,254 | 13,583 |
| plurigrid | org | 100 | 77 | 45 |
| bmorphism | user | 100 | 247 | 73 |
| zubyul | user | 49 | 14 | 2 |
| migalkin | social graph | 40 | 108 | 36 |
| AustinCStone | social graph | 19 | 280 | 49 |
| wasita | social graph | 11 | 5 | 1 |
| M1shaaa | social graph | 8 | 0 | 0 |
| DJedamski | social graph | 6 | 3 | 1 |
| TeglonLabs | org | 5 | 2 | 2 |
| kristinezheng | social graph | 5 | 0 | 0 |
| **TOTAL** | | **391** | **35,000** | **13,792** |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,742 | — | 2026-06-18 |
| kubeflow/pipelines | 4,157 | Python | 2026-06-24 |
| kubeflow/spark-operator | 3,128 | Python | 2026-06-24 |
| kubeflow/trainer | 2,121 | Go | 2026-06-24 |
| kubeflow/katib | 1,685 | Python | 2026-06-23 |

### Most Recently Active (today, 2026-06-25)

- `plurigrid/gorj` — 08:10 UTC (808 open issues!)
- `kubeflow/docs-agent` — 05:33 UTC
- `kubeflow/sdk` — 03:04 UTC
- `M1shaaa/M1shaaa` — 02:52 UTC (profile repo active today)
- `bmorphism/Gay.jl` — 00:40 UTC (active today!)

### Notable Signals
- `plurigrid/gorj` has **808 open issues** — highest issue count in the sweep
- `plurigrid/eirobri` has 30 open issues (EiRoBri replay world)
- `bmorphism/Gay.jl` active today — zubyul social graph connection
- All TeglonLabs repos (5) public, jank-crane newest (GF3 convergence maps)

### GF(3) Color Chain

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 130 |
| 1 | PLUS | #b8bb26 | 131 |
| -1 | MINUS | #cc241d | 130 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

28 addresses probed (alice, bob, A–Z) via Aptos mainnet fullnode.

**All 28 returned 404** — no `CoinStore<AptosCoin>` resource initialized on mainnet.  
Balances recorded as NULL in `aptos_snapshots`.

| World | Address |
|-------|---------|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d |
| A | 0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a |
| ... | (A through Z, all 404) |

### Multisig Contract Health

All 5 contracts **healthy** — all require 2-of-2 signatures.

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | YES |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | YES |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | YES |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | YES |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | YES |

### MNX Markets (testnet.mnx.fi)

All API endpoints returned **401 Unauthorized**. Authentication required; no data available.

---

## Database Summary

```
world_increments   391 rows  — GF(3) color-chained repo events
repo_snapshots     391 rows  — full repo metadata snapshot
aptos_snapshots     28 rows  — hamming swarm wallets (all NULL balance)
multisig_probes      5 rows  — 2-of-2 multisig, all healthy
mnx_snapshots        0 rows  — unavailable (401)
```
