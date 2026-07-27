# World-Increment Sweep — 2026-07-27

## Sweep Metadata
- **Date:** 2026-07-27
- **Agent:** world-increment-sweep
- **DuckDB version:** v1.5.5
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 34 |
| Total Repo Snapshots | 1338 |
| New Increments This Sweep | 11 (IDs 13–23) |
| New Repo Snapshots | 394 |
| Aptos Snapshots | 28 |
| Multisig Probes | 5 (all healthy) |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain — New Increments (IDs 13–23)

| ID | Source | Type | Repos | GF3 Trit | Color | Name |
|----|--------|------|------:|-----------|-------|------|
| 13 | plurigrid | org | 100 | +1 | `#b8bb26` | **PLUS** |
| 14 | kubeflow | org | 49 | -1 | `#cc241d` | **MINUS** |
| 15 | TeglonLabs | org | 5 | 0 | `#d3869b` | **ERGODIC** |
| 16 | bmorphism | user | 100 | +1 | `#b8bb26` | **PLUS** |
| 17 | zubyul | user | 49 | -1 | `#cc241d` | **MINUS** |
| 18 | migalkin | user | 19 | 0 | `#d3869b` | **ERGODIC** |
| 19 | DJedamski | user | 6 | +1 | `#b8bb26` | **PLUS** |
| 20 | wasita | user | 12 | -1 | `#cc241d` | **MINUS** |
| 21 | kristinezheng | user | 5 | 0 | `#d3869b` | **ERGODIC** |
| 22 | M1shaaa | user | 8 | +1 | `#b8bb26` | **PLUS** |
| 23 | AustinCStone | user | 41 | -1 | `#cc241d` | **MINUS** |

GF(3) chain this sweep: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## Hamming Swarm: Aptos Wallet Snapshot

Queried via `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | null (FA standard) |
| bob | 0x0a3c...2d5d | null (FA standard) |
| A | 0x8699...9d7a | null (FA standard) |
| B | 0x3f89...b13 | null (FA standard) |
| C | 0x38b9...535e | null (FA standard) |
| D | 0xf776...fdd1 | null (FA standard) |
| E | 0xdc1d...8d36 | null (FA standard) |
| F | 0x18a1...cf71 | null (FA standard) |
| G | 0x69a3...f32 | null (FA standard) |
| H | 0xce67...300f | null (FA standard) |
| I | 0x070f...1fc9 | null (FA standard) |
| J | 0x4d96...7f54 | null (FA standard) |
| K | 0xa732...dc4 | null (FA standard) |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

> alice–K: `resource_not_found` — these addresses use the modern Aptos Fungible Asset (FA) standard rather than the legacy CoinStore resource.  
> L–Z: API responded, balance = 0.0 APT.

---

## Hamming Swarm: Multisig Probes

Probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|:-------------:|:-------:|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

All 5 multisig contracts healthy, all requiring 2-of-N signatures.

---

## MNX Markets

`testnet.mnx.fi` — Next.js SPA, all API path attempts return HTML. No market data available this sweep.

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
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
