# World Increment Sweep — 2026-04-15

## Part 1: GitHub Repository Snapshot

### Repos per Source

| Source | Type | Count |
|--------|------|-------|
| plurigrid | org | 99 |
| bmorphism | user | 99 |
| kubeflow | org | 47 |
| zubyul | user | 47 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| wasita | user | 10 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| kristinezheng | user | 6 |
| TeglonLabs | org | 4 |

**Total repos snapshotted: 385**

### Top 15 Repos by Stars

| # | Repo | Language | Stars | Forks |
|---|------|----------|-------|-------|
| 1 | kubeflow/kubeflow | N/A | 15,575 | 2,636 |
| 2 | kubeflow/pipelines | Python | 4,118 | 1,985 |
| 3 | kubeflow/spark-operator | Python | 3,114 | 1,483 |
| 4 | kubeflow/trainer | Go | 2,084 | 945 |
| 5 | kubeflow/katib | Python | 1,678 | 521 |
| 6 | kubeflow/examples | Jsonnet | 1,460 | 756 |
| 7 | kubeflow/manifests | YAML | 1,010 | 1,069 |
| 8 | kubeflow/arena | Go | 809 | 190 |
| 9 | kubeflow/kale | Python | 683 | 156 |
| 10 | kubeflow/mpi-operator | Go | 523 | 236 |
| 11 | kubeflow/fairing | Jsonnet | 337 | 143 |
| 12 | kubeflow/pytorch-operator | Jsonnet | 309 | 143 |
| 13 | kubeflow/community | Jsonnet | 195 | 255 |
| 14 | kubeflow/website | HTML | 184 | 914 |
| 15 | kubeflow/kfp-tekton | TypeScript | 182 | 123 |

## Part 2: Aptos Wallet Balances

Balances retrieved via `0x1::coin::balance` view function on Aptos mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| bob | `0x0a3c00c58f...512d5d` | 12.65700700 |
| F | `0x18a14b5b4b...c3cf71` | 1.96051600 |
| L | `0x7c2eaeafad...37eba9` | 1.92726900 |
| J | `0x4d964db8f5...e87f54` | 1.89509300 |
| alice | `0xc793acdec1...24cc7b` | 0.43643352 |
| O | `0x73252b6011...25a89d` | 0.21013600 |
| K | `0xa732040a6b...425dc4` | 0.16196100 |
| P | `0x6218792de4...1ec948` | 0.14013600 |
| M | `0x6fed37a755...b7f2e9` | 0.11228500 |
| N | `0xe7dde6da0a...551b2c` | 0.10612100 |
| Q | `0xac40fa50b8...5c89a9` | 0.10324000 |
| S | `0xb8753014e4...9d0386` | 0.09178800 |
| R | `0x7ce605cc8f...d76e10` | 0.09021700 |
| T | `0x35781dc0e4...3f4588` | 0.07371300 |
| U | `0x75860da475...ef9956` | 0.05577300 |
| A | `0x8699edc096...be9d7a` | 0.05176700 |
| V | `0xb59dd81703...9af2c3` | 0.04883299 |
| Y | `0xd8e32848f1...2444c4` | 0.04444900 |
| X | `0xa95cbbd116...33047d` | 0.04257700 |
| W | `0x5f32aef70f...ccc7b0` | 0.04070500 |
| B | `0x3f892ebe6e...77cb13` | 0.03625600 |
| Z | `0x7af0ef6e1b...4e197c` | 0.02426800 |
| D | `0xf77656248f...fcfdd1` | 0.01162900 |
| C | `0x38b99e63ad...91535e` | 0.01018500 |
| E | `0xdc1d9d533b...958d36` | 0.00937200 |
| H | `0xce67c327a7...e5300f` | 0.00168100 |
| G | `0x69a394c0b0...cc7f32` | 0.00068100 |
| I | `0x070fe5d74e...0c1fc9` | 0.00068100 |

**Total APT across all wallets: 20.34477251 APT**

## Part 3: Multisig Probes

All 5 multisig pairs probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | `0x0da4f428a0...987003` | 2 | YES |
| A-G | `0xf56c4a1c09...bc0096` | 2 | YES |
| Y-Z | `0xd3ffe1812b...75b883` | 2 | YES |
| S-T | `0x3b1c3ae905...ed7883` | 2 | YES |
| V-W | `0x40fad7b423...80eb6d` | 2 | YES |

**All 5 multisig accounts are healthy, all require 2-of-N signatures.**

## Part 4: MNX Market Status

- `https://testnet.mnx.fi/api/markets` — HTTP 404 (route not found)
- `https://testnet.mnx.fi/api/v1/markets` — HTTP 404 (route not found)
- `https://testnet.mnx.fi` — Returns Next.js SPA HTML (site is live but no public REST API)
- `https://testnet.mnx.fi/api/v2/markets` — HTTP 200 but returns HTML (SPA fallback)

**MNX testnet is accessible as a web app but exposes no public JSON market data API. `mnx_snapshots` table is empty.**

## Part 5: DuckDB Storage Summary

Database: `/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 385 |
| repo_snapshots | 385 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

## Part 6: GF(3) Color Chain Stats

GF(3) assignment based on `id % 3` for each world increment:

| Trit | Value | Name | Color | Count |
|------|-------|------|-------|-------|
| 0 | 0 | ERGODIC | `#d3869b` (pink) | 128 |
| 1 | 1 | PLUS | `#b8bb26` (yellow-green) | 129 |
| 2 | -1 | MINUS | `#cc241d` (red) | 128 |

Total increments: 385 (balanced distribution across GF(3) trits)
