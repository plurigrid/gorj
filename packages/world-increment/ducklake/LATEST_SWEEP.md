# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-06-11  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1 — GitHub Social Graph Sweep

### Sources Crawled
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social-graph | 5 |
| DJedamski | social-graph | 3 |
| wasita | social-graph | 4 |
| kristinezheng | social-graph | 3 |
| M1shaaa | social-graph | 3 |
| AustinCStone | social-graph | 5 |
| **Total** | | **325** |

### GF(3) Color Distribution
- trit=0 ERGODIC `#d3869b` — 108 repos
- trit=1 PLUS `#b8bb26` — 109 repos
- trit=-1 MINUS `#cc241d` — 108 repos

### Top Starred Repos
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,712 | — |
| kubeflow/pipelines | 4,152 | Python |
| kubeflow/spark-operator | 3,126 | Python |
| kubeflow/trainer | 2,111 | Go |
| kubeflow/katib | 1,683 | Python |
| kubeflow/examples | 1,462 | Jsonnet |
| kubeflow/manifests | 1,022 | YAML |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/NodePiece | 144 | Python |
| migalkin/StarE | 89 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| plurigrid/asi | 25 | HTML |

### Notable Recent Activity (pushed within 7 days of 2026-06-11)
- `plurigrid/gorj` — 2026-06-11 — 497 open issues — Clojure
- `plurigrid/place` — 2026-06-10 — TeX
- `plurigrid/asi` — 2026-06-10 — HTML (25 stars)
- `kubeflow/hub` — 2026-06-11 — Go (model registry)
- `kubeflow/pipelines` — 2026-06-11 — Python (4152 stars)
- `TeglonLabs/jank-crane` — 2026-06-08 — C++ (GF3 convergence maps)
- `wasita/wasita.github.io` — 2026-06-01 — Svelte
- `kristinezheng/kristinezheng.github.io` — 2026-06-07 — HTML

---

## JOB 2 — Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (28 addresses, 2026-06-11)
| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| bob | 0x0a3c00c5… | 12.657007 |
| F | 0x18a14b5b… | 1.960516 |
| L | 0x7c2eaeaf… | 1.927269 |
| J | 0x4d964db8… | 1.895093 |
| alice | 0xc793acde… | 0.436434 |
| O | 0x73252b60… | 0.210136 |
| K | 0xa732040a… | 0.161961 |
| P | 0x62187924… | 0.140136 |
| M | 0x6fed37a7… | 0.112285 |
| N | 0xe7dde6da… | 0.106121 |
| Q | 0xac40fa50… | 0.103240 |
| S | 0xb8753014… | 0.091788 |
| R | 0x7ce605cc… | 0.090217 |
| T | 0x35781dc0… | 0.073713 |
| U | 0x75860da4… | 0.055773 |
| A | 0x8699edc0… | 0.051767 |
| V | 0xb59dd817… | 0.048833 |
| Y | 0xd8e32848… | 0.044449 |
| X | 0xa95cbbd1… | 0.042577 |
| W | 0x5f32aef7… | 0.040705 |
| B | 0x3f892ebe… | 0.036256 |
| Z | 0x7af0ef6e… | 0.024268 |
| D | 0xf7765624… | 0.011629 |
| C | 0x38b99e63… | 0.010185 |
| E | 0xdc1d9d53… | 0.009372 |
| H | 0xce67c327… | 0.001681 |
| G | 0x69a394c0… | 0.000681 |
| I | 0x070fe5d7… | 0.000681 |

**Total swarm APT:** ~22.22 APT  
**Method:** `0x1::coin::balance` view function (legacy CoinStore resource absent)

### Multisig Contract Probes (5 pairs)
| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428… | 2-of-2 | healthy |
| A-G | 0xf56c4a1c… | 2-of-2 | healthy |
| Y-Z | 0xd3ffe181… | 2-of-2 | healthy |
| S-T | 0x3b1c3ae9… | 2-of-2 | healthy |
| V-W | 0x40fad7b4… | 2-of-2 | healthy |

All 5 multisig contracts respond at tip, each requiring 2-of-2 signatures. Hamming swarm topology intact.

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — `/api/markets` and `/api/v1/markets` both returned no response. SPA requires browser rendering; no machine-readable market data extractable at this time.

---

## DuckDB Schema
```
packages/world-increment/ducklake/world-increments.duckdb
  world_increments  325 rows  -- GF(3)-tagged increment events
  repo_snapshots    325 rows  -- GitHub repo metadata
  aptos_snapshots    28 rows  -- Hamming swarm wallet balances
  multisig_probes     5 rows  -- 2-of-2 multisig health checks
  mnx_snapshots       0 rows  -- MNX markets (unavailable)
```
