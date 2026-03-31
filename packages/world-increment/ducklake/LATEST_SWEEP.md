# World-Increment Sweep — 2026-03-31

## Sweep Metadata
- **Date:** 2026-03-31
- **Agent:** world-increment-sweep + hamming swarm snapshot
- **DuckDB version:** v1.2.x
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 371 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 |
| Multisig Probes | 5 |

---

## GitHub Sweep: Repos Per Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 93 |
| kubeflow | org | 46 |
| TeglonLabs | org | 3 |
| bmorphism | user | 97 |
| zubyul | user | 44 |
| migalkin | user (zubyul social) | 19 |
| DJedamski | user (zubyul social) | 6 |
| wasita | user (zubyul social) | 9 |
| kristinezheng | user (zubyul social) | 6 |
| M1shaaa | user (zubyul social) | 8 |
| AustinCStone | user (zubyul social) | 40 |
| **TOTAL** | | **371** |

---

## GF(3) Color Chain — 11 Increments

| ID | Source | GF3 Trit | Color | Name |
|----|--------|-----------|-------|------|
| 1  | plurigrid | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## Aptos Hamming Swarm Balances

Queried via `0x1::coin::balance<0x1::aptos_coin::AptosCoin>` view function on Aptos mainnet.

| Label | Balance (APT) |
|-------|--------------|
| alice | 0.43643352 |
| bob | 12.657007 |
| A | 0.051767 |
| B | 0.036256 |
| C | 0.010185 |
| D | 0.011629 |
| E | 0.012561 |
| F | 1.960516 |
| G | 0.000681 |
| H | 0.000681 |
| I | 0.000681 |
| J | 1.895093 |
| K | 0.161961 |
| L | 1.927269 |
| M | 0.112285 |
| N | 0.106121 |
| O | 0.210136 |
| P | 0.140136 |
| Q | 0.103240 |
| R | 0.090217 |
| S | 0.091788 |
| T | 0.073713 |
| U | 0.055773 |
| V | 0.047833 |
| W | 0.040705 |
| X | 0.042577 |
| Y | 0.044449 |
| Z | 0.023268 |

---

## Multisig Probes

All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428...987003 | 2 | true |
| A-G | 0xf56c4a1c...c0096 | 2 | true |
| Y-Z | 0xd3ffe181...b883 | 2 | true |
| S-T | 0x3b1c3ae9...7883 | 2 | true |
| V-W | 0x40fad7b4...eb6d | 2 | true |

All multisigs require 2-of-N signatures. All healthy.

---

## MNX Markets

`https://testnet.mnx.fi/api/markets` — **unavailable** (returns HTTP 404).
The site `https://testnet.mnx.fi` is reachable (Next.js app, title "MNX - The AI Exchange") but the `/api/markets` endpoint does not exist on the testnet instance.

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,550 stars — Machine Learning Toolkit for Kubernetes
- **plurigrid/asi**: 14 stars — topological chemputer (pushed 2026-03-30)
- **bmorphism**: 97 repos, most active individual in the sweep
- **bob**: 12.657 APT — highest balance in Hamming swarm
- **F, J, L**: each hold ~1.9-2.0 APT
