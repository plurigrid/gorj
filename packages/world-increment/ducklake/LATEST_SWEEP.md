# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-07-05  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Orgs Snapshotted

| Org/User | Source | Repos | Top Repo (stars) |
|---|---|---|---|
| plurigrid | org | 100 | asi (28★) |
| kubeflow | org | 10 (sample) | kubeflow/kubeflow (15,763★) |
| TeglonLabs | org | 5 | mathpix-gem (2★) |
| bmorphism | user | 15 | risc0-cosmwasm-example (23★) |
| zubyul | user | 10 | WGCNA (2★) |

### Zubyul Social Graph

| User | Repos | Top Repo |
|---|---|---|
| migalkin | 4 | NodePiece (144★) |
| DJedamski | 3 | kaggle_ncaa18 (0★) |
| wasita | 3 | magic-garden (2★) |
| kristinezheng | 2 | kristinezheng.github.io (0★) |
| M1shaaa | 2 | M1shaaa/M1shaaa (0★) |
| AustinCStone | 4 | TextGAN (92★) |

### DuckDB world_increments GF(3) Chain

| trit | color | name | count |
|---|---|---|---|
| 0 | #d3869b | ERGODIC | 11 |
| 1 | #b8bb26 | PLUS | 12 |
| -1 | #cc241d | MINUS | 11 |

**Total repo_snapshots:** 1,102 rows  
**Total world_increments:** 34 rows

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A-Z) returned `resource_not_found` on  
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` -- no activated APT coin store.

| Label | Address (prefix) | Balance (APT) |
|---|---|---|
| alice | 0xc793acd... | 0.0 |
| bob | 0x0a3c00c... | 0.0 |
| A-Z | 0x8699edc... to 0x7af0ef6... | 0.0 (all) |

Note: `resource_not_found` = address exists on Aptos but has not activated an APT CoinStore.

### Multisig Contract Probes

All 5 multisig contracts are HEALTHY with `sigs_required = 2`.

| Pair | Address (prefix) | Sigs Required | Status |
|---|---|---|---|
| A-B | 0x0da4f428... | 2 | HEALTHY |
| A-G | 0xf56c4a1c... | 2 | HEALTHY |
| Y-Z | 0xd3ffe181... | 2 | HEALTHY |
| S-T | 0x3b1c3ae9... | 2 | HEALTHY |
| V-W | 0x40fad7b4... | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** -- `testnet.mnx.fi` is behind Vercel password protection.  
All endpoints return `Authentication Required`. No market data accessible without bypass token.

---

## Schema Summary

```sql
world_increments   -- 34 rows (GF3 color chain, per-source increment IDs)
repo_snapshots     -- 1,102 rows (org/user, repo metadata)
aptos_snapshots    -- 28 rows (alice, bob, A-Z; all 0.0 APT)
multisig_probes    -- 5 rows (all healthy, sigs=2)
mnx_snapshots      -- 1 row (auth-gated placeholder)
```

*Sweep agent: world-increment-sweep + hamming-swarm-snapshot | Run: 2026-07-05 UTC*
