# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-14

## Sweep Metadata
- **Date:** 2026-04-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 40 |
| Repo Snapshots | 35 |
| Events Captured | 5 (zubyul; bmorphism rate-limited) |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (SPA) |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Distribution

| GF3 Name | Color | Trit | Count |
|----------|-------|------|-------|
| ERGODIC | `#d3869b` | 0 | 13 |
| PLUS | `#b8bb26` | +1 | 14 |
| MINUS | `#cc241d` | -1 | 13 |

GF(3) chain: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ...`

### Sources Queried

| Source | Type | Sample Repos |
|--------|------|--------------|
| plurigrid | org | gorj, nash-portal, asi, nanoclj-zig, zig-syrup |
| kubeflow | org | kubeflow, pipelines, trainer, spark-operator, katib |
| TeglonLabs | org | Stahl, mathpix-gem, vibespace, topOS |
| bmorphism | user | boxxy, postweb, ocaml-mcp-sdk, shitcoin |
| zubyul | user | big-bad-plurigrid-quiz, Gay.jl, gay-world |
| migalkin | social | kgcourse2021 |
| wasita | social | wasita.github.io |
| M1shaaa | social | M1shaaa profile |
| AustinCStone | social | EpsteinSearch |
| kristinezheng | social | kristinezheng.github.io |
| DJedamski | social | kaggle_ncaa18 |

### Top Repos by Stars

```
15,572  kubeflow/kubeflow           — Machine Learning Toolkit for Kubernetes
 4,119  kubeflow/pipelines          — ML Pipelines for Kubeflow
 3,114  kubeflow/spark-operator     — K8s operator for Apache Spark
 2,082  kubeflow/trainer            — Distributed AI Model Training on K8s
 1,678  kubeflow/katib              — Automated ML on Kubernetes
   150  kubeflow/mcp-apache-spark   — MCP Server for Spark History Server
    60  bmorphism/ocaml-mcp-sdk     — OCaml SDK for MCP (Jane Street oxcaml_effect)
    25  migalkin/kgcourse2021       — Knowledge Graphs course materials
    23  bmorphism/anti-bullshit-mcp — MCP server for claim analysis & manipulation detection
    16  plurigrid/asi               — everything is topological chemputer!
```

### Recent zubyul Events (2026-04-14)

```
01:57:46Z  PullRequestEvent  plurigrid/gorj
01:57:32Z  CreateEvent       plurigrid/gorj
01:49:55Z  PushEvent         plurigrid/gorj
01:07:44Z  PullRequestEvent  plurigrid/gorj
Apr13 23:53  PushEvent       plurigrid/nash-portal
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Balances

Queried via `0x1::coin::balance` view function with FA fallback.

| World | APT Balance |
|-------|-------------|
| bob | 12.6570 |
| F | 1.9605 |
| L | 1.9273 |
| J | 1.8951 |
| alice | 0.4364 |
| O | 0.2101 |
| K | 0.1620 |
| P | 0.1401 |
| S | 0.0918 |
| M | 0.1123 |
| N | 0.1061 |
| Q | 0.1032 |
| R | 0.0902 |
| T | 0.0737 |
| A | 0.0518 |
| U | 0.0558 |
| B | 0.0363 |
| X | 0.0426 |
| Y | 0.0444 |
| V | 0.0488 |
| W | 0.0407 |
| Z | 0.0243 |
| C | 0.0102 |
| D | 0.0116 |
| E | 0.0094 |
| H | 0.0017 |
| G | 0.0007 |
| I | 0.0007 |

**Total swarm APT:** ~21.00 APT  
**Richest node:** bob (12.657 APT, ~60% of swarm total)

### Multisig Contract Probes

All queried via `0x1::multisig_account::num_signatures_required`.

| Pair | Sigs Required | Healthy |
|------|---------------|---------|
| A-B (`0x0da4f428...`) | 2 | ✓ |
| A-G (`0xf56c4a1c...`) | 2 | ✓ |
| Y-Z (`0xd3ffe181...`) | 2 | ✓ |
| S-T (`0x3b1c3ae9...`) | 2 | ✓ |
| V-W (`0x40fad7b4...`) | 2 | ✓ |

All 5 multisig contracts are 2-of-N, all healthy.

### MNX Markets

`https://testnet.mnx.fi` — **SPA only**: Next.js app, no public JSON API. Recorded as `unavailable` in `mnx_snapshots` table.

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
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
