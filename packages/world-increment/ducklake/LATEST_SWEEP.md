# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-08

## Sweep Metadata
- **Date:** 2026-05-08
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Previous sweep:** 2026-04-12

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts (Today's Sweep)

| Metric | Value |
|--------|-------|
| World Increments | 11 |
| Repo Snapshots (today) | 350 |
| Sources: Orgs | 3 (plurigrid, kubeflow, TeglonLabs) |
| Sources: Users | 8 (bmorphism, zubyul + 6 social graph) |

---

### GF(3) Color Chain — 11 Increments

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 1  | plurigrid | org | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | org | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | user | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | user | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | user | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | user | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | user | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

### Repos by Source (Today)

| Source | Repos | Stars | Top Repo |
|--------|-------|-------|----------|
| kubeflow | 48 | 34,022 | spark-operator (3,124★) |
| migalkin | 8 | 279 | NodePiece (144★) |
| bmorphism | 100 | 248 | ocaml-mcp-sdk (60★) |
| AustinCStone | 10 | 107 | TextGAN (92★) |
| plurigrid | 100 | 70 | asi (21★) |
| zubyul | 49 | 14 | wasita.github.io (1★) |
| wasita | 11 | 4 | magic-garden (2★) |
| DJedamski | 6 | 3 | Kaggle (1★) |
| TeglonLabs | 4 | 2 | mathpix-gem (2★) |
| kristinezheng | 6 | 0 | — |
| M1shaaa | 8 | 0 | — |

### Notable Activity Since April 2026

**plurigrid:**
- `gorj` (this repo) — Clojure, pushed 2026-05-08 — forj + Rama topology nREPL routing + GF(3) coloring
- `zig-syrup` — Zig, pushed 2026-04-30 — OCapN Syrup + CapTP
- `nash-portal` — Rust, pushed 2026-04-26 — NASH token TUI with GeckoTerminal OHLCV
- `horse` — TeX, pushed 2026-05-07

**bmorphism:**
- `Gay.jl` — Julia, pushed 2026-05-08
- `nanoclj-zig` — Zig, pushed 2026-05-07
- `boxxy` — Move, pushed 2026-04-30

**wasita (zubyul social graph):**
- `vocoder` — JavaScript, pushed 2026-05-06 (new repo)
- `wasita.github.io` — Svelte, pushed 2026-04-28

**zubyul:**
- `voice-observatory` — Python, pushed 2026-04-24 — passive macOS TUI for voice-download pathways
- `ghostel-emacs-worlds` — GLSL, pushed 2026-04-24

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All 28 Hamming swarm addresses queried via Aptos fullnode mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...f956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

> All balances: 0.0 APT — addresses exist on-chain but CoinStore is empty or not initialized.

---

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All 5 multisig contracts require **2-of-N** signatures. All healthy.

---

### MNX Markets (testnet.mnx.fi)

Status: **SPA — no REST API endpoint available.** `https://testnet.mnx.fi/api/markets` returns a Next.js rendered HTML page. Market data loads client-side; no JSON API reachable server-side.

---

## DuckDB Tables Summary

| Table | Rows (today) | Total Rows (cumulative) |
|-------|-------------|------------------------|
| `world_increments` | 11 | 34 |
| `repo_snapshots` | 350 | 1,294 |
| `aptos_snapshots` | 28 | 28 |
| `multisig_probes` | 5 | 5 |
| `mnx_snapshots` | 1 (N/A) | 1 |

---

## Cross-Sweep Delta (Apr 12 → May 8)

| Source | Notable Changes |
|--------|----------------|
| plurigrid | gorj, zig-syrup, nash-portal, horse all active |
| kubeflow | +1 new repo (mlflow-integration), website + spark-operator pushed today |
| bmorphism | Gay.jl, nanoclj-zig both pushed this week |
| zubyul | voice-observatory new (Apr 2026) |
| wasita | vocoder new repo (May 6, 2026) |
| TeglonLabs | mathpix-gem added Oct 2025; now 4 public repos |
