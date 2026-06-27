# World Increment Sweep + Hamming Snapshot
**Timestamp:** 2026-06-27T21:00:00Z  
**GF(3) Color Chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d → …

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| # | Source | Type | GF3 Trit | GF3 Color | Repos |
|---|--------|------|-----------|-----------|-------|
| 1 | plurigrid | org | 1 (PLUS) | #b8bb26 | 100 |
| 2 | kubeflow | org | -1 (MINUS) | #cc241d | 48 |
| 3 | TeglonLabs | org | 0 (ERGODIC) | #d3869b | 5 |
| 4 | bmorphism | user | 1 (PLUS) | #b8bb26 | 100 |
| 5 | zubyul | user | -1 (MINUS) | #cc241d | 49 |
| 6 | migalkin | user | 0 (ERGODIC) | #d3869b | 19 |
| 7 | AustinCStone | user | 1 (PLUS) | #b8bb26 | 40 |
| 8 | wasita | user | -1 (MINUS) | #cc241d | 11 |
| 9 | DJedamski | user | 0 (ERGODIC) | #d3869b | 6 |
| 10 | kristinezheng | user | 1 (PLUS) | #b8bb26 | 5 |
| 11 | M1shaaa | user | -1 (MINUS) | #cc241d | 8 |

**Total repos snapshotted: 391**

### Notable Highlights

**plurigrid (100 repos):** gorj (866 open issues, pushed 2026-06-27), asi (26⭐, HTML "everything is topological chemputer!"), zig-syrup, nanoclj-zig, Gay.jl integrations, GF(3) color tooling, category theory, cosmwasm  
**kubeflow (48 repos):** pipelines (4158⭐), spark-operator (3129⭐), trainer (2125⭐), kubeflow/kubeflow (15749⭐), mcp-server, mcp-apache-spark-history-server  
**TeglonLabs (5 repos):** jank-crane (C++ GF3 IR hub), mathpix-gem (Ruby, 2⭐), coin-flip-mcp (JS, 2 forks), monad-mcp-server, topoi (Python)  
**bmorphism (100 repos):** Gay.jl (2⭐, 187 issues), ocaml-mcp-sdk (61⭐), anti-bullshit-mcp-server (23⭐), manifold-mcp-server (14⭐), say-mcp-server (20⭐), open-games-agda, multiverse-color-game, vibespace-mcp-go-ternary  
**zubyul (49 repos):** voice-observatory, gay-world (1⭐), Nash TUI/web, tilelang-kernels, openbci-visualizer, Gay.jl fork, vibesnipe  
**migalkin (19 repos):** NodePiece (144⭐, ICLR'22), StarE (89⭐, EMNLP'20), NBFNet_mlx (10⭐, Apple Silicon)  
**AustinCStone (40 repos):** TextGAN (92⭐), StereoVisionMRF (11⭐), StructureFromMotion, ML/CV research  
**wasita (11 repos):** wasita.github.io (Svelte, 2026-06-25), wm-cv, vocoder, magic-garden  
**DJedamski (6 repos):** kaggle_ncaa18, Project_Euler, R coursera projects  
**kristinezheng (5 repos):** personal site (HTML, 2026-06-07), lookit-jenga, HackMIT 2021  
**M1shaaa (8 repos):** active profile (pushed 2026-06-27 today), lab-bookshelf- (TypeScript), MNIST-Classifier  

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, mainnet)

All 28 Hamming swarm addresses (alice, bob, A–Z) queried against `fullnode.mainnet.aptoslabs.com`.  
**Result: All balances = 0.0 APT** — accounts have no CoinStore<AptosCoin> resource or zero coin balance.

| World | Address (truncated) | APT |
|-------|---------------------|-----|
| alice | 0xc793ac...cc7b | 0.0 |
| bob | 0x0a3c00...2d5d | 0.0 |
| A–Z | 0x869..–0x7af0ef... | 0.0 each |

Total Hamming swarm balance: **0.0 APT**

### Multisig Contract Probes (5 pairs)

Probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428a0c007da... | **2** | ✅ healthy |
| A-G | 0xf56c4a1c09062... | **2** | ✅ healthy |
| Y-Z | 0xd3ffe1812b2df4... | **2** | ✅ healthy |
| S-T | 0x3b1c3ae905d44c... | **2** | ✅ healthy |
| V-W | 0x40fad7b423a843... | **2** | ✅ healthy |

All 5 multisig contracts: **2-of-N threshold, all responsive and healthy.**

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable.** `testnet.mnx.fi` is a Vercel-deployed SPA requiring authentication. All probed paths (`/`, `/api/markets`, `/api/v1/markets`, `/markets`, `/api/tickers`) return auth gate HTML. No market data accessible without bypass token.

---

## DuckDB Summary

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows | Notes |
|-------|------|-------|
| world_increments | 11 | One per source, GF3 color assigned |
| repo_snapshots | 391 | Full repo metadata for all sources |
| aptos_snapshots | 28 | All Hamming swarm addresses |
| multisig_probes | 5 | A-B, A-G, Y-Z, S-T, V-W |
| mnx_snapshots | 0 | Auth-gated, unavailable |

### GF(3) Color Chain (id % 3)
- `trit=0 ERGODIC #d3869b`: TeglonLabs(3), migalkin(6), DJedamski(9)
- `trit=1 PLUS #b8bb26`: plurigrid(1), bmorphism(4), AustinCStone(7), kristinezheng(10)
- `trit=-1 MINUS #cc241d`: kubeflow(2), zubyul(5), wasita(8), M1shaaa(11)
