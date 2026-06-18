# World Increment Sweep — 2026-06-18 09:12 UTC

## Summary

| Table | Count |
|-------|-------|
| world_increments | 158 |
| repo_snapshots (all-time) | 1079 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Indexed

| Org/User | Repos |
|----------|-------|
| plurigrid | 114 |
| bmorphism | 110 |
| TeglonLabs | 54 |
| kubeflow | 47 |
| AustinCStone | 43 |
| wasita | 32 |
| migalkin | 30 |
| zubyul | 27 |
| kristinezheng | 18 |
| M1shaaa | 16 |
| DJedamski | 11 |

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15732 |  |
| kubeflow/pipelines | 4154 | Python |
| kubeflow/spark-operator | 3127 | Python |
| kubeflow/trainer | 2115 | Go |
| kubeflow/katib | 1683 | Python |
| kubeflow/examples | 1460 | Jsonnet |
| kubeflow/manifests | 1010 | YAML |
| kubeflow/arena | 812 | Go |
| kubeflow/kale | 694 | Python |
| kubeflow/mpi-operator | 528 | Go |
| kubeflow/fairing | 337 | Jsonnet |
| kubeflow/pytorch-operator | 309 | Jsonnet |
| kubeflow/community | 195 | Jsonnet |
| kubeflow/website | 184 | HTML |
| kubeflow/kfctl | 182 | Go |

### GF(3) Color Chain

Each world_increment is colored by `id % 3`:
- `trit=0` → ERGODIC `#d3869b`
- `trit=1` → PLUS `#b8bb26`  
- `trit=-1` → MINUS `#cc241d`

### Notable Activity (2026-06-18)

- **plurigrid/gorj** pushed today (645 open issues — active development)
- **kubeflow/trainer** pushed today (2115 stars, Go, distributed training)
- **bmorphism/Gay.jl** pushed today (187 open issues — high activity)
- **M1shaaa/M1shaaa** profile pushed today

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 Hamming swarm wallets queried on Aptos mainnet (ledger v5796958906).

| World | Address | Balance (APT) |
|-------|---------|---------------|
| A | `0x8699edc0...be9d7a` | 0.0000 |
| B | `0x3f892ebe...77cb13` | 0.0000 |
| C | `0x38b99e63...91535e` | 0.0000 |
| D | `0xf7765624...fcfdd1` | 0.0000 |
| E | `0xdc1d9d53...958d36` | 0.0000 |
| F | `0x18a14b5b...c3cf71` | 0.0000 |
| G | `0x69a394c0...cc7f32` | 0.0000 |
| H | `0xce67c327...e5300f` | 0.0000 |
| I | `0x070fe5d7...0c1fc9` | 0.0000 |
| J | `0x4d964db8...e87f54` | 0.0000 |
| K | `0xa732040a...425dc4` | 0.0000 |
| L | `0x7c2eaeaf...37eba9` | 0.0000 |
| M | `0x6fed37a7...b7f2e9` | 0.0000 |
| N | `0xe7dde6da...551b2c` | 0.0000 |
| O | `0x73252b60...25a89d` | 0.0000 |
| P | `0x6218792d...1ec948` | 0.0000 |
| Q | `0xac40fa50...5c89a9` | 0.0000 |
| R | `0x7ce605cc...d76e10` | 0.0000 |
| S | `0xb8753014...9d0386` | 0.0000 |
| T | `0x35781dc0...3f4588` | 0.0000 |
| U | `0x75860da4...ef9956` | 0.0000 |
| V | `0xb59dd817...9af2c3` | 0.0000 |
| W | `0x5f32aef7...ccc7b0` | 0.0000 |
| X | `0xa95cbbd1...33047d` | 0.0000 |
| Y | `0xd8e32848...2444c4` | 0.0000 |
| Z | `0x7af0ef6e...4e197c` | 0.0000 |
| alice | `0xc793acde...24cc7b` | 0.0000 |
| bob | `0x0a3c00c5...512d5d` | 0.0000 |

> **Note:** All wallets return `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
> This indicates APT CoinStore not initialized — accounts may hold other assets or are pre-funded wallets.

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428...987003` | 2 | ✓ |
| A-G | `0xf56c4a1c...bc0096` | 2 | ✓ |
| Y-Z | `0xd3ffe181...75b883` | 2 | ✓ |
| S-T | `0x3b1c3ae9...ed7883` | 2 | ✓ |
| V-W | `0x40fad7b4...80eb6d` | 2 | ✓ |

> All 5 multisig contracts require **2 signatures**. All healthy.

### MNX Markets

`testnet.mnx.fi` requires Vercel authentication — API data unavailable this sweep.

---

## DuckDB Ducklake Path

```
packages/world-increment/ducklake/world-increments.duckdb
```

Accumulates world-increment sweeps over time. Each run appends new snapshots.
