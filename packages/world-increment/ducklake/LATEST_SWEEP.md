# World-Increment Sweep + Hamming Snapshot
**Date:** 2026-04-16  
**Run timestamp:** 2026-04-16T21:10 UTC  
**GF(3) chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources queried
| Source | Type | Repos captured | Status |
|--------|------|---------------|--------|
| plurigrid | org | 100 | ✓ |
| kubeflow | org | 47 | ✓ |
| TeglonLabs | org | 0 | rate-limited |
| bmorphism | user | 0 | rate-limited |
| zubyul | user | 0 | rate-limited |
| migalkin | user | 0 | rate-limited |
| DJedamski | user | 0 | rate-limited |
| wasita | user | 0 | rate-limited |
| kristinezheng | user | 0 | rate-limited |
| M1shaaa | user | 0 | rate-limited |
| AustinCStone | user | 0 | rate-limited |

GitHub unauthenticated API limit (60 req/hr) was exhausted mid-sweep. plurigrid (100) and kubeflow (47) repos captured before limit hit.

### DuckDB Ducklake
- **DB path:** `packages/world-increment/ducklake/world-increments.duckdb`
- **world_increments:** 170 rows (GF3: 56 ERGODIC / 57 PLUS / 57 MINUS)
- **repo_snapshots:** 1091 rows (cumulative across runs)
- **New this run:** 147 increment + repo rows from plurigrid + kubeflow

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-04-16)

| World | APT Balance |
|-------|-------------|
| alice | 0.43643352 |
| bob   | **12.65700700** |
| A | 0.05176700 |
| B | 0.03625600 |
| C | 0.01018500 |
| D | 0.01162900 |
| E | 0.00937200 |
| **F** | **1.96051600** |
| G | 0.00068100 |
| H | 0.00168100 |
| I | 0.00068100 |
| **J** | **1.89509300** |
| K | 0.16196100 |
| **L** | **1.92726900** |
| M | 0.11228500 |
| N | 0.10612100 |
| O | 0.21013600 |
| P | 0.14013600 |
| Q | 0.10324000 |
| R | 0.09021700 |
| S | 0.09178800 |
| T | 0.07371300 |
| U | 0.05577300 |
| V | 0.04883299 |
| W | 0.04070500 |
| X | 0.04257700 |
| Y | 0.04444900 |
| Z | 0.02426800 |

**Total swarm APT:** ~18.79 APT  
**Richest:** bob (12.66 APT), F (1.96 APT), L (1.93 APT), J (1.90 APT)  
**Balance queried via:** `0x1::coin::balance` view function (CoinStore resource not registered on these accounts)

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | **2** | ✓ |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | **2** | ✓ |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | **2** | ✓ |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | **2** | ✓ |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | **2** | ✓ |

All 5 multisig contracts healthy. All require 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable as JSON API** — returns Next.js SPA HTML on all probed paths (`/`, `/api/markets`, `/api/v1/markets`). No structured market data extractable via HTTP.

---

## DuckDB Table Summary

| Table | Rows |
|-------|------|
| world_increments | 170 |
| repo_snapshots | 1091 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (SPA note) |
