# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-13

## Sweep Metadata
- **Date:** 2026-06-13
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| World Increments (today) | 12 |
| Repo Snapshots (today) | 44 |
| Sources Covered | 3 orgs + 8 users = 11 total |
| Aptos Wallets Queried | 28 |
| Multisig Probes | 5 |
| Total Repos Indexed | 341 |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — 12 Increments

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|----------|-------|------|
| 1  | plurigrid | org | 0 | `#d3869b` | **ERGODIC** |
| 2  | kubeflow | org | +1 | `#b8bb26` | **PLUS** |
| 3  | TeglonLabs | org | -1 | `#cc241d` | **MINUS** |
| 4  | bmorphism | user | 0 | `#d3869b` | **ERGODIC** |
| 5  | zubyul | user | +1 | `#b8bb26` | **PLUS** |
| 6  | migalkin | user | -1 | `#cc241d` | **MINUS** |
| 7  | DJedamski | user | 0 | `#d3869b` | **ERGODIC** |
| 8  | wasita | user | +1 | `#b8bb26` | **PLUS** |
| 9  | kristinezheng | user | -1 | `#cc241d` | **MINUS** |
| 10 | M1shaaa | user | 0 | `#d3869b` | **ERGODIC** |
| 11 | AustinCStone | user | +1 | `#b8bb26` | **PLUS** |
| 12 | hamming_swarm (aptos) | event | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

### Repo Counts by Source

| Source | Type | Total Repos |
|--------|------|-------------|
| plurigrid | org | 101 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 104 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| DJedamski | user | 6 |
| wasita | user | 11 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| AustinCStone | user | 40 |
| **TOTAL** | | **396** |

### Notable Repos (most recently pushed, 2026-06-13 sweep)

**plurigrid** (101 repos):
- `plurigrid/asi` (HTML, ⭐26) — pushed 2026-06-12 — "everything is topological chemputer!"
- `plurigrid/gorj` (Clojure, 543 open issues) — pushed 2026-05-08 — this repo: forj + Rama GF(3) trit coloring
- `plurigrid/nash-portal` (Rust, ⭐2) — pushed 2026-05-19 — NASH token TUI in browser (ratzilla WASM + GeckoTerminal)
- `plurigrid/nanoclj-zig` (Zig, ⭐1) — pushed 2026-04-25 — NaN-boxed Clojure interpreter in Zig 0.15
- `plurigrid/vcg-auction` (Rust, ⭐7) — simple VCG auction CosmWasm contract

**kubeflow** (48 repos, flagship ML platform):
- `kubeflow/kubeflow` (⭐15720) — pushed 2026-06-13 — Machine Learning Toolkit for Kubernetes
- `kubeflow/pipelines` (Python, ⭐4153) — pushed 2026-06-13 — ML Pipelines for Kubeflow
- `kubeflow/spark-operator` (Python, ⭐3128) — pushed 2026-06-13 — Kubernetes operator for Apache Spark
- `kubeflow/trainer` (Go, ⭐2114) — pushed 2026-06-13 — Distributed AI Model Training & LLM Fine-Tuning
- `kubeflow/mcp-server` (Python, ⭐11) — new 2026 — MCP Server for AI-Assisted Kubeflow dev

**TeglonLabs** (5 repos):
- `TeglonLabs/jank-crane` (C++) — pushed 2026-06-08 — crane-jank converged-IR hub, GF3 convergence maps, simonw workflow

**bmorphism** (104 repos, most active):
- `bmorphism/Gay.jl` (Julia, 189 open issues) — pushed 2026-06-10 — wide-gamut color sampling SPI
- `bmorphism/satreadout` (Lean) — pushed 2026-06-10 — machine-checked saturating perceptual readout
- `bmorphism/ocaml-mcp-sdk` (OCaml, ⭐61) — OCaml SDK for MCP using Jane Street oxcaml_effect
- `bmorphism/anti-bullshit-mcp-server` (JavaScript, ⭐23) — epistemological claim analysis
- `bmorphism/babashka-mcp-server` (JavaScript, ⭐19) — MCP for Babashka Clojure

**zubyul** (49 repos):
- `zubyul/voice-observatory` — pushed 2026-04-24 — companion to bmorphism/say-mcp-server
- `zubyul/tilelang-kernels` — TileLang GPU kernels for GF(3) trit classification on NVIDIA GB10 Blackwell
- `zubyul/gay-world` (Python, ⭐1) — Goblin world builder: each goblin is a world

**migalkin** (19 repos, knowledge graphs):
- `migalkin/NodePiece` (Python, ⭐144) — ICLR'22: scalable knowledge graph embeddings
- `migalkin/StarE` (Python, ⭐89) — EMNLP 2020: hyper-relational knowledge graphs
- `migalkin/NBFNet_mlx` (Python, ⭐10) — Neural Bellman-Ford in MLX for Apple Silicon

**AustinCStone** (40 repos):
- `AustinCStone/TextGAN` (Python, ⭐92) — GAN for text generation in TensorFlow
- `AustinCStone/StereoVisionMRF` (Python, ⭐11) — depth from stereo with MRF + loopy belief propagation

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried via `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{ADDR}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` with 1s sleep between calls. All 28 wallets returned 0 APT — `CoinStore` resource not registered (accounts unfunded or not yet initialized on mainnet).

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob   | 0x0a3c...2d5d | 0.0 |
| A–Z   | (26 addresses) | 0.0 each |

**Total APT across 28 wallets: 0.0**

### Multisig Contract Probes

POST `https://fullnode.mainnet.aptoslabs.com/v1/view` → `0x1::multisig_account::num_signatures_required`. All 5 contracts live and healthy.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | **2** | ✅ healthy |
| A-G | 0xf56c...0096 | **2** | ✅ healthy |
| Y-Z | 0xd3ff...b883 | **2** | ✅ healthy |
| S-T | 0x3b1c...7883 | **2** | ✅ healthy |
| V-W | 0x40fa...eb6d | **2** | ✅ healthy |

All multisig accounts require **2-of-N** signatures. All 5/5 contracts responsive on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` and `https://testnet.mnx.fi/api/markets` both returned **HTTP 401 Unauthorized**. The testnet requires authentication. No market data retrievable without credentials. Recorded as unavailable in `mnx_snapshots`.

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
