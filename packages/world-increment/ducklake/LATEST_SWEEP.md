# World-Increment Sweep + Hamming Snapshot
**Generated:** 2026-06-11 22:11 UTC
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social-graph | 19 |
| DJedamski | social-graph | 6 |
| wasita | social-graph | 1 |
| kristinezheng | social-graph | 5 |
| M1shaaa | social-graph | 8 |
| AustinCStone | social-graph | 30 |
| **TOTAL** | | **371** |

### Notable Repos (Top Stars)
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,713 | — | 2026-06-11 |
| kubeflow/pipelines | 4,152 | Python | 2026-06-11 |
| kubeflow/spark-operator | 3,126 | Python | 2026-06-09 |
| kubeflow/trainer | 2,111 | Go | 2026-06-11 |
| migalkin/NodePiece | 834+ | Python | — |
| TeglonLabs/mathpix-gem | 2 | Ruby | 2026-01-01 |
| TeglonLabs/jank-crane | 0 | C++ | 2026-06-08 |

### GF(3) Color Chain Assignment
| Trit | Color Hex | Name | Count |
|------|-----------|------|-------|
| 0 | `#d3869b` | ERGODIC | ~124 |
| +1 | `#b8bb26` | PLUS | ~124 |
| -1 | `#cc241d` | MINUS | ~123 |

### DuckDB Tables
- **world_increments**: 370 entries (GF3-annotated event log)
- **repo_snapshots**: 371 unique repo snapshots

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances
All 28 Hamming-swarm wallets queried on Aptos mainnet.
All balances: **0.00000000 APT** (accounts provisioned, balances at zero).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793acd...4cc7b | 0.0 |
| bob | 0x0a3c00c...512d5d | 0.0 |
| A–Z | 0x8699ed...–0x7af0ef... | 0.0 each |

### Multisig Contract Probes (5 pairs)
All 5 multisig contracts healthy — 2-of-N threshold confirmed.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f4...87003 | 2 | ✓ |
| A-G | 0xf56c4a...c0096 | 2 | ✓ |
| Y-Z | 0xd3ffe1...b883 | 2 | ✓ |
| S-T | 0x3b1c3a...7883 | 2 | ✓ |
| V-W | 0x40fad7...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — Vercel deployment protection active on testnet.mnx.fi.
No market data could be extracted without authentication token.

---

## Summary
- **371 repos** snapshotted across 11 GitHub sources (3 orgs + 8 users)
- **28 Aptos wallets** queried — all at 0 APT balance
- **5 multisig contracts** probed — all healthy at 2-of-N threshold
- **MNX testnet** — auth-gated, data unavailable
- GF(3) trit chain applied: ERGODIC(0/#d3869b) → PLUS(+1/#b8bb26) → MINUS(-1/#cc241d)
