# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-19  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1 — GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|----------------|
| kubeflow | org | 48 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| AustinCStone | user (zubyul social graph) | 40 |
| migalkin | user (zubyul social graph) | 19 |
| M1shaaa | user (zubyul social graph) | 8 |
| DJedamski | user (zubyul social graph) | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user (zubyul social graph) | 5 |
| plurigrid | org | not captured (file collision) |
| **Total** | | **280 repos** |

> plurigrid org data was lost to a tool-result file ID collision with zubyul; wasita similarly affected. All other sources successfully captured.

### GF(3) Color Chain Distribution (280 world_increments)
| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 93 |
| +1 | PLUS | #b8bb26 | 94 |
| -1 | MINUS | #cc241d | 93 |

### Star Leaderboard (by org/user)
| Org/User | Total Stars | Repos |
|----------|-------------|-------|
| kubeflow | 34,230 | 48 |
| migalkin | 280 | 19 |
| bmorphism | 241 | 100 |
| AustinCStone | 108 | 40 |
| zubyul | 14 | 49 |
| TeglonLabs | 2 | 5 |

### Most Recently Pushed (top 10)
| Repo | Stars | Pushed At |
|------|-------|-----------|
| M1shaaa/M1shaaa | 0 | 2026-06-19T03:58:06Z |
| kubeflow/internal-acls | 19 | 2026-06-19T01:07:46Z |
| bmorphism/Gay.jl | 1 | 2026-06-19T00:48:59Z |
| kubeflow/mcp-apache-spark-history-server | 177 | 2026-06-19T00:32:53Z |
| kubeflow/pipelines | 4,154 | 2026-06-18T20:30:56Z |
| kubeflow/hub | 173 | 2026-06-18T20:25:32Z |
| kubeflow/community | 194 | 2026-06-18T20:07:55Z |
| kubeflow/website | 184 | 2026-06-18T19:52:47Z |
| kubeflow/community-distribution | 1,025 | 2026-06-18T19:10:25Z |
| kubeflow/notebooks | 73 | 2026-06-18T18:58:28Z |

Notable: `kubeflow/mcp-apache-spark-history-server` (177 stars) — a new MCP server for Apache Spark History Server, signaling kubeflow's push into AI-agent-for-infra territory.
TeglonLabs/jank-crane pushed 2026-06-08 — crane+jank converged IR hub with GF3 convergence maps, recent activity.

---

## JOB 2 — Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (28 addresses: alice, bob, A–Z)
All 28 addresses queried against `0x1::coin::CoinStore<AptosCoin>`.
**All balances: 0.0 APT** — accounts uninitialized (no CoinStore resource) or empty.

### Multisig Contract Probes (5 pairs)
All 5 probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...4987003 | 2 | healthy |
| A-G | 0xf56c4a1c...bc0096 | 2 | healthy |
| Y-Z | 0xd3ffe181...75b883 | 2 | healthy |
| S-T | 0x3b1c3ae9...ed7883 | 2 | healthy |
| V-W | 0x40fad7b4...80eb6d | 2 | healthy |

All 5 multisig contracts operational: 2-of-2 signatures required.

### MNX Markets (testnet.mnx.fi)
**UNAVAILABLE** — Vercel visitor password authentication required. No market data accessible without bypass token.

---

## DuckDB Tables
```
world_increments : 280 rows  (GF3 color chain on repo push events)
repo_snapshots   : 280 rows  (lang, stars, forks, issues, pushed_at, description)
aptos_snapshots  : 28 rows   (all 0.0 APT)
multisig_probes  : 5 rows    (all healthy, 2-of-2)
mnx_snapshots    : 0 rows    (auth required)
```
