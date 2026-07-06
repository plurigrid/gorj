# LATEST_SWEEP — World Increment + Hamming Swarm Snapshot

**Timestamp:** 2026-07-06 15:11:29 UTC

---

## JOB 1: GitHub Social Graph Sweep

### Overview

| Metric | Value |
|--------|-------|
| Total world-increments recorded | 415 |
| Total repo snapshots | 1336 |
| Sources covered | 11 (3 orgs + 8 users) |

### Repo Counts by Source

| Source | Repos |
|--------|-------|
| plurigrid | 300 |
| bmorphism | 300 |
| kubeflow | 143 |
| AustinCStone | 126 |
| TeglonLabs | 111 |
| zubyul | 97 |
| migalkin | 79 |
| wasita | 71 |
| kristinezheng | 41 |
| M1shaaa | 40 |
| DJedamski | 28 |

### Top Repos by Stars

| Source | Repo | Stars | Forks | Language |
|--------|------|-------|-------|----------|
| kubeflow | kubeflow | 15766 | 2683 | - |
| kubeflow | kubeflow | 15572 | 2633 | - |
| kubeflow | kubeflow | 15565 | 2626 | - |
| kubeflow | pipelines | 4169 | 2024 | Python |
| kubeflow | pipelines | 4119 | 1984 | Python |
| kubeflow | pipelines | 4119 | 1985 | Python |
| kubeflow | spark-operator | 3132 | 1497 | Python |
| kubeflow | spark-operator | 3114 | 1483 | Python |
| kubeflow | spark-operator | 3111 | 1483 | Python |
| kubeflow | trainer | 2129 | 978 | Go |
| kubeflow | trainer | 2082 | 945 | Go |
| kubeflow | trainer | 2080 | 944 | Go |
| kubeflow | katib | 1690 | 530 | Python |
| kubeflow | katib | 1678 | 521 | Python |
| kubeflow | katib | 1676 | 521 | Python |

### GF(3) Color Chain Distribution

| Name | Color | Count |
|------|-------|-------|
| PLUS | #b8bb26 | 139 |
| MINUS | #cc241d | 138 |
| ERGODIC | #d3869b | 138 |

GF(3) mapping: `id%3==0` → trit=0 ERGODIC #d3869b | `id%3==1` → trit=1 PLUS #b8bb26 | `id%3==2` → trit=-1 MINUS #cc241d

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (26 addresses A–Z + alice + bob)

All 28 addresses returned HTTP 404 from `fullnode.mainnet.aptoslabs.com`, indicating these wallets have not yet registered an AptosCoin store (uninitialized accounts). This is expected for newly generated addresses that have never received a transaction.

| World | Address (truncated) | Status |
|-------|---------------------|--------|
| A | `0x8699edc0960dd5b916...` | 404 (unregistered) |
| B | `0x3f892ebe6e45164e63...` | 404 (unregistered) |
| C | `0x38b99e63ada9b6fef1...` | 404 (unregistered) |
| D | `0xf77656248f64d5dd00...` | 404 (unregistered) |
| E | `0xdc1d9d533bac3507f9...` | 404 (unregistered) |
| F | `0x18a14b5b4bec118c1c...` | 404 (unregistered) |
| G | `0x69a394c0b0ac842127...` | 404 (unregistered) |
| H | `0xce67c327a7844e5488...` | 404 (unregistered) |
| I | `0x070fe5d74e4eda30e2...` | 404 (unregistered) |
| J | `0x4d964db8f538374034...` | 404 (unregistered) |
| K | `0xa732040a6b0d559041...` | 404 (unregistered) |
| L | `0x7c2eaeafad9725492e...` | 404 (unregistered) |
| M | `0x6fed37a7553ef16b2a...` | 404 (unregistered) |
| N | `0xe7dde6da0a65f51062...` | 404 (unregistered) |
| O | `0x73252b6011a75115a2...` | 404 (unregistered) |
| P | `0x6218792de4a9bc3891...` | 404 (unregistered) |
| Q | `0xac40fa50b81b4ca6b1...` | 404 (unregistered) |
| R | `0x7ce605cc8fda4f8e4a...` | 404 (unregistered) |
| S | `0xb8753014e4888ea48a...` | 404 (unregistered) |
| T | `0x35781dc0e42fef3f25...` | 404 (unregistered) |
| U | `0x75860da47565f6509b...` | 404 (unregistered) |
| V | `0xb59dd8170321dfab5a...` | 404 (unregistered) |
| W | `0x5f32aef70f5ba530d3...` | 404 (unregistered) |
| X | `0xa95cbbd116548ac990...` | 404 (unregistered) |
| Y | `0xd8e32848f1dffa811b...` | 404 (unregistered) |
| Z | `0x7af0ef6e1bd706f4b3...` | 404 (unregistered) |
| alice | `0xc793acdec12b4a6371...` | 404 (unregistered) |
| bob | `0x0a3c00c58fdf9020b2...` | 404 (unregistered) |

### Multisig Contract Probes

All 5 multisig contracts are **healthy** with 2 signatures required.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | `0x0da4f428a0c007da0f7629c3ec6a...` | 2 | ✓ |
| A-G | `0xf56c4a1c0906214f3f859ccd8b49...` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b2df4062281c7ddd502...` | 2 | ✓ |
| S-T | `0x3b1c3ae905d44c3a49f0dedd918a...` | 2 | ✓ |
| V-W | `0x40fad7b423a843650fddcad36b7d...` | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

Status: **401 Unauthorized** — all API endpoints (`/api/markets`, `/api/v1/markets`, `/markets`, `/api/tickers`) require authentication. The testnet appears to be gated; no market data could be retrieved without credentials.

---

## DuckDB Schema

Database: `packages/world-increment/ducklake/world-increments.duckdb`

Tables:
- `world_increments` — GF(3)-annotated event log (415 rows)
- `repo_snapshots` — GitHub repo metadata (1336 rows)
- `aptos_snapshots` — Aptos wallet balances (28 rows)
- `multisig_probes` — Multisig contract health (5 rows)
- `mnx_snapshots` — MNX market data (1 row, unavailable)

Sequences: `increment_seq`, `repo_seq`
