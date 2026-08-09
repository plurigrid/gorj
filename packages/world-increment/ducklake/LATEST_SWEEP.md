# World Increment Sweep + Hamming Swarm Snapshot

**Run timestamp:** 2026-08-09T14:30 UTC  
**Branch:** world-increment/sweep-2026-08-09  

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social graph | 19 |
| wasita | social graph | 14 |
| AustinCStone | social graph | 41 |
| M1shaaa | social graph | 8 |
| DJedamski | social graph | 6 |
| kristinezheng | social graph | 5 |
| **Total** | | **396 repos** |

### Top Starred Repos (this sweep)

| Repo | Stars | Forks | Open Issues | Language | Last Push |
|------|-------|-------|-------------|----------|-----------|
| kubeflow/kubeflow | 15808 | 2691 | 0 | — | 2026-07-10 |
| kubeflow/pipelines | 4182 | 2084 | 525 | Python | 2026-08-09 |
| kubeflow/spark-operator | 3146 | 1512 | 122 | Python | 2026-08-08 |
| kubeflow/trainer | 2177 | 1017 | 154 | Go | 2026-08-08 |
| kubeflow/community-distribution | 1030 | 1070 | 29 | YAML | 2026-08-04 |
| AustinCStone/TextGAN | 92 | 30 | 5 | Python | 2016-09-19 |
| migalkin/NodePiece | 144 | 21 | 0 | Python | 2021-06-14 |
| migalkin/StarE | 89 | 16 | 1 | Python | 2020-09-17 |
| plurigrid/asi | 60 | 13 | 4 | HTML | 2026-07-10 |
| bmorphism/ocaml-mcp-sdk | 61 | 2 | 0 | OCaml | 2026-03-16 |

### Notable Activity

- **plurigrid/gorj** (this repo): 1745 open issues, last push 2026-08-09 — highly active
- **plurigrid/place**: GF3 topology canvas with 16 open issues
- **kubeflow/pipelines**: 525 open issues, active ML pipeline work
- **wasita**: new repo `xoxowasita-analysis` created 2026-08-04, actively updated
- **bmorphism**: 100 repos across Julia, OCaml, Zig, Clojure, Python — active polyglot
- **TeglonLabs/jank-crane**: C++ IR hub with GF3 convergence maps

### GF(3) Color Chain Distribution (cumulative ducklake)

| Trit | Name | Color | Count |
|------|------|-------|-------|
| +1 | PLUS | `#b8bb26` | 113 |
| 0 | ERGODIC | `#d3869b` | 111 |
| −1 | MINUS | `#cc241d` | 112 |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (alice–Z, 28 addresses)

All 28 addresses queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result:** All addresses returned 0 APT. These accounts appear to be unregistered for APT on mainnet (no CoinStore resource found), or are zero-balance accounts. The Aptos fullnode API responded successfully to all requests.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0 |
| bob | 0x0a3c...512d | 0 |
| A–Z | 0x8699...–0x7af0... | 0 each |

### Multisig Contract Probes

Endpoint: `POST /v1/view` → `0x1::multisig_account::num_signatures_required`

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | **2** | ✅ |
| A-G | 0xf56c...0096 | **2** | ✅ |
| Y-Z | 0xd3ff...b883 | **2** | ✅ |
| S-T | 0x3b1c...7883 | **2** | ✅ |
| V-W | 0x40fa...eb6d | **2** | ✅ |

All 5 multisig accounts are **healthy and require 2-of-N signatures**. No anomalies detected.

### MNX Markets (testnet.mnx.fi)

The site (`https://testnet.mnx.fi`) is a Next.js SPA and does not expose a public REST API at the probed paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`). The SPA returned HTML for all API probe paths — **market data unavailable via static endpoint probing.** Site is live and responsive (62KB HTML).

---

## DuckDB Ducklake Status

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows (cumulative) |
|-------|-------------------|
| world_increments | 336 |
| repo_snapshots | 1257 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA, no API) |

---

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent*
