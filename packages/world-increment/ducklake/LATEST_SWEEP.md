# World Increment Sweep + Hamming Snapshot

**Date:** 2026-06-19  
**DB:** `world-increments.duckdb`  
**GF(3) color chain:** ERGODIC #d3869b (trit=0) · PLUS #b8bb26 (trit=1) · MINUS #cc241d (trit=-1)

---

## JOB 1 — GitHub Social Graph Sweep

### Repo Snapshot Summary

| Source | Type | Repos | Stars | Forks |
|---|---|---|---|---|
| plurigrid | org | 100 | 77 | 48 |
| kubeflow | org | 48 | 34,231 | 13,570 |
| TeglonLabs | org | 5 | 2 | 2 |
| bmorphism | user | 100 | 247 | 73 |
| zubyul | user | 49 | 14 | 2 |
| migalkin | user | 19 | 280 | 49 |
| AustinCStone | user | 40 | 108 | 36 |
| wasita | user | 11 | 5 | 1 |
| M1shaaa | user | 8 | 0 | 0 |
| DJedamski | user | 6 | 3 | 1 |
| kristinezheng | user | 5 | 0 | 0 |
| **TOTAL** | | **391** | **35,967** | **13,782** |

### Top Languages

| Language | Repos |
|---|---|
| Python | 81 |
| Rust | 26 |
| JavaScript | 25 |
| TypeScript | 23 |
| Go | 15 |
| HTML | 15 |
| Clojure | 14 |
| Jupyter Notebook | 14 |
| Julia | 9 |
| Zig | 7 |

### Most Recently Pushed

| Repo | Pushed At |
|---|---|
| kubeflow/pipelines-components | 2026-06-19T16:58 |
| kubeflow/community | 2026-06-19T16:50 |
| kubeflow/pipelines | 2026-06-19T16:47 |
| plurigrid/gorj | 2026-06-19T16:11 |
| kubeflow/notebooks | 2026-06-19T16:02 |
| M1shaaa/M1shaaa | 2026-06-19T14:57 |

### GF(3) Distribution (391 increments)

| Trit | Color | Name | Count |
|---|---|---|---|
| 0 | #d3869b | ERGODIC | 130 |
| 1 | #b8bb26 | PLUS | 131 |
| -1 | #cc241d | MINUS | 130 |

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses queried via fullnode.mainnet.aptoslabs.com.
All balances returned 0 APT — accounts have no registered CoinStore or hold zero balance.

| World | Address (truncated) | Balance (APT) |
|---|---|---|
| alice | 0xc793...7b | 0.00 |
| bob | 0x0a3c...5d | 0.00 |
| A–Z (26 wallets) | 0x8699...→0x7af0... | 0.00 each |

### Multisig Contract Probes

All 5 contracts probed via 0x1::multisig_account::num_signatures_required:

| Pair | Address (truncated) | Sigs Required | Status |
|---|---|---|---|
| A-B | 0x0da4...003 | 2 | healthy |
| A-G | 0xf56c...096 | 2 | healthy |
| Y-Z | 0xd3ff...883 | 2 | healthy |
| S-T | 0x3b1c...883 | 2 | healthy |
| V-W | 0x40fa...b6d | 2 | healthy |

All multisigs require 2-of-N signatures and responded successfully.

### MNX Markets (testnet.mnx.fi)

Status: UNAVAILABLE — site returns HTTP 401 (Vercel deployment protection with password authentication). No market data accessible without bypass token.

---

## DuckDB Tables

| Table | Rows |
|---|---|
| world_increments | 391 |
| repo_snapshots | 391 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (blocked) |
