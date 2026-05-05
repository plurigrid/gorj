# World-Increment Sweep + Hamming Snapshot
**Date:** 2026-05-05T12:02–12:15 UTC  
**DuckDB:** v1.5.2 (Variegata)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 50 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 50 |
| zubyul | user | 49 |
| migalkin | user (social graph) | 19 |
| DJedamski | user (social graph) | 6 |
| wasita | user (social graph) | 10 |
| kristinezheng | user (social graph) | 6 |
| M1shaaa | user (social graph) | 8 |
| AustinCStone | user (social graph) | 30 |
| **Total new** | | **279** |

### Notable Repos (by stars)
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,621 | — | 2026-04-29 |
| kubeflow/pipelines | 4,132 | Python | 2026-05-04 |
| kubeflow/spark-operator | 3,123 | Python | 2026-04-28 |
| kubeflow/trainer | 2,096 | Go | 2026-05-05 |
| kubeflow/arena | 810 | Go | 2026-04-28 |
| migalkin/NodePiece | 143 | Python | 2022-02-02 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml | 2026-03-16 |
| plurigrid/asi | 18 | HTML | 2026-04-26 |

### Recent Plurigrid Activity
| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| plurigrid/zig-syrup | Zig | 2 | 2026-04-30 |
| plurigrid/gorj | Clojure | 0 | 2026-05-05 |
| plurigrid/horse | TeX | 1 | 2026-04-29 |
| plurigrid/asi | HTML | 18 | 2026-04-26 |
| plurigrid/nash-portal | Rust | 2 | 2026-04-26 |

### Recent bmorphism Activity
| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| bmorphism/boxxy | Move | 0 | 2026-04-30 |
| bmorphism/Gay.jl | Julia | 1 | 2026-05-05 |
| bmorphism/nanoclj-zig | Zig | 0 | 2026-04-25 |
| bmorphism/postweb | Go | 0 | 2026-04-09 |
| bmorphism/shitcoin | Python | 5 | 2026-04-08 |

### GF(3) Color Chain Distribution
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 100 |
| 1 | `#b8bb26` | PLUS | 101 |
| -1 | `#cc241d` | MINUS | 101 |

GF(3) rule: id%3==0 -> ERGODIC, id%3==1 -> PLUS, id%3==2 -> MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet — 28 addresses)
All addresses (alice, bob, A-Z) returned resource_not_found for
0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>.
All balances: **0.0 APT** (accounts not initialized with APT on mainnet).

| World | Address | Balance |
|-------|---------|---------|
| alice | 0xc793...cc7b | 0.0 APT |
| bob | 0x0a3c...2d5d | 0.0 APT |
| A-Z | (26 addresses) | 0.0 APT each |

### Multisig Contract Probes (5 pairs)
All 5 probed via 0x1::multisig_account::num_signatures_required. All return ["2"].
**Swarm multisig layer is fully intact.**

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | healthy |
| A-G | 0xf56c...0096 | 2 | healthy |
| Y-Z | 0xd3ff...b883 | 2 | healthy |
| S-T | 0x3b1c...7883 | 2 | healthy |
| V-W | 0x40fa...eb6d | 2 | healthy |

### MNX Markets (testnet.mnx.fi)
testnet.mnx.fi is a Next.js SPA. No REST API endpoints returned data:
- /api/markets -> 404
- /api/v1/markets -> 404
- /api/tickers -> 404

MNX market data **unavailable** via public API. mnx_snapshots table is empty.

---

## DuckDB State
| Table | Total Rows |
|-------|-----------|
| world_increments | 302 |
| repo_snapshots | 1,223 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

Cumulative across all sweeps since 2026-04-12.

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
