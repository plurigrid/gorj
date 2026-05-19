# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-29

## Sweep Metadata
- **Date:** 2026-04-29
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 34 (+11 this sweep, ids 13–23) |
| Total Repo Snapshots | 1333 (+389 this sweep) |
| Sources Covered | 3 orgs + 8 users (social graph) |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 (all healthy) |

---

## JOB 1: GitHub Social Graph Sweep — New Increments (ids 13–23)

| ID | Source | Type | GF3 Trit | Color | Repos |
|----|--------|------|-----------|-------|-------|
| 13 | plurigrid | org | +1 | `#b8bb26` PLUS | 100 |
| 14 | kubeflow | org | -1 | `#cc241d` MINUS | 47 |
| 15 | TeglonLabs | org | 0 | `#d3869b` ERGODIC | 4 |
| 16 | bmorphism | user | +1 | `#b8bb26` PLUS | 100 |
| 17 | zubyul | user | -1 | `#cc241d` MINUS | 49 |
| 18 | migalkin | user | 0 | `#d3869b` ERGODIC | 19 |
| 19 | DJedamski | user | +1 | `#b8bb26` PLUS | 6 |
| 20 | wasita | user | -1 | `#cc241d` MINUS | 10 |
| 21 | kristinezheng | user | 0 | `#d3869b` ERGODIC | 6 |
| 22 | M1shaaa | user | +1 | `#b8bb26` PLUS | 8 |
| 23 | AustinCStone | user | -1 | `#cc241d` MINUS | 40 |

GF(3) chain continues: `…MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

### Notable Activity (2026-04-29 sweep)
- **wasita/wasita.github.io** — Svelte personal site pushed 2026-04-28 (yesterday)
- **M1shaaa/M1shaaa** — profile config repo pushed 2026-04-29 (today)
- **TeglonLabs/mathpix-gem** — Ruby math OCR gem (11 open issues)
- **plurigrid** org snapshot refreshed: 100 repos across AI/energy/coordination research
- **bmorphism**: 100 repos — plurigrid ecosystem, ocaml-mcp-sdk (60★), anti-bullshit-mcp-server (23★)

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (28 addresses: alice, bob, A–Z)

All 28 addresses queried against Aptos mainnet `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
**All returned `resource_not_found`** — accounts unfunded/uninitialized on mainnet at ledger ~5047247582.
Balance recorded as **0.0 APT** for each.

### Multisig Contract Probes — ALL HEALTHY

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428a0c007… | 2 | ✓ healthy |
| A-G | 0xf56c4a1c090621… | 2 | ✓ healthy |
| Y-Z | 0xd3ffe1812b2df4… | 2 | ✓ healthy |
| S-T | 0x3b1c3ae905d44c… | 2 | ✓ healthy |
| V-W | 0x40fad7b423a843… | 2 | ✓ healthy |

All 5 contracts use 2-of-2 multisig scheme and are live on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` is a Next.js SPA. No public REST API endpoints found — market data **unavailable** via direct API probe. mnx_snapshots table empty this sweep.

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
