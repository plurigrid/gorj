# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-24

## Sweep Metadata
- **Date:** 2026-07-24
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 314 |
| Total Repo Snapshots | 314 |
| Sources Covered | 3 orgs + 8 users + social graph |
| Aptos Addresses Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 (all HEALTHY) |
| MNX Markets | SPA (unavailable via API) |

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source
| Source | Type | Repos | Stars | Forks |
|--------|------|------:|------:|------:|
| kubeflow | org | 49 | 34,406 | 13,756 |
| migalkin | social | 3 | 257 | 45 |
| bmorphism | user | 100 | 246 | 73 |
| AustinCStone | social | 2 | 92 | 30 |
| plurigrid | org | 100 | 83 | 48 |
| zubyul | user | 49 | 14 | 2 |
| TeglonLabs | org | 5 | 2 | 2 |
| wasita | social | 3 | 2 | 0 |
| kristinezheng | social | 1 | 0 | 0 |
| DJedamski | social | 1 | 0 | 0 |
| M1shaaa | social | 1 | 0 | 0 |
| **TOTAL** | | **314** | **35,102** | **13,956** |

### Most Recently Pushed (last 7 days)
| Repo | Language | Stars | Pushed |
|------|----------|------:|--------|
| plurigrid/gorj | Clojure | 1 | 2026-07-24 |
| kubeflow/trainer | Go | 2,153 | 2026-07-24 |
| kubeflow/pipelines | Python | 4,169 | 2026-07-24 |
| kubeflow/hub | Go | 178 | 2026-07-24 |
| bmorphism/Gay.jl | Julia | 2 | 2026-07-24 |
| kubeflow/mpi-operator | Go | 530 | 2026-07-23 |
| kubeflow/community-distribution | YAML | 1,029 | 2026-07-23 |
| kubeflow/katib | Python | 1,692 | 2026-07-22 |
| plurigrid/eirobri | Clojure | 0 | 2026-07-21 |
| wasita/wasita.github.io | Svelte | 1 | 2026-07-21 |

### Notable Activity
- **plurigrid/gorj** (this repo): pushed 2026-07-24, 1,362 open issues, active
- **bmorphism/Gay.jl**: pushed 2026-07-24 — GF(3) gay trit coloring Julia lib
- **plurigrid/eirobri**: pushed 2026-07-21 — EiRoBri replay world (Clojure)
- **kubeflow**: heavily active — trainer, pipelines, hub, mpi-operator all pushed today
- **TeglonLabs/jank-crane**: new C++ repo (2026-06-08) — crane-jank converged-IR hub with GF3 convergence maps
- **wasita/pnas-typst-template**: created 2026-07-16 — new PNAS typst template
- **AustinCStone/byteruckus**: created 2026-07-15 — new HTML repo

### Top Repos by Stars (All Sources)
| Repo | Language | Stars | Forks |
|------|----------|------:|------:|
| kubeflow/pipelines | Python | 4,169 | 2,053 |
| kubeflow/spark-operator | Python | 3,143 | 1,504 |
| kubeflow/trainer | Go | 2,153 | 994 |
| kubeflow/katib | Python | 1,692 | 532 |
| kubeflow/community-distribution | YAML | 1,029 | 1,072 |
| kubeflow/arena | Go | 815 | 196 |
| migalkin/NodePiece | Python | 144 | 21 |
| AustinCStone/TextGAN | Python | 92 | 30 |
| migalkin/StarE | Python | 89 | 16 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2 |
| plurigrid/asi | HTML | 31 | 10 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
Queried 28 addresses (alice, bob, A–Z) on `fullnode.mainnet.aptoslabs.com`.

| Result | Count |
|--------|------:|
| No coin store (account not initialized) | 28 |
| Active balance > 0 APT | 0 |

All 28 Hamming-swarm addresses returned `Resource not found` — no `CoinStore<AptosCoin>` registered on mainnet. Accounts are defined in the swarm but have not been on-chain initialized.

### Multisig Contract Probes
All 5 probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|:-------------:|--------|
| A-B | 0x0da4f428…87003 | **2** | ✓ HEALTHY |
| A-G | 0xf56c4a1c…0096 | **2** | ✓ HEALTHY |
| Y-Z | 0xd3ffe181…b883 | **2** | ✓ HEALTHY |
| S-T | 0x3b1c3ae9…7883 | **2** | ✓ HEALTHY |
| V-W | 0x40fad7b4…eb6d | **2** | ✓ HEALTHY |

All multisig contracts respond with 2-of-N threshold. All contracts are deployed and callable on mainnet.

### MNX Markets (testnet.mnx.fi)
Probed `/api/markets`, `/api/v1/markets`, `/api/tickers` — all return a Next.js SPA. Market data is client-side rendered; **no public REST API available**. Logged as placeholder in `mnx_snapshots`.

---

## DuckDB Ducklake State
**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|-----:|
| world_increments | 314 |
| repo_snapshots | 314 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (placeholder) |

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
