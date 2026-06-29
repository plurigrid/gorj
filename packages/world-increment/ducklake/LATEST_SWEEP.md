# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-29  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured | Total Stars |
|---|---|---|---|
| plurigrid | org | 100 | 78 |
| kubeflow | org | 48 | 34,279 |
| TeglonLabs | org | 5 | 2 |
| bmorphism | user | 100 | 247 |
| zubyul | user | 49 | 14 |
| migalkin | user (social) | 19 | 280 |
| wasita | user (social) | 11 | 5 |
| kristinezheng | user (social) | 5 | 0 |
| M1shaaa | user (social) | 8 | 0 |
| DJedamski | user (social) | 6 | 3 |
| AustinCStone | user (social) | 40 | 108 |
| **TOTAL** | | **391** | **35,016** |

### Top 10 Repos by Stars

| Repo | Stars | Language | Last Pushed |
|---|---|---|---|
| kubeflow/kubeflow | 15,750 | — | 2026-06-18 |
| kubeflow/pipelines | 4,162 | Python | 2026-06-29 |
| kubeflow/spark-operator | 3,129 | Python | 2026-06-29 |
| kubeflow/trainer | 2,127 | Go | 2026-06-26 |
| kubeflow/katib | 1,687 | Python | 2026-06-23 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1,028 | YAML | 2026-06-29 |
| kubeflow/arena | 814 | Go | 2026-06-29 |
| kubeflow/kale | 694 | Python | 2026-06-29 |
| kubeflow/mpi-operator | 528 | Go | 2026-06-29 |

### Notable Recent Activity

- **plurigrid/asi** — `everything is topological chemputer!` — pushed 2026-06-29 (27★)
- **plurigrid/place** — pushed 2026-06-29
- **plurigrid/eirobri** — EiRoBri replay world — pushed 2026-06-23 (Clojure)
- **plurigrid/nash-portal** — NASH token TUI in browser (Rust/WASM) — pushed 2026-05-19 (2★)
- **TeglonLabs/jank-crane** — crane-jank converged-IR hub, GF3 convergence maps — pushed 2026-06-08 (C++)
- **M1shaaa/M1shaaa** — profile config — pushed 2026-06-29 (today)
- **wasita/wasita.github.io** — personal website — pushed 2026-06-25

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|---|---|---|---|
| 0 | #d3869b | ERGODIC | 130 |
| +1 | #b8bb26 | PLUS | 131 |
| -1 | #cc241d | MINUS | 130 |

Total world-increment IDs assigned: **391** (IDs 1–391)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried via `fullnode.mainnet.aptoslabs.com` — all 28 addresses (alice, bob, A–Z).

**Result:** All 28 wallets returned 0 APT. The CoinStore resource was absent for all queried addresses, indicating these accounts have no APT balance on Aptos mainnet at time of snapshot (or accounts are uninitialized).

| Wallet | Address (truncated) | Balance (APT) |
|---|---|---|
| alice | 0xc793...cc7b | 0 |
| bob | 0x0a3c...2d5d | 0 |
| A–Z | (26 addresses) | 0 each |

### Multisig Contract Probes

All 5 contracts healthy — **2 signatures required** for each.

| Pair | Address (truncated) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel deployment protection (auth required). All API paths probed returned auth wall. No market data captured.

---

## DuckDB Schema Summary

```
world_increments:  391 rows  (GF3-tagged repo snapshots)
repo_snapshots:    391 rows  (per-repo metadata)
aptos_snapshots:    28 rows  (all 0 APT)
multisig_probes:     5 rows  (all healthy, 2-of-N)
mnx_snapshots:       0 rows  (unavailable - Vercel auth)
```
