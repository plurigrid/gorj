# World-Increment Sweep + Hamming Snapshot — 2026-08-01

## Sweep Metadata
- **Date:** 2026-08-01
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source (this sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 49 |
| AustinCStone | user (social graph) | 41 |
| migalkin | user (social graph) | 19 |
| wasita | user (social graph) | 12 |
| M1shaaa | user (social graph) | 8 |
| DJedamski | user (social graph) | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user (social graph) | 5 |
| **TOTAL** | | **394 new repos** |

### DuckDB State (cumulative)
```
world_increments : 417 rows  (23 prior + 394 this sweep)
repo_snapshots   : 1338 rows (944 prior + 394 this sweep)
```

### GF(3) Color Chain (increment IDs 24–417)
- IDs 24–417, cycling: ERGODIC #d3869b (trit=0) → PLUS #b8bb26 (trit=1) → MINUS #cc241d (trit=-1)

### Notable Recent Activity
- **plurigrid/gorj** — Clojure, pushed 2026-08-01 (today), 1,563 open issues — highly active
- **TeglonLabs/jank-crane** — C++, pushed 2026-06-08 — crane-jank converged-IR hub with GF3 convergence maps
- **M1shaaa/M1shaaa** — pushed 2026-08-01 (today) — zubyul social graph activity
- **wasita/wasita.github.io** — Svelte, pushed 2026-07-21

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 wallets (alice, bob, A–Z) queried via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result: 0 APT in all 28 wallets.** Accounts either empty or using fungible asset module rather than legacy coin store.

| Wallet | Address (prefix) | APT Balance |
|--------|-----------------|-------------|
| alice | 0xc793... | 0 |
| bob | 0x0a3c... | 0 |
| A | 0x8699... | 0 |
| B–Z | various | 0 each |

### Multisig Contract Probes (5 pairs)

All 5 returned `num_signatures_required = 2`. All healthy.

| Pair | Address (prefix) | Threshold | Status |
|------|-----------------|-----------|--------|
| A-B | 0x0da4... | 2-of-2 | ✓ healthy |
| A-G | 0xf56c... | 2-of-2 | ✓ healthy |
| Y-Z | 0xd3ff... | 2-of-2 | ✓ healthy |
| S-T | 0x3b1c... | 2-of-2 | ✓ healthy |
| V-W | 0x40fa... | 2-of-2 | ✓ healthy |

### MNX Markets

`https://testnet.mnx.fi/api/markets` returns a Next.js SPA — no public REST API available from server-side fetch. `mnx_snapshots` table: 0 rows (unavailable).

---

## Full DuckDB State

```
world_increments : 417 rows
repo_snapshots   : 1338 rows
aptos_snapshots  :   28 rows (all 0 APT)
multisig_probes  :    5 rows (all healthy, 2-of-2)
mnx_snapshots    :    0 rows (SPA, unavailable)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
