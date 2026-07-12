# LATEST_SWEEP — 2026-07-12T23:11:56Z

## World-Increment GitHub Social Graph Sweep

**Total world_increments:** 353  
**Unique repos snapshotted:** 647  
**Aptos wallet snapshots:** 28  
**Multisig probes:** 5  

---

## GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| -1 | #cc241d | MINUS | 118 |
| 0 | #d3869b | ERGODIC | 117 |
| 1 | #b8bb26 | PLUS | 118 |

---

## GitHub Repo Snapshots by Source

| Org / User | Unique Repos | Max Stars |
|-----------|-------------|-----------|
| plurigrid | 168 | 30 |
| bmorphism | 165 | 61 |
| zubyul | 59 | 2 |
| TeglonLabs | 54 | 2 |
| kubeflow | 51 | 15772 |
| AustinCStone | 43 | 92 |
| wasita | 32 | 2 |
| migalkin | 30 | 144 |
| kristinezheng | 18 | 0 |
| M1shaaa | 16 | 0 |
| DJedamski | 11 | 2 |


**Sources:** plurigrid (100), bmorphism (100), kubeflow (49), zubyul (49), TeglonLabs (5), migalkin (19), AustinCStone (30+), wasita (11), DJedamski (6), kristinezheng (5), M1shaaa (8)

---

## Top 15 Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15772 | - |
| kubeflow/pipelines | 4169 | Python |
| kubeflow/spark-operator | 3137 | Python |
| kubeflow/trainer | 2137 | Go |
| kubeflow/katib | 1690 | Python |
| kubeflow/examples | 1460 | Jsonnet |
| kubeflow/community-distribution | 1029 | YAML |
| kubeflow/manifests | 1010 | YAML |
| kubeflow/arena | 815 | Go |
| kubeflow/kale | 695 | Python |
| kubeflow/mpi-operator | 529 | Go |
| kubeflow/fairing | 337 | Jsonnet |
| kubeflow/pytorch-operator | 310 | Jsonnet |
| kubeflow/community | 195 | Jupyter Notebook |
| kubeflow/website | 184 | HTML |

---

## Hamming Swarm — Aptos Wallet Snapshot

> Queried via `fullnode.mainnet.aptoslabs.com` on 2026-07-12T23:11:56Z

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| A | `0x8699edc096...be9d7a` | 0.00000000 |
| B | `0x3f892ebe6e...77cb13` | 0.00000000 |
| C | `0x38b99e63ad...91535e` | 0.00000000 |
| D | `0xf77656248f...fcfdd1` | 0.00000000 |
| E | `0xdc1d9d533b...958d36` | 0.00000000 |
| F | `0x18a14b5b4b...c3cf71` | 0.00000000 |
| G | `0x69a394c0b0...cc7f32` | 0.00000000 |
| H | `0xce67c327a7...e5300f` | 0.00000000 |
| I | `0x070fe5d74e...0c1fc9` | 0.00000000 |
| J | `0x4d964db8f5...e87f54` | 0.00000000 |
| K | `0xa732040a6b...425dc4` | 0.00000000 |
| L | `0x7c2eaeafad...37eba9` | 0.00000000 |
| M | `0x6fed37a755...b7f2e9` | 0.00000000 |
| N | `0xe7dde6da0a...551b2c` | 0.00000000 |
| O | `0x73252b6011...25a89d` | 0.00000000 |
| P | `0x6218792de4...1ec948` | 0.00000000 |
| Q | `0xac40fa50b8...5c89a9` | 0.00000000 |
| R | `0x7ce605cc8f...d76e10` | 0.00000000 |
| S | `0xb8753014e4...9d0386` | 0.00000000 |
| T | `0x35781dc0e4...3f4588` | 0.00000000 |
| U | `0x75860da475...ef9956` | 0.00000000 |
| V | `0xb59dd81703...9af2c3` | 0.00000000 |
| W | `0x5f32aef70f...ccc7b0` | 0.00000000 |
| X | `0xa95cbbd116...33047d` | 0.00000000 |
| Y | `0xd8e32848f1...2444c4` | 0.00000000 |
| Z | `0x7af0ef6e1b...4e197c` | 0.00000000 |
| alice | `0xc793acdec1...24cc7b` | 0.00000000 |
| bob | `0x0a3c00c58f...512d5d` | 0.00000000 |

**Note:** All addresses returned 0.0 APT — accounts do not hold CoinStore<AptosCoin> resource at mainnet. Addresses are valid and queryable.

---

## Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | `0x0da4f428a0...987003` | 2 | ✓ |
| A-G | `0xf56c4a1c09...bc0096` | 2 | ✓ |
| S-T | `0x3b1c3ae905...ed7883` | 2 | ✓ |
| V-W | `0x40fad7b423...80eb6d` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b...75b883` | 2 | ✓ |

**Status:** All 5 multisig accounts are healthy with 2-of-N signing threshold confirmed.

---

## MNX Markets

`https://testnet.mnx.fi` returns a single-page application (13,462 bytes) with no accessible REST API at probed paths. Market data: **unavailable** (SPA, no data endpoint).

---

## DuckDB Tables

- `world_increments` — GF(3)-tagged event log
- `repo_snapshots` — GitHub repo metadata at snapshot time  
- `aptos_snapshots` — Aptos wallet balance per address
- `multisig_probes` — Multisig signature threshold verification
- `mnx_snapshots` — MNX market data (empty — SPA endpoint)

Database: `packages/world-increment/ducklake/world-increments.duckdb`
