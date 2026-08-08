# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-08-08  
**Run:** world-increment-sweep + hamming-swarm-snapshot  
**GF3 color chain:** ERGODIC #d3869b / PLUS #b8bb26 / MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 (of 103) |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 (of 106) |
| zubyul | user | 49 |
| migalkin | social | 19 |
| DJedamski | social | 6 |
| wasita | social | 14 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| AustinCStone | social | 30 |

**Total new repos this sweep:** 385  
**Cumulative repo_snapshots in DB:** 1,329  
**Total world_increments:** 409

### Notable Recent Activity

- `plurigrid/gorj` (Clojure) — pushed 2026-08-08 (this repo)
- `plurigrid/place` (TeX) — pushed 2026-08-02
- `plurigrid/zig-syrup` (Zig) — pushed 2026-07-28
- `plurigrid/asi` (HTML, ⭐59) — pushed 2026-07-10
- `TeglonLabs/jank-crane` (C++) — pushed 2026-06-08, GF3 convergence maps
- `wasita/wm-cv` (Svelte) — pushed 2026-08-07
- `M1shaaa/M1shaaa` — pushed 2026-08-08

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (26 + alice/bob)

All 28 addresses returned `resource_not_found` for `CoinStore<AptosCoin>`.  
This indicates APT coin stores are uninitialized (accounts not yet activated on mainnet, or funds held in non-coin-store resources).

| World | Address (truncated) | Balance (APT) | Status |
|-------|---------------------|---------------|--------|
| alice | 0xc793...c7b | 0 | resource_not_found |
| bob | 0x0a3c...2d5d | 0 | resource_not_found |
| A–Z (26) | various | 0 | resource_not_found |

### Multisig Contract Probes

All 5 multisig contracts are **healthy** with 2 signatures required:

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a pure Next.js SPA — all API paths (`/api/markets`, `/api/tickers`, etc.) return HTML instead of JSON. **No REST API is publicly accessible.** Recorded as unavailable.

---

## DuckDB State

```
Tables: world_increments, repo_snapshots, aptos_snapshots, multisig_probes, mnx_snapshots
world_increments: 409 rows
repo_snapshots: 1329 rows
aptos_snapshots: 28 rows (this run)
multisig_probes: 5 rows (this run)
mnx_snapshots: 0 rows (unavailable)
```

Location: `packages/world-increment/ducklake/world-increments.duckdb`
