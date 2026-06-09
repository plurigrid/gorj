# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-06-09  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos | GF3 |
|--------|------|-------|-----|
| plurigrid | org | 100 | PLUS #b8bb26 (trit=1) |
| kubeflow | org | 48 | ERGODIC #d3869b (trit=0) |
| TeglonLabs | org | 5 | MINUS #cc241d (trit=-1) |
| bmorphism | user | 49 | MINUS #cc241d (trit=-1) |
| zubyul | user | 19 | PLUS #b8bb26 (trit=1) |
| migalkin | user | 100 | PLUS #b8bb26 (trit=1) |
| DJedamski | user | 6 | ERGODIC #d3869b (trit=0) |
| wasita | user | 11 | ERGODIC #d3869b (trit=0) |
| kristinezheng | user | 5 | MINUS #cc241d (trit=-1) |
| M1shaaa | user | 8 | PLUS #b8bb26 (trit=1) |
| AustinCStone | user | 40 | MINUS #cc241d (trit=-1) |

**Total repos snapshotted: 391**

### Notable Repos
- `TeglonLabs/jank-crane` (C++, pushed 2026-06-08) — crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps
- `TeglonLabs/mathpix-gem` (Ruby, 2★) — Transform mathematical images to LaTeX
- `wasita/wasita.github.io` (Svelte, pushed 2026-06-01) — personal website
- `kristinezheng/kristinezheng.github.io` (HTML, pushed 2026-06-07)
- `M1shaaa/M1shaaa` (pushed 2026-06-09) — GitHub profile config

### GF3 Color Chain Distribution
- ERGODIC #d3869b (trit=0): 3 sources
- PLUS #b8bb26 (trit=1): 4 sources
- MINUS #cc241d (trit=-1): 4 sources

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
Queried 28 addresses from `fullnode.mainnet.aptoslabs.com`.

All 28 addresses (alice, bob, A–Z) returned **0.0 APT** — no `CoinStore<AptosCoin>` resource found (accounts uninitialized or no APT deposits on mainnet).

### Multisig Contract Probes
All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...987003 | 2 | ✓ |
| A-G | 0xf56c4a1c...c0096 | 2 | ✓ |
| Y-Z | 0xd3ffe181...5b883 | 2 | ✓ |
| S-T | 0x3b1c3ae9...d7883 | 2 | ✓ |
| V-W | 0x40fad7b4...0eb6d | 2 | ✓ |

**All 5 multisig contracts healthy — 2-of-2 threshold confirmed.**

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — protected by Vercel Deployment Protection. No market data accessible without auth token. `mnx_snapshots` table has 0 rows.

---

## DuckDB Schema Summary

```
world_increments  11 rows   GF3-tagged sweep events per source
repo_snapshots   391 rows   GitHub repos (lang/stars/forks/issues/pushed_at)
aptos_snapshots   28 rows   Hamming swarm wallet balances (all 0.0 APT)
multisig_probes    5 rows   2-of-2 multisig health (all healthy)
mnx_snapshots      0 rows   Unavailable (Vercel protection)
```
