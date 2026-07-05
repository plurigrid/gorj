# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-05

## Sweep Metadata
- **Date:** 2026-07-05
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| World Increments (this run) | 319 |
| Repo Snapshots (this run) | 319 |
| Aptos Wallet Snapshots | 28 |
| Multisig Probes | 5 |
| MNX Market Snapshots | 0 (auth blocked) |
| Total DB Increments | 342 |
| Total DB Repo Snapshots | 1263 |

---

## JOB 1: GitHub Social Graph Sweep

### Sources (this run)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social) | 19 |
| DJedamski | user (social) | 6 |
| wasita | user (social) | 11 |
| kristinezheng | user (social) | 5 |
| M1shaaa | user (social) | 8 |
| AustinCStone | user (social) | 40 |
| **TOTAL** | | **391** |

### GF(3) Color Chain Distribution

| GF3 Name | Trit | Color | Count |
|----------|------|-------|-------|
| ERGODIC | 0 | `#d3869b` | 113 |
| PLUS | +1 | `#b8bb26` | 115 |
| MINUS | -1 | `#cc241d` | 114 |

### Top Repos by Stars (2026-07-05 snapshot)

| Repo | Lang | Stars | Forks | Last Push |
|------|------|-------|-------|-----------|
| kubeflow/kubeflow | — | 15762 | 2683 | 2026-06-18 |
| kubeflow/pipelines | Python | 4169 | 2023 | 2026-07-04 |
| kubeflow/spark-operator | Python | 3132 | 1496 | 2026-07-02 |
| kubeflow/trainer | Go | 2129 | 978 | 2026-07-03 |
| kubeflow/katib | Python | 1689 | 530 | 2026-07-01 |
| migalkin/NodePiece | Python | 144 | 21 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 30 | 2025-03-03 |
| migalkin/StarE | Python | 89 | 16 | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2 | 2026-03-16 |
| plurigrid/asi | HTML | 28 | 8 | 2026-06-29 |

### Notable Recent Activity

- `plurigrid/gorj` — Clojure — pushed **2026-07-05** (today)
- `bmorphism/Gay.jl` — Julia — pushed **2026-07-05**
- `kubeflow/pipelines` — Python — pushed **2026-07-04**
- `plurigrid/shrimp` — pushed **2026-07-03**
- `wasita/wasita.github.io` — Svelte — pushed **2026-07-05**
- `TeglonLabs/jank-crane` — C++ — GF3 convergence maps, jank-crane IR hub

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

**Result:** All 28 addresses (`alice`, `bob`, `A`–`Z`) returned `resource_not_found`  
for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` on Aptos mainnet.

Accounts exist but have no APT coin resource initialized (zero-balance / pre-funded).  
All balance values stored as `NULL` in `aptos_snapshots`.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | `0xc793acd…` | NULL |
| bob | `0x0a3c00c…` | NULL |
| A–Z (26) | various | NULL |

### Multisig Contract Probes

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | `0x0da4f428…` | **2** | ✅ healthy |
| A-G | `0xf56c4a1c…` | **2** | ✅ healthy |
| Y-Z | `0xd3ffe181…` | **2** | ✅ healthy |
| S-T | `0x3b1c3ae9…` | **2** | ✅ healthy |
| V-W | `0x40fad7b4…` | **2** | ✅ healthy |

All 5 multisig contracts are **2-of-2** and healthy on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable — HTTP 401 (Vercel authentication required).  
`mnx_snapshots` table remains empty this run.

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,762 stars (+197 since Apr sweep) — flagship ML platform
- **plurigrid/gorj**: active today — forj MCP + Clojure REPL + GF(3) trit coloring
- **bmorphism/Gay.jl**: Julia, active today
- **TeglonLabs/jank-crane**: new — crane-jank converged-IR hub with GF3 convergence maps
- **All 5 multisig contracts**: healthy, 2-of-2 threshold
- **28 Hamming swarm wallets**: uninitialized on mainnet (no APT resources)
