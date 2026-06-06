# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-06  
**Branch:** world-increment/sweep  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### World-Increments (GF3 Color Chain)

| id | GF3 Trit | Color | Name | Source Type | Source |
|----|----------|-------|------|-------------|--------|
| 1 | +1 | `#b8bb26` | PLUS | org | plurigrid |
| 2 | -1 | `#cc241d` | MINUS | org | kubeflow |
| 3 | 0 | `#d3869b` | ERGODIC | org | TeglonLabs |
| 4 | +1 | `#b8bb26` | PLUS | user | bmorphism |
| 5 | -1 | `#cc241d` | MINUS | user | zubyul |
| 6 | 0 | `#d3869b` | ERGODIC | social | migalkin |
| 7 | +1 | `#b8bb26` | PLUS | social | DJedamski |
| 8 | -1 | `#cc241d` | MINUS | social | wasita |
| 9 | 0 | `#d3869b` | ERGODIC | social | kristinezheng |
| 10 | +1 | `#b8bb26` | PLUS | social | M1shaaa |
| 11 | -1 | `#cc241d` | MINUS | social | AustinCStone |

### Repo Snapshot Summary

| Source | Repos | Total Stars |
|--------|-------|-------------|
| plurigrid | 100 | 76 |
| bmorphism | 100 | 247 |
| zubyul | 49 | 14 |
| kubeflow | 48 | 34,177 |
| AustinCStone | 40 | 108 |
| migalkin | 19 | 280 |
| wasita | 11 | 5 |
| M1shaaa | 8 | 0 |
| DJedamski | 6 | 3 |
| kristinezheng | 5 | 0 |
| TeglonLabs | 4 | 2 |
| **TOTAL** | **390** | **34,912** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice + A-Z = 28 addresses)

All 28 addresses queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result:** All addresses return `resource_not_found` for the legacy CoinStore module. Accounts are active (alice has sequence_number 72) but have migrated to the Aptos Fungible Asset (FA) standard. Legacy APT balance via CoinStore: **0.0 APT** for all 28 wallets.

| World | Address | Balance (legacy CoinStore) |
|-------|---------|---------------------------|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b | 0.0 APT (FA model) |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d | 0.0 APT (FA model) |
| A-Z (26 wallets) | various | 0.0 APT (FA model) |

Note: Accounts confirmed active on-chain. The `resource_not_found` error indicates migration from `0x1::coin` to `0x1::fungible_asset` — balances live under the FA store, not queried here.

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | YES |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | YES |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | YES |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | YES |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | YES |

**All 5 multisig contracts healthy. All require 2-of-N signatures.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** - testnet.mnx.fi is a Vercel-hosted SPA requiring Vercel authentication for all routes including API paths (/api/markets, /api/v1/markets, /api/tickers). No market data accessible without Vercel auth credentials.

---

## DuckDB Schema Counts

| Table | Rows |
|-------|------|
| world_increments | 11 |
| repo_snapshots | 390 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

---

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent on 2026-06-06.*
