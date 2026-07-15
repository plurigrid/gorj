# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-15  
**Branch:** world-increment/sweep-2026-07-15

---

## JOB 1: GitHub Social Graph Sweep

### Sources Crawled

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin (social) | user | 19 |
| wasita (social) | user | 11 |
| AustinCStone (social) | user | 40 |
| DJedamski (social) | user | 6 |
| kristinezheng (social) | user | 5 |
| M1shaaa (social) | user | 8 |
| **Total** | | **392** |

### Top Repos by Stars

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,777 | 2026-07-10 |
| kubeflow/pipelines | Python | 4,166 | 2026-07-14 |
| kubeflow/spark-operator | Python | 3,136 | 2026-07-14 |
| kubeflow/trainer | Go | 2,143 | 2026-07-14 |
| migalkin/NodePiece | Python | 144 | 2021-06-14 |
| AustinCStone/TextGAN | Python | 92 | 2016-09-19 |
| migalkin/StarE | Python | 89 | 2020-09-17 |
| plurigrid/asi | HTML | 30 | 2026-07-10 |
| migalkin/kgcourse2021 | HTML | 24 | 2020-09-01 |
| plurigrid/gorj | Clojure | 1 | 2026-07-15 |

### Notable Recent Activity (plurigrid)
- `plurigrid/gorj` — pushed 2026-07-15 (today): forj + Rama topology nREPL routing + GF(3) gay trit coloring
- `plurigrid/place` — pushed 2026-07-14
- `plurigrid/eirobri` — pushed 2026-07-14: EiRoBri replay world
- `plurigrid/asi` — pushed 2026-07-10: everything is topological chemputer!

### TeglonLabs Recent
- `TeglonLabs/jank-crane` — pushed 2026-06-08: crane-jank converged-IR hub; loopify pass spec, GF3 convergence maps

### GF(3) Color Chain Distribution
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 112 |
| 1 | #b8bb26 | PLUS | 112 |
| -1 | #cc241d | MINUS | 112 |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances

All 28 addresses (alice, bob, A–Z) returned **HTTP 404** from `0x1::coin::CoinStore`.  
Accounts appear uninitialized or APT CoinStore not registered on mainnet.

| World | Address (truncated) | Status |
|-------|---------------------|--------|
| alice | 0xc793...cc7b | not_found |
| bob | 0x0a3c...12d5 | not_found |
| A–Z | 26 addresses | not_found |

### Multisig Contract Probes

All 5 multisig contracts **healthy** (sigs_required=2):

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Unavailable** — all API paths return HTTP 401 (authentication/login required).  
Paths tried: `/api/markets`, `/api/v1/markets`, `/api/tickers`

---

## DuckDB Ducklake

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | New Rows |
|-------|----------|
| world_increments | 313 |
| repo_snapshots | 313 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (unavailable) |
