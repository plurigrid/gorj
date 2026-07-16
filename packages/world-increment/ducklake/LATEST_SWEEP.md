# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-16

## Sweep Metadata
- **Date:** 2026-07-16
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (this sweep) | 42 |
| Total Repo Snapshots (this sweep) | 41 representative repos |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 (all healthy, 2/2 sigs) |
| MNX Markets | Unavailable (Vercel auth) |

---

## GF(3) Color Chain — This Sweep

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 21 |
| +1 | PLUS | `#b8bb26` | 22 |
| -1 | MINUS | `#cc241d` | 22 |

GF(3) chain: `ERGODIC → PLUS → MINUS → ERGODIC → ...` (42 increments, 14 full cycles)

---

## Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances — 28 addresses (alice, bob, A–Z)

All 28 Hamming swarm addresses queried against Aptos mainnet CoinStore resource.  
**Result:** 0 APT on all addresses — `0x1::coin::CoinStore<AptosCoin>` resource absent (accounts not funded or not yet initialized on mainnet).

### Multisig Contract Probes — 5 pairs

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f4... | 2 | ✅ healthy |
| A-G | 0xf56c4a... | 2 | ✅ healthy |
| Y-Z | 0xd3ffe1... | 2 | ✅ healthy |
| S-T | 0x3b1c3a... | 2 | ✅ healthy |
| V-W | 0x40fad7... | 2 | ✅ healthy |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Behind Vercel deployment protection. No market data retrieved.

---

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

## Notable Highlights (2026-07-16 sweep)
- **kubeflow/kubeflow**: 15,779 stars — flagship ML platform for Kubernetes (up from 15,565 in Apr)
- **kubeflow/pipelines**: 4,167 stars — most popular ML pipeline for Kubernetes (pushed 2026-07-16)
- **kubeflow/spark-operator**: 3,137 stars — Kubernetes operator for Apache Spark
- **bmorphism/Gay.jl**: active development — 187 open issues, wide-gamut GF(3) color library
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for Model Context Protocol (Jane Street oxcaml_effect)
- **migalkin/NodePiece**: 144 stars — scalable knowledge graph embeddings (ICLR'22)
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 30 stars (+14 since Apr) — topological chemputer (pushed 2026-07-10)
- **plurigrid/gorj**: 1204 open issues — this repo, active world-increment hub
- **Multisig health**: All 5 Hamming swarm multisigs (A-B, A-G, Y-Z, S-T, V-W) reporting 2/2 sigs, healthy
