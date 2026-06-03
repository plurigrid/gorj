# World Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-06-03  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 25 (100 total in org) |
| kubeflow | org | 13 (representative sample) |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 10 (50 total) |
| migalkin | social graph | 5 |
| wasita | social graph | 4 |
| DJedamski | social graph | 2 |
| kristinezheng | social graph | 2 |
| M1shaaa | social graph | 2 |
| AustinCStone | social graph | 3 |
| **Total** | | **170 repo snapshots** |

### Top Repos by Stars
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,704 | — | 2026-05-24 |
| kubeflow/pipelines | 4,152 | Python | 2026-06-03 |
| kubeflow/spark-operator | 3,125 | Python | 2026-06-01 |
| kubeflow/trainer | 2,110 | Go | 2026-06-03 |
| kubeflow/katib | 1,685 | Python | 2026-05-29 |
| kubeflow/manifests | 1,020 | YAML | 2026-06-02 |
| kubeflow/arena | 811 | Go | 2026-05-07 |
| kubeflow/mpi-operator | 528 | Go | 2026-06-02 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/asi | 24 | HTML | 2026-04-26 |
| bmorphism/risc0-cosmwasm-example | 23 | Rust | 2022-10-20 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| bmorphism/say-mcp-server | 20 | JavaScript | 2025-01-07 |
| migalkin/StarE | 89 | Python | 2023-12-01 |

### Most Active (Open Issues)
| Repo | Open Issues |
|------|-------------|
| kubeflow/pipelines | 487 |
| plurigrid/gorj | 321 |
| bmorphism/Gay.jl | 189 |
| kubeflow/notebooks | 174 |
| kubeflow/sdk | 134 |
| kubeflow/mpi-operator | 103 |
| plurigrid/eirobri | 28 |
| plurigrid/nanoclj-zig | 20 |

### GF(3) Color Chain Distribution (170 increments)
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 56 |
| 1 | #b8bb26 | PLUS | 57 |
| -1 | #cc241d | MINUS | 57 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)
All 28 Hamming swarm addresses (alice, bob, A-Z) queried against
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
All returned 0 APT -- no CoinStore resource registered on mainnet for
these addresses (accounts exist but hold no native APT or have not
initialized the coin store).

### Multisig Contract Probes (5 pairs)
All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428a0c007da... | 2 | YES |
| A-G | 0xf56c4a1c09062143... | 2 | YES |
| Y-Z | 0xd3ffe1812b2df406... | 2 | YES |
| S-T | 0x3b1c3ae905d44c3a... | 2 | YES |
| V-W | 0x40fad7b423a84365... | 2 | YES |

All multisigs healthy -- 2-of-N threshold confirmed on-chain.

### MNX Markets (testnet.mnx.fi)
Status: SPA (Next.js) -- no public REST API endpoint accessible.
The frontend loads as a client-side rendered app; /api/markets and
/api/v1/markets return 404. Market data not extractable without browser
execution. No entries written to mnx_snapshots.

---

## Database Tables
- **world_increments**: 170 rows -- GF(3) trit-colored repo push events
- **repo_snapshots**: 170 rows -- stars, forks, issues, pushed_at, description
- **aptos_snapshots**: 28 rows -- alice, bob, A-Z balances (all 0 APT)
- **multisig_probes**: 5 rows -- all pairs require 2 sigs, all healthy
- **mnx_snapshots**: 0 rows -- SPA, no API data available
