# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-30

## Sweep Metadata
- **Date:** 2026-07-30
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 165 |
| Total Repo Snapshots (cumulative) | 1,086 |
| **New Increments This Run** | **142** |
| Sources Covered | 3 orgs + 8 users |
| Aptos addresses probed | 28 |
| Multisig contracts probed | 5 |

---

## GF(3) Color Chain Distribution (Cumulative)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| +1 | `#b8bb26` | PLUS | 56 |
| -1 | `#cc241d` | MINUS | 55 |
| 0 | `#d3869b` | ERGODIC | 54 |

GF(3) rule: `id mod 3 == 0 → ERGODIC` | `id mod 3 == 1 → PLUS` | `id mod 3 == 2 → MINUS`

---

## Hamming Swarm Snapshot (2026-07-30)

### Aptos Wallet Balances (alice, bob, A–Z)

**Network status: UNREACHABLE** — environment proxy blocks `fullnode.mainnet.aptoslabs.com` (returns connection refused). All 28 addresses recorded as `NULL` balance in `aptos_snapshots`. Addresses on record for next reachable run:

- `alice` → `0xc793...cc7b`
- `bob` → `0x0a3c...512d`
- `A` → `0x8699...9d7a` through `Z` → `0x7af0...197c`

### Multisig Contract Probes (5 pairs)

**Network status: UNREACHABLE** — same proxy restriction.

| Pair | Contract Address | Status |
|------|-----------------|--------|
| A-B | `0x0da4...7003` | unreachable |
| A-G | `0xf56c...0096` | unreachable |
| Y-Z | `0xd3ff...b883` | unreachable |
| S-T | `0x3b1c...7883` | unreachable |
| V-W | `0x40fa...eb6d` | unreachable |

### MNX Markets

- `testnet.mnx.fi/api/markets` → 404
- SPA frontend renders `MNX` ticker only; no OHLCV data extractable via WebFetch
- `mnx_snapshots`: 0 rows this run

---

## Top Repos by Source (2026-07-30 snapshot)

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 56 | 2026-07-10 |
| zig-syrup | Zig | 2 | 2026-07-28 |
| gorj | Clojure | 1 | 2026-07-30 |
| place | TeX | 1 | 2026-07-14 |
| eirobri | Clojure | 0 | 2026-07-21 |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,798 | 2026-07-30 |
| pipelines | Python | 4,171 | 2026-07-29 |
| spark-operator | Python | 3,142 | 2026-07-29 |
| trainer | Go | 2,163 | 2026-07-30 |
| katib | Python | 1,694 | 2026-07-29 |

### TeglonLabs (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| jank-crane | C++ | 0 |
| monad-mcp-server | — | 0 |

### bmorphism (106 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 61 |
| risc0-cosmwasm-example | Rust | 23 |
| anti-bullshit-mcp-server | JavaScript | 22 |
| say-mcp-server | JavaScript | 20 |
| Gay.jl | Julia | 2 (188 open issues) |

### migalkin (19 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 24 |

### zubyul (49 repos)
| Repo | Language | Stars |
|------|----------|-------|
| WGCNA | HTML | 2 |
| gay-world | Python | 1 |
| ghostel-emacs-worlds | GLSL | 0 |

### AustinCStone (41 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source (2026-07-30)

| Source | Type | Repos Known |
|--------|------|-------------|
| plurigrid | org | 100 |
| bmorphism | user | 106 |
| kubeflow | org | 49 |
| AustinCStone | user | 41 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| wasita | user | 12 |
| M1shaaa | user | 8 |
| TeglonLabs | org | 5 |
| kristinezheng | user | 5 |
| DJedamski | user | 6 |
| **TOTAL** | | **400** |

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

## Notable Highlights (2026-07-30)
- **kubeflow/kubeflow**: 15,798 stars (+233 since Apr) — flagship ML platform
- **kubeflow/trainer**: 2,163 stars (+83) — Distributed AI/LLM Fine-Tuning on Kubernetes
- **kubeflow/mcp-server**: 31 stars (new) — MCP Server for AI-Assisted Kubeflow dev
- **migalkin/NodePiece**: 144 stars (+1) — ICLR'22 knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 61 stars (+1) — OCaml MCP SDK using Jane Street oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text GAN
- **plurigrid/asi**: 56 stars (+40 since Apr!) — topological chemputer, fastest-growing plurigrid repo
- **plurigrid/gorj**: 1 star, 1,514 open issues — active Clojure REPL orchestration (pushed today)
- **zubyul/tilelang-kernels**: TileLang GPU kernels for GF(3) trit classification on NVIDIA Blackwell
- **bmorphism/Gay.jl**: 188 open issues — wide-gamut color sampling project
- **Network constraint**: Aptos mainnet and MNX testnet unreachable from this environment
