# LATEST_SWEEP.md

## Sweep Date/Time
2026-04-01 00:00:00 UTC

---

## GitHub Sources Queried

| Source | Type | Repo Count |
|--------|------|-----------|
| plurigrid | org | 93 |
| kubeflow | org | 46 |
| TeglonLabs | org | 3 |
| bmorphism | user | 97 |
| zubyul | user | 44 |
| migalkin | user | 19 |
| DJedamski | user | 6 |
| wasita | user | 9 |
| kristinezheng | user | 6 |
| M1shaaa | user | 8 |
| AustinCStone | user | 40 |

**Total repos snapshotted: 371**

Events also fetched for: bmorphism, zubyul

---

## Aptos Wallet Balances

| Label | Address (truncated) | Balance (APT) |
|-------|---------------------|--------------|
| alice | 0xc793acde...24cc7b | 0.00000000 |
| bob | 0x0a3c00c5...512d5d | 0.00000000 |
| A | 0x8699edc0...be9d7a | 0.00000000 |
| B | 0x3f892ebe...77cb13 | 0.00000000 |
| C | 0x38b99e63...91535e | 0.00000000 |
| D | 0xf7765624...fcfdd1 | 0.00000000 |
| E | 0xdc1d9d53...958d36 | 0.00000000 |
| F | 0x18a14b5b...c3cf71 | 0.00000000 |
| G | 0x69a394c0...cc7f32 | 0.00000000 |
| H | 0xce67c327...e5300f | 0.00000000 |
| I | 0x070fe5d7...0c1fc9 | 0.00000000 |
| J | 0x4d964db8...e87f54 | 0.00000000 |
| K | 0xa732040a...425dc4 | 0.00000000 |
| L | 0x7c2eaeaf...37eba9 | 0.00000000 |
| M | 0x6fed37a7...b7f2e9 | 0.00000000 |
| N | 0xe7dde6da...551b2c | 0.00000000 |
| O | 0x73252b60...25a89d | 0.00000000 |
| P | 0x6218792d...1ec948 | 0.00000000 |
| Q | 0xac40fa50...5c89a9 | 0.00000000 |
| R | 0x7ce605cc...d76e10 | 0.00000000 |
| S | 0xb8753014...9d0386 | 0.00000000 |
| T | 0x35781dc0...3f4588 | 0.00000000 |
| U | 0x75860da4...ef9956 | 0.00000000 |
| V | 0xb59dd817...9af2c3 | 0.00000000 |
| W | 0x5f32aef7...ccc7b0 | 0.00000000 |
| X | 0xa95cbbd1...33047d | 0.00000000 |
| Y | 0xd8e32848...2444c4 | 0.00000000 |
| Z | 0x7af0ef6e...4e197c | 0.00000000 |

All wallets show 0.00000000 APT (accounts not funded on mainnet).

---

## Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required |
|------|---------------------|--------------|
| A-B | 0x0da4f428...987003 | 2 |
| A-G | 0xf56c4a1c...bc0096 | 2 |
| Y-Z | 0xd3ffe181...75b883 | 2 |
| S-T | 0x3b1c3ae9...ed7883 | 2 |
| V-W | 0x40fad7b4...80eb6d | 2 |

All 5 multisig contracts require **2 signatures** (2-of-N multisig).

---

## MNX Market Status

All three endpoints probed:
- `https://testnet.mnx.fi/api/markets` → **unavailable** (returns HTML, no JSON)
- `https://testnet.mnx.fi/api/tickers` → **unavailable** (returns HTML, no JSON)
- `https://testnet.mnx.fi/api/v1/markets` → **unavailable** (returns HTML, no JSON)

The testnet.mnx.fi API endpoints are not returning JSON data at sweep time.

---

## GF(3) Color Chain Summary

The world_increments table applies a GF(3) cyclic color assignment based on `id % 3`:

| Trit | Color | Name | Meaning |
|------|-------|------|---------|
| 0 | `#d3869b` (pink) | ERGODIC | Equilibrium/stationary state |
| 1 | `#b8bb26` (yellow-green) | PLUS | Positive increment |
| 2 | `#cc241d` (red) | MINUS | Negative increment |

Distribution across 11 world_increment sources:
- ERGODIC (trit=0): TeglonLabs (id=3), migalkin (id=6), kristinezheng (id=9)
- PLUS (trit=1): plurigrid (id=1), bmorphism (id=4), DJedamski (id=7), M1shaaa (id=10)
- MINUS (trit=2): kubeflow (id=2), zubyul (id=5), wasita (id=8), AustinCStone (id=11)

---

## Database

Location: `packages/world-increment/ducklake/world-increments.duckdb`

Tables:
- `world_increments`: 11 rows (one per GitHub source)
- `repo_snapshots`: 371 rows (one per repo)
- `aptos_wallets`: 28 rows (alice, bob, A-Z)
- `aptos_multisigs`: 5 rows (A-B, A-G, Y-Z, S-T, V-W)
- `mnx_markets`: 3 rows (endpoint status)
