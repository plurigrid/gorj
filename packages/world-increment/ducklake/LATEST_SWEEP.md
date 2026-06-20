# World-Increment Sweep + Hamming Snapshot
**Sweep Date:** 2026-06-20  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social | 19 |
| AustinCStone | social | 30 |
| wasita | social | 11 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| DJedamski | social | 6 |
| **TOTAL** | | **381** |

### Most Recently Pushed Repos
| Repo | Pushed At |
|------|-----------|
| plurigrid/gorj | 2026-06-20T22:24:48Z |
| kubeflow/pipelines | 2026-06-20T19:12:02Z |
| kubeflow/notebooks | 2026-06-20T17:12:47Z |
| kubeflow/hub | 2026-06-20T15:40:26Z |
| kubeflow/dashboard | 2026-06-20T15:13:23Z |

### GF(3) Color Chain (id%3)
| id | Source | Trit | Color | Name |
|----|--------|------|-------|------|
| 1 | plurigrid | 1 | #b8bb26 | PLUS |
| 2 | kubeflow | -1 | #cc241d | MINUS |
| 3 | bmorphism | 0 | #d3869b | ERGODIC |
| 4 | zubyul | 1 | #b8bb26 | PLUS |
| 5 | migalkin | -1 | #cc241d | MINUS |
| 6 | AustinCStone | 0 | #d3869b | ERGODIC |
| 7 | wasita | 1 | #b8bb26 | PLUS |
| 8 | TeglonLabs | -1 | #cc241d | MINUS |
| 9 | kristinezheng | 0 | #d3869b | ERGODIC |
| 10 | M1shaaa | 1 | #b8bb26 | PLUS |
| 11 | DJedamski | -1 | #cc241d | MINUS |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets: alice, bob, A-Z)
**Result:** All 28 wallets returned null — no `0x1::coin::CoinStore<AptosCoin>` resource found on any address.  
All wallets recorded in `aptos_snapshots` with `balance_apt = 0.0`.

### Multisig Contract Probes (5 pairs)
| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428... | 2 | YES |
| A-G | 0xf56c4a1c... | 2 | YES |
| Y-Z | 0xd3ffe181... | 2 | YES |
| S-T | 0x3b1c3ae9... | 2 | YES |
| V-W | 0x40fad7b4... | 2 | YES |

**All 5 multisig contracts healthy -- all require 2 signatures.**

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** -- testnet.mnx.fi is behind Vercel deployment protection and requires
an authenticated session. No market data could be extracted without a bypass token.
`mnx_snapshots` table is empty this run.

---

## DuckDB Schema Summary

| Table | Rows | Notes |
|-------|------|-------|
| world_increments | 11 | GF3 color-chained source events |
| repo_snapshots | 381 | Full repo metadata |
| aptos_snapshots | 28 | All wallets, balance_apt=0 |
| multisig_probes | 5 | All healthy, sigs_required=2 |
| mnx_snapshots | 0 | Vercel auth required |
