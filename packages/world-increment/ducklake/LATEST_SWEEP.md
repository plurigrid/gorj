# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-06-25  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Coverage
| Source | Type | Repos Snapshotted | Total Stars |
|--------|------|-------------------|-------------|
| plurigrid | org | 100 | 157 |
| kubeflow | org | 48 | 101,978 |
| TeglonLabs | org | 5 | 14 |
| bmorphism | user | 100 | 509 |
| zubyul | user | 49 | 40 |
| migalkin | user (social) | 19 | 834 |
| wasita | user (social) | 11 | 11 |
| kristinezheng | user (social) | 5 | 0 |
| M1shaaa | user (social) | 8 | 0 |
| DJedamski | user (social) | 6 | 17 |
| AustinCStone | user (social) | 40 | 324 |
| **TOTAL** | | **391 new / 1335 cumulative** | **103,884** |

### Top Repos by Stars
| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,743 | 2026-06-18 |
| kubeflow/pipelines | Python | 4,157 | 2026-06-24 |
| kubeflow/spark-operator | Python | 3,128 | 2026-06-24 |
| kubeflow/trainer | Go | 2,121 | 2026-06-24 |
| kubeflow/katib | Python | 1,685 | 2026-06-23 |
| migalkin/* | various | ~834 total | — |
| bmorphism/* | various | ~509 total | — |

### Notable New Repos
- **TeglonLabs/jank-crane** (C++, 2026-06-08) — crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps
- **TeglonLabs/mathpix-gem** (Ruby, 2 stars) — MathOCR gem: LaTeX/SMILES/markdown
- **wasita/proj-template** — pushed 2026-06-19, most recent in social graph
- **M1shaaa/M1shaaa** — profile config, pushed 2026-06-25 (today)
- **kubeflow/pipelines** — very active (pushed 2026-06-24), Python ML pipeline platform

### GF(3) Color Chain Distribution
| Name | Color | Count | % |
|------|-------|-------|---|
| ERGODIC | #d3869b (trit=0) | 137 | 33.1% |
| PLUS | #b8bb26 (trit=1) | 139 | 33.6% |
| MINUS | #cc241d (trit=-1) | 138 | 33.3% |

Near-perfect GF(3) equipartition across 414 increments.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
**All 28 addresses (alice, bob, A–Z) returned 0.000000 APT.**

Root cause: none of the addresses have a `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource registered on mainnet Aptos (HTTP 404 = no coin store). The accounts are either unfunded or use a different resource type.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.000000 |
| bob | 0x0a3c...512d | 0.000000 |
| A | 0x8699...9d7a | 0.000000 |
| B | 0x3f89...b13 | 0.000000 |
| C | 0x38b9...35e | 0.000000 |
| D | 0xf776...dd1 | 0.000000 |
| E | 0xdc1d...d36 | 0.000000 |
| F | 0x18a1...f71 | 0.000000 |
| G | 0x69a3...f32 | 0.000000 |
| H | 0xce67...00f | 0.000000 |
| I | 0x070f...c9 | 0.000000 |
| J | 0x4d96...f54 | 0.000000 |
| K | 0xa732...dc4 | 0.000000 |
| L | 0x7c2e...ba9 | 0.000000 |
| M | 0x6fed...2e9 | 0.000000 |
| N | 0xe7dd...b2c | 0.000000 |
| O | 0x7325...89d | 0.000000 |
| P | 0x6218...948 | 0.000000 |
| Q | 0xac40...89a9 | 0.000000 |
| R | 0x7ce6...e10 | 0.000000 |
| S | 0xb875...386 | 0.000000 |
| T | 0x3578...588 | 0.000000 |
| U | 0x7586...956 | 0.000000 |
| V | 0xb59d...b3 | 0.000000 |
| W | 0x5f32...b0 | 0.000000 |
| X | 0xa95c...47d | 0.000000 |
| Y | 0xd8e3...4c4 | 0.000000 |
| Z | 0x7af0...97c | 0.000000 |

### Multisig Contract Probes
All 5 contracts responded successfully with `num_signatures_required = 2`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | healthy |
| A-G | 0xf56c...096 | 2 | healthy |
| Y-Z | 0xd3ff...883 | 2 | healthy |
| S-T | 0x3b1c...883 | 2 | healthy |
| V-W | 0x40fa...b6d | 2 | healthy |

All multisig contracts are healthy 2-of-2 threshold schemas.

### MNX Markets
`testnet.mnx.fi` API endpoints returned HTTP 401 Unauthorized — auth token required for market data. No data available this sweep.

---

## DuckDB Tables Summary
| Table | Row Count |
|-------|-----------|
| world_increments | 414 |
| repo_snapshots | 1,335 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (placeholder) |
