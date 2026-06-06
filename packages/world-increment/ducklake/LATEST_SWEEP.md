# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-06

## Sweep Metadata
- **Date:** 2026-06-06
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 87 (cumulative) |
| Total Repo Snapshots | 1008 (cumulative) |
| This Sweep Added | 64 new increments |
| Sources Covered | 3 orgs + 8 users + social graph |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts | 5 (all healthy, 2-of-N) |
| MNX Markets | unavailable (Vercel auth required) |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain (latest 64 increments, ids 1–64)

GF(3) rule: `id%3==0 → ERGODIC #d3869b | id%3==1 → PLUS #b8bb26 | id%3==2 → MINUS #cc241d`

| Trit | Name | Hex | Count |
|------|------|-----|-------|
| 0 | ERGODIC | #d3869b | 22 |
| +1 | PLUS | #b8bb26 | 21 |
| -1 | MINUS | #cc241d | 21 |

### Repo Activity by Source (2026-06-06 sweep)

| Source | Type | Repos Indexed | Top Repo (Stars) |
|--------|------|---------------|-----------------|
| plurigrid | org | 211 cumul. | `asi` (25★) |
| bmorphism | user | 209 cumul. | `ocaml-mcp-sdk` (61★) |
| kubeflow | org | 112 cumul. | `kubeflow` (15,706★) |
| TeglonLabs | org | 110 cumul. | `mathpix-gem` (2★) |
| AustinCStone | user | 89 cumul. | `TextGAN` (92★) |
| migalkin | user | 64 cumul. | `NodePiece` (144★) |
| wasita | user | 63 cumul. | `magic-garden` (2★) |
| zubyul | user | 54 cumul. | `jonikas_lab_data_analysis_misc` (2★) |
| kristinezheng | user | 38 cumul. | — |
| M1shaaa | user | 34 cumul. | — |
| DJedamski | user | 24 cumul. | `School` (1★) |

### Hot Repos (pushed 2026-06-06)
- **plurigrid/gorj** — 394 open issues; Clojure; forj+Rama+GF(3) REPL
- **kubeflow/pipelines** — 4,152★ Python ML pipelines
- **kubeflow/notebooks** — interactive dev environments on Kubernetes
- **bmorphism/Gay.jl** — Julia wide-gamut color sampling, 189 open issues

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 worlds)

All 28 addresses queried against `fullnode.mainnet.aptoslabs.com`. The CoinStore resource was not found for any address (addresses may be unfunded, or the resource path is unavailable from this execution container).

| World | Address | Balance |
|-------|---------|---------|
| alice | 0xc793...cc7b | NULL |
| bob | 0x0a3c...2d5d | NULL |
| A–Z | 0x8699...–0x7af0... | NULL ×26 |

### Multisig Probes — 5/5 Healthy ✓

All five multisig contracts respond with `num_signatures_required = 2`:

| Pair | Contract Address | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4...7003 | **2** | ✓ HEALTHY |
| A-G | 0xf56c...0096 | **2** | ✓ HEALTHY |
| Y-Z | 0xd3ff...b883 | **2** | ✓ HEALTHY |
| S-T | 0x3b1c...7883 | **2** | ✓ HEALTHY |
| V-W | 0x40fa...eb6d | **2** | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)
**Unavailable** — all API endpoints (`/api/markets`, `/api/v1/markets`, `/api/tickers`) return Vercel authentication gate. `mnx_snapshots` table: 0 rows.

---

## GF(3) Color Chain — Selected Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| ... | ... | ... | ... | ... | ... |
| 63 | M1shaaa | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 64 | DJedamski | repo_snapshot | +1 | `#b8bb26` | **PLUS** |

GF(3) chain continues: `PLUS→MINUS→ERGODIC→PLUS→MINUS→ERGODIC→...`

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
