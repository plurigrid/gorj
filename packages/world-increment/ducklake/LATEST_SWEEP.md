# World Increment Sweep + Hamming Snapshot
**Date:** 2026-08-06  
**Run type:** Scheduled autonomous sweep

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Total Repos | Sampled |
|--------|------|-------------|---------|
| plurigrid | org | 103 | 12 |
| kubeflow | org | 49 | 8 |
| TeglonLabs | org | 5 | 5 |
| bmorphism | user | 106 | 7 |
| zubyul | user | 49 | 5 |
| migalkin (social) | user | 19 | 3 |
| DJedamski (social) | user | 6 | 1 |
| wasita (social) | user | 14 | 3 |
| kristinezheng (social) | user | 5 | 1 |
| M1shaaa (social) | user | 8 | 1 |
| AustinCStone (social) | user | 41 | 3 |

### Most Recently Pushed (top 10)
| Repo | Pushed At | Stars |
|------|-----------|-------|
| wasita/xoxowasita-analysis | 2026-08-06 | 0 |
| plurigrid/gorj | 2026-08-06 | 1 |
| kubeflow/sdk | 2026-08-06 | 133 |
| kubeflow/trainer | 2026-08-06 | 2171 |
| bmorphism/Gay.jl | 2026-08-06 | 2 |
| kubeflow/pipelines | 2026-08-05 | 4178 |
| kubeflow/spark-operator | 2026-08-05 | 3144 |
| kubeflow/katib | 2026-08-05 | 1694 |
| plurigrid/eirobri | 2026-08-04 | 0 |
| plurigrid/place | 2026-08-02 | 1 |

### GF(3) Color Chain Distribution
| Color | Name | Trit | Count |
|-------|------|------|-------|
| #d3869b | ERGODIC | 0 | 16 |
| #b8bb26 | PLUS | 1 | 17 |
| #cc241d | MINUS | -1 | 16 |

**Total world_increments:** 49  
**Total repo_snapshots:** 49  

### Notable Repos
- `plurigrid/gorj` — forj + Rama topology nREPL routing + GF(3) gay trit coloring (1,676 open issues, active today)
- `kubeflow/kubeflow` — 15,805 stars, flagship ML-on-K8s toolkit
- `bmorphism/Gay.jl` — 188 open issues, wide-gamut color sampling with splittable determinism
- `TeglonLabs/jank-crane` — C++ crane-jank converged-IR hub with GF3 convergence maps
- `migalkin/NodePiece` — 144 stars, compositional KG representations (ICLR'22)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
All 28 addresses (alice, bob, A–Z) queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result: All wallets show 0.0 APT**

CoinStore resource not initialized or zero balance for all addresses. Addresses are valid on-chain but hold no APT in the coin store.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I–Z | (18 addresses) | 0.0 each |

### Multisig Contract Probes
All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✅ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✅ HEALTHY |

**All multisig contracts respond with 2-of-N threshold. All healthy.**

### MNX Markets (testnet.mnx.fi)
Status: **SPA-only, no public API available**  
The site is a Next.js single-page application. Direct API probes to `/api/markets`, `/api/v1/markets`, and `/api/tickers` returned the full SPA HTML rather than JSON market data. No structured market data extractable without a headless browser session.

---

## DuckDB Schema Summary
Database: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 49 |
| repo_snapshots | 49 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA unavailable) |
