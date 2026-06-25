# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-25

## Sweep Metadata
- **Date:** 2026-06-25
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Source Counts
| Source | Type | Repos |
|--------|------|-------|
| bmorphism | user | 103 |
| plurigrid | org | 102 |
| zubyul | user | 51 |
| kubeflow | org | 50 |
| AustinCStone | user | 42 |
| migalkin | user | 21 |
| wasita | user | 13 |
| M1shaaa | user (social graph) | 10 |
| DJedamski | user (social graph) | 8 |
| TeglonLabs | org | 7 |
| kristinezheng | user (social graph) | 7 |
| **TOTAL** | | **414** |

### Top Languages
| Language | Repos | Total Stars |
|----------|-------|-------------|
| Python | 234 | 31,409 |
| Rust | 57 | 53 |
| HTML | 53 | 696 |
| JavaScript | 53 | 207 |
| Go | 51 | 11,963 |
| TypeScript | 47 | 1,005 |
| Jupyter Notebook | 40 | 991 |
| Clojure | 30 | 6 |
| Jsonnet | 23 | 7,034 |
| Zig | 15 | 17 |

### Most Recently Pushed (Top 10)
| Repo | Stars | Pushed At |
|------|-------|-----------|
| kubeflow/internal-acls | 19 | 2026-06-25T12:46Z |
| kubeflow/sdk | 121 | 2026-06-25T12:44Z |
| plurigrid/gorj | 0 | 2026-06-25T12:13Z |
| kubeflow/community-distribution | 1028 | 2026-06-25T11:31Z |
| kubeflow/docs-agent | 39 | 2026-06-25T05:33Z |
| M1shaaa/M1shaaa | 0 | 2026-06-25T02:52Z |
| bmorphism/Gay.jl | 2 | 2026-06-25T00:40Z |
| kubeflow/pipelines | 4157 | 2026-06-24T18:51Z |
| kubeflow/spark-operator | 3128 | 2026-06-24T16:53Z |
| kubeflow/notebooks | 73 | 2026-06-24T15:34Z |

### GF(3) Color Chain Distribution
| GF3 Name | Color | Trit | Count |
|----------|-------|------|-------|
| ERGODIC | #d3869b | 0 | 138 |
| PLUS | #b8bb26 | +1 | 138 |
| MINUS | #cc241d | -1 | 138 |

### Notable Repos
- **kubeflow/pipelines** — 4,157★ — most starred in sweep, pushed today
- **kubeflow/spark-operator** — 3,128★
- **plurigrid/gorj** — This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring (812 open issues!)
- **plurigrid/asi** — 26★ — everything is topological chemputer
- **bmorphism/Gay.jl** — pushed 2026-06-25 (today)
- **TeglonLabs/jank-crane** — crane-jank converged-IR hub: GF3 convergence maps (C++, 2026-06-08)
- **wasita/proj-template** — pushed 2026-06-19

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)
All 28 addresses returned **no CoinStore resource** on mainnet. These accounts likely use the newer **Fungible Asset (FA)** based APT (`0x1::fungible_asset`) rather than the legacy `0x1::coin::CoinStore<AptosCoin>` interface. Recorded as NULL in aptos_snapshots.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | NULL (no CoinStore) |
| bob | 0x0a3c...512d | NULL |
| A–Z | 26 addresses | NULL (all) |

### Multisig Contract Probes — ✅ ALL HEALTHY
All 5 multisig contracts are live on Aptos mainnet requiring 2 signatures.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✅ |
| A-G | 0xf56c...096 | 2 | ✅ |
| Y-Z | 0xd3ff...883 | 2 | ✅ |
| S-T | 0x3b1c...883 | 2 | ✅ |
| V-W | 0x40fa...b6d | 2 | ✅ |

All 5 probes respond with **2-of-N threshold** — healthy.

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — Site returns Vercel authentication challenge on all probed endpoints (`/`, `/api/markets`, `/api/v1/markets`). No market data extractable without auth token.

---

## DuckDB Table Summary

| Table | Rows |
|-------|------|
| world_increments | 414 |
| repo_snapshots | 414 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

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
