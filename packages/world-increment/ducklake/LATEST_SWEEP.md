# World-Increment Sweep — 2026-07-08

## Sweep Metadata
- **Date:** 2026-07-08
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumul.) | 395 |
| Total Repo Snapshots (cumul.) | 1316 |
| New repo_snapshots this sweep | 372 |
| Sources Covered | 3 orgs + 8 users |
| Aptos wallets probed | 28 |
| Multisig contracts probed | 5 |

---

## JOB 1: GitHub Social Graph Sweep

### New Repos This Sweep (2026-07-08)

| Source | Type | Repos Captured | Top Stars |
|--------|------|----------------|-----------|
| plurigrid | org | 100 (of 103) | asi(30), vcg-auction(7), agent(5) |
| kubeflow | org | 49 | kubeflow(15,768), pipelines(4,169), spark-operator(3,135) |
| TeglonLabs | org | 5 | mathpix-gem(2) |
| bmorphism | user | 100 (of 105) | ocaml-mcp-sdk(61), anti-bullshit-mcp(23), risc0-cosmwasm(23) |
| zubyul | user | 49 | WGCNA(2), jonikas_lab_data(2) |
| migalkin | user | 19 | NodePiece(144), StarE(89), kgcourse2021(25) |
| AustinCStone | user | 20 (of 40) | TextGAN(92), StereoVisionMRF(11) |
| wasita | user | 11 | magic-garden(2), wasita.github.io(1) |
| M1shaaa | user | 8 | — |
| DJedamski | user | 6 | — |
| kristinezheng | user | 5 | — |

### Notable Activity (pushed 2026-07)
- `plurigrid/gorj` — pushed 2026-07-08, 1063 open issues (active, this repo)
- `plurigrid/place` — pushed 2026-07-07
- `kubeflow/pipelines` — pushed 2026-07-08 (4,169 stars)
- `kubeflow/kubeflow` — pushed 2026-07-08 (15,768 stars)
- `bmorphism/Gay.jl` — pushed 2026-07-08, 187 open issues
- `wasita/wasita.github.io` — pushed 2026-07-06

### Top Repos by Source

#### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 30 | 2026-06-29 |
| ontology | JavaScript | 8 | 2025-05-27 |
| vcg-auction | Rust | 7 | 2023-03-16 |
| agent | Python | 5 | 2023-03-31 |
| StochFlow | Python | 4 | 2024-03-20 |

#### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,768 | 2026-07-08 |
| pipelines | Python | 4,169 | 2026-07-08 |
| spark-operator | Python | 3,135 | 2026-07-08 |
| trainer | Go | 2,132 | 2026-07-08 |
| katib | Python | 1,689 | 2026-07-08 |

#### bmorphism (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| risc0-cosmwasm-example | Rust | 23 | 2022-10-20 |
| say-mcp-server | JavaScript | 20 | 2025-01-07 |
| babashka-mcp-server | JavaScript | 19 | 2025-01-05 |

#### migalkin (19 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| NodePiece | Python | 144 | 2026-05-07 |
| StarE | Python | 89 | 2026-04-16 |
| kgcourse2021 | HTML | 25 | 2026-02-16 |

#### AustinCStone (20 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## GF(3) Color Chain

- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=**ERGODIC**
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=**MINUS**

This sweep added increments 29–395, cycling through the ERGODIC→PLUS→MINUS triad 122 full cycles plus 2 extra.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-07-08)

All 28 addresses queried at `fullnode.mainnet.aptoslabs.com/v1`.

| World | Balance (APT) | World | Balance (APT) |
|-------|---------------|-------|---------------|
| alice | 0.0 | N | 0.0 |
| bob   | 0.0 | O | 0.0 |
| A | 0.0 | P | 0.0 |
| B | 0.0 | Q | 0.0 |
| C | 0.0 | R | 0.0 |
| D | 0.0 | S | 0.0 |
| E | 0.0 | T | 0.0 |
| F | 0.0 | U | 0.0 |
| G | 0.0 | V | 0.0 |
| H | 0.0 | W | 0.0 |
| I | 0.0 | X | 0.0 |
| J | 0.0 | Y | 0.0 |
| K | 0.0 | Z | 0.0 |
| L | 0.0 | | |
| M | 0.0 | | |

**Summary:** All 28 Hamming-swarm wallets at 0.0 APT (zero-balance probe addresses).

### Multisig Contract Probes

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ healthy |
| A-G | 0xf56c...0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✅ healthy |
| S-T | 0x3b1c...7883 | 2 | ✅ healthy |
| V-W | 0x40fa...eb6d | 2 | ✅ healthy |

All 5 multisig contracts require **2-of-N signatures** and respond normally via `0x1::multisig_account::num_signatures_required`.

### MNX Markets (`testnet.mnx.fi`)
**Status: UNAVAILABLE** — Vercel deployment protection active. All API paths (`/api/markets`, `/api/tickers`) return 401/authentication-required. No market data extractable without a bypass token.

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,768 stars (+203 vs April sweep) — active Kubernetes ML platform
- **kubeflow/pipelines**: 4,169 stars — pushed today (2026-07-08)
- **migalkin/NodePiece**: 144 stars (+1 vs April) — knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 61 stars (+1) — OCaml SDK for MCP using oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — TensorFlow text generation GAN
- **plurigrid/asi**: 30 stars (+14 vs April!) — topological chemputer, strong growth
- **plurigrid/gorj**: active with 1063 open issues — this repo running the sweep
- **Multisigs**: all 5 pairs (A-B, A-G, Y-Z, S-T, V-W) healthy at 2-of-N threshold
