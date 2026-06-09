# World Increment Sweep — 2026-06-09

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos Snapshotted | Total Stars |
|--------|------|-------------------|-------------|
| plurigrid | org | 42 | 135 |
| kubeflow | org | 20 | ~100,502 |
| TeglonLabs | org | 5 | 14 |
| bmorphism | user | 17 | 393 |
| zubyul | user | 13 | 31 |
| migalkin | user (social) | 6 | 833 |
| DJedamski | user (social) | 6 | 17 |
| wasita | user (social) | 7 | 11 |
| kristinezheng | user (social) | 5 | 0 |
| M1shaaa | user (social) | 8 | 0 |
| AustinCStone | user (social) | 8 | 324 |

### Notable Repos

**plurigrid** (most recently active: `gorj` pushed 2026-06-09):
- `gorj` — forj + Rama topology nREPL routing + GF(3) gay trit coloring (464 open issues)
- `eirobri` — EiRoBri replay world (Clojure)
- `asi` — topological chemputer (25 ⭐)
- `nanoclj-zig` — NaN-boxed Clojure interpreter in Zig 0.15

**kubeflow** (most active ML platform org):
- `kubeflow` — 15,713 ⭐, ML Toolkit for Kubernetes
- `pipelines` — 4,153 ⭐, ML Pipelines
- `spark-operator` — 3,126 ⭐
- `trainer` — 2,112 ⭐, Distributed AI Model Training and LLM Fine-Tuning
- `mcp-apache-spark-history-server` — MCP server for Spark debugging (174 ⭐)

**TeglonLabs**:
- `jank-crane` — crane-jank converged-IR hub with GF3 convergence maps (C++, pushed 2026-06-08)
- `mathpix-gem` — mathematical OCR Ruby gem (2 ⭐)

**bmorphism** (very active, 60+ public repos):
- `Gay.jl` — Wide-gamut deterministic color sampling via SPI (Julia)
- `ocaml-mcp-sdk` — OCaml SDK for Model Context Protocol (61 ⭐)
- `anti-bullshit-mcp-server` — claim validation via epistemological frameworks (23 ⭐)
- `world` — Local worlds launcher for SA3, jank, and world proofs (pushed 2026-06-02)
- `oxgame` — Stellar resolution and open-game composition for OCaml

**zubyul**:
- `nash-tui` / `nash-web` — NASH token TUI via GeckoTerminal OHLCV (Rust)
- `gay-world` — Goblin world builder with MLX task decomposition (pushed 2026-03-26)
- `voice-observatory` — Passive macOS TUI observing voice-download pathways

**Social graph (zubyul connections)**:
- `wasita` — personal website (Svelte), CV, magic-garden discord bot
- `kristinezheng` — personal website (HTML, pushed 2026-06-07), cognitive science research
- `M1shaaa` — profile active (pushed 2026-06-09), Python/TypeScript projects
- `migalkin` — knowledge graph research (NodePiece 144⭐, StarE 89⭐)
- `DJedamski` — data science / Kaggle competition work

### GF(3) Color Chain (world_increments id % 3)
- id%3==0 → trit=0 ERGODIC `#d3869b`
- id%3==1 → trit=1 PLUS `#b8bb26`
- id%3==2 → trit=-1 MINUS `#cc241d`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

All 28 wallets queried: **alice, bob, A–Z**

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.00000000 |
| bob | 0x0a3c...512d | 0.00000000 |
| A–Z (26 wallets) | 0x8699...–0x7af0... | 0.00000000 each |

> All 28 addresses returned 0 APT. The `CoinStore<AptosCoin>` resource was not found for any address — wallets have not been initialized with APT on mainnet (no coin store registered).

**Total Hamming swarm APT: 0.00000000**

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | HEALTHY |
| A-G | 0xf56c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY |
| S-T | 0x3b1c...7883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

All multisig contracts are live on Aptos mainnet and require 2-of-N signatures.

### MNX Markets

`https://testnet.mnx.fi` — **UNAVAILABLE**. Both `/api/markets` and `/api/v1/markets`
returned no data. The SPA did not expose accessible API endpoints at the probed paths.

---

## DuckDB Schema (world-increments.duckdb)

| Table | Rows | Description |
|-------|------|-------------|
| world_increments | 34 | GF(3) color-chained source events |
| repo_snapshots | 1081 | Repo metadata across 11 sources |
| aptos_snapshots | 28 | Hamming swarm wallet balances |
| multisig_probes | 5 | Multisig contract health checks |
| mnx_snapshots | 0 | MNX market data (unavailable) |

---

*Sweep timestamp: 2026-06-09 UTC*
*GF(3) chain: ERGODIC(#d3869b) → PLUS(#b8bb26) → MINUS(#cc241d) → ...*
