# World-Increment Sweep + Hamming Snapshot

**Date:** 2026-03-30
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## GitHub Social Graph Snapshot

| Source | Type | Repo Count |
|--------|------|------------|
| plurigrid | org | 100 |
| kubeflow | org | 46 |
| TeglonLabs | org | 53 |
| bmorphism | user | 100 |
| zubyul | user | 23 |
| migalkin | user | 30 |
| DJedamski | user | 11 |
| wasita | user | 28 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| AustinCStone | user | 43 |
| **TOTAL** | | **468** |

Public events captured: bmorphism (30), zubyul (30)

---

## Aptos Mainnet Wallet Balances

| World | Address (first 10 chars) | Balance (APT) |
|-------|--------------------------|---------------|
| alice | 0xc793acde | 0.0 |
| bob | 0x0a3c00c5 | 0.0 |
| A | 0x8699edc0 | 0.0 |
| B | 0x3f892ebe | 0.0 |
| C | 0x38b99e63 | 0.0 |
| D | 0xf7765624 | 0.0 |
| E | 0xdc1d9d53 | 0.0 |
| F | 0x18a14b5b | 0.0 |
| G | 0x69a394c0 | 0.0 |
| H | 0xce67c327 | 0.0 |
| I | 0x070fe5d7 | 0.0 |
| J | 0x4d964db8 | 0.0 |
| K | 0xa732040a | 0.0 |
| L | 0x7c2eaeaf | 0.0 |
| M | 0x6fed37a7 | 0.0 |
| N | 0xe7dde6da | 0.0 |
| O | 0x73252b60 | 0.0 |
| P | 0x62187920 | 0.0 |
| Q | 0xac40fa50 | 0.0 |
| R | 0x7ce605cc | 0.0 |
| S | 0xb8753014 | 0.0 |
| T | 0x35781dc0 | 0.0 |
| U | 0x75860da4 | 0.0 |
| V | 0xb59dd817 | 0.0 |
| W | 0x5f32aef7 | 0.0 |
| X | 0xa95cbbd1 | 0.0 |
| Y | 0xd8e32848 | 0.0 |
| Z | 0x7af0ef6e | 0.0 |

Note: All wallets returned 0 APT balance (accounts may not hold CoinStore or have zero balance on mainnet).

---

## Multisig Contract Probes (Aptos Mainnet)

| Pair | Address (first 18 chars) | Sigs Required | Healthy |
|------|--------------------------|---------------|---------|
| A-B | 0x0da4f428a0c007da | 2 | true |
| A-G | 0xf56c4a1c0906214f | 2 | true |
| Y-Z | 0xd3ffe1812b2df406 | 2 | true |
| S-T | 0x3b1c3ae905d44c3a | 2 | true |
| V-W | 0x40fad7b423a84365 | 2 | true |

All 5 multisig contracts are healthy with 2-of-N signature requirement.

---

## MNX Markets Status

**Status: UNAVAILABLE**

Both endpoints (`https://testnet.mnx.fi/api/markets` and `https://testnet.mnx.fi/api/v1/markets`) returned HTML (SPA shell), not JSON API data. No market data available.

---

## GF(3) Color Chain Stats

The 468 repo snapshots are tagged with GF(3) trits cycling as id%3:

| Trit | GF3 Value | Color | Name | Count |
|------|-----------|-------|------|-------|
| 0 | 0 | `#d3869b` (mauve) | ERGODIC | 160 |
| 1 | 1 | `#b8bb26` (yellow-green) | PLUS | 160 |
| 2 | -1 (stored as 2) | `#cc241d` (red) | MINUS | 160 |

Total world_increments: **480** (includes 12 additional event entries)
Total repo_snapshots: **468**

---

## DuckDB Schema Summary

- `world_increments` - 480 rows (GF3-tagged event log)
- `repo_snapshots` - 468 rows (repo metadata snapshot)
- `aptos_snapshots` - 28 rows (wallet balances)
- `multisig_probes` - 5 rows (multisig health check)
- `mnx_snapshots` - 0 rows (unavailable)
