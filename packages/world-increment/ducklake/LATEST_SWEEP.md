# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-07-17  
**Timestamp:** 2026-07-17T00:00:00Z  
**GF(3) Color Chain:** id%3==0 → trit=0 ERGODIC #d3869b | id%3==1 → trit=1 PLUS #b8bb26 | id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 50+ |
| zubyul | user | 49 |
| migalkin | user | 19 |
| DJedamski | user | 6 |
| wasita | user | 12 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| AustinCStone | user | 41 |

**Total:** 131 repos stored across 11 sources.

### Notable Recent Activity (>=2026-07-10)
- **plurigrid/gorj** (Clojure) — pushed 2026-07-17 (this repo)
- **kubeflow/pipelines** (Python, stars=4168) — pushed 2026-07-17
- **kubeflow/sdk** (Python, stars=125) — pushed 2026-07-17
- **kubeflow/spark-operator** (Python, stars=3138) — pushed 2026-07-17
- **bmorphism/gay-chat** (Scheme) — pushed 2026-07-14
- **bmorphism/anti-bullshit-mcp-server** (JS, stars=22) — pushed 2026-07-12
- **wasita/wasita.github.io** (Svelte) — pushed 2026-07-16
- **migalkin/kgcourse2021** (HTML) — pushed 2026-07-10
- **AustinCStone/byteruckus** (HTML) — pushed 2026-07-15

### DuckDB Tables
- **world_increments**: 154 rows (GF3 color-chained increment events)
- **repo_snapshots**: 131 repos across 11 sources

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
**Endpoint:** fullnode.mainnet.aptoslabs.com/v1

All 28 addresses (alice, bob, A-Z) queried. All returned `no_resource` for
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — addresses exist on-chain
but have no APT CoinStore registered at this snapshot timestamp.

| World | Address (truncated) | Balance APT | Status |
|-------|---------------------|-------------|--------|
| alice | 0xc793...cc7b | 0.0 | no_resource |
| bob | 0x0a3c...512d | 0.0 | no_resource |
| A | 0x8699...9d7a | 0.0 | no_resource |
| B-Z | (see DB) | 0.0 | no_resource |

### Multisig Contract Probes (Mainnet)
All 5 multisig contracts are **healthy** — each requires 2-of-2 signatures.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | healthy |
| A-G | 0xf56c...0096 | 2 | healthy |
| Y-Z | 0xd3ff...b883 | 2 | healthy |
| S-T | 0x3b1c...7883 | 2 | healthy |
| V-W | 0x40fa...eb6d | 2 | healthy |

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — site is behind Vercel authentication (visitor password required).
No market data could be extracted.

---

## DuckDB Schema Summary

```
packages/world-increment/ducklake/world-increments.duckdb
  world_increments    154 rows  -- GF3-chained increment log
  repo_snapshots      131 rows  -- GitHub repo metadata
  aptos_snapshots      28 rows  -- Hamming swarm wallet balances
  multisig_probes       5 rows  -- Multisig contract health
  mnx_snapshots         0 rows  -- Unavailable (auth-gated)
```
