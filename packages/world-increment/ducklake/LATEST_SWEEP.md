# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-16

## Sweep Metadata
- **Date:** 2026-04-16
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 32 |
| Total Repo Snapshots | 1172 (cumulative across sweeps) |
| New Repos This Sweep | 228 |
| Sources Covered (today) | 2 orgs + 4 users (6 rate-limited) |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 (all healthy) |
| MNX Markets | Unavailable (SPA, no API) |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried (2026-04-16)

| Source | Type | Repos | Last Push |
|--------|------|-------|-----------|
| plurigrid | org | 100 | 2026-04-16 |
| TeglonLabs | org | 53 | 2026-01-16 |
| migalkin | user (zubyul graph) | 30 | 2025-08-04 |
| kristinezheng | user (zubyul graph) | 18 | 2026-04-09 |
| M1shaaa | user (zubyul graph) | 16 | 2026-04-16 |
| DJedamski | user (zubyul graph) | 11 | 2018-03-07 |

**Rate-limited (no auth token):** kubeflow, bmorphism, zubyul, wasita, AustinCStone

### GF(3) Color Chain — Today's Increments (IDs 12–20)

| ID | GF3 Trit | Color | Name | Source |
|----|----------|-------|------|--------|
| 12 | 0 | `#d3869b` | **ERGODIC** | plurigrid |
| 13 | 1 | `#b8bb26` | **PLUS** | TeglonLabs |
| 14 | -1 | `#cc241d` | **MINUS** | migalkin |
| 15 | 0 | `#d3869b` | **ERGODIC** | DJedamski |
| 16 | 1 | `#b8bb26` | **PLUS** | kristinezheng |
| 17 | -1 | `#cc241d` | **MINUS** | M1shaaa |
| 18 | 0 | `#d3869b` | **ERGODIC** | aptos_hamming |
| 19 | 1 | `#b8bb26` | **PLUS** | multisig_probes |
| 20 | -1 | `#cc241d` | **MINUS** | mnx_markets |

GF(3) balanced: 3× ERGODIC / 3× PLUS / 3× MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
Wallets are unfunded or hold Fungible Assets (not legacy CoinStore).

| World | Short Address | Balance APT |
|-------|--------------|-------------|
| alice | 0xc793...4cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z (26 wallets) | various | 0.0 each |

### Multisig Contract Probes (`num_signatures_required`)

All 5 pairs healthy — **2-of-2 threshold** confirmed on every pair.

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (`testnet.mnx.fi`)

SPA confirmed live (Next.js). All REST API paths (`/api/markets`, `/api/v1/markets`) returned DNS routing errors — no structured market data extractable without browser execution. `mnx_snapshots`: 0 rows.

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
