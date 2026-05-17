# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-05-17  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain

| inc_id | source | type | trit | color | gf3_name | repos |
|--------|--------|------|------|-------|----------|-------|
| 1 | TeglonLabs | org | +1 | #b8bb26 | PLUS | 4 |
| 2 | kubeflow | org | -1 | #cc241d | MINUS | 20 |
| 3 | plurigrid | org | 0 | #d3869b | ERGODIC | 22 |
| 4 | bmorphism | user | +1 | #b8bb26 | PLUS | 20 |
| 5 | zubyul | user | -1 | #cc241d | MINUS | 20 |
| 6 | migalkin | user | 0 | #d3869b | ERGODIC | 7 |
| 7 | DJedamski | user | +1 | #b8bb26 | PLUS | 4 |
| 8 | wasita | user | -1 | #cc241d | MINUS | 7 |
| 9 | kristinezheng | user | 0 | #d3869b | ERGODIC | 4 |
| 10 | M1shaaa | user | +1 | #b8bb26 | PLUS | 5 |
| 11 | AustinCStone | user | -1 | #cc241d | MINUS | 9 |

**Total repos snapshotted:** 122  
**Total world_increments:** 11

### Notable Repos by Source

**plurigrid** (22 repos, ERGODIC #d3869b)
- `gorj` — forj + Rama topology nREPL + GF(3) trit coloring (222 open issues)
- `nanoclj-zig` — NaN-boxed Clojure in Zig 0.15, interaction nets, GF(3)
- `asi` — topological chemputer (23 stars)
- `zig-syrup` — OCapN Syrup in Zig (2 stars)
- `ontology` — autopoietic ergodicity (8 stars)

**kubeflow** (20 repos, MINUS #cc241d)
- `kubeflow` — 15,637 stars, ML Toolkit for Kubernetes
- `pipelines` — 4,139 stars, ML Pipelines
- `spark-operator` — 3,125 stars, Kubernetes Spark operator
- `katib` — 1,682 stars, AutoML on Kubernetes
- `examples` — 1,463 stars

**bmorphism** (20 repos, PLUS #b8bb26)
- `Gay.jl` — 189 open issues, wide-gamut color sampling
- `ocaml-mcp-sdk` — 61 stars, OCaml SDK for MCP
- `anti-bullshit-mcp-server` — 23 stars
- `risc0-cosmwasm-example` — 23 stars, CosmWasm + zkVM
- `say-mcp-server` — 20 stars, macOS TTS via MCP

**zubyul** (20 repos, MINUS #cc241d)
- `gay-world` — 1 star, goblin world builder, MLX task decomposition
- `cascade-world` — 1 star, cascade dev env
- `ghostty-modifications` — 1 star, Ghostty MCP servers
- `plurigrid-site` — 11 open issues

**migalkin** (7 repos, ERGODIC #d3869b)
- `NodePiece` — 144 stars, Knowledge Graph representations (ICLR 2022)
- `StarE` — 89 stars, Hyper-Relational KG (EMNLP 2020)
- `kgcourse2021` — 25 stars, KG course materials

**AustinCStone** (9 repos, MINUS #cc241d)
- `TextGAN` — 92 stars, GAN for text generation in TensorFlow
- `StereoVisionMRF` — 11 stars, MRF depth inference

**wasita** (7 repos, MINUS #cc241d)
- `magic-garden` — 2 stars, Discord bot for magic garden game
- `wasita.github.io` — Svelte personal site, active 2026-05-17

**TeglonLabs** (4 repos, PLUS #b8bb26)
- `mathpix-gem` — 2 stars, Ruby gem: math images to LaTeX
- `coin-flip-mcp` — 2 forks, MCP random coin flipper
- `monad-mcp-server` — Monad MCP Server

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All 28 wallets (alice, bob, A-Z) queried against `fullnode.mainnet.aptoslabs.com`.

| World | Balance (APT) |
|-------|--------------|
| alice | 0.0 |
| bob | 0.0 |
| A through Z (26) | 0.0 each |

**Total APT across swarm:** 0.0 APT  
All addresses returned zero balance — wallets not funded or not yet activated on mainnet.

### Multisig Probes (5 contracts)

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428...7003 | 2 | YES |
| A-G | 0xf56c4a1c...0096 | 2 | YES |
| Y-Z | 0xd3ffe181...b883 | 2 | YES |
| S-T | 0x3b1c3ae9...7883 | 2 | YES |
| V-W | 0x40fad7b4...eb6d | 2 | YES |

All 5 multisig contracts healthy — all require 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA. No REST API endpoints (`/api/markets`, `/api/v1/markets`) returned structured data — the site renders client-side only. MNX market data: unavailable (SPA, no public API).

---

## Database Summary

| Table | Rows |
|-------|------|
| world_increments | 11 |
| repo_snapshots | 122 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA, no API) |

GF(3) trit balance: ERGODIC(0) x3, PLUS(+1) x4, MINUS(-1) x4
