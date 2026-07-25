# World-Increment Sweep — 2026-07-25

## Sweep Metadata
- **Date:** 2026-07-25
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (cumulative in DB after this run)

| Metric | Value |
|--------|-------|
| Total World Increments | 367 |
| Total Repo Snapshots | 1288 |
| Aptos Snapshots | 28 |
| Multisig Probes | 5 |
| Sources This Run | 3 orgs + 8 users (344 repos) |

---

## GF(3) Color Chain (this run — 344 increments, id 1..344)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 1 | `#b8bb26` | **PLUS** | 115 |
| -1 | `#cc241d` | **MINUS** | 115 |
| 0 | `#d3869b` | **ERGODIC** | 114 |

GF(3) assignment: `id%3==0 → ERGODIC, id%3==1 → PLUS, id%3==2 → MINUS`

---

## Repo Counts by Source (this run)

| Source | Type | Repos | Latest Push |
|--------|------|-------|-------------|
| plurigrid | org | 100 | 2026-07-25T05:12:33Z |
| bmorphism | user | 100 | 2026-07-25T00:38:43Z |
| zubyul | user | 49 | 2026-07-18T12:02:57Z |
| kubeflow | org | 30 | 2026-07-25T03:08:10Z |
| wasita | social-graph | 12 | 2026-07-21T15:55:45Z |
| migalkin | social-graph | 19 | 2025-08-04T03:01:46Z |
| M1shaaa | social-graph | 8 | 2026-04-13T13:19:39Z |
| AustinCStone | social-graph | 10 | 2026-04-01T07:39:41Z |
| TeglonLabs | org | 5 | 2026-06-08T19:03:03Z |
| kristinezheng | social-graph | 5 | 2026-07-01T20:57:48Z |
| DJedamski | social-graph | 6 | 2023-04-21T01:42:35Z |
| **TOTAL** | | **344** | |

**Hot sources (pushed within 24h):** plurigrid, kubeflow, bmorphism

---

## Language Distribution (cumulative DB)

| Language | Repos |
|----------|-------|
| Python | 217 |
| Rust | 57 |
| JavaScript | 52 |
| HTML | 51 |
| Go | 48 |
| TypeScript | 45 |
| Jupyter Notebook | 38 |
| Clojure | 29 |
| R | 22 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

All 28 addresses returned `Resource not found` from Aptos mainnet — no `CoinStore<AptosCoin>` resource on any address (unfunded/uninitialized). Stored as NULL in `aptos_snapshots`.

### Multisig Contract Probes — ALL HEALTHY

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428...987003 | 2 | HEALTHY |
| A-G | 0xf56c4a1c...c0096 | 2 | HEALTHY |
| Y-Z | 0xd3ffe181...75b883 | 2 | HEALTHY |
| S-T | 0x3b1c3ae9...ed7883 | 2 | HEALTHY |
| V-W | 0x40fad7b4...80eb6d | 2 | HEALTHY |

All multisig pairs require 2-of-N signatures and are responsive on mainnet.

### MNX Markets (testnet.mnx.fi)

**Unavailable** — `testnet.mnx.fi` is a Next.js SPA with no accessible REST endpoints. Both `/api/markets` and `/api/v1/markets` return the HTML shell. `mnx_snapshots` table has 0 rows.

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
