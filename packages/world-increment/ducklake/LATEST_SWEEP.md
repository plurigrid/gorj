# LATEST_SWEEP.md

**Generated:** 2026-07-06 02:13 UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org/user | 101 |
| bmorphism | org/user | 101 |
| zubyul | org/user | 50 |
| kubeflow | org/user | 50 |
| AustinCStone | org/user | 41 |
| migalkin | org/user | 20 |
| wasita | org/user | 12 |
| M1shaaa | org/user | 9 |
| DJedamski | org/user | 7 |
| TeglonLabs | org/user | 6 |
| kristinezheng | org/user | 6 |

**Total increments:** 415  
**Total repo snapshots:** 1336

### Top Repos by Stars

| Repo | Language | ★ | Forks | Last Push |
|------|----------|---|-------|-----------|
| kubeflow/kubeflow | - | 15764 | 2684 | 2026-06-18 |
| kubeflow/kubeflow | - | 15572 | 2633 | 2026-01-05T13:47:10Z |
| kubeflow/kubeflow | - | 15565 | 2626 | 2026-01-05T13:47:10Z |
| kubeflow/pipelines | Python | 4169 | 2024 | 2026-07-05 |
| kubeflow/pipelines | Python | 4119 | 1984 | 2026-04-10T23:07:19Z |
| kubeflow/pipelines | Python | 4119 | 1985 | 2026-04-14T01:20:50Z |
| kubeflow/spark-operator | Python | 3132 | 1497 | 2026-07-02 |
| kubeflow/spark-operator | Python | 3114 | 1483 | 2026-04-13T18:28:43Z |
| kubeflow/spark-operator | Python | 3111 | 1483 | 2026-04-10T18:21:12Z |
| kubeflow/trainer | Go | 2129 | 978 | 2026-07-03 |
| kubeflow/trainer | Go | 2082 | 945 | 2026-04-13T23:41:09Z |
| kubeflow/trainer | Go | 2080 | 944 | 2026-04-10T13:35:59Z |
| kubeflow/katib | Python | 1689 | 530 | 2026-07-01 |
| kubeflow/katib | Python | 1678 | 521 | 2026-04-14T01:21:37Z |
| kubeflow/katib | Python | 1676 | 521 | 2026-04-02T07:08:12Z |

### GF(3) Color Chain Distribution

| Color | Name | Trit | Count |
|-------|------|------|-------|
| `#b8bb26` | PLUS | 1 | 139 |
| `#cc241d` | MINUS | -1 | 138 |
| `#d3869b` | ERGODIC | 0 | 138 |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

**Timestamp:** 2026-07-06 02:13 UTC  
**Total wallets:** 28  
**Combined APT:** 20.3448 APT

### Wallet Balances

| World | Address | Balance (APT) |
|-------|---------|---------------|
| bob | `0x0a3c00c5...512d5d` | 12.65700700 |
| F | `0x18a14b5b...c3cf71` | 1.96051600 |
| L | `0x7c2eaeaf...37eba9` | 1.92726900 |
| J | `0x4d964db8...e87f54` | 1.89509300 |
| alice | `0xc793acde...24cc7b` | 0.43643352 |
| O | `0x73252b60...25a89d` | 0.21013600 |
| K | `0xa732040a...425dc4` | 0.16196100 |
| P | `0x6218792d...1ec948` | 0.14013600 |
| M | `0x6fed37a7...b7f2e9` | 0.11228500 |
| N | `0xe7dde6da...551b2c` | 0.10612100 |
| Q | `0xac40fa50...5c89a9` | 0.10324000 |
| S | `0xb8753014...9d0386` | 0.09178800 |
| R | `0x7ce605cc...d76e10` | 0.09021700 |
| T | `0x35781dc0...3f4588` | 0.07371300 |
| U | `0x75860da4...ef9956` | 0.05577300 |
| A | `0x8699edc0...be9d7a` | 0.05176700 |
| V | `0xb59dd817...9af2c3` | 0.04883299 |
| Y | `0xd8e32848...2444c4` | 0.04444900 |
| X | `0xa95cbbd1...33047d` | 0.04257700 |
| W | `0x5f32aef7...ccc7b0` | 0.04070500 |
| B | `0x3f892ebe...77cb13` | 0.03625600 |
| Z | `0x7af0ef6e...4e197c` | 0.02426800 |
| D | `0xf7765624...fcfdd1` | 0.01162900 |
| C | `0x38b99e63...91535e` | 0.01018500 |
| E | `0xdc1d9d53...958d36` | 0.00937200 |
| H | `0xce67c327...e5300f` | 0.00168100 |
| I | `0x070fe5d7...0c1fc9` | 0.00068100 |
| G | `0x69a394c0...cc7f32` | 0.00068100 |

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428...987003` | 2 | ✅ |
| A-G | `0xf56c4a1c...bc0096` | 2 | ✅ |
| S-T | `0x3b1c3ae9...ed7883` | 2 | ✅ |
| V-W | `0x40fad7b4...80eb6d` | 2 | ✅ |
| Y-Z | `0xd3ffe181...75b883` | 2 | ✅ |

### MNX Markets

testnet.mnx.fi returned HTTP 401 (requires authentication) — SPA with auth-gated API. No market data extracted.

---

## DuckDB Schema

```sql
world_increments  -- 415 rows
repo_snapshots    -- 1336 rows  
aptos_snapshots   -- 28 rows
multisig_probes   -- 5 rows
mnx_snapshots     -- 0 rows
```
