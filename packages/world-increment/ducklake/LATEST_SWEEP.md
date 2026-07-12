# World-Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-07-12 17:12 UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Job 1: GitHub Social Graph Sweep

### Repository Sources

| Source | Repos |
|--------|-------|
| plurigrid | 250 |
| bmorphism | 212 |
| TeglonLabs | 111 |
| kubeflow | 106 |
| AustinCStone | 86 |
| wasita | 60 |
| migalkin | 60 |
| zubyul | 56 |
| kristinezheng | 36 |
| M1shaaa | 32 |
| DJedamski | 22 |

**Total repos snapshotted:** 1031

### Top 10 Repos by Stars

| Repository | Stars | Language |
|---|---|---|
| kubeflow/kubeflow | 15772 | N/A |
| kubeflow/kubeflow | 15572 | N/A |
| kubeflow/kubeflow | 15565 | N/A |
| kubeflow/pipelines | 4169 | Python |
| kubeflow/pipelines | 4119 | Python |
| kubeflow/pipelines | 4119 | Python |
| kubeflow/spark-operator | 3137 | Python |
| kubeflow/spark-operator | 3114 | Python |
| kubeflow/spark-operator | 3111 | Python |
| kubeflow/trainer | 2137 | Go |

### GF(3) Color Chain Distribution

| GF3 Name | Color | Count |
|---|---|---|
| PLUS | `#b8bb26` | 37 |
| MINUS | `#cc241d` | 37 |
| ERGODIC | `#d3869b` | 36 |

---

## Job 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

**Total APT across swarm:** `20.344773 APT`

| World | Address | Balance (APT) |
|-------|---------|---------------|
| A | `0x8699edc0960dd5...` | 0.051767 |
| B | `0x3f892ebe6e4516...` | 0.036256 |
| C | `0x38b99e63ada9b6...` | 0.010185 |
| D | `0xf77656248f64d5...` | 0.011629 |
| E | `0xdc1d9d533bac35...` | 0.009372 |
| F | `0x18a14b5b4bec11...` | 1.960516 |
| G | `0x69a394c0b0ac84...` | 0.000681 |
| H | `0xce67c327a7844e...` | 0.001681 |
| I | `0x070fe5d74e4eda...` | 0.000681 |
| J | `0x4d964db8f53837...` | 1.895093 |
| K | `0xa732040a6b0d55...` | 0.161961 |
| L | `0x7c2eaeafad9725...` | 1.927269 |
| M | `0x6fed37a7553ef1...` | 0.112285 |
| N | `0xe7dde6da0a65f5...` | 0.106121 |
| O | `0x73252b6011a751...` | 0.210136 |
| P | `0x6218792de4a9bc...` | 0.140136 |
| Q | `0xac40fa50b81b4c...` | 0.103240 |
| R | `0x7ce605cc8fda4f...` | 0.090217 |
| S | `0xb8753014e4888e...` | 0.091788 |
| T | `0x35781dc0e42fef...` | 0.073713 |
| U | `0x75860da47565f6...` | 0.055773 |
| V | `0xb59dd8170321df...` | 0.048833 |
| W | `0x5f32aef70f5ba5...` | 0.040705 |
| X | `0xa95cbbd116548a...` | 0.042577 |
| Y | `0xd8e32848f1dffa...` | 0.044449 |
| Z | `0x7af0ef6e1bd706...` | 0.024268 |
| alice | `0xc793acdec12b4a...` | 0.436434 |
| bob | `0x0a3c00c58fdf90...` | 12.657007 |

### Notable Balances

| World | APT |
|---|---|
| bob | 12.657007 |
| F | 1.960516 |
| L | 1.927269 |
| J | 1.895093 |
| alice | 0.436434 |
| O | 0.210136 |
| K | 0.161961 |
| P | 0.140136 |
| M | 0.112285 |
| N | 0.106121 |
| Q | 0.103240 |

### Multisig Contract Probes (5 pairs)

| Pair | Address | Sigs Required | Healthy |
|---|---|---|---|
| A-B | `0x0da4f428a0c007da0f...` | 2 | ✓ |
| A-G | `0xf56c4a1c0906214f3f...` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b2df40622...` | 2 | ✓ |
| S-T | `0x3b1c3ae905d44c3a49...` | 2 | ✓ |
| V-W | `0x40fad7b423a843650f...` | 2 | ✓ |

All 5 multisig contracts are **healthy** (sigs_required=2).

### MNX Markets (testnet.mnx.fi)

Status: **401 Unauthorized** — API requires authentication, data unavailable.

---

## Schema

```sql
world_increments   -- GF(3) color-chained event log
repo_snapshots     -- GitHub repo metadata snapshots  
aptos_snapshots    -- Aptos wallet balances
multisig_probes    -- Multisig contract health checks
mnx_snapshots      -- MNX market data (empty - auth required)
```
