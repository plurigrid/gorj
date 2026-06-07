# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-07

## Sweep Metadata
- **Date:** 2026-06-07
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 275 |
| Total Repo Snapshots | 275 |
| Aptos Wallet Snapshots | 28 |
| Multisig Probes | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain Distribution (275 increments)

| GF3 Trit | Name | Color | Count |
|----------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 91 |
| 1 | PLUS | `#b8bb26` | 92 |
| 2 | MINUS | `#cc241d` | 92 |

Chain cycles: `ERGODIC → PLUS → MINUS` repeating across all 275 world-increment events.

---

## Top Repos by Source

### plurigrid (100 repos snapshotted)
| Repo | Language | Stars | Open Issues | Last Push |
|------|----------|-------|-------------|-----------|
| gorj | Clojure | 0 | **411** | 2026-06-07 |
| asi | HTML | 25 | 4 | 2026-04-26 |
| eirobri | Clojure | 0 | 29 | 2026-06-03 |
| ontology | JavaScript | 8 | 16 | 2025-05-27 |
| vcg-auction | Rust | 7 | 1 | 2023-03-16 |

### kubeflow (22 repos snapshotted)
| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow | — | 15706 | 2026-05-24 |
| pipelines | Python | 4153 | 2026-06-06 |
| spark-operator | Python | 3125 | 2026-06-04 |
| trainer | Go | 2112 | 2026-06-05 |
| katib | Python | 1685 | 2026-06-05 |

### bmorphism (100 repos snapshotted)
| Repo | Language | Stars | Open Issues | Last Push |
|------|----------|-------|-------------|-----------|
| Gay.jl | Julia | 1 | **189** | 2026-06-07 |
| ocaml-mcp-sdk | OCaml | 61 | 0 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 1 | 2026-01-16 |
| say-mcp-server | JavaScript | 20 | 3 | 2025-01-07 |
| babashka-mcp-server | JavaScript | 19 | 3 | 2025-01-05 |

### zubyul (18 repos snapshotted)
| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| voice-observatory | Python | 0 | 2026-04-24 |
| nash-tui | Rust | 0 | 2026-04-13 |
| tilelang-kernels | Python | 0 | 2026-03-16 |
| WGCNA | HTML | 2 | 2023-07-05 |

### migalkin (6 repos snapshotted)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 25 |

### AustinCStone (7 repos snapshotted)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source (This Sweep)

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 22 |
| zubyul | user | 18 |
| AustinCStone | user | 7 |
| migalkin | user | 6 |
| wasita | user | 6 |
| TeglonLabs | org | 4 |
| kristinezheng | user | 4 |
| DJedamski | user | 4 |
| M1shaaa | user | 4 |
| **TOTAL** | | **275** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-06-07)

All 28 wallets queried (alice, bob, A–Z) via `fullnode.mainnet.aptoslabs.com`. All returned **0.0 APT** — accounts have no APT in `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at snapshot time.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z (26 wallets) | 0x8699...→ 0x7af0... | 0.0 each |

**Total APT across swarm: 0.0**

### Multisig Contract Probes

All 5 multisig contracts returned `num_signatures_required = 2`. All **healthy**.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✅ |
| A-G | 0xf56c...096 | 2 | ✅ |
| Y-Z | 0xd3ff...883 | 2 | ✅ |
| S-T | 0x3b1c...883 | 2 | ✅ |
| V-W | 0x40fa...b6d | 2 | ✅ |

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — HTTP 401 Unauthorized on both `/api/markets` and root. No market data retrievable without credentials. `mnx_snapshots` table has 0 rows.

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
- **kubeflow/kubeflow**: 15,706 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,153 stars — most popular ML pipeline for Kubernetes (pushed 2026-06-06)
- **kubeflow/spark-operator**: 3,125 stars — Kubernetes operator for Apache Spark
- **plurigrid/gorj**: 411 open issues — this very repo, most active in plurigrid org
- **bmorphism/Gay.jl**: 189 open issues — wide-gamut GF(3) color sampling, pushed 2026-06-07
- **migalkin/NodePiece**: 144 stars — compositional knowledge graph representations (ICLR'22)
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 25 stars — everything is topological chemputer
- **Hamming swarm**: 5/5 multisig contracts healthy, all requiring 2-of-N threshold
- **Increment 275**: MINUS — sweep spans 91 ERGODIC + 92 PLUS + 92 MINUS across all sources
