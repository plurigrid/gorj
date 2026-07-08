# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-08

## Sweep Metadata
- **Date:** 2026-07-08T00:00 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB:** v1.5.4 (via pip)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Previous sweep:** 2026-04-12 (IDs 1–12)
- **This sweep:** IDs 13–23 (11 new world increments)

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (all-time) | 34 |
| New World Increments (this sweep) | 11 |
| Total Repo Snapshots (all-time) | 1,083 |
| New Repo Snapshots (this sweep) | 139 |
| Sources Covered | 3 orgs + 8 users |

### GF(3) Color Chain — New Increments (IDs 13–23)

| ID | Source | Type | Repos | GF3 Trit | Color | Name |
|----|--------|------|-------|-----------|-------|------|
| 13 | plurigrid | org | 103 | +1 | `#b8bb26` | **PLUS** |
| 14 | kubeflow | org | 49 | -1 | `#cc241d` | **MINUS** |
| 15 | TeglonLabs | org | 5 | 0 | `#d3869b` | **ERGODIC** |
| 16 | bmorphism | user | 105 | +1 | `#b8bb26` | **PLUS** |
| 17 | zubyul | user | 49 | -1 | `#cc241d` | **MINUS** |
| 18 | migalkin | user | 19 | 0 | `#d3869b` | **ERGODIC** |
| 19 | DJedamski | user | 6 | +1 | `#b8bb26` | **PLUS** |
| 20 | wasita | user | 11 | -1 | `#cc241d` | **MINUS** |
| 21 | kristinezheng | user | 5 | 0 | `#d3869b` | **ERGODIC** |
| 22 | M1shaaa | user | 8 | +1 | `#b8bb26` | **PLUS** |
| 23 | AustinCStone | user | 40 | -1 | `#cc241d` | **MINUS** |

GF(3) chain (IDs 13–23): `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

### Top Repos by Source

#### plurigrid (103 repos total, 20 sampled)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gorj | Clojure | 1 | 2026-07-07 |
| asi | HTML | 30 | 2026-07-07 |
| ontology | JavaScript | 8 | 2026-05-09 |
| vcg-auction | Rust | 7 | 2025-12-16 |
| nash-portal | Rust | 2 | 2026-05-19 |

#### kubeflow (49 repos total)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,768 | 2026-07-08 |
| pipelines | Python | 4,169 | 2026-07-08 |
| trainer | Go | 2,132 | 2026-07-08 |
| spark-operator | Python | 3,135 | 2026-07-08 |
| katib | Python | 1,689 | 2026-07-08 |

#### TeglonLabs (5 repos total)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-03-16 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

#### bmorphism (105 repos total, 20 sampled)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| Gay.jl | Julia | 2 | 2026-06-20 |
| risc0-cosmwasm-example | Rust | 23 | 2025-05-21 |
| say-mcp-server | JavaScript | 20 | 2026-03-19 |
| babashka-mcp-server | JavaScript | 19 | 2026-06-05 |

#### zubyul (49 repos total, 20 sampled)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gay-world | Python | 1 | 2026-04-05 |
| magic-garden | Python | 2 | 2026-04-22 |
| send2kobo | TypeScript | 1 | 2026-05-19 |
| jonikas_lab_data_analysis_misc | Jupyter Notebook | 2 | 2023-06-15 |
| WGCNA | HTML | 2 | 2023-06-16 |

#### Social Graph Users (zubyul network)

| User | Repos | Notable |
|------|-------|---------|
| migalkin | 19 | NodePiece (144★), StarE (89★), kgcourse2021 (25★) |
| DJedamski | 6 | kaggle_ncaa18, School, Getting-and-Cleaning-Data |
| wasita | 11 | wasita.github.io, magic-garden, send2kobo |
| kristinezheng | 5 | kristinezheng.github.io, lookit-jenga |
| M1shaaa | 8 | lab-bookshelf-, Python-Lookit-Uploads |
| AustinCStone | 40 | TextGAN (92★), StereoVisionMRF (11★), SpectralClustering (3★) |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 Hamming swarm addresses (alice, bob, A–Z) returned **0.00000000 APT**.

Status: `resource_not_found` — none hold an active `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version ~6,180,184,088. Accounts may never have held APT or use non-standard balance storage.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...c9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...89a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **healthy** — 2 signatures required on each.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...003 | 2 | HEALTHY |
| A-G | 0xf56c...096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...883 | 2 | HEALTHY |
| S-T | 0x3b1c...883 | 2 | HEALTHY |
| V-W | 0x40fa...b6d | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)

All probed API paths (`/api/markets`, `/markets`, `/api/v1/markets`, `/api/tickers`) returned **HTTP 401 Unauthorized**. No public market data was accessible. `mnx_snapshots` table remains empty for this sweep.

---

## Database Totals (All-Time)

| Table | Rows |
|-------|------|
| world_increments | 34 |
| repo_snapshots | 1,083 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |
