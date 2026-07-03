# World-Increment Sweep + Hamming Swarm Snapshot
**Date**: 2026-07-03

## JOB 1: GitHub Social Graph Sweep

### Sources Scanned
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social graph | 19 |
| wasita | social graph | 11 |
| DJedamski | social graph | 6 |
| kristinezheng | social graph | 5 |
| M1shaaa | social graph | 8 |
| AustinCStone | social graph | 30 |

**Total repos snapshotted**: 381

### Notable Recent Activity (as of 2026-07-03)
- `plurigrid/shrimp` — pushed 2026-07-03 (most recent)
- `bmorphism/Gay.jl` (Julia) — pushed 2026-07-03
- `M1shaaa/M1shaaa` (profile) — pushed 2026-07-03
- `kristinezheng/kristinezheng.github.io` (HTML) — pushed 2026-07-01
- `TeglonLabs/jank-crane` (C++) — pushed 2026-06-08 ("crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps")
- `plurigrid/asi` (HTML) — 28 stars, pushed 2026-06-29

### GF(3) Color Chain Applied
- ERGODIC (#d3869b): trit=0 (id%3==0)
- PLUS (#b8bb26): trit=1 (id%3==1)
- MINUS (#cc241d): trit=-1 (id%3==2)

### DuckDB Tables
| Table | Rows |
|-------|------|
| world_increments | 404 |
| repo_snapshots | 1325 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses A–Z + alice + bob)

| World | Balance (APT) |
|-------|--------------|
| A | ERROR/EMPTY |
| B | ERROR/EMPTY |
| C | ERROR/EMPTY |
| D | ERROR/EMPTY |
| E | ERROR/EMPTY |
| F | ERROR/EMPTY |
| G | ERROR/EMPTY |
| H | ERROR/EMPTY |
| I | ERROR/EMPTY |
| J | ERROR/EMPTY |
| K | ERROR/EMPTY |
| L | ERROR/EMPTY |
| M | ERROR/EMPTY |
| N | ERROR/EMPTY |
| O | ERROR/EMPTY |
| P | ERROR/EMPTY |
| Q | ERROR/EMPTY |
| R | ERROR/EMPTY |
| S | ERROR/EMPTY |
| T | ERROR/EMPTY |
| U | ERROR/EMPTY |
| V | ERROR/EMPTY |
| W | ERROR/EMPTY |
| X | ERROR/EMPTY |
| Y | ERROR/EMPTY |
| Z | ERROR/EMPTY |
| alice | ERROR/EMPTY |
| bob | ERROR/EMPTY |

**Total APT across active wallets**: 0.0000 APT
**Addresses with errors/empty**: 28/28

### Multisig Probes

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4f428a0c007...` | 2 | ✓ HEALTHY |
| A-G | `0xf56c4a1c090621...` | 2 | ✓ HEALTHY |
| Y-Z | `0xd3ffe1812b2df4...` | 2 | ✓ HEALTHY |
| S-T | `0x3b1c3ae905d44c...` | 2 | ✓ HEALTHY |
| V-W | `0x40fad7b423a843...` | 2 | ✓ HEALTHY |

**Healthy multisigs**: 5/5 (100%)

### MNX Markets (testnet.mnx.fi)

**Status**: Unavailable — testnet.mnx.fi appears to be a SPA with no public REST API endpoint accessible. All probed paths returned connection errors or HTML. No structured market data captured this sweep.

---

## DuckDB Location
`packages/world-increment/ducklake/world-increments.duckdb`

Query example:
```sql
SELECT gf3_color, gf3_name, COUNT(*) FROM world_increments GROUP BY 1,2;
SELECT world, balance_apt FROM aptos_snapshots ORDER BY balance_apt DESC;
```
