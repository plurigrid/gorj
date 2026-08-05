# World Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-08-05  **Time:** 18:19 UTC

---

## JOB 1: GitHub Social Graph Sweep

### Sources
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 (total: 103) |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 (total: 106) |
| zubyul | user | 49 |
| migalkin | user (social graph) | 4 |
| DJedamski | user (social graph) | 1 |
| wasita | user (social graph) | 3 |
| kristinezheng | user (social graph) | 1 |
| M1shaaa | user (social graph) | 2 |
| AustinCStone | user (social graph) | 3 |
| **TOTAL** | | **317** |

### DuckDB Schema
- `world_increments` — 317 rows with GF(3) trit color chain
- `repo_snapshots` — 317 rows with language, stars, forks, pushed_at

### GF(3) Color Distribution
| Name | Color | Trit | Count |
|------|-------|------|-------|
| ERGODIC | #d3869b | 0 | 106 |
| PLUS | #b8bb26 | +1 | 106 |
| MINUS | #cc241d | -1 | 105 |

### Top Repos by Stars (>500)
| Org/User | Repo | Stars | Language |
|----------|------|-------|----------|
| kubeflow | kubeflow | 15,805 | — |
| kubeflow | pipelines | 4,177 | Python |
| kubeflow | spark-operator | 3,143 | Python |
| kubeflow | trainer | 2,170 | Go |
| kubeflow | katib | 1,694 | Python |
| kubeflow | examples | 1,461 | Jsonnet |
| kubeflow | community-distribution | 1,029 | YAML |
| kubeflow | arena | 816 | Go |
| kubeflow | kale | 699 | Python |
| kubeflow | mpi-operator | 530 | Go |
| migalkin | NodePiece | 144 | Python |
| plurigrid | asi | 59 | HTML |
| migalkin | StarE | 89 | Python |
| AustinCStone | TextGAN | 92 | Python |
| bmorphism | Gay.jl | 2 | Julia |
| plurigrid | ontology | 8 | JavaScript |

### Notable Recent Activity (pushed_at)
- **plurigrid/gorj** — 2026-08-05 (today) — Clojure, 1 star, 1653 open issues
- **plurigrid/place** — 2026-08-02 — TeX
- **plurigrid/eirobri** — 2026-08-04 — Clojure (EiRoBri replay world)
- **wasita/xoxowasita-analysis** — 2026-08-05 (today) — Python
- **bmorphism/Gay.jl** — 2026-08-05 (today) — Julia, 188 open issues
- **kubeflow/pipelines** — 2026-08-05 — Python, 4177 stars
- **kubeflow/sdk** — 2026-08-05 — Python

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)
**Status:** All 28 wallets return `resource_not_found` on mainnet.  
The `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource does not exist for any of these addresses at ledger version 6,628,068,031. Balance recorded as 0.0 APT for all.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...12d5 | 0.0 |
| A–Z (26 wallets) | various | 0.0 each |

### Multisig Contract Probes
All 5 contracts respond healthy with 2-of-2 signatures required.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|--------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)
**Status:** SPA (Next.js app) — API paths `/api/markets`, `/api/v1/markets`, `/api/tickers` do not return JSON; the site serves client-rendered HTML only. No market data extractable. `mnx_snapshots` table is empty (0 rows).

---

## DuckDB Summary
```
world_increments : 317 rows (GF3 color-chained)
repo_snapshots   : 317 rows (language/stars/forks/pushed_at)
aptos_snapshots  :  28 rows (all 0.0 APT, resource_not_found)
multisig_probes  :   5 rows (all 2-of-2, healthy=true)
mnx_snapshots    :   0 rows (SPA, no API)
```
