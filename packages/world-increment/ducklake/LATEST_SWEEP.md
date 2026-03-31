# LATEST_SWEEP.md
Generated: 2026-03-31

## GitHub Social Graph Sweep Summary

### Sources Swept
| # | Source | Type | Repos | GF(3) Trit | GF(3) Color | GF(3) Name |
|---|--------|------|-------|-----------|-------------|------------|
| 1 | plurigrid | org | 93 | 0 | #d3869b | ERGODIC |
| 2 | kubeflow | org | 46 | 1 | #b8bb26 | PLUS |
| 3 | TeglonLabs | org | 3 | -1 | #cc241d | MINUS |
| 4 | bmorphism | user | 97 | 0 | #d3869b | ERGODIC |
| 5 | zubyul | user | 44 | 1 | #b8bb26 | PLUS |
| 6 | migalkin | user_social | 19 | -1 | #cc241d | MINUS |
| 7 | DJedamski | user_social | 6 | 0 | #d3869b | ERGODIC |
| 8 | wasita | user_social | 9 | 1 | #b8bb26 | PLUS |
| 9 | kristinezheng | user_social | 6 | -1 | #cc241d | MINUS |
| 10 | M1shaaa | user_social | 8 | 0 | #d3869b | ERGODIC |
| 11 | AustinCStone | user_social | 40 | 1 | #b8bb26 | PLUS |

**Total repos snapshotted: 371**

### Top 10 Repos by Stars
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15547 | N/A |
| kubeflow/pipelines | 4114 | Python |
| kubeflow/spark-operator | 3110 | Python |
| kubeflow/trainer | 2071 | Go |
| kubeflow/katib | 1673 | Python |
| kubeflow/examples | 1459 | Jsonnet |
| kubeflow/manifests | 1006 | YAML |
| kubeflow/arena | 810 | Go |
| kubeflow/kale | 681 | Python |
| kubeflow/mpi-operator | 519 | Go |

## Aptos Balance Snapshot (Hamming Swarm)

All 28 wallets queried via Aptos mainnet fullnode. All returned 0.0 APT
(API returns `resource_not_found` indicating no CoinStore or zero balance).

| World Label | Address (short) | Balance APT |
|-------------|----------------|-------------|
| alice | 0xc793acde...24cc7b | 0.0 |
| bob | 0x0a3c00c5...512d5d | 0.0 |
| A | 0x8699edc0...be9d7a | 0.0 |
| B | 0x3f892ebe...77cb13 | 0.0 |
| C | 0x38b99e63...91535e | 0.0 |
| D | 0xf7765624...fcfdd1 | 0.0 |
| E | 0xdc1d9d53...958d36 | 0.0 |
| F | 0x18a14b5b...c3cf71 | 0.0 |
| G | 0x69a394c0...cc7f32 | 0.0 |
| H | 0xce67c327...e5300f | 0.0 |
| I | 0x070fe5d7...0c1fc9 | 0.0 |
| J | 0x4d964db8...e87f54 | 0.0 |
| K | 0xa732040a...425dc4 | 0.0 |
| L | 0x7c2eaeaf...37eba9 | 0.0 |
| M | 0x6fed37a7...b7f2e9 | 0.0 |
| N | 0xe7dde6da...551b2c | 0.0 |
| O | 0x73252b60...25a89d | 0.0 |
| P | 0x6218792d...1ec948 | 0.0 |
| Q | 0xac40fa50...5c89a9 | 0.0 |
| R | 0x7ce605cc...d76e10 | 0.0 |
| S | 0xb8753014...9d0386 | 0.0 |
| T | 0x35781dc0...3f4588 | 0.0 |
| U | 0x75860da4...ef9956 | 0.0 |
| V | 0xb59dd817...9af2c3 | 0.0 |
| W | 0x5f32aef7...ccc7b0 | 0.0 |
| X | 0xa95cbbd1...33047d | 0.0 |
| Y | 0xd8e32848...2444c4 | 0.0 |
| Z | 0x7af0ef6e...4e197c | 0.0 |

## Multisig Probe Results

| Pair | Address (short) | Sigs Required | Healthy |
|------|----------------|---------------|----------|
| A-B | 0x0da4f428...987003 | 2 | YES |
| A-G | 0xf56c4a1c...bc0096 | 2 | YES |
| Y-Z | 0xd3ffe181...75b883 | 2 | YES |
| S-T | 0x3b1c3ae9...ed7883 | 2 | YES |
| V-W | 0x40fad7b4...80eb6d | 2 | YES |

## MNX Markets Status

All three endpoints tested returned HTML (not JSON market data):
- `https://testnet.mnx.fi/api/markets` - HTML (SPA web app)
- `https://testnet.mnx.fi/api/tickers` - HTML (SPA web app)
- `https://testnet.mnx.fi/api/v1/markets` - HTML (SPA web app)

**Status: UNAVAILABLE** - testnet.mnx.fi serves a React SPA, not a REST API at these paths.

## DuckDB Schema Overview

Database: `packages/world-increment/ducklake/world-increments.duckdb`

### Tables

| Table | Row Count | Description |
|-------|-----------|-------------|
| world_increments | 11 | GF(3) color-chained increment events per source |
| repo_snapshots | 371 | Full repo metadata per source |
| aptos_snapshots | 28 | Aptos mainnet wallet balance snapshots |
| multisig_probes | 5 | Multisig contract signature threshold probes |
| mnx_snapshots | 1 | MNX market data (unavailable, placeholder) |

### GF(3) Color Chain Rule
- id%3==1 (mod after 1-indexed): trit=0, color=#d3869b (ERGODIC)
- id%3==2: trit=1, color=#b8bb26 (PLUS)
- id%3==0: trit=-1, color=#cc241d (MINUS)

### world_increments Columns
`id, timestamp, gf3_trit, gf3_color, gf3_name, source_type, source_name, event_type, repo_name, actor, snapshot_hash`

### repo_snapshots Columns
`id, timestamp, increment_id, org_or_user, repo_name, full_name, language, stars, forks, open_issues, pushed_at, description`

### aptos_snapshots Columns
`timestamp, world, address, balance_apt`

### multisig_probes Columns
`timestamp, pair, address, sigs_required, healthy`

### mnx_snapshots Columns
`timestamp, ticker, name, category, price, change_pct`
