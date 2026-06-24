# World-Increment Sweep + Hamming Snapshot
**Date:** 2026-06-24  
**DB:** `world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 101 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 105 |
| zubyul | user | 49 |
| migalkin | social | 19 |
| DJedamski | social | 6 |
| AustinCStone | social | 40 |
| wasita | social | 11 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |

### Notable Recently-Pushed Repos
| Repo | Lang | Stars | Pushed |
|------|------|-------|--------|
| plurigrid/gorj | Clojure | 0 | 2026-06-24 |
| plurigrid/place | TeX | 1 | 2026-06-24 |
| kubeflow/dashboard | TypeScript | 16 | 2026-06-24 |
| bmorphism/Gay.jl | Julia | 2 | 2026-06-24 |
| plurigrid/eirobri | Clojure | 0 | 2026-06-23 |
| kubeflow/spark-operator | Python | 3128 | 2026-06-23 |
| kubeflow/mcp-apache-spark-history-server | Python | 178 | 2026-06-23 |
| kubeflow/pipelines | Python | 4157 | 2026-06-23 |
| kubeflow/kubeflow | — | 15741 | 2026-06-18 |
| wasita/proj-template | — | 0 | 2026-06-19 |
| wasita/wasita.github.io | Svelte | 1 | 2026-06-15 |
| kristinezheng/kristinezheng.github.io | HTML | 0 | 2026-06-07 |
| TeglonLabs/jank-crane | C++ | 0 | 2026-06-08 |

### GF(3) World-Increment Color Distribution
101 increments inserted into `world_increments`:
- **ERGODIC** `#d3869b` (trit=0, id%3=0): 33 increments
- **PLUS** `#b8bb26` (trit=1, id%3=1): 34 increments
- **MINUS** `#cc241d` (trit=-1, id%3=2): 34 increments

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances
All 28 wallets (alice, bob, A-Z) probed via Aptos mainnet fullnode.  
**Result:** All wallets returned `null` CoinStore resource — accounts not initialized on mainnet or hold 0 APT. Recorded as 0.0 APT.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793ac... | 0.0 |
| bob | 0x0a3c00... | 0.0 |
| A | 0x8699ed... | 0.0 |
| B | 0x3f892e... | 0.0 |
| C | 0x38b99e... | 0.0 |
| D | 0xf77656... | 0.0 |
| E | 0xdc1d9d... | 0.0 |
| F | 0x18a14b... | 0.0 |
| G | 0x69a394... | 0.0 |
| H | 0xce67c3... | 0.0 |
| I | 0x070fe5... | 0.0 |
| J | 0x4d964d... | 0.0 |
| K | 0xa73204... | 0.0 |
| L | 0x7c2eae... | 0.0 |
| M | 0x6fed37... | 0.0 |
| N | 0xe7dde6... | 0.0 |
| O | 0x73252b... | 0.0 |
| P | 0x621879... | 0.0 |
| Q | 0xac40fa... | 0.0 |
| R | 0x7ce605... | 0.0 |
| S | 0xb87530... | 0.0 |
| T | 0x35781d... | 0.0 |
| U | 0x75860d... | 0.0 |
| V | 0xb59dd8... | 0.0 |
| W | 0x5f32ae... | 0.0 |
| X | 0xa95cbb... | 0.0 |
| Y | 0xd8e328... | 0.0 |
| Z | 0x7af0ef... | 0.0 |

### Multisig Contract Probes
All 5 probed via `0x1::multisig_account::num_signatures_required`.  
**Result: All healthy -- 2-of-2 multisig.**

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f4... | 2 | yes |
| A-G | 0xf56c4a... | 2 | yes |
| Y-Z | 0xd3ffe1... | 2 | yes |
| S-T | 0x3b1c3a... | 2 | yes |
| V-W | 0x40fad7... | 2 | yes |

### MNX Markets (testnet.mnx.fi)
**Status: Unavailable** -- testnet.mnx.fi is protected by Vercel deployment authentication. No market data extractable without bypass token or Vercel CLI auth. No rows inserted into `mnx_snapshots`.

---

## DuckDB Schema Summary
```
world_increments  : 101 rows  (GF3 color chain, repo sweep events)
repo_snapshots    : 101 rows  (org/user/social graph repos)
aptos_snapshots   :  28 rows  (Hamming swarm wallets, all 0.0 APT)
multisig_probes   :   5 rows  (all 2-of-2, all healthy)
mnx_snapshots     :   0 rows  (Vercel auth blocked)
```
