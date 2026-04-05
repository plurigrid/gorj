# World-Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-04-05 03:20 UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 95 |
| kubeflow | org | 46 |
| TeglonLabs | org | 3 |
| bmorphism | user | 97 |
| zubyul | user | 44 |
| migalkin | user (zubyul social) | 19 |
| DJedamski | user (zubyul social) | 6 |
| wasita | user (zubyul social) | 9 |
| kristinezheng | user (zubyul social) | 6 |
| M1shaaa | user (zubyul social) | 8 |
| AustinCStone | user (zubyul social) | 40 |
| **Total** | | **373 repos** |

### Recent Events

**bmorphism** (10 events): All `PushEvent` to `plurigrid/horse` and `plurigrid/nanoclj-zig`  
**zubyul** (10 events): Mix of `CreateEvent`, `PushEvent`, `PullRequestEvent` on `plurigrid/gorj` and `plurigrid/horse`

### DuckDB Tables

| Table | Rows |
|-------|------|
| world_increments | 853 |
| repo_snapshots | 1,311 |

### GF(3) Color Chain Distribution

| GF3 Name | Color | Trit | Count |
|----------|-------|------|-------|
| ERGODIC | `#d3869b` | 0 | 283 |
| PLUS | `#b8bb26` | +1 | 286 |
| MINUS | `#cc241d` | -1 | 284 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

Queried 28 addresses (alice, bob, A-Z) against Aptos mainnet fullnode.  
`https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

**Result:** All 28 addresses returned `resource_not_found` — accounts either do not hold APT in a CoinStore or are not active on mainnet. Balance recorded as `-1` APT for all.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | -1 (no CoinStore) |
| bob | 0x0a3c...2d5d | -1 (no CoinStore) |
| A | 0x8699...9d7a | -1 (no CoinStore) |
| B | 0x3f89...b13 | -1 (no CoinStore) |
| C | 0x38b9...535e | -1 (no CoinStore) |
| D | 0xf776...fdd1 | -1 (no CoinStore) |
| E | 0xdc1d...8d36 | -1 (no CoinStore) |
| F | 0x18a1...f71 | -1 (no CoinStore) |
| G | 0x69a3...f32 | -1 (no CoinStore) |
| H | 0xce67...00f | -1 (no CoinStore) |
| I | 0x070f...fc9 | -1 (no CoinStore) |
| J | 0x4d96...f54 | -1 (no CoinStore) |
| K | 0xa732...dc4 | -1 (no CoinStore) |
| L | 0x7c2e...ba9 | -1 (no CoinStore) |
| M | 0x6fed...2e9 | -1 (no CoinStore) |
| N | 0xe7dd...1b2c | -1 (no CoinStore) |
| O | 0x7325...89d | -1 (no CoinStore) |
| P | 0x6218...948 | -1 (no CoinStore) |
| Q | 0xac40...89a9 | -1 (no CoinStore) |
| R | 0x7ce6...e10 | -1 (no CoinStore) |
| S | 0xb875...386 | -1 (no CoinStore) |
| T | 0x3578...588 | -1 (no CoinStore) |
| U | 0x7586...956 | -1 (no CoinStore) |
| V | 0xb59d...2c3 | -1 (no CoinStore) |
| W | 0x5f32...b0 | -1 (no CoinStore) |
| X | 0xa95c...47d | -1 (no CoinStore) |
| Y | 0xd8e3...44c4 | -1 (no CoinStore) |
| Z | 0x7af0...97c | -1 (no CoinStore) |

### Multisig Contract Probes

POST `https://fullnode.mainnet.aptoslabs.com/v1/view` -> `0x1::multisig_account::num_signatures_required`

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4...003 | 2 | yes |
| A-G | 0xf56c...096 | 2 | yes |
| Y-Z | 0xd3ff...883 | 2 | yes |
| S-T | 0x3b1c...883 | 2 | yes |
| V-W | 0x40fa...b6d | 2 | yes |

**All 5 multisig accounts healthy — 2-of-N threshold confirmed.**

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` serves a Next.js SPA — no public JSON API endpoints (`/api/markets`, `/api/tickers`) returned data. Recorded as unavailable.

---

## DuckDB Summary

```sql
-- Tables and row counts
SELECT 'world_increments' as tbl, count(*) FROM world_increments
UNION ALL SELECT 'repo_snapshots', count(*) FROM repo_snapshots
UNION ALL SELECT 'aptos_snapshots', count(*) FROM aptos_snapshots
UNION ALL SELECT 'multisig_probes', count(*) FROM multisig_probes;

-- Top repos by stars (plurigrid org)
SELECT repo_name, stars, language FROM repo_snapshots
WHERE org_or_user = 'plurigrid' ORDER BY stars DESC LIMIT 10;
```

**File:** `packages/world-increment/ducklake/world-increments.duckdb`
