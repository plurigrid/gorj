# World-Increment Sweep — 2026-07-11

## Sweep Metadata
- **Date:** 2026-07-11 15:13:37 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 35 |
| Total Repo Snapshots (cumulative) | 1336 |
| New Increments This Run | 12 |
| New Repo Snapshots This Run | 392 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Testnet | unavailable (401) |

---

## GF(3) Color Chain — This Run

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 14 | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 15 | TeglonLabs (org) | repo_snapshot | +0 | `#d3869b` | **ERGODIC** |
| 16 | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 17 | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 18 | migalkin (user) | repo_snapshot | +0 | `#d3869b` | **ERGODIC** |
| 19 | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 20 | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 21 | kristinezheng (user) | repo_snapshot | +0 | `#d3869b` | **ERGODIC** |
| 22 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 23 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 24 | gorj (system) | sweep_complete | +0 | `#d3869b` | **ERGODIC** |

GF(3) chain: **PLUS** → **MINUS** → **ERGODIC** → **PLUS** → **MINUS** → **ERGODIC** → **PLUS** → **MINUS** → **ERGODIC** → **PLUS** → **MINUS** → **ERGODIC**

---

## Top Repos by Stars (This Run)

| Source | Repo | Language | Stars | Last Push |
|--------|------|----------|-------|-----------|
| kubeflow | [kubeflow/kubeflow](https://github.com/kubeflow/kubeflow) | — | 15770 | 2026-07-10 |
| kubeflow | [kubeflow/pipelines](https://github.com/kubeflow/pipelines) | Python | 4169 | 2026-07-11 |
| kubeflow | [kubeflow/spark-operator](https://github.com/kubeflow/spark-operator) | Python | 3137 | 2026-07-10 |
| kubeflow | [kubeflow/trainer](https://github.com/kubeflow/trainer) | Go | 2135 | 2026-07-10 |
| kubeflow | [kubeflow/katib](https://github.com/kubeflow/katib) | Python | 1689 | 2026-07-10 |
| kubeflow | [kubeflow/examples](https://github.com/kubeflow/examples) | Jsonnet | 1460 | 2025-04-14 |
| kubeflow | [kubeflow/community-distribution](https://github.com/kubeflow/community-distribution) | YAML | 1029 | 2026-07-11 |
| kubeflow | [kubeflow/arena](https://github.com/kubeflow/arena) | Go | 815 | 2026-07-10 |
| kubeflow | [kubeflow/kale](https://github.com/kubeflow/kale) | Python | 695 | 2026-07-10 |
| kubeflow | [kubeflow/mpi-operator](https://github.com/kubeflow/mpi-operator) | Go | 529 | 2026-07-10 |
| kubeflow | [kubeflow/fairing](https://github.com/kubeflow/fairing) | Jsonnet | 337 | 2022-04-11 |
| kubeflow | [kubeflow/pytorch-operator](https://github.com/kubeflow/pytorch-operator) | Jsonnet | 310 | 2021-12-01 |
| kubeflow | [kubeflow/community](https://github.com/kubeflow/community) | Jupyter Notebook | 195 | 2026-07-11 |
| kubeflow | [kubeflow/website](https://github.com/kubeflow/website) | HTML | 184 | 2026-07-10 |
| kubeflow | [kubeflow/kfp-tekton](https://github.com/kubeflow/kfp-tekton) | TypeScript | 183 | 2024-11-19 |

---

## Repo Counts by Source (This Run)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 49 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| wasita | user | 11 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user | 5 |
| **TOTAL** | | **392** |

---

## Hamming Swarm — Aptos Wallet Snapshot

- **Wallets probed:** 28 (alice, bob, A–Z)
- **Balances with CoinStore resource:** 0 / 28 (all accounts lack APT CoinStore on mainnet)
- **Note:** resource_not_found for all — accounts may exist but have no APT coin store initialized

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428a0c007da0f...` | 2 | ✓ |
| A-G | `0xf56c4a1c0906214f3f...` | 2 | ✓ |
| S-T | `0x3b1c3ae905d44c3a49...` | 2 | ✓ |
| V-W | `0x40fad7b423a843650f...` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b2df40622...` | 2 | ✓ |

**All 5 multisig contracts healthy — each requires 2-of-N signatures.**

---

## MNX Testnet

- Status: **Unavailable** — HTTP 401 Unauthorized on all probed endpoints
- Paths tried: `/api/markets`, `/api/v1/markets`, `/markets`, `/api/ticker`

---

## Notable Highlights
- **kubeflow/kubeflow**: 15,770 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,169 stars — most popular ML pipeline for Kubernetes
- **kubeflow/spark-operator**: 3,137 stars — Kubernetes operator for Apache Spark
- **migalkin/NodePiece**: 144 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for Model Context Protocol
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 30 stars — topological chemputer (pushed 2026-07-10)
- **plurigrid/gorj**: 1 star, 1122 open issues — this repo — forj + GF(3) trit coloring
- **TeglonLabs/jank-crane**: new since last sweep — crane-jank converged-IR hub with GF3 convergence maps
- **M1shaaa/M1shaaa**: pushed 2026-07-11 — active today — profile config repo
- **wasita/wasita.github.io**: pushed 2026-07-06 — personal website in Svelte
- **kristinezheng/kristinezheng.github.io**: pushed 2026-07-01 — personal site

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
