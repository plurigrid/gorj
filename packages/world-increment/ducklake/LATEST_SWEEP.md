# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-28

## Sweep Metadata
- **Date:** 2026-06-28
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos This Run |
|--------|------|----------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | zubyul social graph | (prior sweep data) |
| DJedamski | zubyul social graph | (prior sweep data) |
| wasita | zubyul social graph | (prior sweep data) |
| kristinezheng | zubyul social graph | (prior sweep data) |
| M1shaaa | zubyul social graph | (prior sweep data) |
| AustinCStone | zubyul social graph | (prior sweep data) |

**Total repo_snapshots in DB:** 1,246 (cumulative)
**World increments in DB:** 320 (cumulative, 297 new this run)

### GF(3) Color Chain
| Name | Color | Trit | Rule |
|------|-------|------|------|
| PLUS | #b8bb26 | +1 | id % 3 == 1 |
| MINUS | #cc241d | -1 | id % 3 == 2 |
| ERGODIC | #d3869b | 0 | id % 3 == 0 |

GF(3) cycle: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → ...`

### Top Repos by Stars (Kubeflow)
| Repo | Language | Stars | Forks | Last Push |
|------|----------|-------|-------|-----------|
| kubeflow | — | 15,749 | 2,680 | 2026-06-18 |
| pipelines | Python | 4,158 | 2,012 | 2026-06-27 |
| spark-operator | Python | 3,129 | 1,492 | 2026-06-26 |
| trainer | Go | 2,125 | 972 | 2026-06-26 |
| katib | Python | 1,687 | 527 | 2026-06-23 |
| examples | Jsonnet | 1,460 | 756 | 2025-04-14 |
| community-distribution | YAML | 1,028 | 1,065 | 2026-06-25 |

### TeglonLabs Repos (newest, 5 repos)
| Repo | Language | Stars | Open Issues | Last Push | Description |
|------|----------|-------|-------------|-----------|-------------|
| jank-crane | C++ | 0 | 0 | 2026-06-08 | crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps |
| mathpix-gem | Ruby | 2 | 11 | 2026-01-01 | Transform mathematical images to LaTeX |
| coin-flip-mcp | JavaScript | 0 | 1 | 2025-09-21 | MCP server for flipping coins |
| monad-mcp-server | — | 0 | 0 | 2025-05-14 | Monad MCP Server |
| topoi | Python | 0 | 1 | 2025-01-24 | — |

### Repo Counts by Source (Cumulative DB)
| Source | Repo Count |
|--------|------------|
| bmorphism | 300 |
| plurigrid | 300 |
| kubeflow | 142 |
| TeglonLabs | 111 |
| zubyul | 97 |
| AustinCStone | 86 |
| wasita | 60 |
| migalkin | 60 |
| kristinezheng | 36 |
| M1shaaa | 32 |
| DJedamski | 22 |
| **TOTAL** | **1,246** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
**28 wallets probed** via `fullnode.mainnet.aptoslabs.com`

| Metric | Value |
|--------|-------|
| Total wallets | 28 |
| Funded wallets | 0 |
| Total APT | 0.00000000 |

All 28 wallets (alice, bob, A–Z) returned 0 APT. The `CoinStore<AptosCoin>` resource was not found or balances are zero — wallets are either uninitialized or empty on mainnet.

### Multisig Contract Probes
All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...987003 | 2 | HEALTHY |
| A-G | 0xf56c4a1c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ffe181...b883 | 2 | HEALTHY |
| S-T | 0x3b1c3ae9...7883 | 2 | HEALTHY |
| V-W | 0x40fad7b4...eb6d | 2 | HEALTHY |

**All 5 multisig contracts are reachable and require 2-of-N signatures.**

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — Protected by Vercel deployment authentication. Both `/api/markets` and `/api/v1/markets` return auth-required HTML. `mnx_snapshots` table: 0 rows this run.

---

## DuckDB Table Summary
| Table | Rows |
|-------|------|
| world_increments | 320 |
| repo_snapshots | 1,246 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

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
