# World-Increment Sweep — Latest Summary

**Sweep Timestamp:** 2026-04-01T23:00:00Z (UTC)

---

## GitHub Sweep

### Sources & Repo Counts

| Source | Type | Repo Count | GF3 Color | GF3 Trit |
|--------|------|-----------|-----------|----------|
| plurigrid | org | 100 | PLUS (#b8bb26) | +1 |
| kubeflow | org | 46 | MINUS (#cc241d) | -1 |
| TeglonLabs | org | 53 | ERGODIC (#d3869b) | 0 |
| bmorphism | user | 100 | PLUS (#b8bb26) | +1 |
| zubyul | user | 0 | MINUS (#cc241d) | -1 |
| migalkin | user (social) | 30 | ERGODIC (#d3869b) | 0 |
| DJedamski | user (social) | 11 | PLUS (#b8bb26) | +1 |
| wasita | user (social) | 29 | MINUS (#cc241d) | -1 |
| kristinezheng | user (social) | 18 | ERGODIC (#d3869b) | 0 |
| M1shaaa | user (social) | 16 | PLUS (#b8bb26) | +1 |
| AustinCStone | user (social) | 43 | MINUS (#cc241d) | -1 |

**Total repos collected:** 446

### Top Repos by Stars

| Repo | Stars |
|------|-------|
| kubeflow/kubeflow | 15,549 |
| kubeflow/pipelines | 4,118 |
| kubeflow/spark-operator | 3,110 |
| kubeflow/trainer | 2,070 |
| kubeflow/katib | 1,674 |
| kubeflow/examples | 1,459 |
| kubeflow/manifests | 1,006 |
| kubeflow/arena | 809 |
| kubeflow/kale | 681 |
| kubeflow/mpi-operator | 519 |

---

## GF(3) Color Chain Assignments

GF(3) assignment rule: `id % 3 == 0` → trit=0 / ERGODIC (#d3869b), `id % 3 == 1` → trit=+1 / PLUS (#b8bb26), `id % 3 == 2` → trit=-1 / MINUS (#cc241d).

| ID | Source | GF3 Trit | GF3 Color | Hex |
|----|--------|----------|-----------|-----|
| 1 | plurigrid | +1 | PLUS | #b8bb26 |
| 2 | kubeflow | -1 | MINUS | #cc241d |
| 3 | TeglonLabs | 0 | ERGODIC | #d3869b |
| 4 | bmorphism | +1 | PLUS | #b8bb26 |
| 5 | zubyul | -1 | MINUS | #cc241d |
| 6 | migalkin | 0 | ERGODIC | #d3869b |
| 7 | DJedamski | +1 | PLUS | #b8bb26 |
| 8 | wasita | -1 | MINUS | #cc241d |
| 9 | kristinezheng | 0 | ERGODIC | #d3869b |
| 10 | M1shaaa | +1 | PLUS | #b8bb26 |
| 11 | AustinCStone | -1 | MINUS | #cc241d |

---

## Aptos Snapshot

All wallets queried on Aptos mainnet. All returned 0 APT (accounts have no CoinStore resource or zero balance).

| Label | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...c7b | 0.0 |
| bob | 0x0a3c...d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...89a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...7b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

---

## Multisig Probes

All 5 multisig contracts queried via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | true |
| A-G | 0xf56c...096 | 2 | true |
| Y-Z | 0xd3ff...883 | 2 | true |
| S-T | 0x3b1c...883 | 2 | true |
| V-W | 0x40fa...b6d | 2 | true |

All multisig contracts are healthy with 2-of-N signature requirements.

---

## MNX Markets

**Status: unavailable**

All endpoints (`https://testnet.mnx.fi/api/markets`, `/api/v1/markets`, `/`) return a Next.js SPA HTML page with no machine-readable market data accessible via direct API calls. No structured market data was retrievable.

---

## Summary

| Metric | Value |
|--------|-------|
| Total world_increments inserted | 11 |
| Total repo_snapshots inserted | 446 |
| Aptos wallet snapshots | 28 |
| Multisig probes | 5 |
| MNX market snapshots | 0 (unavailable) |
| GitHub sources queried | 11 |
| Events collected | 60 (30 each for bmorphism, zubyul) |
