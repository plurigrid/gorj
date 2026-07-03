# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-03

## Sweep Metadata
- **Date:** 2026-07-03
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (This Sweep)

| Metric | Value |
|--------|-------|
| New World Increments | 170 |
| New Repo Snapshots | 170 |
| Total (all-time) Increments | 193 |
| Total (all-time) Repo Snapshots | 1114 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 |
| Multisig Pairs Probed | 5 |

---

## GF(3) Color Chain (2026-07-03 Sweep)

GF(3) rule: `id%3==0` → trit=0 ERGODIC #d3869b | `id%3==1` → trit=1 PLUS #b8bb26 | `id%3==2` → trit=-1 MINUS #cc241d

Pattern repeats: ERGODIC → PLUS → MINUS → ERGODIC → … (57 full cycles across 170 new increments)

---

## Top Repos by Source (2026-07-03 Snapshot)

### plurigrid (103 repos, 100 captured)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 28 | 2026-06-29 |
| ontology | JavaScript | 8 | 2025-05-27 |
| vcg-auction | Rust | 7 | 2023-03-16 |
| agent | Python | 5 | 2023-03-31 |
| StochFlow | Python | 4 | 2024-03-20 |
| gorj | Clojure | 0 | 2026-07-03 |
| shrimp | — | 0 | 2026-07-03 |
| eirobri | Clojure | 0 | 2026-06-30 |

### kubeflow (48 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,760 | 2026-06-18 |
| pipelines | Python | 4,167 | 2026-07-03 |
| spark-operator | Python | 3,132 | 2026-07-02 |
| trainer | Go | 2,129 | 2026-07-02 |
| katib | Python | 1,688 | 2026-07-01 |
| mcp-apache-spark-history-server | Python | 179 | 2026-06-25 |
| mcp-server | Python | 19 | 2026-06-29 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| jank-crane | C++ | 0 | 2026-06-08 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

### bmorphism (105 repos, 100 captured)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| risc0-cosmwasm-example | Rust | 23 | 2022-10-20 |
| say-mcp-server | JavaScript | 20 | 2025-01-07 |
| babashka-mcp-server | JavaScript | 19 | 2025-01-05 |
| Gay.jl | Julia | 2 | 2026-07-03 |

### zubyul (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| WGCNA | HTML | 2 | 2023-07-05 |
| gay-world | Python | 1 | 2026-03-26 |
| send2kobo | TypeScript | 1 | 2026-05-19 |

### migalkin (19 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| NodePiece | Python | 144 | 2026-05-07 |
| StarE | Python | 89 | 2026-04-16 |
| kgcourse2021 | HTML | 25 | 2026-02-16 |
| NBFNet_mlx | Python | 10 | 2026-03-11 |
| RWL | Python | 8 | 2026-05-28 |

### AustinCStone (40 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| TextGAN | Python | 92 | 2025-03-03 |
| StereoVisionMRF | Python | 11 | 2026-04-01 |
| SpectralClustering | Python | 3 | 2021-04-16 |

---

## Repo Counts by Source (2026-07-03)

| Source | Type | Repos (this sweep) |
|--------|------|---------------------|
| plurigrid | org | 100 (of 103) |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 (of 105) |
| zubyul | user | 49 |
| migalkin | social | 19 |
| AustinCStone | social | 40 |
| wasita | social | 11 |
| DJedamski | social | 6 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| **TOTAL** | | **170** new |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

All probed via `fullnode.mainnet.aptoslabs.com`. CoinStore resource returned 0 APT for all
addresses — accounts exist on-chain but the AptosCoin CoinStore not initialized with funded balance.

### Multisig Contract Probes (5 pairs)

All 5 healthy — each requires 2 signatures:

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...03 | 2 | ✓ healthy |
| A-G | 0xf56c...96 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...83 | 2 | ✓ healthy |
| S-T | 0x3b1c...83 | 2 | ✓ healthy |
| V-W | 0x40fa...6d | 2 | ✓ healthy |

### MNX Markets

`testnet.mnx.fi` — Vercel auth-gated SPA. Market data unavailable without auth token.

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

## Notable Highlights (2026-07-03)
- **kubeflow/pipelines**: Pushed 2026-07-03 — 4,167★, 412 open issues, actively maintained
- **kubeflow/mcp-server** (19★) and **mcp-apache-spark-history-server** (179★): Kubeflow integrating MCP
- **bmorphism/Gay.jl**: 187 open issues, pushed 2026-07-03 — very active Julia color SPI library
- **plurigrid/gorj**: 937 open issues, pushed 2026-07-03 — this repo
- **plurigrid/shrimp**: New Jank worked example, pushed today 2026-07-03
- **TeglonLabs/jank-crane**: C++ crane-jank converged-IR hub with GF3 convergence maps (Jun 2026)
- **migalkin/NodePiece**: 144★ ICLR'22 knowledge graph embeddings, still growing
- **All 5 multisig pairs**: 2-of-N threshold confirmed healthy on Aptos mainnet
- **Prior sweep** (2026-04-12): 471 repo snapshots archived in ducklake
