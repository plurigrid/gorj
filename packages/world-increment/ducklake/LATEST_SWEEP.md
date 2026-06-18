# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-18
**DuckDB:** `world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Inc ID | GF3 Trit | Color | Name | Source | Type | Repos |
|--------|----------|-------|------|--------|------|-------|
| 1 | 1 | #b8bb26 | PLUS | plurigrid | org | 100 |
| 2 | 2 | #cc241d | MINUS | kubeflow | org | 48 |
| 3 | 0 | #d3869b | ERGODIC | TeglonLabs | org | 5 |
| 4 | 1 | #b8bb26 | PLUS | bmorphism | user | 100 |
| 5 | 2 | #cc241d | MINUS | zubyul | user | 49 |
| 6 | 0 | #d3869b | ERGODIC | migalkin | user | 6 |
| 7 | 1 | #b8bb26 | PLUS | DJedamski | user | 3 |
| 8 | 2 | #cc241d | MINUS | wasita | user | 5 |
| 9 | 0 | #d3869b | ERGODIC | kristinezheng | user | 3 |
| 10 | 1 | #b8bb26 | PLUS | M1shaaa | user | 3 |
| 11 | 2 | #cc241d | MINUS | AustinCStone | user | 4 |

**Total repos snapshotted: 326**

### Top Repos by Stars

| Org/User | Repo | Stars | Language | Last Push |
|----------|------|-------|----------|-----------|
| kubeflow | kubeflow | 15,734 | — | 2026-06-18 |
| kubeflow | pipelines | 4,154 | Python | 2026-06-18 |
| kubeflow | spark-operator | 3,127 | Python | 2026-06-18 |
| kubeflow | trainer | 2,116 | Go | 2026-06-18 |
| kubeflow | katib | 1,683 | Python | 2026-06-15 |
| migalkin | NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone | TextGAN | 92 | Python | 2025-03-03 |
| migalkin | StarE | 89 | Python | 2026-04-16 |
| TeglonLabs | mathpix-gem | 2 | Ruby | 2026-01-01 |

### Notable Activity
- **kubeflow**: 6 repos pushed on 2026-06-18 (active CI day)
- **TeglonLabs/jank-crane**: new C++ repo (pushed 2026-06-08) — crane-jank converged-IR hub with GF3 convergence maps
- **wasita/wasita.github.io**: Svelte site pushed 2026-06-15
- **migalkin/RWL**: Weisfeiler-Leman relational — pushed 2026-05-28

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-06-18)

> API: `0x1::coin::balance` view function (legacy CoinStore not present on these accounts)

| World | APT Balance | Address (truncated) |
|-------|-------------|---------------------|
| alice | 0.43643352 | 0xc793...c7b |
| bob | **12.65700700** | 0x0a3c...d5d |
| A | 0.05176700 | 0x8699...a7a |
| B | 0.03625600 | 0x3f89...b13 |
| C | 0.01018500 | 0x38b9...35e |
| D | 0.01162900 | 0xf776...dd1 |
| E | 0.00937200 | 0xdc1d...d36 |
| F | **1.96051600** | 0x18a1...f71 |
| G | 0.00068100 | 0x69a3...f32 |
| H | 0.00168100 | 0xce67...00f |
| I | 0.00068100 | 0x070f...fc9 |
| J | **1.89509300** | 0x4d96...f54 |
| K | 0.16196100 | 0xa732...dc4 |
| L | **1.92726900** | 0x7c2e...ba9 |
| M | 0.11228500 | 0x6fed...2e9 |
| N | 0.10612100 | 0xe7dd...b2c |
| O | 0.21013600 | 0x7325...89d |
| P | 0.14013600 | 0x6218...948 |
| Q | 0.10324000 | 0xac40...a9 |
| R | 0.09021700 | 0x7ce6...e10 |
| S | 0.09178800 | 0xb875...386 |
| T | 0.07371300 | 0x3578...588 |
| U | 0.05577300 | 0x7586...956 |
| V | 0.04883299 | 0xb59d...2c3 |
| W | 0.04070500 | 0x5f32...7b0 |
| X | 0.04257700 | 0xa95c...47d |
| Y | 0.04444900 | 0xd8e3...4c4 |
| Z | 0.02426800 | 0x7af0...97c |

**Total swarm APT: ~20.13 APT**
Notable balances: `bob` (12.66 APT), `F` (1.96 APT), `L` (1.93 APT), `J` (1.90 APT)

### Multisig Contract Probes

All 5 probed contracts returned `sigs_required = 2`

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...003 | 2 | healthy |
| A-G | 0xf56c...096 | 2 | healthy |
| Y-Z | 0xd3ff...883 | 2 | healthy |
| S-T | 0x3b1c...883 | 2 | healthy |
| V-W | 0x40fa...b6d | 2 | healthy |

### MNX Markets

`https://testnet.mnx.fi` — **UNAVAILABLE**: Vercel authentication required. Market data could not be fetched without deployment credentials.

---

## DuckDB Schema Summary

| Table | Rows | Notes |
|-------|------|-------|
| world_increments | 11 | GF3 color chain per source |
| repo_snapshots | 326 | orgs + users + social graph |
| aptos_snapshots | 28 | alice, bob, A-Z |
| multisig_probes | 5 | all sigs_required=2 |
| mnx_snapshots | 0 | Vercel auth blocked |
