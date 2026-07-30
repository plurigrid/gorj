# World-Increment Sweep + Hamming Snapshot — 2026-07-30

## Sweep Metadata
- **Date:** 2026-07-30T14:12 UTC
- **Branch:** `world-increment/sweep-2026-07-30-1412`
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted | Notable |
|--------|------|-------------------|---------|
| plurigrid | org | 100 (103 total) | gorj active today (1512 open issues) |
| kubeflow | org | 49 | flagship 15,798★; pipelines+spark+trainer most active |
| TeglonLabs | org | 5 | jank-crane (C++) pushed 2026-06-08 |
| bmorphism | user | 100 (106 total) | Gay.jl active today; ocaml-mcp-sdk 61★ |
| zubyul | user | 49 | from-possible-worlds pushed 2026-07-18 |
| migalkin | social | 19 | NodePiece 144★, StarE 89★ |
| AustinCStone | social | 30+ (41 total) | TextGAN 92★ |
| DJedamski | social | 6 | quiet (last active 2023) |
| wasita | social | 12 | wasita.github.io active 2026-07-21 |
| kristinezheng | social | 5 | site updated 2026-07-01 |
| M1shaaa | social | 8 | M1shaaa profile updated 2026-02-04 |

### GF(3) Color Chain Applied

- `id % 3 == 0` → trit=0, **ERGODIC** #d3869b (pink)
- `id % 3 == 1` → trit=1, **PLUS** #b8bb26 (yellow-green)
- `id % 3 == 2` → trit=-1, **MINUS** #cc241d (red)

### Top Repos by Stars (this sweep batch)

| Repo | Stars | Lang | Last Push |
|------|-------|------|-----------|
| kubeflow/kubeflow | 15,798 | — | 2026-07-10 |
| kubeflow/pipelines | 4,171 | Python | 2026-07-29 |
| kubeflow/spark-operator | 3,142 | Python | 2026-07-29 |
| kubeflow/trainer | 2,163 | Go | 2026-07-30 |
| kubeflow/katib | 1,694 | Python | 2026-07-26 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/asi | 56 | HTML | 2026-07-10 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |

### Most Active Today (2026-07-30)

- `plurigrid/gorj` (pushed 13:14 UTC) — this repo
- `kubeflow/mlflow-integration` (pushed 13:12 UTC)
- `kubeflow/hub` (pushed 12:24 UTC)
- `kubeflow/mcp-server` (pushed 11:34 UTC)
- `kubeflow/notebooks` (pushed 10:58 UTC)
- `bmorphism/Gay.jl` (pushed 02:12 UTC, 188 open issues)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

Queried 28 addresses (alice, bob, A–Z) via Aptos fullnode mainnet.

**All 28 addresses returned 0 APT.** Accounts have no `CoinStore<AptosCoin>` resource on mainnet (not funded or testnet addresses).

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793ac... | 0.00000000 |
| bob | 0x0a3c00... | 0.00000000 |
| A–Z | (26 addresses) | 0.00000000 each |

### Multisig Contract Probes

All 5 contracts queried via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f4... | **2** | healthy |
| A-G | 0xf56c4a... | **2** | healthy |
| Y-Z | 0xd3ffe1... | **2** | healthy |
| S-T | 0x3b1c3a... | **2** | healthy |
| V-W | 0x40fad7... | **2** | healthy |

All multisig contracts live, 2-of-N, no anomalies.

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — `testnet.mnx.fi` serves a Next.js SPA for all paths. No JSON market data accessible. Recorded in `mnx_snapshots` (empty).

---

## DuckDB State (cumulative)

```
world_increments:  113 rows
repo_snapshots:   1034 rows
total stars:     101,307
aptos_snapshots:    28 rows (this run)
multisig_probes:     5 rows (this run)
mnx_snapshots:       0 rows (unavailable)
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

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
