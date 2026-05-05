# World-Increment Sweep + Hamming Snapshot
**Date:** 2026-05-05  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** v1.5.2 (Variegata) — `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Source | Type | Increments | Top Repo (stars) |
|--------|------|-----------|-----------------|
| plurigrid | org | 32 | asi (18 ★) |
| kubeflow | org | 19 | kubeflow/kubeflow (15,621 ★) |
| TeglonLabs | org | 6 | mathpix-gem (2 ★) |
| bmorphism | user | 25 | anti-bullshit-mcp-server (23 ★) |
| zubyul | user | 22 | gay-world (1 ★) |
| migalkin | user_social | 6 | NodePiece (143 ★) |
| DJedamski | user_social | 3 | kaggle_ncaa18 (0 ★) |
| wasita | user_social | 4 | wasita.github.io (1 ★) |
| kristinezheng | user_social | 3 | kristinezheng.github.io (0 ★) |
| M1shaaa | user_social | 4 | M1shaaa (0 ★) |
| AustinCStone | user_social | 5 | TextGAN (92 ★) |
| **TOTAL** | | **129 increments / 495 distinct repos** | |

### GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 42 |
| +1 | PLUS | #b8bb26 | 44 |
| -1 | MINUS | #cc241d | 43 |

GF(3) rule: `id%3==0` → ERGODIC #d3869b | `id%3==1` → PLUS #b8bb26 | `id%3==2` → MINUS #cc241d

### Notable Repos by Source

**kubeflow** (19 increments, most active org):
- kubeflow/kubeflow — 15,621 ★ — ML Toolkit for Kubernetes
- kubeflow/pipelines — 4,132 ★ — ML Pipelines (pushed 2026-05-04)
- kubeflow/spark-operator — 3,123 ★ — Apache Spark Operator
- kubeflow/trainer — 2,096 ★ — Distributed AI Training (pushed 2026-05-05)

**plurigrid** (32 increments):
- plurigrid/gorj — 68 open issues — forj + Rama nREPL (this repo, pushed 2026-05-05)
- plurigrid/asi — 18 ★ — topological chemputer
- plurigrid/nanoclj-zig — 20 open issues — NaN-boxed Clojure in Zig

**bmorphism** (25 increments):
- bmorphism/Gay.jl — 187 open issues — wide-gamut color sampling (pushed 2026-05-05)
- bmorphism/ocaml-mcp-sdk — 60 ★ — OCaml MCP SDK
- bmorphism/anti-bullshit-mcp-server — 23 ★

**migalkin** (social graph):
- migalkin/NodePiece — 143 ★ — KG representations (ICLR'22)
- migalkin/StarE — 89 ★ — Hyper-Relational KGs (EMNLP 2020)

**AustinCStone** (social graph):
- AustinCStone/TextGAN — 92 ★ — GAN text generation (TensorFlow)

### Most Recently Pushed
1. `kubeflow/trainer` — 2026-05-05T10:43:07Z
2. `plurigrid/gorj` — 2026-05-05T10:16:13Z
3. `bmorphism/Gay.jl` — 2026-05-05T00:31:58Z
4. `kubeflow/mpi-operator` — 2026-05-05T05:00:55Z
5. `kubeflow/hub` — 2026-05-05T09:41:03Z

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances — alice, bob, A–Z

All 28 Hamming addresses queried via  
`https://fullnode.mainnet.aptoslabs.com/v1/accounts/{ADDR}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

| World | Balance (APT) |
|-------|--------------|
| alice | 0.0 |
| bob | 0.0 |
| A–Z (26) | 0.0 each |

**Total APT across swarm: 0.0 APT**  
All addresses lack `CoinStore<AptosCoin>` resources — wallets exist on-chain but hold no native APT.

### Multisig Contract Probes

Function: `0x1::multisig_account::num_signatures_required`

| Pair | Contract Address (truncated) | Sigs Required | Status |
|------|------------------------------|--------------|--------|
| A-B | `0x0da4f428a0c007da...` | 2 | HEALTHY |
| A-G | `0xf56c4a1c0906214f...` | 2 | HEALTHY |
| Y-Z | `0xd3ffe1812b2df406...` | 2 | HEALTHY |
| S-T | `0x3b1c3ae905d44c3a...` | 2 | HEALTHY |
| V-W | `0x40fad7b423a84365...` | 2 | HEALTHY |

All 5 pairs: 2-of-N multisig, fully responsive.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE — SPA only**  
All API paths (`/api/markets`, `/api/tickers`, `/api/v1/tickers`, `/api/v2/markets`, `/markets`, `/api/orderbook`, `/api/pairs`) return Next.js HTML. No JSON market data extractable without headless browser execution. No MNX rows inserted.

---

## DuckDB Tables

```
world_increments   129 rows  — GF(3)-colored increment log
repo_snapshots     495 distinct repos (1050 total rows, multi-source join)
aptos_snapshots     28 rows  — alice, bob, A–Z balances
multisig_probes      5 rows  — A-B, A-G, Y-Z, S-T, V-W
mnx_snapshots        0 rows  — SPA unavailable
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
