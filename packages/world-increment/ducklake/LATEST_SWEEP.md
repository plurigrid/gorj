# World-Increment Sweep + Hamming Swarm Snapshot — 2026-08-05

## Sweep Metadata
- **Date:** 2026-08-05
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 419 |
| Total Repo Snapshots | 396 unique (1340 rows incl. historical) |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 (all healthy) |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain Distribution (2026-08-05)

| Name | Trit | Color | Count |
|------|:----:|-------|------:|
| ERGODIC | 0 | `#d3869b` | 139 |
| PLUS | +1 | `#b8bb26` | 140 |
| MINUS | -1 | `#cc241d` | 140 |

### Repos by Source

| Source | Type | Repos | Total Stars | Latest Push |
|--------|------|:-----:|:-----------:|-------------|
| plurigrid | org | 100 | 192 | 2026-08-05 |
| kubeflow | org | 49 | 102,192 | 2026-08-05 |
| TeglonLabs | org | 5 | 14 | 2026-06-08 |
| bmorphism | user | 100 | 515 | 2026-08-05 |
| zubyul | user | 49 | 40 | 2026-07-18 |
| migalkin | social | 19 | 833 | 2025-08-04 |
| DJedamski | social | 6 | 17 | 2018-03-07 |
| wasita | social | 14 | 11 | 2026-08-04 |
| kristinezheng | social | 5 | 0 | 2026-07-01 |
| M1shaaa | social | 8 | 0 | 2026-08-05 |
| AustinCStone | social | 41 | 324 | 2026-07-15 |
| **TOTAL** | | **396** | **104,138** | |

### Top Starred Repos (2026-08-05)

| Repo | Language | Stars | Description |
|------|----------|------:|-------------|
| kubeflow/kubeflow | — | 15,805 | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | Python | 4,177 | Machine Learning Pipelines for Kubeflow |
| kubeflow/spark-operator | Python | 3,143 | Kubernetes operator for Apache Spark |
| kubeflow/trainer | Go | 2,170 | Distributed AI Training & LLM Fine-Tuning on Kubernetes |
| migalkin/NodePiece | Python | 143 | Scalable knowledge graph embeddings |
| AustinCStone/TextGAN | Python | 92 | Text generation with GANs |
| migalkin/StarE | Python | 88 | Relation prediction on temporal knowledge graphs |
| bmorphism/ocaml-mcp-sdk | OCaml | 60 | OCaml SDK for Model Context Protocol |
| plurigrid/asi | HTML | 59 | everything is topological chemputer! |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | Anti-bullshit MCP server |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-08-05)

Queried `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` for all 28 addresses.

**Result:** All 28 addresses returned `resource_not_found` — accounts exist on-chain but have not registered the legacy CoinStore module. Balance = 0.0 APT for all.

### Multisig Contract Health (5 pairs)

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|:-------------:|:------:|
| A-B | 0x0da4…3003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c…0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff…b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c…7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa…eb6d | 2 | ✓ HEALTHY |

All 5 multisig accounts require 2-of-2 signatures and are fully operational.

### MNX Testnet Markets

`https://testnet.mnx.fi` is a Next.js SPA — no accessible REST API at `/api/markets` or similar paths. Status: **unavailable via direct probe**.

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
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — most popular ML pipeline for Kubernetes (pushed 2026-04-10)
- **kubeflow/spark-operator**: 3,111 stars — Kubernetes operator for Apache Spark (pushed 2026-04-10)
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 16 stars — topological chemputer (pushed 2026-04-10)
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **Increment 12**: ERGODIC — sweep_complete closing the 4th full GF(3) cycle
