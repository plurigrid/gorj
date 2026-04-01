# World-Increment Sweep + Hamming Snapshot

**Sweep Timestamp:** 2026-04-01T17:19:09Z

---

## GitHub Social Graph Sweep

### Sources Queried

| # | Type | Source | Repos Captured | GF(3) Trit | GF(3) Name | GF(3) Color |
|---|------|--------|---------------|------------|------------|-------------|
| 1 | org | plurigrid | 100 | 1 | PLUS | `#b8bb26` |
| 2 | org | kubeflow | 46 | -1 | MINUS | `#cc241d` |
| 3 | org | TeglonLabs | 53 | 0 | ERGODIC | `#d3869b` |
| 4 | user | bmorphism | 100 | 1 | PLUS | `#b8bb26` |
| 5 | user | zubyul | 23 | -1 | MINUS | `#cc241d` |
| 6 | user | migalkin | 30 | 0 | ERGODIC | `#d3869b` |
| 7 | user | DJedamski | 11 | 1 | PLUS | `#b8bb26` |
| 8 | user | wasita | 29 | -1 | MINUS | `#cc241d` |
| 9 | user | kristinezheng | 18 | 0 | ERGODIC | `#d3869b` |
| 10 | user | M1shaaa | 16 | 1 | PLUS | `#b8bb26` |
| 11 | user | AustinCStone | 43 | -1 | MINUS | `#cc241d` |

**Total repos captured:** 469 across 11 sources

### GF(3) Color Chain Summary

The GF(3) color chain cycles through three states based on `id % 3`:

| id%3 | Trit | Name | Hex Color |
|------|------|------|-----------|
| 0 | 0 | ERGODIC | `#d3869b` (pink/mauve) |
| 1 | +1 | PLUS | `#b8bb26` (yellow-green) |
| 2 | -1 | MINUS | `#cc241d` (red) |

---

## Hamming Swarm Snapshot

### Aptos Wallet Balances

| Label | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| A | `0x8699edc0...be9d7a` | 0.00000000 |
| B | `0x3f892ebe...77cb13` | 0.00000000 |
| C | `0x38b99e63...91535e` | 0.00000000 |
| D | `0xf7765624...fcfdd1` | 0.00000000 |
| E | `0xdc1d9d53...958d36` | 0.00000000 |
| F | `0x18a14b5b...c3cf71` | 0.00000000 |
| G | `0x69a394c0...cc7f32` | 0.00000000 |
| H | `0xce67c327...e5300f` | 0.00000000 |
| I | `0x070fe5d7...0c1fc9` | 0.00000000 |
| J | `0x4d964db8...e87f54` | 0.00000000 |
| K | `0xa732040a...425dc4` | 0.00000000 |
| L | `0x7c2eaeaf...37eba9` | 0.00000000 |
| M | `0x6fed37a7...b7f2e9` | 0.00000000 |
| N | `0xe7dde6da...551b2c` | 0.00000000 |
| O | `0x73252b60...25a89d` | 0.00000000 |
| P | `0x6218792d...1ec948` | 0.00000000 |
| Q | `0xac40fa50...5c89a9` | 0.00000000 |
| R | `0x7ce605cc...d76e10` | 0.00000000 |
| S | `0xb8753014...9d0386` | 0.00000000 |
| T | `0x35781dc0...3f4588` | 0.00000000 |
| U | `0x75860da4...ef9956` | 0.00000000 |
| V | `0xb59dd817...9af2c3` | 0.00000000 |
| W | `0x5f32aef7...ccc7b0` | 0.00000000 |
| X | `0xa95cbbd1...33047d` | 0.00000000 |
| Y | `0xd8e32848...2444c4` | 0.00000000 |
| Z | `0x7af0ef6e...4e197c` | 0.00000000 |
| alice | `0xc793acde...24cc7b` | 0.00000000 |
| bob | `0x0a3c00c5...512d5d` | 0.00000000 |

All addresses returned resource_not_found for CoinStore - indicating 0.0 APT balance (accounts not initialized with APT).

---

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | `0x0da4f428...987003` | 2 | YES |
| A-G | `0xf56c4a1c...bc0096` | 2 | YES |
| Y-Z | `0xd3ffe181...75b883` | 2 | YES |
| S-T | `0x3b1c3ae9...ed7883` | 2 | YES |
| V-W | `0x40fad7b4...80eb6d` | 2 | YES |

All 5 multisig contracts are healthy with 2 signatures required.

---

### MNX Markets Status

**Status: UNAVAILABLE**

All three endpoints attempted:
- `https://testnet.mnx.fi/api/markets` → HTML response (not JSON)
- `https://testnet.mnx.fi/api/v1/markets` → HTML response (not JSON)
- `https://testnet.mnx.fi/api/tickers` → HTML response (not JSON)

The MNX testnet API does not expose machine-readable market data at these endpoints.

---

## DuckDB Tables

File: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 11 |
| repo_snapshots | 469 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |
