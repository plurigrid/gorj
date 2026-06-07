# LATEST_SWEEP.md

**Generated:** 2026-06-07 00:15:27 UTC
**Sweep:** world-increment sweep + hamming snapshot [GF3 color chain]

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 10 |
| zubyul | user | 5 |
| migalkin | user | 5 |
| DJedamski | user | 2 |
| wasita | user | 4 |
| kristinezheng | user | 2 |
| M1shaaa | user | 2 |
| AustinCStone | user | 3 |
| **TOTAL** | | **185** |

### Top 10 Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15706 | Unknown |
| kubeflow/pipelines | 4153 | Python |
| kubeflow/spark-operator | 3125 | Python |
| kubeflow/trainer | 2112 | Go |
| kubeflow/katib | 1685 | Python |
| kubeflow/examples | 1462 | Jsonnet |
| kubeflow/manifests | 1020 | YAML |
| kubeflow/arena | 811 | Go |
| kubeflow/kale | 691 | Python |
| kubeflow/mpi-operator | 528 | Go |

**Total stars across sweep:** 34813

### GF(3) Color Chain Summary

The 185 repo snapshots map to world_increments IDs 1–185.
Color distribution:
- ERGODIC (#d3869b, trit=0): 61 repos
- PLUS (#b8bb26, trit=1): 62 repos
- MINUS (#cc241d, trit=-1): 62 repos

### DuckDB Tables
- `world_increments`: 185 new rows (total in DB: 208)
- `repo_snapshots`: 185 new rows (total in DB: 1129)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793acde...24cc7b | 0.43643352 |
| bob | 0x0a3c00c5...512d5d | 12.65700700 |
| A | 0x8699edc0...be9d7a | 0.05176700 |
| B | 0x3f892ebe...77cb13 | 0.03625600 |
| C | 0x38b99e63...91535e | 0.01018500 |
| D | 0xf7765624...fcfdd1 | 0.01162900 |
| E | 0xdc1d9d53...958d36 | 0.00937200 |
| F | 0x18a14b5b...c3cf71 | 1.96051600 |
| G | 0x69a394c0...cc7f32 | 0.00068100 |
| H | 0xce67c327...e5300f | 0.00168100 |
| I | 0x070fe5d7...0c1fc9 | 0.00068100 |
| J | 0x4d964db8...e87f54 | 1.89509300 |
| K | 0xa732040a...425dc4 | 0.16196100 |
| L | 0x7c2eaeaf...37eba9 | 1.92726900 |
| M | 0x6fed37a7...b7f2e9 | 0.11228500 |
| N | 0xe7dde6da...551b2c | 0.10612100 |
| O | 0x73252b60...25a89d | 0.21013600 |
| P | 0x6218792d...1ec948 | 0.14013600 |
| Q | 0xac40fa50...5c89a9 | 0.10324000 |
| R | 0x7ce605cc...d76e10 | 0.09021700 |
| S | 0xb8753014...9d0386 | 0.09178800 |
| T | 0x35781dc0...3f4588 | 0.07371300 |
| U | 0x75860da4...ef9956 | 0.05577300 |
| V | 0xb59dd817...9af2c3 | 0.04883299 |
| W | 0x5f32aef7...ccc7b0 | 0.04070500 |
| X | 0xa95cbbd1...33047d | 0.04257700 |
| Y | 0xd8e32848...2444c4 | 0.04444900 |
| Z | 0x7af0ef6e...4e197c | 0.02426800 |

**Total APT across swarm:** 20.34477251 APT

**Top 5 by balance:**
- bob (0x0a3c00c58f...): 12.65700700 APT
- F (0x18a14b5b4b...): 1.96051600 APT
- L (0x7c2eaeafad...): 1.92726900 APT
- J (0x4d964db8f5...): 1.89509300 APT
- alice (0xc793acdec1...): 0.43643352 APT

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts probed — all **healthy** with `sigs_required=2`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4f428a0...987003 | 2 | ✓ healthy |
| A-G | 0xf56c4a1c09...bc0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ffe1812b...75b883 | 2 | ✓ healthy |
| S-T | 0x3b1c3ae905...ed7883 | 2 | ✓ healthy |
| V-W | 0x40fad7b423...80eb6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

**Status:** UNAVAILABLE — site is behind Vercel deployment protection (authentication required).
API paths `/api/markets`, `/api/v1/markets` all return 401/auth redirect.
No market data could be extracted. `mnx_snapshots` table is empty.

---

## DuckDB Summary

**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | New Rows | Total Rows |
|-------|----------|------------|
| world_increments | 185 | 208 |
| repo_snapshots | 185 | 1129 |
| aptos_snapshots | 28 | 28 |
| multisig_probes | 5 | 5 |
| mnx_snapshots | 0 | 0 |
