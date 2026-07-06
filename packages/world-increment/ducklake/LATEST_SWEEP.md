# LATEST_SWEEP — 2026-07-06

## GitHub Social Graph Sweep

**Sources swept:** plurigrid (org), kubeflow (org), TeglonLabs (org), bmorphism (user), zubyul (user)  
**Social graph:** migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone

### DuckDB Stats
| Table | Rows |
|-------|------|
| world_increments | 344 |
| repo_snapshots | 1265 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |

### Repos by Source (world_increments)
| Source | Increments |
|--------|-----------|
| bmorphism | 103 |
| plurigrid | 102 |
| zubyul | 51 |
| kubeflow | 51 |
| TeglonLabs | 7 |
| migalkin | 7 |
| DJedamski | 5 |
| wasita | 5 |
| AustinCStone | 5 |
| kristinezheng | 4 |
| M1shaaa | 4 |

### GF(3) Color Chain Distribution
| Trit | Name | Color | Count |
|------|------|-------|-------|
| -1 | MINUS | #cc241d | 115 |
| 0 | ERGODIC | #d3869b | 114 |
| 1 | PLUS | #b8bb26 | 115 |

### Top Repos by Stars
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15766 | N/A |
| kubeflow/kubeflow | 15572 | N/A |
| kubeflow/kubeflow | 15565 | N/A |
| kubeflow/pipelines | 4169 | Python |
| kubeflow/pipelines | 4119 | Python |
| kubeflow/pipelines | 4119 | Python |
| kubeflow/spark-operator | 3132 | Python |
| kubeflow/spark-operator | 3114 | Python |
| kubeflow/spark-operator | 3111 | Python |
| kubeflow/trainer | 2129 | Go |

---

## Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (A–Z + alice/bob)
All 28 addresses returned `resource_not_found` — accounts exist on-chain but have no APT CoinStore registered (unfunded on mainnet).

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| A | 0x8699edc0960dd5...be9d7a | 0.0000 |
| B | 0x3f892ebe6e4516...77cb13 | 0.0000 |
| C | 0x38b99e63ada9b6...91535e | 0.0000 |
| D | 0xf77656248f64d5...fcfdd1 | 0.0000 |
| E | 0xdc1d9d533bac35...958d36 | 0.0000 |
| F | 0x18a14b5b4bec11...c3cf71 | 0.0000 |
| G | 0x69a394c0b0ac84...cc7f32 | 0.0000 |
| H | 0xce67c327a7844e...e5300f | 0.0000 |
| I | 0x070fe5d74e4eda...0c1fc9 | 0.0000 |
| J | 0x4d964db8f53837...e87f54 | 0.0000 |
| K | 0xa732040a6b0d55...425dc4 | 0.0000 |
| L | 0x7c2eaeafad9725...37eba9 | 0.0000 |
| M | 0x6fed37a7553ef1...b7f2e9 | 0.0000 |
| N | 0xe7dde6da0a65f5...551b2c | 0.0000 |
| O | 0x73252b6011a751...25a89d | 0.0000 |
| P | 0x6218792de4a9bc...1ec948 | 0.0000 |
| Q | 0xac40fa50b81b4c...5c89a9 | 0.0000 |
| R | 0x7ce605cc8fda4f...d76e10 | 0.0000 |
| S | 0xb8753014e4888e...9d0386 | 0.0000 |
| T | 0x35781dc0e42fef...3f4588 | 0.0000 |
| U | 0x75860da47565f6...ef9956 | 0.0000 |
| V | 0xb59dd8170321df...9af2c3 | 0.0000 |
| W | 0x5f32aef70f5ba5...ccc7b0 | 0.0000 |
| X | 0xa95cbbd116548a...33047d | 0.0000 |
| Y | 0xd8e32848f1dffa...2444c4 | 0.0000 |
| Z | 0x7af0ef6e1bd706...4e197c | 0.0000 |
| alice | 0xc793acdec12b4a...24cc7b | 0.0000 |
| bob | 0x0a3c00c58fdf90...512d5d | 0.0000 |

### Multisig Contract Probes (5 pairs)
| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f428a0c007...987003 | 2 | ✓ |
| A-G | 0xf56c4a1c090621...bc0096 | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df4...75b883 | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c...ed7883 | 2 | ✓ |
| V-W | 0x40fad7b423a843...80eb6d | 2 | ✓ |

**All 5 multisig contracts require 2-of-N signatures and are healthy.**

### MNX Markets (testnet.mnx.fi)
Status: **Unavailable** — all API paths return the SPA shell HTML (no JSON market data exposed via API). Data not persisted.

---

## Notes
- DuckDB: `packages/world-increment/ducklake/world-increments.duckdb`
- GF(3) color chain: `id%3==0` → ERGODIC (#d3869b), `id%3==1` → PLUS (#b8bb26), `id%3==2` → MINUS (#cc241d)
- Aptos resource_not_found indicates accounts have no registered CoinStore (not yet funded)
- MNX testnet is SPA-only; no REST/GraphQL API accessible at known endpoints
