# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-23

## Sweep Metadata
- **Date:** 2026-06-23
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.2.2
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 87 |
| Total Repo Snapshots | 87 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 9 users |

---

## GF(3) Trit Distribution (June 2026 sweep)

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 28 |
| 1 | PLUS | `#b8bb26` | 30 |
| -1 | MINUS | `#cc241d` | 29 |

GF(3) assignment: `id mod 3 == 0` → ERGODIC · `id mod 3 == 1` → PLUS · `id mod 3 == 2` → MINUS

---

## Top Repos by Source (June 2026)

### plurigrid (100 repos)
| Repo | Language | Stars | Open Issues | Pushed At |
|------|----------|-------|-------------|-----------|
| gorj | Clojure | 0 | **768** | 2026-06-23 |
| eirobri | Clojure | 0 | 30 | 2026-06-23 |
| place | TeX | 1 | 9 | 2026-06-20 |
| asi | HTML | 26 | 4 | 2026-06-10 |
| nash-portal | Rust | 2 | 1 | 2026-05-19 |
| nanoclj-zig | Zig | 1 | 20 | 2026-04-25 |
| ontology | JavaScript | 8 | 16 | 2025-05-27 |

### kubeflow (48 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | **15,741** | 2026-06-18 |
| pipelines | Python | **4,157** | 2026-06-23 |
| spark-operator | Python | **3,128** | 2026-06-23 |
| trainer | Go | **2,119** | 2026-06-22 |
| katib | Python | 1,685 | 2026-06-23 |
| mcp-apache-spark-history-server | Python | 178 | 2026-06-23 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

### bmorphism (100 repos)
| Repo | Language | Stars | Open Issues | Pushed At |
|------|----------|-------|-------------|-----------|
| Gay.jl | Julia | 2 | **187** | 2026-06-23 |
| ocaml-mcp-sdk | OCaml | 61 | 0 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 1 | 2026-01-16 |
| oxgame | OCaml | 0 | 0 | 2026-05-15 |

### zubyul (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| voice-observatory | Python | 0 | 2026-04-24 |
| nash-tui | Rust | 0 | 2026-04-13 |
| gay-world | Python | 1 | 2026-03-26 |

### Social Graph (migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| migalkin/NodePiece | Python | 144 | 2022-02-02 |
| migalkin/StarE | Python | 89 | 2023-12-01 |
| migalkin/kgcourse2021 | HTML | 25 | 2025-08-04 |
| AustinCStone/TextGAN | Python | 92 | 2016-10-04 |
| wasita/wasita.github.io | Svelte | 1 | 2026-06-15 |
| M1shaaa/M1shaaa | — | 0 | **2026-06-23** (today!) |

---

## Hot Signals

- **plurigrid/gorj** — 768 open issues (highest in org), pushed today. Core active forj+Rama+GF(3) repo.
- **bmorphism/Gay.jl** — 187 open issues, pushed today. GF(3) deterministic color library is in heavy development.
- **kubeflow/mcp-apache-spark-history-server** (178★, Jun 2026) — new MCP-Spark integration; ML infra ↔ AI agent tooling convergence signal.
- **TeglonLabs/jank-crane** (C++, Jun 2026) — jank + crane converged-IR hub with GF3 convergence maps. New.
- **M1shaaa/M1shaaa** profile pushed **today (2026-06-23T14:40:59Z)** — active.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A–Z) returned **0.000000 APT**.  
The `0x1::coin::CoinStore<AptosCoin>` resource is not registered — these are unfunded/unactivated addresses on mainnet that have never received a transaction.

| World | Balance (APT) |
|-------|---------------|
| alice | 0.0 |
| bob | 0.0 |
| A–Z (26 worlds) | 0.0 each |

### Multisig Contract Probes (Mainnet) — ALL HEALTHY

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4f4...987003` | 2 | ✓ healthy |
| A-G | `0xf56c4a...c0096` | 2 | ✓ healthy |
| Y-Z | `0xd3ffe1...b883` | 2 | ✓ healthy |
| S-T | `0x3b1c3a...7883` | 2 | ✓ healthy |
| V-W | `0x40fad7...eb6d` | 2 | ✓ healthy |

All 5 multisig contracts respond to `0x1::multisig_account::num_signatures_required` and require **2-of-N** signatures.

### MNX Markets (testnet.mnx.fi)

- **Status:** HTTP 401 Unauthorized on both `https://testnet.mnx.fi/` and `/api/markets`
- **Conclusion:** testnet.mnx.fi requires auth (closed beta / internal testnet). No public market data available.

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
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,741 stars (+176 since Apr 2026) — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,157 stars — most popular ML pipeline for Kubernetes
- **kubeflow/spark-operator**: 3,128 stars — Kubernetes operator for Apache Spark
- **migalkin/NodePiece**: 144 stars — scalable knowledge graph embeddings (ICLR'22)
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for Model Context Protocol
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/gorj**: 768 open issues — this very repo, most active in plurigrid org today
- **All 5 multisig contracts HEALTHY** — 2-of-N sigs required, all responding on Aptos mainnet
