# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-14

## Sweep Metadata
- **Date:** 2026-06-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (this run)

| Metric | Value |
|--------|-------|
| New World Increments | 97 |
| New Repo Snapshots | 97 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph Sweep

### Hot Repos (pushed within 72h of 2026-06-14)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| plurigrid/gorj | Clojure | 0 | **2026-06-14** (TODAY, 561 issues) |
| bmorphism/Gay.jl | Julia | 1 | **2026-06-14** (189 issues) |
| plurigrid/asi | HTML | 26 | 2026-06-10 |
| plurigrid/place | TeX | 1 | 2026-06-10 |
| bmorphism/satreadout | Lean | 0 | 2026-06-10 |
| kubeflow/website | HTML | 184 | 2026-06-13 |
| kubeflow/pipelines | Python | 4153 | 2026-06-13 |
| kubeflow/trainer | Go | 2114 | 2026-06-13 |
| kubeflow/spark-operator | Python | 3128 | 2026-06-12 |
| TeglonLabs/jank-crane | C++ | 0 | 2026-06-08 |

### Top Repos by Source

#### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 26 | 2026-06-10 |
| ontology | JavaScript | 8 | 2025-05-27 |
| vcg-auction | Rust | 7 | 2023-03-16 |
| agent | Python | 5 | 2023-03-31 |
| StochFlow | Python | 4 | 2024-03-20 |
| gorj | Clojure | 0 | 2026-06-14 (561 issues) |

#### kubeflow (47 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15720 | 2026-06-11 |
| pipelines | Python | 4153 | 2026-06-13 |
| spark-operator | Python | 3128 | 2026-06-12 |
| trainer | Go | 2114 | 2026-06-13 |
| katib | Python | 1683 | 2026-06-12 |

#### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| jank-crane | C++ | 0 | 2026-06-08 |
| topoi | Python | 0 | 2025-01-24 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |

#### bmorphism (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| risc0-cosmwasm-example | Rust | 23 | 2022-10-20 |
| say-mcp-server | JavaScript | 20 | 2025-01-07 |
| babashka-mcp-server | JavaScript | 19 | 2025-01-05 |
| manifold-mcp-server | JavaScript | 14 | 2025-01-11 |
| Gay.jl | Julia | 1 | 2026-06-14 (189 issues) |

#### zubyul (50 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| WGCNA | HTML | 2 | 2023-07-05 |
| Nikolova_lab_data_analysis | R | 2 | 2023-06-16 |
| gay-world | Python | 1 | 2026-03-26 |
| ghostty-modifications | JavaScript | 1 | 2025-09-15 |

#### Social Graph
| User | Top Repo | Stars | Domain |
|------|----------|-------|--------|
| migalkin | NodePiece (Python, 144★) | KG embeddings (ICLR'22) |
| DJedamski | School (R, 1★) | data science |
| wasita | magic-garden (Python, 2★) | neuroscience/web |
| kristinezheng | kristinezheng.github.io | MIT cog sci |
| M1shaaa | M1shaaa profile | Yale lab work |
| AustinCStone | TextGAN (Python, 92★) | ML/DL |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses, 2026-06-14)
All 28 wallets returned **0.0 APT** — CoinStore resource absent or unfunded on mainnet.

| World | Address (truncated) | APT |
|-------|---------------------|-----|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…2d5d | 0.0 |
| A–Z | 26 addresses | 0.0 each |

### Multisig Contract Probes — All HEALTHY
All 5 contracts returned `sigs_required=2`. Contracts are live on Aptos mainnet.

| Pair | Address (truncated) | Sigs | Status |
|------|---------------------|------|--------|
| A-B | 0x0da4…7003 | 2 | HEALTHY |
| A-G | 0xf56c…0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff…b883 | 2 | HEALTHY |
| S-T | 0x3b1c…7883 | 2 | HEALTHY |
| V-W | 0x40fa…eb6d | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)
**UNAVAILABLE** — HTTP 401 on both `/` and `/api/markets`. Requires authentication.
Recorded as null entry in mnx_snapshots table.

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

## Key Signals (2026-06-14)
- **gorj + Gay.jl both pushed today** — active development on core plurigrid/bmorphism axis
- **All 5 multisig contracts healthy** — A-B, A-G, Y-Z, S-T, V-W all respond with sigs=2
- **Hamming wallets all at 0 APT** — 28 addresses unfunded on mainnet; may require testnet check
- **kubeflow very active**: pipelines, trainer, katib, spark-operator all pushed within 48h
- **TeglonLabs/jank-crane** appeared 2026-06-08 — new C++ crane-jank convergence IR hub
- **bmorphism/ocaml-mcp-sdk** at 61★ — highest-starred new repo since last sweep
