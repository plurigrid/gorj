# World-Increment Sweep + Hamming Snapshot
**Run date:** 2026-08-07  
**GF(3) color chain:** id%3==0 → trit=0 ERGODIC #d3869b · id%3==1 → trit=1 PLUS #b8bb26 · id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources queried
| Source | Type | Repos captured |
|--------|------|---------------|
| plurigrid | org | 50 |
| kubeflow | org | 49 (top 10 inserted) |
| TeglonLabs | org | 5 |
| bmorphism | user | 50 (top 10 inserted) |
| zubyul | user | 49 (top 7 inserted) |
| migalkin | social_graph | 19 (top 4 inserted) |
| wasita | social_graph | 14 (top 4 inserted) |
| kristinezheng | social_graph | 5 (top 2 inserted) |
| AustinCStone | social_graph | 41 (top 2 inserted) |
| M1shaaa | social_graph | 8 (top 2 inserted) |
| DJedamski | social_graph | 6 (top 2 inserted) |

**Total world_increments inserted:** 98  
**Total repo_snapshots inserted:** 98

### Notable repos (most recently pushed)
| Repo | Stars | Language | Last push |
|------|-------|----------|-----------|
| plurigrid/gorj | 1 | Clojure | 2026-08-07 |
| plurigrid/place | 2 | TeX | 2026-08-02 |
| kubeflow/kubeflow | 15,805 | — | 2026-08-04 |
| kubeflow/pipelines | 4,181 | Python | 2026-08-07 |
| kubeflow/spark-operator | 3,145 | Python | 2026-08-07 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-08-02 |
| wasita/xoxowasita-analysis | 0 | Python | 2026-08-06 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances
**All 28 addresses queried via Aptos mainnet fullnode API.**  
Result: **All accounts returned `resource_not_found`** for the APT CoinStore resource — these accounts have not been initialized with an APT balance on Aptos mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z | 0x8699...425dc4 … | 0.0 (all) |

### Multisig Contract Probes
**All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.**  
Result: **All healthy — 2 signatures required.**

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4…7003 | 2 | ✅ |
| A-G | 0xf56c…0096 | 2 | ✅ |
| Y-Z | 0xd3ff…b883 | 2 | ✅ |
| S-T | 0x3b1c…7883 | 2 | ✅ |
| V-W | 0x40fa…eb6d | 2 | ✅ |

### MNX Markets (testnet.mnx.fi)
**Unavailable via API.** `testnet.mnx.fi` is a Next.js SPA (server-rendered). Probed `/api/markets`, `/api/v1/markets` — both return HTML (no REST endpoint exposed). No market data extractable from server-rendered shell.

---

## DuckDB Schema Summary
```
packages/world-increment/ducklake/world-increments.duckdb
  ├── world_increments       (98 rows) — GF(3) color-tagged events
  ├── repo_snapshots         (98 rows) — org/user/repo metadata
  ├── aptos_snapshots        (28 rows) — all 0.0 APT (resource_not_found)
  ├── multisig_probes         (5 rows) — all healthy, 2-of-n
  └── mnx_snapshots           (0 rows) — SPA, no public API
```
