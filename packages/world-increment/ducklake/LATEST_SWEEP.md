# LATEST_SWEEP.md — World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-02  
**Branch:** world-increment/sweep-2026-07-02  

---

## JOB 1: GitHub Social Graph Sweep

### DuckDB Ducklake Stats
- **Total world_increments:** 170 (GF3 color chain applied)
- **Unique repos snapshotted:** 518

### GF(3) Color Distribution
| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 56 |
| -1 | MINUS | `#cc241d` | 57 |
| 1 | PLUS | `#b8bb26` | 57 |

### Sources Snapshotted
| Org/User | Repos |
|----------|-------|
| kubeflow | 37 |
| plurigrid | 29 |
| bmorphism | 28 |
| zubyul | 22 |
| wasita | 11 |
| migalkin | 10 |
| AustinCStone | 8 |
| TeglonLabs | 7 |
| kristinezheng | 6 |
| M1shaaa | 6 |
| DJedamski | 6 |

### Top 15 Repos by Stars
| Org/User | Repo | Language | Stars | Forks | Last Push |
|----------|------|----------|-------|-------|----------|
| kubeflow | kubeflow | - | 15757 | 2683 | 2026-06-18 |
| kubeflow | pipelines | Python | 4167 | 2020 | 2026-07-02 |
| kubeflow | spark-operator | Python | 3130 | 1496 | 2026-07-02 |
| kubeflow | trainer | Go | 2128 | 974 | 2026-07-02 |
| kubeflow | katib | Python | 1688 | 529 | 2026-07-01 |
| kubeflow | examples | Jsonnet | 1460 | 756 | 2025-04-14 |
| kubeflow | community-distribution | YAML | 1028 | 1067 | 2026-06-30 |
| kubeflow | manifests | YAML | 1010 | 1069 | 2026-04-09 |
| kubeflow | arena | Go | 814 | 194 | 2026-07-02 |
| kubeflow | kale | Python | 694 | 156 | 2026-07-01 |
| kubeflow | mpi-operator | Go | 529 | 237 | 2026-07-02 |
| kubeflow | fairing | Jsonnet | 337 | 143 | 2022-04-11 |
| kubeflow | pytorch-operator | Jsonnet | 310 | 143 | 2021-12-01 |
| kubeflow | community | Jsonnet | 195 | 255 | 2026-04-08 |
| kubeflow | website | HTML | 184 | 916 | 2026-04-08 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

All 28 addresses queried via `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| A | `0x8699edc0960dd5b916...` | 0.00000000 |
| B | `0x3f892ebe6e45164e63...` | 0.00000000 |
| C | `0x38b99e63ada9b6fef1...` | 0.00000000 |
| D | `0xf77656248f64d5dd00...` | 0.00000000 |
| E | `0xdc1d9d533bac3507f9...` | 0.00000000 |
| F | `0x18a14b5b4bec118c1c...` | 0.00000000 |
| G | `0x69a394c0b0ac842127...` | 0.00000000 |
| H | `0xce67c327a7844e5488...` | 0.00000000 |
| I | `0x070fe5d74e4eda30e2...` | 0.00000000 |
| J | `0x4d964db8f538374034...` | 0.00000000 |
| K | `0xa732040a6b0d559041...` | 0.00000000 |
| L | `0x7c2eaeafad9725492e...` | 0.00000000 |
| M | `0x6fed37a7553ef16b2a...` | 0.00000000 |
| N | `0xe7dde6da0a65f51062...` | 0.00000000 |
| O | `0x73252b6011a75115a2...` | 0.00000000 |
| P | `0x6218792de4a9bc3891...` | 0.00000000 |
| Q | `0xac40fa50b81b4ca6b1...` | 0.00000000 |
| R | `0x7ce605cc8fda4f8e4a...` | 0.00000000 |
| S | `0xb8753014e4888ea48a...` | 0.00000000 |
| T | `0x35781dc0e42fef3f25...` | 0.00000000 |
| U | `0x75860da47565f6509b...` | 0.00000000 |
| V | `0xb59dd8170321dfab5a...` | 0.00000000 |
| W | `0x5f32aef70f5ba530d3...` | 0.00000000 |
| X | `0xa95cbbd116548ac990...` | 0.00000000 |
| Y | `0xd8e32848f1dffa811b...` | 0.00000000 |
| Z | `0x7af0ef6e1bd706f4b3...` | 0.00000000 |
| alice | `0xc793acdec12b4a6371...` | 0.00000000 |
| bob | `0x0a3c00c58fdf9020b2...` | 0.00000000 |

> Note: All balances returned 0 APT. Accounts may not have initialized a CoinStore resource, or the addresses represent multisig/contract accounts without direct APT holdings.

### Multisig Contract Probes
| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|--------|
| A-B | `0x0da4f428a0c007da0f...` | 2 | ✓ |
| A-G | `0xf56c4a1c0906214f3f...` | 2 | ✓ |
| S-T | `0x3b1c3ae905d44c3a49...` | 2 | ✓ |
| V-W | `0x40fad7b423a843650f...` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b2df40622...` | 2 | ✓ |

> All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`. All require 2-of-N signatures — healthy.

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — Vercel authentication required. All API paths (`/`, `/api/markets`, `/api/v1/markets`) returned 401 authentication challenge. No market data extractable.

---

## DuckDB Tables

| Table | Rows | Description |
|-------|------|-------------|
| world_increments | 170 | GF(3) color-chained event log |
| repo_snapshots | 1091 | GitHub repo metadata snapshots |
| aptos_snapshots | 28 | Aptos wallet balance snapshots |
| multisig_probes | 5 | Aptos multisig sigs-required probes |
| mnx_snapshots | 0 | MNX market data (empty — auth required) |

---
*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent*
