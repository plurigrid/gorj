# World-Increment Sweep + Hamming Snapshot
**Date:** 2026-04-21  
**DuckDB:** `world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 47 |
| migalkin | social graph | 19 |
| DJedamski | social graph | 6 |
| wasita | social graph | 10 |
| kristinezheng | social graph | 6 |
| M1shaaa | social graph | 8 |
| AustinCStone | social graph | 40 |
| **Total** | | **387** |

### GF(3) Color Chain Distribution
| GF3 Name | Color | Trit | Count |
|----------|-------|------|-------|
| ERGODIC | `#d3869b` | 0 | 129 |
| PLUS | `#b8bb26` | +1 | 129 |
| MINUS | `#cc241d` | -1 | 129 |

### Top Languages Across Social Graph
| Language | Repos |
|----------|-------|
| Python | 79 |
| Rust | 26 |
| JavaScript | 23 |
| TypeScript | 23 |
| HTML | 16 |
| Go | 15 |
| Jupyter Notebook | 14 |
| Clojure | 13 |
| Julia | 9 |
| Jsonnet | 8 |

### Top Starred Repos
| Repo | Language | Stars |
|------|----------|-------|
| kubeflow/kubeflow | — | 15,587 |
| kubeflow/pipelines | Python | 4,125 |
| kubeflow/spark-operator | Python | 3,117 |
| kubeflow/trainer | Go | 2,085 |
| kubeflow/katib | Python | 1,680 |

### Notable Recent Activity
- **wasita/wasita.github.io** (Svelte) — pushed 2026-04-13
- **M1shaaa/M1shaaa** — pushed 2026-04-21 (today)
- **kristinezheng/kristinezheng.github.io** — pushed 2026-04-09
- **TeglonLabs/mathpix-gem** (Ruby) — pushed 2026-01-01, 2 stars

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)
All 28 Hamming-swarm wallets (alice, bob, A-Z) queried against Aptos mainnet.
All returned **0 APT** from `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` —
wallets may hold assets in other modules or have zero APT balance at sweep time.

### Multisig Contract Probes
All 5 multisig contracts responded healthy with **2 signatures required**:

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...87003 | 2 | OK |
| A-G | 0xf56c4a1c...0096 | 2 | OK |
| Y-Z | 0xd3ffe181...b883 | 2 | OK |
| S-T | 0x3b1c3ae9...7883 | 2 | OK |
| V-W | 0x40fad7b4...eb6d | 2 | OK |

### MNX Markets (testnet.mnx.fi)
API endpoint /api/markets returned HTTP 404 (Next.js SPA, no public REST API exposed).
Market data **unavailable** at sweep time — recorded as 0 rows in mnx_snapshots.

---

## DuckDB Table Summary

| Table | Rows |
|-------|------|
| world_increments | 387 |
| repo_snapshots | 387 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |
