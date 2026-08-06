# World Increment Sweep + Hamming Swarm Snapshot
**Timestamp:** 2026-08-06T (UTC)  
**Sweep ID:** world-increment-sweep + hamming-swarm-snapshot

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Found |
|--------|------|-------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social graph | 19 |
| DJedamski | social graph | 6 |
| wasita | social graph | 14 |
| kristinezheng | social graph | 5 |
| M1shaaa | social graph | 8 |
| AustinCStone | social graph | 41 |
| **Total (this sweep)** | | **328 repos** |

### Top Repos by Stars (this sweep)
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,805 | Jupyter Notebook |
| kubeflow/pipelines | 4,178 | Python |
| kubeflow/katib | 2,454 | Go |
| migalkin/NodePiece | 144 | Python |
| migalkin/StarE | 89 | Python |
| AustinCStone/TextGAN | 92 | Python |

### Notable Activity
- **wasita/xoxowasita-analysis**: Created 2026-08-04, last pushed 2026-08-05 (very recent activity)
- **TeglonLabs/jank-crane**: GF3 convergence maps and loopify pass spec (C++), pushed 2026-06-08
- **AustinCStone/byteruckus**: New repo created 2026-07-15
- **migalkin/kgcourse2021**: Updated 2026-07-10 (Knowledge Graphs course materials)

### GF(3) Color Chain Distribution (this sweep)
| Color | Name | Trit | Count |
|-------|------|------|-------|
| #d3869b | ERGODIC | 0 | 116 |
| #b8bb26 | PLUS | +1 | 118 |
| #cc241d | MINUS | -1 | 117 |

### DuckDB State
- `world_increments`: 351 total rows (prior + this sweep)
- `repo_snapshots`: 1272 total rows (prior + this sweep)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
All 28 addresses (alice, bob, A–Z) returned **0.0 APT** — accounts have no CoinStore resource registered on mainnet (unfunded or different network).

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...12d5 | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...f588 | 0.0 |
| U | 0x7586...f956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

### Multisig Contract Probes (Mainnet)
All 5 multisig contracts are **healthy** — each requires exactly 2 signatures.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)
**Status: SPA — no JSON API exposed.** All probed paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`) return the Next.js HTML shell. Market data is unavailable without browser execution. `mnx_snapshots` table is empty for this sweep.

---

## DuckDB Tables Written
- `packages/world-increment/ducklake/world-increments.duckdb`
  - `world_increments` — 351 rows (GF3 color-chained)
  - `repo_snapshots` — 1272 rows
  - `aptos_snapshots` — 28 rows (all 0.0 APT)
  - `multisig_probes` — 5 rows (all healthy, 2-of-N)
  - `mnx_snapshots` — 0 rows (SPA, unavailable)
