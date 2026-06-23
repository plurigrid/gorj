# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-23  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos | Total Count |
|--------|------|-------|-------------|
| plurigrid | org | 100 | 101 |
| kubeflow | org | 48 | 48 |
| TeglonLabs | org | 5 | 5 |
| bmorphism | user | 100 | 105 |
| zubyul | user | 49 | 49 |
| migalkin | user | 19 | 19 |
| DJedamski | user | 6 | 6 |
| wasita | user | 11 | 11 |
| kristinezheng | user | 5 | 5 |
| M1shaaa | user | 8 | 8 |
| AustinCStone | user | 40 | 40 |
| **Total** | | **391** | |

### Notable Repos (by stars)

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15741 | Jsonnet |
| kubeflow/pipelines | 4157 | Python |
| kubeflow/spark-operator | 3128 | Go |
| kubeflow/trainer | 2119 | Python |
| kubeflow/katib | 1685 | Go |
| kubeflow/examples | 1460 | Jupyter Notebook |

### Language Distribution (top 10)

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

### GF(3) Color Chain

- **ERGODIC** (#d3869b, trit=0): id % 3 == 0  
- **PLUS** (#b8bb26, trit=1): id % 3 == 1  
- **MINUS** (#cc241d, trit=-1): id % 3 == 2  

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 addresses (alice, bob, A-Z) queried against Aptos mainnet fullnode.  
**Result:** All addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
Recorded as 0.0 APT. API reachable; addresses have not initialized a CoinStore.

### Multisig Contract Probes (5 contracts)

All probes via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...003 | 2 | healthy |
| A-G | 0xf56c...096 | 2 | healthy |
| Y-Z | 0xd3ff...883 | 2 | healthy |
| S-T | 0x3b1c...883 | 2 | healthy |
| V-W | 0x40fa...b6d | 2 | healthy |

**All 5 multisig contracts operational at 2-of-2 threshold.**

### MNX Markets (testnet.mnx.fi)

`GET https://testnet.mnx.fi/api/markets` returned **401 Unauthorized**.  
Market data unavailable - testnet requires authentication.

---

## DuckDB Schema Summary

```
world_increments  (391 rows) - GF3 color-tagged events
repo_snapshots    (391 rows) - GitHub repo metadata
aptos_snapshots   (28 rows)  - Hamming swarm wallet balances
multisig_probes   (5 rows)   - Multisig contract health
mnx_snapshots     (0 rows)   - MNX markets (unavailable)
```
