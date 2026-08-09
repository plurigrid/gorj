# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-08-09  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Job 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social graph | 19 |
| DJedamski | social graph | 6 |
| wasita | social graph | 14 |
| kristinezheng | social graph | 5 |
| M1shaaa | social graph | 8 |
| AustinCStone | social graph | 41 |
| **TOTAL** | | **396** |

### Top 10 Most Recently Pushed Repos

| Repo | Pushed | Language | Stars |
|------|--------|----------|-------|
| plurigrid/gorj | 2026-08-09T08:16:39Z | Clojure | 1 |
| kubeflow/pipelines | 2026-08-09T07:28:45Z | Python | 4182 |
| M1shaaa/M1shaaa | 2026-08-09T01:21:57Z | — | 0 |
| plurigrid/place | 2026-08-09T01:07:33Z | TeX | 3 |
| kubeflow/docs-agent | 2026-08-08T17:09:05Z | Python | 40 |
| kubeflow/spark-operator | 2026-08-08T13:53:59Z | Python | 3145 |
| kubeflow/trainer | 2026-08-08T00:56:11Z | Go | 2176 |
| kubeflow/blog | 2026-08-07T22:06:18Z | Jupyter Notebook | 32 |
| kubeflow/sdk | 2026-08-07T21:39:01Z | Python | 136 |
| wasita/xoxowasita-analysis | 2026-08-07T20:50:03Z | Python | 0 |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 139 |
| 1 | #b8bb26 | PLUS | 140 |
| -1 | #cc241d | MINUS | 140 |

---

## Job 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 wallets queried (alice, bob, A–Z). All returned **0.0 APT** — accounts either have no APT balance or the `CoinStore<AptosCoin>` resource has not been initialized for these addresses at time of snapshot.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793ac... | 0.0 |
| bob | 0x0a3c00... | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Probe Results

All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f4... | 2 | ✅ |
| A-G | 0xf56c4a... | 2 | ✅ |
| Y-Z | 0xd3ffe1... | 2 | ✅ |
| S-T | 0x3b1c3a... | 2 | ✅ |
| V-W | 0x40fad7... | 2 | ✅ |

All multisigs require **2 signatures** and are reachable on mainnet.

### MNX Markets (testnet.mnx.fi)

Status: **SPA — no public JSON API available**. The site serves a Next.js client-side app (HTTP 200) but `/api/markets` and `/api/v1/markets` return HTML, not JSON. No market data extracted.

---

## DuckDB Tables Summary

| Table | Rows |
|-------|------|
| world_increments | 419+ |
| repo_snapshots | 1340+ |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA) |

> Note: row counts include any prior sweep data accumulated in the DB (table created with `IF NOT EXISTS`, inserts are append-only).
