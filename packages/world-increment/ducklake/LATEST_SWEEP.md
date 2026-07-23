# World-Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-07-23T13:13:59Z
**Increment ID:** 12  |  **GF3:** trit=0 ERGODIC `#d3869b`
**DB version:** world-increments.duckdb

---

## JOB 1: GitHub Social Graph

**Total repos snapshotted:** 1263  |  **Total increments in DB:** 24

### Sources Swept
| Source | Type | Notes |
|--------|------|-------|
| plurigrid | org | 100 repos |
| kubeflow | org | 49 repos |
| TeglonLabs | org | 5 repos incl. jank-crane (GF3) |
| bmorphism | user | 100 repos |
| zubyul | user | 49 repos |
| migalkin | social-graph | KG/GNN researcher, 19 repos |
| DJedamski | social-graph | data science, 6 repos |
| wasita | social-graph | active (last push 2026-07-21), 12 repos |
| kristinezheng | social-graph | MIT cog-sci, 5 repos |
| M1shaaa | social-graph | Yale, 8 repos |
| AustinCStone | social-graph | ML/vision, 41 repos |

### Top 10 Repos by Stars
| Rank | Org/User | Repo | Stars |
|------|----------|------|-------|
| 1 | kubeflow | kubeflow | 15789 |
| 2 | kubeflow | kubeflow | 15572 |
| 3 | kubeflow | kubeflow | 15565 |
| 4 | kubeflow | pipelines | 4169 |
| 5 | kubeflow | pipelines | 4119 |
| 6 | kubeflow | pipelines | 4119 |
| 7 | kubeflow | spark-operator | 3143 |
| 8 | kubeflow | spark-operator | 3114 |
| 9 | kubeflow | spark-operator | 3111 |
| 10 | kubeflow | trainer | 2153 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

**Wallets queried:** 28/28 reachable  |  **Ledger version:** 6,416,500,342
**Status:** All accounts exist on-chain; CoinStore not initialized (zero APT balances)
**Total APT across swarm:** 0.000000 APT

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | `0xc793acdec12b4a6371...` | 0.000000 |
| bob | `0x0a3c00c58fdf9020b2...` | 0.000000 |
| A | `0x8699edc0960dd5b916...` | 0.000000 |
| B | `0x3f892ebe6e45164e63...` | 0.000000 |
| C | `0x38b99e63ada9b6fef1...` | 0.000000 |
| D | `0xf77656248f64d5dd00...` | 0.000000 |
| E | `0xdc1d9d533bac3507f9...` | 0.000000 |
| F | `0x18a14b5b4bec118c1c...` | 0.000000 |
| G | `0x69a394c0b0ac842127...` | 0.000000 |
| H | `0xce67c327a7844e5488...` | 0.000000 |
| I | `0x070fe5d74e4eda30e2...` | 0.000000 |
| J | `0x4d964db8f538374034...` | 0.000000 |
| K | `0xa732040a6b0d559041...` | 0.000000 |
| L | `0x7c2eaeafad9725492e...` | 0.000000 |
| M | `0x6fed37a7553ef16b2a...` | 0.000000 |
| N | `0xe7dde6da0a65f51062...` | 0.000000 |
| O | `0x73252b6011a75115a2...` | 0.000000 |
| P | `0x6218792de4a9bc3891...` | 0.000000 |
| Q | `0xac40fa50b81b4ca6b1...` | 0.000000 |
| R | `0x7ce605cc8fda4f8e4a...` | 0.000000 |
| S | `0xb8753014e4888ea48a...` | 0.000000 |
| T | `0x35781dc0e42fef3f25...` | 0.000000 |
| U | `0x75860da47565f6509b...` | 0.000000 |
| V | `0xb59dd8170321dfab5a...` | 0.000000 |
| W | `0x5f32aef70f5ba530d3...` | 0.000000 |
| X | `0xa95cbbd116548ac990...` | 0.000000 |
| Y | `0xd8e32848f1dffa811b...` | 0.000000 |
| Z | `0x7af0ef6e1bd706f4b3...` | 0.000000 |

### Multisig Contract Probes

**All 5 multisig contracts healthy** (2-of-2 signature scheme confirmed)

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428a0c007da0f...` | 2 | ✓ |
| A-G | `0xf56c4a1c0906214f3f...` | 2 | ✓ |
| S-T | `0x3b1c3ae905d44c3a49...` | 2 | ✓ |
| V-W | `0x40fad7b423a843650f...` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b2df40622...` | 2 | ✓ |

### MNX Markets

**Status:** unavailable — `testnet.mnx.fi` is a SPA with no accessible REST endpoints at `/api/markets`, `/api/v1/markets`, or `/api/ticker`.

---

## DuckDB Schema (world-increments.duckdb)

| Table | Rows | Description |
|-------|------|-------------|
| world_increments | 24 | GF3 increment log |
| repo_snapshots | 1263 | GitHub repo metadata |
| aptos_snapshots | 28 | Hamming swarm wallet balances |
| multisig_probes | 5 | Multisig contract state |
| mnx_snapshots | 0 | MNX market data (unavailable) |

*Automated sweep — world-increment-sweep + hamming-swarm-snapshot agent*
*GF3 color chain: trit=0 ERGODIC #d3869b | trit=1 PLUS #b8bb26 | trit=-1 MINUS #cc241d*
