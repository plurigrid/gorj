# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-20

## Sweep Metadata
- **Date:** 2026-04-20
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
- **Orgs:** plurigrid, kubeflow, TeglonLabs
- **Users:** bmorphism, zubyul
- **Social graph (zubyul):** migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone
- **Events:** bmorphism (18 recent public events), zubyul (20 recent public events)

> Note: GitHub API core endpoint was rate-limited (0/60 remaining); data collected via Search API (separate 10 req/min limit).

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 64 |
| Total Repo Snapshots | 54 |
| Sources Covered | 3 orgs + 8 users |
| Event Records | 10 (5 bmorphism + 5 zubyul) |

### Repo Stats by Source

| Source | Type | Repos | Total Stars | Total Forks |
|--------|------|------:|------------:|------------:|
| kubeflow | org | 10 | 29,913 | 9,860 |
| migalkin | user | 2 | 99 | 17 |
| bmorphism | user | 9 | 89 | 10 |
| plurigrid | org | 18 | 26 | 12 |
| TeglonLabs | org | 4 | 2 | 2 |
| zubyul | user | 5 | 1 | 1 |
| others | users | 6 | 0 | 0 |

### Top Repos by Stars
| Repo | Language | Stars | Pushed |
|------|----------|------:|--------|
| kubeflow/kubeflow | — | 15,585 | 2026-01-05 |
| kubeflow/pipelines | Python | 4,124 | 2026-04-18 |
| kubeflow/spark-operator | Python | 3,116 | 2026-04-16 |
| kubeflow/trainer | Go | 2,086 | 2026-04-17 |
| kubeflow/katib | Python | 1,680 | 2026-04-14 |
| migalkin/StarE | Python | 89 | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | OCaml | 60 | 2026-03-16 |
| plurigrid/asi | HTML | 17 | 2026-04-20 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |

### Active Repos (pushed within 48h of sweep, 2026-04-20)
- `plurigrid/gorj` — 235 open issues, this repo!
- `plurigrid/asi` — 17★, "everything is topological chemputer!"
- `plurigrid/bci-blue-share` — BCI signal infrastructure
- `plurigrid/nanoclj-zig` — NaN-boxed Clojure in Zig, 21 open issues
- `bmorphism/Gay.jl` — Julia wide-gamut deterministic colors, 187 open issues
- `M1shaaa/M1shaaa` — profile updated 2026-04-20T02:25:48Z (same day!)
- `kubeflow/pipelines` — 4,124★ pushed 2026-04-18

### GF(3) Trit Color Chain (64 world-increments)

| GF(3) Name | Hex     | Count |
|-----------|---------|------:|
| ERGODIC (trit=0) | #d3869b | 21 |
| PLUS (trit=1) | #b8bb26 | 22 |
| MINUS (trit=-1) | #cc241d | 21 |

Assignment: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

### Event Highlights
**bmorphism recent activity:**
- ForkEvent: `chrisreade/PenroseKiteDart`, `janestreet/parallel`
- ReleaseEvent: `bmorphism/tree-sitter-hy`
- PushEvents: `plurigrid/nanoclj-zig`
- PullRequestReviewEvent: `plurigrid/nash-portal`

**zubyul recent activity:**
- PullRequestEvents + CreateEvents: `plurigrid/gorj` (multiple branches)
- PushEvents: `plurigrid/bci-blue-share` (6 pushes)
- CreateEvent: `plurigrid/asi`
- DeleteEvent: `plurigrid/bci-blue-share`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, Mainnet)

All 28 addresses queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version ~4,937,447,026. All returned `resource_not_found` — accounts have **0.0 APT** (no CoinStore initialized = unfunded on mainnet).

| Range | Status |
|-------|--------|
| alice, bob | 0.0 APT (resource_not_found) |
| A through Z (26 addresses) | 0.0 APT (resource_not_found) |

### Multisig Contract Probes (5 pairs)

All 5 probed via `0x1::multisig_account::num_signatures_required`. All **healthy**, all require **2 signatures**.

| Pair | Address | Sigs Required | Healthy |
|------|---------|:-------------:|:-------:|
| A-B | 0x0da4…7003 | 2 | ✓ |
| A-G | 0xf56c…0096 | 2 | ✓ |
| Y-Z | 0xd3ff…b883 | 2 | ✓ |
| S-T | 0x3b1c…7883 | 2 | ✓ |
| V-W | 0x40fa…eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA. Endpoints `/api/markets`, `/api/v1/markets`, `/api/tokens` all return the HTML shell. No REST API discovered. Market data recorded as **unavailable**.

---

## DuckDB Tables

| Table | Rows | Description |
|-------|-----:|-------------|
| `world_increments` | 64 | GF(3) trit-colored event log (54 repo + 10 events) |
| `repo_snapshots` | 54 | GitHub repo metadata (stars, forks, language, pushed_at) |
| `aptos_snapshots` | 28 | Hamming swarm wallet balances (all 0.0 APT) |
| `multisig_probes` | 5 | Multisig signature requirements (all 2-of-N, healthy) |
| `mnx_snapshots` | 1 | MNX market data (SPA only, unavailable) |

```sql
-- Schema
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

## Notable Highlights
- **kubeflow/kubeflow**: 15,585★ — flagship ML platform for Kubernetes
- **plurigrid/gorj**: This repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **plurigrid/asi**: 17★ pushed 2026-04-20T01:01:28Z (same day as sweep)
- **bmorphism/Gay.jl**: 187 open issues — active wide-gamut deterministic color work
- **M1shaaa**: profile README updated same day as sweep (2026-04-20T02:25:48Z)
- **All 5 multisigs**: 2-of-N threshold, all healthy on Aptos mainnet
- **Hamming swarm**: 28 addresses, 0 APT each — swarm is pre-funded
