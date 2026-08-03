# World-Increment Sweep + Hamming Swarm Snapshot — 2026-08-03

## Sweep Metadata
- **Date:** 2026-08-03
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 268 |
| Total Repo Snapshots | 268 |
| Sources Covered | 3 orgs + 8 users |

### GF(3) Trit Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 89 |
| +1 | #b8bb26 | PLUS | 90 |
| -1 | #cc241d | MINUS | 89 |

GF(3) assignment rule: `id mod 3 == 0` → ERGODIC · `id mod 3 == 1` → PLUS · `id mod 3 == 2` → MINUS

### Top Repos by Stars

| Repo | Stars | Forks | Language |
|------|-------|-------|----------|
| kubeflow/kubeflow | 15,805 | 2,690 | — |
| kubeflow/pipelines | 4,173 | 2,075 | Python |
| kubeflow/spark-operator | 3,143 | 1,509 | Python |
| kubeflow/trainer | 2,165 | 1,008 | Go |
| kubeflow/katib | 1,694 | 534 | Python |
| migalkin/NodePiece | 144 | 21 | Python |
| AustinCStone/TextGAN | 92 | 30 | Python |
| migalkin/StarE | 89 | 16 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | 2 | OCaml |
| plurigrid/asi | 58 | 13 | HTML |

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| zubyul | user | 4 |
| migalkin | user (social) | 3 |
| wasita | user (social) | 2 |
| AustinCStone | user (social) | 2 |
| M1shaaa | user (social) | 1 |
| DJedamski | user (social) | 1 |
| kristinezheng | user (social) | 1 |
| **TOTAL** | | **268** |

### Notable Recent Activity (pushed 2026-08-03)

- **plurigrid/gorj** — forj + Rama topology + GF(3) (1604 open issues, active)
- **kubeflow/hub** — Model Registry (Go)
- **kubeflow/pipelines** — ML Pipelines (Python)
- **bmorphism/Gay.jl** — Wide-gamut color SPI (Julia)
- **TeglonLabs/jank-crane** — crane-jank converged-IR hub, GF3 convergence maps (C++)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

**Result:** All 28 addresses returned `Resource not found` from Aptos mainnet fullnode.  
No `0x1::coin::CoinStore<AptosCoin>` resource registered on any address — accounts are unfunded/unactivated. Balance recorded as NULL.

### Multisig Contract Probes (5/5 healthy)

All contracts required exactly **2 signatures**:

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428… | 2 | ✓ |
| A-G | 0xf56c4a1c… | 2 | ✓ |
| Y-Z | 0xd3ffe181… | 2 | ✓ |
| S-T | 0x3b1c3ae9… | 2 | ✓ |
| V-W | 0x40fad7b4… | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable.** The URL returns a Next.js SPA — no REST API endpoint exposes market data without JavaScript execution. No rows inserted into `mnx_snapshots`.

---

## DuckDB Tables

| Table | Rows |
|-------|------|
| world_increments | 268 |
| repo_snapshots | 268 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

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
