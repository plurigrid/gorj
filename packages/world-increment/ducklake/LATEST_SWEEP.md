# World Increment Sweep — Latest

**Sweep timestamp:** 2026-05-07T07:30 UTC

---

## GitHub Sweep Summary

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| DJedamski | user | 6 |
| wasita | user | 11 |
| kristinezheng | user | 6 |
| M1shaaa | user | 8 |
| AustinCStone | user | 40 |
| **TOTAL** | | **390** |

Note: GitHub public API rate limit (60 req/hr unauthenticated) was exceeded; data collected via MCP GitHub tool (authenticated).

---

## Top 5 Most Recently Pushed Repos

| Rank | Repo | Pushed At |
|------|------|-----------|
| 1 | kubeflow/arena | 2026-05-07T06:46:17Z |
| 2 | plurigrid/gorj | 2026-05-07T06:16:14Z |
| 3 | plurigrid/horse | 2026-05-07T04:35:12Z |
| 4 | M1shaaa/M1shaaa | 2026-05-07T02:35:34Z |
| 5 | kubeflow/pipelines | 2026-05-07T01:34:49Z |

---

## Aptos Snapshot

Queried via `0x1::coin::balance` view function on Aptos mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...4cc7b | 0.43643352 |
| bob   | 0x0a3c...512d5d | 12.657007 |
| A | 0x8699...be9d7a | 0.051767 |
| B | 0x3f89...7cb13 | 0.036256 |
| C | 0x38b9...1535e | 0.010185 |
| D | 0xf776...cfdd1 | 0.011629 |
| E | 0xdc1d...8d36 | 0.009372 |
| F | 0x18a1...3cf71 | 1.960516 |
| G | 0x69a3...7f32 | 0.000681 |
| H | 0xce67...5300f | 0.001681 |
| I | 0x070f...1fc9 | 0.000681 |
| J | 0x4d96...87f54 | 1.895093 |
| K | 0xa732...25dc4 | 0.161961 |
| L | 0x7c2e...eba9 | 1.927269 |
| M | 0x6fed...f2e9 | 0.112285 |
| N | 0xe7dd...51b2c | 0.106121 |
| O | 0x7325...a89d | 0.210136 |
| P | 0x6218...ec948 | 0.140136 |
| Q | 0xac40...c89a9 | 0.103240 |
| R | 0x7ce6...76e10 | 0.090217 |
| S | 0xb875...d0386 | 0.091788 |
| T | 0x3578...f4588 | 0.073713 |
| U | 0x7586...ef9956 | 0.055773 |
| V | 0xb59d...af2c3 | 0.048833 |
| W | 0x5f32...cc7b0 | 0.040705 |
| X | 0xa95c...3047d | 0.042577 |
| Y | 0xd8e3...444c4 | 0.044449 |
| Z | 0x7af0...197c | 0.024268 |

---

## Multisig Probe Results

All 5 multisig contracts are healthy with 2 signatures required.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...4987003 | 2 | true |
| A-G | 0xf56c4a1c...bc0096 | 2 | true |
| Y-Z | 0xd3ffe181...75b883 | 2 | true |
| S-T | 0x3b1c3ae9...ed7883 | 2 | true |
| V-W | 0x40fad7b4...80eb6d | 2 | true |

---

## MNX Markets

**Status: unavailable** — `testnet.mnx.fi/api/markets` and `/api/v1/markets` return HTML (Next.js SPA), no JSON API accessible from this environment.

---

## GF3 Color Chain Summary

Applied cyclically (id % 3) to 413 world increment entries:

| trit | color | name | count |
|------|-------|------|-------|
| 0 | #d3869b (mauve) | ERGODIC | 137 |
| 1 | #b8bb26 (lime) | PLUS | 138 |
| -1 | #cc241d (red) | MINUS | 138 |

GF(3) encodes the ternary logic of world increments: ERGODIC (0, identity), PLUS (+1, forward), MINUS (-1, reverse).

---

## Database

Path: `/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb`

Tables:
- `world_increments` — 413 rows
- `repo_snapshots` — 390 rows (one per repo)
- `aptos_snapshots` — 28 rows (A-Z + alice + bob)
- `multisig_probes` — 5 rows
- `mnx_snapshots` — 0 rows (unavailable)
