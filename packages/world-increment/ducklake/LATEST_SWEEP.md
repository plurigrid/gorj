# World-Increment Sweep + Hamming Snapshot — 2026-07-04

## Sweep Metadata
- **Date:** 2026-07-04
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 391 |
| Total Repo Snapshots | 391 |
| Sources Covered | 3 orgs + 8 users |

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social | 19 |
| AustinCStone | social | 40 |
| wasita | social | 11 |
| kristinezheng | social | 5 |
| DJedamski | social | 6 |
| M1shaaa | social | 8 |
| **TOTAL** | | **391** |

### Top 10 Repos by Stars
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,761 | — |
| kubeflow/pipelines | 4,169 | Python |
| kubeflow/spark-operator | 3,132 | Python |
| kubeflow/trainer | 2,129 | Go |
| kubeflow/katib | 2,076 | Go |
| kubeflow/manifests | 1,434 | — |
| kubeflow/website | 370 | HTML |
| kubeflow/arena | 328 | Go |
| kubeflow/fairing | 321 | Python |
| migalkin/NodePiece | 143 | Python |

### Notable Highlights
- **TeglonLabs/jank-crane** (C++): crane-jank converged-IR hub, GF3 convergence maps — pushed 2026-06-08
- **bmorphism**: 100 repos, actively pushing across OCaml, Zig, and MCP ecosystem
- **zubyul/wasita (kristinezheng)**: active research group with cognitive science repos (Lookit studies)
- **M1shaaa**: profile pushed today (2026-07-04T02:34:32Z) — active

### GF(3) Color Chain Distribution
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 137 |
| +1 | `#b8bb26` | PLUS | 139 |
| -1 | `#cc241d` | MINUS | 138 |

GF(3) assignment: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice–Z, 28 wallets)
All 28 wallets queried against `fullnode.mainnet.aptoslabs.com`.
**Result:** 0 funded wallets — all accounts returned 404 (unfunded on mainnet).

### Multisig Probes (5 pairs)
All probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...987003 | 2 | ✅ |
| A-G | 0xf56c4a1c...c0096 | 2 | ✅ |
| Y-Z | 0xd3ffe181...75b883 | 2 | ✅ |
| S-T | 0x3b1c3ae9...ed7883 | 2 | ✅ |
| V-W | 0x40fad7b4...80eb6d | 2 | ✅ |

**All 5 multisig contracts healthy** — 2-of-2 threshold confirmed on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)
Probed `/api/markets`, `/api/v1/markets`, `/markets`, `/api/tickers`, `/`.
**Result:** SPA only — no public JSON API. `mnx_snapshots` table empty.

---

## DuckDB Schema
Database: `packages/world-increment/ducklake/world-increments.duckdb`

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

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 391 | GF3-colored event log |
| `repo_snapshots` | 391 | GitHub repo metadata |
| `aptos_snapshots` | 28 | Wallet balances (all null/unfunded) |
| `multisig_probes` | 5 | Multisig health (all healthy, 2-of-2) |
| `mnx_snapshots` | 0 | MNX market data (SPA, unavailable) |
