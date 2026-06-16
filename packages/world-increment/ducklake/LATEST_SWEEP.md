# World-Increment Sweep + Hamming Snapshot
**Date:** 2026-06-16  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social-graph | 19 |
| DJedamski | social-graph | 6 |
| wasita | social-graph | 11 |
| kristinezheng | social-graph | 5 |
| M1shaaa | social-graph | 8 |
| AustinCStone | social-graph | 40 |
| **TOTAL** | | **315** |

### GF(3) Color Chain
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 105 |
| 1 | `#b8bb26` | PLUS | 105 |
| -1 | `#cc241d` | MINUS | 105 |

### Top Repos by Stars
| Org/User | Repo | Stars | Language |
|----------|------|-------|----------|
| kubeflow | kubeflow | 15,725 | — |
| kubeflow | pipelines | 4,154 | Python |
| kubeflow | spark-operator | 3,127 | Python |
| kubeflow | trainer | 2,115 | Go |
| kubeflow | katib | 1,683 | Python |
| migalkin | NodePiece | 144 | Python |
| AustinCStone | TextGAN | 92 | Python |
| migalkin | StarE | 89 | Python |
| bmorphism | Gay.jl | 187 | Julia |
| plurigrid | gorj | 619 open issues | — |

### Notable Activity
- **TeglonLabs/jank-crane** pushed 2026-06-08: crane-jank converged-IR hub with GF3 convergence maps
- **wasita/wasita.github.io** pushed 2026-06-15 (most recent in sweep)
- **kristinezheng/kristinezheng.github.io** pushed 2026-06-07
- **bmorphism/ocaml-mcp-sdk**: 61 stars — MCP SDK for OCaml

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses probed)
**API:** `fullnode.mainnet.aptoslabs.com/v1`  
**Ledger version:** 5,766,344,585

All 28 wallets (alice, bob, A-Z) returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. All addresses are uninitialised — no APT CoinStore registered. Balance recorded as NULL.

| World | Balance APT |
|-------|-------------|
| alice | NULL |
| bob | NULL |
| A through Z (26) | NULL |

### Multisig Contract Probes (5 contracts)
Probed via `0x1::multisig_account::num_signatures_required` — all healthy, all require 2 signatures.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | YES |
| A-G | 0xf56c...0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — Vercel deployment authentication required. All API paths return auth gate. No market data extractable without bypass token.

---

## DuckDB Schema Summary
| Table | Rows |
|-------|------|
| world_increments | 315 |
| repo_snapshots | 315 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |
