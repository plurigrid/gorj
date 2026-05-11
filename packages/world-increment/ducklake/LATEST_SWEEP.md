# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-11

## Sweep Metadata
- **Date:** 2026-05-11
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **GF(3) Increment id=12:** trit=1, color=#b8bb26 (PLUS)

---

## JOB 1: GitHub Social Graph Sweep

**Total repos snapshotted this run:** 391 across 11 sources

### Source Counts
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 48 |
| kubeflow | org | 100 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| DJedamski | user | 6 |
| wasita | user | 11 |
| kristinezheng | user | 6 |
| M1shaaa | user | 8 |
| AustinCStone | user | 40 |
| **TOTAL** | | **391** |

### Top 20 Repos by Stars (2026-05-11 sweep)
| org/user | repo | lang | ⭐ | forks | last push |
|----------|------|------|-----|-------|-----------|
| plurigrid | kubeflow | — | 15630 | 2648 | 2026-05-07 |
| plurigrid | pipelines | Python | 4138 | 1991 | 2026-05-11 |
| plurigrid | spark-operator | Python | 3125 | 1480 | 2026-05-08 |
| plurigrid | trainer | Go | 2097 | 948 | 2026-05-09 |
| plurigrid | katib | Python | 1683 | 522 | 2026-05-09 |
| plurigrid | examples | Jsonnet | 1462 | 756 | 2025-04-14 |
| plurigrid | manifests | YAML | 1016 | 1062 | 2026-05-08 |
| plurigrid | arena | Go | 810 | 190 | 2026-05-07 |
| plurigrid | kale | Python | 685 | 156 | 2026-05-11 |
| plurigrid | mpi-operator | Go | 526 | 235 | 2026-05-11 |
| plurigrid | fairing | Jsonnet | 337 | 143 | 2022-04-11 |
| plurigrid | pytorch-operator | Jsonnet | 310 | 143 | 2021-12-01 |
| plurigrid | community | Jsonnet | 196 | 257 | 2026-05-11 |
| plurigrid | website | HTML | 184 | 919 | 2026-05-08 |
| plurigrid | kfp-tekton | TypeScript | 182 | 123 | 2024-11-19 |
| plurigrid | kfctl | Go | 182 | 134 | 2023-08-15 |
| plurigrid | hub | Go | 175 | 178 | 2026-05-11 |
| plurigrid | example-seldon | Jupyter Notebook | 172 | 56 | 2021-12-01 |
| plurigrid | mcp-apache-spark-history-server | Python | 168 | 58 | 2026-05-11 |
| migalkin | NodePiece | Python | 144 | 21 | 2022-02-02 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances
Queried via `0x1::coin::balance` view function — `fullnode.mainnet.aptoslabs.com`

| World | APT Balance |
|-------|------------|
| bob | 12.657007 |
| F | 1.960516 |
| L | 1.927269 |
| J | 1.895093 |
| alice | 0.436434 |
| O | 0.210136 |
| K | 0.161961 |
| P | 0.140136 |
| M | 0.112285 |
| N | 0.106121 |
| Q | 0.103240 |
| S | 0.091788 |
| R | 0.090217 |
| T | 0.073713 |
| U | 0.055773 |
| A | 0.051767 |
| V | 0.048833 |
| Y | 0.044449 |
| X | 0.042577 |
| W | 0.040705 |
| B | 0.036256 |
| Z | 0.024268 |
| D | 0.011629 |
| C | 0.010185 |
| E | 0.009372 |
| H | 0.001681 |
| I | 0.000681 |
| G | 0.000681 |

**Total swarm:** ~20.13 APT  
**Top holder:** bob (12.66 APT, ~62.9%)  
**Active wallets:** 28/28

### Multisig Contract Probes — All 5/5 Healthy
All contracts report `sigs_required = 2` (2-of-N threshold).

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...87003 | 2 | ✓ healthy |
| A-G | 0xf56c4a1c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ healthy |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)
**Status: API unavailable** — Next.js SPA only. No data endpoints accessible at `/api/markets` or `/api/v1/markets` without browser execution. No records inserted into `mnx_snapshots`.

---

## DuckDB Table Updates (2026-05-11)
| Table | New Rows | Total (cumulative) |
|-------|----------|-------------------|
| world_increments | 1 | 24+ |
| repo_snapshots | 391 | 1335 |
| aptos_snapshots | 28 | 28 |
| multisig_probes | 5 | 5 |
| mnx_snapshots | 0 | 0 |

---

## GF(3) Color Chain
| trit | color | name |
|------|-------|------|
| 0 | #d3869b | ERGODIC |
| 1 | #b8bb26 | PLUS |
| -1 | #cc241d | MINUS |

Assignment: `id % 3 == 0 → ERGODIC`, `id % 3 == 1 → PLUS`, `id % 3 == 2 → MINUS`

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name, actor, snapshot_hash)
repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues, pushed_at, description)
aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```
