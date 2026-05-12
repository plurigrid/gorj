# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-05-12T16:14Z  
**Branch:** world-increment/sweep  
**DuckDB:** `world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Covered

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 48 |
| AustinCStone | user (zubyul graph) | 30 |
| migalkin | user (zubyul graph) | 19 |
| wasita | user (zubyul graph) | 11 |
| M1shaaa | user (zubyul graph) | 8 |
| DJedamski | user (zubyul graph) | 6 |
| kristinezheng | user (zubyul graph) | 5 |
| TeglonLabs | org | 4 |
| **TOTAL** | | **380** |

### Top Languages

| Language | Repos |
|----------|-------|
| Python | 79 |
| Rust | 26 |
| JavaScript | 24 |
| TypeScript | 23 |
| Go | 15 |
| HTML | 15 |
| Jupyter Notebook | 14 |
| Clojure | 13 |
| Julia | 9 |
| Jsonnet | 8 |

### Top Starred Repos

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,629 | — |
| kubeflow/pipelines | 4,139 | Python |
| kubeflow/spark-operator | 3,125 | Python |
| kubeflow/trainer | 2,097 | Go |
| kubeflow/katib | 1,683 | Python |
| kubeflow/examples | 1,462 | Jsonnet |
| kubeflow/manifests | 1,016 | YAML |
| kubeflow/arena | 810 | Go |
| kubeflow/kale | 686 | Python |
| kubeflow/mpi-operator | 526 | Go |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 126 |
| +1 | `#b8bb26` | PLUS | 127 |
| -1 | `#cc241d` | MINUS | 127 |

### Notable Recent Activity

- **plurigrid/gorj** — pushed 2026-05-12 (this repo!) — Clojure, 162 open issues
- **plurigrid/zig-syrup** — pushed 2026-04-30 — High-perf Zig OCapN Syrup + CapTP
- **plurigrid/asi** — pushed 2026-04-26 — topological chemputer (21 ⭐)
- **M1shaaa/M1shaaa** — pushed 2026-05-12 — GitHub profile config (active today)
- **TeglonLabs/mathpix-gem** — pushed 2026-01-01 — Ruby math OCR gem (2 ⭐, 11 issues)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

All 28 addresses queried. Results:

| World | Status | Balance (APT) |
|-------|--------|---------------|
| alice | resource_not_found (unregistered) | 0.0 |
| bob | resource_not_found (unregistered) | 0.0 |
| A–R | resource_not_found (unregistered) | 0.0 each |
| S | CoinStore registered, empty | 0.0 |
| T | CoinStore registered, empty | 0.0 |
| U | CoinStore registered, empty | 0.0 |
| V | CoinStore registered, empty | 0.0 |
| W | CoinStore registered, empty | 0.0 |
| X | CoinStore registered, empty | 0.0 |
| Y | CoinStore registered, empty | 0.0 |
| Z | CoinStore registered, empty | 0.0 |

All 28 wallets hold **0.0 APT** as of snapshot. Addresses A–R have no `CoinStore` resource registered (accounts exist on-chain but APT coin store not initialized). Addresses S–Z have registered CoinStores with zero balance.

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428...` | 2 | ✅ |
| A-G | `0xf56c4a1c...` | 2 | ✅ |
| Y-Z | `0xd3ffe181...` | 2 | ✅ |
| S-T | `0x3b1c3ae9...` | 2 | ✅ |
| V-W | `0x40fad7b4...` | 2 | ✅ |

All 5 multisig contracts respond correctly. Each requires **2-of-N signatures** — healthy.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — The frontend SPA (`testnet.mnx.fi`) is a Next.js Vercel deployment. The backend API (`api.testnet.mnx.fi`) returns Express `Cannot GET` for all probed paths (`/`, `/markets`, `/v1/markets`). Market data is served over WebSocket (`wss://api.testnet.mnx.fi`) per CSP headers. No REST market data extractable without auth.

---

## DuckDB Schema Summary

```
world_increments   — 380 rows (GF3-colored repo snapshot increments)
repo_snapshots     — 380 rows (org/user/repo metadata)
aptos_snapshots    —  28 rows (Hamming swarm wallet balances)
multisig_probes    —   5 rows (2-of-N contract health checks)
mnx_snapshots      —   1 row  (unavailable marker)
```
