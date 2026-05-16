# World-Increment Sweep + Hamming Swarm Snapshot
**Timestamp:** 2026-05-16  
**GF(3) Color Chain:** id%3==0 → trit=0 ERGODIC #d3869b | id%3==1 → trit=1 PLUS #b8bb26 | id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept
| Source | Type | Repos Snapshotted |
|--------|------|------------------|
| plurigrid | org | 100 (22 sampled into increments) |
| kubeflow | org | 48 (16 sampled into increments) |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (zubyul graph) | 19 |
| wasita | user (zubyul graph) | 11 |
| kristinezheng | user (zubyul graph) | 6 |
| M1shaaa | user (zubyul graph) | 8 |
| AustinCStone | user (zubyul graph) | 30 |
| DJedamski | user (zubyul graph) | 6 |

### Top Repos by Stars (Current Snapshot)
| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,636 | — | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4,139 | Python | Machine Learning Pipelines for Kubeflow |
| kubeflow/spark-operator | 3,125 | Python | Kubernetes operator for Apache Spark |
| kubeflow/trainer | 2,098 | Go | Distributed AI Model Training on Kubernetes |
| kubeflow/katib | 1,682 | Python | Automated Machine Learning on Kubernetes |
| migalkin/NodePiece | 144 | Python | Compositional KG representations (ICLR'22) |
| migalkin/StarE | 89 | Python | Hyper-relational KG message passing (EMNLP 2020) |
| AustinCStone/TextGAN | 92 | Python | GAN for text generation in TensorFlow |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | OCaml SDK for Model Context Protocol |
| plurigrid/asi | 23 | HTML | everything is topological chemputer! |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | MCP server for epistemological claim analysis |

### Most Active (by Open Issues, current snapshot)
| Repo | Open Issues |
|------|------------|
| kubeflow/pipelines | 467 |
| kubeflow/sdk | 136 |
| kubeflow/katib | 122 |
| kubeflow/mpi-operator | 100 |
| plurigrid/gorj | 219 |
| bmorphism/Gay.jl | 188 |

### Notable Signals
- **plurigrid/gorj** (this repo!) pushed today 2026-05-16 — 219 open issues, active GF(3) development
- **bmorphism** has 100 repos, heavily MCP-server focused (say, babashka, manifold, nats, marginalia, penrose, penumbra, ocaml-mcp-sdk with 61 stars)
- **kubeflow** launched **mcp-apache-spark-history-server** (170 stars) — MCP expanding into MLOps tooling
- **zubyul** active 2026: nash-tui, nash-web, gay-world, voice-observatory — NASH token TUI + Gay.jl SPI colors
- **migalkin** focus: knowledge graphs (NodePiece 144★, StarE 89★, kgcourse2021 25★)
- **wasita** recently active: personal site + wm-cv pushed 2026-05-14
- **AustinCStone** recent: bmfork/bmforkupdate (bitmind forks), EpsteinSearch
- **M1shaaa** profile pushed today 2026-05-16 — actively maintained

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
All 28 Hamming swarm wallets queried via `fullnode.mainnet.aptoslabs.com`.

| World | Balance (APT) | Notes |
|-------|--------------|-------|
| alice | 0.0 | CoinStore resource absent |
| bob | 0.0 | CoinStore resource absent |
| A–Z (26 wallets) | 0.0 each | All accounts empty or uninitialized |

**Total APT across swarm: 0.0 APT**  
All 28 wallets returned 0 APT. The `CoinStore<AptosCoin>` resource was absent on all accounts, indicating they have never received APT on mainnet.

### Multisig Contract Probes
All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428...987003 | **2** | ✅ Healthy |
| A-G | 0xf56c4a1c...0096 | **2** | ✅ Healthy |
| Y-Z | 0xd3ffe181...b883 | **2** | ✅ Healthy |
| S-T | 0x3b1c3ae9...7883 | **2** | ✅ Healthy |
| V-W | 0x40fad7b4...eb6d | **2** | ✅ Healthy |

All 5 multisig contracts are live on Aptos mainnet with **2-of-N threshold**.

### MNX Markets (testnet.mnx.fi)
- Status: **UNAVAILABLE** — Next.js SPA, no public JSON API exposed
- Paths tried: `/api/markets`, `/api/v1/markets`, `/api/tickers` — all return SPA HTML shell
- No market data could be extracted without browser-side JavaScript execution

---

## DuckDB Schema (ducklake/world-increments.duckdb)
```sql
world_increments   -- GF(3) colored sweep log (id, trit, color, source)
repo_snapshots     -- GitHub repo state per sweep
aptos_snapshots    -- Hamming swarm wallet balances (timestamp, world, address, APT)
multisig_probes    -- Multisig contract sigs_required probes
mnx_snapshots      -- MNX market data (empty this sweep — SPA, no API)
```

### Current Row Counts (cumulative across all sweeps)
| Table | Rows |
|-------|------|
| world_increments | 137 |
| repo_snapshots | 1,058 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |
