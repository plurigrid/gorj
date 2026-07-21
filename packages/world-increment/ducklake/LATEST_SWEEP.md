# LATEST_SWEEP.md

**Timestamp:** 2026-07-21 15:13:43 UTC
**Run:** world-increment-sweep + hamming-swarm-snapshot

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org/user | 300 |
| bmorphism | org/user | 300 |
| kubeflow | org/user | 143 |
| TeglonLabs | org/user | 111 |
| AustinCStone | org/user | 98 |
| zubyul | org/user | 97 |
| wasita | org/user | 70 |
| migalkin | org/user | 67 |
| kristinezheng | org/user | 41 |
| M1shaaa | org/user | 37 |
| DJedamski | org/user | 28 |

**Total repo snapshots in DB:** 1292

### GF(3) World Increments (this run)
| ID | GF3 Trit | Color | Name | Source |
|----|---------|-------|------|--------|
| 22 | -1 | `#cc241d` | MINUS | zubyul |
| 21 | 1 | `#b8bb26` | PLUS | wasita |
| 20 | 0 | `#d3869b` | ERGODIC | plurigrid |
| 19 | -1 | `#cc241d` | MINUS | migalkin |
| 18 | 1 | `#b8bb26` | PLUS | kubeflow |
| 17 | 0 | `#d3869b` | ERGODIC | kristinezheng |
| 16 | -1 | `#cc241d` | MINUS | bmorphism |
| 15 | 1 | `#b8bb26` | PLUS | TeglonLabs |
| 14 | 0 | `#d3869b` | ERGODIC | M1shaaa |
| 13 | -1 | `#cc241d` | MINUS | DJedamski |
| 12 | 1 | `#b8bb26` | PLUS | AustinCStone |

**GF(3) chain:** 0→ERGODIC #d3869b, 1→PLUS #b8bb26, -1→MINUS #cc241d

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances
All 28 addresses (A–Z + alice, bob) queried via Aptos mainnet fullnode.

**All 28 Hamming wallets: 0.0 APT** (quiescent / uninitialized state)


### Multisig Contract Probes
All 5 contracts probed via `0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4f428...` | 2 | ✓ healthy |
| A-G | `0xf56c4a1c...` | 2 | ✓ healthy |
| S-T | `0x3b1c3ae9...` | 2 | ✓ healthy |
| V-W | `0x40fad7b4...` | 2 | ✓ healthy |
| Y-Z | `0xd3ffe181...` | 2 | ✓ healthy |

**All multisig contracts healthy: 2-of-N threshold confirmed.**

### MNX Markets (testnet.mnx.fi)
**Status:** Unavailable — Vercel authentication (HTTP 401) required.
API paths `/api/markets` and `/api/v1/markets` both return 401. Data not accessible without credentials.

---

## DuckDB Tables Summary

| Table | Rows (cumulative) |
|-------|-------------------|
| world_increments | see DB |
| repo_snapshots | see DB |
| aptos_snapshots | 28 (this run) |
| multisig_probes | 5 (this run) |
| mnx_snapshots | 1 (unavailable marker) |

**DB location:** `packages/world-increment/ducklake/world-increments.duckdb`
