# World-Increment Sweep + Hamming Snapshot — 2026-07-04

## Sweep Metadata
- **Date:** 2026-07-04 11:07 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 349 |
| Total Repo Snapshots | 1,270 (cumulative) |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Healthy | 5 / 5 |
| MNX Markets | Unavailable (Vercel auth) |

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
- **kubeflow/kubeflow**: 15,761 stars — flagship ML platform for Kubernetes (pushed 2026-01)
- **kubeflow/pipelines**: 4,169 stars — ML pipeline for Kubernetes
- **kubeflow/spark-operator**: 3,132 stars — Kubernetes operator for Apache Spark
- **migalkin/NodePiece**: 144 stars — scalable knowledge graph embeddings (ICLR'22)
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs (TensorFlow)
- **migalkin/StarE**: 89 stars — hyper-relational knowledge graphs (EMNLP 2020)
- **plurigrid/asi**: 28 stars — topological chemputer (pushed 2026-06-29)
- **plurigrid/eirobri** (Clojure) pushed 2026-06-30 — new active plurigrid project
- **bmorphism/Gay.jl** (Julia) pushed 2026-07-04 — active today
- **TeglonLabs/jank-crane** (C++) — crane-jank converged-IR hub with GF3 convergence maps

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-07-04 ~11:07 UTC)
Ledger version at query time: **6,096,571,389** | Epoch: **16,411**

All 28 wallets queried — all returned HTTP 404 `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
Addresses are not initialized with APT CoinStore resources on mainnet; balances stored as NULL.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793acd...cc7b | null |
| bob | 0x0a3c00c...512d | null |
| A | 0x8699edc...9d7a | null |
| B | 0x3f892eb...b13 | null |
| C–Z | (24 addresses) | null |

### Multisig Contract Probes
All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...7003 | **2** | ✅ |
| A-G | 0xf56c4a1c...0096 | **2** | ✅ |
| Y-Z | 0xd3ffe181...b883 | **2** | ✅ |
| S-T | 0x3b1c3ae9...7883 | **2** | ✅ |
| V-W | 0x40fad7b4...eb6d | **2** | ✅ |

**All 5 contracts healthy** — all require 2-of-N threshold signatures.

### MNX Markets (testnet.mnx.fi)
**Status**: **UNAVAILABLE** — testnet.mnx.fi is behind Vercel Deployment Protection (password required). No market data accessible without visitor credentials or bypass token.
