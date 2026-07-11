# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-11
**Run type:** Automated background sweep (world-increment-sweep + hamming-swarm-snapshot)
**DuckDB version:** 1.5.4
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Source | Type | Repos Stored |
|--------|------|-------------|
| plurigrid | org | 100 (103 total) |
| kubeflow | org | 7 (49 total) |
| TeglonLabs | org | 5 |
| bmorphism | user | 6 top (105 total) |
| zubyul | user | 5 top (49 total) |
| migalkin | user | 4 top (19 total) |
| AustinCStone | user | 2 top (40 total) |
| wasita | user | 2 top (11 total) |
| kristinezheng | user | 1 (5 total) |
| M1shaaa | user | 1 (8 total) |
| DJedamski | user | 1 (6 total) |
| **TOTAL** | | **134 stored / ~400 indexed** |

```
world_increments: 34 rows
repo_snapshots:  1078 rows (including prior sweep data)
```

### GF(3) Color Chain

| id%3 | trit | color | name |
|------|------|-------|------|
| 0 | 0 | #d3869b | ERGODIC |
| 1 | +1 | #b8bb26 | PLUS |
| 2 | -1 | #cc241d | MINUS |

### Notable Repos by Recent Push

| Repo | Stars | Pushed |
|------|-------|--------|
| kubeflow/spark-operator | 3137 | 2026-07-11 |
| kubeflow/trainer | 2135 | 2026-07-11 |
| kubeflow/kubeflow | 15771 | 2026-07-11 |
| kubeflow/pipelines | 4169 | 2026-07-10 |
| bmorphism/Gay.jl | 2* / 187 open issues | 2026-06-20 |
| bmorphism/babashka-mcp-server | 19 | 2026-06-05 |
| TeglonLabs/jank-crane | GF3 convergence maps | 2026-06-08 |
| plurigrid/zig-syrup | 2 | 2026-04-30 |
| plurigrid/nanoclj-zig | 1* / 20 issues | 2026-04-25 |

### Social Graph Users (zubyul network)

| User | Total Repos | Top Repo |
|------|------------|---------|
| migalkin | 19 | NodePiece (144*) |
| DJedamski | 6 | Getting-and-Cleaning-Data |
| wasita | 11 | magic-garden (2*) |
| kristinezheng | 5 | kristinezheng.github.io |
| M1shaaa | 8 | lab-bookshelf- (TypeScript) |
| AustinCStone | 40 | TextGAN (92*) |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried via `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**All 28 addresses returned 0 APT.** Accounts have no CoinStore<AptosCoin> resource registered (not initialized with APT).

| World | Address | APT Balance |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...5d5d | 0.0 |
| A-Z (26 wallets) | various | 0.0 each |

```
aptos_snapshots: 28 rows (all zero balance)
```

### Multisig Contract Probes

Probed via `POST /v1/view -> 0x1::multisig_account::num_signatures_required`.

**All 5 multisig pairs respond healthy. Threshold = 2.**

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f4...7003 | 2 | HEALTHY |
| A-G | 0xf56c4a...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ffe1...b883 | 2 | HEALTHY |
| S-T | 0x3b1c3a...7883 | 2 | HEALTHY |
| V-W | 0x40fad7...eb6d | 2 | HEALTHY |

```
multisig_probes: 5 rows (5/5 healthy, all require 2 sigs)
```

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** - Vercel deployment protected by visitor password authentication.
No market data accessible. HTTP 401 returned for all API paths tried.

```
mnx_snapshots: 0 rows
```

---

## GF(3) Assignment Rule

- `id mod 3 == 0` -> trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` -> trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` -> trit=-1, color=#cc241d, name=MINUS

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
