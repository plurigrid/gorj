# World-Increment Sweep — 2026-04-03

## Sweep Metadata
- **Date:** 2026-04-03
- **Agent:** world-increment-sweep
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 21 |
| Total Repo Snapshots | 769 |
| Sources Covered | 3 orgs + 8 users + 2 event streams |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GitHub Sources Queried

| Source | Type | Repos | Status |
|--------|------|-------|--------|
| plurigrid | org | 100 (prior sweep) | 403 rate-limited |
| kubeflow | org | 46 this sweep (92 total) | 200 OK |
| TeglonLabs | org | 53 (prior sweep) | 403 rate-limited |
| bmorphism | user | 100 this sweep (200 total) | 200 OK |
| zubyul | user | 23 this sweep (46 total) | 200 OK |
| migalkin | user | 30 this sweep (60 total) | 200 OK |
| DJedamski | user | 11 this sweep (22 total) | 200 OK |
| wasita | user | 29 this sweep (58 total) | 200 OK |
| kristinezheng | user | 18 this sweep (36 total) | 200 OK |
| M1shaaa | user | 16 (prior sweep) | 403 rate-limited |
| AustinCStone | user | 43 this sweep (86 total) | 200 OK |
| bmorphism events | user | 30 events | 200 OK |
| zubyul events | user | 30 events | 200 OK |

**Total unique repo snapshots in DB:** 769 across 11 sources

---

## GF(3) Color Chain Summary

The GF(3) (Galois Field mod 3) color chain assigns each world_increment a trit and color:

| Trit | Color | Name | Hex | Count |
|------|-------|------|-----|-------|
| 0 | Pink/Mauve | ERGODIC | `#d3869b` | 7 |
| 1 | Yellow-Green | PLUS | `#b8bb26` | 7 |
| -1 | Red | MINUS | `#cc241d` | 7 |

Chain rule: `id % 3 == 0 → ERGODIC`, `id % 3 == 1 → PLUS`, `id % 3 == 2 → MINUS`

Total world_increments: **21** (perfectly balanced: 7 ERGODIC + 7 PLUS + 7 MINUS)

---

## Aptos Wallet Balances

Queried via `0x1::coin::balance` view function on Aptos mainnet (ledger ~4.76B).
Note: `CoinStore` resource probe returns "not found" for FA-store accounts; view function returns real balances.

| Label | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| bob | 0x0a3c00c58fdf90... | 12.657007 |
| F | 0x18a14b5b4bec11... | 1.960516 |
| L | 0x7c2eaeafad9725... | 1.927269 |
| J | 0x4d964db8f53837... | 1.895093 |
| alice | 0xc793acdec12b4a... | 0.436434 |
| O | 0x73252b6011a751... | 0.210136 |
| K | 0xa732040a6b0d55... | 0.161961 |
| P | 0x6218792de4a9bc... | 0.140136 |
| M | 0x6fed37a7553ef1... | 0.112285 |
| N | 0xe7dde6da0a65f5... | 0.106121 |
| Q | 0xac40fa50b81b4c... | 0.103240 |
| S | 0xb8753014e4888e... | 0.091788 |
| R | 0x7ce605cc8fda4f... | 0.090217 |
| T | 0x35781dc0e42fef... | 0.073713 |
| U | 0x75860da47565f6... | 0.055773 |
| A | 0x8699edc0960dd5... | 0.051767 |
| V | 0xb59dd8170321df... | 0.047833 |
| Y | 0xd8e32848f1dffa... | 0.044449 |
| X | 0xa95cbbd116548a... | 0.042577 |
| W | 0x5f32aef70f5ba5... | 0.040705 |
| B | 0x3f892ebe6e4516... | 0.036256 |
| Z | 0x7af0ef6e1bd706... | 0.023268 |
| E | 0xdc1d9d533bac35... | 0.012561 |
| D | 0xf77656248f64d5... | 0.011629 |
| C | 0x38b99e63ada9b6... | 0.010185 |
| H | 0xce67c327a7844e... | 0.000681 |
| I | 0x070fe5d74e4eda... | 0.000681 |
| G | 0x69a394c0b0ac84... | 0.000681 |

---

## Multisig Probe Results

All probes via `0x1::multisig_account::num_signatures_required` view on Aptos mainnet.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f428a0c007... | 2 | true |
| A-G | 0xf56c4a1c090621... | 2 | true |
| Y-Z | 0xd3ffe1812b2df4... | 2 | true |
| S-T | 0x3b1c3ae905d44c... | 2 | true |
| V-W | 0x40fad7b423a843... | 2 | true |

All 5 multisig contracts require 2 signatures and are healthy.

---

## MNX Markets Status

**Status: UNAVAILABLE**

`testnet.mnx.fi` serves a Next.js single-page application (HTML). No public REST API endpoints (`/api/markets`, `/api/v1/markets`) returned JSON data. Market data is client-side rendered and not machine-readable without a headless browser.

---

## DuckDB Table Row Counts

| Table | Rows |
|-------|------|
| world_increments | 21 |
| repo_snapshots | 769 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

---

## Schema Reference

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
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **bob** wallet holds 12.66 APT — largest balance in the set
- **F, L, J** each hold ~1.9 APT — mid-tier holders
- **kubeflow/pipelines**: 4,112 stars — most popular repo in this snapshot
- All 5 multisig contracts are live and require exactly 2 signatures
- GF(3) chain perfectly balanced across 21 increments
