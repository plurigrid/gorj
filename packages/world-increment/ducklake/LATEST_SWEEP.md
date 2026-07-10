# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-10
**Run by:** world-increment-sweep + hamming-swarm-snapshot agent
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured | Total |
|--------|------|---------------|-------|
| plurigrid | org | 48 | 103 |
| kubeflow | org | 10 | 49 |
| TeglonLabs | org | 5 | 5 |
| bmorphism | user | 7 | 105 |
| zubyul | user | 6 | 49 |
| migalkin | social graph | 4 | 19 |
| DJedamski | social graph | 2 | 6 |
| wasita | social graph | 3 | 11 |
| kristinezheng | social graph | 1 | 5 |
| M1shaaa | social graph | 2 | 8 |
| AustinCStone | social graph | 3 | 40 |

> **Note:** GitHub API access scoped to repo-scoped endpoints. Used GitHub MCP search tools. Events API unavailable (non-repo endpoint restriction).

### Top 10 Repos by Stars
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15771 | — | 2026-07-10 |
| kubeflow/pipelines | 4169 | Python | 2026-07-09 |
| kubeflow/spark-operator | 3136 | Python | 2026-07-09 |
| kubeflow/trainer | 2134 | Go | 2026-07-10 |
| kubeflow/katib | 1689 | Python | 2026-07-09 |
| kubeflow/arena | 815 | Go | 2026-07-08 |
| kubeflow/kale | 695 | Python | 2026-07-10 |
| kubeflow/hub | 177 | Go | 2026-07-10 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |

### Most Active plurigrid repos (by recency)
| Repo | Stars | Open Issues | Language |
|------|-------|-------------|----------|
| plurigrid/asi | 30 | 4 | HTML |
| plurigrid/gorj | 1 | 1099 | Clojure |
| plurigrid/ontology | 8 | 16 | JavaScript |
| plurigrid/vcg-auction | 7 | 1 | Rust |
| plurigrid/agent | 5 | 6 | Python |
| plurigrid/zig-syrup | 2 | 0 | Zig |

### GF(3) Trit Color Chain Distribution
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 30 |
| 1 | #b8bb26 | PLUS | 31 |
| -1 | #cc241d | MINUS | 30 |

Total world_increments: 91 | repo_snapshots: 91

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 wallets (alice, bob, A-Z) queried against Aptos mainnet fullnode.
Result: All returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
Balance: 0.0 APT across all 28 addresses.

These addresses either do not hold APT directly or coin store not initialized on mainnet.

### Multisig Contract Probes (Aptos Mainnet)
All 5 probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|--------------|--------|
| A-B | 0x0da4...7003 | 2 | HEALTHY |
| A-G | 0xf56c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY |
| S-T | 0x3b1c...7883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

All 5 multisig contracts operational -- 2-of-N signatures required.

### MNX Markets (testnet.mnx.fi)
Status: UNAVAILABLE -- testnet frontend requires Vercel authentication.
API endpoints /api/markets and /api/v1/markets inaccessible. No market data inserted.

---

## DB Summary
| Table | Rows |
|-------|------|
| world_increments | 91 |
| repo_snapshots | 91 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

Sweep completed: 2026-07-10 UTC
