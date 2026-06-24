# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-24  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | GF(3) Trit | Color | Name | Repos |
|--------|------|-----------|-------|------|-------|
| plurigrid | org | -1 (2) | #cc241d | MINUS | 100 |
| migalkin | user | 1 | #b8bb26 | PLUS | 100 |
| bmorphism | user | 1 | #b8bb26 | PLUS | 49 |
| kubeflow | org | 0 | #d3869b | ERGODIC | 48 |
| AustinCStone | user | 0 | #d3869b | ERGODIC | 40 |
| zubyul | user | -1 (2) | #cc241d | MINUS | 19 |
| M1shaaa | user (social) | 1 | #b8bb26 | PLUS | 8 |
| DJedamski | user (social) | -1 (2) | #cc241d | MINUS | 6 |
| TeglonLabs | org | 1 | #b8bb26 | PLUS | 5 |
| kristinezheng | user (social) | 0 | #d3869b | ERGODIC | 5 |

**Total repos snapshotted: 380**

### Notable Repos (plurigrid)

- `plurigrid/gorj` — forj + Rama topology nREPL routing + GF(3) gay trit coloring (pushed 2026-06-24)
- `plurigrid/asi` — everything is topological chemputer! stars:26
- `plurigrid/eirobri` — EiRoBri replay world (pushed 2026-06-23)
- `plurigrid/nash-portal` — NASH token TUI in the browser — ratzilla WASM + GeckoTerminal OHLCV
- `plurigrid/nanoclj-zig` — NaN-boxed Clojure interpreter in Zig 0.15, interaction nets, GF(3) trit conservation

### Notable Repos (TeglonLabs)

- `TeglonLabs/jank-crane` — crane-jank converged-IR hub: GF3 convergence maps (pushed 2026-06-08, C++)
- `TeglonLabs/mathpix-gem` — Math OCR Ruby gem, stars:2, 11 open issues

### DuckDB Tables

- `world_increments` — 10 rows (one per source, GF3 color chain)
- `repo_snapshots` — 380 rows

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A-Z) returned **0.0 APT** — accounts empty or not registered on mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793acd...4cc7b | 0.0 |
| bob | 0x0a3c00c...512d5d | 0.0 |
| A-Z | (see aptos_snapshots table) | 0.0 each |

### Multisig Contract Probes (Aptos Mainnet)

All 5 multisig contracts are **HEALTHY** with 2-of-2 signatures required.

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428...987003 | 2 | YES |
| A-G | 0xf56c4a1c...c0096 | 2 | YES |
| Y-Z | 0xd3ffe181...5b883 | 2 | YES |
| S-T | 0x3b1c3ae9...d7883 | 2 | YES |
| V-W | 0x40fad7b4...0eb6d | 2 | YES |

### MNX Markets (testnet.mnx.fi)

**Unavailable** — testnet endpoint requires Vercel deployment authentication. No market data could be retrieved. `mnx_snapshots` table has 0 rows.

### DuckDB Tables

- `aptos_snapshots` — 28 rows (all 0.0 APT)
- `multisig_probes` — 5 rows (all healthy, 2-of-2)
- `mnx_snapshots` — 0 rows (endpoint auth-blocked)

---

## GF(3) Color Chain Legend

| id mod 3 | Trit | Color | Name | Hex |
|----------|------|-------|------|-----|
| 0 | 0 | ERGODIC | rose | #d3869b |
| 1 | +1 | PLUS | yellow-green | #b8bb26 |
| 2 | -1 | MINUS | red | #cc241d |
