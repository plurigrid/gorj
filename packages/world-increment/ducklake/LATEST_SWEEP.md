# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-20

## Sweep Metadata
- **Date:** 2026-06-20
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** latest
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 24 (historical) |
| Repo Snapshots This Sweep | 381 |
| Total Repo Snapshots (historical) | 1325+ |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (Vercel auth) |

---

## GF(3) Color Chain — This Sweep (id 1–381)

| ID Range | GF3 Pattern | Color | Name |
|----------|-------------|-------|------|
| id%3==0 | trit=0 | `#d3869b` | **ERGODIC** |
| id%3==1 | trit=+1 | `#b8bb26` | **PLUS** |
| id%3==2 | trit=-1 | `#cc241d` | **MINUS** |

GF(3) chain cycles: `ERGODIC → PLUS → MINUS → ERGODIC → ...` (127 full cycles in 381 repos)

---

## Hamming Swarm — Aptos Mainnet Snapshot

All 28 addresses (alice, bob, A–Z) probed. **All return 0 APT** — addresses are infrastructure/wallet addresses that are not yet initialized with CoinStore resources on mainnet.

### Multisig Health

All 5 multisig pairs healthy, each requiring **2 signatures**:

| Pair | Address | Status |
|------|---------|--------|
| A-B | 0x0da4f428... | ✓ 2-of-n |
| A-G | 0xf56c4a1c... | ✓ 2-of-n |
| Y-Z | 0xd3ffe181... | ✓ 2-of-n |
| S-T | 0x3b1c3ae9... | ✓ 2-of-n |
| V-W | 0x40fad7b4... | ✓ 2-of-n |

### MNX Markets

`testnet.mnx.fi` returns HTTP 401 Vercel authentication gate for all endpoints. No market data available without Vercel credentials.

---

---

## Top Repos by Source (2026-06-20 sweep)

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 26 | 2026-06-10 |
| ontology | JavaScript | 8 | 2025-05-27 |
| vcg-auction | Rust | 7 | 2023-03-16 |
| agent | Python | 5 | 2023-03-31 |
| gorj | Clojure | 0 | 2026-06-20 ← today! (685 open issues) |

### kubeflow (48 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15736 | 2026-06-18 |
| pipelines | Python | 4154 | 2026-06-19 |
| spark-operator | Python | 3127 | 2026-06-18 |
| trainer | Go | 2117 | 2026-06-19 |
| mcp-apache-spark-history-server | Python | 177 | 2026-06-19 |

### TeglonLabs (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| jank-crane | C++ | 0 |
| coin-flip-mcp | JavaScript | 0 |

### bmorphism (100 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 61 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| risc0-cosmwasm-example | Rust | 23 |
| say-mcp-server | JavaScript | 20 |
| babashka-mcp-server | JavaScript | 19 |

### migalkin (19 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 25 |

### AustinCStone (30 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source (this sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 48 |
| zubyul | user | 49 |
| AustinCStone | user | 30 |
| migalkin | user | 19 |
| wasita | user | 11 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user | 5 |
| **TOTAL** | | **381** |

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
- **kubeflow/kubeflow**: 15,736 stars — flagship ML platform for Kubernetes (pushed 2026-06-18)
- **kubeflow/pipelines**: 4,154 stars — most popular ML pipeline for Kubernetes (pushed 2026-06-19)
- **kubeflow/spark-operator**: 3,127 stars — Kubernetes operator for Apache Spark (pushed 2026-06-18)
- **kubeflow/mcp-apache-spark-history-server**: 177 stars — new high-activity kubeflow repo (pushed 2026-06-19)
- **migalkin/NodePiece**: 144 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 26 stars — topological chemputer (pushed 2026-06-10)
- **plurigrid/gorj**: This very repo — 685 open issues, pushed today (2026-06-20)
- **Increment 24**: ERGODIC — sweep_complete closing the 8th full GF(3) cycle
- **Hamming Swarm**: All 28 Aptos addresses at 0 APT (uninitialized CoinStore); all 5 multisigs healthy at 2-of-n
- **MNX Markets**: Blocked by Vercel auth gate on testnet.mnx.fi — no market data this sweep
