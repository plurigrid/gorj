# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-25

## Sweep Metadata
- **Date:** 2026-06-25
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Increment IDs:** 13–81 (69 new world_increments)
- **Repo Snapshot IDs:** 474–542 (69 new repo_snapshots)

---

## GitHub Social Graph Sweep

**69 repos** catalogued across 11 sources.

### GF(3) Color Chain Distribution (today's sweep, inc_ids 13–81)
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 23 |
| 1 | `#b8bb26` | PLUS | 23 |
| -1 | `#cc241d` | MINUS | 23 |

GF(3) assignment rule:
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS

### Repos by Source
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 16 |
| kubeflow | org | 13 |
| bmorphism | user | 12 |
| zubyul | user | 8 |
| TeglonLabs | org | 5 |
| migalkin | user | 4 |
| wasita | user | 3 |
| AustinCStone | user | 2 |
| DJedamski | user | 2 |
| M1shaaa | user | 2 |
| kristinezheng | user | 2 |
| **TOTAL** | | **69** |

### Top Repos by Stars
| Repo | Stars |
|------|-------|
| kubeflow/kubeflow | 15,742 |
| kubeflow/pipelines | 4,157 |
| kubeflow/spark-operator | 3,128 |
| kubeflow/trainer | 2,121 |
| kubeflow/katib | 1,685 |

### Notable Highlights
- **kubeflow/kubeflow**: 15,742 stars — flagship ML platform for Kubernetes
- **plurigrid/gorj**: 806 open issues — highest issue count in plurigrid
- **bmorphism/Gay.jl**: 187 open issues

---

## Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (28 wallets: alice, bob, A–Z)
All 28 wallets returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
No APT CoinStore registered on mainnet for any of the Hamming swarm addresses.
**All balances: 0.0 APT**

### Multisig Contract Probes
All 5 multisig contracts confirmed **healthy**, each requiring exactly **2 signatures**.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428…` | 2 | true |
| A-G | `0xf56c4a1c…` | 2 | true |
| Y-Z | `0xd3ffe181…` | 2 | true |
| S-T | `0x3b1c3ae9…` | 2 | true |
| V-W | `0x40fad7b4…` | 2 | true |

### MNX Markets
`https://testnet.mnx.fi/api/markets` returned **401 Unauthorized** — authentication required.
`mnx_snapshots` table remains empty this sweep.

---

## DB Totals (cumulative after this sweep)
| Table | Rows |
|-------|------|
| world_increments | 92 |
| repo_snapshots | 1,013 |
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
