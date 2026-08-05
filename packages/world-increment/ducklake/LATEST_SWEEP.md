# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-08-05  
**Run type:** Automated — world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** v1.5.5 (Variegata)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted | Latest Push |
|--------|------|-------------------|-------------|
| plurigrid | org | 100 | 2026-08-05T06:21:22Z |
| kubeflow | org | 49 | 2026-08-05T05:43:13Z |
| TeglonLabs | org | 5 | 2026-06-08T19:03:03Z |
| bmorphism | user | 100 | 2026-08-05T02:24:27Z |
| zubyul | user | 49 | 2026-07-18T12:02:57Z |
| migalkin | social-graph | 19 | 2025-08-04T03:01:46Z |
| DJedamski | social-graph | 6 | 2018-03-07T12:36:09Z |
| wasita | social-graph | 14 | 2026-08-04T21:49:54Z |
| kristinezheng | social-graph | 5 | 2026-07-01T20:57:44Z |
| M1shaaa | social-graph | 8 | 2026-08-05T02:07:23Z |
| AustinCStone | social-graph | 30 | 2026-07-15T05:19:30Z |

**Total repos snapshotted (this sweep):** 385  
**Total world increments in DB:** 408  
**Total repo snapshot records in DB:** 1329

### GF(3) Color Chain
- `id % 3 == 0` → trit=0 **ERGODIC** #d3869b (pink)
- `id % 3 == 1` → trit=1 **PLUS** #b8bb26 (green)
- `id % 3 == 2` → trit=-1 **MINUS** #cc241d (red)

### Notable Active Repos (2026-08-05)
- **wasita/xoxowasita-analysis** — Python data analysis, pushed 2026-08-04
- **M1shaaa/M1shaaa** — profile updated today (2026-08-05)
- **bmorphism** — most recently pushed 2026-08-05
- **plurigrid** — most recently pushed 2026-08-05
- **kubeflow/pipelines** — 4119 stars, active development

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (FA API)

All 28 addresses queried via `0x1::primary_fungible_store::balance` (Fungible Asset API).  
**Note:** Legacy `0x1::coin::CoinStore` returned resource-not-found; Aptos migrated to FA module.

| World | Balance (APT) |
|-------|--------------|
| bob | 12.6570 |
| F | 1.9605 |
| L | 1.9273 |
| J | 1.8951 |
| alice | 0.4364 |
| O | 0.2101 |
| K | 0.1620 |
| P | 0.1401 |
| M | 0.1123 |
| N | 0.1061 |
| Q | 0.1032 |
| S | 0.0918 |
| R | 0.0902 |
| T | 0.0737 |
| U | 0.0558 |
| A | 0.0518 |
| V | 0.0488 |
| Y | 0.0444 |
| X | 0.0426 |
| W | 0.0407 |
| B | 0.0363 |
| Z | 0.0243 |
| D | 0.0116 |
| C | 0.0102 |
| E | 0.0094 |
| H | 0.0017 |
| I | 0.0007 |
| G | 0.0007 |

**Total APT across all 28 addresses:** 20.3448 APT  
**Largest holder:** bob (12.6570 APT — 62% of swarm total)

### Multisig Contract Probes

All 5 multisig contracts are **HEALTHY** — all require exactly 2 signatures.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...987003 | 2 | ✓ healthy |
| A-G | 0xf56c4a1c...c0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ healthy |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

**Status: SPA — no REST API data accessible**  
`/api/markets` returns the Next.js SPA HTML shell; market data is client-rendered. No structured data available via static HTTP. `mnx_snapshots` table remains empty.

---

## DuckDB Table State

| Table | Records This Sweep | Total in DB |
|-------|-------------------|-------------|
| world_increments | 385 | 408 |
| repo_snapshots | 385 | 1329 |
| aptos_snapshots | 28 | 28 |
| multisig_probes | 5 | 5 |
| mnx_snapshots | 0 | 0 |

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
