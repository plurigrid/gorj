# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-15

## Sweep Metadata
- **Date:** 2026-06-15
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 97 |
| Total Repo Snapshots (cumulative) | 1018 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 (all healthy, 2-of-N) |
| MNX Markets | Unavailable (Vercel auth) |

---

## JOB 1: GitHub Social Graph Sweep — 2026-06-15 Delta

### Sources Queried This Run
| Source | Type | Repos Discovered |
|--------|------|-----------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 104 |
| zubyul | user | 49 |
| migalkin | social | 19 |
| DJedamski | social | 6 |
| wasita | social | 11 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| AustinCStone | social | 40 |

**Total repos discovered: ~395**

### Most Recently Pushed (as of 2026-06-15)
- `plurigrid/gorj` — 2026-06-15T17:12:06Z (Clojure, **599** open issues)
- `kubeflow/sdk` — 2026-06-15T18:05:30Z (Python)
- `kubeflow/pipelines` — 2026-06-15T17:45:03Z (Python)
- `bmorphism/Gay.jl` — 2026-06-15T16:43:51Z (Julia, 188 open issues)
- `kubeflow/community-distribution` — 2026-06-15T16:47:58Z (YAML)

### Notable New Repos Since Last Sweep
- `TeglonLabs/jank-crane` (C++, 2026-06-08): "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow"
- `bmorphism/satreadout` (Lean, 2026-06-10): machine-checked saturating non-Riemannian perceptual readout
- `bmorphism/world` (Python, 2026-06-02): Local worlds launcher for SA3, jank, and world proofs
- `zubyul/voice-observatory` (Python, 2026-04-24): Passive macOS TUI observing voice-download pathways

### Star Counts Delta (top repos, now vs. April 2026)
| Repo | Stars (Apr) | Stars (Jun) | Δ |
|------|-------------|-------------|---|
| kubeflow/kubeflow | 15565 | 15726 | +161 |
| kubeflow/pipelines | 4119 | 4154 | +35 |
| kubeflow/spark-operator | 3111 | 3127 | +16 |
| kubeflow/trainer | 2080 | 2115 | +35 |
| plurigrid/asi | 16 | 26 | +10 |
| bmorphism/ocaml-mcp-sdk | 60 | 61 | +1 |
| AustinCStone/TextGAN | 92 | 92 | 0 |

---

## JOB 2: Hamming Swarm Snapshot — Aptos Mainnet

### Wallet Balances (28 addresses: alice, bob, A–Z)
**All probed 2026-06-15 via Aptos fullnode mainnet API.**

All 28 addresses returned 0 APT. The CoinStore resource was not found on mainnet for any address — accounts are likely not initialized or pre-funded on mainnet.

### Multisig Contract Probes
All 5 pairs probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f4...7003 | **2** | ✓ HEALTHY |
| A-G | 0xf56c4a...0096 | **2** | ✓ HEALTHY |
| Y-Z | 0xd3ffe1...b883 | **2** | ✓ HEALTHY |
| S-T | 0x3b1c3a...7883 | **2** | ✓ HEALTHY |
| V-W | 0x40fad7...eb6d | **2** | ✓ HEALTHY |

**All 5 multisig contracts are live on mainnet, requiring 2-of-N co-signatures.**

### MNX Markets (testnet.mnx.fi)
Status: **UNAVAILABLE** — behind Vercel visitor-password authentication. No market data extracted.

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
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — most popular ML pipeline for Kubernetes (pushed 2026-04-10)
- **kubeflow/spark-operator**: 3,111 stars — Kubernetes operator for Apache Spark (pushed 2026-04-10)
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 16 stars — topological chemputer (pushed 2026-04-10)
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **Increment 12**: ERGODIC — sweep_complete closing the 4th full GF(3) cycle
