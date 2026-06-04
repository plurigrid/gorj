# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-04

## Sweep Metadata
- **Date:** 2026-05-04
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (repo) | 137 |
| Total Repo Snapshots | 137 |
| Aptos Wallets Snapshotted | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances — 28 addresses (alice, bob, A–Z)

All 28 addresses returned **0.0 APT** — `CoinStore<AptosCoin>` resource not found on mainnet, indicating accounts have not received APT or CoinStore has not been initialized.

| Pair | Count | Total APT |
|---|---|---|
| alice, bob | 2 | 0.0 |
| A–Z (26 worlds) | 26 | 0.0 |
| **TOTAL** | **28** | **0.0 APT** |

### Multisig Contract Probes — 5 contracts

All 5 probed via `0x1::multisig_account::num_signatures_required`. All returned `2` (2-of-N), all **healthy**.

| Pair | Contract Address | Sigs Required | Healthy |
|---|---|---|---|
| A-B | `0x0da4f428a0c007da...` | 2 | ✓ |
| A-G | `0xf56c4a1c09062...` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b2df4...` | 2 | ✓ |
| S-T | `0x3b1c3ae905d44c...` | 2 | ✓ |
| V-W | `0x40fad7b423a843...` | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` responds with a **Next.js SPA** — no REST market data API accessible at common paths (`/api/markets`, `/api/v1/markets`). Recorded as `unavailable` in `mnx_snapshots`. Browser-side JS execution required to extract market data.

---

## GF(3) Color Chain — All 12 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 12 | bmorphism (org) | sweep_complete (gorj) | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

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
- **kubeflow/kubeflow**: 15,620 stars — flagship ML platform for Kubernetes (2026-05-04)
- **kubeflow/pipelines**: 4,132 stars — most popular ML pipeline for Kubernetes (pushed 2026-05-01)
- **kubeflow/spark-operator**: 3,123 stars — Kubernetes operator for Apache Spark
- **kubeflow/trainer**: 2,096 stars — Distributed AI Model Training (pushed 2026-05-01)
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings (ICLR 22)
- **migalkin/StarE**: 89 stars — hyper-relational knowledge graph message passing (EMNLP 20)
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs in TensorFlow
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **plurigrid/asi**: 17 stars — topological chemputer (pushed 2026-04-26)
- **plurigrid/gorj**: 57 open issues — forj + Rama topology nREPL routing + GF(3) coloring (this repo!)
- **bmorphism/Gay.jl**: 187 open issues — wide-gamut GF(3) color sampling (pushed 2026-05-04)
- **Hamming swarm**: 28 wallets (alice, bob, A–Z) all at 0 APT; 5 multisigs all requiring 2 sigs
