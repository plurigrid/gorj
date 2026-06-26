# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-26
**Run:** world-increment-sweep + hamming-swarm-snapshot agent
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos | Stars |
|--------|------|-------|-------|
| plurigrid | org | 100 | 77 |
| kubeflow | org | 48 | 34,257 |
| TeglonLabs | org | 5 | 2 |
| bmorphism | user | 100 | 247 |
| zubyul | user | 49 | 14 |
| migalkin | social | 19 | 280 |
| DJedamski | social | 6 | 3 |
| wasita | social | 11 | ~1 |
| kristinezheng | social | 5 | 0 |
| M1shaaa | social | 8 | 0 |
| AustinCStone | social | 30 | 108 |

**Total:** 370 repo snapshots stored

### Notable Repos

- **kubeflow** org — 34,257 total stars (dominant MLOps ecosystem)
- **plurigrid/asi** — 26 stars, "everything is topological chemputer!" (pushed 2026-06-26)
- **TeglonLabs/jank-crane** — "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps" (C++, 2026-06-08)
- **TeglonLabs/mathpix-gem** — 2 stars, 11 open issues
- **migalkin** — 280 stars, graph ML focus
- **bmorphism** — 100 repos, broad eclectic mix

### GF(3) Color Chain

| id | Trit | Color | Name | Source |
|----|------|-------|------|--------|
| 1 | 0 | #d3869b | ERGODIC | plurigrid |
| 2 | 1 | #b8bb26 | PLUS | kubeflow |
| 3 | -1 | #cc241d | MINUS | TeglonLabs |
| 4 | 0 | #d3869b | ERGODIC | bmorphism |
| 5 | 1 | #b8bb26 | PLUS | zubyul |
| 6 | -1 | #cc241d | MINUS | migalkin |
| 7 | 0 | #d3869b | ERGODIC | DJedamski |
| 8 | 1 | #b8bb26 | PLUS | wasita |
| 9 | -1 | #cc241d | MINUS | kristinezheng |
| 10 | 0 | #d3869b | ERGODIC | M1shaaa |
| 11 | 1 | #b8bb26 | PLUS | AustinCStone |
| 12 | -1 | #cc241d | MINUS | hamming_swarm (aptos) |
| 13 | 0 | #d3869b | ERGODIC | multisig probes |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (APT mainnet)

Queried via `0x1::coin::balance` view function. Note: legacy CoinStore resource
absent on these accounts; balances retrieved via view function instead.

| World | Balance (APT) |
|-------|---------------|
| bob | 12.657007 |
| F | 1.960516 |
| L | 1.927269 |
| J | 1.895093 |
| alice | 0.436434 |
| O | 0.210136 |
| K | 0.161961 |
| P | 0.140136 |
| M | 0.112285 |
| N | 0.106121 |
| Q | 0.103240 |
| S | 0.091788 |
| R | 0.090217 |
| T | 0.073713 |
| U | 0.055773 |
| A | 0.051767 |
| Y | 0.044449 |
| X | 0.042577 |
| W | 0.040705 |
| B | 0.036256 |
| V | 0.048833 |
| Z | 0.024268 |
| D | 0.011629 |
| C | 0.010185 |
| E | 0.009372 |
| H | 0.001681 |
| G | 0.000681 |
| I | 0.000681 |

**Total swarm:** ~20.05 APT
**Richest:** bob (12.66 APT), F (1.96), L (1.93), J (1.90)
**Dust wallets:** G, I (0.000681 APT each)

### Multisig Contract Probes

All 5 multisig pairs healthy — 2-of-2 signatures required.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...7003 | 2 | yes |
| A-G | 0xf56c4a1c...0096 | 2 | yes |
| Y-Z | 0xd3ffe181...b883 | 2 | yes |
| S-T | 0x3b1c3ae9...7883 | 2 | yes |
| V-W | 0x40fad7b4...eb6d | 2 | yes |

### MNX Markets (testnet.mnx.fi)

**Unavailable** — Vercel visitor authentication wall. No market data accessible.

---

## DuckDB Tables

| Table | Rows |
|-------|------|
| world_increments | 13 |
| repo_snapshots | 370 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (unavailable marker) |
