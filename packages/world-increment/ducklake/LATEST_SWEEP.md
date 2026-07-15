# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-15

## Sweep Metadata
- **Date:** 2026-07-15
- **Increment ID:** 13 — GF(3) trit=+1, color=#b8bb26, name=**PLUS**
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Prior sweep:** 2026-05-08 (67 days elapsed)
- **Aptos ledger version:** 6282680614

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 13 (25 rows incl. start/complete) |
| Total Repo Snapshots | 945 (cumulative) |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Market Data | Unavailable (SPA) |

---

## JOB 1: GitHub Social Graph Sweep

**Scope note:** GitHub REST API in this session is proxy-scoped to repository-scoped endpoints only (`repos/plurigrid/gorj/...`). Org-level queries (`/orgs/{org}/repos`) returned 403 — external orgs (kubeflow, TeglonLabs) and user repos (bmorphism, zubyul, social graph) were inaccessible this run. Only `plurigrid/gorj` was snapshotted. Prior sweep data (471 repos from 11 sources, 2026-04-12) is intact in the database.

### plurigrid/gorj (increment 13 snapshot)
| Field | Value |
|---|---|
| Language | Clojure |
| Last push | 2026-05-08T14:04:34Z |
| Description | MCP server + hooks that give AI coding agents a Clojure REPL |
| Active branches | 30+ (25+ `world-increment/sweep-*` from Apr–May 2026) |
| Recent activity | Claude-bot commits (duckdb sweep state, ducklake sync) |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, ledger v6282680614)

All 28 Hamming swarm addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. Accounts may hold APT via the newer `0x1::fungible_asset` framework, or be unfunded.

| World | Address (truncated) | APT Balance |
|---|---|---|
| alice | 0xc793...cc7b | 0 (no CoinStore) |
| bob | 0x0a3c...12d5d | 0 (no CoinStore) |
| A | 0x8699...9d7a | 0 (no CoinStore) |
| B | 0x3f89...b13 | 0 (no CoinStore) |
| C | 0x38b9...535e | 0 (no CoinStore) |
| D | 0xf776...fdd1 | 0 (no CoinStore) |
| E | 0xdc1d...d36 | 0 (no CoinStore) |
| F | 0x18a1...cf71 | 0 (no CoinStore) |
| G–Z | (20 addresses) | 0 each (no CoinStore) |
| **TOTAL APT** | | **0.0 APT** |

### Multisig Contract Probes

All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|---|---|---|---|
| A-B | 0x0da4...7003 | 2 | ✅ healthy |
| A-G | 0xf56c...0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✅ healthy |
| S-T | 0x3b1c...7883 | 2 | ✅ healthy |
| V-W | 0x40fa...eb6d | 2 | ✅ healthy |

**All 5 multisig contracts live, all require 2-of-N signatures.**

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` is a single-page application. All API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`, `/api/v1/tickers`) return the HTML shell. **No market data available.**

---

## GF(3) Color Chain — Increments 1–13

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 12 | bmorphism (org) | sweep_complete | 0 | `#d3869b` | **ERGODIC** |
| **13** | **plurigrid (org)** | **sweep_complete** | **+1** | **`#b8bb26`** | **PLUS** |

GF(3) position after sweep 13: `... → ERGODIC → **PLUS**`. Next sweep = increment 14 → MINUS (#cc241d).

---

## DuckDB Table State

| Table | Rows |
|---|---|
| world_increments | 25 |
| repo_snapshots | 945 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

---

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

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
