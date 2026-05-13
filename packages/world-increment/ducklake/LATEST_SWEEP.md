# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-05-13
**Branch:** world-increment/sweep
**GF(3) color chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Repos | Stars | Top Language |
|--------|-------|-------|-------------|
| plurigrid | 100 | 72 | Clojure / Rust / Zig |
| kubeflow | 48 | 34,045 | Go / Python |
| bmorphism | 100 | 248 | Rust / JavaScript / Julia |
| zubyul | 49 | 14 | Python / Rust |
| AustinCStone | 40 | 108 | Python |
| migalkin | 19 | 279 | Python (KG research) |
| wasita | 11 | 4 | Svelte |
| M1shaaa | 8 | 0 | TypeScript |
| kristinezheng | 6 | 0 | Python |
| DJedamski | 6 | 3 | R / Jupyter |
| TeglonLabs | 4 | 2 | Ruby / JavaScript |
| **TOTAL** | **391** | **34,775** | |

### Top Repos by Stars

| Rank | Repo | Stars |
|------|------|-------|
| 1 | kubeflow/kubeflow | ★15,628 |
| 2 | kubeflow/pipelines | ★4,140 |
| 3 | kubeflow/spark-operator | ★3,126 |
| 4 | kubeflow/trainer | ★2,098 |
| 5 | kubeflow/katib | ★1,682 |
| 6 | kubeflow/examples | ★1,462 |
| 7 | kubeflow/manifests | ★1,017 |
| 8 | kubeflow/arena | ★810 |
| 9 | kubeflow/kale | ★686 |
| 10 | kubeflow/mpi-operator | ★526 |

### Notable Highlights

- **plurigrid/gorj** (this repo): Clojure, 171 open issues, pushed 2026-05-13 — active development today
- **plurigrid/asi**: 21 stars — "everything is topological chemputer!"
- **bmorphism/Gay.jl**: Julia, 188 open issues, active today — wide-gamut color sampling with splittable determinism
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **bmorphism/anti-bullshit-mcp-server**: 23 stars — multi-epistemic claim analysis
- **migalkin/NodePiece**: 144 stars — ICLR'22 KG representation paper
- **TeglonLabs/mathpix-gem**: Ruby gem for mathematical OCR, active through Jan 2026

### GF(3) Trit Distribution (391 world increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 130 |
| 1 | #b8bb26 | PLUS | 131 |
| -1 | #cc241d | MINUS | 130 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 addresses (alice, bob, A–Z) were queried against `fullnode.mainnet.aptoslabs.com`.
All addresses returned **0.0 APT** — no active CoinStore balances detected.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z (26) | various | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.
All are **HEALTHY** — each requires exactly **2 signatures**.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | 0x0da4...003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c...096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ff...883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c...883 | 2 | ✅ HEALTHY |
| V-W | 0x40fa...b6d | 2 | ✅ HEALTHY |

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA (client-side rendered). Public REST API endpoints
(`/api/markets`, `/api/v1/markets`, `/api/tickers`) returned HTML rather than JSON.
**Market data: unavailable from server-side probe.** No entries in `mnx_snapshots`.

---

## DuckDB Schema

Database: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 391 |
| repo_snapshots | 391 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA, no public API) |
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
