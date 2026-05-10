# World-Increment Sweep + Hamming Snapshot

**Timestamp:** 2026-05-10T19:11:00Z
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## GitHub Sweep Summary

Total repos collected: **391** across 3 orgs and 8 users (plurigrid and bmorphism each hit the 100-result search cap)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 48 |
| zubyul | user | 49 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| wasita | user | 11 |
| M1shaaa | user | 8 |
| kristinezheng | user | 6 |
| DJedamski | user | 6 |
| TeglonLabs | org | 4 |
| **TOTAL** | | **391** |

---

## GF(3) Color Chain — 11 World Increments

| ID | Source | GF3 Trit | Color | Name |
|----|--------|----------|-------|------|
| 1  | AustinCStone | +1 | `#b8bb26` | **PLUS** |
| 2  | DJedamski | -1 | `#cc241d` | **MINUS** |
| 3  | M1shaaa | 0 | `#d3869b` | **ERGODIC** |
| 4  | TeglonLabs | +1 | `#b8bb26` | **PLUS** |
| 5  | bmorphism | -1 | `#cc241d` | **MINUS** |
| 6  | kristinezheng | 0 | `#d3869b` | **ERGODIC** |
| 7  | kubeflow | +1 | `#b8bb26` | **PLUS** |
| 8  | migalkin | -1 | `#cc241d` | **MINUS** |
| 9  | plurigrid | 0 | `#d3869b` | **ERGODIC** |
| 10 | wasita | +1 | `#b8bb26` | **PLUS** |
| 11 | zubyul | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## Aptos Wallet Snapshot

All 28 addresses probed. All returned `resource_not_found` — addresses exist on-chain but hold no APT coin resource (balance=0.0 APT).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...e9d7 | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...3cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...9956 | 0.0 |
| V | 0xb59d...af2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

---

## Multisig Probes

Endpoint: `POST https://fullnode.mainnet.aptoslabs.com/v1/view` (`0x1::multisig_account::num_signatures_required`)

All 5 multisig accounts are healthy with `sigs_required=2`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

---

## MNX Markets Status

**UNAVAILABLE** — Both `https://testnet.mnx.fi/api/markets` and `https://testnet.mnx.fi/api/v1/markets` return a Next.js SPA HTML page (no REST JSON API data accessible). The MNX testnet frontend is a client-side rendered application.

---

## GF(3) Color Chain Legend

World-increment IDs assigned GF(3) trit values cyclically (1-indexed):

| id % 3 | Trit | Name | Color |
|--------|------|------|-------|
| 1 | +1 | PLUS | `#b8bb26` (gruvbox green) |
| 2 | -1 | MINUS | `#cc241d` (gruvbox red) |
| 0 | 0 | ERGODIC | `#d3869b` (gruvbox pink) |

---

## DuckDB Table Summary

| Table | Rows |
|-------|------|
| world_increments | 11 |
| repo_snapshots | 391 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

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
