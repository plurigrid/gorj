# World Increment Sweep + Hamming Snapshot
**Run date:** 2026-07-27
**Increment ID:** 13
**GF(3) color:** PLUS (#b8bb26) — trit=1 (13 % 3 = 1)

---

## JOB 1: GitHub Social Graph Sweep

### Sources queried
| Source | Type | Repos captured |
|---|---|---|
| plurigrid | org | 50 |
| bmorphism | user | 50 |
| zubyul | user | 49 |
| AustinCStone | user (social graph) | 20 |
| migalkin | user (social graph) | 19 |
| wasita | user (social graph) | 12 |
| M1shaaa | user (social graph) | 8 |
| DJedamski | user (social graph) | 6 |
| kristinezheng | user (social graph) | 5 |
| **TOTAL** | | **219** |

> Note: `org:kubeflow` and `org:TeglonLabs` were not accessible via direct org-listing API (session-scoped GitHub token returns 403). Used `search_repositories` with `org:`/`user:` qualifiers instead. Previous sweeps had data for these orgs and remain in the DB.

### DuckDB state
- `repo_snapshots` total rows: 1163 (cumulative across all sweeps)
- New rows this sweep: 219 (increment_id=13)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (2026-07-27)
All 28 addresses queried against Aptos mainnet. All return `resource_not_found` — these are uninitialized accounts (CoinStore not registered). Balance = 0.00000000 APT for all.

| World | Address (truncated) | APT Balance |
|---|---|---|
| alice | 0xc793…4cc7b | 0.00000000 |
| bob | 0x0a3c…512d5d | 0.00000000 |
| A–Z (26 addrs) | 0x8699…–0x7af0… | 0.00000000 each |

### Multisig Contract Probes
All 5 multisig contracts respond healthy. All require **2 signatures**.

| Pair | Address (truncated) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4…7003 | 2 | ✅ |
| A-G | 0xf56c…0096 | 2 | ✅ |
| Y-Z | 0xd3ff…b883 | 2 | ✅ |
| S-T | 0x3b1c…7883 | 2 | ✅ |
| V-W | 0x40fa…eb6d | 2 | ✅ |

### MNX Markets (testnet.mnx.fi)
- Site reachable: **HTTP 200**
- API endpoints (`/api/markets`, `/api/v1/markets`): **404** — SPA with client-side routing only
- Status: **unavailable** — no market data extractable via public REST

---

## DuckDB Tables (cumulative)
| Table | Rows |
|---|---|
| world_increments | 24 |
| repo_snapshots | 1163 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

---

## GF(3) Color Chain
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

| ID | GF3 Trit | Color | Name |
|---|---|---|---|
| 11 | -1 | #cc241d | MINUS |
| 12 | 0 | #d3869b | ERGODIC |
| **13** | **+1** | **#b8bb26** | **PLUS** |

GF(3) chain continues: `…MINUS → ERGODIC → PLUS`

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
