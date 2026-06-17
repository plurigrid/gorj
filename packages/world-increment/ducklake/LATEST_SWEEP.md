# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-17  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) color chain:** ERGODIC #d3869b (trit=0) · PLUS #b8bb26 (trit=1) · MINUS #cc241d (trit=-1)

---

## JOB 1 — GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos | Stars | Most Recent Push |
|---|---|---|---|---|
| bmorphism | user | 100 | 247 | 2026-06-17T00:44:37Z |
| plurigrid | org | 100 | 77 | 2026-06-17T10:15:37Z |
| zubyul | user | 49 | 14 | 2026-04-24T05:56:17Z |
| kubeflow | org | 48 | 34,216 | 2026-06-17T10:59:49Z |
| AustinCStone | user | 40 | 108 | 2026-02-11T01:10:54Z |
| migalkin | user (zubyul social) | 19 | 280 | 2025-08-04T03:01:46Z |
| wasita | user (zubyul social) | 11 | 5 | 2026-06-15T20:15:02Z |
| M1shaaa | user (zubyul social) | 8 | 0 | 2026-06-17T03:43:28Z |
| DJedamski | user (zubyul social) | 6 | 3 | 2018-03-07T12:36:09Z |
| TeglonLabs | org | 5 | 2 | 2026-06-08T19:03:03Z |
| kristinezheng | user (zubyul social) | 5 | 0 | 2026-06-07T22:52:50Z |

**Total repos snapshotted:** 391  
**Total world-increment entries:** 391 (GF3 color-chained)

### Notable Activity
- **kubeflow** dominates star count (34,216 across 48 repos) — pushed today
- **plurigrid** most recently pushed today at 10:15 UTC
- **bmorphism** and **M1shaaa** both pushed within last 24h
- **TeglonLabs/jank-crane** (C++, 2026-06-08): GF3-convergence-maps project
- **wasita/wasita.github.io** (Svelte) — pushed 2026-06-15, 8 open issues

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses queried (alice, bob, A–Z). All returned **0 APT** — accounts either have no CoinStore resource or hold no APT.

### Multisig Contract Probes

All 5 probes returned **2 sigs required** — healthy 2-of-N across the board.

| Pair | Address | Sigs Required | Status |
|---|---|---|---|
| A-B | 0x0da4...7003 | 2 | healthy |
| A-G | 0xf56c...0096 | 2 | healthy |
| Y-Z | 0xd3ff...b883 | 2 | healthy |
| S-T | 0x3b1c...7883 | 2 | healthy |
| V-W | 0x40fa...eb6d | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

Endpoint is Vercel-auth-gated — no market data available. `mnx_snapshots` table is empty this sweep.

---

## DuckDB Table Summary

| Table | Rows |
|---|---|
| world_increments | 391 |
| repo_snapshots | 391 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (auth-gated) |
