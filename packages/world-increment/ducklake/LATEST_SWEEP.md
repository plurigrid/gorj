# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-07-06  **Time:** 04:10 UTC

## JOB 1: GitHub Social Graph Sweep

### Summary
- **Total repos captured:** 1336
- **Sources covered:** 11 orgs/users

### Repos by Source
| Source | Count |
|--------|-------|
| plurigrid | 300 |
| bmorphism | 300 |
| kubeflow | 143 |
| AustinCStone | 126 |
| TeglonLabs | 111 |
| zubyul | 97 |
| migalkin | 79 |
| wasita | 71 |
| kristinezheng | 41 |
| M1shaaa | 40 |
| DJedamski | 28 |

### Top Repos by Stars
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15764 | N/A |
| kubeflow/kubeflow | 15572 | N/A |
| kubeflow/kubeflow | 15565 | N/A |
| kubeflow/pipelines | 4169 | Python |
| kubeflow/pipelines | 4119 | Python |
| kubeflow/pipelines | 4119 | Python |
| kubeflow/spark-operator | 3132 | Python |
| kubeflow/spark-operator | 3114 | Python |
| kubeflow/spark-operator | 3111 | Python |
| kubeflow/trainer | 2129 | Go |

### GF(3) Color Chain
- `id%3==0` → trit=0, ERGODIC `#d3869b` (rose)
- `id%3==1` → trit=1, PLUS `#b8bb26` (yellow-green)
- `id%3==2` → trit=-1, MINUS `#cc241d` (red)

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances
| World | Address (short) | Balance (APT) |
|-------|-----------------|---------------|
| A | `0x8699edc0...be9d7a` | N/A |
| B | `0x3f892ebe...77cb13` | N/A |
| C | `0x38b99e63...91535e` | N/A |
| D | `0xf7765624...fcfdd1` | N/A |
| E | `0xdc1d9d53...958d36` | N/A |
| F | `0x18a14b5b...c3cf71` | N/A |
| G | `0x69a394c0...cc7f32` | N/A |
| H | `0xce67c327...e5300f` | N/A |
| I | `0x070fe5d7...0c1fc9` | N/A |
| J | `0x4d964db8...e87f54` | N/A |
| K | `0xa732040a...425dc4` | N/A |
| L | `0x7c2eaeaf...37eba9` | N/A |
| M | `0x6fed37a7...b7f2e9` | N/A |
| N | `0xe7dde6da...551b2c` | N/A |
| O | `0x73252b60...25a89d` | N/A |
| P | `0x6218792d...1ec948` | N/A |
| Q | `0xac40fa50...5c89a9` | N/A |
| R | `0x7ce605cc...d76e10` | N/A |
| S | `0xb8753014...9d0386` | N/A |
| T | `0x35781dc0...3f4588` | N/A |
| U | `0x75860da4...ef9956` | N/A |
| V | `0xb59dd817...9af2c3` | N/A |
| W | `0x5f32aef7...ccc7b0` | N/A |
| X | `0xa95cbbd1...33047d` | N/A |
| Y | `0xd8e32848...2444c4` | N/A |
| Z | `0x7af0ef6e...4e197c` | N/A |
| alice | `0xc793acde...24cc7b` | N/A |
| bob | `0x0a3c00c5...512d5d` | N/A |

**Wallets with balance:** 0
**Wallets with zero/no balance:** 28

### Multisig Contract Probes
| Pair | Address (short) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | `0x0da4f428...987003` | 2 | ✓ healthy |
| A-G | `0xf56c4a1c...bc0096` | 2 | ✓ healthy |
| S-T | `0x3b1c3ae9...ed7883` | 2 | ✓ healthy |
| V-W | `0x40fad7b4...80eb6d` | 2 | ✓ healthy |
| Y-Z | `0xd3ffe181...75b883` | 2 | ✓ healthy |

**Healthy multisigs:** 5 / 5

### MNX Markets (testnet.mnx.fi)
Status: **Unavailable** — testnet SPA returns HTML, no JSON API accessible from this environment.

---

## DuckDB Location
`packages/world-increment/ducklake/world-increments.duckdb`

### Tables
- `world_increments` — GF(3)-tagged event log
- `repo_snapshots` — GitHub repo metadata
- `aptos_snapshots` — Hamming swarm wallet balances
- `multisig_probes` — multisig contract health checks
- `mnx_snapshots` — MNX market data (unavailable this run)
