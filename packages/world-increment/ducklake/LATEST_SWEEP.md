# World Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-07-11  
**Ledger timestamp:** Aptos epoch 16497, block height ~891.6M

---

## GitHub Social Graph Sweep

### Orgs

| Org/User | Repos | Notable |
|---|---|---|
| plurigrid | ~80 | gorj (1122 open issues!), asi (30★), ontology (8★) — active Clojure/Zig/Rust work |
| kubeflow | ~50 | kubeflow/kubeflow (15,770★), pipelines (4,169★), spark-operator (3,137★) — very active |
| TeglonLabs | 5 | jank-crane (C++, GF3 maps), mathpix-gem (Ruby), coin-flip-mcp (JS) |

### Users

| User | Repos | Latest Activity |
|---|---|---|
| bmorphism | 105 | satreadout (Lean4, 2026-06-20), Gay.jl (187 issues), ocaml-mcp-sdk (61★) |
| zubyul | 49 | voice-observatory (2026-04-24), gay-world, nash-tui |
| migalkin | 19 | kgcourse2021 (HTML, updated 2026-07-10), NodePiece (144★) — KG researcher |
| DJedamski | 6 | Kaggle, Getting-and-Cleaning-Data — data science |
| wasita | 11 | wasita.github.io (Svelte, updated 2026-07-06) |
| kristinezheng | 5 | personal site updated 2026-07-01 |
| M1shaaa | 8 | lab-bookshelf- (TypeScript) |
| AustinCStone | 40 | TextGAN (92★), EpsteinSearch |

### GF3 Color Chain (last sweep)
- ID 46 PLUS #b8bb26 — DJedamski/Getting-and-Cleaning-Data  
- ID 47 MINUS #cc241d — kristinezheng/kristinezheng.github.io  
- ID 48 ERGODIC #d3869b — M1shaaa/lab-bookshelf-

---

## Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
**Chain state:** epoch 16497, ledger v6,228,322,479, block 891,621,100

All 28 addresses (alice, bob, A–Z) returned `resource_not_found` for  
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
These wallets have no initialized APT CoinStore on mainnet (unfunded or unregistered).

| World | Address (truncated) | APT Balance |
|---|---|---|
| alice | 0xc793...cc7b | 0.0 (not found) |
| bob | 0x0a3c...2d5d | 0.0 (not found) |
| A–Z | (26 addresses) | 0.0 (all not found) |

### Multisig Contract Probes (Mainnet)
All 5 multisig contracts are **healthy** — each requires **2 signatures**.

| Pair | Address (truncated) | Sigs Required | Status |
|---|---|---|---|
| A-B | 0x0da4...7003 | 2 | ✅ healthy |
| A-G | 0xf56c...0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✅ healthy |
| S-T | 0x3b1c...7883 | 2 | ✅ healthy |
| V-W | 0x40fa...eb6d | 2 | ✅ healthy |

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — testnet.mnx.fi is a JavaScript SPA that does not expose a public JSON API.  
All probed paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`, `/api/pairs`) returned HTML.

---

## DuckDB Summary
| Table | Rows |
|---|---|
| world_increments | 59 (cumulative) |
| repo_snapshots | 980 (cumulative) |
| aptos_snapshots | 28 (this run) |
| multisig_probes | 5 (this run) |
| mnx_snapshots | 1 (unavailable note) |

DB: `packages/world-increment/ducklake/world-increments.duckdb`
