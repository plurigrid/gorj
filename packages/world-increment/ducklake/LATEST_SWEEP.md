# World Increment Sweep + Hamming Snapshot
**Date:** 2026-07-31  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 24 |
| bmorphism | user | 20 |
| zubyul | user | 17 |
| kubeflow | org | 15 |
| wasita | social graph | 12 |
| AustinCStone | social graph | 8 |
| M1shaaa | social graph | 8 |
| migalkin | social graph | 6 |
| DJedamski | social graph | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | social graph | 5 |
| **TOTAL** | | **126** |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 42 |
| 1 | `#b8bb26` | PLUS | 42 |
| -1 | `#cc241d` | MINUS | 42 |

### Notable Active Repos (pushed within 30 days)

| Repo | Stars | Lang | Pushed | Description |
|------|-------|------|--------|-------------|
| kubeflow/pipelines | 4171 | Python | 2026-07-29 | ML Pipelines for Kubeflow |
| kubeflow/kubeflow | 15798 | — | 2026-07-10 | ML Toolkit for Kubernetes |
| kubeflow/trainer | 2165 | Go | 2026-07-31 | Distributed AI Model Training |
| kubeflow/spark-operator | 3142 | Python | 2026-07-31 | Kubernetes operator for Spark |
| plurigrid/gorj | 1 | Clojure | 2026-07-31 | forj + Rama topology nREPL + GF(3) |
| plurigrid/asi | 56 | HTML | 2026-07-10 | everything is topological chemputer! |
| plurigrid/eirobri | 0 | Clojure | 2026-07-21 | EiRoBri replay world |
| bmorphism/Gay.jl | 2 | Julia | 2026-07-31 | Wide-gamut color sampling (GF3 SPI) |
| bmorphism/gay-chat | 0 | Scheme | 2026-07-14 | gay:// chat over Spritely Brassica |
| zubyul/from-possible-worlds | 0 | TeX | 2026-07-18 | possible worlds formalism |
| wasita/wasita.github.io | 1 | Svelte | 2026-07-21 | personal site |
| migalkin/kgcourse2021 | 24 | HTML | 2026-07-10 | Knowledge Graphs course |

### High-Star Repos Across Graph

| Repo | Stars | Forks |
|------|-------|-------|
| kubeflow/kubeflow | 15798 | 2690 |
| kubeflow/spark-operator | 3142 | 1509 |
| kubeflow/pipelines | 4171 | 2070 |
| kubeflow/katib | 1695 | 532 |
| kubeflow/examples | 1461 | 755 |
| kubeflow/community-distribution | 1029 | 1070 |
| migalkin/NodePiece | 144 | 21 |
| migalkin/StarE | 89 | 16 |
| AustinCStone/TextGAN | 92 | 30 |
| bmorphism/ocaml-mcp-sdk | 61 | 2 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)

Queried 28 addresses via `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result: All 28 wallets returned 0 APT** — no `CoinStore<AptosCoin>` resource found on any address. Wallets appear unfunded or not yet initialized for APT coin storage.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B–Z | (see DB) | 0.0 each |

### Multisig Contract Probes (5 pairs)

Probed `0x1::multisig_account::num_signatures_required` on Aptos mainnet.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

**All 5 multisig contracts healthy: 2-of-2 signature requirement confirmed.**

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` responded with a Next.js SPA. No REST API endpoints for market data were found at `/api/markets` or `/api/v1/markets`. **Market data unavailable** — the frontend is client-side rendered with no accessible JSON endpoints. `mnx_snapshots` table is empty for this sweep.

---

## DuckDB Schema Summary

```
world_increments: 126 rows   (GF3 color-chained repo events)
repo_snapshots:   126 rows   (full repo metadata)
aptos_snapshots:   28 rows   (all wallets: 0 APT)
multisig_probes:    5 rows   (all healthy: 2-of-2)
mnx_snapshots:      0 rows   (SPA, no API)
```

---

## GF(3) Trit Legend

| id % 3 | Trit | Color | Name |
|--------|------|-------|------|
| 0 | 0 | `#d3869b` | ERGODIC |
| 1 | +1 | `#b8bb26` | PLUS |
| 2 | -1 | `#cc241d` | MINUS |
