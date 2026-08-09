# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-08-09  
**GF(3) Color Chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d (cycling)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| AustinCStone | user | 41 |
| migalkin | user | 19 |
| wasita | user | 14 |
| DJedamski | user | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user | 5 |
| M1shaaa | user | 5 |
| **TOTAL** | | **393 new repos** |

### Most Recently Active (plurigrid/bmorphism/zubyul)

| Repo | Last Push |
|------|-----------|
| plurigrid/place | 2026-08-09 |
| plurigrid/gorj | 2026-08-09 |
| bmorphism/Gay.jl | 2026-08-07 |
| plurigrid/eirobri | 2026-08-04 |
| plurigrid/zig-syrup | 2026-07-28 |
| zubyul/from-possible-worlds | 2026-07-18 |
| bmorphism/gay-chat | 2026-07-14 |
| plurigrid/asi | 2026-07-10 |

### Top Stars (this sweep)

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15808 | 2026-07-10 |
| kubeflow/pipelines | Python | 4180 | 2026-08-09 |
| kubeflow/spark-operator | Python | 3146 | 2026-08-09 |
| kubeflow/trainer | Go | 2177 | 2026-08-08 |
| kubeflow/katib | Python | 1694 | 2026-08-06 |
| kubeflow/examples | Jsonnet | 1461 | 2025-04-14 |
| kubeflow/community-distribution | YAML | 1030 | 2026-08-04 |

### DuckDB ducklake

- **DB:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Total increments recorded (all-time):** 34
- **Total repo snapshots (all-time):** 1337
- **This sweep:** 11 increment rows, 393 repo rows

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 wallets (alice, bob, A–Z) queried via  
`https://fullnode.mainnet.aptoslabs.com/v1/accounts/{ADDR}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

**Result:** All accounts returned 0 APT — CoinStore resource not initialized on any of these addresses. The accounts may exist on-chain but have not received APT deposits or initialized the coin store resource.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z (26 wallets) | various | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts responded healthy with `num_signatures_required = 2`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)

Both `/api/markets` and `/api/v1/markets` returned HTML (Next.js SPA shell).  
No JSON market data extractable from API probe — frontend renders data client-side.  
**Status: UNAVAILABLE via direct API probe.**

---

## GF(3) Color Chain Summary

| Increment | Source | Trit | Color | Name |
|-----------|--------|------|-------|------|
| 1 | plurigrid | 1 | #b8bb26 | PLUS |
| 2 | kubeflow | -1 | #cc241d | MINUS |
| 3 | bmorphism | 0 | #d3869b | ERGODIC |
| 4 | zubyul | 1 | #b8bb26 | PLUS |
| 5 | migalkin | -1 | #cc241d | MINUS |
| 6 | AustinCStone | 0 | #d3869b | ERGODIC |
| 7 | TeglonLabs | 1 | #b8bb26 | PLUS |
| 8 | DJedamski | -1 | #cc241d | MINUS |
| 9 | kristinezheng | 0 | #d3869b | ERGODIC |
| 10 | M1shaaa | 1 | #b8bb26 | PLUS |
| 11 | wasita | -1 | #cc241d | MINUS |
