# World Increment Sweep — Latest Results

**Timestamp:** 2026-04-04T20:00:00Z  
**DuckDB Version:** v1.5.1 (Variegata)  
**Database:** `packages/world-increment/ducklake/sweep.duckdb`

---

## GitHub Sweep Summary

| Source | Type | Repos Collected | Top Repo (stars) |
|--------|------|-----------------|------------------|
| plurigrid | org | 20 (of 95) | asi (15★) |
| kubeflow | org | 20 (of 46) | kubeflow/kubeflow (15551★) |
| TeglonLabs | org | 3 (of 3) | mathpix-gem (2★) |
| bmorphism | user | 20 (of 97) | ocaml-mcp-sdk (60★) |
| zubyul | user | 20 (of 44) | gay-world (1★) |
| migalkin | user | 5 (of 19) | NodePiece (143★) |
| DJedamski | user | 5 (of 6) | Kaggle (1★) |
| wasita | user | 3 (of 9) | magic-garden (1★) |
| kristinezheng | user | 3 (of 6) | (0★) |
| M1shaaa | user | 3 (of 8) | (0★) |
| AustinCStone | user | 20 (of 40) | (0★) |

**Total repos stored:** 122

### Top Repos by Stars

| Rank | Repo | Language | Stars | Forks |
|------|------|----------|-------|-------|
| 1 | kubeflow/kubeflow | — | 15551 | — |
| 2 | kubeflow/pipelines | Python | 4117 | 1983 |
| 3 | kubeflow/spark-operator | Python | 3109 | 1480 |
| 4 | kubeflow/trainer | Go | 2074 | 942 |
| 5 | kubeflow/katib | Python | 1674 | — |
| 6 | kubeflow/manifests | YAML | 1007 | 1068 |
| 7 | migalkin/NodePiece | Python | 143 | 21 |
| 8 | migalkin/StarE | Python | 88 | 16 |
| 9 | bmorphism/ocaml-mcp-sdk | OCaml | 60 | 2 |
| 10 | plurigrid/asi | HTML | 15 | 5 |

---

## GF(3) Color Chain — World Increments

| id | source | type | trit | color | name |
|----|--------|------|------|-------|------|
| 1 | plurigrid | org | 1 | #b8bb26 | PLUS |
| 2 | kubeflow | org | -1 | #cc241d | MINUS |
| 3 | TeglonLabs | org | 0 | #d3869b | ERGODIC |
| 4 | bmorphism | user | 1 | #b8bb26 | PLUS |
| 5 | zubyul | user | -1 | #cc241d | MINUS |
| 6 | migalkin | user | 0 | #d3869b | ERGODIC |
| 7 | DJedamski | user | 1 | #b8bb26 | PLUS |
| 8 | wasita | user | -1 | #cc241d | MINUS |
| 9 | kristinezheng | user | 0 | #d3869b | ERGODIC |
| 10 | M1shaaa | user | 1 | #b8bb26 | PLUS |
| 11 | AustinCStone | user | -1 | #cc241d | MINUS |

---

## Aptos Wallet Snapshot

All 28 addresses queried against Aptos mainnet `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...89a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

> Note: All balances are 0 APT — addresses may hold other tokens or have no registered CoinStore on mainnet.

---

## Multisig Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | true |
| A-G | 0xf56c...096 | 2 | true |
| Y-Z | 0xd3ff...883 | 2 | true |
| S-T | 0x3b1c...883 | 2 | true |
| V-W | 0x40fa...b6d | 2 | true |

All 5 multisig accounts require **2-of-N signatures** and respond as healthy.

---

## MNX Markets Status

**Status:** Unavailable as JSON API  
`https://testnet.mnx.fi/api/markets` and `https://testnet.mnx.fi/api/tickers` both return HTML (Next.js SPA — no public REST endpoint accessible). No ticker data stored.

---

## Tables in sweep.duckdb

- `world_increments` — 11 rows (one per org/user)
- `repo_snapshots` — 122 rows
- `aptos_snapshots` — 28 rows
- `multisig_probes` — 5 rows
- `mnx_snapshots` — 1 row (unavailable marker)
