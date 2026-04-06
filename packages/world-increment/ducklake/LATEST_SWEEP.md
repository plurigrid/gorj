# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-04-06T14:06 UTC  
**GF(3) color chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d (cycling)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted (13 increments)

| # | Source Type | Name | GF3 Trit | Color | Repos |
|---|------------|------|----------|-------|-------|
| 1 | org | plurigrid | 1 PLUS | #b8bb26 | 100 |
| 2 | org | kubeflow | 2 MINUS | #cc241d | 46 |
| 3 | org | TeglonLabs | 0 ERGODIC | #d3869b | 0 |
| 4 | user | bmorphism | 1 PLUS | #b8bb26 | 100 |
| 5 | user | zubyul | 2 MINUS | #cc241d | 23 |
| 6 | social_graph | migalkin | 0 ERGODIC | #d3869b | 30 |
| 7 | social_graph | DJedamski | 1 PLUS | #b8bb26 | 0 |
| 8 | social_graph | wasita | 2 MINUS | #cc241d | 29 |
| 9 | social_graph | kristinezheng | 0 ERGODIC | #d3869b | 18 |
| 10 | social_graph | M1shaaa | 1 PLUS | #b8bb26 | 16 |
| 11 | social_graph | AustinCStone | 2 MINUS | #cc241d | 0 |
| 12 | events | bmorphism | 0 ERGODIC | #d3869b | PushEvent (30 events) |
| 13 | events | zubyul | 1 PLUS | #b8bb26 | PullRequestEvent,CreateEvent (30 events) |

### Repo Snapshot Summary

| Source | Repos | Total Stars |
|--------|-------|-------------|
| bmorphism | 130 | 132 |
| plurigrid | 100 | 39 |
| zubyul | 53 | 13 |
| kubeflow | 46 | 33,818 |
| migalkin | 30 | 277 |
| wasita | 29 | 3 |
| kristinezheng | 18 | 0 |
| M1shaaa | 16 | 0 |

**Total:** 422 repo snapshot rows in DuckDB

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, mainnet)

All 28 wallets (alice, bob, A-Z) queried via Aptos fullnode mainnet.  
**All balances: 0 APT** — addresses have no CoinStore resource registered (unfunded / unused accounts).

| World | Address | Balance (APT) |
|-------|---------|--------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A-Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes (5 pairs)

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

**All 5 multisigs healthy, 2-of-N threshold confirmed.**

### MNX Markets (testnet.mnx.fi)

Status: **SPA detected** - testnet.mnx.fi serves a Next.js single-page application.  
No public JSON API endpoints found (/api/markets, /api/v1/markets, /api/tickers, etc. all 404).  
Market data unavailable without browser rendering. Recorded as `unavailable` in mnx_snapshots.

---

## DuckDB Schema Summary

```
world-increments.duckdb
- world_increments   (13 rows)  - GF3 color-chained sweep increments
- repo_snapshots     (422 rows) - GitHub repo metadata
- aptos_snapshots    (28 rows)  - Hamming swarm wallet balances
- multisig_probes    (5 rows)   - Multisig threshold probes
- mnx_snapshots      (1 row)    - MNX markets (unavailable)
```
