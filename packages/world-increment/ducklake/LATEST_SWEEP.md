# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-05-08  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources queried

| Source | Type | Repos |
|--------|------|------:|
| plurigrid | org | 100 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (zubyul social) | 19 |
| DJedamski | user (zubyul social) | 6 |
| wasita | user (zubyul social) | 11 |
| kristinezheng | user (zubyul social) | 6 |
| M1shaaa | user (zubyul social) | 8 |
| AustinCStone | user (zubyul social) | 40 |
| **Total** | | **390** |

### GF(3) Color Chain

| GF3 Name | Trit | Color | Count |
|----------|------|-------|------:|
| PLUS | +1 | `#b8bb26` | 130 |
| ERGODIC | 0 | `#d3869b` | 130 |
| MINUS | -1 | `#cc241d` | 130 |

Perfect balanced GF(3) distribution across 390 increments.

### Top Stars by Source

| Source | Repos | Stars | Forks |
|--------|------:|------:|------:|
| kubeflow | 47 | 34,014 | 13,398 |
| migalkin | 19 | 279 | 49 |
| bmorphism | 100 | 247 | 73 |
| AustinCStone | 40 | 108 | 38 |
| plurigrid | 100 | 70 | 43 |
| zubyul | 49 | 14 | 2 |
| wasita | 11 | 4 | 1 |
| TeglonLabs | 4 | 2 | 2 |
| DJedamski | 6 | 3 | 1 |
| kristinezheng | 6 | 0 | 0 |
| M1shaaa | 8 | 0 | 0 |

### DuckDB Tables

- **world_increments**: 390 rows (one per repo snapshot, GF3-colored)
- **repo_snapshots**: 390 rows (full repo metadata)
- **Sequences**: `increment_seq`, `repo_seq`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried 28 addresses (alice, bob, A–Z) via `fullnode.mainnet.aptoslabs.com`.  
All accounts show **0.00000000 APT** — accounts are not funded / not registered on mainnet with the `AptosCoin` CoinStore resource.

| World | Address (prefix) | Balance APT |
|-------|-----------------|------------:|
| alice | 0xc793acdec1… | 0.00000000 |
| bob | 0x0a3c00c58f… | 0.00000000 |
| A | 0x8699edc096… | 0.00000000 |
| B | 0x3f892ebe6e… | 0.00000000 |
| C | 0x38b99e63ad… | 0.00000000 |
| D | 0xf77656248f… | 0.00000000 |
| E | 0xdc1d9d533b… | 0.00000000 |
| F | 0x18a14b5b4b… | 0.00000000 |
| G | 0x69a394c0b0… | 0.00000000 |
| H | 0xce67c327a7… | 0.00000000 |
| I | 0x070fe5d74e… | 0.00000000 |
| J | 0x4d964db8f5… | 0.00000000 |
| K | 0xa732040a6b… | 0.00000000 |
| L | 0x7c2eaeafad… | 0.00000000 |
| M | 0x6fed37a755… | 0.00000000 |
| N | 0xe7dde6da0a… | 0.00000000 |
| O | 0x73252b6011… | 0.00000000 |
| P | 0x6218792de4… | 0.00000000 |
| Q | 0xac40fa50b8… | 0.00000000 |
| R | 0x7ce605cc8f… | 0.00000000 |
| S | 0xb8753014e4… | 0.00000000 |
| T | 0x35781dc0e4… | 0.00000000 |
| U | 0x75860da475… | 0.00000000 |
| V | 0xb59dd81703… | 0.00000000 |
| W | 0x5f32aef70f… | 0.00000000 |
| X | 0xa95cbbd116… | 0.00000000 |
| Y | 0xd8e32848f1… | 0.00000000 |
| Z | 0x7af0ef6e1b… | 0.00000000 |

### Multisig Contract Probes

All 5 multisig contracts are **healthy** (responsive) with **2 signatures required**.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|:-------------:|:-------:|
| A-B | 0x0da4f428a0… | 2 | ✓ |
| A-G | 0xf56c4a1c09… | 2 | ✓ |
| Y-Z | 0xd3ffe1812b… | 2 | ✓ |
| S-T | 0x3b1c3ae905… | 2 | ✓ |
| V-W | 0x40fad7b423… | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

The MNX testnet frontend loaded (SPA, ~293 KB HTML) but exposes **no public REST API** at the probed paths (`/api/markets`, `/api/v1/markets`, `api.testnet.mnx.fi/markets`). Market data is **unavailable** via direct API probe. Recorded as placeholder row in `mnx_snapshots`.

---

## Schema Summary

```sql
world_increments   -- 390 rows: GF(3) colored repo events
repo_snapshots     -- 390 rows: full GitHub repo metadata
aptos_snapshots    -- 28 rows: Hamming swarm wallet balances
multisig_probes    -- 5 rows: 2-of-N multisig health checks
mnx_snapshots      -- 1 row: MNX market data (unavailable)
```
