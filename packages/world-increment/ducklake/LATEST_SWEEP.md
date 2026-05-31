# World-Increment Sweep + Hamming Swarm Snapshot
**Timestamp:** 2026-04-28  
**GF(3) Color Chain:** trit=0 ERGODIC #d3869b · trit=1 PLUS #b8bb26 · trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured | Total Stars | Total Forks |
|--------|------|---------------|-------------|-------------|
| plurigrid | org | 100 | 65 | 42 |
| kubeflow | org | 47 | 33,957 | 13,383 |
| TeglonLabs | org | 4 | 2 | 2 |
| bmorphism | user | 100 | 246 | 73 |
| zubyul | user | 49 | 14 | 2 |
| migalkin | user (social graph) | 19 | 278 | 49 |
| DJedamski | user (social graph) | 6 | 3 | 1 |
| wasita | user (social graph) | 10 | 4 | 1 |
| AustinCStone | user (social graph) | 30 | 108 | 38 |
| **TOTAL** | | **365** | **34,677** | **13,591** |

> kristinezheng and M1shaaa returned 0 public repos. GitHub API rate-limit exhausted; MCP GitHub search tools used.

### Top 10 Most-Starred Repos
| Repo | Stars |
|------|-------|
| kubeflow/kubeflow | 15,609 |
| kubeflow/pipelines | 4,127 |
| kubeflow/spark-operator | 3,120 |
| kubeflow/trainer | 2,094 |
| kubeflow/katib | 1,681 |
| kubeflow/examples | 1,460 |
| kubeflow/manifests | 1,012 |
| kubeflow/arena | 810 |
| kubeflow/kale | 685 |
| kubeflow/mpi-operator | 524 |

### Top Languages Across Swarm
| Language | Repos |
|----------|-------|
| Python | 75 |
| Rust | 26 |
| JavaScript | 23 |
| TypeScript | 22 |
| Go | 15 |
| Clojure | 13 |
| Jupyter Notebook | 13 |
| HTML | 13 |
| Julia | 9 |
| Zig | 7 |

### Recently Active plurigrid Repos (top 5 by pushed_at)
- `plurigrid/gorj` (Clojure) — pushed 2026-04-28 — "forj + Rama topology nREPL routing + GF(3) gay trit coloring"
- `plurigrid/zig-syrup` (Zig) — pushed 2026-04-26 — "High-performance Zig OCapN Syrup implementation"
- `plurigrid/horse` (TeX) — pushed 2026-04-26
- `plurigrid/asi` (HTML) — pushed 2026-04-26 — "everything is topological chemputer!"
- `plurigrid/nash-portal` (Rust) — pushed 2026-04-26 — "NASH token TUI in the browser"

### GF(3) World-Increment Distribution
| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 121 |
| +1 | PLUS | #b8bb26 | 122 |
| -1 | MINUS | #cc241d | 122 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
**Timestamp:** 2026-04-28

All 28 wallets probed via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource.

| World | Address (truncated) | Balance (APT) | Status |
|-------|--------------------|----|--------|
| alice | 0xc793...cc7b | 0.0 | No CoinStore |
| bob | 0x0a3c...512d | 0.0 | No CoinStore |
| A | 0x8699...9d7a | 0.0 | No CoinStore |
| B | 0x3f89...b13 | 0.0 | No CoinStore |
| C | 0x38b9...35e | 0.0 | No CoinStore |
| D | 0xf776...dd1 | 0.0 | No CoinStore |
| E–Z | (24 addresses) | 0.0 each | No CoinStore |

> All 28 addresses returned empty for CoinStore resource — wallets not yet initialized APT coin storage. Total swarm balance: **0.0 APT**.

### Multisig Contract Probes (Mainnet)
| Pair | Address (truncated) | Sigs Required | Status |
|------|--------------------|----|--------|
| A-B | 0x0da4...003 | 2 | ✓ Healthy |
| A-G | 0xf56c...096 | 2 | ✓ Healthy |
| Y-Z | 0xd3ff...883 | 2 | ✓ Healthy |
| S-T | 0x3b1c...883 | 2 | ✓ Healthy |
| V-W | 0x40fa...b6d | 2 | ✓ Healthy |

All 5 multisig contracts are **2-of-N** (2 signatures required). All healthy.

### MNX Markets (testnet.mnx.fi)
**Status:** Unavailable — testnet.mnx.fi serves a Next.js SPA with no public REST API. `/api/markets` returns 404. No market data extractable.

---

## DuckDB Schema Summary (`world-increments.duckdb`)
| Table | Rows | Description |
|-------|------|-------------|
| world_increments | 365 | One per repo snapshot, GF(3) trit colored |
| repo_snapshots | 365 | Full repo metadata |
| aptos_snapshots | 28 | All wallets alice/bob/A–Z |
| multisig_probes | 5 | All pairs healthy, sigs_required=2 |
| mnx_snapshots | 1 | Unavailable marker |

**Previous sweep metadata:**
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 12 |
| Total Repo Snapshots | 471 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain — All 12 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 12 | bmorphism (org) | sweep_complete (gorj) | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## Top Repos by Source

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 16 | 2026-04-10 |
| ontology | JavaScript | 7 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-09 |
| zig-syrup | Zig | 2 | 2026-04-09 |
| vivarium | Clojure | 1 | 2026-04-08 |

### kubeflow (47 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15565 | 2026-01-05 |
| pipelines | Python | 4119 | 2026-04-10 |
| spark-operator | Python | 3111 | 2026-04-10 |
| trainer | Go | 2080 | 2026-04-10 |
| katib | Python | 1676 | 2026-04-02 |

### TeglonLabs (53 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| vibespace | HTML | 2 |
| acp.el | — | 1 |
| mcp-terminal | — | 1 |

### bmorphism (100 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 60 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| shitcoin | Python | 5 |
| open-location-code-zig | Zig | 3 |

### migalkin (30 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 143 |
| StarE | Python | 88 |
| kgcourse2021 | HTML | 25 |

### AustinCStone (43 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 47 |
| AustinCStone | user | 43 |
| migalkin | user | 30 |
| wasita | user | 29 |
| zubyul | user | 24 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| **TOTAL** | | **471** |

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
