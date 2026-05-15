# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-15

---

## JOB 1: GitHub Social Graph Sweep

### Increments Added (IDs 13–23)

| ID | GF3 Trit | Color | Name | Source | Repos Snapped |
|----|----------|-------|------|--------|---------------|
| 13 | +1 | `#b8bb26` | PLUS | plurigrid (org) | 33 |
| 14 | -1 | `#cc241d` | MINUS | kubeflow (org) | 20 |
| 15 | 0 | `#d3869b` | ERGODIC | TeglonLabs (org) | 4 |
| 16 | +1 | `#b8bb26` | PLUS | bmorphism (user) | 25 |
| 17 | -1 | `#cc241d` | MINUS | zubyul (user) | 15 |
| 18 | 0 | `#d3869b` | ERGODIC | migalkin (social) | 7 |
| 19 | +1 | `#b8bb26` | PLUS | DJedamski (social) | 6 |
| 20 | -1 | `#cc241d` | MINUS | AustinCStone (social) | 6 |
| 21 | 0 | `#d3869b` | ERGODIC | kristinezheng (social) | 6 |
| 22 | +1 | `#b8bb26` | PLUS | wasita (social) | 8 |
| 23 | -1 | `#cc241d` | MINUS | M1shaaa (social) | 8 |

**Total new repo snapshots: 138 | Total in DB: 1082**

### Notable Repos by Source

**plurigrid** — gorj (Clojure, 202 open issues, 2026-05-15), nanoclj-zig (Zig GF3 trit conservation), zig-syrup (OCapN Syrup), asi (HTML 23★)

**kubeflow** — pipelines (Python 4140★), kubeflow/kubeflow (15632★), trainer (Go 2098★), katib (AutoML 1682★), spark-operator (3125★)

**TeglonLabs** — topoi (Python), mathpix-gem (Ruby), monad-mcp-server, coin-flip-mcp (JS)

**bmorphism** — Gay.jl (Julia, 188 open issues, 2026-05-15), anti-bullshit-mcp (JS 23★), ocaml-mcp-sdk (OCaml 61★), say-mcp-server (JS 20★), nanoclj-zig (Zig), zig-syrup (Zig)

**zubyul** — gay-world (Python goblin world builder), big-bad-plurigrid-quiz (Emacs Lisp), voice-observatory, nash-tui/nash-web (Rust)

**migalkin** (social) — NodePiece (Python 144★ ICLR'22), StarE (89★ EMNLP'20), NBFNet_mlx (Apple Silicon)

**AustinCStone** (social) — TextGAN (Python 92★), StereoVisionMRF (11★)

**wasita** (social) — wasita.github.io (Svelte 2026-05-14), magic-garden (Python bot 2★), wm-cv

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 Hamming-swarm addresses returned **0 APT** at time of snapshot.
Network: Aptos Mainnet (`fullnode.mainnet.aptoslabs.com`)

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.00000000 |
| bob | 0x0a3c...512d | 0.00000000 |
| A–Z (26) | (see aptos_snapshots table) | 0.00000000 each |

### Multisig Contract Probes (5 pairs) — ALL HEALTHY

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

### MNX Markets (`testnet.mnx.fi`)

Status: **SPA (Next.js) — no REST API endpoint available**.
Probed `/api/markets`, `/api/v1/markets`, `/api/tickers` — all returned HTML shell, no extractable market data.

---

## DuckDB State

```
world_increments : 34 rows  (11 new this sweep)
repo_snapshots   : 1082 rows (138 new this sweep)
aptos_snapshots  : 28 rows
multisig_probes  : 5 rows
mnx_snapshots    : 1 row  (spa_unavailable)
```

DB: `packages/world-increment/ducklake/world-increments.duckdb`

---

# Previous Sweep — 2026-04-12

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
