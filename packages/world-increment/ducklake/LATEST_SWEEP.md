# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-03

## Sweep Metadata
- **Date:** 2026-07-03
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 24 |
| Total Repo Snapshots | 1335 |
| Sources Covered | 3 orgs + 8 users (GitHub sweep) |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Market Snapshots | 0 (auth required) |

---

## GF(3) Color Chain — Increments 13–24 (this sweep)

GF(3) rule: `id%3==0` → ERGODIC #d3869b · `id%3==1` → PLUS #b8bb26 · `id%3==2` → MINUS #cc241d

This run added increment id=24 (ERGODIC #d3869b) for the consolidated multi-org GitHub sweep.

Cumulative chain (ids 1–24): 8 PLUS · 8 MINUS · 8 ERGODIC — balanced GF(3) sequence.

---

## JOB 2: Hamming Swarm Snapshot (2026-07-03)

### Aptos Wallet Balances (28 addresses)

All 28 Hamming-swarm addresses probed against Aptos mainnet fullnode.

**Result:** All return `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
Accounts exist on-chain but no APT CoinStore has been initialized / no balance. Recorded as NULL.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793ac...4cc7b | null |
| bob | 0x0a3c00...512d5d | null |
| A | 0x8699ed...9d7a | null |
| B | 0x3f892e...cb13 | null |
| C | 0x38b99e...535e | null |
| D | 0xf77656...fdd1 | null |
| E | 0xdc1d9d...8d36 | null |
| F | 0x18a14b...f71 | null |
| G | 0x69a394...f32 | null |
| H | 0xce67c3...300f | null |
| I | 0x070fe5...1fc9 | null |
| J | 0x4d964d...f54 | null |
| K | 0xa73204...dc4 | null |
| L | 0x7c2eae...ba9 | null |
| M | 0x6fed37...f2e9 | null |
| N | 0xe7dde6...1b2c | null |
| O | 0x73252b...a89d | null |
| P | 0x621879...948 | null |
| Q | 0xac40fa...89a9 | null |
| R | 0x7ce605...6e10 | null |
| S | 0xb87530...386 | null |
| T | 0x357819...588 | null |
| U | 0x75860d...956 | null |
| V | 0xb59dd8...f2c3 | null |
| W | 0x5f32ae...b0 | null |
| X | 0xa95cbb...47d | null |
| Y | 0xd8e328...44c4 | null |
| Z | 0x7af0ef...97c | null |

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f4...003 | 2 | ✓ |
| A-G | 0xf56c4a...096 | 2 | ✓ |
| Y-Z | 0xd3ffe1...883 | 2 | ✓ |
| S-T | 0x3b1c3a...883 | 2 | ✓ |
| V-W | 0x40fad7...b6d | 2 | ✓ |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed.**

### MNX Testnet Markets

`testnet.mnx.fi` is Vercel-protected (HTTP 401, visitor password required). No market data accessible without credentials. `mnx_snapshots` table: 0 rows.

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

## Repo Counts by Source (cumulative DB: 1335 rows)

### This Sweep (391 new repos)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 48 |
| zubyul | user | 49 |
| AustinCStone | user | 40 |
| wasita | user | 11 |
| migalkin | user | 19 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| kristinezheng | user | 5 |
| TeglonLabs | org | 5 |
| **TOTAL** | | **391** |

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
