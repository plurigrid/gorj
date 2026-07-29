# World-Increment Sweep + Hamming Swarm Snapshot
**Timestamp:** 2026-07-29T16:15Z  
**Ledger epoch:** 16715 | block height 934,238,307 (Aptos mainnet)

---

## JOB 1: GitHub Social Graph Sweep

### Repos Snapshotted: 239 (this run) across 11 sources

| Source | Repos | Top Stars |
|--------|-------|-----------|
| plurigrid | 100 | gorj (1), asi (54), ontology (8) |
| bmorphism | 50 | Gay.jl (2), ocaml-mcp-sdk (61), anti-bullshit-mcp-server (22) |
| zubyul | 49 | gay-world (1), zubyul.github.io (1) |
| kubeflow | 19 | kubeflow/kubeflow (15,796★), pipelines (4,170★), spark-operator (3,142★), trainer (2,162★) |
| TeglonLabs | 5 | jank-crane (C++), mathpix-gem (2★), coin-flip-mcp (JS) |
| migalkin | 5 | NodePiece (144★), StarE (89★), kgcourse2021 (24★) |
| wasita | 3 | wasita.github.io (Svelte), magic-garden, send2kobo |
| AustinCStone | 3 | TextGAN (92★), StereoVisionMRF (11★), byteruckus |
| M1shaaa | 2 | M1shaaa profile, lab-bookshelf- (TypeScript) |
| DJedamski | 2 | kaggle_ncaa18, Kaggle |
| kristinezheng | 1 | kristinezheng.github.io |

### GF(3) Trit Distribution (this run)
- ERGODIC (trit=0, #d3869b): 79 repos
- PLUS (trit=1, #b8bb26): 80 repos
- MINUS (trit=-1, #cc241d): 80 repos

### Notable Activity (most recently pushed)
- `plurigrid/gorj` pushed **2026-07-29** — forj + Rama topology nREPL (Clojure)
- `plurigrid/zig-syrup` pushed **2026-07-28** — OCapN Syrup in Zig
- `plurigrid/asi` — 54 stars, topological chemputer (HTML)
- `bmorphism/Gay.jl` pushed **2026-07-29** — wide-gamut color sampling (Julia, 188 open issues)
- `kubeflow/sdk` pushed **2026-07-29** — Universal Python SDK for Kubernetes AI (131★)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets: alice, bob, A–Z)

**Result:** All 28 wallets return `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
Aptos mainnet API is reachable (HTTP 200, epoch 16715). These addresses have no APT balance resource — they either have never received APT on mainnet or hold only non-APT tokens.

| World | Status |
|-------|--------|
| alice | no_apt_resource |
| bob | no_apt_resource |
| A–Z (26 wallets) | no_apt_resource |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **healthy** — each requires 2-of-N signatures.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f428...987003 | 2 | ✓ |
| A-G | 0xf56c4a1c...0096 | 2 | ✓ |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` serves a Next.js SPA (HTTP 200) with no public REST API endpoints. All API paths probed (`/api/markets`, `/api/v1/markets`, `/api/tickers`, `/api/v1/tickers`) return 404. Market data is rendered client-side and not available via static fetch. Status: **unavailable via HTTP fetch**.

---

## DuckDB Summary

**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows (cumulative) |
|-------|-------------------|
| world_increments | 262 |
| repo_snapshots | 1,183 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA, unavailable) |
