# World Increment Sweep + Hamming Swarm Snapshot
**Generated:** 2026-06-21 17:09 UTC

## JOB 1: GitHub Social Graph Sweep

### Source Coverage

| Source | Repos Snapshotted |
|--------|-------------------|
| bmorphism | 100 |
| plurigrid | 100 |
| zubyul | 49 |
| kubeflow | 48 |
| AustinCStone | 40 |
| migalkin | 19 |
| wasita | 11 |
| M1shaaa | 8 |
| DJedamski | 6 |
| TeglonLabs | 5 |
| kristinezheng | 5 |

**Total:** 391 repositories across plurigrid, kubeflow, TeglonLabs orgs + bmorphism, zubyul users + zubyul social graph (migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone)

### GF(3) Color Chain Distribution

| GF3 State | Color | Count |
|-----------|-------|-------|
| ERGODIC | `#d3869b` | 130 |
| MINUS | `#cc241d` | 130 |
| PLUS | `#b8bb26` | 131 |

### Top Repos by Stars

| Repo | Language | Stars | Forks | Last Pushed |
|------|----------|-------|-------|-------------|
| kubeflow/kubeflow | — | 15738 | 2680 | 2026-06-18 |
| kubeflow/pipelines | Python | 4156 | 2009 | 2026-06-20 |
| kubeflow/spark-operator | Python | 3127 | 1490 | 2026-06-18 |
| kubeflow/trainer | Go | 2118 | 970 | 2026-06-19 |
| kubeflow/katib | Python | 1684 | 528 | 2026-06-20 |
| kubeflow/examples | Jsonnet | 1460 | 756 | 2025-04-14 |
| kubeflow/community-distribution | YAML | 1026 | 1065 | 2026-06-18 |
| kubeflow/arena | Go | 813 | 190 | 2026-05-07 |
| kubeflow/kale | Python | 694 | 155 | 2026-06-20 |
| kubeflow/mpi-operator | Go | 528 | 236 | 2026-06-15 |
| kubeflow/fairing | Jsonnet | 337 | 143 | 2022-04-11 |
| kubeflow/pytorch-operator | Jsonnet | 310 | 143 | 2021-12-01 |
| kubeflow/community | Jupyter Notebook | 194 | 264 | 2026-06-19 |
| kubeflow/website | HTML | 184 | 923 | 2026-06-19 |
| kubeflow/kfctl | Go | 182 | 134 | 2023-08-15 |

### Language Distribution (Top 10)

| Language | Repos |
|----------|-------|
| Python | 80 |
| Rust | 26 |
| JavaScript | 25 |
| TypeScript | 23 |
| HTML | 17 |
| Go | 15 |
| Jupyter Notebook | 14 |
| Clojure | 14 |
| Julia | 9 |
| Jsonnet | 7 |


---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 wallets queried against Aptos mainnet (`fullnode.mainnet.aptoslabs.com`).

**All 28 wallets report 0.0 APT.** Addresses may be inactive, unfunded, or coin stores not initialized.

### Multisig Contract Probes (5 pairs)

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428a0c007...` | 2 | ✓ |
| A-G | `0xf56c4a1c090621...` | 2 | ✓ |
| S-T | `0x3b1c3ae905d44c...` | 2 | ✓ |
| V-W | `0x40fad7b423a843...` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b2df4...` | 2 | ✓ |

All 5 multisig accounts require 2-of-N signatures and are live on mainnet.

### MNX Markets (`testnet.mnx.fi`)

**Status: UNAVAILABLE** — All API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`) return Vercel deployment protection authentication wall. No market data could be fetched.

---

## DuckDB Schema

Tables written to `packages/world-increment/ducklake/world-increments.duckdb`:

| Table | Rows |
|-------|------|
| `world_increments` | 391 |
| `repo_snapshots` | 391 |
| `aptos_snapshots` | 28 |
| `multisig_probes` | 5 |
| `mnx_snapshots` | 0 (unavailable) |
