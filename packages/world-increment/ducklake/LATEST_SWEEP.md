# World Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-07-16  
**Run:** autonomous sweep — GF(3) color chain applied

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos Captured |
|--------|------|---------------|
| bmorphism | user | 100 |
| plurigrid | org | 100 |
| zubyul | user | 49 |
| kubeflow | org | 49 |
| migalkin | user | 5 |
| TeglonLabs | org | 5 |
| wasita | user | 4 |
| AustinCStone | user | 3 |
| M1shaaa | user | 2 |
| kristinezheng | user | 2 |
| DJedamski | user | 2 |

**Total world_increments:** 344  
**Total repo_snapshots:** 1265

### GF(3) Color Distribution

| Name | Color | Count |
|------|-------|-------|
| ERGODIC | `#d3869b` | 114 |
| MINUS | `#cc241d` | 115 |
| PLUS | `#b8bb26` | 115 |

### Top Repos by Stars

| Repo | Language | ⭐ Stars | 🍴 Forks | Last Push |
|------|----------|---------|---------|----------|
| kubeflow/kubeflow | — | 15779 | 2685 | 2026-07-10 |
| kubeflow/pipelines | Python | 4167 | 2036 | 2026-07-16 |
| kubeflow/spark-operator | Python | 3137 | 1500 | 2026-07-16 |
| kubeflow/trainer | Go | 2150 | 988 | 2026-07-16 |
| kubeflow/katib | Python | 1690 | 533 | 2026-07-16 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (APT)

| World | Address | Balance (APT) |
|-------|---------|--------------|
| bob | `0x0a3c00c5...512d5d` | 12.657007 |
| F | `0x18a14b5b...c3cf71` | 1.960516 |
| L | `0x7c2eaeaf...37eba9` | 1.927269 |
| J | `0x4d964db8...e87f54` | 1.895093 |
| alice | `0xc793acde...24cc7b` | 0.436434 |
| O | `0x73252b60...25a89d` | 0.210136 |
| K | `0xa732040a...425dc4` | 0.161961 |
| P | `0x6218792d...1ec948` | 0.140136 |
| M | `0x6fed37a7...b7f2e9` | 0.112285 |
| N | `0xe7dde6da...551b2c` | 0.106121 |
| Q | `0xac40fa50...5c89a9` | 0.103240 |
| S | `0xb8753014...9d0386` | 0.091788 |
| R | `0x7ce605cc...d76e10` | 0.090217 |
| T | `0x35781dc0...3f4588` | 0.073713 |
| U | `0x75860da4...ef9956` | 0.055773 |
| A | `0x8699edc0...be9d7a` | 0.051767 |
| V | `0xb59dd817...9af2c3` | 0.048833 |
| Y | `0xd8e32848...2444c4` | 0.044449 |
| X | `0xa95cbbd1...33047d` | 0.042577 |
| W | `0x5f32aef7...ccc7b0` | 0.040705 |
| B | `0x3f892ebe...77cb13` | 0.036256 |
| Z | `0x7af0ef6e...4e197c` | 0.024268 |
| D | `0xf7765624...fcfdd1` | 0.011629 |
| C | `0x38b99e63...91535e` | 0.010185 |
| E | `0xdc1d9d53...958d36` | 0.009372 |
| H | `0xce67c327...e5300f` | 0.001681 |
| I | `0x070fe5d7...0c1fc9` | 0.000681 |
| G | `0x69a394c0...cc7f32` | 0.000681 |

**Total APT across swarm:** `20.344773 APT`  
**Note:** Balances queried via `0x1::coin::balance` view function (covers both Coin and FA stores).

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | `0x0da4f428...987003` | 2 | ✅ |
| A-G | `0xf56c4a1c...bc0096` | 2 | ✅ |
| Y-Z | `0xd3ffe181...75b883` | 2 | ✅ |
| S-T | `0x3b1c3ae9...ed7883` | 2 | ✅ |
| V-W | `0x40fad7b4...80eb6d` | 2 | ✅ |

All 5 multisig contracts respond to `0x1::multisig_account::num_signatures_required` — all require **2 signatures**.

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — `testnet.mnx.fi` returns HTTP 401 (Vercel authentication required). No market data retrievable without credentials.

---

## DuckDB Tables Summary

| Table | Rows |
|-------|------|
| `world_increments` | 344 |
| `repo_snapshots` | 1265 |
| `aptos_snapshots` | 28 |
| `multisig_probes` | 5 |
| `mnx_snapshots` | 0 |

**Database:** `packages/world-increment/ducklake/world-increments.duckdb`
