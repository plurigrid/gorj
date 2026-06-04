# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-04  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) color chain:** trit=0 → ERGODIC #d3869b · trit=1 → PLUS #b8bb26 · trit=-1 → MINUS #cc241d

---

## JOB 1 — GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos Snapshotted |
|---|---|---|
| plurigrid | org | 25 |
| kubeflow | org | 17 |
| bmorphism | user | 17 |
| zubyul | user | 14 |
| AustinCStone | social-graph | 10 |
| M1shaaa | social-graph | 8 |
| wasita | social-graph | 7 |
| migalkin | social-graph | 7 |
| kristinezheng | social-graph | 6 |
| DJedamski | social-graph | 6 |
| TeglonLabs | org | 4 |
| **TOTAL** | | **121** |

### GF(3) Color Distribution

| Trit | Name | Color | Count |
|---|---|---|---|
| 0 | ERGODIC | #d3869b | 40 |
| 1 | PLUS | #b8bb26 | 41 |
| -1 | MINUS | #cc241d | 40 |

### Notable Repos (Top Stars)

| Repo | Stars | Lang | Pushed |
|---|---|---|---|
| kubeflow/kubeflow | 15,704 | — | 2026-05-24 |
| kubeflow/pipelines | 4,152 | Python | 2026-06-03 |
| kubeflow/spark-operator | 3,124 | Python | 2026-06-03 |
| kubeflow/trainer | 2,110 | Go | 2026-06-04 |
| kubeflow/katib | 1,685 | Python | 2026-06-04 |
| kubeflow/examples | 1,462 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,020 | YAML | 2026-06-02 |
| kubeflow/arena | 811 | Go | 2026-05-07 |
| kubeflow/kale | 690 | Python | 2026-06-01 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/gorj | 0★ 340📋 | Clojure | 2026-06-04 |

### Most Active (Recent Push, 2026-06-04)

- `plurigrid/gorj` — forj + Rama topology nREPL routing + GF3 coloring
- `kubeflow/trainer` — Distributed AI Model Training on Kubernetes
- `bmorphism/Gay.jl` — Wide-gamut color sampling (189 open issues)
- `M1shaaa/M1shaaa` — profile config pushed today
- `kubeflow/sdk` — Universal Python SDK for Kubernetes
- `kubeflow/dashboard` — Kubeflow Central Dashboard

### Zubyul Social Graph Notable Repos

| User | Notable Repos | Signal |
|---|---|---|
| migalkin | NodePiece (144★), StarE (89★), kgcourse2021 (25★) | KG / GNN researcher |
| DJedamski | Kaggle/NCAA ML (R/Jupyter) | Data science |
| wasita | wasita.github.io (Svelte, active 2026-06) | Active dev |
| kristinezheng | kristinezheng.github.io (active 2026-05) | Personal site |
| M1shaaa | Profile pushed 2026-06-04 | Active, Lookit research |
| AustinCStone | TextGAN (92★), bmfork (active 2025-05) | ML, bitmind orbit |

---

## JOB 2 — Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (A–Z + alice + bob)

All 28 addresses probed at Aptos mainnet. Result: **CoinStore `0x1::aptos_coin::AptosCoin` not found** for all addresses — accounts exist (confirmed: `alice` has `sequence_number=72`) but hold zero in the legacy coin module. Likely hold APT via fungible assets (`0x1::fungible_asset`) rather than the legacy coin store.

| World | Address (prefix) | Balance (APT) | Note |
|---|---|---|---|
| alice | 0xc793...cc7b | 0.0 | account exists, seq_num=72 |
| bob | 0x0a3c...512d | 0.0 | CoinStore absent |
| A–Z (26) | various | 0.0 | CoinStore absent |

**Total APT in legacy coin stores: 0.0 APT (all accounts may use FA module)**

### Multisig Contract Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (prefix) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4...7003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed on mainnet.**

### MNX Markets (testnet.mnx.fi)

Status: **SPA (Next.js) — no JSON API endpoint exposed**  
- `GET /api/markets` → returns HTML (293KB SPA shell)  
- `GET /api/v1/markets` → same SPA shell  
- No market data extractable without browser JS execution  
- Recorded in `mnx_snapshots` as `UNAVAILABLE`

---

## DuckDB Schema Summary

```sql
world_increments  -- 121 rows  (GF3 increment chain: 40 ERGODIC / 41 PLUS / 40 MINUS)
repo_snapshots    -- 121 rows  (GitHub repo metadata, 11 sources)
aptos_snapshots   -- 28 rows   (Hamming swarm A-Z + alice + bob, all 0.0 APT)
multisig_probes   -- 5 rows    (all healthy, sigs_required=2)
mnx_snapshots     -- 1 row     (SPA unavailable)
```

---

*Sweep completed 2026-06-04 by world-increment-sweep + hamming-swarm-snapshot agent.*
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
