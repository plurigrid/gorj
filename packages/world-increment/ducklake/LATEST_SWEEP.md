# World-Increment Sweep — 2026-07-23

## Sweep Metadata
- **Date:** 2026-07-23T18:17 UTC
- **Agent:** world-increment-sweep
- **DuckDB version:** v1.5.5
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 257 |
| Total Repo Snapshots (cumulative) | 1178 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 85 |
| +1 | PLUS | `#b8bb26` | 86 |
| -1 | MINUS | `#cc241d` | 86 |

GF(3) rule: `id % 3 == 0` → ERGODIC, `id % 3 == 1` → PLUS, `id % 3 == 2` → MINUS

---

## GitHub Social Graph Coverage (this run)

| Source | Type | Increments |
|--------|------|------------|
| bmorphism | user | 53 |
| plurigrid | org | 52 |
| zubyul | user | 51 |
| kubeflow | org | 22 |
| migalkin | user | 21 |
| wasita | user | 14 |
| AustinCStone | user | 12 |
| M1shaaa | user | 10 |
| DJedamski | user | 8 |
| TeglonLabs | org | 7 |
| kristinezheng | user | 7 |
| **TOTAL** | | **257** |

---

## Hamming Swarm Snapshot (Aptos Mainnet)

**Timestamp:** 2026-07-23T18:13 UTC

### Wallet Balances

All 28 addresses returned **0.0 APT** — accounts have no registered `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource or zero balance on mainnet.

| Label | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9... | 0.0 |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf78... | 0.0 |
| A–Z | 0x8699edc… → 0x7af0ef6… | 0.0 each |

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428a0c007da0f7629c3ec6a08a661ee2084...` | 2 | ✓ |
| A-G | `0xf56c4a1c0906214f3f859ccd8b498ab673979df6...` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d...` | 2 | ✓ |
| S-T | `0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5...` | 2 | ✓ |
| V-W | `0x40fad7b423a843650fddcad36b7de6609eead0cf...` | 2 | ✓ |

All 5 multisig contracts healthy — 2-of-N threshold confirmed via `0x1::multisig_account::num_signatures_required`.

---

## MNX Testnet Market Data

**Status:** UNAVAILABLE — `/api/markets` returns 404; SPA yields no extractable data.
`mnx_snapshots` table: 0 rows.

---

## Database State

| Table | Row Count |
|-------|-----------|
| world_increments | 257 |
| repo_snapshots | 1178 |
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
