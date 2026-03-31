# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-03-31T00:00:00Z (UTC)
**DuckDB Version:** v1.5.1 (Variegata)
**Database:** `world-increments.duckdb`

---

## GitHub Sweep Summary

### Repo Counts by Source

| Source | Type | Unique Repos Fetched |
|--------|------|---------------------|
| bmorphism | user | 97 |
| plurigrid | org | 93 |
| kubeflow | org | 46 |
| zubyul | user | 44 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| wasita | user | 9 |
| M1shaaa | user | 8 |
| kristinezheng | user | 6 |
| DJedamski | user | 6 |
| TeglonLabs | org | 3 |
| **Total** | | **371** |

### Top Repos by Stars

| Repository | Stars | Language |
|-----------|-------|----------|
| kubeflow/kubeflow | 15,550 | — |
| kubeflow/pipelines | 4,117 | Python |
| kubeflow/spark-operator | 3,111 | Python |
| kubeflow/trainer | 2,071 | Go |
| kubeflow/katib | 1,465 | Go |

### Notes
- GitHub API rate-limited for unauthenticated curl; all data retrieved via GitHub MCP search tool
- Social graph users (zubyul follows): migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone

---

## GF(3) Color Chain Summary

**Rule:** `id % 3 == 0` → trit=0 ERGODIC (#d3869b), `id % 3 == 1` → trit=1 PLUS (#b8bb26), `id % 3 == 2` → trit=-1 MINUS (#cc241d)

| GF3 Name | Color | Trit | Row Count (world_increments) |
|----------|-------|------|------------------------------|
| ERGODIC | #d3869b (pink) | 0 | 107 |
| PLUS | #b8bb26 (yellow-green) | 1 | 109 |
| MINUS | #cc241d (red) | -1 | 108 |

---

## Aptos Wallet Balances

All 28 wallets queried against `fullnode.mainnet.aptoslabs.com`. All returned 0 APT (accounts not found / no CoinStore resource at these addresses).

| Name | Address (truncated) | Balance (APT) |
|------|---------------------|--------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...12d5 | 0.0 |
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
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...9956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

---

## Multisig Probe Results

All 5 probed contracts responded successfully with `sigs_required = 2`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

---

## MNX Market Status

**Status: UNAVAILABLE — returns SPA HTML (Next.js)**

Both `https://testnet.mnx.fi/api/markets` and `https://testnet.mnx.fi/api/v1/markets` return a Next.js HTML page rather than JSON. The testnet REST API is not publicly accessible. No market ticker data recorded.

---

## DuckDB Table Row Counts

| Table | Rows |
|-------|------|
| world_increments | 324 |
| repo_snapshots | 999 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (unavailability placeholder) |
| **Total** | **1,357** |

> Note: `repo_snapshots` row count (999) reflects raw inserts from search pagination; unique source repos total 371.
