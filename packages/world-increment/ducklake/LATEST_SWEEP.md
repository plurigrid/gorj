# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp**: 2026-08-07 00:27 UTC
**Database**: `packages/world-increment/ducklake/world-increments.duckdb`

---

## Job 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 25 (of 103 total) |
| kubeflow | org | 20 (of 49 total) |
| TeglonLabs | org | 5 (of 5 total) |
| bmorphism | user | 18 (of 106 total) |
| zubyul | user | 10 (of 49 total) |
| migalkin (social) | user | 5 |
| wasita (social) | user | 3 |
| AustinCStone (social) | user | 2 |
| kristinezheng (social) | user | 1 |
| M1shaaa (social) | user | 1 |
| DJedamski (social) | user | 1 |
| **Total** | | **91 new increments** |

### Top Repos by Stars
| Repo | Lang | ⭐ | 🍴 | Last Push |
|------|------|-----|-----|-----------|
| kubeflow/kubeflow | — | 15,805 | 2,691 | 2026-07-10 |
| kubeflow/pipelines | Python | 4,179 | 2,080 | 2026-08-06 |
| kubeflow/spark-operator | Python | 3,144 | 1,511 | 2026-08-06 |
| kubeflow/trainer | Go | 2,172 | 1,015 | 2026-08-06 |
| kubeflow/katib | Python | 1,694 | 534 | 2026-08-06 |
| kubeflow/examples | Jsonnet | 1,461 | 755 | 2025-04-14 |
| kubeflow/community-distribution | YAML | 1,029 | 1,070 | 2026-08-04 |
| plurigrid/asi | HTML | 59 | 13 | 2026-07-10 |
| bmorphism/Gay.jl | Julia | 2 | 1 | 2026-08-06 |
| plurigrid/gorj | Clojure | 1 | 0 | 2026-08-06 |

### GF(3) Color Chain Distribution (this run)
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | ~30 |
| 1 | #b8bb26 | PLUS | ~31 |
| -1 | #cc241d | MINUS | ~30 |

### Notable Activity
- **plurigrid/gorj**: 1,683 open issues, pushed 2026-08-06 — most active plurigrid repo
- **kubeflow/katib**: AutoML on K8s pushed 2026-08-06T23:09
- **bmorphism/Gay.jl**: 188 open issues, pushed 2026-08-06 — highly active color math lib
- **TeglonLabs/jank-crane**: crane-jank converged-IR hub, GF3 convergence maps (2026-06-08)
- **wasita/xoxowasita-analysis**: pushed 2026-08-06 — zubyul social graph active

---

## Job 2: Hamming Swarm Snapshot (Aptos Mainnet)

**Total APT across swarm**: 20.3448 APT
**Snapshot taken**: 2026-08-07 00:27 UTC

### Wallet Balances (alice/bob + A-Z)

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.43643352 |
| bob | 0x0a3c...2d5d | 12.657007 |
| A | 0x8699...9d7a | 0.051767 |
| B | 0x3f89...b13 | 0.036256 |
| C | 0x38b9...35e | 0.010185 |
| D | 0xf776...dd1 | 0.011629 |
| E | 0xdc1d...d36 | 0.009372 |
| F | 0x18a1...f71 | 1.960516 |
| G | 0x69a3...f32 | 0.000681 |
| H | 0xce67...00f | 0.001681 |
| I | 0x070f...c9 | 0.000681 |
| J | 0x4d96...f54 | 1.895093 |
| K | 0xa732...dc4 | 0.161961 |
| L | 0x7c2e...ba9 | 1.927269 |
| M | 0x6fed...e9 | 0.112285 |
| N | 0xe7dd...b2c | 0.106121 |
| O | 0x7325...89d | 0.210136 |
| P | 0x6218...948 | 0.140136 |
| Q | 0xac40...9a9 | 0.10324 |
| R | 0x7ce6...e10 | 0.090217 |
| S | 0xb875...386 | 0.091788 |
| T | 0x3578...588 | 0.073713 |
| U | 0x7586...956 | 0.055773 |
| V | 0xb59d...2c3 | 0.048833 |
| W | 0x5f32...b0 | 0.040705 |
| X | 0xa95c...47d | 0.042577 |
| Y | 0xd8e3...4c4 | 0.044449 |
| Z | 0x7af0...97c | 0.024268 |

**Notable**: bob leads at 12.657 APT; F, J, L each hold ~1.9-1.96 APT.

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c...096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ff...883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c...883 | 2 | ✅ HEALTHY |
| V-W | 0x40fa...b6d | 2 | ✅ HEALTHY |

All 5 multisig contracts respond with 2-of-N requirement. All healthy.

### MNX Markets (testnet.mnx.fi)

Status: **SPA unavailable** — testnet.mnx.fi returns a Next.js SPA with no public REST API endpoints. Data extraction not possible without browser execution. Recorded as unavailable in `mnx_snapshots`.

---

## DuckDB Ducklake Summary

**File**: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows (cumulative) |
|-------|-------------------|
| world_increments | 1 (this run) |
| repo_snapshots | (cumulative across runs) |
| aptos_snapshots | 28 (this run) |
| multisig_probes | 5 (this run) |
| mnx_snapshots | 0 (unavailable) |
