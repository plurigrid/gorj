# World Increment Sweep + Hamming Snapshot
**Date:** 2026-07-05  
**DuckDB:** `world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Coverage
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 49 |
| AustinCStone | user (social) | 30 |
| migalkin | user (social) | 19 |
| wasita | user (social) | 11 |
| M1shaaa | user (social) | 8 |
| DJedamski | user (social) | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user (social) | 5 |
| **TOTAL** | | **382** |

### Top Repos by Stars
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,763 | — | 2026-06-18 |
| kubeflow/pipelines | 4,169 | Python | 2026-07-05 |
| kubeflow/spark-operator | 3,132 | Python | 2026-07-02 |
| kubeflow/trainer | 2,129 | Go | 2026-07-03 |
| kubeflow/katib | 1,689 | Python | 2026-07-01 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1,028 | YAML | 2026-07-05 |
| kubeflow/arena | 815 | Go | 2026-07-03 |
| kubeflow/kale | 696 | Python | 2026-07-01 |
| kubeflow/mpi-operator | 529 | Go | 2026-07-03 |

### Notable Activity (most recent)
- `plurigrid/shrimp` — pushed 2026-07-03
- `plurigrid/eirobri` — Clojure, pushed 2026-06-30
- `plurigrid/asi` — HTML, 28 stars, pushed 2026-06-29
- `TeglonLabs/jank-crane` — C++ GF3 convergence maps, pushed 2026-06-08
- `wasita/wasita.github.io` — Svelte, pushed 2026-07-05 (today)
- `M1shaaa/M1shaaa` — profile config, pushed 2026-07-05 (today)
- `kristinezheng/kristinezheng.github.io` — HTML, pushed 2026-07-01

### GF(3) Color Chain Distribution
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 1 | `#b8bb26` | PLUS | 128 |
| 0 | `#d3869b` | ERGODIC | 127 |
| -1 | `#cc241d` | MINUS | 127 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
**Sweep time:** 2026-07-05T15:09 UTC  
All 28 addresses (alice, bob, A-Z) returned **0.000000 APT**.  
The CoinStore resource was not found for any address — these accounts have not yet been funded/initialized on Aptos mainnet.

| Range | Status |
|-------|--------|
| alice, bob | 0.0 APT (unfunded) |
| A-Z (26 addresses) | 0.0 APT (unfunded) |

### Multisig Contract Probes
All 5 multisig pairs are **healthy** — responding with 2-of-N signature requirement.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4f428...` | 2 | HEALTHY |
| A-G | `0xf56c4a1c...` | 2 | HEALTHY |
| Y-Z | `0xd3ffe181...` | 2 | HEALTHY |
| S-T | `0x3b1c3ae9...` | 2 | HEALTHY |
| V-W | `0x40fad7b4...` | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** - Site requires Vercel authentication (password-protected deployment). No market data extracted.

---

## DuckDB Schema
```sql
world_increments  -- GF(3)-tagged event stream (382 rows)
repo_snapshots    -- full repo metadata per increment (382 rows)
aptos_snapshots   -- hamming swarm wallet balances (28 rows)
multisig_probes   -- multisig health checks (5 rows)
mnx_snapshots     -- market data (0 rows - auth protected)
```
