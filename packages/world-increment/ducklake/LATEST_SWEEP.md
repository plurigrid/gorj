# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-25

## Sweep Metadata

- **Date:** 2026-04-25
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 50 |
| kubeflow | org | 19 |
| bmorphism | user | 19 |
| zubyul | user | 13 |
| migalkin | user (zubyul social graph) | 7 |
| wasita | user (zubyul social graph) | 7 |
| AustinCStone | user (zubyul social graph) | 7 |
| DJedamski | user (zubyul social graph) | 5 |
| M1shaaa | user (zubyul social graph) | 5 |
| TeglonLabs | org | 4 |
| kristinezheng | user (zubyul social graph) | 4 |
| **TOTAL** | | **140** |

> Note: GitHub unauthenticated REST API was rate-limited (60 req/hr); all data collected via authenticated GitHub MCP search tools.

### GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 46 |
| +1 | PLUS | `#b8bb26` | 47 |
| -1 | MINUS | `#cc241d` | 47 |

GF(3) rule: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

### Top Repos by Stars

| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15,599 | — | 2026-04-24 |
| kubeflow/pipelines | 4,125 | Python | 2026-04-24 |
| kubeflow/spark-operator | 3,120 | Python | 2026-04-24 |
| kubeflow/trainer | 2,092 | Go | 2026-04-25 |
| kubeflow/katib | 1,679 | Python | 2026-04-23 |
| kubeflow/examples | 1,460 | Jsonnet | 2026-04-14 |
| kubeflow/manifests | 1,012 | YAML | 2026-04-19 |
| migalkin/NodePiece | 143 | Python | 2026-03-02 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml | 2026-03-28 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-02-05 |
| plurigrid/asi | 17 | HTML | 2026-04-25 |

### Notable Recent Activity (pushed 2026-04-25)

- `plurigrid/nanoclj-zig` — NaN-boxed Clojure interpreter in Zig 0.15, interaction nets, GF(3) trit conservation
- `plurigrid/asi` — "everything is topological chemputer!" (17 stars)
- `plurigrid/gorj` — forj + Rama topology nREPL routing + GF(3) gay trit coloring (273 open issues)
- `kubeflow/mcp-apache-spark-history-server` — 152 stars, MCP bridge for Apache Spark
- `bmorphism/nanoclj-zig` — personal fork of plurigrid/nanoclj-zig
- `zubyul/voice-observatory` — passive macOS TUI for voice-download pathways

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses queried via `POST /v1/view` → `0x1::coin::balance` view function.  
(Legacy `CoinStore` resource returns `resource_not_found` on migrated accounts; view function is the correct path.)

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
| A | 0.0518 |
| U | 0.0558 |
| V | 0.0488 |
| X | 0.0426 |
| Y | 0.0444 |
| B | 0.0363 |
| W | 0.0407 |
| Z | 0.0243 |
| C | 0.0102 |
| D | 0.0116 |
| E | 0.0094 |
| H | 0.0017 |
| G | 0.0007 |
| I | 0.0007 |

**Total APT across swarm:** 20.3448 APT

### Multisig Contract Probes (Aptos Mainnet)

All 5 contracts probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428a0c007da...` | 2 | ✅ |
| A-G | `0xf56c4a1c0906214f...` | 2 | ✅ |
| Y-Z | `0xd3ffe1812b2df406...` | 2 | ✅ |
| S-T | `0x3b1c3ae905d44c3a...` | 2 | ✅ |
| V-W | `0x40fad7b423a84365...` | 2 | ✅ |

All multisigs are 2-of-N. **5/5 healthy.**

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — DNS resolution failed (`DNS cache overflow`). The testnet endpoint is not reachable from this network environment. `mnx_snapshots` table is empty for this sweep.

---

## DuckDB Table Summary

| Table | Rows |
|-------|------|
| world_increments | 140 |
| repo_snapshots | 140 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

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
