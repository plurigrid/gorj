# World Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-06-21  
**GF(3) Color Chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d → …

---

## JOB 1: GitHub Social Graph Sweep

### Summary
| Source | Type | Repos Snapshotted | Latest Push |
|--------|------|-------------------|-------------|
| plurigrid | org | 100 | 2026-06-21 |
| kubeflow | org | 48 | 2026-06-21 |
| TeglonLabs | org | 5 | 2026-06-08 |
| bmorphism | user | 100 | 2026-06-21 |
| zubyul | user | 49 | 2026-04-24 |
| migalkin | user | 19 | 2025-08-04 |
| DJedamski | user | 6 | 2018-03-07 |
| wasita | user | 1 | 2026-06-19 |
| kristinezheng | user | 5 | 2026-06-07 |
| M1shaaa | user | 8 | 2026-06-21 |
| AustinCStone | user | 40 | 2026-02-11 |
| **TOTAL** | | **381** | |

### Notable Repos (most recently pushed)
- `plurigrid/*` — 100 repos, most active today (2026-06-21)
- `bmorphism/*` — 100 repos, active today
- `kubeflow/*` — 48 repos, active today
- `TeglonLabs/jank-crane` — C++, GF3 convergence maps (pushed 2026-06-08)
- `M1shaaa/M1shaaa` — profile config, pushed today (2026-06-21)
- `wasita/proj-template` — pushed 2026-06-19

### DuckDB Tables Updated
- `world_increments`: 11 new increment rows (this sweep)
- `repo_snapshots`: 381 new rows (this sweep)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
**Sweep time:** 2026-06-21  
**Result:** All 28 addresses (alice, bob, A-Z) returned `null` — no APT `CoinStore` resource found for any address. Accounts are either unfunded or not initialized on Aptos mainnet.

| Label | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | null |
| bob | 0x0a3c...2d5d | null |
| A-Z | (26 addresses) | null (all) |

### Multisig Contract Probes
All 5 probed multisig accounts are **healthy** (responsive, 2-of-N configured).

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | healthy |
| A-G | 0xf56c...0096 | 2 | healthy |
| Y-Z | 0xd3ff...b883 | 2 | healthy |
| S-T | 0x3b1c...7883 | 2 | healthy |
| V-W | 0x40fa...eb6d | 2 | healthy |

### MNX Markets (testnet.mnx.fi)
**Status:** UNAVAILABLE — both `/api/markets` endpoint and root SPA returned no data (connection refused or network policy blocks outbound access to testnet.mnx.fi).

---

## DuckDB Ducklake Status
**Path:** `packages/world-increment/ducklake/world-increments.duckdb`

```
Tables:
  world_increments  — GF(3) color-chained event log
  repo_snapshots    — GitHub repo metadata snapshots
  aptos_snapshots   — Hamming swarm wallet balances
  multisig_probes   — Multisig contract health checks
  mnx_snapshots     — MNX market tickers (empty, unavailable)
```

### GF(3) Color Chain (this sweep)
| Increment ID | Source | GF3 Trit | Color | Name |
|---|---|---|---|---|
| 1 | plurigrid | 1 | #b8bb26 | PLUS |
| 2 | kubeflow | -1 | #cc241d | MINUS |
| 3 | TeglonLabs | 0 | #d3869b | ERGODIC |
| 4 | bmorphism | 1 | #b8bb26 | PLUS |
| 5 | zubyul | -1 | #cc241d | MINUS |
| 6 | migalkin | 0 | #d3869b | ERGODIC |
| 7 | DJedamski | 1 | #b8bb26 | PLUS |
| 8 | wasita | -1 | #cc241d | MINUS |
| 9 | kristinezheng | 0 | #d3869b | ERGODIC |
| 10 | M1shaaa | 1 | #b8bb26 | PLUS |
| 11 | AustinCStone | -1 | #cc241d | MINUS |
