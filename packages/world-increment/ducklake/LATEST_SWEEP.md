# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-19  
**Run type:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Unique Repos | Top Stars |
|--------|------|-------------|-----------|
| plurigrid | org | 168 | 26 (asi) |
| bmorphism | user | 165 | 509 total |
| zubyul | user | 59 | 40 total |
| TeglonLabs | org | 54 | 14 total |
| kubeflow | org | 50 | 15,736 (kubeflow/kubeflow) |
| AustinCStone | user (social graph) | 43 | 92 (TextGAN) |
| wasita | user (social graph) | 32 | 11 total |
| migalkin | user (social graph) | 30 | 144 (NodePiece) |
| kristinezheng | user (social graph) | 18 | 0 total |
| M1shaaa | user (social graph) | 16 | 0 total |
| DJedamski | user (social graph) | 11 | 17 total |
| **TOTAL** | | **646 unique** | |

### Most Recently Pushed Repos

- `plurigrid/gorj` — 2026-06-19 — GF(3) trit coloring + forj REPL orchestration
- `M1shaaa/M1shaaa` — 2026-06-19 — profile config (active today)
- `kubeflow/pipelines` — 2026-06-19 — 4,154 stars
- `wasita/wasita.github.io` — 2026-06-15 — personal site (Svelte)
- `kristinezheng/kristinezheng.github.io` — 2026-06-07 — personal site (HTML)
- `TeglonLabs/jank-crane` — 2026-06-08 — crane-jank C++ GF3 IR hub

### GF(3) Color Chain Distribution

| GF3 Name | Trit | Color | Increment Count |
|----------|------|-------|----------------|
| ERGODIC  | 0    | #d3869b | 134 |
| PLUS     | +1   | #b8bb26 | 135 |
| MINUS    | -1   | #cc241d | 135 |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (alice, bob, A–Z = 28 total)

All 28 wallets queried against Aptos fullnode mainnet.  
**Result:** All returned 0.0 APT — CoinStore resource not initialized or zero balance on all addresses.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob   | 0x0a3c...2d5d | 0.0 |
| A–Z   | (26 addresses) | 0.0 each |

### Multisig Contract Health (5 contracts)

All **HEALTHY** — `num_signatures_required = 2` on every pair.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | HEALTHY |
| A-G | 0xf56c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY |
| S-T | 0x3b1c...7883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — site is behind Vercel deployment protection (visitor password required). No market data accessible.

---

## DuckDB Table Counts

| Table | Rows |
|-------|------|
| world_increments | 404 |
| repo_snapshots | 1,325 (includes pagination dupes) |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (service unavailable) |

---

*Generated: 2026-06-19 by world-increment-sweep + hamming-swarm-snapshot agent*
