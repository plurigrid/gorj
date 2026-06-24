# World Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-06-24  
**GF(3) Color Chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted (Today)

| Source | Type | Repos Sampled | Total Stars |
|--------|------|---------------|-------------|
| kubeflow | org | 48 | 34,250 |
| plurigrid | org | 100 | 77 |
| bmorphism | user | 50+ (10 top) | 84 |
| migalkin | user | 19 | 276 |
| zubyul | user | 49 (5 top) | 1 |
| AustinCStone | user | 40 (5 top) | 106 |
| wasita | user | 11 (5 top) | 4 |
| TeglonLabs | org | 5 | 2 |
| DJedamski | user | 6 (4 top) | 3 |
| kristinezheng | user | 5 (3 top) | 0 |
| M1shaaa | user | 8 (3 top) | 0 |

### Top Repos by Stars (Today's Snapshot)

| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15,741 | — | 2026-06-18 |
| kubeflow/pipelines | 4,157 | Python | 2026-06-23 |
| kubeflow/spark-operator | 3,128 | Python | 2026-06-24 |
| kubeflow/trainer | 2,119 | Go | 2026-06-22 |
| kubeflow/katib | 1,685 | Python | 2026-06-23 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1,028 | YAML | 2026-06-18 |
| kubeflow/arena | 813 | Go | 2026-05-07 |
| kubeflow/kale | 694 | Python | 2026-06-22 |
| kubeflow/mpi-operator | 528 | Go | 2026-06-23 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-02-05 |
| bmorphism/say-mcp-server | 20 | JavaScript | 2026-03-19 |
| bmorphism/babashka-mcp-server | 19 | JavaScript | 2026-06-05 |

### Notable Plurigrid Repos

| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| plurigrid/ontology | JavaScript | 8 | 2025-05-27 |
| plurigrid/StochFlow | Python | 4 | 2024-03-20 |
| plurigrid/Plurigraph | JavaScript | 3 | 2025-01-05 |
| plurigrid/asi-skills | Julia | 3 | 2026-04-26 |
| plurigrid/zig-syrup | Zig | 2 | 2026-04-30 |
| plurigrid/nanoclj-zig | Zig | 1 | 2026-04-25 |
| plurigrid/duck-kanban | Rust | 1 | 2025-09-26 |

### Notable TeglonLabs Repos

| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| TeglonLabs/jank-crane | C++ | 0 | 2026-06-08 |
| TeglonLabs/mathpix-gem | Ruby | 2 | 2026-01-01 |
| TeglonLabs/coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

### DuckDB Ducklake State (Cumulative)

- **world_increments**: 216 rows total (GF3 color-chained, accumulating since 2026-04-12)
- **repo_snapshots**: 1,137 rows total (554 unique repos across all sweeps)
- **Database**: `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (2026-06-24)

All 28 Hamming swarm addresses (alice, bob, A–Z) probed via Aptos fullnode mainnet API  
(`https://fullnode.mainnet.aptoslabs.com/v1/accounts/{ADDR}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`).

**Result: All balances returned 0 APT.** The `CoinStore<AptosCoin>` resource was not found  
for any address — accounts are either not initialized on mainnet or hold zero APT.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.00000000 |
| bob | 0x0a3c...2d5d | 0.00000000 |
| A | 0x8699...9d7a | 0.00000000 |
| B–Z | (see DB) | 0.00000000 each |

### Multisig Contract Probes (Aptos Mainnet)

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f...7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c4...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✓ HEALTHY |

All multisig contracts require **2-of-N** signatures and are responsive and healthy.

### MNX Markets

**Status: UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel authentication.  
All API endpoints (`/api/markets`, `/api/tickers`, root) return auth challenge.  
No market data extractable without bypass token. `mnx_snapshots` table has 0 rows.

---

## GF(3) Color Chain

| trit | color | name | rule |
|------|-------|------|------|
| 0 | #d3869b | ERGODIC | id mod 3 == 0 |
| +1 | #b8bb26 | PLUS | id mod 3 == 1 |
| -1 | #cc241d | MINUS | id mod 3 == 2 |

Current world_increments chain: 216 entries spanning 2026-04-12 → 2026-06-24.

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
