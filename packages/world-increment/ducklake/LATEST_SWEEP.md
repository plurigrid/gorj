# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-06-27  
**Run:** world-increment-sweep + hamming-swarm-snapshot agent  

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos This Run |
|--------|------|---------------|
| plurigrid | org | 10 (top by pushed) |
| kubeflow | org | 9 (top active) |
| TeglonLabs | org | 5 (all public) |
| bmorphism | user | 5 (top by stars/activity) |
| zubyul | user | 4 (top recent) |
| migalkin | social-graph | 5 (top by pushed) |
| DJedamski | social-graph | 2 |
| wasita | social-graph | 3 |
| kristinezheng | social-graph | 2 |
| M1shaaa | social-graph | 2 |
| AustinCStone | social-graph | 3 |
| **TOTAL** | | **50 new snapshots** |

### GF(3) Color Chain Summary (This Run)
- **ERGODIC** (#d3869b, trit=0): 23 increments (id%3==0)
- **PLUS** (#b8bb26, trit=1): 25 increments (id%3==1)
- **MINUS** (#cc241d, trit=-1): 25 increments (id%3==2)

### Notable Active Repos
| Repo | Stars | Issues | Last Push |
|------|-------|--------|-----------|
| kubeflow/kubeflow | 15,746 | 0 | 2026-06-18 |
| kubeflow/pipelines | 4,156 | 451 | 2026-06-26 |
| kubeflow/spark-operator | 3,128 | 101 | 2026-06-26 |
| kubeflow/trainer | 2,123 | 128 | 2026-06-26 |
| migalkin/NodePiece | 144 | 0 | 2026-05-07 |
| bmorphism/ocaml-mcp-sdk | 61 | 0 | 2026-03-16 |
| plurigrid/gorj | 0 | 851 | 2026-06-27 |
| plurigrid/asi | 26 | 4 | 2026-06-26 |
| bmorphism/Gay.jl | 2 | 187 | 2026-06-27 |

### DuckDB Ducklake State
- **DB path:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Total world_increments** (all runs): 73
- **Total repo_snapshots** (all runs): 994
- **Cumulative orgs/users tracked:** plurigrid (210), bmorphism (205), TeglonLabs (111), kubeflow (103), AustinCStone (89), migalkin (65), wasita (63), zubyul (52), kristinezheng (38), M1shaaa (34), DJedamski (24)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)
All 28 addresses (alice, bob, A-Z) queried via Aptos mainnet fullnode.  
**Result: All wallets returned 0.0 APT** — no CoinStore resources found on mainnet.  
These appear to be freshly-generated or unfunded addresses.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...e9d7 | 0.0 |
| B-Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes (5 contracts)
All 5 contracts probed via `0x1::multisig_account::num_signatures_required`. All **healthy** (2-of-N).

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | yes |
| A-G | 0xf56c...0096 | 2 | yes |
| Y-Z | 0xd3ff...b883 | 2 | yes |
| S-T | 0x3b1c...7883 | 2 | yes |
| V-W | 0x40fa...eb6d | 2 | yes |

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — returns Vercel authentication wall.  
All API paths probed (`/api/markets`, `/api/v1/markets`, `/api/tickers`) are behind Vercel deployment protection. No market data extractable without bypass token.

---

## Summary
- **50 GitHub repo snapshots** added with GF(3) color chain (23 ERGODIC, 25 PLUS, 25 MINUS)
- **28 Aptos wallets** queried: all show 0.0 APT (unfunded/uninitialized on mainnet)
- **5 multisig contracts** probed: all healthy at 2-of-N threshold
- **MNX testnet** inaccessible (Vercel auth required)
- DuckDB ducklake at `packages/world-increment/ducklake/world-increments.duckdb` updated
