# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-24

## Sweep Metadata
- **Date:** 2026-07-24
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Captured

| Source | Type | Repos (this run) |
|--------|------|------------------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | user (zubyul social) | ~38 |
| TeglonLabs | org | 5 |
| migalkin | user (zubyul social) | ~26 |
| wasita | user (zubyul social) | 12 |
| kristinezheng | user (zubyul social) | 5 |
| M1shaaa | user (zubyul social) | 8 |
| DJedamski | user (zubyul social) | 6 |

**DB state after this run:** 382 world_increments, 1303 repo_snapshots (cumulative incl. prior sweeps)

### Top Repos by Stars (this sweep)

| Repo | Stars | Forks | Language |
|------|-------|-------|----------|
| kubeflow/kubeflow | 15,792 | 2,686 | — |
| kubeflow/pipelines | 4,169 | 2,058 | Python |
| kubeflow/spark-operator | 3,143 | 1,504 | Python |
| kubeflow/trainer | 2,153 | 995 | Go |
| migalkin/NodePiece | 143 | 28 | Python |
| bmorphism/ocaml-mcp-sdk | 60 | — | OCaml |
| AustinCStone/TextGAN | 92 | — | Python |
| plurigrid/asi | 16 | — | HTML |

### Notable Activity

- **M1shaaa/M1shaaa** profile repo last pushed **2026-07-24T13:28 UTC** (today)
- **wasita/wasita.github.io** last pushed **2026-07-21T15:52** (Svelte personal site, active)
- **kristinezheng/kristinezheng.github.io** last pushed **2026-07-01** (HTML portfolio)
- **TeglonLabs/jank-crane** (C++, pushed 2026-06-08): crane-jank converged-IR hub, GF3 convergence maps
- **TeglonLabs/mathpix-gem** (Ruby ★2): mathematical OCR gem

### GF(3) Color Chain (per-increment ID mod 3)
- `id%3==0` → trit=0, color=#d3869b, name=**ERGODIC**
- `id%3==1` → trit=1, color=#b8bb26, name=**PLUS**
- `id%3==2` → trit=-1, color=#cc241d, name=**MINUS**

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Balances (28 wallets, queried 2026-07-24)

| World | Balance (APT) |
|-------|---------------|
| alice | 0.4364 |
| bob | **12.6570** |
| A | 0.0518 |
| B | 0.0363 |
| C | 0.0102 |
| D | 0.0116 |
| E | 0.0094 |
| F | **1.9605** |
| G | 0.0007 |
| H | 0.0017 |
| I | 0.0007 |
| J | **1.8951** |
| K | 0.1620 |
| L | **1.9273** |
| M | 0.1123 |
| N | 0.1061 |
| O | 0.2101 |
| P | 0.1401 |
| Q | 0.1032 |
| R | 0.0902 |
| S | 0.0918 |
| T | 0.0737 |
| U | 0.0558 |
| V | 0.0488 |
| W | 0.0407 |
| X | 0.0426 |
| Y | 0.0444 |
| Z | 0.0243 |

**Total swarm APT:** ~20.41 APT  
**Top holders:** bob (12.66), F (1.96), L (1.93), J (1.90), alice (0.44)  
**Dust wallets (< 0.002 APT):** G, H, I

### Multisig Contract Probes

| Pair | Threshold | Healthy |
|------|-----------|---------|
| A-B (0x0da4…003) | 2-of-2 | ✅ |
| A-G (0xf56c…096) | 2-of-2 | ✅ |
| Y-Z (0xd3ff…883) | 2-of-2 | ✅ |
| S-T (0x3b1c…883) | 2-of-2 | ✅ |
| V-W (0x40fa…b6d) | 2-of-2 | ✅ |

All 5 multisig contracts operational with 2-of-2 threshold.

### MNX Markets

`https://testnet.mnx.fi` — Next.js SPA (200 OK, served from Vercel).  
REST API paths `/markets`, `/v1/markets` return 404 — data served over WebSocket (`wss://api.testnet.mnx.fi`).  
**mnx_snapshots: 0 rows this run (WebSocket-only API, not crawlable via curl).**

---

## DuckDB Table Counts

| Table | Rows |
|-------|------|
| world_increments | 382 |
| repo_snapshots | 1303 |
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
