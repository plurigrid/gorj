# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-22
**GF(3) color chain:** id%3==1 → PLUS #b8bb26 | id%3==2 → MINUS #cc241d | id%3==0 → ERGODIC #d3869b

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| # | GF3 | Source | Type | Repos Snapped | Stars (top) |
|---|-----|--------|------|---------------|-------------|
| 1 | PLUS | plurigrid | org | 20 (of 100) | gorj/746 issues, asi/26★ |
| 2 | MINUS | kubeflow | org | 15 (of 48) | kubeflow/15740★ |
| 3 | ERGODIC | TeglonLabs | org | 5 | jank-crane, mathpix-gem |
| 4 | PLUS | bmorphism | user | 20 (of 105) | ocaml-mcp-sdk/61★ |
| 5 | MINUS | zubyul | user | 10 (of 49) | gay-world, voice-observatory |
| 6 | ERGODIC | migalkin | user | 5 (of 19) | NodePiece/144★ |
| 7 | PLUS | wasita | user | 5 (of 11) | magic-garden/2★ |
| 8 | MINUS | AustinCStone | user | 5 (of 40) | TextGAN/92★ |
| 9 | ERGODIC | DJedamski | user | 3 (of 6) | Getting-and-Cleaning-Data |
| 10 | PLUS | kristinezheng | user | 3 (of 5) | lookit-jenga |
| 11 | MINUS | M1shaaa | user | 3 (of 8) | lab-bookshelf- |

### Notable Activity (2026-06-22 sweep)

**plurigrid** (most active):
- `plurigrid/gorj` pushed 2026-06-22 — 746 open issues (GF3 trit activity)
- `plurigrid/place` pushed 2026-06-20 (forester/bci.place preview)
- `plurigrid/asi` pushed 2026-06-10 (26 stars, topological chemputer)

**kubeflow** (high velocity):
- `mcp-apache-spark-history-server` pushed 2026-06-22 (177★, new MCP)
- `spark-operator` pushed 2026-06-22 (3128★)
- `pipelines` pushed 2026-06-22 (4157★, 448 open issues)
- `dashboard` pushed 2026-06-22 (TypeScript, 81 issues)

**TeglonLabs** (5 repos):
- `jank-crane` — crane-jank converged-IR hub with GF3 convergence maps (Jun 2026)
- `mathpix-gem` — Ruby gem for mathematical OCR (Jan 2026)

**bmorphism** (105 public repos):
- `Gay.jl` — 187 open issues, wide-gamut SPI color sampling
- `satreadout` — Lean 4.28 machine-checked non-Riemannian readout (Jun 2026)
- `nanoclj-zig` — active development (Jun 2026)
- `flox-mcp-bb` — active Babashka MCP for Flox
- `ocaml-mcp-sdk` — 61★ OCaml SDK for Model Context Protocol

**zubyul** (49 repos):
- `voice-observatory` + `ghostel-emacs-worlds` — most recent (Apr 2026)
- `big-bad-plurigrid-quiz` — 27 flashcards from bmorphism/plurigrid/zubyul activity
- `tilelang-kernels` — TileLang GPU kernels for NVIDIA GB10 Blackwell

**migalkin** (knowledge graph researcher, 19 repos):
- `NodePiece` — 144★ (ICLR 2022 KG representations)
- `StarE` — 89★ (EMNLP 2020 hyper-relational KGs)
- `RWL` updated May 2026 (Weisfeiler and Leman Go Relational)

**wasita**: active personal site, vocoder (May 2026), magic-garden Discord bot

**AustinCStone**: `TextGAN` 92★ (TF GAN for text), `bmfork` links to bmorphism

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

API: `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

**Result:** All 28 addresses (alice, bob, A-Z) returned **0.0 APT**.
All accounts lack an initialized CoinStore<AptosCoin> resource on mainnet — expected for accounts holding other token types or not yet receiving native APT.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C-Z | (24 addrs) | 0.0 each |

### Multisig Probes (`0x1::multisig_account::num_signatures_required`)

All 5 multisig contracts are **healthy** with 2-of-2 threshold:

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | YES |
| A-G | 0xf56c...0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

Swarm consensus: all active multisig pairs require 2-of-2. No threshold drift detected.

### MNX Markets (`https://testnet.mnx.fi`)

**UNAVAILABLE** — protected behind Vercel deployment authentication.
All API paths (/api/markets, /api/tickers, /api/v1/markets) return 401.
Market data requires bypass token or trusted-source OIDC config.

---

## DuckDB Ducklake Schema

File: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 14 |
| repo_snapshots | 94 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

### Top Repos by Stars (in DB)

| org/user | repos | total_stars |
|----------|-------|-------------|
| kubeflow | 15 | 31,909 |
| migalkin | 5 | 276 |
| bmorphism | 20 | 205 |
| AustinCStone | 5 | 106 |
| plurigrid | 20 | 68 |
| zubyul | 10 | 7 |
| wasita | 5 | 4 |
| DJedamski | 3 | 3 |
| TeglonLabs | 5 | 2 |
| kristinezheng | 3 | 0 |
| M1shaaa | 3 | 0 |

---

*Generated 2026-06-22 by world-increment-sweep + hamming-swarm-snapshot agent*
