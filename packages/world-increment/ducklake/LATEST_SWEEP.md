# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-08-03  
**GF(3) Color Chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d (cycle)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| DJedamski | user | 6 |
| wasita | user | 1 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| AustinCStone | user | 41 |
| **TOTAL** | | **383** |

### GF(3) World Increment Color Chain
| ID | Source | Trit | Color | Name |
|----|--------|------|-------|------|
| 1 | AustinCStone | 1 | #b8bb26 | PLUS |
| 2 | DJedamski | -1 | #cc241d | MINUS |
| 3 | M1shaaa | 0 | #d3869b | ERGODIC |
| 4 | TeglonLabs | 1 | #b8bb26 | PLUS |
| 5 | bmorphism | -1 | #cc241d | MINUS |
| 6 | kristinezheng | 0 | #d3869b | ERGODIC |
| 7 | kubeflow | 1 | #b8bb26 | PLUS |
| 8 | migalkin | -1 | #cc241d | MINUS |
| 9 | plurigrid | 0 | #d3869b | ERGODIC |
| 10 | wasita | 1 | #b8bb26 | PLUS |
| 11 | zubyul | -1 | #cc241d | MINUS |

### Notable Repos (Recently Pushed)
- **plurigrid/gorj** (Clojure) — pushed 2026-08-03 — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **plurigrid/place** (TeX) — pushed 2026-08-02 — 15 open issues
- **plurigrid/asi** (HTML) — ★58 — everything is topological chemputer!
- **TeglonLabs/jank-crane** (C++) — pushed 2026-06-08 — crane-jank converged-IR hub
- **wasita/wasita.github.io** (Svelte) — pushed 2026-07-21 — personal website
- **M1shaaa/M1shaaa** — pushed 2026-08-02

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances
All 28 wallets (alice, bob, A–Z) queried against Aptos mainnet.

**Result:** All 28 wallets returned **0 APT** — accounts exist on-chain but hold no APT coin store resources (likely unfunded or using non-standard token types).

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793...4cc7b | 0.00000000 |
| bob | 0x0a3c...512d5d | 0.00000000 |
| A–Z | (26 addresses) | 0.00000000 each |

**Total APT tracked:** 0.00000000 APT across 28 wallets

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✅ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✅ HEALTHY |

**All 5 multisig contracts healthy** — 2-of-N threshold on all pairs.

### MNX Markets (testnet.mnx.fi)
Status: **SPA — No data API accessible**  
All probed endpoints (`/api/markets`, `/api/v1/markets`, `/api/tickers`) returned the Next.js SPA HTML shell rather than JSON market data. MNX testnet appears to be a client-side rendered app with no public REST API. No market data recorded.

---

## DuckDB Summary

```
world_increments  : 11 rows  (one per source, GF3-colored)
repo_snapshots    : 383 rows (all repos from sweep)
aptos_snapshots   : 28 rows  (alice, bob, A–Z wallets)
multisig_probes   : 5 rows   (A-B, A-G, Y-Z, S-T, V-W)
mnx_snapshots     : 0 rows   (SPA, no data API)
```

DB path: `packages/world-increment/ducklake/world-increments.duckdb`
