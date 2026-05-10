# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-10

## Sweep Metadata
- **Date:** 2026-05-10
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Branch:** `world-increment/sweep-2026-05-10-1314`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 24 |
| New Increments This Sweep | 12 (ids 13–24) |
| Sources Covered | 3 orgs + 8 users |
| Live Repo Fetch | Rate-limited (unauthenticated; last known: 2026-04-14) |
| plurigrid/gorj (MCP live) | Latest commit: 2026-05-08 |

> **Note:** GitHub REST API returned HTTP 403 (rate limit exceeded, no auth token). Last-known repo counts from the 2026-04-14 sweep are preserved in `repo_snapshots`. The `plurigrid/gorj` repository was queried live via MCP — latest commit `5b28fe0` ("chore: ignore duckdb binary") on 2026-05-08.

---

### GF(3) Color Chain — New Increments (ids 13–24)

| ID | Source | Type | Event | GF3 Trit | Color | Name |
|----|--------|------|-------|-----------|-------|------|
| 13 | plurigrid | org | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 14 | kubeflow | org | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 15 | TeglonLabs | org | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 16 | bmorphism | user | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 17 | zubyul | user | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 18 | migalkin | user | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 19 | DJedamski | user | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 20 | wasita | user | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 21 | kristinezheng | user | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 22 | M1shaaa | user | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 23 | AustinCStone | user | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 24 | plurigrid/gorj | sweep_complete | — | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain continues: `PLUS → MINUS → ERGODIC` (repeating, ids 1–24 = 8 full cycles)

---

### Last-Known Repo Counts (2026-04-14)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 200+ |
| kubeflow | org | 94 |
| TeglonLabs | org | 106 |
| bmorphism | user | 200+ |
| zubyul | user | 48 |
| migalkin | user | 60 |
| DJedamski | user | 22 |
| wasita | user | 60 |
| kristinezheng | user | 36 |
| M1shaaa | user | 32 |
| AustinCStone | user | 86 |

### plurigrid/gorj — Recent Commits (Live via MCP)

| SHA | Date | Message |
|-----|------|---------|
| `5b28fe0` | 2026-05-08 | chore: ignore duckdb binary in repo root |
| `ebf263f` | 2026-04-14 | world-increment ducklake: sync world.duckdb sweep state |
| `b434a43` | 2026-04-14 | Merge sweep state into master |
| `e76792f` | 2026-04-14 | world-increments.duckdb: sync latest sweep state |
| `631518b` | 2026-04-12 | world-increment sweep 2026-04-12: insert id=12 ERGODIC |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances — 2026-05-10 13:14 UTC

All 28 addresses queried via `0x1::coin::balance` view function (new fungible asset model; `CoinStore` resource deprecated for these accounts).

| World | APT Balance | Address (truncated) |
|-------|-------------|---------------------|
| alice | 0.43643352 | `0xc793...4cc7b` |
| bob | 12.65700700 | `0x0a3c...512d5d` |
| A | 0.05176700 | `0x8699...be9d7a` |
| B | 0.03625600 | `0x3f89...cb13` |
| C | 0.01018500 | `0x38b9...535e` |
| D | 0.01162900 | `0xf776...cfdd1` |
| E | 0.00937200 | `0xdc1d...8d36` |
| **F** | **1.96051600** | `0x18a1...cf71` |
| G | 0.00068100 | `0x69a3...c7f32` |
| H | 0.00168100 | `0xce67...300f` |
| I | 0.00068100 | `0x070f...c1fc9` |
| **J** | **1.89509300** | `0x4d96...7f54` |
| K | 0.16196100 | `0xa732...25dc4` |
| **L** | **1.92726900** | `0x7c2e...eba9` |
| M | 0.11228500 | `0x6fed...7f2e9` |
| N | 0.10612100 | `0xe7dd...51b2c` |
| O | 0.21013600 | `0x7325...a89d` |
| P | 0.14013600 | `0x6218...c948` |
| Q | 0.10324000 | `0xac40...c89a9` |
| R | 0.09021700 | `0x7ce6...76e10` |
| S | 0.09178800 | `0xb875...0386` |
| T | 0.07371300 | `0x3578...4588` |
| U | 0.05577300 | `0x7586...9956` |
| V | 0.04883299 | `0xb59d...af2c3` |
| W | 0.04070500 | `0x5f32...c7b0` |
| X | 0.04257700 | `0xa95c...047d` |
| Y | 0.04444900 | `0xd8e3...444c4` |
| Z | 0.02426800 | `0x7af0...197c` |

**Total swarm APT:** ~20.19 APT
**Richest:** bob (12.66 APT), F (1.96 APT), L (1.93 APT), J (1.90 APT)
**Dust wallets (< 0.01 APT):** E, G, H, I

---

### Multisig Contract Probes

All 5 multisig contracts responded to `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | `0x0da4...7003` | 2 | healthy |
| A-G | `0xf56c...0096` | 2 | healthy |
| Y-Z | `0xd3ff...b883` | 2 | healthy |
| S-T | `0x3b1c...7883` | 2 | healthy |
| V-W | `0x40fa...eb6d` | 2 | healthy |

All multisig accounts are 2-of-N — configuration healthy across all 5 pairs.

---

### MNX Markets (testnet.mnx.fi)

**Status: SPA — no JSON API accessible**

`testnet.mnx.fi` is a Next.js client-side rendered application. All probed API paths (`/api/markets`, `/api/v1/markets`, `/api/prices`, `/markets`, `/api/tickers`) return the SPA HTML shell. No market data could be extracted programmatically. Recorded sentinel row in `mnx_snapshots`.

---

## DuckDB Table Counts (post-sweep)

| Table | Total Rows |
|-------|-----------|
| world_increments | 35 |
| repo_snapshots | 956 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |
