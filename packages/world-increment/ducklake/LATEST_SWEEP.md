# World-Increment Sweep — 2026-07-14

## Sweep Metadata
- **Date:** 2026-07-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 73 (+50 this run) |
| Total Repo Snapshots | 994 (+50 this run) |
| Sources Covered | 3 orgs + 8 users (cumulative) |
| Aptos Wallets Snapshotted | 28 |
| Multisig Contracts Probed | 5 |
| Total Swarm APT | 20.344773 |

---

## GitHub Social Graph — Repo Counts by Source (Cumulative)

| Source | Type | Repos | Total Stars | Latest Push |
|--------|------|------:|------------:|-------------|
| plurigrid | org | 250 | 137 | 2026-07-14 |
| bmorphism | user | 200 | 262 | 2026-04-09 |
| TeglonLabs | org | 106 | 12 | 2026-01-16 |
| kubeflow | org | 94 | 67,723 | 2026-04-14 |
| AustinCStone | user | 86 | 216 | 2026-02-11 |
| migalkin | user | 60 | 554 | 2025-08-04 |
| wasita | user | 60 | 6 | 2026-04-13 |
| zubyul | user | 48 | 26 | 2026-04-09 |
| kristinezheng | user | 36 | 0 | 2026-04-09 |
| M1shaaa | user | 32 | 0 | 2026-04-13 |
| DJedamski | user | 22 | 14 | 2018-03-07 |
| **TOTAL** | | **994** | **69,950** | |

### Plurigrid Hot Repos (pushed 2026-07)
- `gorj` — Clojure, 1★ — forj + Rama topology nREPL routing + GF(3) gay trit coloring (pushed today)
- `eirobri` — Clojure, 0★ — EiRoBri replay world (pushed today)
- `asi` — HTML, 30★ — everything is topological chemputer!
- `place` — TeX, 1★
- `shrimp` — Jank worked example

### GF(3) Color Chain (this batch, increments 24–73)
| id % 3 | Trit | Color | Name |
|--------|-----:|-------|------|
| 0 | 0 | `#d3869b` | ERGODIC |
| 1 | +1 | `#b8bb26` | PLUS |
| 2 | −1 | `#cc241d` | MINUS |

Chain repeats: `ERGODIC → PLUS → MINUS → ...` (17 full cycles completed)

---

## Hamming Swarm Snapshot — Aptos Mainnet

**Timestamp:** 2026-07-14T04:13 UTC  
**Method:** `0x1::coin::balance` via POST `/v1/view` (fungible asset module)

### Wallet Balances (28 wallets)

| World | Balance (APT) | Address |
|-------|-------------:|---------|
| bob | 12.657007 | `0x0a3c00c5...` |
| F | 1.960516 | `0x18a14b5b...` |
| L | 1.927269 | `0x7c2eaeaf...` |
| J | 1.895093 | `0x4d964db8...` |
| alice | 0.436434 | `0xc793acde...` |
| O | 0.210136 | `0x73252b60...` |
| K | 0.161961 | `0xa732040a...` |
| P | 0.140136 | `0x6218792d...` |
| M | 0.112285 | `0x6fed37a7...` |
| N | 0.106121 | `0xe7dde6da...` |
| Q | 0.103240 | `0xac40fa50...` |
| S | 0.091788 | `0xb8753014...` |
| R | 0.090217 | `0x7ce605cc...` |
| T | 0.073713 | `0x35781dc0...` |
| U | 0.055773 | `0x75860da4...` |
| A | 0.051767 | `0x8699edc0...` |
| V | 0.048833 | `0xb59dd817...` |
| Y | 0.044449 | `0xd8e32848...` |
| X | 0.042577 | `0xa95cbbd1...` |
| W | 0.040705 | `0x5f32aef7...` |
| B | 0.036256 | `0x3f892ebe...` |
| Z | 0.024268 | `0x7af0ef6e...` |
| D | 0.011629 | `0xf7765624...` |
| C | 0.010185 | `0x38b99e63...` |
| E | 0.009372 | `0xdc1d9d53...` |
| H | 0.001681 | `0xce67c327...` |
| I | 0.000681 | `0x070fe5d7...` |
| G | 0.000681 | `0x69a394c0...` |

**Total swarm balance: 20.344773 APT**

Top holders: bob (62.2%), F (9.6%), L (9.5%), J (9.3%)

### Multisig Contract Probes — All Healthy

| Pair | Address | Sigs Required | Status |
|------|---------|:-------------:|--------|
| A-B | `0x0da4f428...` | 2 | healthy |
| A-G | `0xf56c4a1c...` | 2 | healthy |
| Y-Z | `0xd3ffe181...` | 2 | healthy |
| S-T | `0x3b1c3ae9...` | 2 | healthy |
| V-W | `0x40fad7b4...` | 2 | healthy |

All 5 multisig contracts require 2-of-2 signatures. All confirmed reachable and healthy.

---

## MNX Markets (testnet.mnx.fi)

**Status: 401 Unauthorized** — SPA requires authentication; no unauthenticated API surface accessible. Recorded as unavailable in `mnx_snapshots`.

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
- `id % 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id % 3 == 1` → trit=+1, color=`#b8bb26`, name=PLUS
- `id % 3 == 2` → trit=−1, color=`#cc241d`, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — most popular ML pipeline for Kubernetes
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml MCP SDK via Jane Street oxcaml_effect
- **plurigrid/asi**: 30 stars (up from 16 on 2026-04-12) — topological chemputer
- **plurigrid/gorj**: This repo — GF(3) trit coloring, active today
- **Aptos bob**: 12.66 APT — largest single wallet in swarm
- **All multisigs**: 2-of-2 threshold, all 5 healthy
