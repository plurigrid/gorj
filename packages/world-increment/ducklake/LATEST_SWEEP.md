# World Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-06-20 08:10:33 UTC

---

## JOB 1: GitHub Social Graph Sweep

### Summary
- **Total repos snapshotted:** 391
- **Sources:** 11 orgs/users
- **DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| AustinCStone | social | 40 |
| DJedamski | social | 6 |
| M1shaaa | social | 8 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| kristinezheng | social | 5 |
| kubeflow | org | 48 |
| migalkin | social | 19 |
| plurigrid | org | 100 |
| wasita | social | 11 |
| zubyul | user | 49 |

**Total:** 391 repos

### Top Starred Repos

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15736 | N/A |
| kubeflow/pipelines | 4154 | Python |
| kubeflow/spark-operator | 3127 | Python |
| kubeflow/trainer | 2117 | Go |
| kubeflow/katib | 1683 | Python |
| kubeflow/examples | 1460 | Jsonnet |
| kubeflow/community-distribution | 1025 | YAML |
| kubeflow/arena | 813 | Go |
| kubeflow/kale | 694 | Python |
| kubeflow/mpi-operator | 528 | Go |

### Most Recently Pushed

| Repo | Pushed At |
|------|-----------|
| kubeflow/dashboard | 2026-06-20T07:59:44Z |
| kubeflow/pipelines | 2026-06-20T07:29:44Z |
| plurigrid/gorj | 2026-06-20T07:12:06Z |
| kubeflow/pipelines-components | 2026-06-20T03:06:51Z |
| kubeflow/sdk | 2026-06-20T03:05:26Z |

### GF(3) Color Chain Distribution

| GF3 Name | Color | Count |
|----------|-------|-------|
| ERGODIC | #d3869b | 130 |
| MINUS | #cc241d | 130 |
| PLUS | #b8bb26 | 131 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)

All wallets queried on Aptos mainnet at 2026-06-20 08:10:33 UTC.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| A | `0x8699edc0960dd5b916...` | 0.00000000 |
| B | `0x3f892ebe6e45164e63...` | 0.00000000 |
| C | `0x38b99e63ada9b6fef1...` | 0.00000000 |
| D | `0xf77656248f64d5dd00...` | 0.00000000 |
| E | `0xdc1d9d533bac3507f9...` | 0.00000000 |
| F | `0x18a14b5b4bec118c1c...` | 0.00000000 |
| G | `0x69a394c0b0ac842127...` | 0.00000000 |
| H | `0xce67c327a7844e5488...` | 0.00000000 |
| I | `0x070fe5d74e4eda30e2...` | 0.00000000 |
| J | `0x4d964db8f538374034...` | 0.00000000 |
| K | `0xa732040a6b0d559041...` | 0.00000000 |
| L | `0x7c2eaeafad9725492e...` | 0.00000000 |
| M | `0x6fed37a7553ef16b2a...` | 0.00000000 |
| N | `0xe7dde6da0a65f51062...` | 0.00000000 |
| O | `0x73252b6011a75115a2...` | 0.00000000 |
| P | `0x6218792de4a9bc3891...` | 0.00000000 |
| Q | `0xac40fa50b81b4ca6b1...` | 0.00000000 |
| R | `0x7ce605cc8fda4f8e4a...` | 0.00000000 |
| S | `0xb8753014e4888ea48a...` | 0.00000000 |
| T | `0x35781dc0e42fef3f25...` | 0.00000000 |
| U | `0x75860da47565f6509b...` | 0.00000000 |
| V | `0xb59dd8170321dfab5a...` | 0.00000000 |
| W | `0x5f32aef70f5ba530d3...` | 0.00000000 |
| X | `0xa95cbbd116548ac990...` | 0.00000000 |
| Y | `0xd8e32848f1dffa811b...` | 0.00000000 |
| Z | `0x7af0ef6e1bd706f4b3...` | 0.00000000 |
| alice | `0xc793acdec12b4a6371...` | 0.00000000 |
| bob | `0x0a3c00c58fdf9020b2...` | 0.00000000 |

> **Note:** All wallets returned 0 APT — accounts may be unfunded or lack a registered CoinStore resource on mainnet.

### Multisig Contract Probes (5 contracts)

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | `0x0da4f428a0c007da0f...` | 2 | YES |
| A-G | `0xf56c4a1c0906214f3f...` | 2 | YES |
| Y-Z | `0xd3ffe1812b2df40622...` | 2 | YES |
| S-T | `0x3b1c3ae905d44c3a49...` | 2 | YES |
| V-W | `0x40fad7b423a843650f...` | 2 | YES |

> **All 5 multisig contracts healthy** (2-of-2 threshold each): A-B, A-G, Y-Z, S-T, V-W

### MNX Markets (testnet.mnx.fi)

**Status:** UNAVAILABLE — requires Vercel deployment protection bypass token.

---

## DuckDB Schema

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 391 | GF(3)-tagged repo events (ERGODIC/PLUS/MINUS) |
| `repo_snapshots` | 391 | Full repo metadata (stars, forks, language, pushed_at) |
| `aptos_snapshots` | 28 | Hamming swarm wallet balances |
| `multisig_probes` | 5 | Multisig contract health checks |
| `mnx_snapshots` | 1 | MNX market data (unavailable this run) |
