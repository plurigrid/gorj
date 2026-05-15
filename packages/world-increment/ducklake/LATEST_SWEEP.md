# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-28

## Sweep Metadata
- **Date:** 2026-04-28
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 412 |
| Total Repo Snapshots | 1,333 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 101 |
| zubyul | user | 49 |
| migalkin | user (social) | 19 |
| DJedamski | user (social) | 6 |
| wasita | user (social) | 10 |
| kristinezheng | user (social) | 6 |
| M1shaaa | user (social) | 8 |
| AustinCStone | user (social) | 40 |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 136 |
| 1 | #b8bb26 | PLUS | 138 |
| -1 | #cc241d | MINUS | 138 |

GF(3) rule: `id%3==0 → ERGODIC | id%3==1 → PLUS | id%3==2 → MINUS`

### Top Repos by Stars

| Repo | Stars | Forks | Language | Last Push |
|------|-------|-------|----------|-----------|
| kubeflow/kubeflow | 15,609 | 2,645 | — | 2026-01-05 |
| kubeflow/pipelines | 4,127 | 1,983 | Python | 2026-04-27 |
| kubeflow/spark-operator | 3,120 | 1,483 | Python | 2026-04-24 |
| kubeflow/trainer | 2,094 | 947 | Go | 2026-04-25 |
| kubeflow/mcp-apache-spark-history-server | 153 | 54 | Python | 2026-04-28 |
| migalkin/NodePiece | 143 | 21 | Python | 2022-02-02 |
| migalkin/StarE | 89 | 16 | Python | 2023-12-01 |
| AustinCStone/TextGAN | 92 | 30 | Python | 2016-10-04 |
| bmorphism/ocaml-mcp-sdk | 60 | 2 | OCaml | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | 23 | 7 | JavaScript | 2026-01-16 |
| plurigrid/asi | 17 | 5 | HTML | 2026-04-26 |
| migalkin/kgcourse2021 | 25 | 9 | HTML | 2025-08-04 |
| TeglonLabs/mathpix-gem | 2 | 0 | Ruby | 2026-01-01 |

### Notable Recent Activity (plurigrid, 2026-04-26+)

- `plurigrid/zig-syrup` — Zig OCapN Syrup with CapTP optimizations
- `plurigrid/nash-portal` — NASH token TUI: ratzilla WASM + GeckoTerminal OHLCV
- `plurigrid/asi-skills` — 69 Julia skills with Galois Hole Types (Seven Sketches §1.4.1)
- `plurigrid/gorj` — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- `plurigrid/nanoclj-zig` — NaN-boxed Clojure in Zig 0.15 + interaction nets + GF(3)

### Social Graph (zubyul connections)

- `wasita/wasita.github.io` — personal site (Svelte), pushed 2026-04-27
- `zubyul/voice-observatory` — passive macOS TUI observing voice-download, 2026-04-24
- `M1shaaa/M1shaaa` — profile config, active 2026-04-27
- `migalkin` — knowledge graph researcher (NodePiece 143★, StarE 89★)
- `DJedamski` — data science/Kaggle competitor
- `kristinezheng` — MIT cognitive science research
- `AustinCStone` — ML/computer vision (TextGAN 92★, EpsteinSearch)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 worlds)

All 28 addresses queried via Aptos fullnode mainnet.  
**Result:** All addresses returned unavailable (-1) — accounts not initialized on mainnet or have no `CoinStore<AptosCoin>` resource.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|--------------|
| alice | 0xc793... | unavailable |
| bob | 0x0a3c... | unavailable |
| A | 0x8699... | unavailable |
| B–Z | 0x3f89...–0x7af0... | unavailable |

### Multisig Contract Probes (5/5 healthy)

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | **2** | healthy |
| A-G | 0xf56c...0096 | **2** | healthy |
| Y-Z | 0xd3ff...b883 | **2** | healthy |
| S-T | 0x3b1c...7883 | **2** | healthy |
| V-W | 0x40fa...eb6d | **2** | healthy |

All 5 contracts confirmed **2-of-N signatures** required, responding healthy on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)

API endpoint `https://testnet.mnx.fi/api/markets` — **unavailable**. Returns a Next.js SPA shell with no REST API exposed. No market data extractable. Recorded as N/A in `mnx_snapshots`.

---

## DuckDB Schema

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

## Table Row Counts

```
world_increments:  412 rows
repo_snapshots:   1333 rows
aptos_snapshots:    28 rows
multisig_probes:     5 rows
mnx_snapshots:       1 row
```

## Notable Highlights

- **kubeflow/kubeflow**: 15,609 stars — ML toolkit for Kubernetes (not changed since 2026-01-05)
- **kubeflow/pipelines**: 4,127 stars — most active Kubeflow component (pushed 2026-04-27)
- **kubeflow/mcp-apache-spark-history-server**: 153 stars — newest Kubeflow MCP, pushed 2026-04-28
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) trit coloring
- **bmorphism/Gay.jl**: Active 2026-04-28, 187 open issues — wide-gamut color sampling
- **All 5 multisig contracts**: 2-of-N, healthy on Aptos mainnet
- **Hamming swarm**: 28 wallet addresses probed; all mainnet coin stores unavailable
