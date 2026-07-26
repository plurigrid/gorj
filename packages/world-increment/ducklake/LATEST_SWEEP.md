# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-07-26  
**GF(3) Color Chain:** ERGODIC #d3869b | PLUS #b8bb26 | MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos Captured | Notes |
|--------|------|----------------|-------|
| plurigrid | org | 13 | gorj (1413 issues), asi (31★), ontology (8★) |
| kubeflow | org | 10 | kubeflow/kubeflow (15.7k★), pipelines (4.2k★), spark-operator (3.1k★) |
| TeglonLabs | org | 5 | jank-crane (C++), mathpix-gem (Ruby), coin-flip-mcp (JS) |
| bmorphism | user | 9 | Gay.jl (188 open issues!), ocaml-mcp-sdk (61★), risc0-cosmwasm (23★) |
| zubyul | user | 5 | from-possible-worlds (TeX), gay-world, plurigrid-site |
| social graph | users | 8 | migalkin/NodePiece (144★), AustinCStone/TextGAN (92★) |

### Social Graph Coverage
- **migalkin**: 19 repos — NodePiece (144★), StarE (89★), NBFNet_mlx (10★)
- **DJedamski**: 6 repos — kaggle_ncaa18, EDA, Kaggle
- **wasita**: 12 repos — wasita.github.io, wm-cv, magic-garden
- **kristinezheng**: 5 repos — personal site, auditory-illusion, Green-Machine
- **M1shaaa**: 8 repos — lab-bookshelf, MNIST-Classifier
- **AustinCStone**: 20 repos — TextGAN (92★), StereoVisionMRF (11★)

### Key Active Repos (pushed today 2026-07-26)
- `kubeflow/pipelines` — Python, 4170★, 466 open issues
- `kubeflow/dashboard` — TypeScript, 16★
- `plurigrid/gorj` — Clojure (this repo!), 1413 open issues
- `bmorphism/Gay.jl` — Julia, 188 open issues

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Balances (28 wallets)

All 28 wallets (alice, bob, A–Z) returned **0 APT** on the CoinStore resource.
Wallets are unfunded on mainnet or hold no native APT (may hold other assets).

| Label | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.00 |
| bob | 0x0a3c...512d | 0.00 |
| A–Z | (26 addresses) | 0.00 each |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **healthy** — each requires 2 signatures (2-of-2).

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...3003 | 2 | HEALTHY |
| A-G | 0xf56c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY |
| S-T | 0x3b1c...7883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status: SPA — no REST API accessible.** The testnet.mnx.fi endpoint serves a
Next.js SPA (client-side rendered). Paths `/api/markets` and `/api/v1/markets`
returned HTML, not JSON. No market data could be extracted without a headless browser.

---

## DuckDB State

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows (cumulative) |
|-------|-------------------|
| world_increments | 73 |
| repo_snapshots | 994 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA, no API) |

---

## GF(3) Color Distribution (this sweep, 50 increments)

- **ERGODIC** (trit=0, #d3869b): ids divisible by 3 — 17 repos
- **PLUS** (trit=1, #b8bb26): ids equiv 1 mod 3 — 17 repos
- **MINUS** (trit=-1, #cc241d): ids equiv 2 mod 3 — 16 repos
