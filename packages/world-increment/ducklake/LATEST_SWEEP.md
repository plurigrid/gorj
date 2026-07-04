# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-04

## Sweep Metadata
- **Date:** 2026-07-04
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| New World Increments (this run) | 301 |
| Cumulative Repo Snapshots | 1,245 |
| Sources Covered | 3 orgs + 8 users |

### GF(3) Color Distribution (this run, 301 increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 100 |
| +1 | `#b8bb26` | PLUS | 101 |
| -1 | `#cc241d` | MINUS | 100 |

### Repo Counts by Source

| Source | Type | Repos This Run |
|--------|------|----------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 16 |
| migalkin | social graph | 7 |
| DJedamski | social graph | 4 |
| wasita | social graph | 7 |
| kristinezheng | social graph | 3 |
| M1shaaa | social graph | 4 |
| AustinCStone | social graph | 7 |
| **TOTAL** | | **301** |

### Top Repos by Source (2026-07-04)

**plurigrid** — Most recently active:
- `gorj` Clojure — forj + Rama topology nREPL routing + GF(3) gay trit coloring (955 issues, pushed 2026-07-04)
- `shrimp` — Jank worked example (pushed 2026-07-03)
- `asi` HTML ⭐28 — everything is topological chemputer (pushed 2026-06-29)
- `place` TeX — bci.place forester (pushed 2026-06-29)
- `eirobri` Clojure — EiRoBri replay world (pushed 2026-06-30)

**kubeflow** — Most recently active:
- `hub` Go ⭐173 — Model Registry (pushed 2026-07-04)
- `trainer` Go ⭐2,129 — Distributed AI Training on Kubernetes (pushed 2026-07-03)
- `pipelines` Python ⭐4,169 — ML Pipelines for Kubeflow (pushed 2026-07-03)
- `kubeflow` ⭐15,761 — ML Toolkit for Kubernetes

**bmorphism** — Most recently active:
- `Gay.jl` Julia ⭐2 — Wide-gamut color sampling, SPI determinism (pushed 2026-06-20)
- `penrose-mcp` JS ⭐9 — Penrose for Infinity-Topos (pushed 2026-06-24)
- `ocaml-mcp-sdk` OCaml ⭐61 — MCP SDK for OCaml/Jane Street oxcaml (pushed 2026-05-08)
- `anti-bullshit-mcp-server` JS ⭐23 — claim validation MCP server

**Social graph** — Notably active:
- `wasita/wasita.github.io` Svelte ⭐1 (pushed 2026-07-02)
- `kristinezheng/kristinezheng.github.io` HTML (pushed 2026-07-01)
- `migalkin/NodePiece` Python ⭐144 — ICLR'22 KG embeddings (pushed 2026-05-07)
- `TeglonLabs/jank-crane` C++ — GF3 convergence maps (pushed 2026-06-08)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)

All 28 addresses queried against `fullnode.mainnet.aptoslabs.com` (ledger v6,091,705,957).

**Result:** All accounts returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
These accounts have no APT CoinStore — either unfunded or using a different resource type.

| World | Balance (APT) | Status |
|-------|--------------|--------|
| alice, bob, A–Z (28 total) | 0 / N/A | resource_not_found |

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.
**All contracts healthy — 2-of-N threshold confirmed.**

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4...7003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — Vercel deployment protection (visitor password required).
No market data accessible without credentials.

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
- **plurigrid/gorj**: 955 open issues — active forj+Rama nREPL orchestration (pushed TODAY)
- **kubeflow/kubeflow**: 15,761 stars — flagship ML platform for Kubernetes
- **kubeflow/trainer**: 2,129 stars — Distributed AI Training (pushed 2026-07-03)
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP (Jane Street oxcaml_effect)
- **migalkin/NodePiece**: 144 stars — compositional KG representations (ICLR'22)
- **AustinCStone/TextGAN**: 92 stars — TF text generation GAN
- **Multisig health**: All 5 pairs (A-B, A-G, Y-Z, S-T, V-W) at 2-of-N, healthy
- **Aptos wallets**: All 28 accounts (alice, bob, A–Z) have no APT CoinStore resource
