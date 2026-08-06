# World-Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-08-06  
**Branch:** world-increment/sweep-$(date)  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos Snapshotted | GF3 |
|--------|------|-------------------|-----|
| plurigrid | org | 100 | PLUS #b8bb26 |
| kubeflow | org | 49 | MINUS #cc241d |
| TeglonLabs | org | 5 | ERGODIC #d3869b |
| bmorphism | user | 100 | PLUS #b8bb26 |
| zubyul | user | 49 | MINUS #cc241d |
| migalkin | social graph | 19 | ERGODIC #d3869b |
| DJedamski | social graph | 6 | PLUS #b8bb26 |
| wasita | social graph | 14 | MINUS #cc241d |
| kristinezheng | social graph | 5 | ERGODIC #d3869b |
| M1shaaa | social graph | 8 | PLUS #b8bb26 |
| AustinCStone | social graph | 41 | MINUS #cc241d |

**Total repos snapshotted: 329**

### Top Repos by Stars

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,805 | - | 2026-07-10 |
| kubeflow/pipelines | 4,178 | Python | 2026-08-05 |
| kubeflow/spark-operator | 3,144 | Python | 2026-08-05 |
| kubeflow/trainer | 2,171 | Go | 2026-08-05 |
| kubeflow/katib | 1,694 | Python | 2026-08-05 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/kgcourse2021 | 24 | HTML | 2026-07-10 |
| TeglonLabs/mathpix-gem | 2 | Ruby | 2026-01-01 |

### Notable Activity

- **wasita**: Most recently active social-graph node — pushed `xoxowasita-analysis` on 2026-08-05, `joint-planning-lit` on 2026-08-04
- **TeglonLabs/jank-crane**: GF3 convergence maps + crane-jank IR hub, pushed 2026-06-08
- **kubeflow/pipelines** and **kubeflow/trainer**: Both active within the last 24h (2026-08-05)
- **kubeflow/mcp-apache-spark-history-server**: New MCP integration, 186 stars, pushed 2026-08-04

### DuckDB Tables

```
world_increments : 14 rows  (one per source, GF3 color chain)
repo_snapshots   : 329 rows (full metadata per repo)
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

**Date:** 2026-08-06 | **Network:** Mainnet | **Ledger:** ~6,639,816,238

All 28 wallets (alice, bob, A–Z) returned `resource_not_found` from the Aptos mainnet fullnode. This indicates the `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource has not been initialized on these addresses — consistent with newly generated keypairs or accounts that have never received a transfer. **Balance: 0.0 APT** for all.

| World | Address (truncated) | Balance (APT) | Status |
|-------|---------------------|---------------|--------|
| alice | 0xc793...cc7b | 0.0 | resource_not_found |
| bob | 0x0a3c...2d5d | 0.0 | resource_not_found |
| A–Z (26 wallets) | various | 0.0 | resource_not_found |

### Multisig Contract Probes

All 5 multisig contracts are **healthy** (2-of-N signature threshold confirmed):

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable — pure SPA (Next.js)**

The site at `https://testnet.mnx.fi` returns HTTP 200 but serves a Next.js single-page app for all paths including `/api/markets`, `/api/v1/markets`, `/api/v2/markets`. No JSON market data is accessible without executing the JavaScript bundle. No ticker data recorded.

### DuckDB Tables

```
aptos_snapshots  : 28 rows (one per wallet, balance=0.0)
multisig_probes  :  5 rows (all healthy, sigs_required=2)
mnx_snapshots    :  1 row  (status=unavailable)
```

---

## GF3 Color Chain (world_increments sequence)

| ID | Trit | Color | Name | Source | Event |
|----|------|-------|------|--------|-------|
| 1 | +1 | #b8bb26 | PLUS | plurigrid | repo_snapshot |
| 2 | -1 | #cc241d | MINUS | kubeflow | repo_snapshot |
| 3 | 0 | #d3869b | ERGODIC | TeglonLabs | repo_snapshot |
| 4 | +1 | #b8bb26 | PLUS | bmorphism | repo_snapshot |
| 5 | -1 | #cc241d | MINUS | zubyul | repo_snapshot |
| 6 | 0 | #d3869b | ERGODIC | migalkin | social_graph |
| 7 | +1 | #b8bb26 | PLUS | DJedamski | social_graph |
| 8 | -1 | #cc241d | MINUS | wasita | social_graph |
| 9 | 0 | #d3869b | ERGODIC | kristinezheng | social_graph |
| 10 | +1 | #b8bb26 | PLUS | M1shaaa | social_graph |
| 11 | -1 | #cc241d | MINUS | AustinCStone | social_graph |
| 12 | 0 | #d3869b | ERGODIC | aptos-mainnet | wallet_snapshot |
| 13 | +1 | #b8bb26 | PLUS | aptos-mainnet | multisig_probe |
| 14 | -1 | #cc241d | MINUS | mnx-testnet | market_snapshot |
