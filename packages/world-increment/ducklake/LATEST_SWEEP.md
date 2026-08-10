# World-Increment Sweep + Hamming Snapshot
**Date:** 2026-08-10  
**Sweep ID:** world-increment/sweep-2026-08-10  
**GF(3) Chain:** 329 new increments — ERGODIC×109 (#d3869b) · PLUS×110 (#b8bb26) · MINUS×110 (#cc241d)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Scanned
| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| kubeflow | org | 49 | 34,498 |
| bmorphism | user | 100 | 247 |
| migalkin | user (zubyul graph) | 6 | 278 |
| plurigrid | org | 100 | 115 |
| AustinCStone | user (zubyul graph) | 6 | 103 |
| zubyul | user | 49 | 14 |
| wasita | user (zubyul graph) | 5 | 3 |
| TeglonLabs | org | 5 | 2 |
| DJedamski | user (zubyul graph) | 3 | 2 |
| kristinezheng | user (zubyul graph) | 3 | 0 |
| M1shaaa | user (zubyul graph) | 3 | 0 |

**Total:** 329 repos snapshotted across 11 sources

### Top Repos by Stars (new this sweep)
| Repo | Language | ★ | Forks |
|------|----------|---|-------|
| kubeflow/kubeflow | — | 15,808 | 2,691 |
| kubeflow/pipelines | Python | 4,180 | 2,084 |
| kubeflow/spark-operator | Python | 3,146 | 1,512 |
| kubeflow/trainer | Go | 2,177 | 1,017 |
| kubeflow/katib | Python | 1,694 | 535 |
| migalkin/NodePiece | Python | 144 | 21 |
| AustinCStone/TextGAN | Python | 92 | 30 |
| migalkin/StarE | Python | 89 | 16 |
| TeglonLabs/mathpix-gem | Ruby | 2 | 0 |
| TeglonLabs/jank-crane | C++ | 0 | 0 |

### Language Distribution (top 10)
| Language | Repos |
|----------|-------|
| Python | 60 |
| Rust | 26 |
| TypeScript | 21 |
| JavaScript | 20 |
| HTML | 16 |
| Go | 15 |
| Clojure | 14 |
| Jupyter Notebook | 13 |
| Julia | 9 |
| Zig | 7 |

### Notable Activity
- **wasita** most recently pushed: `xoxowasita-analysis` (2026-08-06), `wm-cv` (2026-08-07) — active
- **TeglonLabs/jank-crane**: C++ repo, crane-jank converged-IR hub with GF3 convergence maps (created 2026-06-08)
- **migalkin**: Knowledge graph ML focus — NBFNet, NodePiece, StarE all updated 2026

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)
All 28 addresses queried via Aptos mainnet fullnode.  
**Result:** All balances = 0 APT — no `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource registered on any address.

| World | Address (prefix) | APT Balance |
|-------|------------------|-------------|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…12d5 | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes
All 5 multisig contracts queried via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|------------------|---------------|---------|
| A-B | 0x0da4…7003 | 2 | ✅ |
| A-G | 0xf56c…0096 | 2 | ✅ |
| Y-Z | 0xd3ff…b883 | 2 | ✅ |
| S-T | 0x3b1c…7883 | 2 | ✅ |
| V-W | 0x40fa…eb6d | 2 | ✅ |

**All 5 multisig contracts respond with 2-of-N threshold. All healthy.**

### MNX Markets (testnet.mnx.fi)
**Status: Unavailable** — `testnet.mnx.fi` serves a Next.js SPA with no public REST API endpoints at `/api/markets`, `/api/v1/markets`, or `/api/tickers`. No market data could be extracted.

---

## DuckDB Ducklake State
**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | New Rows | Cumulative |
|-------|----------|------------|
| world_increments | 329 | 352 |
| repo_snapshots | 329 | 1,273 |
| aptos_snapshots | 28 | 28 |
| multisig_probes | 5 | 5 |
| mnx_snapshots | 0 | 0 |
