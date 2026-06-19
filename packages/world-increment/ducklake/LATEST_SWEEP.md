# World-Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-06-19  
**DuckDB:** `world-increments.duckdb`  
**GF3 color chain:** id%3==0 → ERGODIC #d3869b | id%3==1 → PLUS #b8bb26 | id%3==2 → MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos | Total Stars | GF3 |
|--------|------|-------|-------------|-----|
| plurigrid | org | 49 | 14 | PLUS #b8bb26 |
| kubeflow | org | 48 | 34,230 | MINUS #cc241d |
| TeglonLabs | org | 5 | 2 | ERGODIC #d3869b |
| bmorphism | user | 100 | 241 | PLUS #b8bb26 |
| zubyul | user | 100 | 77 | MINUS #cc241d |
| migalkin | user | 19 | 280 | ERGODIC #d3869b |
| DJedamski | user | 6 | 3 | PLUS #b8bb26 |
| wasita | user | 11 | 5 | MINUS #cc241d |
| kristinezheng | user | 5 | 0 | ERGODIC #d3869b |
| M1shaaa | user | 8 | 0 | PLUS #b8bb26 |
| AustinCStone | user | 40 | 108 | MINUS #cc241d |
| **TOTAL** | | **391** | **34,960** | |

### Top Repos by Stars

| Repo | Stars | Forks | Language | Last Push |
|------|-------|-------|----------|-----------|
| kubeflow/kubeflow | 15,736 | 2,680 | — | 2026-06-18 |
| kubeflow/pipelines | 4,154 | 2,009 | Python | 2026-06-19 |
| kubeflow/spark-operator | 3,127 | 1,490 | Python | 2026-06-18 |
| kubeflow/trainer | 2,116 | 970 | Go | 2026-06-18 |
| kubeflow/katib | 1,683 | 528 | Python | 2026-06-15 |
| migalkin/NodePiece | 144 | 21 | Python | 2022-02-02 |

### Most Recently Active Repos (key graph nodes)

| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| zubyul/gorj | 0 | Clojure | 2026-06-19 ← this repo |
| bmorphism/Gay.jl | 1 | Julia | 2026-06-19 |
| zubyul/place | 1 | TeX | 2026-06-15 |
| bmorphism/satreadout | 0 | Lean | 2026-06-15 |
| zubyul/asi | 26 | HTML | 2026-06-10 |
| TeglonLabs/jank-crane | 0 | C++ | 2026-06-08 |
| bmorphism/world | 0 | Python | 2026-06-02 |

### World Increments (GF3 chain)

13 increment records in `world_increments` table:
- ids 1-11: GitHub org/user snapshots
- id 12: Aptos wallet swarm snapshot (ERGODIC #d3869b)
- id 13: Aptos multisig snapshot (PLUS #b8bb26)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried 28 addresses (alice, bob, A-Z) at fullnode.mainnet.aptoslabs.com.

**Result:** All 28 addresses returned 0 APT. The CoinStore<AptosCoin> resource was not registered for any address — accounts are uninitialized on mainnet.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793ac... | 0.0 |
| bob | 0x0a3c00... | 0.0 |
| A-Z | 0x8699ed... thru 0x7af0ef... | 0.0 each |

Total swarm APT: **0.0**

### Multisig Contract Probes

All 5 multisig contracts healthy, all require 2 signatures.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f4... | 2 | healthy |
| A-G | 0xf56c4a... | 2 | healthy |
| Y-Z | 0xd3ffe1... | 2 | healthy |
| S-T | 0x3b1c3a... | 2 | healthy |
| V-W | 0x40fad7... | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** - Both https://testnet.mnx.fi and /api/markets returned HTTP 401 Unauthorized. No market data retrieved.

---

## DuckDB Schema

Tables in `world-increments.duckdb`:

| Table | Rows |
|-------|------|
| world_increments | 13 |
| repo_snapshots | 391 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |
