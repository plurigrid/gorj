# LATEST_SWEEP.md

**Generated:** 2026-07-07 08:12:21 UTC  
**Branch:** world-increment/sweep  
**GF3 Color Chain:** ERGODIC=#d3869b (trit=0) | PLUS=#b8bb26 (trit=1) | MINUS=#cc241d (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Summary
- **Total world-increments logged:** 394
- **Total repo snapshots:** 646 unique repos
- **Total stars across graph:** 103,952

### Repo Coverage by Source

| Source | Repos | Stars | Latest Push | Languages |
|--------|-------|-------|-------------|-----------|
| plurigrid | 168 | 159 | 2026-07-07 | 24 |
| bmorphism | 165 | 509 | 2026-07-07 | 28 |
| zubyul | 59 | 40 | 2026-04-24 | 22 |
| TeglonLabs | 54 | 14 | 2026-06-08 | 8 |
| kubeflow | 51 | 102,049 | 2026-07-07 | 9 |
| AustinCStone | 43 | 324 | 2026-02-11 | 11 |
| wasita | 31 | 6 | 2026-04-13 | 10 |
| migalkin | 30 | 834 | 2025-08-04 | 10 |
| kristinezheng | 18 | 0 | 2026-07-01 | 6 |
| M1shaaa | 16 | 0 | 2026-07-07 | 5 |
| DJedamski | 11 | 17 | 2018-03-07 | 4 |

### GF3 Trit Distribution

| GF3 Name | Color | Count |
|----------|-------|-------|
| PLUS | `#b8bb26` | 132 |
| MINUS | `#cc241d` | 132 |
| ERGODIC | `#d3869b` | 130 |


---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances
> Queried: 2026-07-07 08:12:21 UTC  
> All balances returned 0 APT — accounts either have no CoinStore resource or hold zero balance.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| A | `0x8699edc0...aebe9d7a` | 0.00000000 |
| B | `0x3f892ebe...4577cb13` | 0.00000000 |
| C | `0x38b99e63...2691535e` | 0.00000000 |
| D | `0xf7765624...d9fcfdd1` | 0.00000000 |
| E | `0xdc1d9d53...d0958d36` | 0.00000000 |
| F | `0x18a14b5b...74c3cf71` | 0.00000000 |
| G | `0x69a394c0...dbcc7f32` | 0.00000000 |
| H | `0xce67c327...94e5300f` | 0.00000000 |
| I | `0x070fe5d7...c00c1fc9` | 0.00000000 |
| J | `0x4d964db8...93e87f54` | 0.00000000 |
| K | `0xa732040a...7a425dc4` | 0.00000000 |
| L | `0x7c2eaeaf...6337eba9` | 0.00000000 |
| M | `0x6fed37a7...49b7f2e9` | 0.00000000 |
| N | `0xe7dde6da...11551b2c` | 0.00000000 |
| O | `0x73252b60...a525a89d` | 0.00000000 |
| P | `0x6218792d...621ec948` | 0.00000000 |
| Q | `0xac40fa50...5e5c89a9` | 0.00000000 |
| R | `0x7ce605cc...36d76e10` | 0.00000000 |
| S | `0xb8753014...f99d0386` | 0.00000000 |
| T | `0x35781dc0...2d3f4588` | 0.00000000 |
| U | `0x75860da4...95ef9956` | 0.00000000 |
| V | `0xb59dd817...a89af2c3` | 0.00000000 |
| W | `0x5f32aef7...a6ccc7b0` | 0.00000000 |
| X | `0xa95cbbd1...be33047d` | 0.00000000 |
| Y | `0xd8e32848...fa2444c4` | 0.00000000 |
| Z | `0x7af0ef6e...6e4e197c` | 0.00000000 |
| alice | `0xc793acde...d624cc7b` | 0.00000000 |
| bob | `0x0a3c00c5...05512d5d` | 0.00000000 |


### Multisig Contract Probes (Aptos Mainnet)
> All 5 multisig contracts respond as **healthy** with `num_signatures_required = 2`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428...f4987003` | 2 | ✓ YES |
| A-G | `0xf56c4a1c...3fbc0096` | 2 | ✓ YES |
| S-T | `0x3b1c3ae9...3ded7883` | 2 | ✓ YES |
| V-W | `0x40fad7b4...2c80eb6d` | 2 | ✓ YES |
| Y-Z | `0xd3ffe181...8e75b883` | 2 | ✓ YES |


### MNX Markets (testnet.mnx.fi)
**Status:** UNAVAILABLE  
testnet.mnx.fi returns HTTP 401 (Vercel authentication required). The site is a protected deployment — no market data could be extracted without Vercel OIDC credentials. No rows inserted into `mnx_snapshots`.

---

## DuckDB Schema

```sql
-- world_increments: GF3-colored event log
-- repo_snapshots:   GitHub repo state snapshots  
-- aptos_snapshots:  Hamming swarm wallet balances
-- multisig_probes:  Aptos multisig health checks
-- mnx_snapshots:    MNX market data (empty — auth required)
```

**Database path:** `packages/world-increment/ducklake/world-increments.duckdb`
