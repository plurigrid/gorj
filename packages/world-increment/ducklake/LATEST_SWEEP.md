# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-14

## Sweep Metadata
- **Date:** 2026-07-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 349 |
| Total Repo Snapshots | 349 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | Unavailable (401 Unauthorized) |

---

## GF(3) Color Chain (per-repo assignment, 349 total increments)

**Rule:** `id mod 3 == 1` → PLUS `#b8bb26` | `id mod 3 == 2` → MINUS `#cc241d` | `id mod 3 == 0` → ERGODIC `#d3869b`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| wasita | user | 11 |
| AustinCStone | user | 10 |
| M1shaaa | user | 8 |
| migalkin | user | 6 |
| DJedamski | user | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user | 5 |
| **TOTAL** | | **349** |

### Top Repos by Source

#### plurigrid (100 repos) — pushed 2026-07-14
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 30 | 2026-07-10 |
| gorj | Clojure | 1 | 2026-07-14 |
| ontology | JavaScript | 8 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-26 |
| microworlds | Rust | 3 | 2023-05-13 |

#### kubeflow (49 repos) — active ML platform
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,777 | 2026-07-10 |
| pipelines | Python | 4,166 | 2026-07-14 |
| spark-operator | Python | 3,136 | 2026-07-14 |
| trainer | Go | 2,143 | 2026-07-14 |
| katib | Python | 1,690 | 2026-07-14 |
| mcp-apache-spark-history-server | Python | 182 | 2026-07-14 |

#### bmorphism (100 repos) — pushed 2026-07-14
| Repo | Language | Stars |
|------|----------|-------|
| Gay.jl | Julia | 2 |
| gay-chat | Scheme | 0 |
| satreadout | HTML | 0 |

#### zubyul (49 repos) — zubyul social graph
| Repo | Language | Stars |
|------|----------|-------|
| gay-world | Python | 1 |
| zubyul.github.io | CSS | 1 |
| nash-tui | Rust | 0 |

#### migalkin (6 featured, 19 total) — knowledge graph research
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 24 |
| NBFNet_mlx | Python | 10 |

#### AustinCStone (10 featured, 40 total) — ML/CV research
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-07-14)

Queried via `0x1::coin::balance` view function (legacy CoinStore endpoint returns 404 — accounts use FA standard).

| World | Balance (APT) |
|-------|--------------|
| bob | 12.65700700 |
| F | 1.96051600 |
| L | 1.92726900 |
| J | 1.89509300 |
| alice | 0.43643352 |
| O | 0.21013600 |
| K | 0.16196100 |
| P | 0.14013600 |
| M | 0.11228500 |
| N | 0.10612100 |
| Q | 0.10324000 |
| S | 0.09178800 |
| R | 0.09021700 |
| T | 0.07371300 |
| U | 0.05577300 |
| A | 0.05176700 |
| Y | 0.04444900 |
| V | 0.04883299 |
| X | 0.04257700 |
| W | 0.04070500 |
| B | 0.03625600 |
| Z | 0.02426800 |
| D | 0.01162900 |
| C | 0.01018500 |
| E | 0.00937200 |
| H | 0.00168100 |
| G | 0.00068100 |
| I | 0.00068100 |

**Total swarm balance: ~21.15 APT**

### Multisig Contract Probes (0x1::multisig_account::num_signatures_required)

All 5 contracts healthy — 2-of-2 signatures required.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428... | 2 | ✅ Healthy |
| A-G | 0xf56c4a1c... | 2 | ✅ Healthy |
| Y-Z | 0xd3ffe181... | 2 | ✅ Healthy |
| S-T | 0x3b1c3ae9... | 2 | ✅ Healthy |
| V-W | 0x40fad7b4... | 2 | ✅ Healthy |

### MNX Markets (testnet.mnx.fi)

API returned HTTP 401 Unauthorized on all probed endpoints — no market data available without credentials.

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
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC

## Notable Highlights
- **kubeflow/kubeflow**: 15,777 stars (+212 vs Apr sweep) — ML platform for Kubernetes
- **kubeflow/pipelines**: 4,166 stars — ML pipelines, pushed 2026-07-14
- **kubeflow/spark-operator**: 3,136 stars — pushed 2026-07-14
- **migalkin/NodePiece**: 144 stars — Knowledge Graph embeddings (ICLR'22)
- **AustinCStone/TextGAN**: 92 stars — GAN for text generation
- **plurigrid/asi**: 30 stars (+14 since Apr) — topological chemputer
- **Hamming swarm leader**: bob (12.66 APT), F (1.96 APT), L (1.93 APT), J (1.90 APT)
- **All 5 multisig contracts healthy**: 2-of-2 threshold maintained across A-B, A-G, Y-Z, S-T, V-W
