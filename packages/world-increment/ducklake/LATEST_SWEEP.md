# World-Increment Sweep + Hamming Snapshot

**Sweep Date/Time:** 2026-04-16T00:00:00Z (UTC)  
**DuckDB:** v1.5.2 (Variegata)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## GitHub Repos Captured

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 99 |
| zubyul | user | 47 |
| migalkin | user | 19 |
| wasita | user | 10 |
| M1shaaa | user | 8 |
| kristinezheng | user | 6 |
| DJedamski | user | 6 |
| AustinCStone | user | 40 |
| **TOTAL** | | **386** |

---

## Aptos Balances (Hamming Swarm)

All accounts queried via Aptos mainnet fullnode. All returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — recorded as 0.0 APT.

| World | Address (first 10 chars) | Balance APT |
|-------|--------------------------|-------------|
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

---

## Multisig Probe Results

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (first 10 chars) | Sigs Required | Healthy |
|------|--------------------------|--------------|---------|
| A-B | 0x0da4f428 | 2 | true |
| A-G | 0xf56c4a1c | 2 | true |
| Y-Z | 0xd3ffe181 | 2 | true |
| S-T | 0x3b1c3ae9 | 2 | true |
| V-W | 0x40fad7b4 | 2 | true |

---

## MNX Markets Status

`testnet.mnx.fi/api/markets` and `testnet.mnx.fi/api/v1/markets`: **UNAVAILABLE** — both endpoints return an HTML page (Next.js SPA), no JSON REST API accessible at these paths.

---

## GF(3) Color Chain Summary

GF(3) tritwise coloring of 386 repo snapshot world-increments:

| Trit | Color | Hex | Name | Count |
|------|-------|-----|------|-------|
| 1 | PLUS | #b8bb26 | gf3_plus | 129 |
| -1 | MINUS | #cc241d | gf3_minus | 129 |
| 0 | ERGODIC | #d3869b | gf3_ergodic | 128 |

Color assignment rule: `id % 3 == 0` → ERGODIC, `id % 3 == 1` → PLUS, `id % 3 == 2` → MINUS.

---

## Database Tables

| Table | Rows |
|-------|------|
| world_increments | 409 (386 repo snapshots + 23 source-level meta) |
| repo_snapshots | 1330 (multi-indexed) |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (API unavailable) |
