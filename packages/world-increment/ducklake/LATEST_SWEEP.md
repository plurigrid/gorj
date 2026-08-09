# World Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-08-09  
**Run:** world-increment-sweep + hamming-swarm-snapshot

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 26 (key repos, full org has 90+) |
| kubeflow | org | 9 (key repos, full org has 47+) |
| TeglonLabs | org | 5 |
| bmorphism | user | 9 (key repos, full user has 90+) |
| zubyul | user | 6 (key repos, full user has 46+) |
| migalkin | social | 3 |
| DJedamski | social | 1 |
| wasita | social | 3 |
| kristinezheng | social | 1 |
| M1shaaa | social | 1 |
| AustinCStone | social | 2 |
| **Total** | | **66 repo snapshots this run** |

### Notable Activity (pushed 2026-08)
- `plurigrid/gorj` — pushed 2026-08-09, 1742 open issues, GF(3) REPL orchestration
- `plurigrid/place` — pushed 2026-08-09, TeX/bci.place forester preview  
- `kubeflow/pipelines` — pushed 2026-08-09, 4182★, 524 issues
- `kubeflow/docs-agent` — pushed 2026-08-08, AI agent for Kubeflow docs
- `bmorphism/Gay.jl` — pushed 2026-08-07, 188 issues, core GF(3) color library
- `wasita/wm-cv` — pushed 2026-08-07, CV web app
- `wasita/xoxowasita-analysis` — pushed 2026-08-06 (brand new repo)

### GF(3) Color Chain Applied
- `id % 3 == 0` → trit=0 ERGODIC #d3869b  
- `id % 3 == 1` → trit=1 PLUS #b8bb26  
- `id % 3 == 2` → trit=-1 MINUS #cc241d  

### DuckDB Tables
- `world_increments`: 89 total rows (cumulative)
- `repo_snapshots`: 1010 total rows (cumulative)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)

All 28 addresses (alice, bob, A–Z) returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version 6,679,326,878. Balances recorded as **0.0 APT** for all.

This indicates these addresses either:
- Have not initialized an APT CoinStore (never received APT)
- Are using the new Fungible Asset standard instead of legacy CoinStore

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...3cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I–Z | ... | 0.0 each |

### Multisig Contract Probes (5 pairs) — ALL HEALTHY ✓

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ healthy |
| A-G | 0xf56c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

All 5 multisig contracts require 2-of-N signatures and responded to the view function.

### MNX Markets (testnet.mnx.fi)

**Status: SPA — data unavailable via server-side curl**

`testnet.mnx.fi` is a Next.js client-side SPA. Both `/api/markets` and `/api/v1/markets` return the same HTML shell. No server-rendered market data could be extracted. `mnx_snapshots` table has 0 rows for this run.

---

## DuckDB Summary

```
packages/world-increment/ducklake/world-increments.duckdb
  world_increments:   89 rows (cumulative)
  repo_snapshots:   1010 rows (cumulative)
  aptos_snapshots:    28 rows (this run)
  multisig_probes:     5 rows (this run)
  mnx_snapshots:       0 rows (SPA unavailable)
```
