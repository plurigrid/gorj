# World Increment Sweep — LATEST_SWEEP.md

**Date/Time of Sweep:** 2026-04-03T22:30:00Z (UTC)

---

## GitHub Snapshot

- **Orgs queried:** 3 (plurigrid, kubeflow, TeglonLabs)
- **Users queried:** 8 (bmorphism, zubyul, migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone)
- **Total repos snapshotted:** 469

### Top 10 Most Recently Pushed Repos

| full_name | language | stars | pushed_at |
|-----------|----------|-------|-----------|
| plurigrid/gorj | Clojure | 0 | 2026-04-03T22:12:54Z |
| kubeflow/model-registry | Go | 171 | 2026-04-03T21:46:07Z |
| plurigrid/horse | TeX | 1 | 2026-04-03T21:15:47Z |
| kubeflow/pipelines | Python | 4117 | 2026-04-03T21:06:07Z |
| kubeflow/trainer | Go | 2074 | 2026-04-03T18:19:35Z |
| kubeflow/community | Jsonnet | 193 | 2026-04-03T16:13:47Z |
| kubeflow/website | HTML | 183 | 2026-04-03T15:23:07Z |
| kubeflow/notebooks | (none) | 70 | 2026-04-03T13:47:07Z |
| M1shaaa/M1shaaa | (none) | 0 | 2026-04-03T12:57:25Z |
| kubeflow/kale | Python | 681 | 2026-04-02T20:54:38Z |

---

## GF(3) Color Chain Summary

11 world_increment rows, one per source (org or user):

| id | source | trit | color | name |
|----|--------|------|-------|------|
| 1 | plurigrid (org) | 1 | #b8bb26 | PLUS |
| 2 | kubeflow (org) | -1 | #cc241d | MINUS |
| 3 | TeglonLabs (org) | 0 | #d3869b | ERGODIC |
| 4 | bmorphism (user) | 1 | #b8bb26 | PLUS |
| 5 | zubyul (user) | -1 | #cc241d | MINUS |
| 6 | migalkin (user) | 0 | #d3869b | ERGODIC |
| 7 | DJedamski (user) | 1 | #b8bb26 | PLUS |
| 8 | wasita (user) | -1 | #cc241d | MINUS |
| 9 | kristinezheng (user) | 0 | #d3869b | ERGODIC |
| 10 | M1shaaa (user) | 1 | #b8bb26 | PLUS |
| 11 | AustinCStone (user) | -1 | #cc241d | MINUS |

Rule: id%3==0 -> trit=0, color=#d3869b, name=ERGODIC; id%3==1 -> trit=1, color=#b8bb26, name=PLUS; id%3==2 -> trit=-1, color=#cc241d, name=MINUS

---

## Aptos Wallet Balances

All addresses returned 0.0 APT (resource not found on mainnet for these addresses).

| label | address (truncated) | balance_apt |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...f588 | 0.0 |
| U | 0x7586...9956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

---

## Multisig Probes

All multisig accounts returned valid integer (2 sigs required), all healthy.

| pair | address (truncated) | sigs_required | healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

---

## MNX Markets

**Status: unavailable**

The endpoint `https://testnet.mnx.fi/api/markets` (and variants `/api/tickers`, `/api/v1/markets`) returned HTML (Next.js SPA), not JSON market data. No structured ticker/price data could be parsed.

---

## DuckDB File

`/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb`

Tables:
- `world_increments` -- 11 rows (one per source)
- `repo_snapshots` -- 469 rows
- `aptos_snapshots` -- 28 rows
- `multisig_probes` -- 5 rows
- `mnx_snapshots` -- 0 rows (data unavailable)
