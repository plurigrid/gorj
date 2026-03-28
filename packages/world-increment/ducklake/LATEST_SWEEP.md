# World-Increment Sweep + Hamming Snapshot

**Date/Time of Sweep:** 2026-03-28 UTC
**Sweep ID:** world-increment/sweep-2026-03-28
**DB:** `packages/world-increment/ducklake/sweep.duckdb`

---

## Orgs / Users Scanned — Repo Counts

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 46 |
| TeglonLabs | org | 0 |
| bmorphism | user | 100 |
| zubyul | user | 23 |
| migalkin | user (zubyul social) | 30 |
| DJedamski | user (zubyul social) | 11 |
| wasita | user (zubyul social) | 28 |
| kristinezheng | user (zubyul social) | 18 |
| M1shaaa | user (zubyul social) | 0 |
| AustinCStone | user (zubyul social) | 0 |
| **TOTAL** | | **356** |

---

## Aptos Wallet Balances

All addresses queried against `fullnode.mainnet.aptoslabs.com`. All returned 0.0 APT (accounts not found / no CoinStore resource registered).

| World Label | Address (truncated) | APT Balance |
|-------------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.00000000 |
| bob | 0x0a3c...2d5d | 0.00000000 |
| A | 0x8699...e9d7a | 0.00000000 |
| B | 0x3f89...b13 | 0.00000000 |
| C | 0x38b9...535e | 0.00000000 |
| D | 0xf776...fdd1 | 0.00000000 |
| E | 0xdc1d...8d36 | 0.00000000 |
| F | 0x18a1...f71 | 0.00000000 |
| G | 0x69a3...f32 | 0.00000000 |
| H | 0xce67...300f | 0.00000000 |
| I | 0x070f...1fc9 | 0.00000000 |
| J | 0x4d96...f54 | 0.00000000 |
| K | 0xa732...dc4 | 0.00000000 |
| L | 0x7c2e...ba9 | 0.00000000 |
| M | 0x6fed...f2e9 | 0.00000000 |
| N | 0xe7dd...1b2c | 0.00000000 |
| O | 0x7325...a89d | 0.00000000 |
| P | 0x6218...c948 | 0.00000000 |
| Q | 0xac40...89a9 | 0.00000000 |
| R | 0x7ce6...6e10 | 0.00000000 |
| S | 0xb875...0386 | 0.00000000 |
| T | 0x3578...f588 | 0.00000000 |
| U | 0x7586...f9956 | 0.00000000 |
| V | 0xb59d...f2c3 | 0.00000000 |
| W | 0x5f32...c7b0 | 0.00000000 |
| X | 0xa95c...047d | 0.00000000 |
| Y | 0xd8e3...44c4 | 0.00000000 |
| Z | 0x7af0...197c | 0.00000000 |

---

## Multisig Probe Results

All probes hit `0x1::multisig_account::num_signatures_required` on Aptos mainnet.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

All 5 multisig accounts require 2-of-N signatures and are healthy.

---

## MNX Markets

**Status: UNAVAILABLE**
Both `https://testnet.mnx.fi/api/markets` and `https://testnet.mnx.fi/api/v1/markets` return an HTML Next.js page rather than JSON market data. No market records inserted into `mnx_snapshots`.

---

## GF(3) Color Distribution

356 world_increment rows across all repo snapshots:

| GF3 Name | Color | Trit | Count |
|----------|-------|------|-------|
| ERGODIC | #d3869b | 0 | 118 |
| PLUS | #b8bb26 | +1 | 119 |
| MINUS | #cc241d | -1 | 119 |

Distribution is nearly uniform (balanced GF3 chain, 356 ≡ 2 mod 3).

---

## DB Table Summary

| Table | Rows |
|-------|------|
| world_increments | 356 |
| repo_snapshots | 356 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

---

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(timestamp, world, address, balance_apt)

multisig_probes(timestamp, pair, address, sigs_required, healthy)

mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Events Fetched
- bmorphism: 30 public events
- zubyul: 30 public events
