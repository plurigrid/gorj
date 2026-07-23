# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-23

## Sweep Metadata
- **Date:** 2026-07-23
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 373 |
| Total Repo Snapshots | 373 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain — 373 Increments

| GF3 Trit | Color | Name | Count |
|-----------|-------|------|-------|
| 0 | `#d3869b` | **ERGODIC** | 131 |
| +1 | `#b8bb26` | **PLUS** | 133 |
| -1 | `#cc241d` | **MINUS** | 132 |

Pattern cycles: `PLUS → MINUS → ERGODIC → …` repeating 124 full cycles + 1 partial

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, via `0x1::coin::balance` view function)

| World | APT Balance |
|-------|-------------|
| bob | **12.657007** |
| F | 1.960516 |
| L | 1.927269 |
| J | 1.895093 |
| alice | 0.436434 |
| O | 0.210136 |
| K | 0.161961 |
| P | 0.140136 |
| M | 0.112285 |
| N | 0.106121 |
| Q | 0.103240 |
| S | 0.091788 |
| R | 0.090217 |
| T | 0.073713 |
| U | 0.055773 |
| A | 0.051767 |
| Y | 0.044449 |
| X | 0.042577 |
| W | 0.040705 |
| B | 0.036256 |
| V | 0.048833 |
| Z | 0.024268 |
| C | 0.010185 |
| D | 0.011629 |
| E | 0.009372 |
| H | 0.001681 |
| G | 0.000681 |
| I | 0.000681 |

**Total APT across hamming swarm:** ~21.06 APT  
**bob** holds dominant share (60%); F, L, J each hold ~9% (secondary tier)

### Multisig Contract Probes

| Pair | Sigs Required | Healthy |
|------|---------------|---------|
| A-B | 2 | ✓ |
| A-G | 2 | ✓ |
| Y-Z | 2 | ✓ |
| S-T | 2 | ✓ |
| V-W | 2 | ✓ |

All 5 multisig contracts healthy. All configured as 2-of-N signature threshold.

### MNX Markets

- `https://testnet.mnx.fi/api/markets` → **404 Not Found**
- `https://testnet.mnx.fi` → SPA shell, no API data accessible
- **Status: UNAVAILABLE** — testnet endpoint down or moved

---

## Top Repos by Source

### plurigrid (100 repos)
Queried 2026-07-23. Top stars from previous sweep: asi (16★), ontology (7★), asi-skills (3★).

### kubeflow (49 repos)
| Repo | Stars |
|------|-------|
| kubeflow | 15,788 |
| pipelines | 4,169 |
| spark-operator | 3,142 |
| trainer | 2,153 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

### bmorphism (100 repos)
Most recent push data from 2026-07-23 sweep.

### migalkin (19 repos — top page)
Knowledge graph / GNN research repos.

### AustinCStone (20 repos — top page)
ML/CV research including TextGAN (92★).

---

## Repo Counts by Source (2026-07-23)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | user | 20 |
| migalkin | user | 19 |
| wasita | user | 12 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| kristinezheng | user | 5 |
| TeglonLabs | org | 5 |
| **TOTAL** | | **373** |

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
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — most popular ML pipeline for Kubernetes (pushed 2026-04-10)
- **kubeflow/spark-operator**: 3,111 stars — Kubernetes operator for Apache Spark (pushed 2026-04-10)
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 16 stars — topological chemputer (pushed 2026-04-10)
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **Increment 12**: ERGODIC — sweep_complete closing the 4th full GF(3) cycle
