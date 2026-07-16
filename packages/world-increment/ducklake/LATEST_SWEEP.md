# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-16

> Previous sweep: 2026-04-12 (471 repo snapshots, 12 world_increments)

---

## 2026-07-16 Sweep Metadata
- **Date:** 2026-07-16T13:30Z
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1 — GitHub Social Graph Sweep (2026-07-16)

### Sources Snapshotted This Run
| Source | Type | Repos Captured | Notable |
|--------|------|---------------|---------|
| plurigrid | org | 50 (103 total) | gorj 1201 issues, asi 30⭐ |
| kubeflow | org | 49 | kubeflow/kubeflow 15779⭐, pipelines 4167⭐ |
| TeglonLabs | org | 5 | jank-crane (C++), mathpix-gem 2⭐ |
| bmorphism | user | 50 (106 total) | Gay.jl 187 issues, ocaml-mcp-sdk 61⭐ |
| zubyul | user | 49 | voice-observatory, ghostel-emacs-worlds |
| migalkin | user (social) | 19 | NodePiece 144⭐, StarE 89⭐ |
| DJedamski | user (social) | 6 | data-science focus |
| wasita | user (social) | 11 | wasita.github.io active 2026-07 |
| kristinezheng | user (social) | 5 | cognitive science / web |
| M1shaaa | user (social) | 8 | cognitive/neuro lab work |
| AustinCStone | user (social) | 20 (41 total) | TextGAN 92⭐, byteruckus updated 2026-07-15 |

### Most Active plurigrid repos
- **gorj** — 1201 open issues, Clojure, pushed 2026-07-16 (this repo)
- **eirobri** — 30 open issues, Clojure, EiRoBri replay world
- **place** — 13 open issues, TeX, pushed 2026-07-14

### New since 2026-04-12
| Repo | Created | Lang |
|------|---------|------|
| bmorphism/gay-chat | 2026-07-14 | Scheme |
| AustinCStone/byteruckus | 2026-07-15 | HTML |
| bmorphism/bci-preview | 2026-06-19 | HTML |
| bmorphism/satreadout | 2026-06-10 | HTML |
| bmorphism/world | 2026-06-02 | Python |

---

## JOB 2 — Hamming Swarm Snapshot (Aptos Mainnet, 2026-07-16)

### Wallet Balances (alice, bob, A–Z) — 28 addresses
All queried via `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

**Result: All 28 wallets returned 0.0 APT** — CoinStore resource not found. Accounts may be unfunded, use a different coin type, or the resource path returns 404 on mainnet for these addresses.

### Multisig Contract Probes — 5 contracts
| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✅ |
| A-G | 0xf56c...096 | 2 | ✅ |
| Y-Z | 0xd3ff...883 | 2 | ✅ |
| S-T | 0x3b1c...883 | 2 | ✅ |
| V-W | 0x40fa...b6d | 2 | ✅ |

**5/5 multisig contracts healthy.** All require 2-of-N signatures (consistent with last sweep).

### MNX Markets (testnet.mnx.fi)
**UNAVAILABLE** — Vercel authentication required on all probed endpoints. No market data extractable without credentials.

---

## DuckDB State After This Sweep
| Table | Cumulative Rows |
|-------|----------------|
| world_increments | 108 |
| repo_snapshots | 1029 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

---

## Previous Sweep (2026-04-12) Summary

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 12 |
| Total Repo Snapshots | 471 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain — All 12 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 12 | bmorphism (org) | sweep_complete (gorj) | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

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
