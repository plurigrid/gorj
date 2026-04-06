# World-Increment Sweep + Hamming Swarm Snapshot

**Date/Time:** 2026-04-06 (sweep executed 2026-04-06)

---

## GitHub: Repository Sources

| Source | Type | Repo Count |
|--------|------|-----------|
| TeglonLabs | org | 106 |
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| migalkin | user | 30 |
| wasita | user | 29 |
| zubyul | user | 23 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| **TOTAL** | | **433** |

> Note: GitHub API rate limit was reached during this sweep (unauthenticated). TeglonLabs was freshly queried; other sources reflect data from previous sweeps in the DB.

---

## Top 10 Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| migalkin/NodePiece | 143 | Python |
| migalkin/StarE | 88 | Python |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml |
| migalkin/kgcourse2021 | 25 | HTML |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |
| plurigrid/asi | 15 | HTML |
| migalkin/NBFNet_mlx | 10 | Python |
| plurigrid/ontology | 7 | JavaScript |
| migalkin/RWL | 7 | Python |
| bmorphism/shitcoin | 5 | HTML |

---

## GF(3) Increment Color Chain Summary

| GF3 Name | Color | Trit | Count |
|----------|-------|------|-------|
| ERGODIC | #d3869b | 0 | 143 |
| PLUS | #b8bb26 | +1 | 145 |
| MINUS | #cc241d | -1 | 145 |

Total world increments: **433**

GF(3) assignment rule:
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

---

## Aptos: World Label Wallet Balances

> All queried addresses returned `resource_not_found` (no CoinStore resource at ledger version 4783731188) — balances recorded as 0.0 APT.

| World Label | Address (truncated) | Balance (APT) |
|-------------|---------------------|--------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...b9d7a | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...cfdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...c7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...25dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...7f2e9 | 0.0 |
| N | 0xe7dd...51b2c | 0.0 |
| O | 0x7325...5a89d | 0.0 |
| P | 0x6218...ec948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...76e10 | 0.0 |
| S | 0xb875...d0386 | 0.0 |
| T | 0x3578...3f4588 | 0.0 |
| U | 0x7586...f9956 | 0.0 |
| V | 0xb59d...af2c3 | 0.0 |
| W | 0x5f32...cc7b0 | 0.0 |
| X | 0xa95c...3047d | 0.0 |
| Y | 0xd8e3...444c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

---

## Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|:-------------:|:-------:|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

All 5 multisig contracts healthy — 2-of-N signatures required.

---

## MNX Markets

**Status: unavailable**

All three endpoints (`/api/markets`, `/api/tickers`, `/api/v1/markets`) at `https://testnet.mnx.fi` returned SPA HTML (not JSON data). Market data could not be retrieved. Placeholder row inserted into `mnx_snapshots`.

---

## Database Summary

- **DB path:** `packages/world-increment/ducklake/world-increments.duckdb`
- **DuckDB version:** v1.5.1 (Variegata)
- **world_increments:** 433 rows
- **repo_snapshots:** 433 rows
- **aptos_snapshots:** 28 rows
- **multisig_probes:** 5 rows
- **mnx_snapshots:** 1 row (placeholder)
