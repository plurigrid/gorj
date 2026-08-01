# World-Increment Sweep + Hamming Swarm Snapshot — 2026-08-01

## Sweep Metadata
- **Date:** 2026-08-01
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Snapshots This Run (382 repos across 11 sources)

| Source | Type | Repos | Latest Push |
|--------|------|------:|-------------|
| plurigrid | org | 100 | 2026-08-01T18:14:24Z |
| bmorphism | user | 100 | 2026-08-01T02:39:17Z |
| kubeflow | org | 49 | 2026-08-01T17:30:30Z |
| zubyul | user | 49 | 2026-07-18T12:02:57Z |
| AustinCStone | user | 30 | 2026-07-15T05:19:30Z |
| migalkin | user | 19 | 2025-08-04T03:01:46Z |
| wasita | user | 12 | 2026-07-21T15:52:20Z |
| M1shaaa | user | 8 | 2026-08-01T13:11:14Z |
| DJedamski | user | 6 | 2018-03-07T12:36:09Z |
| kristinezheng | user | 5 | 2026-07-01T20:57:44Z |
| TeglonLabs | org | 4 (public) | 2026-06-08T19:03:03Z |
| **TOTAL** | | **382** | — |

### Notable Activity
- **plurigrid**, **bmorphism**, **M1shaaa**: pushed today (2026-08-01)
- **kubeflow**: 49 repos active, latest push 17:30 UTC today
- **TeglonLabs/jank-crane** (C++): GF3 convergence maps + loopify pass spec, pushed 2026-06-08
- **TeglonLabs/mathpix-gem** (Ruby, 2★): 11 open issues — mathematical OCR gem
- **wasita/wasita.github.io** (Svelte): personal site pushed 2026-07-21

### GF(3) Color Chain Distribution (382 world-increments this run)
- **ERGODIC** (trit=0, `#d3869b`): 128 increments
- **PLUS** (trit=1, `#b8bb26`): 127 increments
- **MINUS** (trit=-1, `#cc241d`): 127 increments

### Cumulative DuckDB State
- `world_increments`: 405 rows total
- `repo_snapshots`: 1326 rows total

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 28 addresses)

All 28 wallets queried via `https://fullnode.mainnet.aptoslabs.com/v1/`.  
**Result:** All wallets returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — balance = **0.0 APT** for all.

Addresses queried: alice, bob, A through Z (28 total).

### Multisig Contract Probes — 5/5 Healthy ✓

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|:-------------:|:-------:|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

All 5 multisig contracts are 2-of-2 signers and respond correctly.

### MNX Markets (testnet.mnx.fi)

Site is live (Next.js SPA) but no REST API endpoints accessible — all data is client-rendered. **Marked unavailable** for this snapshot. `mnx_snapshots` table is empty.

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
- `id mod 3 == 0` → trit=0, `#d3869b`, ERGODIC
- `id mod 3 == 1` → trit=1, `#b8bb26`, PLUS
- `id mod 3 == 2` → trit=-1, `#cc241d`, MINUS
