# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-04-28 05:22:14 UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) color chain:** trit=0 ERGODIC #d3869b · trit=1 PLUS #b8bb26 · trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| # | Source | Type | Repos Snapshotted | Total Stars | GF(3) |
|---|--------|------|------------------:|------------:|-------|
| 1 | plurigrid | org | 100 | 65 | ERGODIC #d3869b |
| 2 | kubeflow | org | 47 | 33,958 | PLUS #b8bb26 |
| 3 | TeglonLabs | org | 4 | 2 | MINUS #cc241d |
| 4 | bmorphism | user | 100 | 246 | ERGODIC #d3869b |
| 5 | zubyul | user | 49 | 14 | PLUS #b8bb26 |
| 6 | migalkin | social | 19 | 278 | MINUS #cc241d |
| 7 | DJedamski | social | 6 | 3 | ERGODIC #d3869b |
| 8 | wasita | social | 10 | 4 | PLUS #b8bb26 |
| 9 | kristinezheng | social | 6 | 0 | MINUS #cc241d |
| 10 | M1shaaa | social | 8 | 0 | ERGODIC #d3869b |
| 11 | AustinCStone | social | 30 | 108 | PLUS #b8bb26 |
| **TOTAL** | | | **379** | **34,678** | |

### Top Active Repos (by push date)

- `kubeflow/trainer` — Go, ★2094, pushed 2026-04-28
- `kubeflow/mcp-apache-spark-history-server` — Python, ★154, pushed 2026-04-28
- `kubeflow/pipelines` — Python, ★4127, pushed 2026-04-28
- `wasita/wasita.github.io` — Svelte, ★1, pushed 2026-04-28
- `M1shaaa/M1shaaa` — pushed 2026-04-28
- `plurigrid/zig-syrup` — Zig, pushed 2026-04-26
- `plurigrid/nash-portal` — Rust, pushed 2026-04-26

### Dominant Languages (plurigrid)

Python, Rust, Julia, Zig, JavaScript, TypeScript, Clojure, TeX

### World-Increment GF(3) Distribution

- **ERGODIC** (trit=0, #d3869b): plurigrid, bmorphism, DJedamski, M1shaaa
- **PLUS** (trit=1, #b8bb26): kubeflow, zubyul, wasita, AustinCStone
- **MINUS** (trit=-1, #cc241d): TeglonLabs, migalkin, kristinezheng

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob   | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...89a | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...7b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

**Note:** All 28 addresses returned 0.0 APT. Accounts may be unfunded or the CoinStore resource is not initialized for these addresses on Aptos mainnet.

### Multisig Contract Probes

All 5 multisig contracts responded successfully and are **HEALTHY** (2-of-N signatures required):

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...003 | 2 | HEALTHY |
| A-G | 0xf56c...096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...883 | 2 | HEALTHY |
| S-T | 0x3b1c...883 | 2 | HEALTHY |
| V-W | 0x40fa...b6d | 2 | HEALTHY |

All pairs require 2 signatures. 5/5 contracts responding = **100% healthy**.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is a Next.js SPA. No public JSON API endpoints found at `/api/markets` or `/api/v1/markets`. Market data not available server-side.

---

## Database Summary

| Table | Rows (this run) |
|-------|-----------------|
| world_increments | 11 (current sweep) |
| repo_snapshots | 379 (current sweep) |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (unavailable marker) |

**Cumulative database:** Contains historical sweeps appended to current run.

---

## GF(3) Color Legend

| Trit | Color Code | Name | Meaning |
|------|-----------|------|---------|
| 0 | #d3869b | ERGODIC | Neutral / self-referential |
| 1 | #b8bb26 | PLUS | Positive / additive |
| -1 | #cc241d | MINUS | Negative / subtractive |
