# World-Increment Sweep + Hamming Snapshot — 2026-04-05

**Date:** 2026-04-05  
**Agent:** world-increment-sweep (autonomous two-job sweep)  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## GitHub Sweep Summary

### Sources Queried

| Source | Type | Repos Found |
|--------|------|-------------|
| plurigrid | org | 95 |
| kubeflow | org | 46 |
| TeglonLabs | org | 3 |
| bmorphism | user | 97 |
| zubyul | user | 44 |
| migalkin | user | 19 |
| DJedamski | user | 6 |
| wasita | user | 9 |
| kristinezheng | user | 6 |
| M1shaaa | user | 8 |
| AustinCStone | user | 40 |
| **TOTAL** | | **373** |

**Total repo_snapshot rows inserted: 1311** (includes GF3 increment chain rows)  
**World increment records: 11**

### Top Repos by Stars

| Repo | Language | Stars | Forks | Description |
|------|----------|-------|-------|-------------|
| kubeflow/kubeflow | - | 15,552 | 2,628 | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | Python | 4,118 | 1,983 | Machine Learning Pipelines for Kubeflow |
| kubeflow/spark-operator | Python | 3,110 | 1,480 | K8s operator for Apache Spark |
| kubeflow/trainer | Go | 2,074 | 942 | Distributed AI Model Training on K8s |
| kubeflow/katib | Python | 1,674 | 519 | Automated Machine Learning on K8s |
| kubeflow/examples | Jsonnet | 1,459 | 755 | Extended examples and tutorials |
| kubeflow/manifests | YAML | 1,007 | 1,068 | Kubeflow AI Reference Platform Deployment |
| kubeflow/arena | Go | 809 | 190 | A CLI for Kubeflow |
| kubeflow/kale | Python | 682 | 156 | Kubeflow's superfood for Data Scientists |
| migalkin/NodePiece | Python | 143 | - | Parameter-Efficient KG Representations |
| migalkin/StarE | Python | 88 | - | StarE knowledge graph model |
| bmorphism/ocaml-mcp-sdk | OCaml | 60 | - | OCaml MCP SDK |
| AustinCStone/TextGAN | Python | 92 | - | Text generation with GANs |
| plurigrid/asi | HTML | 15 | 5 | ASI topological chemputer |
| plurigrid/ontology | JavaScript | 7 | 9 | Plurigrid ontology |

---

## Aptos Snapshot (Hamming Swarm)

All 28 addresses queried on Aptos Mainnet via `CoinStore<AptosCoin>` resource.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...9956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

> All 28 addresses returned 0 APT balance. The `CoinStore<AptosCoin>` resource was not initialized for any of these addresses on Aptos mainnet at time of sweep.

---

## Multisig Probe Results

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✓ HEALTHY |

**All 5 multisig contracts healthy** — 2-of-N signature threshold confirmed.

---

## MNX Market Status

**Status: UNAVAILABLE**

`https://testnet.mnx.fi/api/markets` returns a Next.js HTML app, not a JSON REST API. No discoverable public API endpoint for market data. MNX markets table left empty this sweep.

---

## GF(3) Color Chain Summary

| ID | trit | Color | Name | Source | Type |
|----|------|-------|------|--------|------|
| 1 | +1 | `#b8bb26` | PLUS | plurigrid | org |
| 2 | -1 | `#cc241d` | MINUS | kubeflow | org |
| 3 | 0 | `#d3869b` | ERGODIC | TeglonLabs | org |
| 4 | +1 | `#b8bb26` | PLUS | bmorphism | user |
| 5 | -1 | `#cc241d` | MINUS | zubyul | user |
| 6 | 0 | `#d3869b` | ERGODIC | migalkin | user |
| 7 | +1 | `#b8bb26` | PLUS | DJedamski | user |
| 8 | -1 | `#cc241d` | MINUS | wasita | user |
| 9 | 0 | `#d3869b` | ERGODIC | kristinezheng | user |
| 10 | +1 | `#b8bb26` | PLUS | M1shaaa | user |
| 11 | -1 | `#cc241d` | MINUS | AustinCStone | user |

**GF(3) rule:** `id%3==0` → trit=0 ERGODIC `#d3869b` | `id%3==1` → trit=+1 PLUS `#b8bb26` | `id%3==2` → trit=-1 MINUS `#cc241d`

---

## DuckDB Table Summary

| Table | Rows |
|-------|------|
| world_increments | 11 |
| repo_snapshots | 1311 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

---

## Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name, actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues, pushed_at, description)

aptos_snapshots(timestamp, world, address, balance_apt)

multisig_probes(timestamp, pair, address, sigs_required, healthy)

mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```
