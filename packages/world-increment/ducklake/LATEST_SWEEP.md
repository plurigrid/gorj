# World-Increment Sweep + Hamming Snapshot — 2026-03-28

## Sweep Metadata
- **Date:** 2026-03-28T22:22 UTC
- **Agent:** world-increment-sweep (two-job autonomous sweep)
- **DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Found | Top Repo (Stars) |
|--------|------|-------------|-----------------|
| plurigrid | org | 87 | asi (13) |
| kubeflow | org | 46 | kubeflow/kubeflow (15538) |
| TeglonLabs | org | 3 | mathpix-gem (2) |
| bmorphism | user | 97 | ocaml-mcp-sdk (60) |
| zubyul | user | 44 | jonikas_lab_data_analysis_misc (2) |
| migalkin | social | 19 | NodePiece (143) |
| DJedamski | social | 6 | Kaggle (1) |
| wasita | social | 9 | wins-search (1) |
| kristinezheng | social | 6 | kristinezheng.github.io (0) |
| M1shaaa | social | 8 | M1shaaa profile (0) |
| AustinCStone | social | 20 | TextGAN (92) |
| bmorphism events | events | 30 captured | — |
| zubyul events | events | 30 captured | — |

### Top Repos by Stars per Source

**plurigrid** (org, 87 repos):
1. `asi` — 13 stars — "everything is topological chemputer!" (HTML, pushed 2026-03-28)
2. `ontology` — 7 stars — "autopoietic ergodicity and embodied gradualism" (JavaScript)
3. `vcg-auction` — 7 stars — "a simple contract that performs a VCG auction" (Rust)

**kubeflow** (org, 46 repos):
1. `kubeflow` — 15538 stars — "Machine Learning Toolkit for Kubernetes"
2. `pipelines` — 4113 stars — "Machine Learning Pipelines for Kubeflow" (Python)
3. `spark-operator` — 3110 stars — "Kubernetes operator for Apache Spark" (Python)
4. `trainer` — 2068 stars — "Distributed AI Model Training and LLM Fine-Tuning" (Go)
5. `katib` — 1672 stars — "Automated Machine Learning on Kubernetes" (Python)

**TeglonLabs** (org, 3 public repos):
1. `mathpix-gem` — 2 stars — "Transform mathematical images to LaTeX" (Ruby)
2. `coin-flip-mcp` — 0 stars — "MCP server for flipping coins" (JavaScript)
3. `topoi` — 0 stars (Python)

**bmorphism** (user, 97 repos):
1. `ocaml-mcp-sdk` — 60 stars — "OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect" (OCaml)
2. `anti-bullshit-mcp-server` — 23 stars — "MCP server for analyzing claims" (JavaScript)
3. `risc0-cosmwasm-example` — 23 stars — "CosmWasm + zkVM RISC-V EFI template" (Rust)
4. `say-mcp-server` — 20 stars — "MCP server for macOS text-to-speech" (JavaScript)
5. `babashka-mcp-server` — 18 stars — "Babashka/Clojure MCP server" (JavaScript)

**zubyul** (user, 44 repos):
1. `jonikas_lab_data_analysis_misc` — 2 stars
2. `WGCNA` — 2 stars
3. `Nikolova_lab_data_analysis` — 2 stars

**Social graph highlights:**
- migalkin/NodePiece — 143 stars (ICLR'22 knowledge graph representations)
- AustinCStone/TextGAN — 92 stars (GAN for text generation in TensorFlow)
- migalkin/StarE — 88 stars (EMNLP 2020 hyper-relational knowledge graphs)

---

## JOB 2: Aptos Hamming Swarm Snapshot

### Wallet Balance Table (28 addresses, Aptos mainnet)

All queried via `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| Label | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob   | 0x0a3c...2d5d | 0.0 |
| A     | 0x8699...9d7a | 0.0 |
| B     | 0x3f89...b13  | 0.0 |
| C     | 0x38b9...35e  | 0.0 |
| D     | 0xf776...dd1  | 0.0 |
| E     | 0xdc1d...d36  | 0.0 |
| F     | 0x18a1...f71  | 0.0 |
| G     | 0x69a3...f32  | 0.0 |
| H     | 0xce67...00f  | 0.0 |
| I     | 0x070f...fc9  | 0.0 |
| J     | 0x4d96...f54  | 0.0 |
| K     | 0xa732...dc4  | 0.0 |
| L     | 0x7c2e...ba9  | 0.0 |
| M     | 0x6fed...2e9  | 0.0 |
| N     | 0xe7dd...b2c  | 0.0 |
| O     | 0x7325...89d  | 0.0 |
| P     | 0x6218...948  | 0.0 |
| Q     | 0xac40...89a9 | 0.0 |
| R     | 0x7ce6...e10  | 0.0 |
| S     | 0xb875...386  | 0.0 |
| T     | 0x3578...588  | 0.0 |
| U     | 0x7586...956  | 0.0 |
| V     | 0xb59d...2c3  | 0.0 |
| W     | 0x5f32...7b0  | 0.0 |
| X     | 0xa95c...47d  | 0.0 |
| Y     | 0xd8e3...44c4 | 0.0 |
| Z     | 0x7af0...97c  | 0.0 |

All 28 addresses returned 0 APT (CoinStore resource not initialized or zero balance at snapshot time).

### Multisig Probe Results

Probed via `POST /v1/view` with `0x1::multisig_account::num_signatures_required`.

| Pair | Multisig Address (truncated) | Sigs Required | Status |
|------|------------------------------|---------------|--------|
| A-B | 0x0da4...003 | **2** | ok |
| A-G | 0xf56c...096 | **2** | ok |
| Y-Z | 0xd3ff...883 | **2** | ok |
| S-T | 0x3b1c...883 | **2** | ok |
| V-W | 0x40fa...b6d | **2** | ok |

All 5 multisig contracts are live and require **2-of-N** signatures.

---

## MNX Markets Status

- URL: `https://testnet.mnx.fi/api/markets` and `.../api/v1/markets`
- **Status: UNAVAILABLE as JSON** — both endpoints return HTML (Next.js SPA, requires browser JS to fetch market data)

---

## GF(3) Color Chain

| id % 3 | Trit | Color | Name |
|--------|------|-------|------|
| 0 | 0 | `#d3869b` | ERGODIC |
| 1 | 1 | `#b8bb26` | PLUS |
| 2 | -1 | `#cc241d` | MINUS |

---

## DuckDB Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)
repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)
aptos_balances(id, timestamp, world_label, address, apt_balance, raw_value)
multisig_probes(id, timestamp, pair_label, multisig_address, num_signatures_required, probe_status)
```

### Row Counts (this sweep + prior)
- `world_increments`: 23 rows
- `repo_snapshots`: 57 rows
- `aptos_balances`: 28 rows
- `multisig_probes`: 5 rows
