# World-Increment Sweep + Hamming Swarm Snapshot — 2026-08-02

## Sweep Metadata
- **Date:** 2026-08-02
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 24 |
| Total Repo Snapshots (cumulative) | 1063 |
| New repo_snapshots this run | 119 |
| Aptos wallets probed | 28 |
| Multisig contracts probed | 5 |
| MNX markets | unavailable (SPA) |
| Sources Covered | 3 orgs + 8 users + zubyul social graph (5) |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color — this increment

| Increment ID | Source | GF3 Trit | Color | Name |
|---|---|---|---|---|
| 24 (this run) | github_sweep | 0 | `#d3869b` | **ERGODIC** |

GF(3) rule: id%3==0 → ERGODIC #d3869b · id%3==1 → PLUS #b8bb26 · id%3==2 → MINUS #cc241d

### Repos indexed this run

| Source | Type | Repos |
|---|---|---|
| plurigrid | org | 51 |
| kubeflow | org | 16 |
| TeglonLabs | org | 5 |
| bmorphism | user | 12 |
| zubyul | user | 10 |
| migalkin | social graph | 6 |
| DJedamski | social graph | 4 |
| wasita | social graph | 5 |
| kristinezheng | social graph | 3 |
| M1shaaa | social graph | 3 |
| AustinCStone | social graph | 3 |
| **This run total** | | **119** |

### Notable repos (most recently active)

| Repo | Lang | ★ | Open Issues | Last Push |
|---|---|---|---|---|
| plurigrid/gorj | Clojure | 1 | 1585 | 2026-08-02 |
| plurigrid/place | TeX | 1 | 15 | 2026-08-02 |
| bmorphism/anti-bullshit-mcp-server | JS | 23 | 1 | 2026-08-02 |
| kubeflow/katib | Python | 1694 | 105 | 2026-08-01 |
| kubeflow/spark-operator | Python | 3142 | 110 | 2026-08-01 |
| kubeflow/kubeflow | — | 15803 | 0 | 2026-08-01 |
| kubeflow/pipelines | Python | 4173 | 511 | 2026-08-01 |
| bmorphism/Gay.jl | Julia | 2 | 188 | 2026-07-21 |
| plurigrid/eirobri | Clojure | 0 | 31 | 2026-07-21 |
| migalkin/kgcourse2021 | HTML | 24 | 0 | 2026-07-10 |
| migalkin/NodePiece | Python | 144 | 0 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 5 | 2025-03-03 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses queried (`alice`, `bob`, `A`–`Z`) via Aptos fullnode.  
**Result: all wallets show 0.0 APT** — `CoinStore<AptosCoin>` resource present but coin value = 0.

| World | Address (truncated) | Balance (APT) |
|---|---|---|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…2d5d | 0.0 |
| A | 0x8699…e9d7a | 0.0 |
| B–Z (24 more) | … | 0.0 each |

### Multisig Contract Probes

`0x1::multisig_account::num_signatures_required` called for all 5 pairs. **All healthy — 2-of-2.**

| Pair | Address (truncated) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4…7003 | 2 | ✅ |
| A-G | 0xf56c…0096 | 2 | ✅ |
| Y-Z | 0xd3ff…b883 | 2 | ✅ |
| S-T | 0x3b1c…7883 | 2 | ✅ |
| V-W | 0x40fa…eb6d | 2 | ✅ |

### MNX Markets (`testnet.mnx.fi`)

**Status: Unavailable as data API.**  
`testnet.mnx.fi/api/markets` returns the full Next.js SPA shell — no public JSON endpoint detected. `mnx_snapshots` table has 0 rows.

---

## DuckDB Table State

```
world_increments:  24 rows   (cumulative)
repo_snapshots:  1063 rows   (cumulative, +119 this run)
aptos_snapshots:   28 rows   (this run)
multisig_probes:    5 rows   (this run)
mnx_snapshots:      0 rows   (SPA, no API)
```

DB path: `packages/world-increment/ducklake/world-increments.duckdb`

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
