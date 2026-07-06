# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-06

## Sweep Metadata
- **Date:** 2026-07-06
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Aptos ledger:** ~v6141820907 (epoch 16439)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 30 |
| kubeflow | org | 30 |
| TeglonLabs | org | 5 |
| bmorphism | user | 20 |
| zubyul | user | 20 |
| migalkin | social-graph | 6 |
| wasita | social-graph | 5 |
| AustinCStone | social-graph | 5 |
| DJedamski | social-graph | 3 |
| kristinezheng | social-graph | 3 |
| M1shaaa | social-graph | 3 |
| **TOTAL** | | **130** |

### Top Starred Repos (this sweep)

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,766 | Jupyter Notebook |
| kubeflow/pipelines | 4,169 | Python |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |

### Top Languages (this sweep)

| Language | Repos |
|----------|-------|
| Python | 189 (cumulative) |
| Go | 44 |
| HTML | 43 |
| Rust | 39 |
| JavaScript | 32 |
| Jupyter Notebook | 30 |
| TypeScript | 27 |
| Clojure | 22 |

### Notable Repos

- **TeglonLabs/jank-crane** — `crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps` (C++, pushed 2026-06-08)
- **wasita/wasita.github.io** — personal Svelte site, pushed 2026-07-05 (most recent in social graph)
- **kristinezheng/kristinezheng.github.io** — pushed 2026-07-01
- **migalkin/NodePiece** — Compositional KG representations, ICLR'22 (144 stars)
- **AustinCStone/TextGAN** — GAN text generation in TensorFlow (92 stars)
- **bmorphism** — 20 recent repos snapshotted; active in MCP/OCaml/Zig space

### GF(3) Color Chain

| Trit | Color | Name | id mod 3 |
|------|-------|------|----------|
| 0 | `#d3869b` | ERGODIC | 0 |
| +1 | `#b8bb26` | PLUS | 1 |
| -1 | `#cc241d` | MINUS | 2 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 addresses queried via `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result: All 28 addresses — `resource_not_found` (no native APT CoinStore).**  
All recorded as **0.0 APT**.

| World | Address (truncated) | Balance |
|-------|---------------------|---------|
| alice | 0xc793...4cc7b | 0.0 APT |
| bob | 0x0a3c...512d | 0.0 APT |
| A–Z | 0x8699… → 0x7af0… | 0.0 APT each |

> All 26 swarm addresses (A–Z) plus alice and bob returned resource_not_found on mainnet. These addresses hold no native APT or use a different asset module.

### Multisig Contract Probes

POST `https://fullnode.mainnet.aptoslabs.com/v1/view` → `0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...987003 | **2** | HEALTHY |
| A-G | 0xf56c4a1c...0096 | **2** | HEALTHY |
| Y-Z | 0xd3ffe181...b883 | **2** | HEALTHY |
| S-T | 0x3b1c3ae9...7883 | **2** | HEALTHY |
| V-W | 0x40fad7b4...eb6d | **2** | HEALTHY |

All 5 multisig contracts are **live and require 2 signatures**.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — all API paths return HTTP 401 Unauthorized.  
No market data recorded in `mnx_snapshots`.

---

## DB State (cumulative)

| Table | Rows |
|-------|------|
| world_increments | 153 |
| repo_snapshots | 1074 |
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
