# World-Increment Sweep + Hamming Snapshot — 2026-06-05

## Sweep Metadata
- **Date:** 2026-06-05
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 198 |
| Total Repo Snapshots | 198 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |
| GF(3) Balance | 66 ERGODIC / 66 PLUS / 66 MINUS |

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos Snapped | Top Repo by Stars |
|--------|------|--------------|-------------------|
| plurigrid | org | 100 | asi (HTML, 25★) |
| kubeflow | org | 20 | kubeflow (15,706★) |
| TeglonLabs | org | 4 | mathpix-gem (Ruby, 2★) |
| bmorphism | user | 31 | flox-mcp-bb (Clojure) |
| zubyul | user | 18 | gay-world (Python, 1★) |
| migalkin | user | 7 | NodePiece (Python, 144★) |
| wasita | user | 5 | magic-garden (Python, 2★) |
| AustinCStone | user | 4 | TextGAN (Python, 92★) |
| kristinezheng | user | 3 | Green-Machine (Python) |
| M1shaaa | user | 3 | lab-bookshelf- (TypeScript) |
| DJedamski | user | 3 | kaggle_ncaa18 (Jupyter) |
| **TOTAL** | | **198** | |

### GF(3) Trit Color Chain

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 66 |
| +1 | `#b8bb26` | PLUS | 66 |
| −1 | `#cc241d` | MINUS | 66 |

Perfectly ternary-balanced across 198 increments (66 × 3 = 198).

### Notable Repos (plurigrid, 2026-06-05 snapshot)
| Repo | Language | Stars | Open Issues | Pushed |
|------|----------|-------|-------------|--------|
| gorj | Clojure | 0 | 373 | 2026-06-05 |
| eirobri | Clojure | 0 | 29 | 2026-06-03 |
| place | TeX | 1 | 8 | 2026-06-04 |
| nash-portal | Rust | 2 | 1 | 2026-05-19 |
| asi | HTML | 25 | 4 | 2026-04-26 |
| nanoclj-zig | Zig | 1 | 20 | 2026-04-25 |

### kubeflow Highlights (2026-06-05)
| Repo | Stars | Updated |
|------|-------|---------|
| kubeflow/kubeflow | 15,706 | 2026-06-04 |
| kubeflow/pipelines | 4,152 | 2026-06-04 |
| kubeflow/spark-operator | 3,125 | 2026-06-05 |
| kubeflow/trainer | 2,111 | 2026-06-04 |
| kubeflow/katib | 1,684 | 2026-06-04 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances
**Queried:** 2026-06-05 via `https://fullnode.mainnet.aptoslabs.com/v1/`

| World | Address (truncated) | Balance |
|-------|---------------------|---------|
| alice | `0xc793ac...` | 0.0 APT |
| bob | `0x0a3c00...` | 0.0 APT |
| A–Z (26 wallets) | `0x8699ed...` → `0x7af0ef...` | 0.0 APT each |
| **Total** | 28 wallets | **0.0 APT** |

All CoinStore resources were accessible; swarm is fully deployed but unfunded at sweep time.

### Multisig Contract Probes
| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | `0x0da4f4...` | 2 | ✓ HEALTHY |
| A-G | `0xf56c4a...` | 2 | ✓ HEALTHY |
| Y-Z | `0xd3ffe1...` | 2 | ✓ HEALTHY |
| S-T | `0x3b1c3a...` | 2 | ✓ HEALTHY |
| V-W | `0x40fad7...` | 2 | ✓ HEALTHY |

All 5 multisig contracts respond: **2-of-N threshold**, all healthy.

### MNX Markets (testnet.mnx.fi)
**Status:** UNAVAILABLE — Vercel deployment protection (authentication required).  
Probed: `/`, `/api/markets`, `/api/v1/markets`. No data extractable without bypass token.  
`mnx_snapshots` table populated with 0 rows.

---

---

## DB Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)           -- 198 rows

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)           -- 198 rows

aptos_snapshots(timestamp, world, address, balance_apt)  -- 28 rows
multisig_probes(timestamp, pair, address, sigs_required, healthy)  -- 5 rows
mnx_snapshots(timestamp, ticker, name, category, price, change_pct) -- 0 rows
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=−1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,706 stars — flagship ML platform for Kubernetes (2026-06-04)
- **kubeflow/pipelines**: 4,152 stars — ML pipeline for Kubernetes (2026-06-04)
- **kubeflow/spark-operator**: 3,125 stars — Kubernetes operator for Apache Spark (2026-06-05)
- **migalkin/NodePiece**: 144 stars — scalable knowledge graph embeddings (ICLR'22)
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs (TensorFlow)
- **plurigrid/asi**: 25 stars — topological chemputer (2026-04-26)
- **plurigrid/gorj**: This repo — forj + Rama topology nREPL routing + GF(3) trit coloring (373 issues)
- **Hamming swarm**: 28 Aptos wallets, all 0 APT, 5 multisig contracts all 2-of-N healthy
- **GF(3) balance**: 66 ERGODIC + 66 PLUS + 66 MINUS = 198 total increments
