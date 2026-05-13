# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-05-13 (UTC)
**Branch:** world-increment/sweep
**GF(3) Color Chain:** id%3==0 → trit=0 ERGODIC #d3869b | id%3==1 → trit=1 PLUS #b8bb26 | id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source Type | Source | Repos Captured |
|-------------|--------|----------------|
| org | plurigrid | 100 |
| org | kubeflow | 48 |
| org | TeglonLabs | 4 |
| user | bmorphism | 13 (sampled) |
| user | zubyul | 5 (sampled) |
| user | migalkin | 3 (sampled) |
| user | DJedamski | 1 (sampled) |
| user | wasita | 2 (sampled) |
| user | kristinezheng | 1 (sampled) |
| user | M1shaaa | 1 (sampled) |
| user | AustinCStone | 2 (sampled) |

**Total repos snapshotted:** 180

### Notable Repos (by stars)

#### plurigrid
- `plurigrid/asi` — HTML, 21 ★, 5 forks — "everything is topological chemputer!"
- `plurigrid/ontology` — JavaScript, 8 ★, 9 forks — "autopoietic ergodicity and embodied gradualism"
- `plurigrid/StochFlow` — Python, 4 ★ — stochastic interpolant models
- `plurigrid/gorj` — Clojure, 177 open issues — forj + Rama topology + GF(3) gay trit coloring (this repo, pushed 2026-05-13)

#### kubeflow
- `kubeflow/kubeflow` — 15,629 ★, 2,648 forks — Machine Learning Toolkit for Kubernetes
- `kubeflow/pipelines` — Python, 4,140 ★ — ML Pipelines
- `kubeflow/spark-operator` — Python, 3,125 ★ — Kubernetes operator for Spark
- `kubeflow/trainer` — Go, 2,098 ★ — Distributed AI Model Training
- `kubeflow/hub` — Go, 175 ★ — Model Registry, pushed 2026-05-13
- `kubeflow/mcp-apache-spark-history-server` — Python, 168 ★ — MCP Server for Spark

#### bmorphism
- `bmorphism/ocaml-mcp-sdk` — OCaml, 61 ★ — OCaml SDK for MCP (Jane Street oxcaml_effect)
- `bmorphism/anti-bullshit-mcp-server` — JavaScript, 23 ★
- `bmorphism/risc0-cosmwasm-example` — Rust, 23 ★ — CosmWasm + zkVM RISC-V
- `bmorphism/say-mcp-server` — JavaScript, 20 ★
- `bmorphism/babashka-mcp-server` — JavaScript, 18 ★

#### migalkin (social graph)
- `migalkin/NodePiece` — Python, 144 ★ — ICLR'22 KG representations
- `migalkin/StarE` — Python, 89 ★ — EMNLP 2020 Hyper-Relational KG

#### AustinCStone (social graph)
- `AustinCStone/TextGAN` — Python, 92 ★ — GAN for text generation

### GF(3) Color Distribution (180 world_increments)
- trit=0 ERGODIC #d3869b: 60 repos (id%3==0)
- trit=1 PLUS #b8bb26: 60 repos (id%3==1)
- trit=-1 MINUS #cc241d: 60 repos (id%3==2)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 wallets queried via `fullnode.mainnet.aptoslabs.com/v1`.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...4cc7b | 0.0 |
| bob | 0x0a3c...512d5d | 0.0 |
| A | 0x8699...e9d7a | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...cfdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...51b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...d0386 | 0.0 |
| T | 0x3578...f4588 | 0.0 |
| U | 0x7586...f9956 | 0.0 |
| V | 0xb59d...af2c3 | 0.0 |
| W | 0x5f32...7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...444c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

**Note:** All accounts show 0 APT. These wallets have no CoinStore for AptosCoin on mainnet, or hold zero balance. Queried with 1s sleep between calls.

**Total Hamming swarm APT:** 0.0 APT

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**All 5/5 multisig contracts healthy** — each requires 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

Status: **UNAVAILABLE via API** — testnet.mnx.fi is a Next.js SPA. The root serves an HTML shell; no `/api/markets` or `/api/v1/markets` endpoints return structured JSON. Market data requires client-side JavaScript hydration. Recorded as placeholder in `mnx_snapshots`.

---

## DuckDB Schema Summary

Database: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows | Description |
|-------|------|-------------|
| world_increments | 180+ | GF(3) trit-colored event log |
| repo_snapshots | 180+ | GitHub repo metadata |
| aptos_snapshots | 28 | Aptos wallet balances |
| multisig_probes | 5 | Multisig contract sigs_required |
| mnx_snapshots | 1 | MNX placeholder (SPA) |

---

## Active Frontiers (2026-05-13)

- **plurigrid/gorj** — most active, 177 open issues, GF(3) color work live
- **kubeflow/hub** — model registry, pushed today
- **kubeflow/trainer** — distributed training, 2k+ stars, active
- **bmorphism/ocaml-mcp-sdk** — OCaml MCP, 61 stars, pushed 2026-05-08
- **wasita/wasita.github.io** — pushed today, personal site
- **migalkin/NodePiece** — KG representation, pushed 2026-05-07
