# World-Increment Sweep + Hamming Snapshot

**Date/Time:** 2026-04-07T15:45:00Z
**DuckDB version:** v1.5.1 (Variegata)
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Job 1: GitHub Social Graph Sweep

### Sources Queried

**Orgs (3):** plurigrid, kubeflow, TeglonLabs
**Users (8):** bmorphism, zubyul, migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone

Events snapshots also fetched for bmorphism and zubyul (30 events each).

### Repo Counts by Source

| type | source        | repos |
|------|---------------|-------|
| org  | plurigrid     | 100   |
| org  | kubeflow      | 46    |
| org  | TeglonLabs    | 53    |
| user | bmorphism     | 100   |
| user | zubyul        | 23    |
| user | migalkin      | 30    |
| user | DJedamski     | 11    |
| user | wasita        | 29    |
| user | kristinezheng | 18    |
| user | AustinCStone  | 43    |
| user | M1shaaa       | 16    |
| **TOTAL** | | **469** |

### GF(3) Color Chain Stats

11 world_increment records assigned via GF(3) modular arithmetic (id % 3):

| id | source        | trit | color    | name    |
|----|---------------|------|----------|---------|
| 1  | plurigrid     | +1   | #b8bb26  | PLUS    |
| 2  | kubeflow      | -1   | #cc241d  | MINUS   |
| 3  | TeglonLabs    |  0   | #d3869b  | ERGODIC |
| 4  | bmorphism     | +1   | #b8bb26  | PLUS    |
| 5  | zubyul        | -1   | #cc241d  | MINUS   |
| 6  | migalkin      |  0   | #d3869b  | ERGODIC |
| 7  | DJedamski     | +1   | #b8bb26  | PLUS    |
| 8  | wasita        | -1   | #cc241d  | MINUS   |
| 9  | kristinezheng |  0   | #d3869b  | ERGODIC |
| 10 | AustinCStone  | +1   | #b8bb26  | PLUS    |
| 11 | M1shaaa       | -1   | #cc241d  | MINUS   |

Chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`
Tally: PLUS=4, MINUS=4, ERGODIC=3

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15557 | — |
| kubeflow/pipelines | 4118 | Python |
| kubeflow/spark-operator | 3111 | Python |
| kubeflow/trainer | 2075 | Go |
| kubeflow/katib | 1674 | Python |
| kubeflow/examples | 1458 | Jsonnet |
| kubeflow/manifests | 1009 | YAML |
| kubeflow/arena | 808 | Go |
| kubeflow/kale | 682 | Python |
| kubeflow/mpi-operator | 520 | Go |

---

## Job 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Aptos Wallet Balances

All queried via `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| Label | Address (truncated)           | Balance (APT) |
|-------|-------------------------------|---------------|
| alice | 0xc793...4cc7b                | 0.0           |
| bob   | 0x0a3c...512d5d               | 0.0           |
| A     | 0x8699...be9d7a               | 0.0           |
| B     | 0x3f89...577cb13              | 0.0           |
| C     | 0x38b9...91535e               | 0.0           |
| D     | 0xf776...fcfdd1               | 0.0           |
| E     | 0xdc1d...958d36               | 0.0           |
| F     | 0x18a1...4c3cf71              | 0.0           |
| G     | 0x69a3...cc7f32               | 0.0           |
| H     | 0xce67...e5300f               | 0.0           |
| I     | 0x070f...0c1fc9               | 0.0           |
| J     | 0x4d96...e87f54               | 0.0           |
| K     | 0xa732...425dc4               | 0.0           |
| L     | 0x7c2e...37eba9               | 0.0           |
| M     | 0x6fed...b7f2e9               | 0.0           |
| N     | 0xe7dd...1551b2c              | 0.0           |
| O     | 0x7325...525a89d              | 0.0           |
| P     | 0x6218...1ec948               | 0.0           |
| Q     | 0xac40...5c89a9               | 0.0           |
| R     | 0x7ce6...d76e10               | 0.0           |
| S     | 0xb875...99d0386              | 0.0           |
| T     | 0x3578...3f4588               | 0.0           |
| U     | 0x7586...ef9956               | 0.0           |
| V     | 0xb59d...89af2c3              | 0.0           |
| W     | 0x5f32...6ccc7b0              | 0.0           |
| X     | 0xa95c...be33047d             | 0.0           |
| Y     | 0xd8e3...2444c4               | 0.0           |
| Z     | 0x7af0...e197c                | 0.0           |

All 28 addresses returned 0.0 APT (accounts unfunded on mainnet or CoinStore not initialized).

### Multisig Probes

Queried via `0x1::multisig_account::num_signatures_required` view function.

| Pair | Multisig Address (truncated) | Sigs Required | Healthy |
|------|------------------------------|---------------|---------|
| A-B  | 0x0da4...87003               | 2             | true    |
| A-G  | 0xf56c...0096                | 2             | true    |
| Y-Z  | 0xd3ff...b883                | 2             | true    |
| S-T  | 0x3b1c...7883                | 2             | true    |
| V-W  | 0x40fa...0eb6d               | 2             | true    |

All 5 multisig accounts are healthy with 2-of-N signing threshold.

---

## MNX Markets

**Status: unavailable** — `https://testnet.mnx.fi/api/markets`, `/api/tickers`, and `/api/v1/markets` all return Next.js SSR HTML, not a JSON API endpoint. No structured market data extractable.

---

## DuckDB Storage Summary

File: `packages/world-increment/ducklake/world-increments.duckdb`

| Table             | Rows |
|-------------------|------|
| world_increments  | 11   |
| repo_snapshots    | 469  |
| aptos_snapshots   | 28   |
| multisig_probes   | 5    |
| mnx_snapshots     | 0    |

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
