# World-Increment Sweep — 2026-08-06

## Sweep Metadata
- **Date:** 2026-08-06
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 12 |
| Total Repo Snapshots | 396 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (A–Z + alice + bob) |
| Multisig Pairs Probed | 5 |
| MNX Markets | unavailable (SPA, no JSON API) |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — All 12 Increments

| ID | Source | Type | Repos | GF3 Trit | Color | Name |
|----|--------|------|-------|-----------|-------|------|
| 1  | plurigrid | org | 100 | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | 49 | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | org | 5 | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | user | 100 | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | user | 49 | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user | 19 | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | user | 6 | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | user | 14 | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | user | 5 | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | 8 | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | 41 | -1 | `#cc241d` | **MINUS** |
| 12 | gorj (sweep_complete) | org | — | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | user | 41 |
| migalkin | user | 19 |
| wasita | user | 14 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user | 5 |
| **TOTAL** | | **396** |

### Top Repos by Source

#### kubeflow (49 repos)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| kubeflow/kubeflow | — | 15,805 | 2026-01-05 |
| kubeflow/pipelines | Python | 4,178 | 2026-04-10 |
| kubeflow/spark-operator | Python | 3,144 | 2026-04-10 |
| kubeflow/trainer | Go | 2,171 | 2026-04-10 |
| kubeflow/katib | Python | 1,694 | 2026-04-02 |

#### plurigrid (100 repos)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| plurigrid/asi | HTML | 59 | 2026-07-10 |
| plurigrid/ontology | JavaScript | 8 | 2025-05-27 |
| plurigrid/vcg-auction | Rust | 7 | 2023-03-16 |
| plurigrid/agent | Python | 5 | 2023-03-31 |
| plurigrid/microworlds | Rust | 4 | 2023-05-13 |

#### bmorphism (100 repos)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| bmorphism/risc0-cosmwasm-example | Rust | 23 | 2022-10-20 |
| bmorphism/say-mcp-server | JavaScript | 20 | 2025-01-07 |
| bmorphism/babashka-mcp-server | JavaScript | 19 | 2025-01-05 |

#### migalkin (19 repos)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| migalkin/NodePiece | Python | 144 | 2022-02-02 |
| migalkin/StarE | Python | 89 | 2023-12-01 |
| migalkin/kgcourse2021 | HTML | 24 | 2025-08-04 |
| migalkin/NBFNet_mlx | Python | 10 | 2024-03-02 |

#### AustinCStone (41 repos)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| AustinCStone/TextGAN | Python | 92 | 2016-10-04 |
| AustinCStone/StereoVisionMRF | Python | 11 | 2016-01-10 |
| AustinCStone/SpectralClustering | Python | 3 | 2015-11-09 |

#### TeglonLabs (5 repos) — NEW: jank-crane added since last sweep
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| TeglonLabs/jank-crane | C++ | 0 | 2026-06-08 |
| TeglonLabs/mathpix-gem | Ruby | 2 | 2026-01-01 |
| TeglonLabs/coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

#### wasita (14 repos) — NEW: xoxowasita-analysis (2026-08-05), joint-planning-lit (2026-08-04)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| wasita/xoxowasita-analysis | Python | 0 | 2026-08-05 |
| wasita/joint-planning-lit | — | 0 | 2026-08-04 |
| wasita/wasita.github.io | Svelte | 1 | 2026-07-21 |

#### M1shaaa (8 repos)
| Repo | Language | Pushed |
|------|----------|--------|
| M1shaaa/M1shaaa | — | 2026-08-06 |
| M1shaaa/lab-bookshelf- | TypeScript | 2024-12-31 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)

All 28 Hamming-world wallets (alice, bob, A–Z) returned **0.0000 APT**.
Wallets are confirmed to exist on-chain (200 OK from Aptos fullnode) but hold no APT balance at this snapshot.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793ac… | 0.0000 |
| bob | 0x0a3c00… | 0.0000 |
| A | 0x8699ed… | 0.0000 |
| B | 0x3f892e… | 0.0000 |
| C | 0x38b99e… | 0.0000 |
| D | 0xf77656… | 0.0000 |
| E | 0xdc1d9d… | 0.0000 |
| F | 0x18a14b… | 0.0000 |
| G | 0x69a394… | 0.0000 |
| H | 0xce67c3… | 0.0000 |
| I | 0x070fe5… | 0.0000 |
| J | 0x4d964d… | 0.0000 |
| K | 0xa73204… | 0.0000 |
| L | 0x7c2eae… | 0.0000 |
| M | 0x6fed37… | 0.0000 |
| N | 0xe7dde6… | 0.0000 |
| O | 0x73252b… | 0.0000 |
| P | 0x621879… | 0.0000 |
| Q | 0xac40fa… | 0.0000 |
| R | 0x7ce605… | 0.0000 |
| S | 0xb87530… | 0.0000 |
| T | 0x35781d… | 0.0000 |
| U | 0x75860d… | 0.0000 |
| V | 0xb59dd8… | 0.0000 |
| W | 0x5f32ae… | 0.0000 |
| X | 0xa95cbb… | 0.0000 |
| Y | 0xd8e328… | 0.0000 |
| Z | 0x7af0ef… | 0.0000 |

### Multisig Contract Probes (5 pairs)

All 5 multisig pairs are **healthy** (2-of-2 threshold).

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f4… | 2 | ✓ healthy |
| A-G | 0xf56c4a… | 2 | ✓ healthy |
| Y-Z | 0xd3ffe1… | 2 | ✓ healthy |
| S-T | 0x3b1c3a… | 2 | ✓ healthy |
| V-W | 0x40fad7… | 2 | ✓ healthy |

### MNX Markets

`testnet.mnx.fi` returned SPA HTML only — no JSON API endpoints responded at `/api/markets`, `/api/v1/markets`, `/markets`, or `/api/tickers`. MNX market data is **unavailable** at this sweep.

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,805 stars — still the flagship ML platform for Kubernetes
- **plurigrid/asi**: 59 stars (up from 16 in April sweep) — topological chemputer, last pushed 2026-07-10
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP using oxcaml_effect
- **migalkin/NodePiece**: 144 stars — scalable knowledge graph embeddings
- **TeglonLabs/jank-crane**: NEW since April — crane-jank converged-IR hub with GF3 convergence maps (C++)
- **wasita**: 2 new repos in 48h — `xoxowasita-analysis` (2026-08-05) and `joint-planning-lit` (2026-08-04)
- **M1shaaa/M1shaaa**: pushed TODAY (2026-08-06T02:11:35Z) — active profile update
- **All 5 multisigs**: healthy at 2-of-2 threshold — Hamming swarm topology intact
- **Increment 12**: ERGODIC — sweep_complete closing the 4th full GF(3) cycle
