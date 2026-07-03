# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-03

## Sweep Metadata
- **Date:** 2026-07-03
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (python)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (Cumulative DB)

| Table | Rows | Notes |
|-------|------|-------|
| world_increments | 128+ | GF(3)-colored event log (cumulative) |
| repo_snapshots | 1049+ | Full repo metadata with language/stars/forks |
| aptos_snapshots | 28 | All 28 Hamming swarm addresses, NULL balance |
| multisig_probes | 5 | All 5 multisigs healthy (2-of-N threshold) |
| mnx_snapshots | 0 | Unavailable (401 auth) |

---

## JOB 1: GitHub Social Graph Sweep (2026-07-03)

### Sources Queried

| Source | Type | Repos Found |
|--------|------|-------------|
| plurigrid | org | 103 (100 fetched) |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 105 (100 fetched) |
| zubyul | user | 49 |
| migalkin | social graph | 19 |
| DJedamski | social graph | 6 |
| wasita | social graph | 11 |
| kristinezheng | social graph | 5 |
| M1shaaa | social graph | 8 |
| AustinCStone | social graph | 40 |

### Top Repos by Stars (2026-07-03 snapshot)

| Repo | Language | Stars | Forks | Pushed |
|------|----------|-------|-------|--------|
| kubeflow/kubeflow | — | 15,758 | 2,682 | 2026-06-18 |
| kubeflow/pipelines | Python | 4,167 | 2,020 | 2026-07-02 |
| kubeflow/spark-operator | Python | 3,131 | 1,496 | 2026-07-02 |
| kubeflow/trainer | Go | 2,129 | 974 | 2026-07-02 |
| kubeflow/community-distribution | YAML | 1,028 | 1,067 | 2026-06-30 |
| kubeflow/katib | Python | 1,688 | 529 | 2026-07-01 |
| migalkin/NodePiece | Python | 144 | 21 | 2022-02-02 |
| AustinCStone/TextGAN | Python | 92 | 30 | 2016-10-04 |
| migalkin/StarE | Python | 89 | 16 | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2 | 2026-03-16 |

### Notable Recent Activity (past 7 days)

- **plurigrid/gorj** (2026-07-03): forj + Rama topology nREPL + GF(3) trit coloring — 933 open issues
- **bmorphism/Gay.jl** (2026-07-03): Wide-gamut color sampling — 187 open issues
- **M1shaaa/M1shaaa** (2026-07-03): Profile config updated today
- **kubeflow/arena** (2026-07-03): CLI for Kubeflow — 44 open issues
- **wasita/wasita.github.io** (2026-07-02): personal website active — Svelte
- **kristinezheng/kristinezheng.github.io** (2026-07-01): portfolio updated
- **plurigrid/eirobri** (2026-06-30): EiRoBri replay world — 30 open issues

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count (this run) |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 42 |
| 1 | `#b8bb26` | PLUS | 43 |
| -1 | `#cc241d` | MINUS | 43 |

---

## JOB 2: Hamming Swarm Snapshot (2026-07-03)

### Aptos Wallet Balances (A–Z + alice + bob)

All 28 addresses exist on Aptos mainnet with active sequence numbers.
`CoinStore<AptosCoin>` resource not registered — wallets use non-native APT or fungible assets.

| World | Address (prefix) | Confirmed Exists | CoinStore |
|-------|-----------------|-----------------|-----------|
| alice | 0xc793acde... | ✅ seq=72 (active builder) | ❌ |
| A | 0x8699edc0... | ✅ seq=58 | ❌ |
| B | 0x3f892ebe... | ✅ seq=35 | ❌ |
| Z | 0x7af0ef6e... | ✅ seq=2 | ❌ |
| bob–Y | (all others) | ✅ exists | ❌ |

**alice** (seq=72) has deployed custom contracts:
- `store_v2::ACSetMeta2`
- `address_book::Mapping`
- `lending_pool::UserPosition`

All 28 Hamming swarm addresses recorded with `balance_apt = NULL`.

### Multisig Contract Probes — ALL HEALTHY ✅

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428a0c007da... | 2 | ✅ healthy |
| A-G | 0xf56c4a1c0906214f... | 2 | ✅ healthy |
| Y-Z | 0xd3ffe1812b2df406... | 2 | ✅ healthy |
| S-T | 0x3b1c3ae905d44c3a... | 2 | ✅ healthy |
| V-W | 0x40fad7b423a84365... | 2 | ✅ healthy |

All 5 multisig contracts respond with `num_signatures_required = 2` and are live on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)

API returned **401 Unauthorized** on all probed endpoints.
Authentication credentials required — no market data available without them.
`mnx_snapshots` table is empty.

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
