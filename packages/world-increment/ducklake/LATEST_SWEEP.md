# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-15T07:11 UTC  
**Branch:** world-increment/sweep-2026-07-15  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

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
| migalkin | social_graph | 19 |
| AustinCStone | social_graph | 30 |
| wasita | social_graph | 11 |
| DJedamski | social_graph | 6 |
| kristinezheng | social_graph | 5 |
| M1shaaa | social_graph | 8 |
| **TOTAL** | | **382** |

### DuckDB Tables

- `world_increments` — 382 rows, GF(3) color chain applied
- `repo_snapshots` — 382 rows, full repo metadata
- `aptos_snapshots` — 28 rows, Hamming swarm wallet probes
- `multisig_probes` — 5 rows, multisig contract health checks
- `mnx_snapshots` — 0 rows (unavailable this run)

### GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 127 |
| 1 | PLUS | #b8bb26 | 128 |
| -1 | MINUS | #cc241d | 127 |

### Notable Repos (Most Recent Activity)

- `plurigrid/gorj` — pushed 2026-07-15 (1,178 open issues)
- `plurigrid/asi` — pushed 2026-07-10 (30 stars, "everything is topological chemputer!")
- `kubeflow/pipelines` — pushed 2026-07-15 (4,166 stars, 2,034 forks)
- `kubeflow/docs-agent` — pushed 2026-07-15
- `TeglonLabs/jank-crane` — pushed 2026-06-08 (crane-jank GF3 convergence maps)
- `wasita/wasita.github.io` — pushed 2026-07-14 (Svelte personal site)
- `M1shaaa/M1shaaa` — pushed 2026-07-15

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A-Z) queried via Aptos fullnode API.

**Result:** All 28 addresses returned `Resource not found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. Accounts appear unfunded or not yet initialized on mainnet.

### Multisig Contract Probes (Aptos Mainnet)

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | HEALTHY |
| A-G | 0xf56c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY |
| S-T | 0x3b1c...7883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

All 5 multisig contracts require 2-of-N and are responsive.

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — Returns HTTP 401 (Vercel Authentication Required). No market data extracted.

---

## Summary

- **382 repos** snapshotted (3 orgs + 8 users in plurigrid/zubyul social graph)
- **28 Aptos wallets** probed — all unfunded on mainnet
- **5 multisig contracts** all healthy, 2-of-N threshold
- **MNX testnet** behind Vercel auth gate — unavailable
- GF(3) coloring: ERGODIC(127) / PLUS(128) / MINUS(127) across all world increments
