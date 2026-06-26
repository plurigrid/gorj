# World-Increment Sweep + Hamming Snapshot — 2026-06-26

## Sweep Metadata
- **Date:** 2026-06-26
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 120 (cumulative) |
| Total Unique Repo Snapshots | 504 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain (This Run — 97 new increments)
- **ERGODIC** (#d3869b, trit=0): 39 increments
- **PLUS** (#b8bb26, trit=1): 41 increments
- **MINUS** (#cc241d, trit=-1): 40 increments

GF(3) chain pattern: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ...`

---

## Top Repos by Source

### plurigrid (112 unique repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 26 | 2026-06-26 |
| ontology | JavaScript | 8 | 2025-05-27 |
| vcg-auction | Rust | 7 | 2023-03-16 |
| agent | Python | 5 | 2023-03-31 |
| StochFlow | Python | 4 | 2024-03-20 |
| gorj | Clojure | 0 (834 issues!) | 2026-06-26 |

### kubeflow (48 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,744 | 2026-06-18 |
| pipelines | Python | 4,156 | 2026-06-25 |
| spark-operator | Python | 3,128 | 2026-06-26 |
| trainer | Go | 2,122 | 2026-06-25 |
| katib | Python | 1,685 | 2026-06-23 |

### TeglonLabs (5 public repos)
| Repo | Language | Stars |
|------|----------|-------|
| jank-crane | C++ | 0 |
| mathpix-gem | Ruby | 2 |
| coin-flip-mcp | JavaScript | 0 |

### bmorphism (113 unique repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 61 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| risc0-cosmwasm-example | Rust | 23 |
| say-mcp-server | JavaScript | 20 |
| babashka-mcp-server | JavaScript | 19 |
| Gay.jl | Julia | 2 (187 issues!) |

### zubyul (28 unique repos)
| Repo | Language | Stars |
|------|----------|-------|
| gay-world | Python | 1 |
| zubyul.github.io | CSS | 1 |
| jonikas_lab_data_analysis_misc | Jupyter | 2 |
| WGCNA | HTML | 2 |

### Social Graph (migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone)
| Repo | User | Stars |
|------|------|-------|
| AustinCStone/TextGAN | AustinCStone | 92 |
| migalkin/NodePiece | migalkin | 144 |
| migalkin/StarE | migalkin | 89 |

---

## Repo Counts by Source (This Run)

| Source | Type | Unique Repos |
|--------|------|-------------|
| plurigrid | org | 112 |
| bmorphism | user | 113 |
| TeglonLabs | org | 5 (public) |
| kubeflow | org | 48 |
| AustinCStone | user | 43 |
| migalkin | user | 30 |
| wasita | user | 31 |
| zubyul | user | 28 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| **TOTAL** | | **504** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet — 2026-06-26)
All 28 wallets (alice, bob, A–Z) queried via `fullnode.mainnet.aptoslabs.com`.

**All balances: 0.00 APT** — accounts are uninitialized or unfunded on Aptos mainnet.

| World | Address | APT Balance |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.00 |
| bob | 0x0a3c...2d5d | 0.00 |
| A–Z | (26 addresses) | 0.00 each |

### Multisig Contract Probes (Aptos Mainnet)
All probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✅ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✅ HEALTHY |

**All 5 multisig contracts healthy** — all require 2-of-2 signatures.

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — Vercel deployment protection active on all endpoints (`/`, `/api/markets`, `/api/v1/markets`, `/markets`). No market data accessible without authentication token.

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
