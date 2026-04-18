# World Increment Sweep + Hamming Snapshot — 2026-04-18

**Sweep Date:** 2026-04-18  
**DuckDB:** `/home/user/gorj/packages/world-increment/ducklake/sweep.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repos Found Per Org/User

| Entity | Type | Repos Found | Notes |
|--------|------|-------------|-------|
| plurigrid | org | 100 (capped at 100) | Active: gorj(225 issues), nanoclj-zig, asi(17 stars), ontology(7 stars) |
| kubeflow | org | 47 | Active: kubeflow(15583 stars), pipelines(4121 stars), spark-operator(3117 stars) |
| TeglonLabs | org | 4 | mathpix-gem(2 stars), topoi, monad-mcp-server, coin-flip-mcp |
| bmorphism | user | 100 (capped) | ocaml-mcp-sdk(60 stars), anti-bullshit-mcp-server(23 stars), say-mcp-server(20 stars) |
| zubyul | user | 47 | gay-world(1 star), WGCNA(2 stars), nash-tui, plurigrid-site |
| migalkin | user | 19 | NodePiece(143 stars), StarE(89 stars), kgcourse2021(25 stars) |
| DJedamski | user | 6 | Getting-and-Cleaning-Data(1 star), School(1 star), kaggle_ncaa18 |
| wasita | user | 10 | magic-garden(1 star), wins-search(1 star), wasita.github.io(active) |
| kristinezheng | user | 6 | Portfolio, lookit-jenga, kristinezheng.github.io(active 2026) |
| M1shaaa | user | 8 | lab-bookshelf-, M1shaaa profile(active 2026-04-18) |
| AustinCStone | user | 40 | TextGAN(92 stars), StereoVisionMRF(11 stars), SpectralClustering(3 stars) |

**Total GitHub repos indexed (DuckDB):** 60 representative repos (curated from full sweep)

### Notable Active Repos (pushed 2026)
- `plurigrid/gorj` - Clojure, 225 open issues, pushed 2026-04-18 (TODAY)
- `plurigrid/nanoclj-zig` - Zig Clojure interpreter with GF(3) trit conservation, 21 issues
- `plurigrid/asi` - HTML, 17 stars, pushed 2026-04-13
- `plurigrid/horse` - TeX, 10 open issues, pushed 2026-04-16
- `kubeflow/pipelines` - Python, 4121 stars, 476 open issues, active daily
- `bmorphism/Gay.jl` - Julia, 187 open issues, pushed 2026-04-18 (TODAY)
- `M1shaaa/M1shaaa` - profile repo pushed 2026-04-18 (TODAY)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 wallets queried via `fullnode.mainnet.aptoslabs.com`. All returned **0 APT** — the `CoinStore<AptosCoin>` resource was not found/unfunded for each address at time of sweep.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...c7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A through Z | (26 addresses) | 0.0 each |

**Sum total:** 0.0 APT across all 28 wallets.

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`. All returned **2 signatures required** and are considered **HEALTHY**.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | YES |
| A-G | 0xf56c...096 | 2 | YES |
| Y-Z | 0xd3ff...883 | 2 | YES |
| S-T | 0x3b1c...883 | 2 | YES |
| V-W | 0x40fa...b6d | 2 | YES |

**All multisigs healthy (5/5), all require 2-of-N signatures.**

### MNX Market Data

**Status: UNAVAILABLE**  
Both `https://testnet.mnx.fi/api/markets` and `https://testnet.mnx.fi/api/tickers` returned no JSON response (connection failed or server down). No market data recorded.

---

## GF(3) Color Chain Statistics

Applied to 60 world increment records:

| GF(3) Name | Trit | Color | Count |
|------------|------|-------|-------|
| ERGODIC | 0 | #d3869b (pink) | 20 |
| PLUS | 1 | #b8bb26 (yellow-green) | 20 |
| MINUS | 2 | #cc241d (red) | 20 |

**Perfect balance:** 20 increments per trit class (60 total, 3-way balanced).

---

## DuckDB Table Summary

| Table | Rows |
|-------|------|
| world_increments | 60 |
| repo_snapshots | 60 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

---

## Sweep Metadata
- **Date:** 2026-04-18
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
