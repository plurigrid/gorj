# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-06-15  
**Branch:** world-increment/sweep-2026-06-15-0712  
**GF(3) Color Chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d → ...

---

## JOB 1: GitHub Social Graph Sweep

### Orgs Snapshot

| Source | Total Repos Found | Top Repo (Stars) | Last Pushed |
|--------|------------------|------------------|-------------|
| plurigrid | 101 | asi (26★) | 2026-06-10 |
| kubeflow | 48 | kubeflow/kubeflow (15722★) | 2026-06-14 |
| TeglonLabs | 5 | mathpix-gem (2★) | 2026-01-01 |

**Highlights:**
- `plurigrid/gorj` (this repo): 588 open issues, Clojure, pushed today 2026-06-15
- `plurigrid/asi` (26★): "everything is topological chemputer!" — HTML, active
- `plurigrid/nanoclj-zig` (1★): NaN-boxed Clojure interpreter in Zig 0.15 with GF(3) trit conservation
- `plurigrid/eirobri`: 29 open issues, EiRoBri replay world
- `kubeflow/kubeflow` (15722★): flagship ML on Kubernetes toolkit
- `kubeflow/pipelines` (4154★): ML Pipelines, pushed 2026-06-14
- `kubeflow/trainer` (2115★): Distributed AI/LLM fine-tuning, pushed 2026-06-13
- `kubeflow/spark-operator` (3127★): Kubernetes Spark operator
- `kubeflow/mcp-apache-spark-history-server` (177★): MCP server for Spark debugging
- `TeglonLabs/jank-crane` (C++): pushed 2026-06-08, crane-jank converged-IR hub w/ GF3 convergence maps

### Users Snapshot

| User | Total Repos | Top Repo (Stars) | Focus |
|------|-------------|------------------|-------|
| bmorphism | 104 | ocaml-mcp-sdk (61★) | MCP servers, categorical CS, Gay.jl |
| zubyul | 49 | WGCNA (2★) | Bio/neuro data, Gay.jl worlds |

**bmorphism highlights:**
- `ocaml-mcp-sdk` (61★): OCaml SDK for MCP via Jane Street's oxcaml_effect
- `anti-bullshit-mcp-server` (23★): epistemological validation MCP
- `Gay.jl` (1★, 189 open issues): wide-gamut color sampling, pushed **2026-06-15** (today)
- `satreadout` (Lean 4.28): machine-checked saturating perceptual readout, pushed 2026-06-10

**zubyul highlights:**
- `gay-world` (Python, 1★): goblin world builder + MLX task decomposition
- `nash-tui` / `nash-web`: NASH token TUI via GeckoTerminal OHLCV
- `plurigrid-site`: Svelte world deployment, 11 open issues

### Zubyul Social Graph

| User | Repos | Top Stars | Activity |
|------|-------|-----------|----------|
| migalkin | 19 | NodePiece (144★), StarE (89★) | KG/GNN research |
| DJedamski | 6 | Getting-and-Cleaning-Data (1★) | Dormant since 2018 |
| wasita | 11 | magic-garden (2★) | Svelte, TypeScript, kobo, WiNS |
| kristinezheng | 5 | (0★) | MIT neuro/psych research |
| M1shaaa | 8 | M1shaaa profile updated **today** | Yale, MIT Lookit |
| AustinCStone | 40 | TextGAN (92★) | Python ML, vision, GAN |

**Notable signals:**
- `M1shaaa/M1shaaa` profile pushed **2026-06-15 03:55 UTC** (today — active)
- `migalkin` is leading knowledge graph ML (NodePiece 144★, StarE 89★)
- `wasita` has active web presence: personal site, kobo tool, WiNS search, vocoder (all 2025-2026)
- `AustinCStone/bmfork` repo (Python, 1 open issue) pushed 2025-05-09 links back to bmorphism orbit

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 Hamming swarm addresses probed at `fullnode.mainnet.aptoslabs.com/v1`.

**Result: All 28 addresses return 0.00000000 APT balance.**  
The `CoinStore<AptosCoin>` resource is present (no 404 errors), indicating accounts are registered on-chain but have zero funded balance on mainnet.

| Range | Sample Address | APT Balance |
|-------|---------------|-------------|
| alice | 0xc793...cc7b | 0.00000000 |
| bob | 0x0a3c...2d5d | 0.00000000 |
| A–M | 0x8699...→0x6fed... | 0.00000000 each |
| N–Z | 0xe7dd...→0x7af0... | 0.00000000 each |

### Multisig Contract Probes

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4...7003 | **2** | ✅ Healthy |
| A-G | 0xf56c...0096 | **2** | ✅ Healthy |
| Y-Z | 0xd3ff...b883 | **2** | ✅ Healthy |
| S-T | 0x3b1c...7883 | **2** | ✅ Healthy |
| V-W | 0x40fa...eb6d | **2** | ✅ Healthy |

All 5 multisig accounts require exactly **2-of-N** signatures. All contracts respond correctly to `0x1::multisig_account::num_signatures_required`.

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — `testnet.mnx.fi` is behind Vercel authentication (visitor password gate). Market data could not be extracted. Both `/api/markets` and `/api/v1/markets` paths redirect to auth gate. `mnx_snapshots` table has 0 rows.

---

## DuckDB Schema Summary

**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Description |
|-------|-------------|
| `world_increments` | GF(3)-colored sweep increments (34 rows, 11 sources) |
| `repo_snapshots` | GitHub repo snapshots across all sources (1277 rows) |
| `aptos_snapshots` | Hamming swarm APT balances (28 rows) |
| `multisig_probes` | Multisig contract health checks (5 rows) |
| `mnx_snapshots` | MNX markets — auth-gated, empty (0 rows) |

### Sources by Increment Type

| Type | Source | Repos Snapshotted |
|------|--------|-------------------|
| org_snapshot | plurigrid | 101 |
| org_snapshot | kubeflow | 48 |
| org_snapshot | bmorphism | 104 |
| org_snapshot | zubyul | 49 |
| org_snapshot | TeglonLabs | 5 |
| social_graph | migalkin | 6 |
| social_graph | DJedamski | 6 |
| social_graph | wasita | 6 |
| social_graph | kristinezheng | 4 |
| social_graph | M1shaaa | 4 |
| social_graph | AustinCStone | 5 |

---

## GF(3) Color Chain (primary increments)

| # | Source | Trit | Color | Name |
|---|--------|------|-------|------|
| 1 | plurigrid | 1 | #b8bb26 | PLUS |
| 2 | kubeflow | -1 | #cc241d | MINUS |
| 3 | bmorphism | 0 | #d3869b | ERGODIC |
| 4 | zubyul | 1 | #b8bb26 | PLUS |
| 5 | TeglonLabs | -1 | #cc241d | MINUS |
| 6 | migalkin | 0 | #d3869b | ERGODIC |
| 7 | DJedamski | 1 | #b8bb26 | PLUS |
| 8 | wasita | -1 | #cc241d | MINUS |
| 9 | kristinezheng | 0 | #d3869b | ERGODIC |
| 10 | M1shaaa | 1 | #b8bb26 | PLUS |
| 11 | AustinCStone | -1 | #cc241d | MINUS |

---

*Sweep completed: 2026-06-15 07:12 UTC. Next recommended: 2026-06-16.*
