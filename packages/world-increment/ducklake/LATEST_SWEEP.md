# World Increment Sweep - LATEST_SWEEP

**Date/Time:** 2026-04-02 05:20:49 UTC

**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## GitHub Data Collection

**Total repos collected:** 307 across 11 orgs/users

### Repo counts per org/user

| Source | Type | Repos |
|--------|------|-------|
| AustinCStone | user | 43 |
| DJedamski | user | 11 |
| M1shaaa | user | 16 |
| TeglonLabs | org | 3 |
| bmorphism | user | 100 |
| kristinezheng | user | 6 |
| kubeflow | org | 46 |
| migalkin | user | 30 |
| plurigrid | org | 20 |
| wasita | user | 9 |
| zubyul | user | 23 |

### Top 10 Repos by Stars

| Repo | Stars | Forks | Language |
|------|-------|-------|----------|
| kubeflow/kubeflow | 15548 | 2627 | N/A |
| kubeflow/pipelines | 4118 | 1983 | Python |
| kubeflow/spark-operator | 3110 | 1480 | Python |
| kubeflow/trainer | 2070 | 943 | Go |
| kubeflow/katib | 1674 | 520 | Python |
| kubeflow/examples | 1459 | 755 | Jsonnet |
| kubeflow/manifests | 1006 | 1067 | YAML |
| kubeflow/arena | 809 | 190 | Go |
| kubeflow/kale | 681 | 156 | Python |
| kubeflow/mpi-operator | 519 | 236 | Go |

---

## Aptos Wallet Balances (Mainnet)

All balances queried via `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | `0xc793acde...24cc7b` | 0.00000000 |
| bob | `0x0a3c00c5...512d5d` | 0.00000000 |
| A | `0x8699edc0...be9d7a` | 0.00000000 |
| B | `0x3f892ebe...77cb13` | 0.00000000 |
| C | `0x38b99e63...91535e` | 0.00000000 |
| D | `0xf7765624...fcfdd1` | 0.00000000 |
| E | `0xdc1d9d53...958d36` | 0.00000000 |
| F | `0x18a14b5b...c3cf71` | 0.00000000 |
| G | `0x69a394c0...cc7f32` | 0.00000000 |
| H | `0xce67c327...e5300f` | 0.00000000 |
| I | `0x070fe5d7...0c1fc9` | 0.00000000 |
| J | `0x4d964db8...e87f54` | 0.00000000 |
| K | `0xa732040a...425dc4` | 0.00000000 |
| L | `0x7c2eaeaf...37eba9` | 0.00000000 |
| M | `0x6fed37a7...b7f2e9` | 0.00000000 |
| N | `0xe7dde6da...551b2c` | 0.00000000 |
| O | `0x73252b60...25a89d` | 0.00000000 |
| P | `0x6218792d...1ec948` | 0.00000000 |
| Q | `0xac40fa50...5c89a9` | 0.00000000 |
| R | `0x7ce605cc...d76e10` | 0.00000000 |
| S | `0xb8753014...9d0386` | 0.00000000 |
| T | `0x35781dc0...3f4588` | 0.00000000 |
| U | `0x75860da4...ef9956` | 0.00000000 |
| V | `0xb59dd817...9af2c3` | 0.00000000 |
| W | `0x5f32aef7...ccc7b0` | 0.00000000 |
| X | `0xa95cbbd1...33047d` | 0.00000000 |
| Y | `0xd8e32848...2444c4` | 0.00000000 |
| Z | `0x7af0ef6e...4e197c` | 0.00000000 |

**Note:** All addresses returned 0 APT balance (accounts may be unfunded or not yet activated on mainnet).

---

## Multisig Account Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | `0x0da4f428...987003` | 2 | YES |
| A-G | `0xf56c4a1c...bc0096` | 2 | YES |
| Y-Z | `0xd3ffe181...75b883` | 2 | YES |
| S-T | `0x3b1c3ae9...ed7883` | 2 | YES |
| V-W | `0x40fad7b4...80eb6d` | 2 | YES |

All multisig accounts returned `num_signatures_required = 2` (healthy 2-of-N multisig).

---

## MNX Markets

**Status:** Unavailable as JSON API endpoint.

`https://testnet.mnx.fi/api/markets` and `https://testnet.mnx.fi/api/tickers` return HTML (Next.js web app), not a JSON API response. No market data could be parsed.

---

## GF(3) Color Chain Summary

| id % 3 | Trit | Color | Hex |
|--------|------|-------|-----|
| 0 | 0 | ERGODIC | `#d3869b` |
| 1 | 1 | PLUS | `#b8bb26` |
| 2 | 2 (= -1) | MINUS | `#cc241d` |

World increments are assigned GF(3) color trits sequentially by source insertion order.

---

## Database Tables

| Table | Row Count |
|-------|-----------|
| world_increments | 11 |
| repo_snapshots | 307 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |
