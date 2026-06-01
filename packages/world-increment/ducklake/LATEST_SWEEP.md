# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-07

## Sweep Metadata
- **Date:** 2026-05-07
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 42 |
| Total Repo Snapshots | 993 |
| Sources Covered | 3 orgs + 8 users |

### Sources Queried

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| kubeflow | org | 100 | 94,552 |
| migalkin | user (zubyul social) | 64 | 822 |
| bmorphism | user | 207 | 351 |
| AustinCStone | user (zubyul social) | 89 | 309 |
| plurigrid | org | 210 | 116 |
| zubyul | user | 53 | 27 |
| TeglonLabs | org | 111 | 16 |
| DJedamski | user (zubyul social) | 24 | 16 |
| wasita | user (zubyul social) | 63 | 9 |
| kristinezheng | user (zubyul social) | 38 | 0 |
| M1shaaa | user (zubyul social) | 34 | 0 |
| **TOTAL** | | **993** | **96,218** |

### GF(3) World Increment Distribution

| trit | color | name | count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 13 |
| 1 | `#b8bb26` | PLUS | 15 |
| -1 | `#cc241d` | MINUS | 14 |
| **total** | | | **42** |

GF(3) assignment rule:
- `id % 3 == 0` → trit=0, `#d3869b` ERGODIC
- `id % 3 == 1` → trit=1, `#b8bb26` PLUS
- `id % 3 == 2` → trit=-1, `#cc241d` MINUS

### Top Repos by Source

#### kubeflow (100 repos, 94,552 ★)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| kubeflow | — | 15,625 | 2026-05-07 |
| pipelines | Python | 4,136 | 2026-05-07 |
| spark-operator | Python | 3,124 | 2026-05-05 |
| trainer | Go | 2,095 | 2026-05-07 |
| katib | Python | 1,683 | 2026-05-07 |
| examples | Jsonnet | 1,461 | 2025-04-14 |
| mcp-apache-spark-history-server | Python | 166 | 2026-05-05 |

#### bmorphism (207 repos, 351 ★)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| ocaml-mcp-sdk | OCaml | 60 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| Gay.jl | Julia | 1 | 2026-05-07 |
| nanoclj-zig | Zig | 0 | 2026-05-07 |
| boxxy | Move | 0 | 2026-04-30 |

#### migalkin (64 repos, 822 ★)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| NodePiece | Python | 144 | 2022-02-02 |
| StarE | Python | 89 | 2023-12-01 |
| kgcourse2021 | HTML | 25 | 2025-08-04 |
| NBFNet_mlx | Python | 10 | 2024-03-02 |

#### plurigrid (210 repos, 116 ★)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| asi | HTML | 21 | 2026-04-26 |
| ontology | JavaScript | 7 | 2025-05-27 |
| zig-syrup | Zig | 2 | 2026-04-30 |
| gorj | Clojure | 0 | 2026-05-07 |

#### AustinCStone (89 repos, 309 ★)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| TextGAN | Python | 92 | 2016-10-04 |
| StereoVisionMRF | Python | 11 | 2016-01-10 |
| EpsteinSearch | Python | 0 | 2026-02-11 |

### Notable Recent Events

**bmorphism** (recent public events):
- `CreateEvent` → `bmorphism/nanoclj-zig` (2026-05-07)
- `WatchEvent` → `scicloj/janqua`, `DavidJaz/DynamicalSystemsBook`
- `ForkEvent` → `DavidJaz/DynamicalSystemsBook`, `rmloveland/edwin-external-scheme`
- `PushEvent` × multiple → `plurigrid/zig-syrup`, `bmorphism/boxxy`

**zubyul** (recent public events):
- **29 events on `plurigrid/gorj` today** (hourly PR cadence, world-increment loop)
- `PullRequestEvent` on `plurigrid/horse` (2026-05-07)
- Extremely active — world-increment agent in continuous loop

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

**Node:** `fullnode.mainnet.aptoslabs.com`  
**Query time:** 2026-05-07 ~17:00Z  
**Result:** All 28 addresses returned **0.0 APT** — `0x1::coin::CoinStore<AptosCoin>` resource absent.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z (26) | 0x8699…7af0 | 0.0 each |

All hamming-swarm wallets have no funded AptosCoin CoinStore on mainnet. These addresses are likely devnet/testnet assignments or unfunded mainnet accounts.

### Multisig Contract Probes

**5/5 contracts healthy.** All return `num_signatures_required = 2`.

| Pair | Address | sigs_required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4...003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...b6d | 2 | ✓ HEALTHY |

All pairs use 2-of-N multisig. Consistent threshold across the swarm.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE — SPA (no REST API)**

`https://testnet.mnx.fi` is a Next.js client-rendered SPA. API paths probed:
- `/api/markets` → HTML
- `/api/v1/markets` → HTML  
- `/api/tickers` → HTML

Market data is not extractable without headless browser execution. `mnx_snapshots` table has 0 rows.

---

## DuckDB Ducklake Table Counts

| Table | Rows |
|-------|------|
| world_increments | 42 |
| repo_snapshots | 993 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

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

---

*Autonomous sweep by world-increment-sweep + hamming-swarm-snapshot agent.*  
*GF(3) color chain: ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d*
