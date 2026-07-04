# World Increment Sweep + Hamming Swarm Snapshot
**Timestamp:** 2026-07-04

---

## JOB 1: GitHub Social Graph Sweep

### Summary
- **Total world increments:** 344
- **Total repo snapshots:** 1265

### Sources Covered
| Source | Repos |
|--------|-------|
| bmorphism | 103 |
| plurigrid | 102 |
| zubyul | 51 |
| kubeflow | 50 |
| TeglonLabs | 7 |
| migalkin | 7 |
| wasita | 6 |
| AustinCStone | 6 |
| kristinezheng | 4 |
| M1shaaa | 4 |
| DJedamski | 4 |

**Orgs:** plurigrid (100), kubeflow (48), TeglonLabs (5)
**Users:** bmorphism (100), zubyul (49)
**Social graph:** migalkin (5★), DJedamski (2), wasita (4), kristinezheng (2), M1shaaa (2), AustinCStone (4)

### Top Repos by Stars
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15761 | N/A |
| kubeflow/kubeflow | 15572 | N/A |
| kubeflow/kubeflow | 15565 | N/A |
| kubeflow/pipelines | 4169 | Python |
| kubeflow/pipelines | 4119 | Python |
| kubeflow/pipelines | 4119 | Python |
| kubeflow/spark-operator | 3132 | Python |
| kubeflow/spark-operator | 3114 | Python |
| kubeflow/spark-operator | 3111 | Python |
| kubeflow/trainer | 2129 | Go |

### GF(3) Color Chain Distribution
| Name | Color | Count |
|------|-------|-------|
| ERGODIC | #d3869b | 114 |
| MINUS | #cc241d | 115 |
| PLUS | #b8bb26 | 115 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses queried via `fullnode.mainnet.aptoslabs.com`.
All returned `resource_not_found` — accounts are unfunded/uninitialized on mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| A | 0x8699edc0960dd5b916... | unfunded |
| B | 0x3f892ebe6e45164e63... | unfunded |
| C | 0x38b99e63ada9b6fef1... | unfunded |
| D | 0xf77656248f64d5dd00... | unfunded |
| E | 0xdc1d9d533bac3507f9... | unfunded |
| F | 0x18a14b5b4bec118c1c... | unfunded |
| G | 0x69a394c0b0ac842127... | unfunded |
| H | 0xce67c327a7844e5488... | unfunded |
| I | 0x070fe5d74e4eda30e2... | unfunded |
| J | 0x4d964db8f538374034... | unfunded |
| K | 0xa732040a6b0d559041... | unfunded |
| L | 0x7c2eaeafad9725492e... | unfunded |
| M | 0x6fed37a7553ef16b2a... | unfunded |
| N | 0xe7dde6da0a65f51062... | unfunded |
| O | 0x73252b6011a75115a2... | unfunded |
| P | 0x6218792de4a9bc3891... | unfunded |
| Q | 0xac40fa50b81b4ca6b1... | unfunded |
| R | 0x7ce605cc8fda4f8e4a... | unfunded |
| S | 0xb8753014e4888ea48a... | unfunded |
| T | 0x35781dc0e42fef3f25... | unfunded |
| U | 0x75860da47565f6509b... | unfunded |
| V | 0xb59dd8170321dfab5a... | unfunded |
| W | 0x5f32aef70f5ba530d3... | unfunded |
| X | 0xa95cbbd116548ac990... | unfunded |
| Y | 0xd8e32848f1dffa811b... | unfunded |
| Z | 0x7af0ef6e1bd706f4b3... | unfunded |
| alice | 0xc793acdec12b4a6371... | unfunded |
| bob | 0x0a3c00c58fdf9020b2... | unfunded |

### Multisig Contract Probes (Aptos Mainnet)

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f428a0c007da0f... | 2 | ✓ |
| A-G | 0xf56c4a1c0906214f3f... | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c3a49... | 2 | ✓ |
| V-W | 0x40fad7b423a843650f... | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df40622... | 2 | ✓ |

**Result:** All 5 multisig contracts are healthy. Each requires 2-of-2 signatures.

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — testnet.mnx.fi is behind Vercel authentication. All API endpoints (
`/api/markets`, `/api/v1/markets`, `/api/tickers`, `/api/v1/tickers`) returned HTTP auth challenges.
Market data could not be extracted from the SPA.

---

## DuckDB Tables
- `world_increments` — 344 rows (GF3 color chain: ERGODIC/PLUS/MINUS)
- `repo_snapshots` — 1265 rows (GitHub repo metadata)
- `aptos_snapshots` — 28 rows (Hamming swarm A–Z + alice/bob)
- `multisig_probes` — 5 rows (2-of-2 all healthy)
- `mnx_snapshots` — 1 row (unavailable marker)
