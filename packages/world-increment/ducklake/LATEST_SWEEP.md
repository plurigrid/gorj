# World-Increment Sweep + Hamming Snapshot

**Run date:** 2026-07-29  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1 — GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|:-----------------:|
| plurigrid | org | 50 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 50 |
| zubyul | user | 49 |
| migalkin | social | 5 |
| wasita | social | 3 |
| AustinCStone | social | 3 |
| DJedamski | social | 2 |
| kristinezheng | social | 2 |
| M1shaaa | social | 2 |
| **Total** | | **220** |

### GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|------:|
| 0 | ERGODIC | `#d3869b` | 73 |
| +1 | PLUS | `#b8bb26` | 74 |
| -1 | MINUS | `#cc241d` | 73 |

### Top Repos by Stars (this sweep)

| Repo | Language | Stars | Forks |
|------|----------|------:|------:|
| kubeflow/kubeflow | — | 15,794 | 2,689 |
| kubeflow/pipelines | Python | 4,171 | 2,069 |
| kubeflow/spark-operator | Python | 3,142 | 1,509 |
| kubeflow/trainer | Go | 2,159 | 1,000 |
| kubeflow/katib | Python | 1,693 | 532 |
| kubeflow/examples | Jsonnet | 1,461 | 756 |
| migalkin/NodePiece | Python | 144 | 21 |
| AustinCStone/TextGAN | Python | 92 | 30 |
| migalkin/StarE | Python | 89 | 16 |
| AustinCStone/StereoVisionMRF | Python | 11 | 4 |

### Notable TeglonLabs Activity

- **jank-crane** (C++, pushed 2026-06-08): crane-jank converged-IR hub with GF3 convergence maps
- **mathpix-gem** (Ruby, pushed 2026-01-01): Mathpix OCR gem — 11 open issues
- **coin-flip-mcp** (JavaScript): MCP server for random.org coin flips — 2 forks

---

## JOB 2 — Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (alice, bob, A–Z)

All 28 wallets queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|:-------------:|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...9956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

**Finding:** All 28 wallets hold 0 APT on mainnet at snapshot time. Accounts exist on-chain but have no funded coin store resources.

### Multisig Contract Probes

All 5 multisig pairs probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|:-------------:|:-------:|
| A-B | 0x0da4...7003 | 2 | yes |
| A-G | 0xf56c...0096 | 2 | yes |
| Y-Z | 0xd3ff...b883 | 2 | yes |
| S-T | 0x3b1c...7883 | 2 | yes |
| V-W | 0x40fa...eb6d | 2 | yes |

**Finding:** All 5 multisig contracts require 2-of-N signatures. All probes responded — contracts deployed and healthy. No threshold anomalies.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA (dark-mode UI, no public REST endpoints). `/api/markets` and `/api/v1/markets` returned HTML, not JSON. No market data extractable without browser execution. **Status: unavailable via API.**

---

## Database Summary

| Table | Rows |
|-------|-----:|
| world_increments | 220 |
| repo_snapshots | 220 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA, no API) |

GF(3) trit distribution: 73 ERGODIC / 74 PLUS / 73 MINUS across 220 world increments.
