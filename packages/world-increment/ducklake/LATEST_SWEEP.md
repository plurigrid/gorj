# LATEST_SWEEP — 2026-04-04 03:19 UTC

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshot

| # | Source | Type | Repos | GF3 Trit | GF3 Color | GF3 Name |
|---|--------|------|-------|----------|-----------|----------|
| 1 | AustinCStone | user | 40 | 1 | #b8bb26 | PLUS |
| 2 | DJedamski | user | 6 | -1 | #cc241d | MINUS |
| 3 | M1shaaa | user | 8 | 0 | #d3869b | ERGODIC |
| 4 | TeglonLabs | org | 3 | 1 | #b8bb26 | PLUS |
| 5 | bmorphism | user | 97 | -1 | #cc241d | MINUS |
| 6 | kristinezheng | user | 6 | 0 | #d3869b | ERGODIC |
| 7 | kubeflow | org | 46 | 1 | #b8bb26 | PLUS |
| 8 | migalkin | user | 19 | -1 | #cc241d | MINUS |
| 9 | plurigrid | org | 94 | 0 | #d3869b | ERGODIC |
| 10 | wasita | user | 9 | 1 | #b8bb26 | PLUS |
| 11 | zubyul | user | 44 | -1 | #cc241d | MINUS |

**Total repos indexed**: 372 across 11 sources  
**Total stars**: 34523 | **Total forks**: 13541

### GF(3) Color Chain
- trit=0 → ERGODIC `#d3869b` (rose)
- trit=1 → PLUS `#b8bb26` (yellow-green)
- trit=-1 → MINUS `#cc241d` (red)

### Top 10 Repos by Stars

| Repo | Language | Stars | Forks | Pushed |
|------|----------|-------|-------|--------|
| kubeflow/kubeflow | N/A | 15551 | 2628 | 2026-01-05 |
| kubeflow/pipelines | Python | 4117 | 1983 | 2026-04-03 |
| kubeflow/spark-operator | Python | 3109 | 1480 | 2026-03-31 |
| kubeflow/trainer | Go | 2074 | 942 | 2026-04-03 |
| kubeflow/katib | Python | 1674 | 519 | 2026-04-02 |
| kubeflow/examples | Jsonnet | 1459 | 755 | 2025-04-14 |
| kubeflow/manifests | YAML | 1007 | 1068 | 2026-03-27 |
| kubeflow/arena | Go | 809 | 190 | 2026-03-19 |
| kubeflow/kale | Python | 682 | 156 | 2026-04-02 |
| kubeflow/mpi-operator | Go | 519 | 236 | 2026-03-23 |

### DuckDB Tables
- `world_increments`: 11 rows (one per source, GF3 color chain)
- `repo_snapshots`: 372 rows
- `aptos_snapshots`: 28 rows
- `multisig_probes`: 5 rows

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)

All balances fetched via `0x1::primary_fungible_store::balance` (FungibleAsset API).

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793acde...24cc7b | 0.436434 |
| bob | 0x0a3c00c5...512d5d | 12.657007 |
| A | 0x8699edc0...be9d7a | 0.051767 |
| B | 0x3f892ebe...77cb13 | 0.036256 |
| C | 0x38b99e63...91535e | 0.010185 |
| D | 0xf7765624...fcfdd1 | 0.011629 |
| E | 0xdc1d9d53...958d36 | 0.012561 |
| F | 0x18a14b5b...c3cf71 | 1.960516 |
| G | 0x69a394c0...cc7f32 | 0.000681 |
| H | 0xce67c327...e5300f | 0.000681 |
| I | 0x070fe5d7...0c1fc9 | 0.000681 |
| J | 0x4d964db8...e87f54 | 1.895093 |
| K | 0xa732040a...425dc4 | 0.161961 |
| L | 0x7c2eaeaf...37eba9 | 1.927269 |
| M | 0x6fed37a7...b7f2e9 | 0.112285 |
| N | 0xe7dde6da...551b2c | 0.106121 |
| O | 0x73252b60...25a89d | 0.210136 |
| P | 0x6218792d...1ec948 | 0.140136 |
| Q | 0xac40fa50...5c89a9 | 0.103240 |
| R | 0x7ce605cc...d76e10 | 0.090217 |
| S | 0xb8753014...9d0386 | 0.091788 |
| T | 0x35781dc0...3f4588 | 0.073713 |
| U | 0x75860da4...ef9956 | 0.055773 |
| V | 0xb59dd817...9af2c3 | 0.047833 |
| W | 0x5f32aef7...ccc7b0 | 0.040705 |
| X | 0xa95cbbd1...33047d | 0.042577 |
| Y | 0xd8e32848...2444c4 | 0.044449 |
| Z | 0x7af0ef6e...4e197c | 0.023268 |

**Total APT across all wallets**: 20.344962 APT  
**Wallets with balance > 1 APT**: 4

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f428...987003 | 2 | ✓ |
| A-G | 0xf56c4a1c...bc0096 | 2 | ✓ |
| Y-Z | 0xd3ffe181...75b883 | 2 | ✓ |
| S-T | 0x3b1c3ae9...ed7883 | 2 | ✓ |
| V-W | 0x40fad7b4...80eb6d | 2 | ✓ |

**All 5 multisig contracts healthy** — 2-of-N threshold confirmed on all pairs.

### MNX Markets (testnet.mnx.fi)

MNX testnet API endpoints were probed but returned no structured data (SPA frontend, no REST endpoints at `/api/markets`, `/api/v1/markets`, or `/api/tickers`). Status: **unavailable**.

---

## DuckDB Location

`packages/world-increment/ducklake/world-increments.duckdb`

```sql
-- Sample queries
SELECT source_name, gf3_name, gf3_color, count(*) AS repos
FROM world_increments wi JOIN repo_snapshots rs ON wi.id = rs.increment_id
GROUP BY 1,2,3 ORDER BY repos DESC;

SELECT world, balance_apt FROM aptos_snapshots ORDER BY balance_apt DESC NULLS LAST;

SELECT pair, sigs_required, healthy FROM multisig_probes;
```
