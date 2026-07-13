# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-07-13  
**GF(3) color chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources scanned
| Source | Type | Repos sampled | Most recent push |
|--------|------|--------------|-----------------|
| plurigrid | org | 50 | gorj 2026-07-13 |
| kubeflow | org | 40 | sdk 2026-07-13 |
| TeglonLabs | org | 5 | jank-crane 2026-06-08 |
| bmorphism | user | 105 | anti-bullshit-mcp-server 2026-07-12 |
| zubyul | user | 49 | voice-observatory 2026-04-24 |
| migalkin | user | 19 | kgcourse2021 2026-07-10 |
| wasita | user | 11 | wasita.github.io 2026-07-06 |
| DJedamski | user | 6 | kaggle_ncaa18 (inactive) |
| kristinezheng | user | 5 | kristinezheng.github.io 2026-07-01 |
| M1shaaa | user | 8 | M1shaaa 2026-02-04 |
| AustinCStone | user | 40 | EpsteinSearch 2026-02-11 |

**Total repo snapshots stored:** 995  
**World increments:** 34 (GF(3) trit-colored)

### Notable activity
- **plurigrid/gorj** pushed 2026-07-13 — 1145 open issues (most active)
- **plurigrid/asi** pushed 2026-07-10 — topological chemputer
- **kubeflow/kubeflow** 15,772 stars, pushed 2026-07-10
- **kubeflow/spark-operator** 3,137 stars — most starred kubeflow repo in sweep
- **bmorphism/anti-bullshit-mcp-server** pushed 2026-07-12 — 22 stars
- **bmorphism/Gay.jl** 187 open issues, active development
- **migalkin/kgcourse2021** pushed 2026-07-10 — Knowledge Graphs course active

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

**Ledger version:** ~6,252,974,150

### Wallet Balances (APT)
| World | Balance (APT) | GF3 trit |
|-------|--------------|---------|
| bob | 12.65701 | PLUS #b8bb26 |
| F | 1.96052 | MINUS #cc241d |
| L | 1.92727 | PLUS #b8bb26 |
| J | 1.89509 | PLUS #b8bb26 |
| alice | 0.43643 | ERGODIC #d3869b |
| O | 0.21014 | MINUS #cc241d |
| K | 0.16196 | ERGODIC #d3869b |
| P | 0.14014 | PLUS #b8bb26 |
| M | 0.11229 | ERGODIC #d3869b |
| N | 0.10612 | MINUS #cc241d |
| Q | 0.10324 | PLUS #b8bb26 |
| R | 0.09022 | ERGODIC #d3869b |
| S | 0.09179 | PLUS #b8bb26 |
| T | 0.07371 | MINUS #cc241d |
| U | 0.05577 | MINUS #cc241d |
| A | 0.05177 | ERGODIC #d3869b |
| Y | 0.04445 | MINUS #cc241d |
| V | 0.04883 | ERGODIC #d3869b |
| X | 0.04258 | PLUS #b8bb26 |
| W | 0.04071 | PLUS #b8bb26 |
| B | 0.03626 | ERGODIC #d3869b |
| Z | 0.02427 | ERGODIC #d3869b |
| D | 0.01163 | ERGODIC #d3869b |
| C | 0.01019 | PLUS #b8bb26 |
| E | 0.00937 | MINUS #cc241d |
| H | 0.00168 | ERGODIC #d3869b |
| G | 0.00068 | PLUS #b8bb26 |
| I | 0.00068 | MINUS #cc241d |

**Total swarm APT:** ~20.17 APT  
**Top holder:** bob (12.657 APT — 62.8% of swarm)  
**Note:** Legacy CoinStore resource absent; balances queried via `0x1::coin::balance` view function (FA-compatible).

### Multisig Probes — all 5 pairs healthy
| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428...987003 | 2 | HEALTHY |
| A-G | 0xf56c4a1c...c0096 | 2 | HEALTHY |
| Y-Z | 0xd3ffe181...5b883 | 2 | HEALTHY |
| S-T | 0x3b1c3ae9...d7883 | 2 | HEALTHY |
| V-W | 0x40fad7b4...eb6d | 2 | HEALTHY |

All 5 multisig pairs require 2-of-N signatures and are responsive on mainnet.

### MNX Markets (testnet.mnx.fi)
Status: **UNAVAILABLE** — Vercel deployment protection requires visitor password. No market data extractable without authentication.

---

## DuckDB Tables Updated
- `world_increments`: 34 rows
- `repo_snapshots`: 995 rows
- `aptos_snapshots`: 28 rows
- `multisig_probes`: 5 rows
- `mnx_snapshots`: 0 rows (auth-gated)

Database: `packages/world-increment/ducklake/world-increments.duckdb`
