# World Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-08-03  
**GF(3) Color Chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d (cycling)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Snapshotted | Total Stars |
|--------|------|-------------------|-------------|
| kubeflow | org | 49 | 34,454 |
| migalkin | user (zubyul social) | 19 | 275 |
| bmorphism | user | 100 | 247 |
| plurigrid | org | 100 | 111 |
| AustinCStone | user (zubyul social) | 41 | 103 |
| zubyul | user | 49 | 14 |
| wasita | user (zubyul social) | 12 | 4 |
| DJedamski | user (zubyul social) | 6 | 3 |
| TeglonLabs | org | 5 | 2 |
| kristinezheng | user (zubyul social) | 5 | 0 |
| M1shaaa | user (zubyul social) | 8 | 0 |

**Total:** 321 repos across 11 sources stored in `repo_snapshots`

### Top Repos by Stars (this sweep)
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,804 | — |
| kubeflow/pipelines | 4,173 | Python |
| kubeflow/spark-operator | 3,142 | Python |
| kubeflow/trainer | 2,165 | Go |
| kubeflow/katib | 1,694 | Python |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| TeglonLabs/mathpix-gem | 2 | Ruby |
| TeglonLabs/jank-crane | 0 | C++ |

### Notable Activity
- **TeglonLabs/jank-crane** pushed 2026-06-08: "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow"
- **kubeflow/mcp-apache-spark-history-server** (185 stars) — MCP tooling for Spark
- **wasita/wasita.github.io** pushed 2026-07-21 (most recent non-kubeflow activity in social graph)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)
**Method:** `0x1::coin::balance` view function on mainnet  
**Total APT across swarm:** ~20.34 APT

| World | Balance (APT) | Address (short) |
|-------|---------------|-----------------|
| bob | 12.6570 | 0x0a3c...512d |
| F | 1.9605 | 0x18a1...cf71 |
| L | 1.9273 | 0x7c2e...eba9 |
| J | 1.8951 | 0x4d96...7f54 |
| alice | 0.4364 | 0xc793...cc7b |
| O | 0.2101 | 0x7325...a89d |
| K | 0.1620 | 0xa732...5dc4 |
| P | 0.1401 | 0x6218...c948 |
| M | 0.1123 | 0x6fed...f2e9 |
| N | 0.1061 | 0xe7dd...1b2c |
| Q | 0.1032 | 0xac40...89a9 |
| S | 0.0918 | 0xb875...0386 |
| R | 0.0902 | 0x7ce6...6e10 |
| T | 0.0737 | 0x3578...4588 |
| U | 0.0558 | 0x7586...9956 |
| A | 0.0518 | 0x8699...9d7a |
| V | 0.0488 | 0xb59d...f2c3 |
| Y | 0.0444 | 0xd8e3...44c4 |
| X | 0.0426 | 0xa95c...047d |
| W | 0.0407 | 0x5f32...c7b0 |
| B | 0.0363 | 0x3f89...cb13 |
| Z | 0.0243 | 0x7af0...197c |
| D | 0.0116 | 0xf776...fdd1 |
| C | 0.0102 | 0x38b9...535e |
| E | 0.0094 | 0xdc1d...8d36 |
| H | 0.0017 | 0xce67...300f |
| I | 0.0007 | 0x070f...1fc9 |
| G | 0.0007 | 0x69a3...c7f32 |

**Observation:** bob (12.66 APT) holds ~62% of total swarm balance. F, L, J each hold ~1.9 APT. Remaining 24 wallets share ~3.5 APT.

### Multisig Contract Probes (5 contracts)
All 5 multisig contracts healthy — requiring 2 signatures each.

| Pair | Address (short) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | OK |
| A-G | 0xf56c...0096 | 2 | OK |
| Y-Z | 0xd3ff...b883 | 2 | OK |
| S-T | 0x3b1c...7883 | 2 | OK |
| V-W | 0x40fa...eb6d | 2 | OK |

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — `testnet.mnx.fi` is a Next.js SPA with no publicly accessible JSON API endpoint. All probed API paths return the SPA HTML shell. No market data extractable.

---

## DuckDB Schema Summary
- `world_increments`: 34 rows (GF(3) color-tagged sweep events)
- `repo_snapshots`: 1,265 rows (cumulative across all sweeps)
- `aptos_snapshots`: 28 rows (this sweep)
- `multisig_probes`: 5 rows (this sweep)
- `mnx_snapshots`: 1 row (unavailable marker)
