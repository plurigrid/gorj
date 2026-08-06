# World-Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-08-06  
**GF(3) color chain:** ERGODIC (#d3869b, trit=0) · PLUS (#b8bb26, trit=1) · MINUS (#cc241d, trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Sources queried

| Source | Type | Repos snapped | Total stars |
|--------|------|--------------|-------------|
| kubeflow | org | 30 | 33,203 |
| bmorphism | user | 100 | 247 |
| plurigrid | org | 100 | 112 |
| migalkin | social | 6 | 278 |
| zubyul | user | 49 | 14 |
| AustinCStone | social | 4 | 103 |
| wasita | social | 4 | 4 |
| TeglonLabs | org | 5 | 2 |
| DJedamski | social | 3 | 2 |
| kristinezheng | social | 2 | 0 |
| M1shaaa | social | 2 | 0 |
| **Total** | | **305** | **33,965** |

### GF(3) distribution (world_increments)

| Name | Color | Trit | Count |
|------|-------|------|-------|
| ERGODIC | #d3869b | 0 | 108 |
| PLUS | #b8bb26 | 1 | 110 |
| MINUS | #cc241d | -1 | 110 |

### Top repos by stars (this sweep)

| Repo | Stars | Language | Last push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,805 | — | 2026-07-10 |
| kubeflow/pipelines | 4,178 | Python | 2026-08-05 |
| kubeflow/spark-operator | 3,144 | Python | 2026-08-05 |
| kubeflow/trainer | 2,171 | Go | 2026-08-05 |
| kubeflow/katib | 1,694 | Python | 2026-08-05 |
| kubeflow/community-distribution | 1,029 | YAML | 2026-08-04 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| wasita/xoxowasita-analysis | 0 | Python | 2026-08-05 ← most recent |

### Notable recent activity
- **wasita/xoxowasita-analysis** — pushed 2026-08-05 (yesterday), new Python analysis repo
- **kubeflow/pipelines** — active push 2026-08-05
- **TeglonLabs/jank-crane** — C++, crane-jank converged-IR hub with GF3 convergence maps, pushed 2026-06-08

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet balances

All 28 Hamming-swarm wallets returned **0.0 APT** via the `0x1::coin::CoinStore` resource. This is consistent with wallets that either:
- have not yet been funded on mainnet, or
- hold only FA (Fungible Asset) balances outside the legacy CoinStore interface.

| World | Address (truncated) | APT |
|-------|-------------------|-----|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…512d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig contract probes

All 5 probed multisig contracts are **healthy** (2-of-2 required):

| Pair | Address (truncated) | Sigs Required | Status |
|------|-------------------|---------------|--------|
| A-B | 0x0da4…7003 | 2 | ✓ healthy |
| A-G | 0xf56c…0096 | 2 | ✓ healthy |
| S-T | 0x3b1c…7883 | 2 | ✓ healthy |
| V-W | 0x40fa…eb6d | 2 | ✓ healthy |
| Y-Z | 0xd3ff…b883 | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

**Status: unavailable via REST API.** The site is a Next.js SPA; no machine-readable `/api/markets` or `/api/v1/markets` endpoint is accessible — both paths return the HTML shell. Market data is loaded client-side via JavaScript bundles. Recorded as `category=unavailable-SPA` in `mnx_snapshots`.

---

## DuckDB Ducklake

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows (cumulative) |
|-------|-------------------|
| world_increments | 328 |
| repo_snapshots | 1,249 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |
