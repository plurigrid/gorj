# World-Increment Sweep — 2026-03-31

## Sweep Metadata
- **Date:** 2026-03-31
- **Agent:** world-increment-sweep
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world_increment.db`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 1 |
| Total Repo Snapshots | 422 |
| Total Aptos Snapshots | 28 |
| Total Multisig Probes | 5 |
| MNX Market Snapshots | 2 |
| Sources Covered | 3 orgs + 2 users + 6 social graph users |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain
- `id % 3 == 0` → trit=0 ERGODIC **#d3869b**
- `id % 3 == 1` → trit=1 PLUS **#b8bb26**
- `id % 3 == 2` → trit=-1 MINUS **#cc241d**

### Repo Counts by Source

| Source | Type | Repos | ERGODIC (#d3869b) | PLUS (#b8bb26) | MINUS (#cc241d) |
|--------|------|-------|-------------------|----------------|-----------------|
| plurigrid | org | 100 | 38 | 27 | 35 |
| kubeflow | org | 46 | 13 | 15 | 18 |
| TeglonLabs | org | 53 | 14 | 21 | 18 |
| bmorphism | user | 100 | 26 | 35 | 39 |
| zubyul | user | 23 | 10 | 7 | 6 |
| migalkin | social | 30 | 10 | 11 | 9 |
| DJedamski | social | 11 | 6 | 1 | 4 |
| wasita | social | 0 | - | - | - |
| kristinezheng | social | 0 | - | - | - |
| M1shaaa | social | 16 | 6 | 6 | 4 |
| AustinCStone | social | 43 | 17 | 15 | 11 |
| **TOTAL** | | **422** | **140** | **138** | **144** |

### Notable Repos (by Stars)
- `kubeflow/pipelines` — 4118 stars — Machine Learning Pipelines for Kubeflow
- `kubeflow/spark-operator` — 3111 stars — Kubernetes operator for Apache Spark
- `bmorphism/ocaml-mcp-sdk` — 60 stars — OCaml SDK for Model Context Protocol
- `plurigrid/asi` — 14 stars — everything is topological chemputer!
- `migalkin/NBFNet_mlx` — 10 stars — Neural Bellman-Ford networks in MLX

### Recent Events (bmorphism — 30 events)
- 2026-03-30: CreateEvent @ plurigrid/asi
- 2026-03-30: PushEvent × 5 @ plurigrid/horse
- 2026-03-30: PullRequestEvent × 2 @ plurigrid/horse

### Recent Events (zubyul — 30 events captured)
- Mix of PushEvent, CreateEvent across zubyul repos

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses queried via `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

| Label | Address | APT Balance | GF3 |
|-------|---------|-------------|-----|
| alice | 0xc793...c7b | 0.0 | ERGODIC #d3869b |
| bob | 0x0a3c...d5d | 0.0 | PLUS #b8bb26 |
| A | 0x8699...d7a | 0.0 | MINUS #cc241d |
| B | 0x3f89...b13 | 0.0 | ERGODIC #d3869b |
| C | 0x38b9...35e | 0.0 | PLUS #b8bb26 |
| D | 0xf776...dd1 | 0.0 | MINUS #cc241d |
| E-Z | (all) | 0.0 | (cycling) |

All 28 balances: **0.0 APT** — accounts not initialized or unfunded on mainnet.

### Multisig Contract Probes

| Pair | Address | Signatures Required |
|------|---------|---------------------|
| A-B | 0x0da4...003 | **2** |
| A-G | 0xf56c...096 | **2** |
| Y-Z | 0xd3ff...883 | **2** |
| S-T | 0x3b1c...883 | **2** |
| V-W | 0x40fa...b6d | **2** |

All 5 multisig contracts: `0x1::multisig_account::num_signatures_required` → **2**

### MNX Markets (testnet.mnx.fi)

- `https://testnet.mnx.fi` — **Reachable** (Next.js SPA)
- `https://testnet.mnx.fi/api/markets` — **Reachable** (returns HTML/SPA, no extractable JSON without JS execution)
- Status: Endpoint is live; market data requires JS hydration

---

## Schema

```sql
world_increments(id, sweep_ts, description, gf3_trit, gf3_color, gf3_label)
repo_snapshots(id, world_increment_id, source_org, source_type, repo_id,
               repo_name, full_name, description, language, stars, forks,
               pushed_at, html_url, gf3_trit, gf3_color, gf3_label, snapshot_ts)
aptos_snapshots(id, world_increment_id, label, address, raw_balance,
                apt_balance, gf3_trit, gf3_color, gf3_label, snapshot_ts)
multisig_probes(id, world_increment_id, pair_label, address,
                signatures_required, snapshot_ts)
mnx_snapshots(id, world_increment_id, endpoint, status, raw_data, snapshot_ts)
```

## Notable Highlights
- **kubeflow/pipelines**: 4,118 stars — most popular ML pipeline for Kubernetes
- **kubeflow/spark-operator**: 3,111 stars — Kubernetes operator for Apache Spark
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol
- **plurigrid/asi**: 14 stars — topological chemputer
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- All 5 multisig contracts confirmed active with threshold=2
- MNX testnet is live (SPA-based, no raw API JSON)
