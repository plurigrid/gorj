# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-16T00:00:00Z  
**GF(3) Color Chain:** ERGODIC #d3869b / PLUS #b8bb26 / MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured | Top Stars | Total Stars |
|--------|------|---------------|-----------|-------------|
| kubeflow | org | 48 | 15,725 | 101,935 |
| migalkin | user (social) | 19 | 144 | 834 |
| bmorphism | user | 100 | 61 | 503 |
| AustinCStone | user (social) | 40 | 92 | 324 |
| plurigrid | org | 100 | 26 | 157 |
| zubyul | user | 49 | 2 | 40 |
| DJedamski | user (social) | 6 | 2 | 17 |
| TeglonLabs | org | 5 | 2 | 14 |
| wasita | user (social) | 11 | 2 | 11 |
| kristinezheng | user (social) | 5 | 0 | 0 |
| M1shaaa | user (social) | 8 | 0 | 0 |

**Total repo snapshots:** 391 unique repos -> 1,335 snapshot rows (multiple search pages)

### GF(3) Trit Distribution (world_increments, 414 rows)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 1 | #b8bb26 | PLUS | 139 |
| -1 | #cc241d | MINUS | 138 |
| 0 | #d3869b | ERGODIC | 137 |

### Notable Activity (2026)

| Org/User | Repo | Language | Stars | Last Push |
|----------|------|----------|-------|-----------|
| kubeflow | kubeflow | - | 15,725 | 2026-06-11 |
| kubeflow | pipelines | Python | 4,154 | 2026-06-16 |
| kubeflow | spark-operator | Python | 3,127 | 2026-06-15 |
| kubeflow | trainer | Go | 2,115 | 2026-06-16 |
| kubeflow | community-distribution | YAML | 1,024 | 2026-06-16 |
| TeglonLabs | jank-crane | C++ | 0 | 2026-06-08 |
| kristinezheng | kristinezheng.github.io | HTML | 0 | 2026-06-07 |
| M1shaaa | M1shaaa (profile) | - | 0 | 2026-06-16 |
| wasita | wasita.github.io | Svelte | 1 | 2026-06-15 |
| AustinCStone | EpsteinSearch | Python | 0 | 2026-02-11 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793... | 0.0 |
| bob | 0x0a3c... | 0.0 |
| A | 0x8699... | 0.0 |
| B | 0x3f89... | 0.0 |
| C | 0x38b9... | 0.0 |
| D | 0xf776... | 0.0 |
| E | 0xdc1d... | 0.0 |
| F | 0x18a1... | 0.0 |
| G | 0x69a3... | 0.0 |
| H | 0xce67... | 0.0 |
| I | 0x070f... | 0.0 |
| J | 0x4d96... | 0.0 |
| K | 0xa732... | 0.0 |
| L | 0x7c2e... | 0.0 |
| M | 0x6fed... | 0.0 |
| N | 0xe7dd... | 0.0 |
| O | 0x7325... | 0.0 |
| P | 0x6218... | 0.0 |
| Q | 0xac40... | 0.0 |
| R | 0x7ce6... | 0.0 |
| S | 0xb875... | 0.0 |
| T | 0x3578... | 0.0 |
| U | 0x7586... | 0.0 |
| V | 0xb59d... | 0.0 |
| W | 0x5f32... | 0.0 |
| X | 0xa95c... | 0.0 |
| Y | 0xd8e3... | 0.0 |
| Z | 0x7af0... | 0.0 |

**Finding:** All 28 addresses return no initialized CoinStore resource on Aptos mainnet (accounts un-funded or CoinStore not registered). Total swarm APT: **0.0 APT**.

### Multisig Contract Probes (5 pairs)

All probes called `0x1::multisig_account::num_signatures_required`. All returned `["2"]`.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428... | 2 | HEALTHY |
| A-G | 0xf56c4a1c... | 2 | HEALTHY |
| Y-Z | 0xd3ffe181... | 2 | HEALTHY |
| S-T | 0x3b1c3ae9... | 2 | HEALTHY |
| V-W | 0x40fad7b4... | 2 | HEALTHY |

**All 5 multisig accounts live and require 2-of-N signatures.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** - testnet.mnx.fi is protected behind Vercel deployment authentication. Neither root nor /api/markets nor /api/v1/markets returned market data. Requires Vercel bypass token or Trusted Sources OIDC token.

---

## DuckDB Tables Summary

| Table | Rows |
|-------|------|
| world_increments | 414 |
| repo_snapshots | 1,335 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

Database: `packages/world-increment/ducklake/world-increments.duckdb`
