# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-13T18:30:00Z  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 100 |
| kubeflow | org | 12 |
| TeglonLabs | org | 4 |
| bmorphism | user | 15 |
| zubyul | user | 10 |
| migalkin | user | 6 |
| wasita | user | 4 |
| AustinCStone | user | 4 |
| DJedamski | user | 3 |
| kristinezheng | user | 3 |
| M1shaaa | user | 3 |
| **TOTAL** | | **164** |

### GF(3) Color Chain Distribution

| Name | Trit | Color | Count |
|------|------|-------|-------|
| ERGODIC | 0 | `#d3869b` | 54 |
| PLUS | 1 | `#b8bb26` | 55 |
| MINUS | -1 | `#cc241d` | 55 |

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,721 | — |
| kubeflow/pipelines | 4,153 | Python |
| kubeflow/spark-operator | 3,128 | Python |
| kubeflow/trainer | 2,114 | Go |
| kubeflow/katib | 1,683 | Python |
| kubeflow/community-distribution | 1,023 | YAML |
| kubeflow/arena | 812 | Go |
| kubeflow/kale | 694 | Python |
| AustinCStone/TextGAN | 92 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |

### Notable Recent Activity (plurigrid org)

- `plurigrid/gorj` — forj + Rama topology nREPL routing + GF(3) gay trit coloring (pushed 2026-06-13, 553 open issues)
- `plurigrid/asi` — everything is topological chemputer! (26 stars, pushed 2026-06-10)
- `plurigrid/eirobri` — EiRoBri replay world (Clojure, pushed 2026-06-03)
- `plurigrid/nanoclj-zig` — NaN-boxed Clojure interpreter in Zig 0.15 with GF(3) trit conservation
- `plurigrid/spi-race` — Splitmix Parallel Integrity across CPU/GPU/every language

### Zubyul Social Graph Highlights

- `zubyul/tilelang-kernels` — TileLang GPU kernels for GF(3) trit classification, Sinkhorn OT, flash attention (targeting NVIDIA GB10 Blackwell)
- `migalkin/NodePiece` — 144 stars, Compositional KG representations (ICLR 2022)
- `migalkin/StarE` — 89 stars, Hyper-Relational Knowledge Graphs (EMNLP 2020)
- `wasita/wasita.github.io` — Network Science researcher, active 2026-06

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses queried on Aptos Mainnet (Ledger v5,719,890,383).  
All balances: 0.000000 APT — `CoinStore<AptosCoin>` resource not found (accounts exist on-chain but hold no APT in the legacy coin store; may hold assets via `0x1::primary_fungible_store`).

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...12d5 | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D-Z | (full data in DB) | 0.0 each |

### Multisig Contract Probes (5 pairs)

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | YES |
| A-G | 0xf56c...096 | 2 | YES |
| Y-Z | 0xd3ff...883 | 2 | YES |
| S-T | 0x3b1c...883 | 2 | YES |
| V-W | 0x40fa...b6d | 2 | YES |

All 5 multisig contracts healthy — 2-of-N threshold confirmed.

### MNX Markets (testnet.mnx.fi)

Status: UNAVAILABLE — Vercel deployment requires authentication for all API paths (/api/markets, /api/v1/markets). No market data extracted this sweep.

---

## DuckDB Schema Summary

```
world_increments   164 rows  (GF3 trit-colored repo snapshot events)
repo_snapshots     164 rows  (full repo metadata per source)
aptos_snapshots     28 rows  (Hamming swarm wallet balances)
multisig_probes      5 rows  (multisig contract health checks)
mnx_snapshots        0 rows  (unavailable this sweep)
```

## Query Examples

```sql
-- Most active repos in sweep
SELECT full_name, stars, forks, language
FROM repo_snapshots ORDER BY stars DESC LIMIT 20;

-- GF3 color chain walk
SELECT id, gf3_trit, gf3_color, gf3_name, source_name, repo_name
FROM world_increments ORDER BY id LIMIT 20;

-- Aptos swarm balances
SELECT world, address, balance_apt FROM aptos_snapshots ORDER BY world;

-- Multisig health
SELECT pair, sigs_required, healthy FROM multisig_probes;
```
