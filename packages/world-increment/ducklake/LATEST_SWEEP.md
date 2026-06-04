# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-05-06T14:30 UTC  
**Branch:** world-increment/sweep-2026-05-06  
**GF(3) Color Chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d → …

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos | Total Stars | Latest Push |
|--------|------|-------|-------------|-------------|
| kubeflow | org | 47 | 97,752 | 2026-05-06 |
| migalkin | user (social) | 19 | 828 | 2026-04-16 |
| bmorphism | user | 101 | 460 | 2026-05-01 |
| AustinCStone | user (social) | 40 | 319 | 2026-04-01 |
| plurigrid | org | 100 | 135 | 2026-05-06 |
| zubyul | user | 49 | 29 | 2026-04-24 |
| TeglonLabs | org | 4 | 14 | 2026-01-01 |
| wasita | user (social) | 11 | 9 | 2026-05-06 |

### Highlighted Repos (Most Active / Notable)

**plurigrid:**
- `gorj` (Clojure, 86 issues) — forj + Rama topology nREPL routing + GF(3) gay trit coloring — pushed 2026-05-06
- `zig-syrup` (Zig, 2★) — High-performance OCapN Syrup with CapTP
- `asi` (HTML, 19★) — everything is topological chemputer!
- `nanoclj-zig` (Zig, 20 issues) — NaN-boxed Clojure in Zig 0.15

**kubeflow:**
- `kubeflow` (15,623★) — Machine Learning Toolkit for Kubernetes
- `pipelines` (Python, 4,133★) — ML Pipelines for Kubeflow
- `trainer` (Go, 2,095★) — Distributed AI Training + LLM Fine-Tuning on Kubernetes
- `spark-operator` (Python, 3,123★) — Kubernetes operator for Apache Spark
- `mcp-apache-spark-history-server` (Python, 164★) — NEW: MCP Server for Spark History Server

**bmorphism:**
- `ocaml-mcp-sdk` (OCaml, 60★) — OCaml SDK for Model Context Protocol
- `say-mcp-server` (JavaScript, 20★) — macOS TTS MCP server
- `babashka-mcp-server` (JavaScript, 18★) — Babashka/Clojure MCP server
- `Gay.jl` (Julia, 187 issues) — Wide-gamut color sampling, splittable determinism

**zubyul:**
- `voice-observatory` — Passive macOS TUI for voice-download pathways (companion to bmorphism/say-mcp-server)
- `gay-world` — Goblin world builder, MLX task decomposition
- `tilelang-kernels` — GPU kernels for SplitMix64 color generation + GF(3) trit classification

**migalkin (social graph):**
- `NodePiece` (Python, 143★) — ICLR'22: Compositional KG representations
- `StarE` (Python, 89★) — EMNLP 2020: Message Passing for Hyper-Relational KGs

**TeglonLabs:**
- `mathpix-gem` (Ruby, 2★) — Mathematical OCR, geodesic path in Ruby
- `coin-flip-mcp` (JavaScript) — MCP server for random.org coin flips

### GF(3) Increment Chain

| ID | Trit | Color | Name | Source |
|----|------|-------|------|--------|
| 1 | 0 | #d3869b | ERGODIC | org:plurigrid |
| 2 | 1 | #b8bb26 | PLUS | org:kubeflow |
| 3 | 2 | #cc241d | MINUS | org:TeglonLabs |
| 4 | 0 | #d3869b | ERGODIC | user:bmorphism |
| 5 | 1 | #b8bb26 | PLUS | user:zubyul |
| 6 | 2 | #cc241d | MINUS | user:migalkin |
| 7 | 0 | #d3869b | ERGODIC | user:AustinCStone |
| 8 | 1 | #b8bb26 | PLUS | user:wasita |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 wallets (alice, bob, A-Z) queried via Aptos mainnet fullnode.  
**Result: All wallets returned 0.00000000 APT** — accounts are unfunded or CoinStore resource not initialized on mainnet.

| World | Balance (APT) |
|-------|---------------|
| alice | 0.00000000 |
| bob   | 0.00000000 |
| A-Z   | 0.00000000 each |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...87003 | 2 | YES |
| A-G | 0xf56c4a1c...0096 | 2 | YES |
| Y-Z | 0xd3ffe181...b883 | 2 | YES |
| S-T | 0x3b1c3ae9...7883 | 2 | YES |
| V-W | 0x40fad7b4...eb6d | 2 | YES |

**All 5 multisig contracts are 2-of-2 and healthy.**

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable for structured data extraction.**  
`testnet.mnx.fi` is a Next.js SPA — API routes (`/api/markets`, `/api/v1/markets`, `/api/tickers`) return the HTML shell, not JSON. No market data extractable without browser-side JS execution. No mnx_snapshots rows inserted.

---

## DuckDB Schema Summary

Database: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows | Description |
|-------|------|-------------|
| world_increments | 31 | GF(3) color-chained increment records |
| repo_snapshots | 1012 | GitHub repo snapshots across all sources |
| aptos_snapshots | 28 | Hamming swarm wallet balances |
| multisig_probes | 5 | Aptos multisig health checks |
| mnx_snapshots | 0 | MNX market data (SPA — unavailable) |
