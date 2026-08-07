# World Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-08-07  
**DuckDB:** `world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Coverage
| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 20 |
| kubeflow | org | 12 |
| TeglonLabs | org | 5 |
| bmorphism | user | 13 |
| zubyul | user | 6 |
| migalkin | social | 4 |
| DJedamski | social | 2 |
| wasita | social | 5 |
| kristinezheng | social | 2 |
| AustinCStone | social | 4 |
| M1shaaa | social | 2 |
| **Total** | | **75** |

### Notable Activity (2026-08-07)
- **plurigrid/gorj** — forj + Rama topology nREPL routing + GF(3) coloring (1,685 open issues)
- **kubeflow/pipelines** — pushed 2026-08-07, 4,179 stars
- **kubeflow/mcp-apache-spark-history-server** — MCP for Spark History Server, active
- **bmorphism/anti-bullshit-mcp-server** — pushed 2026-08-02, 23 stars
- **wasita/xoxowasita-analysis** — pushed 2026-08-06 (newest in social graph)
- **wasita/joint-planning-lit** — pushed 2026-08-04

### Top Repos by Stars
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,805 | — |
| kubeflow/pipelines | 4,179 | Python |
| kubeflow/spark-operator | 3,144 | Python |
| kubeflow/trainer | 2,172 | Go |
| kubeflow/katib | 1,694 | Python |
| kubeflow/examples | 1,461 | Jsonnet |
| kubeflow/community-distribution | 1,029 | YAML |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/NodePiece | 144 | Python |
| plurigrid/asi | 59 | HTML |

### GF(3) Color Chain Distribution
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 25 |
| 1 | #b8bb26 | PLUS | 25 |
| -1 | #cc241d | MINUS | 25 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-08-07)
*Note: Balances via `0x1::coin::balance` view function (legacy APT CoinStore resource not initialized on most wallets)*

| World | APT Balance |
|-------|-------------|
| alice | 0.436434 |
| bob | **12.657007** |
| A | 0.051767 |
| B | 0.036256 |
| C | 0.010185 |
| D | 0.011629 |
| E | 0.009372 |
| F | **1.960516** |
| G | 0.000681 |
| H | 0.001681 |
| I | 0.000681 |
| J | **1.895093** |
| K | 0.161961 |
| L | **1.927269** |
| M | 0.112285 |
| N | 0.106121 |
| O | 0.210136 |
| P | 0.140136 |
| Q | 0.103240 |
| R | 0.090217 |
| S | 0.091788 |
| T | 0.073713 |
| U | 0.055773 |
| V | 0.048833 |
| W | 0.040705 |
| X | 0.042577 |
| Y | 0.044449 |
| Z | 0.024268 |
| **TOTAL** | **20.344773 APT** |

**Richest:** bob (12.66 APT), F (1.96), L (1.93), J (1.90)  
**Dust wallets (< 0.01 APT):** E, G, H, I

### Multisig Contract Probes (Aptos Mainnet)
All 5 multisig contracts healthy — **2 signatures required** each.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...4987003 | 2 | ✓ healthy |
| A-G | 0xf56c4a1c...fbc0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ffe181...e75b883 | 2 | ✓ healthy |
| S-T | 0x3b1c3ae9...ded7883 | 2 | ✓ healthy |
| V-W | 0x40fad7b4...80eb6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)
**Status: SPA — API data unavailable via static fetch.**  
`testnet.mnx.fi` is a Next.js SPA (dpl_4rqXCY7GNz88uxzdkWQfJwa1ExiY). No REST API endpoint exposed at `/api/markets`, `/api/v1/markets`. Market data requires JS execution. No rows inserted into `mnx_snapshots`.

---

## DuckDB Tables Summary
```
world_increments:  75 rows  (GF3 color-chained repo events)
repo_snapshots:    75 rows  (org/user repos snapshotted)
aptos_snapshots:   28 rows  (Hamming swarm wallet balances)
multisig_probes:    5 rows  (all healthy, 2-of-N threshold)
mnx_snapshots:      0 rows  (SPA, no API access)
```

## Branch
`world-increment/sweep-2026-08-07`
