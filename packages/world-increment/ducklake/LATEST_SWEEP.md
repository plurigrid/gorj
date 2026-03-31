# World-Increment Sweep — 2026-03-31 (Full Social Graph + Hamming Snapshot)

## Sweep Metadata
- **Date:** 2026-03-31
- **Agent:** world-increment-sweep (full social graph + hamming)
- **DuckDB version:** v1.2.x
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 371 |
| Total Repo Snapshots | 371 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain

371 world-increments assigned via GF(3) modular color chain:
- `id % 3 == 0` → trit=0, ERGODIC, #d3869b (124 rows)
- `id % 3 == 1` → trit=1, PLUS, #b8bb26 (124 rows)
- `id % 3 == 2` → trit=-1, MINUS, #cc241d (123 rows)

---

## Top 10 Repos by Stars

| full_name | stars | language |
|-----------|-------|----------|
| kubeflow/kubeflow | 15547 | Jupyter Notebook |
| kubeflow/pipelines | 4114 | Python |
| kubeflow/spark-operator | 3110 | Go |
| kubeflow/trainer | 2070 | Go |
| kubeflow/katib | 1673 | Go |
| kubeflow/website | 473 | HTML |
| kubeflow/manifests | 464 | Jsonnet |
| kubeflow/model-registry | 383 | Go |
| kubeflow/notebooks | 369 | Python |
| kubeflow/kfp-tekton | 299 | Python |

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 93 |
| kubeflow | org | 46 |
| TeglonLabs | org | 3 |
| bmorphism | user | 100 |
| zubyul | user | 46 |
| migalkin | user | 20 |
| DJedamski | user | 6 |
| wasita | user | 9 |
| kristinezheng | user | 6 |
| M1shaaa | user | 8 |
| AustinCStone | user | 40 |
| **TOTAL** | | **371** |

---

## Aptos Hamming Snapshot

All 28 wallets probed on Aptos mainnet. All balances returned 0.0 APT.

| world | address (short) | balance APT |
|-------|----------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...c9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...c3 | 0.0 |
| W | 0x5f32...b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

---

## Multisig Probes

All 5 pairs healthy, all require 2 signatures.

| pair | address (short) | sigs_required | healthy |
|------|----------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | true |
| A-G | 0xf56c...096 | 2 | true |
| Y-Z | 0xd3ff...883 | 2 | true |
| S-T | 0x3b1c...883 | 2 | true |
| V-W | 0x40fa...b6d | 2 | true |

---

## MNX Markets

**Status:** unavailable — `https://testnet.mnx.fi/api/markets` returns HTML (SPA 404), no structured JSON market data accessible.

---

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/pipelines**: 4,112 stars — most popular ML pipeline for Kubernetes (pushed 2026-03-28)
- **kubeflow/spark-operator**: 3,110 stars — Kubernetes operator for Apache Spark
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect
- **plurigrid/asi**: 13 stars — topological chemputer (pushed 2026-03-28)
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
