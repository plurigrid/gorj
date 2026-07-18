# LATEST_SWEEP.md — World Increment + Hamming Swarm Snapshot

Generated: 2026-07-18 06:11 UTC

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain Distribution
| GF3 Name | Color | Count |
|----------|-------|-------|
| ERGODIC | #d3869b | 56 |
| MINUS | #cc241d | 57 |
| PLUS | #b8bb26 | 58 |

### Source Coverage
| Source | Repos Snapshotted |
|--------|-------------------|
| bmorphism | 33 |
| plurigrid | 32 |
| zubyul | 32 |
| kubeflow | 32 |
| AustinCStone | 12 |
| TeglonLabs | 7 |
| migalkin | 6 |
| wasita | 5 |
| kristinezheng | 4 |
| M1shaaa | 4 |
| DJedamski | 4 |

### Top Repos by Stars
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15780 | - | 2026-07-10 |
| kubeflow/kubeflow | 15572 | - | 2026-01-05 |
| kubeflow/kubeflow | 15565 | - | 2026-01-05 |
| kubeflow/pipelines | 4168 | Python | 2026-07-17 |
| kubeflow/pipelines | 4119 | Python | 2026-04-10 |
| kubeflow/pipelines | 4119 | Python | 2026-04-14 |
| kubeflow/spark-operator | 3139 | Python | 2026-07-17 |
| kubeflow/spark-operator | 3114 | Python | 2026-04-13 |
| kubeflow/spark-operator | 3111 | Python | 2026-04-10 |
| kubeflow/trainer | 2151 | Go | 2026-07-18 |

### Key Observations
- **plurigrid**: 103 repos total; `gorj` (Clojure, 1 star, 1233 open issues) last pushed 2026-07-18; `asi` (HTML, 31 stars) is the most-starred
- **kubeflow**: 49 repos; `kubeflow/kubeflow` (15780 stars) is the flagship; active ML infra with trainer/pipelines/katib/spark-operator all pushed this week
- **TeglonLabs**: 5 repos; `jank-crane` (C++, GF3 convergence maps) most recent (2026-06-08)
- **bmorphism**: 106 repos; `Gay.jl` (Julia, wide-gamut color/SPI) most active; `ocaml-mcp-sdk` (61 stars) notable
- **zubyul**: 49 repos; active in Nash TUI, Gay.jl forks, openbci-visualizer
- **migalkin**: 19 repos; `NodePiece` (144 stars), `StarE` (89 stars) are KG research highlights
- **DJedamski**: 6 repos; inactive (last push 2018)
- **wasita**: 12 repos; personal website + research tools, last pushed 2026-07-16
- **kristinezheng**: 5 repos; academic/cognitive science work
- **M1shaaa**: 8 repos; profile updated 2026-07-18
- **AustinCStone**: 41 repos; `byteruckus` (HTML) most recent (2026-07-15)

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (alice–Z, 28 worlds)
All 28 addresses queried on Aptos mainnet. **All wallets returned null CoinStore balance** — accounts exist but have zero or uninitialized APT CoinStore resource at time of snapshot.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| A | 0x8699edc0960dd5b916... | null |
| B | 0x3f892ebe6e45164e63... | null |
| C | 0x38b99e63ada9b6fef1... | null |
| D | 0xf77656248f64d5dd00... | null |
| E | 0xdc1d9d533bac3507f9... | null |
| F | 0x18a14b5b4bec118c1c... | null |
| G | 0x69a394c0b0ac842127... | null |
| H | 0xce67c327a7844e5488... | null |
| I | 0x070fe5d74e4eda30e2... | null |
| J | 0x4d964db8f538374034... | null |
| K | 0xa732040a6b0d559041... | null |
| L | 0x7c2eaeafad9725492e... | null |
| M | 0x6fed37a7553ef16b2a... | null |
| N | 0xe7dde6da0a65f51062... | null |
| O | 0x73252b6011a75115a2... | null |
| P | 0x6218792de4a9bc3891... | null |
| Q | 0xac40fa50b81b4ca6b1... | null |
| R | 0x7ce605cc8fda4f8e4a... | null |
| S | 0xb8753014e4888ea48a... | null |
| T | 0x35781dc0e42fef3f25... | null |
| U | 0x75860da47565f6509b... | null |
| V | 0xb59dd8170321dfab5a... | null |
| W | 0x5f32aef70f5ba530d3... | null |
| X | 0xa95cbbd116548ac990... | null |
| Y | 0xd8e32848f1dffa811b... | null |
| Z | 0x7af0ef6e1bd706f4b3... | null |
| alice | 0xc793acdec12b4a6371... | null |
| bob | 0x0a3c00c58fdf9020b2... | null |

### Multisig Contract Probes (5 pairs)
All 5 multisig contracts are **healthy** and require **2 signatures**.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|--------------|---------|
| A-B | 0x0da4f428a0c007da0f... | 2 | ✓ |
| A-G | 0xf56c4a1c0906214f3f... | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df40622... | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c3a49... | 2 | ✓ |
| V-W | 0x40fad7b423a843650f... | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)
Status: **UNAVAILABLE** — testnet.mnx.fi requires Vercel authentication. No market data could be retrieved.

---

## DuckDB Schema Summary
- `world_increments`: 171 rows
- `repo_snapshots`: 1092 rows  
- `aptos_snapshots`: 28 rows
- `multisig_probes`: 5 rows
- `mnx_snapshots`: 0 rows (unavailable)
