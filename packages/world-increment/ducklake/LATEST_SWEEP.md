# World Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-04-20 (UTC)
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 47 |
| migalkin | user | 18 |
| DJedamski | user | 6 |
| wasita | user | 10 |
| kristinezheng | user | 6 |
| M1shaaa | user | 8 |
| AustinCStone | user | 70 |

**Total repos snapshotted:** 416 (this run) / 1360 cumulative in DB

### GF(3) Color Chain Applied

| id % 3 | Trit | Color | Name |
|--------|------|-------|------|
| 0 | 0 | #d3869b | ERGODIC |
| 1 | +1 | #b8bb26 | PLUS |
| 2 | -1 | #cc241d | MINUS |

### Notable Recent Activity

- **wasita/wasita.github.io** — pushed 2026-04-13 (Svelte, 8 open issues)
- **M1shaaa/M1shaaa** — pushed 2026-04-19 (profile config)
- **kristinezheng/kristinezheng.github.io** — pushed 2026-04-09

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 wallets (alice, bob, A-Z) queried against Aptos mainnet CoinStore.
**Result:** All wallets returned 0.0 APT — accounts either not initialized or hold zero APT.

### Multisig Contract Probes

All 5 multisig contracts responded successfully. All require **2 signatures**.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | YES |
| A-G | 0xf56c...0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

**Swarm health:** 5/5 multisig contracts healthy.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — testnet.mnx.fi is a Next.js SPA. All API paths return HTML. No public REST endpoints accessible without browser JS execution.

---

## DuckDB Tables Summary

| Table | Rows |
|-------|------|
| world_increments | 439 |
| repo_snapshots | 1360 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (unavailable marker) |
