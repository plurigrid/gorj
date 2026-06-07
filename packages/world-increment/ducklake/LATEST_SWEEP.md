# World-Increment Sweep + Hamming Swarm Snapshot
**Generated:** 2026-06-07T19:11:20Z  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Job 1: GitHub Social Graph Sweep

### Sources Swept
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| DJedamski | user | 6 |
| wasita | user | 11 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| AustinCStone | user | 40 |

**Total repos snapshotted:** 390

### Top 10 Repos by Stars
| Repo | Language | Stars | Forks | Pushed |
|------|----------|-------|-------|--------|
| `kubeflow/kubeflow` | — | 15706 | 2671 | 2026-05-24 |
| `kubeflow/pipelines` | Python | 4153 | 2006 | 2026-06-06 |
| `kubeflow/spark-operator` | Python | 3126 | 1488 | 2026-06-04 |
| `kubeflow/trainer` | Go | 2112 | 964 | 2026-06-05 |
| `kubeflow/katib` | Python | 1685 | 526 | 2026-06-05 |
| `kubeflow/examples` | Jsonnet | 1462 | 756 | 2025-04-14 |
| `kubeflow/manifests` | YAML | 1020 | 1065 | 2026-06-05 |
| `kubeflow/arena` | Go | 811 | 191 | 2026-05-07 |
| `kubeflow/kale` | Python | 691 | 155 | 2026-06-05 |
| `kubeflow/mpi-operator` | Go | 528 | 235 | 2026-06-02 |

### Top Languages
| Language | Count |
|----------|-------|
| Python | 82 |
| Rust | 26 |
| JavaScript | 25 |
| TypeScript | 23 |
| HTML | 15 |
| Go | 15 |
| Clojure | 14 |
| Jupyter Notebook | 14 |
| Julia | 9 |
| Zig | 7 |

### GF(3) Color Chain Distribution
| Trit | Color | Hex | Count |
|------|-------|-----|-------|
| 0 | ERGODIC | #d3869b | 130 |
| 1 | PLUS | #b8bb26 | 130 |
| 2 | MINUS | #cc241d | 130 |

---

## Job 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)
All 28 wallets queried (alice, bob, A–Z). Results from `fullnode.mainnet.aptoslabs.com`.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|--------------|
| alice | `0xc793acdec12b4a6371…` | 0.0 |
| bob | `0x0a3c00c58fdf9020b2…` | 0.0 |
| A | `0x8699edc0960dd5b916…` | 0.0 |
| B | `0x3f892ebe6e45164e63…` | 0.0 |
| C | `0x38b99e63ada9b6fef1…` | 0.0 |
| D | `0xf77656248f64d5dd00…` | 0.0 |
| E | `0xdc1d9d533bac3507f9…` | 0.0 |
| F | `0x18a14b5b4bec118c1c…` | 0.0 |
| G | `0x69a394c0b0ac842127…` | 0.0 |
| H | `0xce67c327a7844e5488…` | 0.0 |
| I | `0x070fe5d74e4eda30e2…` | 0.0 |
| J | `0x4d964db8f538374034…` | 0.0 |
| K | `0xa732040a6b0d559041…` | 0.0 |
| L | `0x7c2eaeafad9725492e…` | 0.0 |
| M | `0x6fed37a7553ef16b2a…` | 0.0 |
| N | `0xe7dde6da0a65f51062…` | 0.0 |
| O | `0x73252b6011a75115a2…` | 0.0 |
| P | `0x6218792de4a9bc3891…` | 0.0 |
| Q | `0xac40fa50b81b4ca6b1…` | 0.0 |
| R | `0x7ce605cc8fda4f8e4a…` | 0.0 |
| S | `0xb8753014e4888ea48a…` | 0.0 |
| T | `0x35781dc0e42fef3f25…` | 0.0 |
| U | `0x75860da47565f6509b…` | 0.0 |
| V | `0xb59dd8170321dfab5a…` | 0.0 |
| W | `0x5f32aef70f5ba530d3…` | 0.0 |
| X | `0xa95cbbd116548ac990…` | 0.0 |
| Y | `0xd8e32848f1dffa811b…` | 0.0 |
| Z | `0x7af0ef6e1bd706f4b3…` | 0.0 |

> Note: All wallets returned 0 APT via `CoinStore` resource query — wallets may be unfunded, or hold APT in a different resource type.

### Multisig Contract Probes
| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | `0x0da4f428…` | 2 | ✓ HEALTHY |
| A-G | `0xf56c4a1c…` | 2 | ✓ HEALTHY |
| Y-Z | `0xd3ffe181…` | 2 | ✓ HEALTHY |
| S-T | `0x3b1c3ae9…` | 2 | ✓ HEALTHY |
| V-W | `0x40fad7b4…` | 2 | ✓ HEALTHY |

All 5 multisig accounts require **2-of-N** signatures and responded successfully.

### MNX Markets (testnet.mnx.fi)
Status: **UNAVAILABLE** — endpoint is behind Vercel deployment protection (auth required). No market data could be extracted.

---

## DuckDB Schema Summary
| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 390 | GF(3)-tagged repo push events |
| `repo_snapshots` | 390 | Full repo metadata per source |
| `aptos_snapshots` | 28 | Wallet balance readings (alice, bob, A–Z) |
| `multisig_probes` | 5 | Multisig sig-threshold results |
| `mnx_snapshots` | 0 | MNX markets (unavailable this sweep) |
