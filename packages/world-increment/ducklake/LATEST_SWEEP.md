# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-21

**Date:** 2026-07-21  
**Run type:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 30 |
| kubeflow | org | 13 |
| TeglonLabs | org | 5 |
| bmorphism | user | 10 |
| zubyul | user | 6 |
| migalkin | social graph | 4 |
| wasita | social graph | 2 |
| AustinCStone | social graph | 2 |
| DJedamski | social graph | 1 |
| kristinezheng | social graph | 1 |
| M1shaaa | social graph | 1 |
| **Total** | | **75** |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 25 |
| 1 | `#b8bb26` | PLUS | 25 |
| 2 | `#cc241d` | MINUS | 25 |

Perfectly balanced across 75 increments (id%3 cycling).

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,786 | — |
| kubeflow/pipelines | 4,169 | Python |
| kubeflow/spark-operator | 3,140 | Python |
| kubeflow/trainer | 2,152 | Go |
| kubeflow/katib | 1,692 | Python |
| kubeflow/examples | 1,460 | Jsonnet |
| kubeflow/community-distribution | 1,029 | YAML |
| kubeflow/arena | 815 | Go |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| plurigrid/asi | 31 | HTML |

### Most Recently Pushed

| Repo | Pushed At |
|------|-----------|
| plurigrid/gorj | 2026-07-21T01:12:44Z |
| kubeflow/katib | 2026-07-20T22:47:05Z |
| kubeflow/kubeflow | 2026-07-20T22:08:12Z |
| wasita/wasita.github.io | 2026-07-20T18:18:51Z |
| bmorphism/Gay.jl | 2026-07-20T09:41:37Z |

### Notable Activity

- **plurigrid/gorj** (pushed today) — forj + Rama topology nREPL routing + GF(3) gay trit coloring — 1,286 open issues
- **bmorphism/Gay.jl** (187 open issues, pushed today) — Wide-gamut color sampling with splittable determinism
- **migalkin/NodePiece** (144★) — Compositional and Parameter-Efficient Representations for Large Knowledge Graphs (ICLR'22)
- **bmorphism/ocaml-mcp-sdk** (61★) — OCaml SDK for MCP using Jane Street oxcaml_effect
- **kubeflow/mcp-apache-spark-history-server** (183★, new 2025-06-26) — MCP Server for Apache Spark
- Active ecosystem in: Gay.jl/GF(3) colors, OCaml/OxCaml MCP, Zig toolchain (nanoclj-zig, zig-syrup), kubeflow SDK

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (A-Z + alice/bob)

**Result:** All 28 wallets queried. No `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource found.
Accounts exist on-chain (confirmed sequence numbers) but use Fungible Asset standard — zero APT via legacy CoinStore API.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793... | null (no CoinStore) |
| bob | 0x0a3c... | null |
| A–Z | 0x8699...–0x7af0... | null (26 wallets) |

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4... | 2 | ✅ |
| A-G | 0xf56c... | 2 | ✅ |
| Y-Z | 0xd3ff... | 2 | ✅ |
| S-T | 0x3b1c... | 2 | ✅ |
| V-W | 0x40fa... | 2 | ✅ |

**5/5 healthy** — all require 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

**Status:** UNAVAILABLE — Vercel authentication required (HTTP 401 on all API paths).

---

## DuckDB Schema Populated

- `world_increments` — 75 rows (GF3-colored repo push events)
- `repo_snapshots` — 75 rows (stars, forks, languages, descriptions)
- `aptos_snapshots` — 28 rows (all balance=NULL, no CoinStore)
- `multisig_probes` — 5 rows (all healthy, sigs_required=2)
- `mnx_snapshots` — 1 row (unavailable placeholder)

---

*Previous sweep content archived below.*

## Sweep Metadata (2026-04-12)
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
