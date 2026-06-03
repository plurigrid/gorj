# World-Increment Sweep + Hamming Snapshot — 2026-06-03

## Sweep Metadata
- **Date:** 2026-06-03
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 171 |
| Sources Covered | 3 orgs + 8 users |
| Total Stars Across Graph | 33,594 |

---

### GF(3) Color Chain — All 11 Increments

| ID | Source | Type | GF3 Trit | Color | Name | Repos | Stars |
|----|--------|------|----------|-------|------|-------|-------|
| 1 | plurigrid | org | +1 | `#b8bb26` | **PLUS** | 46 | 71 |
| 2 | kubeflow | org | −1 | `#cc241d` | **MINUS** | 25 | 32,913 |
| 3 | TeglonLabs | org | 0 | `#d3869b` | **ERGODIC** | 4 | 2 |
| 4 | bmorphism | user | +1 | `#b8bb26` | **PLUS** | 28 | 202 |
| 5 | zubyul | user | −1 | `#cc241d` | **MINUS** | 24 | 10 |
| 6 | migalkin | user | 0 | `#d3869b` | **ERGODIC** | 8 | 280 |
| 7 | DJedamski | user | +1 | `#b8bb26` | **PLUS** | 5 | 3 |
| 8 | wasita | user | −1 | `#cc241d` | **MINUS** | 9 | 5 |
| 9 | kristinezheng | user | 0 | `#d3869b` | **ERGODIC** | 5 | 0 |
| 10 | M1shaaa | user | +1 | `#b8bb26` | **PLUS** | 7 | 0 |
| 11 | AustinCStone | user | −1 | `#cc241d` | **MINUS** | 10 | 108 |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

### Top Repos by Source

#### plurigrid (46 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gorj | Clojure | 0 | 2026-06-03 |
| asi | HTML | 24 | 2026-04-26 |
| vcg-auction | Rust | 7 | 2023-03-16 |
| agent | Python | 5 | 2023-03-31 |
| ontology | JavaScript | 8 | 2025-05-27 |
| nanoclj-zig | Zig | 1 | 2026-04-25 |

#### kubeflow (25 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,705 | 2026-05-24 |
| pipelines | Python | 4,152 | 2026-06-03 |
| spark-operator | Python | 3,125 | 2026-06-03 |
| trainer | Go | 2,110 | 2026-06-03 |
| katib | Python | 1,685 | 2026-05-29 |

#### bmorphism (28 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| risc0-cosmwasm-example | Rust | 23 | 2022-10-20 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| say-mcp-server | JavaScript | 20 | 2025-01-07 |
| babashka-mcp-server | JavaScript | 18 | 2025-01-05 |
| Gay.jl | Julia | 1 | 2026-06-03 |

#### migalkin (8 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| NodePiece | Python | 144 | 2026-05-07 |
| StarE | Python | 89 | 2026-04-16 |
| kgcourse2021 | HTML | 25 | 2026-02-16 |
| NBFNet_mlx | Python | 10 | 2026-03-11 |

#### AustinCStone (10 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| TextGAN | Python | 92 | 2025-03-03 |
| StereoVisionMRF | Python | 11 | 2026-04-01 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All 28 Hamming swarm addresses queried via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
All returned `resource_not_found` — accounts may use the newer `0x1::fungible_asset` framework
or have not been funded on mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.00000000 |
| bob | 0x0a3c...512d | 0.00000000 |
| A–Z (26) | 0x8699... – 0x7af0... | 0.00000000 each |

**Total APT balance across swarm: 0.00000000**

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts healthy — `num_signatures_required = 2`:

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

**5/5 multisig pairs healthy (2-of-N threshold confirmed)**

### MNX Markets (testnet.mnx.fi)

- `GET /api/markets` → HTML (Next.js SPA, no REST JSON)
- `GET /api/v1/markets` → HTML (SPA fallback)
- `GET /api/tickers` → HTML (SPA fallback)

**Status: No public REST API available. `mnx_snapshots` table: 0 rows.**

---

## DuckDB Tables

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 11 | GF(3) sweep events per source |
| `repo_snapshots` | 171 | GitHub repo metadata |
| `aptos_snapshots` | 28 | Hamming swarm APT balances |
| `multisig_probes` | 5 | Aptos 2-of-N multisig health |
| `mnx_snapshots` | 0 | MNX market data (unavailable) |

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
- `id % 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id % 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id % 3 == 2` → trit=−1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,705★ — flagship ML platform for Kubernetes (pushed 2026-05-24)
- **kubeflow/pipelines**: 4,152★ — most popular ML pipeline for Kubernetes (pushed 2026-06-03)
- **kubeflow/spark-operator**: 3,125★ — Kubernetes operator for Apache Spark (pushed 2026-06-03)
- **migalkin/NodePiece**: 144★ — scalable KG embeddings, ICLR'22
- **bmorphism/ocaml-mcp-sdk**: 61★ — OCaml MCP SDK using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92★ — GAN text generation in TensorFlow
- **plurigrid/gorj**: This repo — forj + Rama topology nREPL routing + GF(3) trit coloring (331 open issues)
- **All 5 multisig pairs**: 2-of-N threshold confirmed healthy on Aptos mainnet
