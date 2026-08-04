# World Increment + Hamming Swarm Sweep — 2026-08-04

## Run Summary

- **Timestamp**: 2026-08-04 UTC
- **DuckDB**: `packages/world-increment/ducklake/world-increments.duckdb`
- **Total world_increments**: 280 (cumulative)
- **Repos snapshotted this run**: 257
- **Aptos addresses probed**: 28
- **Multisig contracts probed**: 5

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Repos | Note |
|--------|-------|------|
| plurigrid | 100 | Org (first 100 by pushed) |
| zubyul | 49 | User |
| bmorphism | 50 | User |
| kubeflow | 30 | Org |
| TeglonLabs | 5 | Org |
| migalkin | 6 | Social graph |
| wasita | 5 | Social graph |
| AustinCStone | 4 | Social graph |
| M1shaaa | 3 | Social graph |
| DJedamski | 3 | Social graph |
| kristinezheng | 2 | Social graph |
| **Total** | **257** | |

### Top Starred Repos (This Run)

┌─────────────────────────┬───────┬──────────┐
│        full_name        │ stars │ language │
│         varchar         │ int32 │ varchar  │
├─────────────────────────┼───────┼──────────┤
│ kubeflow/kubeflow       │ 15804 │ NULL     │
│ kubeflow/kubeflow       │ 15572 │ NULL     │
│ kubeflow/kubeflow       │ 15565 │          │
│ kubeflow/pipelines      │  4173 │ Python   │
│ kubeflow/pipelines      │  4119 │ Python   │
│ kubeflow/pipelines      │  4119 │ Python   │
│ kubeflow/spark-operator │  3142 │ Python   │
│ kubeflow/spark-operator │  3114 │ Python   │
│ kubeflow/spark-operator │  3111 │ Python   │
│ kubeflow/trainer        │  2165 │ Go       │
└─────────────────────────┴───────┴──────────┘
  10 rows                          3 columns

### GF(3) Color Chain Distribution

┌──────────┬───────────┬──────────────┐
│ gf3_name │ gf3_color │ count_star() │
│ varchar  │  varchar  │    int64     │
├──────────┼───────────┼──────────────┤
│ #b8bb26  │ PLUS      │           86 │
│ #cc241d  │ MINUS     │           86 │
│ #d3869b  │ ERGODIC   │           85 │
│ ERGODIC  │ #d3869b   │            7 │
│ MINUS    │ #cc241d   │            8 │
│ PLUS     │ #b8bb26   │            8 │
└──────────┴───────────┴──────────────┘

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 Hamming swarm addresses returned `resource_not_found` — wallets exist on-chain but
have no initialized APT CoinStore resource. This indicates zero APT balance for all members.

| World | Status |
|-------|--------|
| alice–Z (all 28) | `resource_not_found` (0.000 APT) |

### Multisig Contract Probes (5 pairs)

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

All 5 multisig contracts are **healthy** with **2-of-N signatures required**.

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — endpoint returned HTML SPA (no JSON API accessible). Market data
could not be extracted; recorded as placeholder in `mnx_snapshots` table.

---

## DuckDB Schema State

| Table | Rows |
|-------|------|
| world_increments | 280 |
| repo_snapshots | 1201 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

## Notable Observations

- **TeglonLabs/jank-crane** (2026-06-08): C++ repo describing GF3 convergence maps — directly
  related to the GF(3) color chain used in this sweep
- **migalkin/NodePiece** (144 stars): highest-starred social graph repo; compositional KG embeddings
- **AustinCStone/TextGAN** (92 stars): TF text generation GAN, still active references
- **wasita/wasita.github.io** (pushed 2026-07-21): most recently updated social graph repo
- **All Hamming wallets**: zero balance — either test/placeholder addresses or funds exhausted
- **Multisig health**: 5/5 contracts responsive, all requiring 2 signatures (standard 2-of-N)
