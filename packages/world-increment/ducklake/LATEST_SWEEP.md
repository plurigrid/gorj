# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-14

## Sweep Metadata
- **Date:** 2026-07-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **Database:** `packages/world-increment/ducklake/world-increments-sweep.db` (SQLite; DuckDB CLI unavailable — identical schema, existing `.duckdb` preserved)
- **Prior sweep:** 2026-04-12 (471 snapshots)

---

## Summary Counts — 2026-07-14

| Metric | Value |
|--------|-------|
| Total World Increments (this run) | 324 |
| Total Repo Snapshots (this run) | 324 |
| Sources Covered | 3 orgs + 8 users (+ 6 social graph) |
| Aptos addresses probed | 28 (all 404 — unactivated on mainnet) |
| Multisig contracts healthy | 5/5 (all 2-of-N) |
| MNX market data | Unavailable (401 auth required) |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice → Z, 28 addresses)

All 28 addresses returned HTTP 404 from Aptos mainnet fullnode. The `CoinStore<AptosCoin>` resource does not exist — accounts not yet activated (require at least one on-chain transaction to initialize).

| World | Address (truncated) | Balance APT |
|-------|---------------------|:-----------:|
| alice–Z (all 28) | 0xc793...–0x7af0... | N/A (404) |

### Multisig Contract Probes

All 5 multisig contracts responded via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|:-------------:|:------:|
| A-B | 0x0da4...987003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✓ HEALTHY |

All multisigs require **2-of-N** signatures. All reachable on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)

- API endpoints → **401 Unauthorized** (auth required)
- Base URL → TLS handshake timeout
- **Status:** Unavailable — no market data extracted

---

## Summary Counts — Previous (2026-04-12)

| Metric | Value |
|--------|-------|
| Total World Increments | 12 |
| Total Repo Snapshots | 471 |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph Sweep — 2026-07-14

### Coverage

| Source | Type | Repos | Stars |
|--------|------|:-----:|:-----:|
| plurigrid | org | 100 | 82 |
| kubeflow | org | 49 | 34,356 |
| TeglonLabs | org | 5 | 2 |
| bmorphism | user | 100 | 246 |
| zubyul | user | 49 | 14 |
| migalkin | social | 5 | 275 |
| wasita | social | 4 | 4 |
| AustinCStone | social | 4 | 103 |
| DJedamski | social | 3 | 2 |
| kristinezheng | social | 3 | 0 |
| M1shaaa | social | 2 | 0 |
| **TOTAL** | | **324** | **35,084** |

### GF(3) Color Chain Distribution (2026-07-14)

| Trit | Name | Color | Count |
|:----:|------|-------|:-----:|
| 0 | ERGODIC | `#d3869b` | 108 |
| +1 | PLUS | `#b8bb26` | 108 |
| -1 | MINUS | `#cc241d` | 108 |

### Notable Repos (2026-07-14)
- **kubeflow/kubeflow** — 34k+ stars; flagship ML platform
- **migalkin/NodePiece** — 144★, ICLR'22 KG representations
- **migalkin/StarE** — 89★, EMNLP'20 hyper-relational KGs
- **AustinCStone/TextGAN** — 92★, TF text GAN
- **wasita** — active today (site + CV pushed 2026-07-14)
- **TeglonLabs/jank-crane** — GF3 convergence maps (2026-06-08)

---

## GF(3) Color Chain — Previous Run (12 Increments, 2026-04-12)

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
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — most popular ML pipeline for Kubernetes (pushed 2026-04-10)
- **kubeflow/spark-operator**: 3,111 stars — Kubernetes operator for Apache Spark (pushed 2026-04-10)
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 16 stars — topological chemputer (pushed 2026-04-10)
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **Increment 12**: ERGODIC — sweep_complete closing the 4th full GF(3) cycle
