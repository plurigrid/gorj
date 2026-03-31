# LATEST_SWEEP

**Timestamp:** 2026-03-31T02:27:00Z

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Type | Source | Repos Found | GF(3) Trit | Color |
|------|--------|-------------|-----------|-------|
| org | plurigrid | 100 | 1 (PLUS) | `#b8bb26` |
| org | kubeflow | 46 | -1 (MINUS) | `#cc241d` |
| org | TeglonLabs | 53 | 0 (ERGODIC) | `#d3869b` |
| user | bmorphism | 100 | 1 (PLUS) | `#b8bb26` |
| user | zubyul | 23 | -1 (MINUS) | `#cc241d` |
| user | migalkin | 30 | 0 (ERGODIC) | `#d3869b` |
| user | DJedamski | 11 | 1 (PLUS) | `#b8bb26` |
| user | wasita | 28 | -1 (MINUS) | `#cc241d` |
| user | kristinezheng | 18 | 0 (ERGODIC) | `#d3869b` |
| user | M1shaaa | 16 | 1 (PLUS) | `#b8bb26` |
| user | AustinCStone | 43 | -1 (MINUS) | `#cc241d` |

**Total repos fetched:** 468  
**Event sweeps:** bmorphism (30 events), zubyul (30 events)  
**Total world_increment rows:** 44  
**Total repo_snapshot rows:** 856  

### GF(3) Color Chain Summary

The GF(3) field assigns each world increment a trit value based on `id % 3`:

| Trit | Value | Color | Name | Semantic |
|------|-------|-------|------|---------|
| 0 | 0 | `#d3869b` (rose) | ERGODIC | neutral / boundary |
| 1 | +1 | `#b8bb26` (yellow-green) | PLUS | constructive |
| 2 | -1 | `#cc241d` (red) | MINUS | deconstructive |

Distribution in this sweep: 15 ERGODIC, 15 PLUS, 14 MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

Queried via Aptos mainnet fullnode (`fullnode.mainnet.aptoslabs.com`).  
All accounts returned 0 APT — CoinStore resource not found, indicating these are likely unfunded or non-existent accounts on mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | `0xc793acde...24cc7b` | 0.0 |
| bob | `0x0a3c00c5...512d5d` | 0.0 |
| A | `0x8699edc0...be9d7a` | 0.0 |
| B | `0x3f892ebe...77cb13` | 0.0 |
| C | `0x38b99e63...91535e` | 0.0 |
| D | `0xf7765624...fcfdd1` | 0.0 |
| E | `0xdc1d9d53...958d36` | 0.0 |
| F | `0x18a14b5b...c3cf71` | 0.0 |
| G | `0x69a394c0...cc7f32` | 0.0 |
| H | `0xce67c327...e5300f` | 0.0 |
| I | `0x070fe5d7...0c1fc9` | 0.0 |
| J | `0x4d964db8...e87f54` | 0.0 |
| K | `0xa732040a...425dc4` | 0.0 |
| L | `0x7c2eaeaf...37eba9` | 0.0 |
| M | `0x6fed37a7...b7f2e9` | 0.0 |
| N | `0xe7dde6da...551b2c` | 0.0 |
| O | `0x73252b60...25a89d` | 0.0 |
| P | `0x6218792d...1ec948` | 0.0 |
| Q | `0xac40fa50...5c89a9` | 0.0 |
| R | `0x7ce605cc...d76e10` | 0.0 |
| S | `0xb8753014...9d0386` | 0.0 |
| T | `0x35781dc0...3f4588` | 0.0 |
| U | `0x75860da4...ef9956` | 0.0 |
| V | `0xb59dd817...9af2c3` | 0.0 |
| W | `0x5f32aef7...ccc7b0` | 0.0 |
| X | `0xa95cbbd1...33047d` | 0.0 |
| Y | `0xd8e32848...2444c4` | 0.0 |
| Z | `0x7af0ef6e...4e197c` | 0.0 |

### Multisig Contract Probes

All probed via `0x1::multisig_account::num_signatures_required` on Aptos mainnet.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | `0x0da4f428...987003` | 2 | YES |
| A-G | `0xf56c4a1c...bc0096` | 2 | YES |
| Y-Z | `0xd3ffe181...75b883` | 2 | YES |
| S-T | `0x3b1c3ae9...ed7883` | 2 | YES |
| V-W | `0x40fad7b4...80eb6d` | 2 | YES |

All 5 multisig contracts are **healthy** with 2 signatures required each.

### MNX Market Data

`https://testnet.mnx.fi/api/markets` and `/api/tickers` returned HTTP 404 — the site is a Next.js SPA and does not expose a public JSON API at those endpoints. **MNX market data: unavailable.**

---

## DuckDB Schema Summary

Database: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 44 | One row per source sweep + event entries |
| `repo_snapshots` | 856 | One row per GitHub repo found |
| `aptos_snapshots` | 28 | Aptos wallet balance snapshot |
| `multisig_probes` | 5 | Multisig contract probe results |
| `mnx_snapshots` | 0 | MNX markets (unavailable) |
