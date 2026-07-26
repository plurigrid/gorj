# World-Increment Sweep + Hamming Snapshot — 2026-07-26

## Sweep Metadata
- **Date:** 2026-07-26
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Increment ID:** 13 · trit=1 · **PLUS** · `#b8bb26`
- **Aptos ledger version at query time:** 6,457,466,291

---

## JOB 1: GitHub Social Graph Sweep

**Scope note:** GitHub API in this session is bound to `plurigrid/gorj` only.  
Cross-org/user queries (`kubeflow`, `TeglonLabs`, `bmorphism`, `zubyul`, social graph) are blocked by the session's repository policy. This sweep records the accessible repo only.

| Field | Value |
|---|---|
| Repo | `plurigrid/gorj` |
| Language | Clojure |
| Description | MCP server + hooks that give AI coding agents a Clojure REPL |
| Last pushed | 2026-05-08T14:04:34Z |
| Total commits | 105 |
| Top contributors | Alex R Teal (67), Claude (36), Yuliya Zubak (2) |

**Cumulative DB state after sweep:**
- `world_increments`: 13 rows (IDs 1–13)
- `repo_snapshots`: 945 rows (+1 this run; 944 from prior sweeps)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
Queried via `https://fullnode.mainnet.aptoslabs.com/v1` — all addresses returned HTTP 404  
(`resource_not_found` = `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` not initialized).

| World | Address (truncated) | Balance (APT) |
|---|---|---|
| alice | `0xc793ac...624cc7b` | 0.00000000 |
| bob | `0x0a3c00...512d5d` | 0.00000000 |
| A | `0x8699ed...be9d7a` | 0.00000000 |
| B | `0x3f892e...7cb13` | 0.00000000 |
| C | `0x38b99e...91535e` | 0.00000000 |
| D | `0xf77656...fcfdd1` | 0.00000000 |
| E | `0xdc1d9d...958d36` | 0.00000000 |
| F | `0x18a14b...c3cf71` | 0.00000000 |
| G | `0x69a394...cc7f32` | 0.00000000 |
| H | `0xce67c3...e5300f` | 0.00000000 |
| I | `0x070fe5...c1fc9` | 0.00000000 |
| J | `0x4d964d...87f54` | 0.00000000 |
| K | `0xa73204...425dc4` | 0.00000000 |
| L | `0x7c2eae...37eba9` | 0.00000000 |
| M | `0x6fed37...b7f2e9` | 0.00000000 |
| N | `0xe7dde6...551b2c` | 0.00000000 |
| O | `0x73252b...a5a89d` | 0.00000000 |
| P | `0x621879...1ec948` | 0.00000000 |
| Q | `0xac40fa...5c89a9` | 0.00000000 |
| R | `0x7ce605...d76e10` | 0.00000000 |
| S | `0xb87530...9d0386` | 0.00000000 |
| T | `0x35781d...d3f4588` | 0.00000000 |
| U | `0x75860d...ef9956` | 0.00000000 |
| V | `0xb59dd8...89af2c3` | 0.00000000 |
| W | `0x5f32ae...cc7b0` | 0.00000000 |
| X | `0xa95cbb...e33047d` | 0.00000000 |
| Y | `0xd8e328...a2444c4` | 0.00000000 |
| Z | `0x7af0ef...4e197c` | 0.00000000 |

**Total swarm APT:** 0.00000000 (all 28 addresses uninitialised on-chain)

### Multisig Contract Probes
All 5 multisig accounts healthy — 2-of-2 threshold confirmed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|---|---|---|---|
| A-B | `0x0da4f4...4987003` | 2 | ✓ |
| A-G | `0xf56c4a...fbc0096` | 2 | ✓ |
| Y-Z | `0xd3ffe1...e75b883` | 2 | ✓ |
| S-T | `0x3b1c3a...ded7883` | 2 | ✓ |
| V-W | `0x40fad7...c80eb6d` | 2 | ✓ |

### MNX Markets (`testnet.mnx.fi`)
Site is reachable (Next.js SPA, HTTP 200). No JSON REST API endpoints found  
(`/api/markets`, `/api/tickers`, `/api/pairs`, `/api/v1/markets`, `/api/v2/markets`, `/markets`, `/api/stats`, `/api/market/list` all return HTML).  
Market data recorded as **unavailable** this sweep.

---

## DuckDB Table Summary

| Table | Total Rows | Added This Run |
|---|---|---|
| `world_increments` | 13 | 1 |
| `repo_snapshots` | 945 | 1 |
| `aptos_snapshots` | 28 | 28 |
| `multisig_probes` | 5 | 5 |
| `mnx_snapshots` | 1 | 1 |

---

## GF(3) Color Chain (full history)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|---|---|---|---|---|---|
| 1 | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2 | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3 | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4 | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5 | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6 | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7 | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8 | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9 | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 12 | bmorphism | sweep_complete | 0 | `#d3869b` | **ERGODIC** |
| **13** | **plurigrid/gorj** | **sweep_complete** | **+1** | **`#b8bb26`** | **PLUS** |

GF(3) chain continues: `…MINUS → ERGODIC → PLUS` (opening 5th cycle)

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
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
