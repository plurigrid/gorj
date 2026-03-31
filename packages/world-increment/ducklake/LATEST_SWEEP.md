# World-Increment Sweep + Hamming Swarm Snapshot

**Date/Time:** 2026-03-31 (UTC)
**DuckDB:** `/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb`

---

## GitHub Repos Summary

**Total repos captured:** 468 across 11 sources

| Source | Type | Repo Count |
|---|---|---|
| bmorphism | user | 100 |
| plurigrid | org | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 46 |
| AustinCStone | user (zubyul social) | 43 |
| migalkin | user (zubyul social) | 30 |
| wasita | user (zubyul social) | 28 |
| zubyul | user | 23 |
| kristinezheng | user (zubyul social) | 18 |
| M1shaaa | user (zubyul social) | 16 |
| DJedamski | user (zubyul social) | 11 |

### Top 20 Repos by Stars

| Repo | Stars | Language |
|---|---|---|
| kubeflow/kubeflow | 15547 | — |
| kubeflow/pipelines | 4114 | Python |
| kubeflow/spark-operator | 3110 | Python |
| kubeflow/trainer | 2070 | Go |
| kubeflow/katib | 1673 | Python |
| kubeflow/examples | 1459 | Jsonnet |
| kubeflow/manifests | 1006 | YAML |
| kubeflow/arena | 810 | Go |
| kubeflow/kale | 681 | Python |
| kubeflow/mpi-operator | 519 | Go |
| kubeflow/fairing | 337 | Jsonnet |
| kubeflow/pytorch-operator | 309 | Jsonnet |
| kubeflow/community | 191 | Jsonnet |
| kubeflow/website | 183 | HTML |
| kubeflow/kfctl | 183 | Go |
| kubeflow/kfp-tekton | 182 | TypeScript |
| kubeflow/example-seldon | 172 | Jupyter Notebook |
| kubeflow/model-registry | 170 | Go |
| kubeflow/mcp-apache-spark-history-server | 147 | Python |
| migalkin/NodePiece | 143 | Python |

Also captured: 30 public events each for bmorphism and zubyul.

---

## Aptos Wallet Balances

All 28 wallets queried via Aptos mainnet fullnode. All show 0.0 APT (accounts not found or no APT balance on mainnet).

| Label | Address (truncated) | Balance (APT) |
|---|---|---|
| alice | 0xc793acde...d624cc7b | 0.0 |
| bob | 0x0a3c00c5...05512d5d | 0.0 |
| A | 0x8699edc0...ebe9d7a | 0.0 |
| B | 0x3f892ebe...4577cb13 | 0.0 |
| C | 0x38b99e63...691535e | 0.0 |
| D | 0xf7765624...9fcfdd1 | 0.0 |
| E | 0xdc1d9d53...0958d36 | 0.0 |
| F | 0x18a14b5b...4c3cf71 | 0.0 |
| G | 0x69a394c0...dbcc7f32 | 0.0 |
| H | 0xce67c327...d94e5300f | 0.0 |
| I | 0x070fe5d7...fc00c1fc9 | 0.0 |
| J | 0x4d964db8...3e87f54 | 0.0 |
| K | 0xa732040a...7a425dc4 | 0.0 |
| L | 0x7c2eaeaf...6337eba9 | 0.0 |
| M | 0x6fed37a7...4b7f2e9 | 0.0 |
| N | 0xe7dde6da...11551b2c | 0.0 |
| O | 0x73252b60...525a89d | 0.0 |
| P | 0x6218792d...621ec948 | 0.0 |
| Q | 0xac40fa50...5e5c89a9 | 0.0 |
| R | 0x7ce605cc...36d76e10 | 0.0 |
| S | 0xb8753014...f99d0386 | 0.0 |
| T | 0x35781dc0...d3f4588 | 0.0 |
| U | 0x75860da4...5ef9956 | 0.0 |
| V | 0xb59dd817...a89af2c3 | 0.0 |
| W | 0x5f32aef7...6ccc7b0 | 0.0 |
| X | 0xa95cbbd1...be33047d | 0.0 |
| Y | 0xd8e32848...fa2444c4 | 0.0 |
| Z | 0x7af0ef6e...6e4e197c | 0.0 |

---

## Multisig Probe Results

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|---|---|---|---|
| A-B | 0x0da4f428...987003 | 2 | HEALTHY |
| A-G | 0xf56c4a1c...bc0096 | 2 | HEALTHY |
| Y-Z | 0xd3ffe181...75b883 | 2 | HEALTHY |
| S-T | 0x3b1c3ae9...ed7883 | 2 | HEALTHY |
| V-W | 0x40fad7b4...80eb6d | 2 | HEALTHY |

All contracts healthy, all requiring 2-of-N signatures.

---

## MNX Market Status

**Status: UNAVAILABLE**

Endpoints probed:
- `https://testnet.mnx.fi/api/markets` — returns HTML (Next.js SPA, no REST API)
- `https://testnet.mnx.fi/api/v1/markets` — returns HTML
- `https://testnet.mnx.fi/api/tickers` — returns HTML

The testnet.mnx.fi site is a client-rendered app; no public REST API endpoints are exposed for market data at these paths.

---

## GF(3) Color Chain Statistics

Total world_increments: 468 (perfectly balanced across all three GF(3) field elements)

| GF3 Trit | Color Name | Hex | Count |
|---|---|---|---|
| 0 (id%3==0) | ERGODIC | #d3869b | 156 |
| 1 (id%3==1) | PLUS | #b8bb26 | 156 |
| -1 (id%3==2) | MINUS | #cc241d | 156 |

**Distribution:** Perfectly uniform — 156 each (33.33% each), total 468 increments.

---

## Database Tables

| Table | Rows |
|---|---|
| world_increments | 468 |
| repo_snapshots | 468 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |
