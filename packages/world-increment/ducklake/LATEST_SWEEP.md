# World-Increment Sweep — 2026-06-13

## Sweep Metadata
- **Date:** 2026-06-13
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 97 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social graph) | 19 |
| DJedamski | user (social graph) | 6 |
| wasita | user (social graph) | 11 |
| kristinezheng | user (social graph) | 5 |
| M1shaaa | user (social graph) | 8 |
| AustinCStone | user (social graph) | 40 |
| **TOTAL** | | **388 new repos** |

### GF(3) Color Chain — This Sweep's Increments

| ID | Source | GF3 Trit | Color | Name |
|----|--------|-----------|-------|------|
| 7  | TeglonLabs | 1 | `#b8bb26` | **PLUS** |
| 8  | DJedamski | -1 | `#cc241d` | **MINUS** |
| 9  | wasita | 0 | `#d3869b` | **ERGODIC** |
| 10 | kristinezheng | 1 | `#b8bb26` | **PLUS** |
| 11 | M1shaaa | -1 | `#cc241d` | **MINUS** |
| 12 | AustinCStone | 0 | `#d3869b` | **ERGODIC** |
| 29 | plurigrid | -1 | `#cc241d` | **MINUS** |
| 30 | kubeflow | 0 | `#d3869b` | **ERGODIC** |
| 31 | bmorphism | 1 | `#b8bb26` | **PLUS** |
| 32 | zubyul | -1 | `#cc241d` | **MINUS** |
| 33 | migalkin | 0 | `#d3869b` | **ERGODIC** |

GF(3) rule: `id%3==0 → ERGODIC #d3869b | id%3==1 → PLUS #b8bb26 | id%3==2 → MINUS #cc241d`

### Top Starred Repos (this sweep)

| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15,721 | — | 2026-06-11 |
| kubeflow/pipelines | 4,153 | Python | 2026-06-13 |
| kubeflow/spark-operator | 3,128 | Python | 2026-06-12 |
| kubeflow/trainer | 2,114 | Go | 2026-06-13 |
| kubeflow/katib | 1,683 | Python | 2026-06-12 |
| kubeflow/examples | 1,461 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1,023 | YAML | 2026-06-12 |
| kubeflow/arena | 812 | Go | 2026-05-07 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| AustinCStone/StereoVisionMRF | 11 | Python | 2026-04-01 |
| plurigrid/asi | 26 | HTML | 2026-06-10 |
| bmorphism/risc0-cosmwasm-example | 23 | Rust | 2022-10-20 |

### Notable Repo Highlights
- **plurigrid/gorj** (this repo): 554 open issues, active Clojure+GF(3) development, pushed 2026-06-13
- **plurigrid/eirobri**: 29 open issues — EiRoBri replay world
- **bmorphism/Gay.jl**: 189 open issues — Julia wide-gamut color sampling, SPI pattern
- **bmorphism/say-mcp-server**: 20★ — macOS TTS via MCP
- **bmorphism/babashka-mcp-server**: 19★ — Babashka/Clojure MCP
- **TeglonLabs/jank-crane**: C++ crane-jank converged-IR hub with GF3 convergence maps (2026-06-08)
- **kubeflow/mcp-apache-spark-history-server**: 177★ MCP bridge for Spark History Server
- **migalkin/kgcourse2021**: 25★ Knowledge Graphs course materials (Russian)
- **zubyul/Gay.jl**: Julia fork of bmorphism/Gay.jl — GF(3) color determinism
- **wasita/magic-garden**: 2★ Discord bot for magic garden game

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances

All 28 Hamming swarm wallets queried via `fullnode.mainnet.aptoslabs.com` with 1s delay between calls.

**Result: All 28 wallets returned 0 APT** (`CoinStore<AptosCoin>` resource value = 0).
Accounts exist on-chain but hold zero native APT at time of sweep.

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793ac...4cc7b | 0.0 |
| bob | 0x0a3c00...2d5d | 0.0 |
| A | 0x8699ed...e9d7a | 0.0 |
| B | 0x3f892e...b13 | 0.0 |
| C | 0x38b99e...535e | 0.0 |
| D | 0xf77656...fdd1 | 0.0 |
| E | 0xdc1d9d...8d36 | 0.0 |
| F | 0x18a14b...f71 | 0.0 |
| G | 0x69a394...7f32 | 0.0 |
| H | 0xce67c3...300f | 0.0 |
| I | 0x070fe5...fc9 | 0.0 |
| J | 0x4d964d...7f54 | 0.0 |
| K | 0xa73204...5dc4 | 0.0 |
| L | 0x7c2eae...eba9 | 0.0 |
| M | 0x6fed37...2e9 | 0.0 |
| N | 0xe7dde6...1b2c | 0.0 |
| O | 0x73252b...a89d | 0.0 |
| P | 0x621879...948 | 0.0 |
| Q | 0xac40fa...89a9 | 0.0 |
| R | 0x7ce605...6e10 | 0.0 |
| S | 0xb87530...386 | 0.0 |
| T | 0x35781d...4588 | 0.0 |
| U | 0x75860d...956 | 0.0 |
| V | 0xb59dd8...f2c3 | 0.0 |
| W | 0x5f32ae...7b0 | 0.0 |
| X | 0xa95cbb...047d | 0.0 |
| Y | 0xd8e328...444c4 | 0.0 |
| Z | 0x7af0ef...197c | 0.0 |

**Total swarm APT: 0.0**

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f4...87003 | **2** | ✅ |
| A-G | 0xf56c4a...0096 | **2** | ✅ |
| Y-Z | 0xd3ffe1...b883 | **2** | ✅ |
| S-T | 0x3b1c3a...7883 | **2** | ✅ |
| V-W | 0x40fad7...eb6d | **2** | ✅ |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` returns Vercel authentication wall (302 redirect).
No market data extractable. `mnx_snapshots` table remains empty.

---

## DuckDB Ducklake Final State

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows | Notes |
|-------|------|-------|
| world_increments | 34 | Cumulative across all sweeps |
| repo_snapshots | 1,310 | Cumulative across all sweeps |
| aptos_snapshots | 28 | This sweep only |
| multisig_probes | 5 | This sweep only |
| mnx_snapshots | 0 | MNX unavailable |

---

## Schema Reference
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

*Sweep completed 2026-06-13. GF(3) trit chain: ERGODIC(#d3869b) → PLUS(#b8bb26) → MINUS(#cc241d) → ...*
