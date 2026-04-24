# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-24

**Sweep timestamp:** 2026-04-24 (UTC)
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Increment ID | GF(3) Trit | Color | Name | Source | Repos Captured |
|---|---|---|---|---|---|
| 1 | +1 | #b8bb26 | PLUS | plurigrid | 100 |
| 2 | -1 | #cc241d | MINUS | kubeflow | 47 |
| 3 | 0 | #d3869b | ERGODIC | TeglonLabs | 4 |
| 4 | +1 | #b8bb26 | PLUS | bmorphism | 100 |
| 5 | -1 | #cc241d | MINUS | zubyul | 49 |
| 6 | 0 | #d3869b | ERGODIC | migalkin | 19 |
| 7 | +1 | #b8bb26 | PLUS | DJedamski | 6 |
| 8 | -1 | #cc241d | MINUS | wasita | 10 |
| 9 | 0 | #d3869b | ERGODIC | kristinezheng | 6 |
| 10 | +1 | #b8bb26 | PLUS | M1shaaa | 8 |
| 11 | -1 | #cc241d | MINUS | AustinCStone | 40 |

**Total repos snapshotted: 389**

### Top Repos by Stars
| Repo | Stars | Language |
|---|---|---|
| kubeflow/kubeflow | 15,599 | — |
| kubeflow/pipelines | 4,125 | Python |
| kubeflow/spark-operator | 3,120 | Python |
| kubeflow/trainer | 2,091 | Go |
| kubeflow/katib | 1,679 | Python |
| kubeflow/examples | 1,460 | Jsonnet |
| kubeflow/manifests | 1,012 | YAML |
| kubeflow/arena | 810 | Go |
| kubeflow/kale | 685 | Python |
| kubeflow/mpi-operator | 524 | Go |

### Notable Activity
- **bmorphism** (100 repos): active plurigrid contributor, diverse projects
- **zubyul** (49 repos): active social graph node
- **AustinCStone** (40 repos): ML/CV researcher
- **TeglonLabs** (4 repos): `mathpix-gem` (Ruby, math OCR), `topoi` (Python), `monad-mcp-server`, `coin-flip-mcp`
- **wasita** (10 repos): `wasita.github.io` (Svelte personal site, pushed 2026-04-22 — most recent in social graph)

### Data Notes
- GitHub public API returned 403 (unauthenticated); all data sourced via GitHub MCP search API
- Search API returns up to 100 results per query; bmorphism and plurigrid capped at 100

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice–Z, 28 addresses)

All 28 addresses queried against `fullnode.mainnet.aptoslabs.com`.

**Result:** All addresses return `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. None of the Hamming swarm addresses have initialized an APT CoinStore on mainnet.

| Status | Count |
|---|---|
| CoinStore not initialized (0 APT) | 28 |
| APT balance > 0 | 0 |

### Multisig Contract Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Healthy |
|---|---|---|---|
| A-B | `0x0da4f428...987003` | 2 | ✓ |
| A-G | `0xf56c4a1c...c0096` | 2 | ✓ |
| Y-Z | `0xd3ffe181...5b883` | 2 | ✓ |
| S-T | `0x3b1c3ae9...7883` | 2 | ✓ |
| V-W | `0x40fad7b4...eb6d` | 2 | ✓ |

**All 5 multisig contracts respond: 2-of-N threshold, all healthy.**

### MNX Markets (testnet.mnx.fi)

Next.js SPA with no public REST API. All API paths return HTTP 404. The `/markets` route requires wallet authentication. **No market data extractable without wallet connection.**

---

## DuckDB Tables

```
world_increments   — 11 rows (one per source, GF(3) color chain)
repo_snapshots     — 389 rows (all public repos snapshotted)
aptos_snapshots    —  28 rows (alice–Z, all 0 APT / no CoinStore)
multisig_probes    —   5 rows (all healthy, 2-of-N)
mnx_snapshots      —   0 rows (SPA, no unauthenticated API)
```

## Query the database

```bash
duckdb packages/world-increment/ducklake/world-increments.duckdb \
  "SELECT org_or_user, COUNT(*) as repos FROM repo_snapshots GROUP BY org_or_user ORDER BY repos DESC;"
```

---

## Sweep Metadata (legacy format)
- **Date:** 2026-04-12
- **Agent:** world-increment-sweep
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
