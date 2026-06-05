# World-Increment Sweep — 2026-06-05

## Sweep Metadata
- **Date:** 2026-06-05
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **New increments this run:** 235 (IDs 24–258)
- **Cumulative total:** 258 world_increments, 1179 repo_snapshots

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 258 |
| Total Repo Snapshots | 1179 |
| New Repo Snapshots This Sweep | 235 |
| Sources Covered | 3 orgs + 8 users (social graph) |
| Aptos Addresses Probed | 28 (alice, bob, A–Z) |
| Multisig Pairs Probed | 5 |
| MNX Markets | UNAVAILABLE (Vercel auth required) |

---

## GF(3) Color Chain — This Sweep (IDs 24–258)

GF(3) assignment rule:
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=**ERGODIC**
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=**MINUS**

Distribution across all 258 increments:

| Color | Name | Count |
|-------|------|-------|
| `#b8bb26` | PLUS | 87 |
| `#cc241d` | MINUS | 86 |
| `#d3869b` | ERGODIC | 85 |

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos in Sweep | Total Stars |
|--------|------|---------------|-------------|
| plurigrid | org | 50 | 131 |
| kubeflow | org | 48 | 101,899 |
| bmorphism | user | 50 | 383 |
| zubyul | user | 49 | 40 |
| TeglonLabs | org | 4 | 14 |
| migalkin | user | 8 | 280+ |
| wasita | user | 7 | 5 |
| AustinCStone | user | 7 | 107 |
| DJedamski | user | 4 | 2 |
| kristinezheng | user | 4 | 0 |
| M1shaaa | user | 4 | 0 |
| **TOTAL NEW** | | **235** | **103,861** |

### Top Repos by Stars

| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,706 | 2026-05-24 |
| kubeflow/pipelines | Python | 4,152 | 2026-06-05 |
| kubeflow/spark-operator | Python | 3,125 | 2026-06-04 |
| kubeflow/trainer | Go | 2,111 | 2026-06-05 |
| kubeflow/katib | Python | 1,684 | 2026-06-04 |
| kubeflow/examples | Jsonnet | 1,462 | 2025-04-14 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| kubeflow/arena | Go | 811 | 2026-05-07 |
| kubeflow/kale | Python | 691 | 2026-06-04 |
| kubeflow/mpi-operator | Go | 528 | 2026-06-02 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| migalkin/kgcourse2021 | HTML | 25 | 2026-02-16 |
| plurigrid/asi | HTML | 25 | 2026-04-26 |

### Notable New Repos Since Last Sweep (2026-04-12)

| Repo | Stars | Description |
|------|-------|-------------|
| kubeflow/mcp-apache-spark-history-server | 174 | MCP Server for Apache Spark — debug from AI agents |
| kubeflow/hub | 175 | Model Registry for MLOps |
| kubeflow/mcp-server | 10 | MCP Server for AI-Assisted Kubeflow Development |
| kubeflow/mlflow-integration | 6 | MLflow ↔ Kubeflow integration |
| plurigrid/gorj | 0 | This repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring (377 open issues) |
| plurigrid/zig-syrup | 2 | High-performance Zig OCapN Syrup implementation |
| plurigrid/nanoclj-zig | 1 | NaN-boxed Clojure in Zig with GF(3) trit conservation |
| plurigrid/nash-portal | 2 | NASH token TUI — ratzilla WASM + GeckoTerminal OHLCV |
| bmorphism/Gay.jl | 1 | Wide-gamut color sampling — 189 open issues |
| bmorphism/oxgame | 0 | Stellar resolution + open-game composition for OCaml |
| zubyul/nash-tui | 0 | NASH token TUI: real-time candles via GeckoTerminal |
| zubyul/tilelang-kernels | 0 | TileLang GPU kernels: SplitMix64, GF(3), flash attention |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 addresses in the Hamming swarm were probed against `fullnode.mainnet.aptoslabs.com`.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z (26 addrs) | 0x8699…–0x7af0… | 0.0 each |

**Total APT across swarm: 0.0 APT**
All addresses are unfunded/dormant on Aptos mainnet as of 2026-06-05.

### Multisig Contract Probes

All 5 multisig pairs probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✓ HEALTHY |

All 5 multisig contracts require 2-of-N signatures and are live on Aptos mainnet.

### MNX Markets

`testnet.mnx.fi` is behind Vercel deployment protection and requires authentication.
Status: **UNAVAILABLE** — no market data could be extracted.

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

## Delta Since Last Sweep (2026-04-12)

| Metric | 2026-04-12 | 2026-06-05 | Delta |
|--------|------------|------------|-------|
| World Increments | 12 | 258 | +246 |
| Repo Snapshots | 471 | 1179 | +708 |
| kubeflow/kubeflow stars | 15,565 | 15,706 | +141 |
| kubeflow/pipelines stars | 4,119 | 4,152 | +33 |
| kubeflow/spark-operator stars | 3,111 | 3,125 | +14 |
| kubeflow/trainer stars | 2,080 | 2,111 | +31 |
| plurigrid/asi stars | 16 | 25 | +9 |
| bmorphism/ocaml-mcp-sdk stars | 60 | 61 | +1 |
| Aptos swarm addresses | 0 | 28 | +28 |
| Multisig probes | 0 | 5 | +5 |

## Notable Highlights
- **kubeflow/kubeflow**: 15,706 stars — flagship ML platform for Kubernetes; 141 new stars since April
- **kubeflow/pipelines**: 4,152 stars — active ML pipeline, pushed 2026-06-05 (same day as this sweep)
- **plurigrid/gorj**: 0 stars, 377 open issues — the host repo for this very sweep agent
- **bmorphism/Gay.jl**: 189 open issues, the GF(3) color sampling engine powering this entire sweep
- **All 5 multisig pairs**: 2-of-N, all live and healthy on Aptos mainnet
- **Hamming swarm (A–Z + alice + bob)**: 28 addresses, all 0 APT — awaiting capitalization
- **MNX testnet**: Blocked by Vercel auth; market data unavailable this cycle
