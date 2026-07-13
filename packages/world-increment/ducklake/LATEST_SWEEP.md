# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-13

## Sweep Metadata
- **Date:** 2026-07-13T03:13Z
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried (2026-07-13)

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 13 |
| kubeflow | org | 11 |
| TeglonLabs | org | 5 |
| bmorphism | user | 8 |
| zubyul | user | 7 |
| migalkin | social graph | 4 |
| DJedamski | social graph | 2 |
| wasita | social graph | 3 |
| kristinezheng | social graph | 1 |
| M1shaaa | social graph | 2 |
| AustinCStone | social graph | 3 |
| **Total** | | **59 new** |

### Notable Repos (Most Active / Highest Stars)

| Repo | Stars | Forks | Last Push |
|------|-------|-------|-----------|
| kubeflow/kubeflow | 15,772 | 2,685 | 2026-07-10 |
| kubeflow/pipelines | 4,169 | 2,031 | 2026-07-12 |
| kubeflow/spark-operator | 3,137 | 1,500 | 2026-07-12 |
| kubeflow/trainer | 2,137 | 983 | 2026-07-10 |
| kubeflow/katib | 1,690 | 532 | 2026-07-10 |
| kubeflow/community-distribution | 1,029 | 1,071 | 2026-07-12 |
| migalkin/NodePiece | 144 | 21 | 2026-05-07 |
| AustinCStone/TextGAN | 92 | 30 | 2025-03-03 |
| migalkin/StarE | 89 | 16 | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | 2 | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | 22 | 7 | 2026-01-16 |
| plurigrid/asi | 30 | 9 | 2026-07-10 |
| plurigrid/gorj | 1 | 0 | 2026-07-13 (1,143 open issues) |

### Most Recently Pushed

| Repo | Pushed At |
|------|-----------|
| kubeflow/sdk | 2026-07-13T00:57:45Z |
| bmorphism/Gay.jl | 2026-07-13T00:30:18Z |
| plurigrid/gorj | 2026-07-13T00:18:02Z |
| kubeflow/mcp-server | 2026-07-12T20:36:22Z |
| kubeflow/pipelines | 2026-07-12T07:25:10Z |

### GF(3) Trit Distribution (This Sweep)
- ERGODIC (trit=0, #d3869b): 27 increments
- PLUS (trit=1, #b8bb26): 28 increments
- MINUS (trit=-1, #cc241d): 27 increments

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (A–Z + alice + bob)

**Status:** Aptos mainnet fullnode API blocked by environment proxy — balance queries returned empty for all 28 addresses. Addresses recorded in `aptos_snapshots` with NULL balance_apt.

| World | Address (truncated) |
|-------|---------------------|
| alice | 0xc793…cc7b |
| bob | 0x0a3c…512d |
| A | 0x8699…9d7a |
| B–Z | see DB |

### Multisig Contract Probes — 5/5 HEALTHY ✓

All 5 contracts respond and require **2 signatures**.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4…7003 | 2 | ✓ healthy |
| A-G | 0xf56c…0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff…b883 | 2 | ✓ healthy |
| S-T | 0x3b1c…7883 | 2 | ✓ healthy |
| V-W | 0x40fa…eb6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

**Status:** Vercel authentication wall — no unauthenticated API access possible. `mnx_snapshots` table empty this run.

---

## DuckDB Cumulative State

**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Description |
|-------|-------------|
| world_increments | GF(3)-colored event log per repo push event |
| repo_snapshots | Full repo metadata per increment |
| aptos_snapshots | Hamming swarm wallet addresses (balances NULL — proxy blocked) |
| multisig_probes | Multisig contract health (all 2-of-2, healthy) |
| mnx_snapshots | MNX market data (empty — auth wall) |

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

## Notable Highlights (2026-07-13 Sweep)
- **kubeflow/kubeflow**: 15,772 stars — flagship ML platform (+207 from April sweep)
- **kubeflow/pipelines**: 4,169 stars — most popular ML pipeline for Kubernetes
- **kubeflow/spark-operator**: 3,137 stars — Kubernetes operator for Apache Spark
- **kubeflow/sdk** just pushed 58 min before sweep — active kubeflow development
- **bmorphism/Gay.jl**: 187 open issues — extremely active GF(3) color work
- **plurigrid/gorj**: 1,143 open issues — this repo is highly active
- **All 5 Hamming multisig contracts**: 2-of-2, healthy — swarm coordination intact
- **Aptos API**: blocked by proxy — needs allowlist update for future sweeps
- **MNX testnet**: behind Vercel auth — needs credentials for market data
