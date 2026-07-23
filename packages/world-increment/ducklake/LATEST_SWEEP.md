# World-Increment Sweep — 2026-07-23

## Sweep Metadata
- **Date:** 2026-07-23
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Python binding)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (all-time) | 35 |
| Total Repo Snapshots (all-time) | 1338 |
| New Increments This Run | 11 |
| New Repo Snapshots This Run | 394 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Aptos Wallets Funded | 0 (all resource_not_found) |
| Multisig Contracts Probed | 5 |
| Multisig Contracts Healthy | 5 |
| MNX Markets | Unavailable (SPA only) |

---

## GF(3) Color Chain — New Increments (IDs 13–24)

| ID | Source | Type | Event | Repos | GF3 Trit | Color | Name |
|----|--------|------|-------|-------|-----------|-------|------|
| 13 | plurigrid | org | repo_snapshot | 100 | 1 | `#b8bb26` | **PLUS** |
| 14 | kubeflow | org | repo_snapshot | 49 | -1 | `#cc241d` | **MINUS** |
| 15 | TeglonLabs | org | repo_snapshot | 5 | 0 | `#d3869b` | **ERGODIC** |
| 16 | bmorphism | user | repo_snapshot | 100 | 1 | `#b8bb26` | **PLUS** |
| 17 | zubyul | user | repo_snapshot | 49 | -1 | `#cc241d` | **MINUS** |
| 18 | migalkin | user | repo_snapshot | 19 | 0 | `#d3869b` | **ERGODIC** |
| 19 | DJedamski | user | repo_snapshot | 6 | 1 | `#b8bb26` | **PLUS** |
| 20 | wasita | user | repo_snapshot | 12 | -1 | `#cc241d` | **MINUS** |
| 21 | kristinezheng | user | repo_snapshot | 5 | 0 | `#d3869b` | **ERGODIC** |
| 22 | M1shaaa | user | repo_snapshot | 8 | 1 | `#b8bb26` | **PLUS** |
| 23 | AustinCStone | user | repo_snapshot | 41 | -1 | `#cc241d` | **MINUS** |
| 24 | world-increment-sweep | meta | sweep_complete | — | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## Top Repos by Stars (This Run)

| Source | Repo | Language | Stars | Last Pushed |
|--------|------|----------|-------|-------------|
| kubeflow | kubeflow | — | 15789 | 2026-07-10 |
| kubeflow | pipelines | Python | 4169 | 2026-07-23 |
| kubeflow | spark-operator | Python | 3143 | 2026-07-17 |
| kubeflow | trainer | Go | 2153 | 2026-07-23 |
| kubeflow | katib | Python | 1692 | 2026-07-22 |
| kubeflow | examples | Jsonnet | 1461 | 2025-04-14 |
| kubeflow | community-distribution | YAML | 1029 | 2026-07-23 |
| kubeflow | arena | Go | 815 | 2026-07-21 |
| kubeflow | kale | Python | 695 | 2026-07-23 |
| kubeflow | mpi-operator | Go | 530 | 2026-07-22 |

---

## Repo Counts by Source (This Run)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | user | 41 |
| migalkin | user | 19 |
| wasita | user | 12 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user | 5 |
| **TOTAL** | | **394** |

---

## Notable Highlights

- **kubeflow/kubeflow**: 15789 stars (unknown) — Machine Learning Toolkit for Kubernetes
- **kubeflow/pipelines**: 4169 stars (Python) — Machine Learning Pipelines for Kubeflow
- **kubeflow/spark-operator**: 3143 stars (Python) — Kubernetes operator for managing the lifecycle of Apache Spark applications on Kubernetes. 
- **kubeflow/trainer**: 2153 stars (Go) — Distributed AI Model Training and LLM Fine-Tuning on Kubernetes
- **kubeflow/katib**: 1692 stars (Python) — Automated Machine Learning on Kubernetes
- **kubeflow/examples**: 1461 stars (Jsonnet) — A repository to host extended examples and tutorials
- **kubeflow/community-distribution**: 1029 stars (YAML) — Kubeflow Community Distribution
- **kubeflow/arena**: 815 stars (Go) — A CLI for Kubeflow. 
- **TeglonLabs/jank-crane** (NEW since last sweep): C++ — crane-jank converged-IR hub with GF3 convergence maps
- **M1shaaa/M1shaaa**: pushed TODAY (2026-07-23T13:48:23Z) — active profile activity detected
- **kristinezheng/kristinezheng.github.io**: pushed 2026-07-01 — recent personal site update

---

## Hamming Swarm Snapshot — Aptos

### Wallet Balances (28 addresses: alice, bob, A–Z)

All 28 wallets returned `resource_not_found` from Aptos mainnet. This indicates the wallet addresses exist but have **no CoinStore<AptosCoin> resource** — i.e. they hold 0 APT and have never received any on-chain APT transfer.

| Status | Count |
|--------|-------|
| resource_not_found (unfunded) | 28 |
| Funded (> 0 APT) | 0 |

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428a0c007da0f...` | 2 | ✓ YES |
| A-G | `0xf56c4a1c0906214f3f...` | 2 | ✓ YES |
| Y-Z | `0xd3ffe1812b2df40622...` | 2 | ✓ YES |
| S-T | `0x3b1c3ae905d44c3a49...` | 2 | ✓ YES |
| V-W | `0x40fad7b423a843650f...` | 2 | ✓ YES |

**All 5 multisig contracts healthy.** All require 2-of-2 signatures. No anomalies detected.

### MNX Markets (testnet.mnx.fi)

Testnet MNX endpoint returns SPA HTML on all probed paths (`/api/markets`, `/api/v1/markets`, `/markets`, `/api/tickers`). No market data available via REST API — likely requires browser execution / WebSocket.

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

## All-Time DB Stats
- World increments: 35 (runs 1–24)
- Repo snapshots: 1338
- Aptos snapshots: 28 rows
- Multisig probes: 5 rows
