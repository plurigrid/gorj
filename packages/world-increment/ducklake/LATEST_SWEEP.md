# World Increment Sweep — 2026-06-28

## JOB 1: GitHub Social Graph Sweep

**381 world increments** across 11 sources, GF(3) color chain applied.

### Repo Snapshot Summary (381 repos)

| Source | Type | Repos | Notes |
|--------|------|-------|-------|
| plurigrid | org | 100 | Most active: gorj (870 issues), eirobri (30 issues), asi (26 stars) |
| bmorphism | user | 100 | Gay.jl (187 issues), ocaml-mcp-sdk (61 stars), anti-bullshit-mcp (23 stars) |
| kubeflow | org | 48 | kubeflow (15749 stars), pipelines (4158), spark-operator (3129) |
| zubyul | user | 49 | gay-world (1 star), nash-tui, openbci-visualizer — active 2026 |
| AustinCStone | user | 30 | TextGAN (92 stars), StructureFromMotion, ML/vision focus |
| migalkin | user | 19 | NodePiece (144 stars), StarE (89), NBFNet_mlx (10), KG researcher |
| wasita | user | 11 | wasita.github.io (Svelte, active Jun 2026), ch3-lib (Typst) |
| M1shaaa | user | 8 | lab-bookshelf- (TypeScript), M1shaaa profile (active Jun 2026) |
| DJedamski | user | 6 | Old Coursera projects, Kaggle NCAA 2018 |
| TeglonLabs | org | 5 | jank-crane (C++, GF3/IR), mathpix-gem (2 stars), coin-flip-mcp |
| kristinezheng | user | 5 | Personal website, MIT cognitive science research |

### GF(3) Color Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 127 |
| 1 | #b8bb26 | PLUS | 127 |
| 2 | #cc241d | MINUS | 127 |

### Notable Activity (last 7 days)

- **plurigrid/gorj** pushed 2026-06-28 — 870 open issues, active Clojure/forj work
- **plurigrid/asi** pushed 2026-06-28 — "everything is topological chemputer!"
- **bmorphism/Gay.jl** pushed 2026-06-28 — 187 open issues, active Julia development
- **kubeflow/pipelines** pushed 2026-06-27 — 4158 stars, active ML pipelines
- **wasita/wasita.github.io** pushed 2026-06-25 — Svelte personal site
- **M1shaaa/M1shaaa** pushed 2026-06-27 — profile config active

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 Hamming swarm wallets (alice, bob, A-Z) returned **0.0 APT** — CoinStore
resources not registered on mainnet (accounts exist but hold no APT).

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **healthy** (reachable, num_signatures_required returned).

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...7003 | 2 | healthy |
| A-G | 0xf56c4a1c...0096 | 2 | healthy |
| Y-Z | 0xd3ffe181...b883 | 2 | healthy |
| S-T | 0x3b1c3ae9...7883 | 2 | healthy |
| V-W | 0x40fad7b4...eb6d | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — testnet.mnx.fi is a Vercel-protected SPA requiring authentication.
All API endpoints return auth wall. No market data extracted.

---

## DuckDB Schema

Database: packages/world-increment/ducklake/world-increments.duckdb

| Table | Rows | Description |
|-------|------|-------------|
| world_increments | 381 | GF(3)-colored increment ledger |
| repo_snapshots | 381 | Full repo metadata per increment |
| aptos_snapshots | 28 | Hamming wallet balances |
| multisig_probes | 5 | Multisig contract health |
| mnx_snapshots | 0 | MNX markets (unavailable) |

---

Sweep completed: 2026-06-28 UTC
Sources: plurigrid, kubeflow, TeglonLabs, bmorphism, zubyul, migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone
