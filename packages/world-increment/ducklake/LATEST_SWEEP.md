# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-24

## Sweep Metadata
- **Date:** 2026-07-24
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (This Run)

| Metric | Value |
|--------|-------|
| World Increments (this run) | 320 |
| Repo Snapshots (this run) | 320 |
| Sources Covered | 3 orgs + 8 users (11 total) |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| DB Total Increments (cumulative) | 343 |
| DB Total Repo Snapshots (cumulative) | 1,264 |

---

## GF(3) Color Chain Distribution (This Run)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 106 |
| +1 | `#b8bb26` | PLUS | 107 |
| -1 | `#cc241d` | MINUS | 107 |

GF(3) rule: `id mod 3 == 0 → ERGODIC`, `id mod 3 == 1 → PLUS`, `id mod 3 == 2 → MINUS`

---

## Top Repos by Source (2026-07-24 Snapshot)

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 16 | 2026-04-10 |
| ontology | JavaScript | 7 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-09 |
| zig-syrup | Zig | 2 | 2026-04-09 |
| vivarium | Clojure | 1 | 2026-04-08 |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15565+ | 2026 |
| pipelines | Python | 4119+ | 2026 |
| spark-operator | Python | 3111+ | 2026 |
| trainer | Go | 2080+ | 2026 |

### TeglonLabs (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| jank-crane | C++ | 0 | (pushed 2026-06-08, GF3 convergence maps)
| mathpix-gem | Ruby | 2 |
| coin-flip-mcp | JavaScript | 0 |

### bmorphism (100 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 60+ |
| anti-bullshit-mcp-server | JavaScript | 23+ |

### migalkin (19 repos — social graph)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 | (ICLR'22)
| StarE | Python | 89 | (EMNLP 2020)
| kgcourse2021 | HTML | 24 |
| NBFNet_mlx | Python | 10 |

### AustinCStone (41 repos — social graph)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| byteruckus | HTML | 0 | (pushed 2026-07-15, newest)

---

## Repo Counts by Source (This Run)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | user (social) | 41 |
| migalkin | user (social) | 19 |
| TeglonLabs | org | 5 |
| wasita | user (social) | 12 |
| M1shaaa | user (social) | 8 |
| DJedamski | user (social) | 6 |
| kristinezheng | user (social) | 5 |
| **TOTAL** | | **394 (API) / 320 (DB inserted)** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, mainnet)

All 28 addresses queried via `fullnode.mainnet.aptoslabs.com/v1`. All return resource-not-found for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — accounts appear unfunded or use non-native token stores.

**Total APT across swarm: 0.0 APT**

| Range | Status |
|-------|--------|
| alice, bob | 0.0 APT each |
| A through Z (26 addresses) | 0.0 APT each |

### Multisig Contract Health (5 pairs)

All 5 multisig contracts **healthy** — all require exactly 2 signatures.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...7003 | 2 | ✅ healthy |
| A-G | 0xf56c4a1c...0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ffe181...b883 | 2 | ✅ healthy |
| S-T | 0x3b1c3ae9...7883 | 2 | ✅ healthy |
| V-W | 0x40fad7b4...eb6d | 2 | ✅ healthy |

**All multisigs operational.** 5/5 pairs healthy with consistent 2-of-N threshold.

### MNX Markets (`testnet.mnx.fi`)

**Status: UNAVAILABLE (SPA only)** — `testnet.mnx.fi` serves a Next.js SPA. API endpoints `/api/markets` and `/api/v1/markets` return empty responses. No market data extractable from the frontend. `mnx_snapshots` table left empty this run.

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
