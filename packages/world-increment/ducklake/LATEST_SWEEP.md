# World Increment Sweep + Hamming Snapshot — 2026-06-16

## Sweep Metadata
- **Date:** 2026-06-16
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos Snapshotted | Total Stars |
|--------|------|:-----------------:|:-----------:|
| kubeflow | org | 15 | 31,206 |
| migalkin | user (social) | 5 | 276 |
| AustinCStone | user (social) | 4 | 106 |
| bmorphism | user | 9 | 96 |
| plurigrid | org | 20 | 50 |
| zubyul | user | 7 | 7 |
| wasita | user (social) | 3 | 4 |
| DJedamski | user (social) | 3 | 2 |
| TeglonLabs | org | 5 | 2 |
| kristinezheng | user (social) | 2 | 0 |
| M1shaaa | user (social) | 2 | 0 |
| **TOTAL** | | **75** | **31,749** |

### Top Repos by Stars (this sweep)

| Repo | Language | Stars | Last Pushed |
|------|----------|------:|-------------|
| kubeflow/kubeflow | — | 15,726 | 2026-06-15 |
| kubeflow/pipelines | Python | 4,154 | 2026-06-15 |
| kubeflow/spark-operator | Python | 3,127 | 2026-06-14 |
| kubeflow/trainer | Go | 2,115 | 2026-06-16 |
| kubeflow/katib | Python | 1,683 | 2026-06-12 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| migalkin/kgcourse2021 | HTML | 25 | 2026-02-16 |

### Most Active Repos (latest pushes)

| Repo | Pushed At | Open Issues | Notes |
|------|-----------|:-----------:|-------|
| plurigrid/gorj | 2026-06-16 | 612 | Clojure, REPL orchestration hub |
| bmorphism/Gay.jl | 2026-06-16 | 187 | Julia, wide-gamut color SPI |
| kubeflow/trainer | 2026-06-16 | 125 | Go, AI/LLM fine-tuning |
| plurigrid/place | 2026-06-15 | 8 | TeX |
| wasita/wasita.github.io | 2026-06-15 | 8 | Svelte personal site |
| kubeflow/community-distribution | 2026-06-16 | 23 | YAML, K8s deployment |
| plurigrid/asi | 2026-06-10 | 4 | HTML, topological chemputer (26⭐) |
| TeglonLabs/jank-crane | 2026-06-08 | 0 | C++, crane-jank GF3 IR hub |
| bmorphism/satreadout | 2026-06-15 | 0 | Lean 4.28, perceptual readout |

### GF(3) Color Chain — New Increments (IDs 24–98)

- **75 new world_increments** written, GF(3) balanced:
  - trit=0 ERGODIC `#d3869b` — 32 records
  - trit=1 PLUS `#b8bb26` — 33 records
  - trit=-1 MINUS `#cc241d` — 33 records
- Cumulative total: **98 world_increments** across all sweeps
- Cumulative repo snapshots: **1,019** (471 from prior sweep + 75 new + historical)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All addresses queried: `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

**Result: All 28 addresses return `resource_not_found`** — accounts have no CoinStore resource initialized on mainnet (balance = 0 APT each).

| World | Address | Balance (APT) |
|-------|---------|:-------------:|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…2d5d | 0.0 |
| A–N | 0x8699…→0xe7dd… | 0.0 each |
| O–Z | 0x7325…→0x7af0… | 0.0 each |

**Total Hamming swarm APT: 0.0**

### Multisig Contract Probes (5 contracts)

All probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|:-------------:|--------|
| A-B | 0x0da4…7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c…0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff…b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c…7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa…eb6d | 2 | ✓ HEALTHY |

**All 5 multisig contracts healthy** — 2-of-N threshold, all responding.

### MNX Markets

`https://testnet.mnx.fi/api/markets` → **HTTP 401 Unauthorized**. No market data available; `mnx_snapshots` table empty for this sweep.

---

## Summary

| Component | Status | Count |
|-----------|--------|:-----:|
| GitHub repos snapshotted (this sweep) | ✓ | 75 |
| World increments written | ✓ | 75 |
| GF(3) chain balance | ✓ | 32E·33P·33M |
| Aptos addresses probed | ✓ | 28 |
| Aptos APT total | — | 0.0 |
| Multisig contracts healthy | ✓ | 5/5 |
| MNX market data | ✗ 401 | 0 |
| DuckDB cumulative repo records | ✓ | 1,019 |
| DuckDB cumulative world increments | ✓ | 98 |

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
