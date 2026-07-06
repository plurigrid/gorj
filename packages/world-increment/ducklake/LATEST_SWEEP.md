# World-Increment Sweep + Hamming Snapshot

**Date:** 2026-07-06
**Run type:** world-increment-sweep + hamming-swarm-snapshot

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social graph) | 19 |
| DJedamski | user (social graph) | 6 |
| wasita | user (social graph) | 11 |
| kristinezheng | user (social graph) | 5 |
| M1shaaa | user (social graph) | 8 |
| AustinCStone | user (social graph) | 40 |

**Total repos snapshotted:** 392

### GF(3) Color Chain Assignment

| ID | Source | Trit | Color | Name |
|----|--------|------|-------|------|
| 1 | plurigrid | 1 | #b8bb26 | PLUS |
| 2 | kubeflow | -1 | #cc241d | MINUS |
| 3 | TeglonLabs | 0 | #d3869b | ERGODIC |
| 4 | bmorphism | 1 | #b8bb26 | PLUS |
| 5 | zubyul | -1 | #cc241d | MINUS |
| 6 | migalkin | 0 | #d3869b | ERGODIC |
| 7 | DJedamski | 1 | #b8bb26 | PLUS |
| 8 | wasita | -1 | #cc241d | MINUS |
| 9 | kristinezheng | 0 | #d3869b | ERGODIC |
| 10 | M1shaaa | 1 | #b8bb26 | PLUS |
| 11 | AustinCStone | -1 | #cc241d | MINUS |

### Notable Repos (by Stars)

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | ~15,767 | Jupyter Notebook |
| kubeflow/pipelines | ~4,169 | Python |
| kubeflow/spark-operator | ~3,132 | Go |
| kubeflow/trainer | ~2,129 | Python |
| plurigrid/asi | 28 | HTML |
| TeglonLabs/mathpix-gem | 2 | Ruby |

### Recently Active

- `plurigrid/place` — pushed 2026-07-06 (TeX)
- `plurigrid/shrimp` — pushed 2026-07-03
- `plurigrid/asi` — pushed 2026-06-29 (HTML, 28 stars)
- `TeglonLabs/jank-crane` — pushed 2026-06-08 (C++, GF3 convergence maps)
- `M1shaaa/M1shaaa` — pushed 2026-07-06 (profile config)
- `kristinezheng/kristinezheng.github.io` — pushed 2026-07-01

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A-Z)

All 28 Hamming-swarm addresses returned **0.00 APT** at query time. Accounts appear unfunded on Aptos mainnet or CoinStore resource not initialized.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b | 0.0 |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d | 0.0 |
| A-Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes (5/5 healthy)

All 5 multisig contracts require **2 signatures**.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | healthy |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | healthy |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | healthy |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | healthy |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — endpoint returns Vercel authentication wall. No market data extractable without credentials.

---

## DuckDB Schema Summary

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows | Description |
|-------|------|-------------|
| world_increments | 11 | One GF(3) increment per source |
| repo_snapshots | 392 | All repos across 11 sources |
| aptos_snapshots | 28 | Hamming swarm wallet balances |
| multisig_probes | 5 | Multisig contract health checks |
| mnx_snapshots | 1 | MNX unavailable marker |
