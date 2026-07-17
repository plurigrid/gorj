# World-Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-07-17 11:12 UTC

---

## Job 1: GitHub Social Graph Sweep

### Coverage
| Source | Repos |
|--------|-------|
| plurigrid | 300 |
| bmorphism | 250 |
| kubeflow | 143 |
| AustinCStone | 116 |
| TeglonLabs | 111 |
| zubyul | 97 |
| migalkin | 79 |
| wasita | 61 |
| kristinezheng | 41 |
| M1shaaa | 40 |
| DJedamski | 28 |

**Total increments recorded:** 345  
**Total repo snapshots:** 1266

### GF(3) Color Chain Distribution
| Name | Color | Count |
|------|-------|-------|
| PLUS | `#b8bb26` | 116 |
| MINUS | `#cc241d` | 115 |
| ERGODIC | `#d3869b` | 114 |

### Top 10 Repos by Stars
| Org/User | Repo | Language | ★ | Forks | Last Push |
|----------|------|----------|---|-------|-----------|
| kubeflow | kubeflow | - | 15779 | 2686 | 2026-07-10 |
| kubeflow | kubeflow | - | 15572 | 2633 | 2026-01-05 |
| kubeflow | kubeflow | - | 15565 | 2626 | 2026-01-05 |
| kubeflow | pipelines | Python | 4167 | 2040 | 2026-07-16 |
| kubeflow | pipelines | Python | 4119 | 1984 | 2026-04-10 |
| kubeflow | pipelines | Python | 4119 | 1985 | 2026-04-14 |
| kubeflow | spark-operator | Python | 3137 | 1500 | 2026-07-16 |
| kubeflow | spark-operator | Python | 3114 | 1483 | 2026-04-13 |
| kubeflow | spark-operator | Python | 3111 | 1483 | 2026-04-10 |
| kubeflow | trainer | Go | 2151 | 989 | 2026-07-16 |

### Top Languages
| Language | Count |
|----------|-------|
| Python | 228 |
| HTML | 54 |
| Go | 51 |
| Rust | 50 |
| JavaScript | 41 |
| TypeScript | 40 |
| Jupyter Notebook | 39 |
| Clojure | 29 |
| Jsonnet | 23 |
| R | 22 |

---

## Job 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (2026-07-17)

All 28 Hamming-swarm addresses queried on Aptos mainnet.  
All accounts returned `resource_not_found` for `0x1::coin::CoinStore<AptosCoin>`,  
indicating coin stores not yet initialized (accounts exist — address A has sequence_number=58).

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| A | `0x8699edc0960dd5b916...` | not initialized |
| B | `0x3f892ebe6e45164e63...` | not initialized |
| C | `0x38b99e63ada9b6fef1...` | not initialized |
| D | `0xf77656248f64d5dd00...` | not initialized |
| E | `0xdc1d9d533bac3507f9...` | not initialized |
| F | `0x18a14b5b4bec118c1c...` | not initialized |
| G | `0x69a394c0b0ac842127...` | not initialized |
| H | `0xce67c327a7844e5488...` | not initialized |
| I | `0x070fe5d74e4eda30e2...` | not initialized |
| J | `0x4d964db8f538374034...` | not initialized |
| K | `0xa732040a6b0d559041...` | not initialized |
| L | `0x7c2eaeafad9725492e...` | not initialized |
| M | `0x6fed37a7553ef16b2a...` | not initialized |
| N | `0xe7dde6da0a65f51062...` | not initialized |
| O | `0x73252b6011a75115a2...` | not initialized |
| P | `0x6218792de4a9bc3891...` | not initialized |
| Q | `0xac40fa50b81b4ca6b1...` | not initialized |
| R | `0x7ce605cc8fda4f8e4a...` | not initialized |
| S | `0xb8753014e4888ea48a...` | not initialized |
| T | `0x35781dc0e42fef3f25...` | not initialized |
| U | `0x75860da47565f6509b...` | not initialized |
| V | `0xb59dd8170321dfab5a...` | not initialized |
| W | `0x5f32aef70f5ba530d3...` | not initialized |
| X | `0xa95cbbd116548ac990...` | not initialized |
| Y | `0xd8e32848f1dffa811b...` | not initialized |
| Z | `0x7af0ef6e1bd706f4b3...` | not initialized |
| alice | `0xc793acdec12b4a6371...` | not initialized |
| bob | `0x0a3c00c58fdf9020b2...` | not initialized |

### Multisig Contract Probes
| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | `0x0da4f428a0c007da0f...` | 2 | ✓ HEALTHY |
| A-G | `0xf56c4a1c0906214f3f...` | 2 | ✓ HEALTHY |
| Y-Z | `0xd3ffe1812b2df40622...` | 2 | ✓ HEALTHY |
| S-T | `0x3b1c3ae905d44c3a49...` | 2 | ✓ HEALTHY |
| V-W | `0x40fad7b423a843650f...` | 2 | ✓ HEALTHY |

All 5 multisig contracts respond with **2-of-2** signature requirement — all healthy.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` returns HTTP 401 "Protected deployment" (password-protected Vercel preview). No market data extractable.

---

## DuckDB Summary

| Table | Rows |
|-------|------|
| world_increments | 345 |
| repo_snapshots | 1266 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (unavailability record) |

Database: `packages/world-increment/ducklake/world-increments.duckdb`
