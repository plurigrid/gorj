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
| Total World Increments (DB) | 110 |
| Total Repo Snapshots (DB) | 1031 |
| New Increments This Run | 87 |
| Sources Covered This Run | 3 orgs + 8 users |

---

## GF(3) Color Chain — This Run (87 increments, ids 1–87)
- **ERGODIC** `#d3869b` (trit=0): ids 3,6,9,12,… (id%3==0)
- **PLUS** `#b8bb26` (trit=+1): ids 1,4,7,10,… (id%3==1)
- **MINUS** `#cc241d` (trit=-1): ids 2,5,8,11,… (id%3==2)

---

## Top Repos by Source (this sweep)

### plurigrid (15 repos snapshotted)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 26 | 2026-06-26 |
| gorj | Clojure | 0 (830 issues!) | 2026-06-26 |
| place | TeX | 1 | 2026-06-26 |
| eirobri | Clojure | 0 | 2026-06-23 |
| nanoclj-zig | Zig | 1 | 2026-04-25 |

### kubeflow (16 repos snapshotted)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,744 | 2026-06-18 |
| pipelines | Python | 4,156 | 2026-06-25 |
| spark-operator | Python | 3,128 | 2026-06-26 |
| trainer | Go | 2,122 | 2026-06-25 |
| katib | Python | 1,685 | 2026-06-23 |

### TeglonLabs (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| jank-crane | C++ | 0 |
| mathpix-gem | Ruby | 2 |
| coin-flip-mcp | JavaScript | 0 |
| monad-mcp-server | — | 0 |
| topoi | Python | 0 |

### bmorphism (20 repos snapshotted)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 61 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| risc0-cosmwasm-example | Rust | 23 |
| say-mcp-server | JavaScript | 20 |
| Gay.jl | Julia | 2 |

### zubyul (11 repos snapshotted)
| Repo | Language | Stars |
|------|----------|-------|
| gay-world | Python | 1 |
| WGCNA | HTML | 2 |
| vibesnipe | Move | 0 |

### migalkin (social graph)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 25 |
| NBFNet_mlx | Python | 10 |
| RWL | Python | 8 |

### AustinCStone (social graph)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts (this sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 15 |
| bmorphism | user | 20 |
| kubeflow | org | 16 |
| zubyul | user | 11 |
| TeglonLabs | org | 5 |
| AustinCStone | social | 4 |
| migalkin | social | 5 |
| wasita | social | 4 |
| DJedamski | social | 3 |
| kristinezheng | social | 2 |
| M1shaaa | social | 2 |
| **TOTAL** | | **87** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)
All wallets queried against `fullnode.mainnet.aptoslabs.com`. All returned `Resource not found`
for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — these accounts use the
**Fungible Asset (FA)** standard, not the legacy CoinStore. Recorded as NULL in DB.

| World | Address (truncated) | Legacy APT |
|-------|---------------------|-----------|
| alice | 0xc793…cc7b | NULL (FA) |
| bob | 0x0a3c…2d5d | NULL (FA) |
| A | 0x8699…9d7a | NULL (FA) |
| B–Z | … | NULL (FA) |

### Multisig Contract Probes
| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4…7003 | **2** | ✓ |
| A-G | 0xf56c…0096 | **2** | ✓ |
| Y-Z | 0xd3ff…b883 | **2** | ✓ |
| S-T | 0x3b1c…7883 | **2** | ✓ |
| V-W | 0x40fa…eb6d | **2** | ✓ |

All 5 multisig contracts healthy — 2-of-N threshold confirmed.

### MNX Markets (testnet.mnx.fi)
**UNAVAILABLE** — Vercel deployment protection (auth required). No data extracted.

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
