# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-04  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**DuckDB version:** 1.5.4

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 48 |
| kubeflow | org | 100 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social graph | 19 |
| wasita | social graph | 11 |
| DJedamski | social graph | 6 |
| kristinezheng | social graph | 5 |
| M1shaaa | social graph | 8 |
| AustinCStone | social graph | 40 |
| **TOTAL** | | **391 repos** |

**349 world_increments** inserted (GF3-chained)

### GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 115 |
| +1 | PLUS | `#b8bb26` | 117 |
| -1 | MINUS | `#cc241d` | 117 |

GF(3) assignment: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

### Top 10 Starred Repos

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,761 | — |
| kubeflow/pipelines | 4,169 | Python |
| kubeflow/spark-operator | 3,132 | Python |
| kubeflow/trainer | 2,129 | Go |
| kubeflow/arena | 815 | Go |
| kubeflow/mpi-operator | 529 | Go |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/NodePiece | 144 | Python |
| migalkin/StarE | 89 | Python |
| AustinCStone/StereoVisionMRF | 11 | Python |

### Top Languages (across all snapshotted repos)

| Language | Repo Count |
|----------|-----------|
| Python | 213 |
| Rust | 56 |
| Go | 51 |
| HTML | 51 |
| JavaScript | 48 |
| TypeScript | 46 |
| Jupyter Notebook | 39 |
| Clojure | 30 |
| Jsonnet | 23 |
| Julia | 19 |

### Most Recently Pushed (2026-07-04)

| Repo | Pushed At |
|------|-----------|
| plurigrid/gorj | 2026-07-04T14:16:10Z |
| kubeflow/hub | 2026-07-04T05:35:35Z |
| bmorphism/Gay.jl | 2026-07-04T00:33:17Z |
| kubeflow/website | 2026-07-03T20:27:09Z |
| kubeflow/internal-acls | 2026-07-03T20:27:04Z |

### Notable Highlights
- **bmorphism/Gay.jl** pushed TODAY (2026-07-04) — active development
- **TeglonLabs/jank-crane** pushed 2026-06-08: crane-jank converged-IR hub with GF3 convergence maps
- **wasita/wasita.github.io** pushed 2026-07-02 — active
- **kristinezheng/kristinezheng.github.io** pushed 2026-07-01 — active

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, ledger ~6,099,724,377)

All 28 Hamming swarm addresses returned `resource_not_found` for
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. Accounts likely use
Fungible Asset (FA) storage or hold no APT via the legacy coin module.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...c7b | 0.0 |
| bob | 0x0a3c...d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I–Z | (18 addresses) | 0.0 each |

### Multisig Contract Probes

All 5 multisig pairs are **healthy** — all require 2-of-2 signatures.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | 2 | YES |
| A-G | 0xf56c...096 | 2 | YES |
| Y-Z | 0xd3ff...883 | 2 | YES |
| S-T | 0x3b1c...883 | 2 | YES |
| V-W | 0x40fa...b6d | 2 | YES |

### MNX Markets (testnet.mnx.fi)

**Unavailable** — HTTP 401, Vercel deployment protection (requires visitor password).
No market data extracted this sweep.

---

## DuckDB Table Summary

```
world_increments  : 349 rows   (GF3-chained increment log)
repo_snapshots    : 1270 rows  (full metadata, accumulated across sweeps)
aptos_snapshots   : 28 rows    (hamming swarm alice/bob + A-Z)
multisig_probes   : 5 rows     (2-of-2 multisig health checks)
mnx_snapshots     : 0 rows     (unavailable this sweep)
```

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
