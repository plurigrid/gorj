# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-04-11 15:21 UTC
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Coverage

| Source | Type | Repos | Total Stars | Latest Push |
|--------|------|-------|-------------|-------------|
| kubeflow | org | 47 | 33,853 | 2026-04-11 |
| bmorphism | user | 100 | 131 | 2026-04-09 |
| plurigrid | org | 98 | 62 | 2026-04-11 |
| TeglonLabs | org | 53 | 6 | 2026-01-16 |
| AustinCStone | user | 43 | 108 | 2026-02-11 |
| migalkin | user | 30 | 277 | 2025-08-04 |
| wasita | user | 29 | 3 | 2026-04-08 |
| kristinezheng | user | 18 | 0 | 2026-04-09 |
| M1shaaa | user | 16 | 0 | 2026-04-11 |
| DJedamski | user | 11 | 7 | 2018-03-07 |
| zubyul | user | 24 | 13 | 2026-04-09 |
| **TOTAL** | | **469** | **34,460** | |

### Top Repos by Stars
- `kubeflow/kubeflow` — 15,566★ Python — Machine Learning Toolkit for Kubernetes
- `kubeflow/pipelines` — 4,119★ Python — Machine Learning Pipelines for Kubeflow
- `kubeflow/spark-operator` — 3,111★ Python
- `kubeflow/trainer` — 2,080★ Go — Distributed ML Training and Fine-Tuning on Kubernetes
- `kubeflow/katib` — 1,676★ Go — Kubernetes Native AutoML
- `migalkin/NodePiece` — 143★ Python — Inductive Entity Representations from Text

### GF(3) Color Chain Distribution (world_increments)
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 13 |
| 1 | `#b8bb26` | PLUS | 14 |
| -1 | `#cc241d` | MINUS | 14 |

### Recent Events (zubyul)
30 public events captured today (2026-04-11), all on `plurigrid/gorj` and `plurigrid/horse`:
- 14× PullRequestEvent
- 14× CreateEvent
- 2× PushEvent

*Active rapid-iteration PR workflow observed across plurigrid/gorj throughout the day.*

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (28 addresses: alice, bob, A–Z)

All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<AptosCoin>`.
These accounts have not been initialized on Aptos mainnet — **all balances: 0.0 APT**.

| Label | Address | Balance |
|-------|---------|---------|
| alice | 0xc793...cc7b | 0.0 APT |
| bob | 0x0a3c...2d5d | 0.0 APT |
| A–Z | (26 addresses) | 0.0 APT each |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **healthy** (2-of-N threshold):

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...003 | 2 | HEALTHY |
| A-G | 0xf56c...096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...883 | 2 | HEALTHY |
| S-T | 0x3b1c...883 | 2 | HEALTHY |
| V-W | 0x40fa...b6d | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status: DATA UNAVAILABLE** — testnet.mnx.fi is a Next.js SPA. No JSON REST API
endpoints were found at `/api/markets`, `/api/v1/markets`, `/api/v2/markets`.
HTTP 200 returned for HTML pages only; no machine-readable market data extracted.

---

## DuckDB Schema Summary

```
world_increments   : 52 rows  (org sweeps + events, GF3 color-coded)
repo_snapshots     : 469 rows (full repo metadata snapshot)
aptos_snapshots    : 28 rows  (hamming swarm wallets alice,bob,A-Z)
multisig_probes    : 5 rows   (A-B, A-G, Y-Z, S-T, V-W — all healthy)
mnx_snapshots      : 1 row    (unavailable — SPA with no public API)
```
