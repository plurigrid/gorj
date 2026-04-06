# World-Increment Sweep

**Date:** 2026-04-06

## GitHub Sweep Summary

Sources queried via `curl` (GitHub public API, unauthenticated):

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 46 |
| TeglonLabs | org | 53 |
| bmorphism | user | 100 |
| zubyul | user | 23 |
| migalkin | user (zubyul social) | 30 |
| DJedamski | user (zubyul social) | 11 |
| wasita | user (zubyul social) | 29 |
| kristinezheng | user (zubyul social) | 18 |
| M1shaaa | user (zubyul social) | 16 |
| AustinCStone | user (zubyul social) | 43 |
| **Total** | | **469** |

Events collected: bmorphism (30 events), zubyul (30 events) - stored as metadata.

Errors: None. All API calls succeeded (unauthenticated rate limit not hit).

## Aptos Wallet Balances

Queried via `0x1::coin::balance` view function on Aptos mainnet.

| World | Address (short) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793...cc7b | 0.43643352 |
| bob | 0x0a3c...2d5d | 12.65700700 |
| A | 0x8699...e9d7a | 0.05176700 |
| B | 0x3f89...cb13 | 0.03625600 |
| C | 0x38b9...535e | 0.01018500 |
| D | 0xf776...fdd1 | 0.01162900 |
| E | 0xdc1d...8d36 | 0.01256100 |
| F | 0x18a1...cf71 | 1.96051600 |
| G | 0x69a3...7f32 | 0.00068100 |
| H | 0xce67...300f | 0.00068100 |
| I | 0x070f...1fc9 | 0.00068100 |
| J | 0x4d96...7f54 | 1.89509300 |
| K | 0xa732...5dc4 | 0.16196100 |
| L | 0x7c2e...eba9 | 1.92726900 |
| M | 0x6fed...f2e9 | 0.11228500 |
| N | 0xe7dd...1b2c | 0.10612100 |
| O | 0x7325...a89d | 0.21013600 |
| P | 0x6218...c948 | 0.14013600 |
| Q | 0xac40...c89a9 | 0.10324000 |
| R | 0x7ce6...6e10 | 0.09021700 |
| S | 0xb875...0386 | 0.09178800 |
| T | 0x3578...4588 | 0.07371300 |
| U | 0x7586...f956 | 0.05577300 |
| V | 0xb59d...f2c3 | 0.04783299 |
| W | 0x5f32...c7b0 | 0.04070500 |
| X | 0xa95c...047d | 0.04257700 |
| Y | 0xd8e3...44c4 | 0.04444900 |
| Z | 0x7af0...197c | 0.02326800 |

Note: CoinStore resource_not_found for all accounts; balances retrieved successfully via `0x1::coin::balance` view function.

## Multisig Contract Probes

Probed via `0x1::multisig_account::num_signatures_required` view function.

| Pair | Address (short) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

All 5 multisig contracts healthy, all require 2-of-N signatures.

## MNX Markets Status

**Unavailable.** All endpoints returned 404 or "Cannot GET":
- `https://testnet.mnx.fi/api/markets` - 404 (Vercel, x-matched-path: /404)
- `https://testnet.mnx.fi/api/v1/markets` - 404
- `https://testnet.mnx.fi/markets` - 404
- `https://api.testnet.mnx.fi/markets` - Cannot GET /markets
- `https://api.testnet.mnx.fi/v1/markets` - Cannot GET /v1/markets

Recorded as single unavailable placeholder row in mnx_snapshots.

## DuckDB Table Row Counts

Database: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 469 |
| repo_snapshots | 469 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (unavailable placeholder) |

## GF(3) Color Chain Distribution

- trit=0 (ERGODIC, #d3869b): 156 rows (id % 3 == 0)
- trit=1 (PLUS, #b8bb26): 157 rows (id % 3 == 1)
- trit=-1 (MINUS, #cc241d): 156 rows (id % 3 == 2)

## GF(3) Assignment Rule

- `id mod 3 == 0` - trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` - trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` - trit=-1, color=#cc241d, name=MINUS
