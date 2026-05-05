# World Increment Sweep + Hamming Snapshot

**Sweep Date/Time:** 2026-05-05 (automated sweep)
**DuckDB Version:** v1.5.2 (Variegata)
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repos Snapshotted Per Source

| Source | Type | Repos Captured |
|--------|------|----------------|
| bmorphism | user | 103 |
| plurigrid | org | 102 |
| TeglonLabs | org | 55 |
| kubeflow | org | 49 |
| AustinCStone | user (zubyul graph) | 45 |
| wasita | user (zubyul graph) | 33 |
| zubyul | user | 29 |
| kristinezheng | user (zubyul graph) | 20 |
| DJedamski | user (zubyul graph) | 13 |
| M1shaaa | user (zubyul graph) | 2 (rate-limited) |
| migalkin | user (zubyul graph) | 2 (rate-limited) |
| **TOTAL** | | **453** |

Note: `migalkin` and `M1shaaa` hit GitHub unauthenticated rate limits; only 2 repos captured each (partial). Public events for bmorphism and zubyul also rate-limited (unauthenticated).

### Total World Increments

- **Total world_increments rows:** 453
- **Total repo_snapshot rows:** 453
- **GF(3) color chain applied per-increment** (id % 3 determines trit/color)

### GF(3) Color Chain Rule

| id % 3 | Trit | Name | Color |
|--------|------|------|-------|
| 0 | 0 | ERGODIC | #d3869b |
| 1 | +1 | PLUS | #b8bb26 |
| 2 | -1 | MINUS | #cc241d |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

Queried via `0x1::coin::balance` view function on Aptos mainnet (`fullnode.mainnet.aptoslabs.com`).
All 28 wallets returned non-zero balances.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| bob | 0x0a3c...12d5d | 12.657007 |
| F | 0x18a1...cf71 | 1.960516 |
| L | 0x7c2e...7eba9 | 1.927269 |
| J | 0x4d96...7f54 | 1.895093 |
| alice | 0xc793...4cc7b | 0.436434 |
| O | 0x7325...a89d | 0.210136 |
| K | 0xa732...25dc4 | 0.161961 |
| P | 0x6218...c948 | 0.140136 |
| M | 0x6fed...7f2e9 | 0.112285 |
| N | 0xe7dd...51b2c | 0.106121 |
| Q | 0xac40...c89a9 | 0.103240 |
| S | 0xb875...d0386 | 0.091788 |
| R | 0x7ce6...76e10 | 0.090217 |
| T | 0x3578...f4588 | 0.073713 |
| U | 0x7586...f9956 | 0.055773 |
| A | 0x8699...e9d7a | 0.051767 |
| V | 0xb59d...af2c3 | 0.048833 |
| Y | 0xd8e3...444c4 | 0.044449 |
| X | 0xa95c...3047d | 0.042577 |
| W | 0x5f32...c7b0 | 0.040705 |
| B | 0x3f89...cb13 | 0.036256 |
| Z | 0x7af0...197c | 0.024268 |
| D | 0xf776...fdd1 | 0.011629 |
| C | 0x38b9...535e | 0.010185 |
| E | 0xdc1d...8d36 | 0.009372 |
| H | 0xce67...300f | 0.001681 |
| I | 0x070f...1fc9 | 0.000681 |
| G | 0x69a3...7f32 | 0.000681 |

**Total APT across all wallets:** ~20.03 APT
**Wallets with non-zero balance:** 28/28

### Multisig Probe Results

All 5 multisig contracts queried via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | YES |
| A-G | 0xf56c...0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

All 5 multisig contracts healthy with 2-of-N signature requirement.

### MNX Market Data

**Status: Unavailable.** `https://testnet.mnx.fi/api/markets` returned HTTP 404 (Next.js SPA — no server-side API data exposed at that path). No market data could be extracted.

---

## Database Tables Summary

| Table | Rows | Description |
|-------|------|-------------|
| world_increments | 453 | GitHub repo snapshot events with GF3 color chain |
| repo_snapshots | 453 | Detailed repo metadata (stars, forks, language, etc.) |
| aptos_snapshots | 28 | Wallet balances at sweep time |
| multisig_probes | 5 | Multisig contract health checks |
| mnx_snapshots | 0 | Unavailable (SPA, no API) |

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```
