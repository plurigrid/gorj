# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-07-08 00:13 UTC
**GF(3) color chain active** — id%3: 0→ERGODIC #d3869b, 1→PLUS #b8bb26, 2→MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos |
|--------|------|-------|
| bmorphism | user | 103 |
| plurigrid | org | 102 |
| zubyul | user | 51 |
| kubeflow | org | 51 |
| AustinCStone | user | 32 |
| migalkin | user | 21 |
| wasita | user | 13 |
| M1shaaa | user | 10 |
| DJedamski | user | 8 |
| TeglonLabs | org | 7 |
| kristinezheng | user | 7 |

**Total world_increments in DB:** 405
**Total repo_snapshots in DB:** 1326

### Top Repos by Stars
| Repo | Language | Stars | Forks | Last Push |
|------|----------|-------|-------|-----------|
| kubeflow/kubeflow |  | 15769 | 2685 | 2026-07-06 |
| kubeflow/kubeflow |  | 15572 | 2633 | 2026-01-05 |
| kubeflow/kubeflow |  | 15565 | 2626 | 2026-01-05 |
| kubeflow/pipelines | Python | 4169 | 2029 | 2026-07-07 |
| kubeflow/pipelines | Python | 4119 | 1984 | 2026-04-10 |
| kubeflow/pipelines | Python | 4119 | 1985 | 2026-04-14 |
| kubeflow/spark-operator | Python | 3133 | 1498 | 2026-07-02 |
| kubeflow/spark-operator | Python | 3114 | 1483 | 2026-04-13 |
| kubeflow/spark-operator | Python | 3111 | 1483 | 2026-04-10 |
| kubeflow/trainer | Go | 2130 | 980 | 2026-07-07 |

### Language Distribution (top 10)
| Language | Repos |
|----------|-------|
| Python | 234 |
| Rust | 57 |
| JavaScript | 54 |
| HTML | 53 |
| Go | 51 |
| TypeScript | 46 |
| Jupyter Notebook | 41 |
| Clojure | 27 |
| Jsonnet | 23 |
| R | 22 |

### GF(3) Trit Distribution
| Name | Color | Count |
|------|-------|-------|
| ERGODIC | #d3869b | 134 |
| MINUS | #cc241d | 135 |
| PLUS | #b8bb26 | 136 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances
All 28 addresses (alice, bob, A-Z) queried against Aptos mainnet.
All returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` —
indicating no APT coin store registered (0 APT balance on mainnet).

| World | Balance (APT) | Status |
|-------|--------------|--------|
| A | 0.0 | no coin store |
| B | 0.0 | no coin store |
| C | 0.0 | no coin store |
| D | 0.0 | no coin store |
| E | 0.0 | no coin store |
| F | 0.0 | no coin store |
| G | 0.0 | no coin store |
| H | 0.0 | no coin store |
| I | 0.0 | no coin store |
| J | 0.0 | no coin store |
| K | 0.0 | no coin store |
| L | 0.0 | no coin store |
| M | 0.0 | no coin store |
| N | 0.0 | no coin store |
| O | 0.0 | no coin store |
| P | 0.0 | no coin store |
| Q | 0.0 | no coin store |
| R | 0.0 | no coin store |
| S | 0.0 | no coin store |
| T | 0.0 | no coin store |
| U | 0.0 | no coin store |
| V | 0.0 | no coin store |
| W | 0.0 | no coin store |
| X | 0.0 | no coin store |
| Y | 0.0 | no coin store |
| Z | 0.0 | no coin store |
| alice | 0.0 | no coin store |
| bob | 0.0 | no coin store |

### Multisig Contract Probes
All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | `0x0da4f428a0c007...` | 2 | ✓ |
| A-G | `0xf56c4a1c090621...` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b2df4...` | 2 | ✓ |
| S-T | `0x3b1c3ae905d44c...` | 2 | ✓ |
| V-W | `0x40fad7b423a843...` | 2 | ✓ |

**Result:** All 5 multisig contracts healthy — 2-of-2 signature threshold on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)
**Status:** UNAVAILABLE — testnet.mnx.fi returns HTTP 401 Unauthorized on all endpoints
(both `/` and `/api/markets`). API requires authentication credentials not available in this sweep.

---

## DuckDB Schema Summary
- `world_increments` — 405 rows (GF3-tagged event log)
- `repo_snapshots` — 1326 rows (full repo metadata)
- `aptos_snapshots` — 28 rows (balance snapshot)
- `multisig_probes` — 5 rows (contract health check)
- `mnx_snapshots` — 1 row (unavailable marker)

**DB location:** `packages/world-increment/ducklake/world-increments.duckdb`
