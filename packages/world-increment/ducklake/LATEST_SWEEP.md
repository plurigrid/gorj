# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-18 07:12 UTC
**Sweep Date:** 2026-07-18

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org/user | 100 |
| bmorphism | org/user | 100 |
| kubeflow | org/user | 49 |
| zubyul | org/user | 49 |
| AustinCStone | org/user | 41 |
| migalkin | org/user | 19 |
| wasita | org/user | 12 |
| M1shaaa | org/user | 8 |
| DJedamski | org/user | 6 |
| TeglonLabs | org/user | 5 |
| kristinezheng | org/user | 5 |

**Total repos:** 394 across 11 sources

### GF(3) Color Chain Distribution
| Trit | Color | Name | Count |
|------|-------|------|-------|
| - | #d3869b | ERGODIC | 131 |
| - | #cc241d | MINUS | 131 |
| - | #b8bb26 | PLUS | 132 |

### Top 10 Repos by Stars
| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | N/A | 15780 | 2026-07-10 |
| kubeflow/pipelines | Python | 4168 | 2026-07-17 |
| kubeflow/spark-operator | Python | 3139 | 2026-07-17 |
| kubeflow/trainer | Go | 2151 | 2026-07-18 |
| kubeflow/katib | Python | 1691 | 2026-07-16 |
| kubeflow/examples | Jsonnet | 1460 | 2025-04-14 |
| kubeflow/community-distribution | YAML | 1029 | 2026-07-17 |
| kubeflow/arena | Go | 815 | 2026-07-17 |
| kubeflow/kale | Python | 696 | 2026-07-16 |
| kubeflow/mpi-operator | Go | 530 | 2026-07-13 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
**Status:** All 28 addresses queried. CoinStore resource not found for any address
(accounts may be uninitialized or non-existent on mainnet).

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| A | 0x8699edc0960dd5b916... | NOT FOUND |
| B | 0x3f892ebe6e45164e63... | NOT FOUND |
| C | 0x38b99e63ada9b6fef1... | NOT FOUND |
| D | 0xf77656248f64d5dd00... | NOT FOUND |
| E | 0xdc1d9d533bac3507f9... | NOT FOUND |
| F | 0x18a14b5b4bec118c1c... | NOT FOUND |
| G | 0x69a394c0b0ac842127... | NOT FOUND |
| H | 0xce67c327a7844e5488... | NOT FOUND |
| I | 0x070fe5d74e4eda30e2... | NOT FOUND |
| J | 0x4d964db8f538374034... | NOT FOUND |
| K | 0xa732040a6b0d559041... | NOT FOUND |
| L | 0x7c2eaeafad9725492e... | NOT FOUND |
| M | 0x6fed37a7553ef16b2a... | NOT FOUND |
| N | 0xe7dde6da0a65f51062... | NOT FOUND |
| O | 0x73252b6011a75115a2... | NOT FOUND |
| P | 0x6218792de4a9bc3891... | NOT FOUND |
| Q | 0xac40fa50b81b4ca6b1... | NOT FOUND |
| R | 0x7ce605cc8fda4f8e4a... | NOT FOUND |
| S | 0xb8753014e4888ea48a... | NOT FOUND |
| T | 0x35781dc0e42fef3f25... | NOT FOUND |
| U | 0x75860da47565f6509b... | NOT FOUND |
| V | 0xb59dd8170321dfab5a... | NOT FOUND |
| W | 0x5f32aef70f5ba530d3... | NOT FOUND |
| X | 0xa95cbbd116548ac990... | NOT FOUND |
| Y | 0xd8e32848f1dffa811b... | NOT FOUND |
| Z | 0x7af0ef6e1bd706f4b3... | NOT FOUND |
| alice | 0xc793acdec12b4a6371... | NOT FOUND |
| bob | 0x0a3c00c58fdf9020b2... | NOT FOUND |

### Multisig Contract Probes
All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428a0c007da0f... | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a1c0906214f3f... | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3ae905d44c3a49... | 2 | ✓ HEALTHY |
| V-W | 0x40fad7b423a843650f... | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe1812b2df40622... | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)
**Status:** UNAVAILABLE — SPA returns HTML only; no REST API endpoint found.
Attempted: `/api/markets`, `/api/v1/markets`, `/api/tickers`. All return the SPA shell.

---

## DuckDB Summary

Database: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 394 |
| repo_snapshots | 394 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |
