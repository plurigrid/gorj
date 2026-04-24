# LATEST_SWEEP — World Increment + Hamming Snapshot

**Timestamp:** 2026-04-24 06:22 UTC  
**GF(3) Color:** #1 → trit=1, PLUS `#b8bb26`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 5 |
| migalkin | social-graph | 4 |
| DJedamski | social-graph | 2 |
| wasita | social-graph | 3 |
| kristinezheng | social-graph | 2 |
| M1shaaa | social-graph | 2 |
| AustinCStone | social-graph | 3 |
| **TOTAL** | | **272** |

### Top Repos by Stars

| Repo | Lang | ★ | Pushed |
|------|------|---|--------|
| `kubeflow/kubeflow` | - | 15598 | 2026-01-05 |
| `kubeflow/pipelines` | Python | 4125 | 2026-04-23 |
| `kubeflow/spark-operator` | Python | 3118 | 2026-04-21 |
| `kubeflow/trainer` | Go | 2090 | 2026-04-23 |
| `kubeflow/katib` | Python | 1679 | 2026-04-14 |
| `kubeflow/examples` | Jsonnet | 1460 | 2025-04-14 |
| `kubeflow/manifests` | YAML | 1012 | 2026-04-11 |
| `kubeflow/arena` | Go | 810 | 2026-04-16 |
| `kubeflow/kale` | Python | 685 | 2026-04-22 |
| `kubeflow/mpi-operator` | Go | 524 | 2026-04-14 |
| `kubeflow/fairing` | Jsonnet | 337 | 2022-04-11 |
| `kubeflow/pytorch-operator` | Jsonnet | 309 | 2021-12-01 |
| `kubeflow/community` | Jsonnet | 195 | 2026-04-08 |
| `kubeflow/website` | HTML | 184 | 2026-04-20 |
| `kubeflow/kfp-tekton` | TypeScript | 182 | 2024-11-19 |

### Top Languages

| Language | Repos |
|----------|-------|
| Python | 46 |
| Rust | 22 |
| TypeScript | 21 |
| Go | 15 |
| JavaScript | 15 |
| Clojure | 12 |
| HTML | 10 |
| Julia | 9 |
| Jupyter Notebook | 9 |
| Jsonnet | 8 |

### Recently Active (plurigrid, pushed within 7d)

| Repo | Language |
|------|----------|
| `plurigrid/gorj` | Clojure |
| `plurigrid/asi` | HTML |
| `plurigrid/nanoclj-zig` | Zig |
| `plurigrid/zig-syrup` | Zig |
| `plurigrid/spi-race` | Swift |
| `plurigrid/bci-blue-share` | HTML |
| `plurigrid/horse` | TeX |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

**Timestamp:** 2026-04-24 06:22 UTC  
**Addresses probed:** 28  
**Successful reads:** 19  
**DNS errors:** 9  
**Zero balances:** 19  
**Non-zero balances:** 0

### Balance Summary (APT)

| World | Balance (APT) | Status |
|-------|---------------|--------|
| A | 0.000000 | empty |
| B | — | DNS error |
| C | — | DNS error |
| D | — | DNS error |
| E | — | DNS error |
| F | 0.000000 | empty |
| G | — | DNS error |
| H | 0.000000 | empty |
| I | — | DNS error |
| J | — | DNS error |
| K | 0.000000 | empty |
| L | 0.000000 | empty |
| M | 0.000000 | empty |
| N | 0.000000 | empty |
| O | 0.000000 | empty |
| P | 0.000000 | empty |
| Q | 0.000000 | empty |
| R | 0.000000 | empty |
| S | 0.000000 | empty |
| T | 0.000000 | empty |
| U | 0.000000 | empty |
| V | 0.000000 | empty |
| W | 0.000000 | empty |
| X | 0.000000 | empty |
| Y | 0.000000 | empty |
| Z | 0.000000 | empty |
| alice | — | DNS error |
| bob | — | DNS error |

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428a0c007da0f...` | 2 | ✓ |
| A-G | `0xf56c4a1c0906214f3f...` | 2 | ✓ |
| S-T | `0x3b1c3ae905d44c3a49...` | 2 | ✓ |
| V-W | `0x40fad7b423a843650f...` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b2df40622...` | 2 | ✓ |

**All 5 multisig contracts report 2-of-2 threshold — swarm is healthy.**

### MNX Markets

**Status:** DNS-unavailable (`testnet.mnx.fi` — DNS cache overflow)  
No market data could be extracted. Placeholder recorded in `mnx_snapshots`.

---

## DuckDB Ducklake

**Path:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Purpose |
|-------|---------|
| `world_increments` | GF(3) color-coded sweep events |
| `repo_snapshots` | GitHub repo metadata per sweep |
| `aptos_snapshots` | Hamming swarm wallet balances |
| `multisig_probes` | Multisig contract health |
| `mnx_snapshots` | MNX market data (currently unavailable) |

**GF(3) chain:** `id%3==0` → trit=0 ERGODIC `#d3869b` · `id%3==1` → trit=1 PLUS `#b8bb26` · `id%3==2` → trit=-1 MINUS `#cc241d`
