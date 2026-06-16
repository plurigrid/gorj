# World-Increment Sweep + Hamming Snapshot
**Sweep date:** 2026-06-16
**GF(3) color chain:** ERGODIC #d3869b (trit=0) · PLUS #b8bb26 (trit=1) · MINUS #cc241d (trit=-1)

---

## JOB 1 — GitHub Social Graph Sweep

### Sources

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| DJedamski | user | 6 |
| wasita | user | 11 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| AustinCStone | user | 30 |
| **TOTAL** | | **381** |

### Notable Repos

**plurigrid** (active today):
- `plurigrid/gorj` · Clojure · 2026-06-16 · *forj + Rama topology nREPL routing + GF(3) gay trit coloring*
- `plurigrid/place` · TeX · 2026-06-15
- `plurigrid/asi` · HTML · ★26 · 2026-06-10 · *everything is topological chemputer!*
- `plurigrid/eirobri` · Clojure · 2026-06-03

**kubeflow** (top by stars):
- `kubeflow/kubeflow` · ★15,725 · 2026-06-11
- `kubeflow/pipelines` · Python · ★4,154 · 2026-06-15
- `kubeflow/spark-operator` · Python · ★3,127 · 2026-06-15
- `kubeflow/trainer` · Go · ★2,115 · 2026-06-16 (active today)
- `kubeflow/mcp-apache-spark-history-server` · Python · ★177 · 2026-06-16

**bmorphism**:
- `bmorphism/Gay.jl` · Julia · ★1 · 2026-06-16 · *Wide-gamut color sampling with splittable determinism*
- `bmorphism/satreadout` · Lean · 2026-06-15 · *Machine-checked saturating non-Riemannian perceptual readout*
- `bmorphism/ocaml-mcp-sdk` · OCaml · ★61 · 2026-03-16

**TeglonLabs**:
- `TeglonLabs/jank-crane` · C++ · 2026-06-08 · *crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps*

**Social graph** (zubyul connections):
- `migalkin/NodePiece` · Python · ★144 · *Compositional representations for Large Knowledge Graphs*
- `migalkin/StarE` · Python · ★89 · *EMNLP 2020 hyper-relational KG message passing*
- `wasita/wasita.github.io` · Svelte · 2026-06-15
- `AustinCStone/TextGAN` · Python · ★92

### GF(3) Distribution
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 127 |
| 1 | #b8bb26 | PLUS | 127 |
| -1 | #cc241d | MINUS | 127 |

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-06-16)

All 28 addresses (alice, bob, A-Z) returned `resource_not_found` from Aptos mainnet.
The `0x1::coin::CoinStore<AptosCoin>` resource is absent — accounts are unfunded on mainnet.
All balances: **0.0 APT**.

### Multisig Contract Probes

All 5 probed multisig accounts are **healthy** (2-of-N sigs required, live on mainnet):

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...87003 | 2 | true |
| A-G | 0xf56c4a1c...c0096 | 2 | true |
| Y-Z | 0xd3ffe181...5b883 | 2 | true |
| S-T | 0x3b1c3ae9...d7883 | 2 | true |
| V-W | 0x40fad7b4...0eb6d | 2 | true |

### MNX Markets

`https://testnet.mnx.fi` is **Vercel-protected** — authentication required. No market data accessible. Status: **unavailable**.

---

## DuckDB Schema

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 381 | GF(3)-colored event log, one row per repo snapshot |
| `repo_snapshots` | 381 | Full repo metadata (stars, forks, language, pushed_at, description) |
| `aptos_snapshots` | 28 | Hamming swarm wallet balances at sweep time |
| `multisig_probes` | 5 | Multisig contract health (all healthy, 2 sigs required) |
| `mnx_snapshots` | 0 | MNX market data (unavailable — Vercel auth required) |

GF(3) on `id`: `id%3==0 → ERGODIC #d3869b`, `id%3==1 → PLUS #b8bb26`, `id%3==2 → MINUS #cc241d`.
