# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-29  
**Run:** world-increment/sweep + hamming-swarm-snapshot

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos | Total Stars | Latest Push |
|--------|------|-------|-------------|-------------|
| kubeflow | org | 49 | 34,434 | 2026-07-29 |
| migalkin | social | 3 | 257 | 2021-06-14 |
| bmorphism | user | 50 | 251 | 2026-07-29 |
| plurigrid | org | 50 | 106 | 2026-07-29 |
| AustinCStone | social | 3 | 106 | 2016-09-19 |
| zubyul | user | 49 | 14 | 2026-07-18 |
| wasita | social | 3 | 4 | 2025-12-10 |
| DJedamski | social | 3 | 3 | 2014-11-03 |
| TeglonLabs | org | 5 | 2 | 2026-06-08 |
| M1shaaa | social | 2 | 0 | 2024-12-31 |
| kristinezheng | social | 2 | 0 | 2023-10-31 |

**Total repos snapshotted this run:** 219

### Notable Repos (most recently pushed)

- **plurigrid/gorj** — pushed 2026-07-29, 1 star, 1493 open issues — "forj + Rama topology nREPL routing + GF(3) gay trit coloring"
- **plurigrid/zig-syrup** — pushed 2026-07-28 — "High-performance Zig OCapN Syrup with CapTP optimizations"
- **plurigrid/asi** — pushed 2026-07-10, 54 stars — "everything is topological chemputer!"
- **bmorphism repos** — 50 repos, latest push 2026-07-29
- **kubeflow** — 49 repos, 34k total stars, active pipeline ML infra

### GF(3) Color Chain (world_increments)

34 increment records generated. Color sequence:
- trit=0 → ERGODIC `#d3869b`
- trit=1 → PLUS `#b8bb26`
- trit=-1 → MINUS `#cc241d`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)

| World | APT Balance |
|-------|-------------|
| alice | 0.43643352 |
| bob | 12.657007 |
| A | 0.051767 |
| B | 0.036256 |
| C | 0.010185 |
| D | 0.011629 |
| E | 0.009372 |
| F | 1.960516 |
| G | 0.000681 |
| H | 0.001681 |
| I | 0.000681 |
| J | 1.895093 |
| K | 0.161961 |
| L | 1.927269 |
| M | 0.112285 |
| N | 0.106121 |
| O | 0.210136 |
| P | 0.140136 |
| Q | 0.10324 |
| R | 0.090217 |
| S | 0.091788 |
| T | 0.073713 |
| U | 0.055773 |
| V | 0.04883299 |
| W | 0.040705 |
| X | 0.042577 |
| Y | 0.044449 |
| Z | 0.024268 |

**Total APT across swarm:** ~18.36 APT  
**Largest balances:** bob (12.66), F (1.96), L (1.93), J (1.90)  
**Method:** `0x1::coin::balance` view function via Aptos mainnet fullnode

### Multisig Contract Probes (5 contracts)

All 5 multisig contracts are **healthy** with `num_signatures_required = 2`:

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428... | 2 | healthy |
| A-G | 0xf56c4a1c... | 2 | healthy |
| Y-Z | 0xd3ffe181... | 2 | healthy |
| S-T | 0x3b1c3ae9... | 2 | healthy |
| V-W | 0x40fad7b4... | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

**Status: SPA unavailable** — testnet.mnx.fi returns a Next.js single-page application with no accessible public JSON API. Market data could not be extracted from the HTML response.

---

## DuckDB Storage Summary

| Table | Rows This Run |
|-------|---------------|
| world_increments | 34 |
| repo_snapshots | 219 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (unavailable note) |

**Database:** `packages/world-increment/ducklake/world-increments.duckdb`
