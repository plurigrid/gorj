# World-Increment Sweep + Hamming Swarm Snapshot
**Generated:** 2026-05-14 14:19 UTC

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (zubyul graph) | 19 |
| DJedamski | user (zubyul graph) | 6 |
| wasita | user (zubyul graph) | 11 |
| kristinezheng | user (zubyul graph) | 6 |
| M1shaaa | user (zubyul graph) | 8 |
| AustinCStone | user (zubyul graph) | 40 |

**Total repos snapshotted:** 391

### DuckDB Schema
- `world_increments` — 11 rows (one per source, GF(3) color chain)
- `repo_snapshots` — 391 rows
- `aptos_snapshots` — 28 rows
- `multisig_probes` — 5 rows
- `mnx_snapshots` — 1 row (unavailable)

### GF(3) Color Chain
- `id % 3 == 0` → trit=0, ERGODIC, #d3869b (pink)
- `id % 3 == 1` → trit=1, PLUS, #b8bb26 (green)
- `id % 3 == 2` → trit=-1, MINUS, #cc241d (red)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-05-14 14:19 UTC)

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

**Total APT across swarm:** 20.344773

**Top 5 by balance:**
- bob (0x0a3c00c58fdf...): 12.65700700 APT
- F (0x18a14b5b4bec...): 1.96051600 APT
- L (0x7c2eaeafad97...): 1.92726900 APT
- J (0x4d964db8f538...): 1.89509300 APT
- alice (0xc793acdec12b...): 0.43643352 APT

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f428...87003 | 2 | ✓ |
| A-G | 0xf56c4a1c...0096 | 2 | ✓ |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ |

All 5 multisig contracts healthy (2-of-N threshold confirmed).

### MNX Markets (testnet.mnx.fi)
Status: **Unavailable** — endpoint returns SPA HTML (no JSON API at /api/markets or /api/v1/markets).

---

## DuckDB Location
`packages/world-increment/ducklake/world-increments.duckdb`

Query example:
```sql
SELECT org_or_user, count(*) FROM repo_snapshots GROUP BY 1 ORDER BY 2 DESC;
SELECT world, balance_apt FROM aptos_snapshots ORDER BY balance_apt DESC;
```
