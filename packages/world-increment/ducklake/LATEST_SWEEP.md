# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-03

**Date:** 2026-06-03  
**Branch:** world-increment/sweep  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 101 total (21 snapshotted) |
| kubeflow | org | 48 total (16 snapshotted) |
| TeglonLabs | org | 4 total (4 snapshotted) |
| bmorphism | user | 103 total (14 snapshotted) |
| zubyul | user | 49 total (8 snapshotted) |
| migalkin | social graph | 5 snapshotted |
| wasita | social graph | 3 snapshotted |
| kristinezheng | social graph | 2 snapshotted |
| M1shaaa | social graph | 2 snapshotted |
| AustinCStone | social graph | 4 snapshotted |
| DJedamski | social graph | 2 snapshotted |

**Total repo snapshots:** 80
**World increments:** 80 (GF3 color chain applied)

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 26 |
| +1 | `#b8bb26` | PLUS | 27 |
| -1 | `#cc241d` | MINUS | 27 |

### Notable Repos

**plurigrid** — top by stars: `asi` (24*), `vcg-auction` (7*), `agent` (5*)
- `gorj` (this repo!): 312 open issues, active
- `nanoclj-zig`: NaN-boxed Clojure in Zig with GF(3) trit conservation

**kubeflow** — flagship ML-on-K8s org
- `kubeflow/kubeflow`: 15,704* — top repo in sweep
- `pipelines`: 4,151*, active (pushed 2026-06-02)
- `spark-operator`: 3,125*
- `trainer`: 2,110* (distributed AI training)
- `mcp-apache-spark-history-server`: 173* — MCP integration for Spark

**bmorphism** — prolific MCP ecosystem builder
- `Gay.jl`: 189 open issues — very active
- `ocaml-mcp-sdk`: 61* — OCaml MCP SDK
- `say-mcp-server`, `babashka-mcp-server`, `manifold-mcp-server`

**migalkin** (knowledge graph researcher)
- `NodePiece`: 144* — compositional KG representations (ICLR 22)
- `StarE`: 89* — hyper-relational KG message passing (EMNLP 20)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses queried via Aptos fullnode mainnet API.

| World | Balance (APT) | Note |
|-------|---------------|------|
| alice | 0.0 | CoinStore absent — unfunded |
| bob   | 0.0 | CoinStore absent — unfunded |
| A-Z   | 0.0 each | All 26 addresses unfunded |

All addresses returned 0 APT. Accounts have no CoinStore resource, consistent with key pairs that have never received a transaction.

### Multisig Contract Probes (Aptos Mainnet)

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | YES |
| A-G | 0xf56c...0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

All 5 multisig accounts live, requiring 2-of-N signatures. All healthy.

### MNX Markets (testnet.mnx.fi)

Status: Unavailable for programmatic extraction. Next.js SPA — no /api/markets endpoint accessible. Zero rows in mnx_snapshots.

---

## DuckDB Schema

```
world-increments.duckdb
  world_increments    80 rows  -- GF3-colored repo push events
  repo_snapshots      80 rows  -- full repo metadata
  aptos_snapshots     28 rows  -- Hamming swarm wallet balances
  multisig_probes      5 rows  -- on-chain multisig health
  mnx_snapshots        0 rows  -- MNX markets (SPA, unavailable)
```

## Sweep Metadata
- **Date:** 2026-04-12
- **Agent:** world-increment-sweep
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 12 |
| Total Repo Snapshots | 471 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain — All 12 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 12 | bmorphism (org) | sweep_complete (gorj) | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## Top Repos by Source

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 16 | 2026-04-10 |
| ontology | JavaScript | 7 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-09 |
| zig-syrup | Zig | 2 | 2026-04-09 |
| vivarium | Clojure | 1 | 2026-04-08 |

### kubeflow (47 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15565 | 2026-01-05 |
| pipelines | Python | 4119 | 2026-04-10 |
| spark-operator | Python | 3111 | 2026-04-10 |
| trainer | Go | 2080 | 2026-04-10 |
| katib | Python | 1676 | 2026-04-02 |

### TeglonLabs (53 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| vibespace | HTML | 2 |
| acp.el | — | 1 |
| mcp-terminal | — | 1 |

### bmorphism (100 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 60 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| shitcoin | Python | 5 |
| open-location-code-zig | Zig | 3 |

### migalkin (30 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 143 |
| StarE | Python | 88 |
| kgcourse2021 | HTML | 25 |

### AustinCStone (43 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 47 |
| AustinCStone | user | 43 |
| migalkin | user | 30 |
| wasita | user | 29 |
| zubyul | user | 24 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| **TOTAL** | | **471** |

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
