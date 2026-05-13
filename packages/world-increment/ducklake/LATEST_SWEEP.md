# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-13

> **Latest:** increment id=13 · GF(3) PLUS · #b8bb26

---

# World-Increment Sweep — 2026-04-12

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

---

# Hamming Swarm Snapshot — 2026-05-13 (Increment 13 · PLUS · #b8bb26)

## GitHub Sweep (increment 13)
GitHub public API rate limit was exhausted (0/60 unauthenticated). Only `plurigrid/gorj` was accessible via MCP GitHub integration.

| Metric | Value |
|--------|-------|
| Total World Increments | 24 |
| Total Repo Snapshots | 946 |
| New repos this sweep | 2 (gorj + rate-limit meta) |

## Aptos Wallet Balances — Hamming Swarm (28 addresses)
All 28 accounts queried against Aptos mainnet (`fullnode.mainnet.aptoslabs.com`).  
All returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — accounts are not initialized with APT. Ledger confirmed live: block 764,097,610, epoch 15789.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob   | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13  | 0.0 |
| C | 0x38b9...35e  | 0.0 |
| D | 0xf776...dd1  | 0.0 |
| E | 0xdc1d...d36  | 0.0 |
| F | 0x18a1...f71  | 0.0 |
| G | 0x69a3...f32  | 0.0 |
| H | 0xce67...00f  | 0.0 |
| I | 0x070f...fc9  | 0.0 |
| J | 0x4d96...f54  | 0.0 |
| K | 0xa732...dc4  | 0.0 |
| L | 0x7c2e...ba9  | 0.0 |
| M | 0x6fed...2e9  | 0.0 |
| N | 0xe7dd...b2c  | 0.0 |
| O | 0x7325...89d  | 0.0 |
| P | 0x6218...948  | 0.0 |
| Q | 0xac40...89a9 | 0.0 |
| R | 0x7ce6...e10  | 0.0 |
| S | 0xb875...386  | 0.0 |
| T | 0x3578...588  | 0.0 |
| U | 0x7586...956  | 0.0 |
| V | 0xb59d...2c3  | 0.0 |
| W | 0x5f32...7b0  | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...97c  | 0.0 |

## Multisig Contract Probes — 5/5 Healthy

All 5 multisig accounts respond with `num_signatures_required = 2` via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

## MNX Markets (testnet.mnx.fi)
Root URL returns HTTP 200 (SPA). No REST API endpoints exposed at `/api/markets`, `/api/v1/markets`, or `/api/tickers`. Market data unavailable via API probe — noted as unavailable in `mnx_snapshots`.

## DuckDB Final State (2026-05-13)
| table | rows |
|-------|------|
| world_increments | 24 |
| repo_snapshots | 946 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

## GF(3) Chain Position
`... ERGODIC(12) → **PLUS(13)** → MINUS(14) → ...`  
Next sweep: id=14 · trit=-1 · MINUS · #cc241d
