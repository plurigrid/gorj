# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-05T00:00Z  
**Branch:** world-increment/sweep-2026-07-05  
**GF(3) color chain:** trit=0 → ERGODIC #d3869b | trit=1 → PLUS #b8bb26 | trit=-1 → MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos |
|---|---|---|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social graph) | 19 |
| DJedamski | user (social graph) | 6 |
| wasita | user (social graph) | 11 |
| kristinezheng | user (social graph) | 5 |
| M1shaaa | user (social graph) | 8 |
| AustinCStone | user (social graph) | 30 |
| **TOTAL** | | **381** |

### Top Repos by Stars

| Org/User | Repo | Stars | Language |
|---|---|---|---|
| kubeflow | kubeflow | 15,761 | - |
| kubeflow | pipelines | 4,169 | Python |
| kubeflow | spark-operator | 3,132 | Python |
| kubeflow | trainer | 2,129 | Go |
| kubeflow | katib | 1,689 | Python |

### Recently Active (TeglonLabs)

| Repo | Language | Pushed | Description |
|---|---|---|---|
| jank-crane | C++ | 2026-06-08 | crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps |
| mathpix-gem | Ruby | 2026-01-01 | LaTeX/SMILES/Markdown OCR SDK |
| coin-flip-mcp | JavaScript | 2025-09-21 | MCP server random.org coin flips |

### DuckDB Tables
- `world_increments`: 381 rows (GF3 trit-colored)
- `repo_snapshots`: 381 rows (stars, forks, issues, pushed_at, language)

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (via `0x1::coin::balance` view function)

| World | Address (prefix) | Balance (APT) |
|---|---|---|
| alice | 0xc793acde... | 0.43643352 |
| bob | 0x0a3c00c5... | 12.65700700 |
| A | 0x8699edc0... | 0.05176700 |
| B | 0x3f892ebe... | 0.03625600 |
| C | 0x38b99e63... | 0.01018500 |
| D | 0xf7765624... | 0.01162900 |
| E | 0xdc1d9d53... | 0.00937200 |
| F | 0x18a14b5b... | 1.96051600 |
| G | 0x69a394c0... | 0.00068100 |
| H | 0xce67c327... | 0.00168100 |
| I | 0x070fe5d7... | 0.00068100 |
| J | 0x4d964db8... | 1.89509300 |
| K | 0xa732040a... | 0.16196100 |
| L | 0x7c2eaeaf... | 1.92726900 |
| M | 0x6fed37a7... | 0.11228500 |
| N | 0xe7dde6da... | 0.10612100 |
| O | 0x73252b60... | 0.21013600 |
| P | 0x62187927... | 0.14013600 |
| Q | 0xac40fa50... | 0.10324000 |
| R | 0x7ce605cc... | 0.09021700 |
| S | 0xb8753014... | 0.09178800 |
| T | 0x35781dc0... | 0.07371300 |
| U | 0x75860da4... | 0.05577300 |
| V | 0xb59dd817... | 0.04883299 |
| W | 0x5f32aef7... | 0.04070500 |
| X | 0xa95cbbd1... | 0.04257700 |
| Y | 0xd8e32848... | 0.04444900 |
| Z | 0x7af0ef6e... | 0.02426800 |

**Total swarm balance:** ~20.34 APT  
**Note:** CoinStore resource returns 404 for all addresses (migrated to Fungible Asset model); balances retrieved via `0x1::coin::balance` view function successfully.

### Multisig Contract Probes

All 5 multisig contracts are **healthy** (2-of-N sigs required):

| Pair | Address (prefix) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4f428... | 2 | yes |
| A-G | 0xf56c4a1c... | 2 | yes |
| Y-Z | 0xd3ffe181... | 2 | yes |
| S-T | 0x3b1c3ae9... | 2 | yes |
| V-W | 0x40fad7b4... | 2 | yes |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — All endpoints return HTTP 401 Unauthorized. SPA also returns 401. No market data extracted.

---

## DuckDB Location

```
packages/world-increment/ducklake/world-increments.duckdb
```

Tables: `world_increments`, `repo_snapshots`, `aptos_snapshots`, `multisig_probes`, `mnx_snapshots`

---

## Sweep Metadata
- **Date:** 2026-07-05
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
