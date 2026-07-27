# World-Increment Sweep — 2026-07-27

## Sweep Metadata
- **Date:** 2026-07-27
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 34 |
| Total Repo Snapshots (cumulative) | 1019 |
| Sources Covered This Run | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — This Run's Increments

| Source | Type | GF3 Trit | Color | Name |
|--------|------|-----------|-------|------|
| plurigrid | org | +1 | `#b8bb26` | **PLUS** |
| kubeflow | org | -1 | `#cc241d` | **MINUS** |
| TeglonLabs | org | 0 | `#d3869b` | **ERGODIC** |
| bmorphism | user | +1 | `#b8bb26` | **PLUS** |
| zubyul | user | -1 | `#cc241d` | **MINUS** |
| migalkin | user | 0 | `#d3869b` | **ERGODIC** |
| wasita | user | +1 | `#b8bb26` | **PLUS** |
| AustinCStone | user | -1 | `#cc241d` | **MINUS** |
| DJedamski | user | 0 | `#d3869b` | **ERGODIC** |
| kristinezheng | user | +1 | `#b8bb26` | **PLUS** |
| M1shaaa | user | -1 | `#cc241d` | **MINUS** |

GF(3) rule: `id mod 3 == 0 → ERGODIC #d3869b · id mod 3 == 1 → PLUS #b8bb26 · id mod 3 == 2 → MINUS #cc241d`

### Top Repos by Source (July 2026 Snapshot)

#### plurigrid (103 repos total)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 47 | 2026-07-10 |
| gorj | Clojure | 1 | 2026-07-26 |
| eirobri | Clojure | 0 | 2026-07-21 |
| ontology | JavaScript | 8 | 2025-05-27 |
| vcg-auction | Rust | 7 | 2023-03-16 |

#### kubeflow (49 repos total)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,792 | 2026-07-10 |
| pipelines | Python | 4,169 | 2026-07-26 |
| spark-operator | Python | 3,142 | 2026-07-25 |
| trainer | Go | 2,154 | 2026-07-26 |
| katib | Python | 1,692 | 2026-07-26 |
| examples | Jsonnet | 1,461 | 2025-04-14 |

#### TeglonLabs (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| jank-crane | C++ | 0 |
| coin-flip-mcp | JavaScript | 0 |

#### bmorphism (100 of 106 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 61 |
| risc0-cosmwasm-example | Rust | 23 |
| anti-bullshit-mcp-server | JavaScript | 22 |
| say-mcp-server | JavaScript | 20 |
| babashka-mcp-server | JavaScript | 19 |
| Gay.jl | Julia | 2 |

#### zubyul (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| from-possible-worlds | TeX | 0 | 2026-07-18 |
| voice-observatory | Python | 0 | 2026-04-24 |
| nash-tui | Rust | 0 | 2026-04-13 |
| gay-world | Python | 1 | 2026-03-26 |

#### migalkin (19 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 24 |
| RWL | Python | 8 |

#### wasita (12 repos) — pushed 2026-07-21
| Repo | Language | Stars |
|------|----------|-------|
| wasita.github.io | Svelte | 1 |
| magic-garden | Python | 2 |

#### AustinCStone (41 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| byteruckus | HTML | 0 |

#### zubyul social graph (DJedamski, kristinezheng, M1shaaa)
- **DJedamski**: 6 repos — Coursera/Kaggle data science (2014–2018, dormant)
- **kristinezheng**: 5 repos — MIT/Harvard neuroscience tools, personal site pushed 2026-07-01
- **M1shaaa**: 8 repos — Lookit study tools, MNIST, TypeScript bookshelf (2023–2026)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

28 addresses queried via `fullnode.mainnet.aptoslabs.com`. All balances = **0.0 APT** (CoinStore not initialized on mainnet for these addresses).

| Worlds | Status |
|--------|--------|
| alice, bob | 0.0 APT |
| A through Z (26 addresses) | 0.0 APT each |

### Multisig Contract Probes

| Pair | Address (short) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | HEALTHY |
| A-G | 0xf56c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY |
| S-T | 0x3b1c...7883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

All 5 multisig contracts healthy with 2-of-N threshold.

### MNX Markets (testnet.mnx.fi)

Testnet responds as Next.js SPA. REST API paths (/api/markets, /api/tickers, /api/v1/markets) return SPA HTML, not JSON. Market data unavailable without browser JS execution.

---

## Schema Reference

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

---

## Notable Highlights (2026-07-27)

- kubeflow/kubeflow: 15,792 stars — flagship ML platform for Kubernetes
- kubeflow/pipelines: 4,169 stars — pushed 2026-07-26, 464 open issues
- plurigrid/gorj: This very repo — 1,426 open issues (issues-as-notes board)
- bmorphism/ocaml-mcp-sdk: 61 stars — OCaml MCP SDK with Jane Street oxcaml_effect
- AustinCStone/TextGAN: 92 stars — TF text generation GAN (2016, still referenced)
- migalkin/NodePiece: 144 stars — ICLR'22 knowledge graph embeddings
- TeglonLabs/jank-crane: new in 2026 — C++ GF3 convergence maps / IR hub
- Multisigs A-B, A-G, Y-Z, S-T, V-W: all healthy at 2-of-N threshold

*Generated by world-increment-sweep + hamming-swarm-snapshot on 2026-07-27*
