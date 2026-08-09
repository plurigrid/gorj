# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-08-09T04:xx UTC  
**GF(3) Chain:** ERGODIC #d3869b (trit=0) · PLUS #b8bb26 (trit=1) · MINUS #cc241d (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Fetched | Stars | Forks |
|---|---|---|---|---|
| plurigrid | org | 17 | 72 | 24 |
| kubeflow | org | 11 | 11,826 | 7,488 |
| TeglonLabs | org | 5 | 2 | 2 |
| bmorphism | user | 8 | 94 | 10 |
| zubyul | user | 6 | 1 | 1 |
| migalkin | social | 4 | 267 | 46 |
| DJedamski | social | 1 | 0 | 0 |
| wasita | social | 3 | 1 | 0 |
| kristinezheng | social | 1 | 0 | 0 |
| M1shaaa | social | 1 | 0 | 0 |
| AustinCStone | social | 3 | 103 | 34 |
| **TOTAL** | | **60** | **12,366** | **7,605** |

### GF(3) Distribution (world_increments)
- ERGODIC #d3869b (trit=0): 20 increments
- PLUS #b8bb26 (trit=1): 20 increments
- MINUS #cc241d (trit=-1): 20 increments

### Top Repos by Stars
| Repo | Language | Stars | Forks | Last Push |
|---|---|---|---|---|
| kubeflow/pipelines | Python | 4,182 | 2,084 | 2026-08-07 |
| kubeflow/spark-operator | Python | 3,145 | 1,512 | 2026-08-08 |
| kubeflow/trainer | Go | 2,176 | 1,017 | 2026-08-08 |
| kubeflow/community-distribution | YAML | 1,030 | 1,070 | 2026-08-04 |
| kubeflow/mpi-operator | Go | 531 | 238 | 2026-08-03 |
| kubeflow/mcp-apache-spark-history-server | Python | 188 | 67 | 2026-08-07 |
| migalkin/NodePiece | Python | 144 | 21 | 2026-05-07 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2 | 2026-05-08 |
| plurigrid/asi | HTML | 59 | 13 | 2026-07-10 |
| AustinCStone/TextGAN | Python | 92 | 30 | 2025-03-03 |

### Notable Activity
- `plurigrid/gorj` (this repo) — 1,734 open issues, last push 2026-08-09T03:15Z (active today)
- `plurigrid/eirobri` — 31 open issues, EiRoBri replay world  
- `kubeflow/pipelines` — 519 open issues; very active ML infra
- `bmorphism/Gay.jl` — 188 open issues on `gay` branch; wide-gamut GF3 color library
- `wasita/xoxowasita-analysis` — created 2026-08-04, updated 2026-08-06 (very fresh)
- `wasita/joint-planning-lit` — created 2026-08-04 (newest repo in sweep)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets: alice, bob, A–Z)

All 28 wallets queried on Aptos mainnet (fullnode.mainnet.aptoslabs.com).  
**Result:** All wallets have 0.0 APT — CoinStore resource not found (accounts may exist  
with sequence numbers but no APT deposits, or CoinStore not initialized).

Confirmed accounts exist with on-chain sequence numbers:
- `alice` (0xc793...c7b) — seq 72
- `A` (0x8699...d7a) — seq 58

All 28 balances: **0.0 APT** each.

### Multisig Contract Probes (5 pairs)

| Pair | Address | Sigs Required | Status |
|---|---|---|---|
| A-B | 0x0da4f428...987003 | 2 | ✓ healthy |
| A-G | 0xf56c4a1c...c0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ffe181...5b883 | 2 | ✓ healthy |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ healthy |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ healthy |

**All 5 multisig contracts healthy — 2-of-N signature threshold.**

### MNX Markets (testnet.mnx.fi)

Site is reachable (Next.js SPA, 58KB) but all routes return the same HTML shell  
— no REST API endpoints accessible without browser JS execution.  
**Status: unavailable** (SPA with client-side data loading only).

---

## DuckDB Ducklake Schema

```
packages/world-increment/ducklake/world-increments.duckdb
├── world_increments   — 60 rows (GF3-colored sweep events)
├── repo_snapshots     — 60 rows (11 orgs/users)
├── aptos_snapshots    — 28 rows (alice, bob, A–Z; all 0.0 APT)
├── multisig_probes    — 5 rows (all healthy, sigs_required=2)
└── mnx_snapshots      — 0 rows (SPA unavailable)
```
