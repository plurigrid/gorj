# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-05-10T14:30:00Z  
**DuckDB:** `world-increments.duckdb`  
**GF(3) color chain:** id%3==0 → trit=0 ERGODIC #d3869b · id%3==1 → trit=1 PLUS #b8bb26 · id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 20 |
| kubeflow | org | 20 |
| TeglonLabs | org | 4 |
| bmorphism | user | 12 |
| zubyul | user | 7 |
| migalkin | user (zubyul graph) | 4 |
| DJedamski | user (zubyul graph) | 1 |
| wasita | user (zubyul graph) | 3 |
| kristinezheng | user (zubyul graph) | 2 |
| M1shaaa | user (zubyul graph) | 2 |
| AustinCStone | user (zubyul graph) | 3 |
| **Total** | | **78** |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15628 | — | 2026-05-07 |
| kubeflow/pipelines | 4137 | Python | 2026-05-08 |
| kubeflow/spark-operator | 3125 | Python | 2026-05-08 |
| kubeflow/trainer | 2097 | Go | 2026-05-09 |
| kubeflow/katib | 1683 | Python | 2026-05-09 |
| kubeflow/examples | 1462 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1015 | YAML | 2026-05-08 |
| kubeflow/arena | 810 | Go | 2026-05-07 |
| kubeflow/kale | 685 | Python | 2026-05-09 |
| kubeflow/mpi-operator | 524 | Go | 2026-05-05 |

### Most Active Recent (plurigrid/bmorphism ecosystem)

| Repo | Language | Last Push |
|------|----------|-----------|
| plurigrid/gorj | Clojure | 2026-05-10 |
| bmorphism/Gay.jl | Julia | 2026-05-10 |
| bmorphism/nanoclj-zig | Zig | 2026-05-07 |
| plurigrid/horse | TeX | 2026-05-07 |
| bmorphism/zig-syrup | Zig | 2026-05-07 |
| plurigrid/zig-syrup | Zig | 2026-04-30 |
| zubyul/voice-observatory | Python | 2026-04-24 |

### GF(3) World-Increment Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| +1 | PLUS | #b8bb26 | 26 |
| -1 | MINUS | #cc241d | 26 |
| 0 | ERGODIC | #d3869b | 26 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried via `0x1::coin::balance<0x1::aptos_coin::AptosCoin>` view function.  
Note: legacy `CoinStore` resource returns `resource_not_found` for these accounts (migrated to FA).

| World | Balance (APT) | Address |
|-------|--------------|---------|
| **bob** | **12.657007** | 0x0a3c...d5d |
| **F** | **1.960516** | 0x18a1...71 |
| **L** | **1.927269** | 0x7c2e...a9 |
| **J** | **1.895093** | 0x4d96...54 |
| alice | 0.436434 | 0xc793...7b |
| K | 0.161961 | 0xa732...c4 |
| O | 0.210136 | 0x7325...9d |
| P | 0.140136 | 0x6218...48 |
| M | 0.112285 | 0x6fed...e9 |
| N | 0.106121 | 0xe7dd...2c |
| Q | 0.103240 | 0xac40...a9 |
| S | 0.091788 | 0xb875...86 |
| R | 0.090217 | 0x7ce6...10 |
| T | 0.073713 | 0x3578...88 |
| U | 0.055773 | 0x7586...56 |
| A | 0.051767 | 0x8699...7a |
| V | 0.048833 | 0xb59d...c3 |
| Y | 0.044449 | 0xd8e3...c4 |
| X | 0.042577 | 0xa95c...7d |
| W | 0.040705 | 0x5f32...b0 |
| B | 0.036256 | 0x3f89...13 |
| Z | 0.024268 | 0x7af0...7c |
| D | 0.011629 | 0xf776...d1 |
| C | 0.010185 | 0x38b9...5e |
| E | 0.009372 | 0xdc1d...36 |
| H | 0.001681 | 0xce67...0f |
| G | 0.000681 | 0x69a3...32 |
| I | 0.000681 | 0x070f...c9 |

**Total swarm APT:** ~20.46 APT

### Multisig Contract Probes

All 5 multisig contracts confirmed healthy (2-of-N signatures required).

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f4...87003 | 2 | true |
| A-G | 0xf56c4a...0096 | 2 | true |
| Y-Z | 0xd3ffe1...b883 | 2 | true |
| S-T | 0x3b1c3a...7883 | 2 | true |
| V-W | 0x40fad7...eb6d | 2 | true |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — site returns a Next.js SPA on all API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`). No JSON API accessible. `mnx_snapshots` table is empty.

---

## DuckDB Tables Summary

| Table | Rows |
|-------|------|
| world_increments | 78 |
| repo_snapshots | 78 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA, no API) |
