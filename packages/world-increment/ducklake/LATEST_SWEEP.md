# LATEST_SWEEP.md — World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-08  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried (This Run)
| Source | Type | Unique Repos |
|--------|------|-------------|
| plurigrid | org | 168 |
| bmorphism | user | 165 |
| zubyul | user | 59 |
| TeglonLabs | org | 54 |
| kubeflow | org | 51 |
| AustinCStone | user | 43 |
| wasita | user | 32 |
| migalkin | user | 30 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |

### Cumulative DuckDB State
- **world_increments:** 415 rows total (all sweeps)
- **repo_snapshots:** 1336 rows total (all sweeps)

### GF(3) Color Chain Distribution (All Sweeps)
| Trit | Name | Color | Count |
|------|------|-------|-------|
| -1 (MINUS) | MINUS | `#cc241d` | 139 |
| 0 (ERGODIC) | ERGODIC | `#d3869b` | 137 |
| +1 (PLUS) | PLUS | `#b8bb26` | 139 |

### Top 15 Repos by Stars
| Repo | Stars | Forks | Last Push |
|------|-------|-------|-----------|
| kubeflow/kubeflow | 15,768 | 2,685 | 2026-07-08 |
| kubeflow/pipelines | 4,169 | 2,030 | 2026-07-08 |
| kubeflow/spark-operator | 3,135 | 1,499 | 2026-07-08 |
| kubeflow/trainer | 2,133 | 981 | 2026-07-08 |
| kubeflow/katib | 1,689 | 532 | 2026-07-08 |
| kubeflow/examples | 1,460 | 756 | 2025-04-14 |
| kubeflow/community-distribution | 1,029 | 1,071 | 2026-07-08 |
| kubeflow/manifests | 1,010 | 1,069 | 2026-04-11 |
| kubeflow/arena | 815 | 195 | 2026-07-08 |
| kubeflow/kale | 695 | 157 | 2026-07-01 |
| kubeflow/mpi-operator | 529 | 237 | 2026-07-07 |
| kubeflow/fairing | 337 | 143 | 2022-04-11 |
| kubeflow/pytorch-operator | 310 | 143 | 2021-12-01 |
| kubeflow/community | 195 | 265 | 2026-07-01 |
| kubeflow/website | 184 | 925 | 2026-07-08 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 28 addresses)
> All addresses returned `resource_not_found` for `CoinStore<AptosCoin>` — 
> accounts exist on-chain but hold 0 APT in the native coin resource.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| Z | `0x7af0ef6e1bd706...6e4e197c` | 0.0000 |
| Y | `0xd8e32848f1dffa...fa2444c4` | 0.0000 |
| X | `0xa95cbbd116548a...be33047d` | 0.0000 |
| W | `0x5f32aef70f5ba5...a6ccc7b0` | 0.0000 |
| V | `0xb59dd8170321df...a89af2c3` | 0.0000 |
| U | `0x75860da47565f6...95ef9956` | 0.0000 |
| T | `0x35781dc0e42fef...2d3f4588` | 0.0000 |
| S | `0xb8753014e4888e...f99d0386` | 0.0000 |
| R | `0x7ce605cc8fda4f...36d76e10` | 0.0000 |
| Q | `0xac40fa50b81b4c...5e5c89a9` | 0.0000 |
| P | `0x6218792de4a9bc...621ec948` | 0.0000 |
| O | `0x73252b6011a751...a525a89d` | 0.0000 |
| N | `0xe7dde6da0a65f5...11551b2c` | 0.0000 |
| M | `0x6fed37a7553ef1...49b7f2e9` | 0.0000 |
| L | `0x7c2eaeafad9725...6337eba9` | 0.0000 |
| K | `0xa732040a6b0d55...7a425dc4` | 0.0000 |
| J | `0x4d964db8f53837...93e87f54` | 0.0000 |
| I | `0x070fe5d74e4eda...c00c1fc9` | 0.0000 |
| H | `0xce67c327a7844e...94e5300f` | 0.0000 |
| G | `0x69a394c0b0ac84...dbcc7f32` | 0.0000 |
| F | `0x18a14b5b4bec11...74c3cf71` | 0.0000 |
| E | `0xdc1d9d533bac35...d0958d36` | 0.0000 |
| D | `0xf77656248f64d5...d9fcfdd1` | 0.0000 |
| C | `0x38b99e63ada9b6...2691535e` | 0.0000 |
| B | `0x3f892ebe6e4516...4577cb13` | 0.0000 |
| A | `0x8699edc0960dd5...aebe9d7a` | 0.0000 |
| bob | `0x0a3c00c58fdf90...05512d5d` | 0.0000 |
| alice | `0xc793acdec12b4a...d624cc7b` | 0.0000 |

### Multisig Contract Probes (Aptos Mainnet, 5 contracts)
All 5 multisig contracts responded healthy with **2-of-2** signature threshold.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4f428a0c007...f4987003` | 2 | ✅ healthy |
| A-G | `0xf56c4a1c090621...3fbc0096` | 2 | ✅ healthy |
| S-T | `0x3b1c3ae905d44c...3ded7883` | 2 | ✅ healthy |
| V-W | `0x40fad7b423a843...2c80eb6d` | 2 | ✅ healthy |
| Y-Z | `0xd3ffe1812b2df4...8e75b883` | 2 | ✅ healthy |

### MNX Markets (`testnet.mnx.fi`)
> **Status: Unavailable** — All API paths return "Authentication Required" (Vercel deployment protection).  
> No market data extractable without Vercel auth token.

---

## DuckDB Tables

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 415 | GF(3) colored GitHub events |
| `repo_snapshots` | 1336 | GitHub repo metadata per sweep |
| `aptos_snapshots` | 28 | Aptos wallet balance snapshots |
| `multisig_probes` | 5 | Aptos multisig contract states |
| `mnx_snapshots` | 1 | MNX market data (unavailable) |
