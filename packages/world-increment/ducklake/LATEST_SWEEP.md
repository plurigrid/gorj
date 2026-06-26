# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-26

## Sweep Metadata
- **Date:** 2026-06-26
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 351 |
| Total Repo Snapshots | 1,272 |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (SPA) |
| Sources Covered | 3 orgs + 8 users + 6 social graph |
| Total GitHub Stars | 103,878 |
| Latest Observed Push | 2026-06-26T05:09:22Z |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| plurigrid | org | 100 | ~157 |
| kubeflow | org | 48 | ~101,980 |
| TeglonLabs | org | 5 | 2 |
| bmorphism | user | 100 | ~509 |
| zubyul | user | 49 | ~40 |
| migalkin | social | 19 | ~283 |
| wasita | social | 11 | 5 |
| AustinCStone | social | 40 | ~107 |
| DJedamski | social | 6 | 3 |
| kristinezheng | social | 5 | 0 |
| M1shaaa | social | 8 | 0 |

### Notable Repos (this sweep)
- **kubeflow/kubeflow** — ⭐15,565 — flagship ML platform for Kubernetes
- **kubeflow/pipelines** — ⭐4,119 — most popular ML pipeline (pushed 2026-04-10)
- **migalkin/NodePiece** — ⭐144 — Compositional KG representations (ICLR'22)
- **migalkin/StarE** — ⭐89 — Hyper-relational KG message passing (EMNLP 2020)
- **AustinCStone/TextGAN** — ⭐92 — GAN for text generation (TensorFlow)
- **TeglonLabs/jank-crane** — C++ — crane-jank converged-IR hub with GF3 convergence maps (pushed 2026-06-08)
- **TeglonLabs/mathpix-gem** — ⭐2, 11 open issues — Math image to LaTeX Ruby gem
- **wasita/wasita.github.io** — Svelte — Updated 2026-06-25 (most recently active in sweep)

### GF(3) Color Chain Distribution

| GF3 Trit | Name | Color | Rule | Count |
|----------|------|-------|------|-------|
| 0 | ERGODIC | #d3869b | id % 3 == 0 | 117 |
| +1 | PLUS | #b8bb26 | id % 3 == 1 | 118 |
| -1 | MINUS | #cc241d | id % 3 == 2 | 116 |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances
All 28 addresses (alice, bob, A–Z) returned **0 APT** — no registered
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource found.
Addresses exist on chain but APT coin storage has not been initialized.

### Multisig Contract Probes — ALL HEALTHY

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ healthy |
| A-G | 0xf56c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)
**Status: SPA only — no REST API data available.**
All probed paths (`/api/markets`, `/api/v1/markets`, `/markets`, `/api/tickers`, `/v1/markets`)
return the single-page application HTML shell. No market data extractable without a headless browser.

---

## GF(3) Color Chain — Sample (first 12 increments)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | plurigrid (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | plurigrid (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | plurigrid (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | plurigrid (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| ... | ... | ... | ... | ... | ... |
| 351 | M1shaaa (social) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain cycles: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → ...`

---

## DuckDB Ducklake Schema

Located at: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 351 |
| repo_snapshots | 1,272 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

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
