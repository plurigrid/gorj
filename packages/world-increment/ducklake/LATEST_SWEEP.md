# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-26

**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB version:** v1.5.5 (Variegata)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) cycle position:** id=13 PLUS #b8bb26 → id=14 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

**Status:** Partial — session scoped to `plurigrid/gorj` only.  
Cross-org/user API endpoints blocked by session scope policy. Orgs `plurigrid`, `kubeflow`, `TeglonLabs` and users `bmorphism`, `zubyul`, `migalkin`, `DJedamski`, `wasita`, `kristinezheng`, `M1shaaa`, `AustinCStone` could not be queried.

### Accessible: plurigrid/gorj

| Field | Value |
|---|---|
| Repo | plurigrid/gorj |
| Language | Clojure |
| Description | MCP server + hooks that give AI coding agents a Clojure REPL |
| Last Push | 2026-05-08T14:04:34Z |
| Last Commit SHA | 5b28fe016e0e3d0b0f22e35e01f7db0722d988e1 |
| Authenticated User | zubyul (Yuliya Zubak, 27 public repos, 6 followers) |
| Open Sweep Branches | 20+ `world-increment/sweep-*` branches (oldest: 2026-04-27) |

### Cumulative DuckDB State

| Table | Rows | Delta This Run |
|---|---|---|
| world_increments | 25 | +2 (id 13, 14) |
| repo_snapshots | 945 | +1 (gorj) |
| aptos_snapshots | 28 | +28 (first ever) |
| multisig_probes | 5 | +5 (first ever) |
| mnx_snapshots | 1 | +1 |

### GF(3) Color Chain — This Run

| id | trit | color | name | source | event |
|---|---|---|---|---|---|
| 13 | +1 | `#b8bb26` | **PLUS** | plurigrid/gorj | sweep_complete |
| 14 | -1 | `#cc241d` | **MINUS** | scope_blocked | cross_org_blocked |

GF(3) chain continues: `…ERGODIC(12) → PLUS(13) → MINUS(14)`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 Hamming swarm addresses queried via `fullnode.mainnet.aptoslabs.com`.  
**All returned 0 APT** — no funded `CoinStore<AptosCoin>` resource on mainnet for any address. Accounts likely exist on testnet only.

| World | Balance (APT) |
|---|---|
| alice | 0.0 |
| bob | 0.0 |
| A–Z (26 addresses) | 0.0 each |

### Multisig Contract Probes — 5/5 Healthy

All contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|---|---|---|---|
| A-B | 0x0da4…7003 | 2 | ✓ healthy |
| A-G | 0xf56c…0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff…b883 | 2 | ✓ healthy |
| S-T | 0x3b1c…7883 | 2 | ✓ healthy |
| V-W | 0x40fa…eb6d | 2 | ✓ healthy |

All 5 multisig contracts require **2-of-N signatures**. Consistent with prior state. No anomalies.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` serves a Next.js SPA. Both `/` and `/api/markets` return HTML, not JSON.  
**Status: unavailable** — market data requires client-side JS execution.

---

## Historical GF(3) Color Chain (all 14 increments)

| ID | Source | Event Type | GF3 | Color | Name |
|---|---|---|---|---|---|
| 1 | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | PLUS |
| 2 | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | MINUS |
| 3 | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | ERGODIC |
| 4 | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | PLUS |
| 5 | zubyul (user) | repo_snapshot | -1 | `#cc241d` | MINUS |
| 6 | migalkin (user) | repo_snapshot | 0 | `#d3869b` | ERGODIC |
| 7 | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | PLUS |
| 8 | wasita (user) | repo_snapshot | -1 | `#cc241d` | MINUS |
| 9 | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | ERGODIC |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | PLUS |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | MINUS |
| 12 | bmorphism | sweep_complete | 0 | `#d3869b` | ERGODIC |
| 13 | plurigrid/gorj | sweep_complete | +1 | `#b8bb26` | **PLUS** |
| 14 | scope_blocked | cross_org_blocked | -1 | `#cc241d` | **MINUS** |

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
