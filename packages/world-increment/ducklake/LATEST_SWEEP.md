# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-28

## Sweep Metadata
- **Date:** 2026-07-28
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 341 |
| Total Repo Snapshots (cumulative) | 1262 |
| New Increments This Sweep | 318 |
| Sources Covered | 3 orgs + 8 users (social graph) |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 pairs |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Scanned (2026-07-28)
| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 7 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social-graph | 19 |
| DJedamski | social-graph | 6 |
| wasita | social-graph | 12 |
| kristinezheng | social-graph | 5 |
| M1shaaa | social-graph | 8 |
| AustinCStone | social-graph | 20 |
| **TOTAL** | | **375 source records → 318 unique this sweep** |

### Notable Repos
- `TeglonLabs/jank-crane` (C++, pushed 2026-06-08) — GF3 convergence maps + loopify pass spec
- `migalkin/NodePiece` (Python, 144★) — scalable KG embeddings (ICLR'22), still active
- `migalkin/StarE` (Python, 89★) — hyper-relational KG (EMNLP 2020)
- `AustinCStone/TextGAN` (Python, 92★) — TensorFlow text GAN
- `wasita/wasita.github.io` (Svelte, updated 2026-07-21) — most recently pushed in social graph
- `bmorphism` — 100 repos captured; heavy MCP/AI tooling focus

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)
All 28 addresses returned **HTTP 404** for `CoinStore<AptosCoin>` on Aptos mainnet. Wallets are **unfunded / no on-chain APT balance** (accounts not registered or never received APT).

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793ac... | NULL (no CoinStore) |
| bob | 0x0a3c00... | NULL (no CoinStore) |
| A–Z (26 wallets) | various | NULL (no CoinStore) |

### Multisig Contract Probes
Probed `0x1::multisig_account::num_signatures_required` — all 5 contracts responded successfully.

| Pair | Contract | Sigs Required | Status |
|------|----------|---------------|--------|
| A-B | 0x0da4f428... | **2** | ✅ healthy |
| A-G | 0xf56c4a1c... | **2** | ✅ healthy |
| Y-Z | 0xd3ffe181... | **2** | ✅ healthy |
| S-T | 0x3b1c3ae9... | **2** | ✅ healthy |
| V-W | 0x40fad7b4... | **2** | ✅ healthy |

**All 5 multisig contracts: 2-of-2 threshold, all healthy.**

### MNX Markets (testnet.mnx.fi)
`/api/markets`, `/api/v1/markets`, `/api/tickers` — all **HTTP 404**. MNX testnet is a SPA; no accessible REST API at standard paths. Recorded as UNAVAILABLE.

---

## GF(3) Color Distribution (2026-07-28 sweep, 318 new increments)
- trit=0 ERGODIC #d3869b: ~106 increments (id%3==0)
- trit=1 PLUS #b8bb26: ~106 increments (id%3==1)
- trit=-1 MINUS #cc241d: ~106 increments (id%3==2)

GF(3) assignment: `id mod 3 == 0 → ERGODIC | id mod 3 == 1 → PLUS | id mod 3 == 2 → MINUS`

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
