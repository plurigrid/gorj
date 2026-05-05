# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-05-05  
**GF(3) Color:** `#b8bb26` PLUS (trit=1)  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured | Total Stars |
|--------|------|----------------|-------------|
| plurigrid | org | 100 | 66 |
| kubeflow | org | 47 | 34,001 |
| TeglonLabs | org | 4 | 2 |
| bmorphism | user | 100 | 247 |
| zubyul | user | 49 | 14 |
| migalkin | social-graph | 5 | 274 |
| AustinCStone | social-graph | 4 | 106 |
| wasita | social-graph | 4 | 3 |
| DJedamski | social-graph | 3 | 2 |
| M1shaaa | social-graph | 3 | 0 |
| kristinezheng | social-graph | 2 | 0 |
| **TOTAL (this sweep)** | | **321** | **34,715** |

### Notable Repos

- **kubeflow/trainer** – Distributed AI Model Training on Kubernetes (2,096 ★)
- **kubeflow/kubeflow** – ML Toolkit for Kubernetes (15,621 ★)
- **kubeflow/spark-operator** – Kubernetes Spark operator (3,123 ★)
- **migalkin/NodePiece** – Compositional KG representations, ICLR'22 (143 ★)
- **migalkin/StarE** – Hyper-relational KG message passing, EMNLP'20 (89 ★)
- **plurigrid/nanoclj-zig** – NaN-boxed Clojure in Zig with GF(3) trit conservation
- **plurigrid/gorj** – forj + Rama topology + GF(3) gay trit coloring (this repo, 64 open issues)
- **bmorphism/Gay.jl** – GF(3) deterministic coloring library

### DuckDB Table Counts

| Table | Total Rows | New This Run |
|-------|-----------|--------------|
| world_increments | 24 | 1 |
| repo_snapshots | 1,265 | 321 |
| aptos_snapshots | 28 | 28 |
| multisig_probes | 5 | 5 |
| mnx_snapshots | 0 | 0 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (A–Z + alice + bob)

All 28 addresses returned HTTP 404 from `fullnode.mainnet.aptoslabs.com`.  
These accounts have not been initialized on-chain (no CoinStore resource registered).  
Balance recorded as NULL in `aptos_snapshots`.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | NULL (404) |
| bob | 0x0a3c...512d | NULL (404) |
| A–Z | 26 addresses | NULL (404) |

### Multisig Contract Probes

All 5 multisig contracts responded successfully. All require **2 signatures**.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...003 | 2 | HEALTHY |
| A-G | 0xf56c...096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...883 | 2 | HEALTHY |
| S-T | 0x3b1c...883 | 2 | HEALTHY |
| V-W | 0x40fa...b6d | 2 | HEALTHY |

### MNX Testnet Markets

`https://testnet.mnx.fi` is a Next.js SPA. All JSON API paths returned HTTP 404.
The `/markets` route returns HTML shell only — no market data extractable.
Status: **UNAVAILABLE** — `mnx_snapshots` table is empty.

---

## GF(3) Color Chain

| id % 3 | Trit | Color | Name |
|--------|------|-------|------|
| 0 | 0 | `#d3869b` | ERGODIC |
| 1 | 1 | `#b8bb26` | PLUS |
| 2 | -1 | `#cc241d` | MINUS |

This sweep added increment **#24** → `#d3869b` ERGODIC (24 % 3 == 0).
