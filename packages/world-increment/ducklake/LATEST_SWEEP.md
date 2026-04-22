# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-04-22T20:10Z  
**DuckDB version:** v1.5.2 (Variegata)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 47 |
| zubyul | user | 47 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| wasita | user | 10 |
| M1shaaa | user | 8 |
| kristinezheng | user | 6 |
| DJedamski | user | 6 |
| TeglonLabs | org | 4 |
| **Total** | | **387** |

Social graph covered: plurigrid org + zubyul's network (migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone).

### GF(3) Color Chain Assignment

Each world-increment row is assigned a GF(3) trit by `(id-1) mod 3`:

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 129 |
| 1 | PLUS | `#b8bb26` | 129 |
| -1 | MINUS | `#cc241d` | 129 |

Chain repeats: ERGODIC → PLUS → MINUS → ERGODIC → ...

### DuckDB Table Counts

| Table | Rows |
|-------|------|
| world_increments | 387 |
| repo_snapshots | 387 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried 28 addresses against `fullnode.mainnet.aptoslabs.com` (1s sleep between calls).  
All addresses returned 0 APT — CoinStore resource not initialized on mainnet for these wallets.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | `0xc793...cc7b` | 0.0 |
| bob | `0x0a3c...2d5d` | 0.0 |
| A | `0x8699...9d7a` | 0.0 |
| B | `0x3f89...b13` | 0.0 |
| C–Z | (each) | 0.0 |

**Total APT across swarm:** 0.0

### Multisig Contract Probes

Probed via `POST /v1/view → 0x1::multisig_account::num_signatures_required`:

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | `0x0da4...7003` | 0 | ❌ not initialized |
| A-G | `0xf56c...0096` | 2 | ✅ healthy |
| Y-Z | `0xd3ff...b883` | 2 | ✅ healthy |
| S-T | `0x3b1c...7883` | 2 | ✅ healthy |
| V-W | `0x40fa...eb6d` | 2 | ✅ healthy |

**4/5 multisig accounts live** with 2-of-N threshold. A-B address has no multisig module.

### MNX Markets

`testnet.mnx.fi` is a Next.js SPA ("MNX — The AI Exchange").  
Backend API endpoint `api.testnet.mnx.fi` was unreachable (DNS not resolving from sweep network).  
`mnx_snapshots` table: 0 rows (no public market data accessible).

---

## Full Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(timestamp, world, address, balance_apt)  -- 28 rows
multisig_probes(timestamp, pair, address, sigs_required, healthy)  -- 5 rows
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)  -- 0 rows
```

## GF(3) Assignment Rule

```
(id-1) mod 3 == 0  →  trit=0,  color=#d3869b,  name=ERGODIC
(id-1) mod 3 == 1  →  trit=1,  color=#b8bb26,  name=PLUS
(id-1) mod 3 == 2  →  trit=-1, color=#cc241d,  name=MINUS
```
