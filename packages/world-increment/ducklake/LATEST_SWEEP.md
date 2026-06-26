# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-26

## Sweep Metadata
- **Date:** 2026-06-26 02:16 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1 — GitHub Social Graph Sweep

### Repo Counts by Source

| # | Source | Type | Repos | GF(3) Trit | Color | Name |
|---|--------|------|-------|-----------|-------|------|
| 1 | plurigrid | org | 100 | +1 | `#b8bb26` | **PLUS** |
| 2 | kubeflow | org | 48 | -1 | `#cc241d` | **MINUS** |
| 3 | TeglonLabs | org | 5 | 0 | `#d3869b` | **ERGODIC** |
| 4 | bmorphism | user | 100 | +1 | `#b8bb26` | **PLUS** |
| 5 | zubyul | user | 49 | -1 | `#cc241d` | **MINUS** |
| 6 | migalkin | social | 19 | 0 | `#d3869b` | **ERGODIC** |
| 7 | DJedamski | social | 6 | +1 | `#b8bb26` | **PLUS** |
| 8 | wasita | social | 11 | -1 | `#cc241d` | **MINUS** |
| 9 | kristinezheng | social | 5 | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | social | 8 | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | social | 40 | -1 | `#cc241d` | **MINUS** |
| | **TOTAL** | | **391** | | | |

### GF(3) Color Chain

- `id % 3 == 0` → trit=0 **ERGODIC** `#d3869b`
- `id % 3 == 1` → trit=1 **PLUS** `#b8bb26`
- `id % 3 == 2` → trit=-1 **MINUS** `#cc241d`

Chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Mainnet Balances (28 addresses)

All 28 world addresses (alice, bob, A–Z) queried via:
`fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

**Result:** All 28 accounts returned null balance — no `CoinStore` resource registered on mainnet.

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4...` | 2 | ✓ |
| A-G | `0xf56c...` | 2 | ✓ |
| Y-Z | `0xd3ff...` | 2 | ✓ |
| S-T | `0x3b1c...` | 2 | ✓ |
| V-W | `0x40fa...` | 2 | ✓ |

All 5 multisig contracts healthy, `num_signatures_required = 2`.

### MNX Markets

`testnet.mnx.fi` — Vercel deployment protection active; authentication required. No data available.

---

## DuckDB Schema

**File:** `ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| `world_increments` | 34 (cumulative across runs) |
| `repo_snapshots` | 1335 (cumulative across runs) |
| `aptos_snapshots` | 28 |
| `multisig_probes` | 5 |
| `mnx_snapshots` | 0 (Vercel auth required) |

Fresh rows this run: 11 world increments, 391 repo snapshots.

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
