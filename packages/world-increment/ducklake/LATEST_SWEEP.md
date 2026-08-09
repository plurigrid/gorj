# World-Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-08-09  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources queried

| Source | Type | Repos captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social-graph | 19 |
| wasita | social-graph | 14 |
| AustinCStone | social-graph | 41 |
| DJedamski | social-graph | 6 |
| kristinezheng | social-graph | 5 |
| M1shaaa | social-graph | 8 |

**Total repo snapshots:** 1,269 (stored in `repo_snapshots` table)  
**World increments:** 34 (one per source, GF(3) color-chained)

### GF(3) color chain applied
- `id % 3 == 0` → trit=0, ERGODIC `#d3869b`
- `id % 3 == 1` → trit=1, PLUS `#b8bb26`
- `id % 3 == 2` → trit=-1, MINUS `#cc241d`

### Notable repos (recent activity, 2026)
- **TeglonLabs/jank-crane** (C++, pushed 2026-06-08): crane-jank converged-IR hub with GF3 convergence maps
- **wasita/wm-cv** (Svelte, pushed 2026-08-07): Academic CV SPA
- **wasita/xoxowasita-analysis** (Python, pushed 2026-08-06): fresh analysis repo
- **AustinCStone/byteruckus** (HTML, pushed 2026-07-15): new project

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, `coin::balance` view)

| World | Address (short) | APT Balance |
|-------|----------------|-------------|
| bob | 0x0a3c…12d5 | 12.6570 |
| F | 0x18a1…cf71 | 1.9605 |
| L | 0x7c2e…ba9 | 1.9273 |
| J | 0x4d96…f54 | 1.8951 |
| alice | 0xc793…c7b | 0.4364 |
| K | 0xa732…dc4 | 0.1620 |
| O | 0x7325…89d | 0.2101 |
| P | 0x6218…948 | 0.1401 |
| M | 0x6fed…2e9 | 0.1123 |
| N | 0xe7dd…b2c | 0.1061 |
| Q | 0xac40…89a | 0.1032 |
| R | 0x7ce6…e10 | 0.0902 |
| S | 0xb875…386 | 0.0918 |
| T | 0x3578…588 | 0.0737 |
| U | 0x7586…956 | 0.0558 |
| A | 0x8699…a7a | 0.0518 |
| B | 0x3f89…b13 | 0.0363 |
| V | 0xb59d…b2c | 0.0488 |
| W | 0x5f32…b0 | 0.0407 |
| X | 0xa95c…47d | 0.0426 |
| Y | 0xd8e3…c4 | 0.0444 |
| Z | 0x7af0…97c | 0.0243 |
| C | 0x38b9…53e | 0.0102 |
| D | 0xf776…dd1 | 0.0116 |
| E | 0xdc1d…d36 | 0.0094 |
| H | 0xce67…00f | 0.0017 |
| G | 0x69a3…f32 | 0.0007 |
| I | 0x070f…c9 | 0.0007 |

**Total APT across swarm:** ~20.57 APT  
**Note:** Initial query used deprecated `CoinStore` resource; switched to `coin::balance` view function.

### Multisig Contract Probes

| Pair | Address (short) | Sigs Required | Status |
|------|----------------|---------------|--------|
| A-B | 0x0da4…003 | 2 | ✓ healthy |
| A-G | 0xf56c…096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff…883 | 2 | ✓ healthy |
| S-T | 0x3b1c…883 | 2 | ✓ healthy |
| V-W | 0x40fa…b6d | 2 | ✓ healthy |

All 5 multisig contracts are healthy and require 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

**Status: SPA — no JSON API accessible.** The site renders as a Next.js client-side application. No `/api/markets` or equivalent endpoint returned structured data. Recorded as unavailable in `mnx_snapshots`.

---

## DuckDB Schema Summary

```sql
world_increments   -- 34 rows: GF(3) colored sweep events per source
repo_snapshots     -- 1,269 rows: full repo metadata
aptos_snapshots    -- 28 rows: wallet balances (alice, bob, A-Z)
multisig_probes    -- 5 rows: multisig health checks
mnx_snapshots      -- 1 row: SPA/unavailable marker
```
