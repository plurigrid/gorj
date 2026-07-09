# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-09T18:13:33Z

## GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org/user | 210 |
| bmorphism | org/user | 208 |
| TeglonLabs | org/user | 110 |
| kubeflow | org/user | 101 |
| AustinCStone | org/user | 89 |
| migalkin | org/user | 65 |
| wasita | org/user | 64 |
| zubyul | org/user | 53 |
| kristinezheng | org/user | 39 |
| M1shaaa | org/user | 35 |
| DJedamski | org/user | 25 |

**Total repo snapshots in DB:** 999
**Total world increments:** 78

### GF(3) Color Chain Distribution
| Name | Color | Trit | Count |
|------|-------|------|-------|
| PLUS | #b8bb26 | 1 | 27 |
| MINUS | #cc241d | -1 | 26 |
| ERGODIC | #d3869b | 0 | 25 |

### Recently Pushed Repos (since 2026-07-01)
| Org/User | Repo | Pushed At | Stars |
|----------|------|-----------|-------|
| kubeflow | kubeflow/pipelines | 2026-07-09T18:01:52Z | 4169 |
| kubeflow | kubeflow/mpi-operator | 2026-07-09T17:44:30Z | 529 |
| plurigrid | plurigrid/gorj | 2026-07-09T17:15:03Z | 1 |
| kubeflow | kubeflow/trainer | 2026-07-09T16:18:26Z | 2134 |
| kubeflow | kubeflow/kubeflow | 2026-07-09T13:40:56Z | 15769 |
| kubeflow | kubeflow/katib | 2026-07-09T13:35:36Z | 1689 |
| kubeflow | kubeflow/spark-operator | 2026-07-09T08:56:50Z | 3136 |
| plurigrid | plurigrid/world-increment | 2026-07-09T00:00:00Z | 0 |
| kubeflow | kubeflow/sdk | 2026-07-08T13:38:30Z | 123 |
| plurigrid | plurigrid/place | 2026-07-07T03:10:28Z | 1 |

## Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (A–Z + alice/bob)

**Result:** All 28 addresses returned HTTP 404 — accounts are not initialized on
Aptos mainnet (no CoinStore resource). Balances recorded as 0.0 APT.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793ac...4cc7b | 0.0 (404) |
| bob | 0x0a3c00...512d5d | 0.0 (404) |
| A | 0x8699ed...b9d7a | 0.0 (404) |
| B | 0x3f892e...b13 | 0.0 (404) |
| C | 0x38b99e...535e | 0.0 (404) |
| D | 0xf77656...cfdd1 | 0.0 (404) |
| E | 0xdc1d9d...8d36 | 0.0 (404) |
| F | 0x18a14b...cf71 | 0.0 (404) |
| G | 0x69a394...7f32 | 0.0 (404) |
| H | 0xce67c3...300f | 0.0 (404) |
| I | 0x070fe5...1fc9 | 0.0 (404) |
| J | 0x4d964d...7f54 | 0.0 (404) |
| K | 0xa73204...25dc4 | 0.0 (404) |
| L | 0x7c2eae...eba9 | 0.0 (404) |
| M | 0x6fed37...7f2e9 | 0.0 (404) |
| N | 0xe7dde6...51b2c | 0.0 (404) |
| O | 0x732526...5a89d | 0.0 (404) |
| P | 0x621879...ec948 | 0.0 (404) |
| Q | 0xac40fa...c89a9 | 0.0 (404) |
| R | 0x7ce605...6e10 | 0.0 (404) |
| S | 0xb87530...0386 | 0.0 (404) |
| T | 0x357810...f4588 | 0.0 (404) |
| U | 0x758604...f9956 | 0.0 (404) |
| V | 0xb59dd8...af2c3 | 0.0 (404) |
| W | 0x5f32ae...c7b0 | 0.0 (404) |
| X | 0xa95cbb...3047d | 0.0 (404) |
| Y | 0xd8e328...444c4 | 0.0 (404) |
| Z | 0x7af0ef...197c | 0.0 (404) |

### Multisig Contract Probes

All 5 multisig contracts are **healthy** (2-of-2 signatures required).

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4f4...87003 | 2 | ✓ healthy |
| A-G | 0xf56c4a...b0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ffe1...5b883 | 2 | ✓ healthy |
| S-T | 0x3b1c3a...7883 | 2 | ✓ healthy |
| V-W | 0x40fad7...0eb6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

Status: **401 Unauthorized** — API requires authentication. No market data available.

## Notes

- DuckDB binary unavailable (GitHub download blocked by proxy); using `duckdb` Python package v1.5.4
- Aptos addresses appear to be pre-funded swarm keys not yet initialized on mainnet
- All 5 Hamming multisig contracts live with 2-of-2 threshold
- GF(3) trit distribution balanced: ERGODIC(25), PLUS(27), MINUS(26)