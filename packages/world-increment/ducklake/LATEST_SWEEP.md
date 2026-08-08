# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-08-08  
**GF(3) Color Chain:** ERGODIC #d3869b | PLUS #b8bb26 | MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Found |
|--------|------|-------------|
| plurigrid | org | 103 total (100 returned) |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 106 total (100 returned) |
| zubyul | user | 49 |
| migalkin | social | 19 |
| DJedamski | social | 6 |
| wasita | social | 14 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| AustinCStone | social | 41 |

### Notable Repos by Source

#### plurigrid (103 repos, most recently pushed 2026-08-08)
- **gorj** (Clojure, 1★, 1712 issues) — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **asi** (HTML, 59★, 13f) — everything is topological chemputer!
- **eirobri** (Clojure, 31 issues) — EiRoBri replay world, pushed 2026-08-04
- **zig-syrup** (Zig, 2★) — OCapN Syrup implementation, pushed 2026-07-28
- **nash-portal** (Rust, 2★) — NASH token TUI in the browser (ratzilla WASM + GeckoTerminal)
- **ontology** (JavaScript, 8★, 9f) — autopoietic ergodicity and embodied gradualism
- **vcg-auction** (Rust, 7★) — VCG auction contract

#### kubeflow (49 repos, very active ML-on-Kubernetes org)
- **kubeflow/kubeflow** (15,805★, 2,691f) — flagship repo
- **pipelines** (4,181★) — ML Pipelines, 516 open issues, active daily
- **spark-operator** (3,145★) — Kubernetes operator for Apache Spark
- **trainer** (2,175★) — Distributed AI/LLM fine-tuning, pushed 2026-08-08
- **katib** (1,694★) — AutoML on Kubernetes
- **mcp-apache-spark-history-server** (188★) — MCP Server for Spark debugging, new addition

#### TeglonLabs (5 repos)
- **jank-crane** (C++, 2026-06-08) — crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps
- **mathpix-gem** (Ruby, 2★) — Math/chemistry OCR to LaTeX/SMILES
- **coin-flip-mcp** (JavaScript, 2f) — random.org coin flip MCP server
- **topoi** (Python) — topos theory

#### bmorphism (106 repos)
- **Gay.jl** (Julia, 2★, 188 issues) — wide-gamut color sampling with SplitMix64, pushed 2026-08-07
- **ocaml-mcp-sdk** (OCaml, 61★) — OCaml SDK for MCP using oxcaml_effect
- **anti-bullshit-mcp-server** (JavaScript, 23★, 7f) — claim validation MCP
- **risc0-cosmwasm-example** (Rust, 23★) — CosmWasm + zkVM RISC-V template
- **say-mcp-server** (JavaScript, 20★, 9f) — macOS TTS MCP
- **babashka-mcp-server** (JavaScript, 19★) — Babashka/Clojure MCP
- **shitcoin** (Python, 5★) — IBC cw20 denom querier, pushed 2026-04-08

#### zubyul (49 repos)
- **wm-cv** (Svelte, pushed 2026-08-07) — academic CV as SPA
- **xoxowasita-analysis** (Python, pushed 2026-08-06) — new repo
- **gay-world** (Python, 1★) — Goblin world builder with MLX task decomposition
- **from-possible-worlds** (TeX, pushed 2026-07-18) — active
- **plurigrid-site** (Svelte, 11 issues) — site deployment

#### Social Graph (zubyul connections)
- **migalkin**: KG researcher — NodePiece (144★, ICLR'22), StarE (89★, EMNLP'20), NBFNet_mlx (10★)
- **wasita**: Neuro/CogSci — wm-cv pushed 2026-08-07 (just yesterday!), xoxowasita-analysis brand new
- **AustinCStone**: ML/vision — TextGAN (92★, 30f), StereoVisionMRF (11★), byteruckus pushed 2026-07-15
- **kristinezheng**: CogSci/neuro at MIT — site updated 2026-07
- **M1shaaa**: Lookit studies, Yale work
- **DJedamski**: Data science, inactive

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
**Status:** All 28 addresses queried. All returned `resource_not_found` for `CoinStore<AptosCoin>` — indicating accounts exist but CoinStore not initialized (effectively 0.00 APT). Aptos API reachable at ledger version 6,664,372,761.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793...7b | 0.0 |
| bob | 0x0a3c...5d | 0.0 |
| A–Z | 0x8699...7a – 0x7af0...7c | 0.0 (all) |

All 26 lettered addresses (A–Z) + alice + bob: zero APT (CoinStore uninitialized).

### Multisig Probes (5 pairs)
All 5 multisig contracts **healthy** — 2-of-N threshold confirmed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)
Site is live (Next.js SPA, dark theme, `dpl_74912uzpR3tUacTmJCdyVuf4m7Bw`), but REST API paths `/api/markets` and `/api/v1/markets` returned no JSON data — standard SPA behavior requiring client-side JS execution. **Market data unavailable via static API probe.**

---

## DuckDB State (world-increments.duckdb)
| Table | Rows |
|-------|------|
| world_increments | 51 |
| repo_snapshots | 944 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA, no API) |

**GF(3) color chain applied:** IDs cycle ERGODIC (#d3869b, trit=0) → PLUS (#b8bb26, trit=1) → MINUS (#cc241d, trit=2)

---

## Key Signals
1. **plurigrid/gorj** (this repo) pushed today — 1712 open issues, actively developed
2. **bmorphism/Gay.jl** has 188 open issues, pushed yesterday — high velocity
3. **wasita** pushed TWO repos in the last 48h (wm-cv and xoxowasita-analysis) — notable activity
4. **kubeflow/trainer** pushed today — distributed AI training on Kubernetes
5. **All 5 multisig contracts healthy** — Hamming swarm integrity confirmed (2-of-N each)
6. **All Aptos addresses at 0 APT** — wallets exist but CoinStore not initialized on mainnet
