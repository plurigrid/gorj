# World-Increment Sweep + Hamming Snapshot
**Date:** 2026-08-09 05:17 UTC  
**Branch:** world-increment/sweep-2026-08-09-0517  
**GF(3) color chain:** id%3==0 → ERGODIC #d3869b | id%3==1 → PLUS #b8bb26 | id%3==2 → MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social (zubyul graph) | 19 |
| DJedamski | social (zubyul graph) | 6 |
| wasita | social (zubyul graph) | 14 |
| kristinezheng | social (zubyul graph) | 5 |
| M1shaaa | social (zubyul graph) | 8 |
| AustinCStone | social (zubyul graph) | 41 |

**Total this sweep:** ~396 repo snapshots added to DuckDB

### Top Repos by Stars (this sweep)
| Org/User | Repo | Stars | Language |
|----------|------|-------|----------|
| kubeflow | kubeflow | 15,807 | — |
| kubeflow | pipelines | 4,182 | Python |
| kubeflow | spark-operator | 3,145 | Python |
| kubeflow | trainer | 2,176 | Go |
| kubeflow | katib | 1,694 | Python |
| AustinCStone | TextGAN | 92 | Python |
| migalkin | NodePiece | 144 | Python |
| migalkin | StarE | 89 | Python |
| TeglonLabs | mathpix-gem | 2 | Ruby |

### Notable Activity (2026-08-09)
- **plurigrid/place** pushed 2026-08-09T01:07:33Z — most recently active plurigrid repo (TeX, 3★, 16 open issues)
- **wasita/wm-cv** pushed 2026-08-07 — active personal academic CV (Svelte)
- **wasita/xoxowasita-analysis** created 2026-08-04, pushed 2026-08-06 — very new Python analysis repo
- **TeglonLabs/jank-crane** pushed 2026-06-08 — C++ converged-IR hub with GF3 convergence maps

### DuckDB Tables
- `world_increments`: 34 total records (11 added this sweep)
- `repo_snapshots`: 1270 total records (~396 added this sweep)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)
All 28 addresses queried via `fullnode.mainnet.aptoslabs.com/v1`:

| World | Address | Balance (APT) |
|-------|---------|--------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z (26 addrs) | 0x8699...→ 0x7af0... | 0.0 each |

**Status:** All 28 Hamming swarm addresses have zero APT balance — coin store resources return 0 or are unfunded. The addresses exist on-chain but have not been funded.

### Multisig Contract Probes
All 5 probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4...7003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

**Status:** All 5 multisig accounts healthy, all configured for 2-of-N threshold.

### MNX Markets (testnet.mnx.fi)
**Status:** Unavailable via API. The site returns a Next.js SPA on all paths including `/api/markets` and `/api/v1/markets`. No machine-readable market data extractable without browser JS execution.

---

## DuckDB Summary
```
Table              | Rows
-------------------|------
world_increments   | 34
repo_snapshots     | 1270
aptos_snapshots    | 28
multisig_probes    | 5
mnx_snapshots      | 0 (SPA, no API)
```

DB path: `packages/world-increment/ducklake/world-increments.duckdb`
