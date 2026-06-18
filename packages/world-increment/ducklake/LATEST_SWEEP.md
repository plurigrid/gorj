# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-18

**Sweep date:** 2026-06-18  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain
| id%3 | Trit | Color | Name |
|------|------|-------|------|
| 0 | 0 | `#d3869b` | ERGODIC |
| 1 | +1 | `#b8bb26` | PLUS |
| 2 | -1 | `#cc241d` | MINUS |

### Sources Swept (11 World Increments)

| id | GF3 | Source | Type | Repos |
|----|-----|--------|------|-------|
| 1 | PLUS #b8bb26 | plurigrid | org | 100+ (20 sampled) |
| 2 | MINUS #cc241d | kubeflow | org | 48 (20 sampled) |
| 3 | ERGODIC #d3869b | TeglonLabs | org | 5 |
| 4 | PLUS #b8bb26 | bmorphism | user | 100 (10 sampled) |
| 5 | MINUS #cc241d | zubyul | user | 49 (9 sampled) |
| 6 | ERGODIC #d3869b | migalkin | user | 19 (6 sampled) |
| 7 | PLUS #b8bb26 | DJedamski | user | 6 |
| 8 | MINUS #cc241d | kristinezheng | user | 5 |
| 9 | ERGODIC #d3869b | M1shaaa | user | 8 |
| 10 | PLUS #b8bb26 | wasita | user | 11 (6 sampled) |
| 11 | MINUS #cc241d | AustinCStone | user | 40 (8 sampled) |

### Notable Repos by Stars

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,734 | — | 2026-06-18 |
| kubeflow/pipelines | 4,154 | Python | 2026-06-18 |
| kubeflow/spark-operator | 3,127 | Python | 2026-06-17 |
| kubeflow/trainer | 2,115 | Go | 2026-06-18 |
| kubeflow/katib | 1,683 | Python | 2026-06-15 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2025-06-01 |
| plurigrid/asi | 26 | HTML | 2026-06-10 |
| migalkin/kgcourse2021 | 25 | HTML | 2025-08-04 |
| bmorphism/say-mcp-server | 20 | JavaScript | 2025-06-01 |
| migalkin/NBFNet_mlx | 10 | Python | 2024-03-02 |
| plurigrid/ontology | 8 | JavaScript | 2025-05-27 |

### Hot Activity (recently pushed today)
- `plurigrid/gorj` — pushed 2026-06-18, **651 open issues** (most active repo in sweep)
- `kubeflow/community`, `kubeflow/pipelines`, `kubeflow/trainer` — all active today
- `M1shaaa/M1shaaa` — pushed 2026-06-18
- `bmorphism/Gay.jl` — pushed 2026-06-18, 187 open issues

### Social Graph Coverage
- **Orgs:** plurigrid, kubeflow, TeglonLabs
- **Primary users:** bmorphism, zubyul
- **Zubyul social graph:** migalkin (KG ML researcher), DJedamski (data science), wasita (network science), kristinezheng (cog sci), M1shaaa (dev psych), AustinCStone (ML/CV)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)

All 28 wallets returned **null** from the Aptos mainnet CoinStore API — no initialized `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource found. Accounts may not have been funded on mainnet or have not initialized their coin store.

**Balance: 0.0 APT** for all wallets (alice, bob, A–Z)

### Multisig Contract Probes

All 5 multisig accounts are **healthy** and respond with `num_signatures_required = 2`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4f4...987003` | 2 | HEALTHY |
| A-G | `0xf56c4a...c0096` | 2 | HEALTHY |
| Y-Z | `0xd3ffe1...b883` | 2 | HEALTHY |
| S-T | `0x3b1c3a...d7883` | 2 | HEALTHY |
| V-W | `0x40fad7...eb6d` | 2 | HEALTHY |

All pairs require 2-of-2 signatures. Swarm multisig infrastructure is operational.

### MNX Markets

`testnet.mnx.fi` is protected by **Vercel authentication** — requires deployment protection bypass token. Market data unavailable in automated sweep context.

---

## DuckDB Schema Summary

```
world_increments:  11 rows  (one per source, GF3 colored)
repo_snapshots:   103 rows  (sampled from 400+ total repos)
aptos_snapshots:   28 rows  (alice, bob, A-Z — all 0.0 APT on mainnet)
multisig_probes:    5 rows  (all healthy, 2-of-2)
mnx_snapshots:      1 row   (unavailable — Vercel auth)
```

---

## Sweep Metadata
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
