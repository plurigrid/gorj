# World-Increment Sweep + Hamming Swarm Snapshot
**Generated:** 2026-06-17  
**Run:** world-increment-sweep + hamming-swarm-snapshot

---

## JOB 1: GitHub Social Graph Sweep

### Sources Crawled (GF(3) Color Chain)

| ID | GF3 Trit | Color | Name | Source | Repos Sampled |
|----|----------|-------|------|--------|---------------|
| 1  | +1 PLUS  | #b8bb26 | plurigrid (org) | org | 19 |
| 2  | -1 MINUS | #cc241d | kubeflow (org)  | org | 10 |
| 3  | 0 ERGODIC| #d3869b | TeglonLabs (org)| org | 5  |
| 4  | +1 PLUS  | #b8bb26 | bmorphism (user)| user | 10 |
| 5  | -1 MINUS | #cc241d | zubyul (user)   | user | 8  |
| 6  | 0 ERGODIC| #d3869b | migalkin (user) | user | 5  |
| 7  | +1 PLUS  | #b8bb26 | DJedamski (user)| user | 2  |
| 8  | -1 MINUS | #cc241d | wasita (user)   | user | 4  |
| 9  | 0 ERGODIC| #d3869b | kristinezheng (user) | user | 2 |
| 10 | +1 PLUS  | #b8bb26 | M1shaaa (user)  | user | 2  |
| 11 | -1 MINUS | #cc241d | AustinCStone (user) | user | 3 |

### Notable Repos

**plurigrid/**
- `gorj` (Clojure) — 627 open issues — forj + Rama topology nREPL + GF(3) trit coloring — pushed 2026-06-16
- `place` (TeX) — 8 open issues — pushed 2026-06-15
- `eirobri` (Clojure) — 29 open issues — EiRoBri replay world — pushed 2026-06-03
- `ontology` (JS) — ⭐8 — autopoietic ergodicity — pushed 2025-05-27

**kubeflow/**
- `kubeflow` — ⭐15,724, 2,674 forks — pushed 2026-06-17
- `pipelines` (Python) — ⭐4,154 — Machine Learning Pipelines — pushed 2026-06-16
- `trainer` (Go) — ⭐2,115 — Distributed AI Model Training — pushed 2026-06-17
- `kale` (Python) — ⭐694 — pushed 2026-06-17 (most active today)

**TeglonLabs/**
- `jank-crane` (C++) — crane-jank converged-IR hub, GF3 convergence maps — pushed 2026-06-08
- `mathpix-gem` (Ruby) — ⭐2 — Mathematical OCR Ruby gem — pushed 2026-01-01

**bmorphism/**
- `Gay.jl` (Julia) — 187 open issues — Wide-gamut color sampling + SPI pattern — pushed 2026-06-15
- `ocaml-mcp-sdk` (OCaml) — ⭐61 — OCaml SDK for MCP using Jane Street oxcaml_effect
- `say-mcp-server` (JS) — ⭐20 — macOS TTS MCP
- `babashka-mcp-server` (JS) — ⭐19 — MCP for Babashka

**zubyul/**
- `voice-observatory` (Python) — macOS TUI for voice-download pathways — pushed 2026-04-24
- `tilelang-kernels` (Python) — TileLang GPU kernels for SplitMix64, GF(3), FlashAttention

**Social Graph (zubyul connections):**
- `migalkin`: Knowledge Graph ML researcher — NodePiece (⭐144), StarE (⭐89)
- `wasita`: Personal site Svelte — active (2026-06-15), magic-garden Discord bot
- `AustinCStone`: TextGAN (⭐92), bmfork repos (active 2025)
- `kristinezheng`: MIT cognitive science, HackMIT 2021
- `M1shaaa`: Yale/lab research, lab-bookshelf TypeScript
- `DJedamski`: Data science, Kaggle competition repos

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 Hamming swarm addresses probed against Aptos mainnet (fullnode.mainnet.aptoslabs.com).

| World | Address (truncated) | Balance (APT) |
|-------|--------------------|----|
| alice | 0xc793...cc7b | 0.0 |
| bob   | 0x0a3c...2d5d | 0.0 |
| A–Z   | (26 addresses)   | 0.0 each |

**Status:** All 28 addresses returned 0 APT balance. Accounts appear unfunded on Aptos mainnet (CoinStore resource returns 0 value). This may indicate accounts are not yet registered for APT, or hold zero balance.

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Status |
|------|--------------------|----|--------|
| A-B  | 0x0da4...7003 | 2 | ✅ HEALTHY |
| A-G  | 0xf56c...0096 | 2 | ✅ HEALTHY |
| Y-Z  | 0xd3ff...b883 | 2 | ✅ HEALTHY |
| S-T  | 0x3b1c...7883 | 2 | ✅ HEALTHY |
| V-W  | 0x40fa...eb6d | 2 | ✅ HEALTHY |

All 5 multisig contracts are live on Aptos mainnet and require **2-of-N signatures**. Contract structure is uniform across all pairs.

### MNX Markets (testnet.mnx.fi)

Status: **UNAVAILABLE** — Site returns Vercel authentication wall (visitor password required). No market data extractable without credentials.

---

## DuckDB Schema

Database: `packages/world-increment/ducklake/world-increments.duckdb`

Tables:
- `world_increments` — 11 rows (one per source, GF(3) trit-colored)
- `repo_snapshots` — 70 rows (representative repos per source)
- `aptos_snapshots` — 28 rows (full Hamming swarm, alice+bob+A-Z)
- `multisig_probes` — 5 rows (A-B, A-G, Y-Z, S-T, V-W)
- `mnx_snapshots` — 0 rows (unavailable, Vercel auth)

---

*GF(3) color legend: ERGODIC=#d3869b (trit 0), PLUS=#b8bb26 (trit +1), MINUS=#cc241d (trit -1)*
