# World-Increment Sweep — 2026-07-14

## Sweep Metadata
- **Date:** 2026-07-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 36 (13 new this run) |
| Total Repo Snapshots | 1168 (224 new this run) |
| Sources Covered | 3 orgs + 8 users + 2 event streams |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Testnet | SPA only — no JSON API accessible |

---

## GF(3) Color Chain — New Increments This Run (IDs 13–25)

| ID | Source | Type | Event | GF3 Trit | Color | Name |
|----|--------|------|-------|-----------|-------|------|
| 13 | plurigrid (org) | org | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 14 | kubeflow (org) | org | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 15 | TeglonLabs (org) | org | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 16 | bmorphism (user) | user | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 17 | zubyul (user) | user | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 18 | migalkin (user) | user | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 19 | DJedamski (user) | user | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 20 | wasita (user) | user | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 21 | kristinezheng (user) | user | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 22 | M1shaaa (user) | user | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 23 | AustinCStone (user) | user | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 24 | bmorphism (events) | events | public_events | 0 | `#d3869b` | **ERGODIC** |
| 25 | zubyul (events) | events | public_events | +1 | `#b8bb26` | **PLUS** |

---

## GitHub Repo Highlights (New This Run)

### plurigrid (100 repos)
- **Most recently pushed:** `plurigrid/gorj` (2026-07-14) — Clojure, MCP REPL server
- **plurigrid/asi** — HTML, 30 stars, pushed 2026-07-10
- **plurigrid/place** — TeX, forester preview
- **plurigrid/eirobri** — Clojure

### kubeflow (49 repos)
- **kubeflow/pipelines** — Python, 4165 stars, active (pushed 2026-07-13)
- **kubeflow/trainer** — Go, 2138 stars
- **kubeflow/spark-operator** — Python, 3135 stars

### TeglonLabs (5 repos)
- **TeglonLabs/jank-crane** — C++, crane-jank converged-IR hub w/ GF3 convergence maps (pushed 2026-06-08)
- **TeglonLabs/mathpix-gem** — Ruby, 2 stars, math OCR

### bmorphism (105 total public repos)
- **bmorphism/anti-bullshit-mcp-server** — 22 stars, updated 2026-07-12
- **bmorphism/ocaml-mcp-sdk** — 61 stars, OCaml MCP SDK
- **bmorphism/satreadout** — new (2026-06-10), machine-checked Lean 4 perceptual readout
- **bmorphism/Gay.jl** — Julia, 2 stars, 187 open issues

### zubyul (49 repos)
- **zubyul/voice-observatory** — Python, passive macOS TUI for voice-download pathways
- **zubyul/ghostel-emacs-worlds** — GLSL, Ghostty + emacs stack (2026-04-24)
- **zubyul/gay-world** — Python, 1 star, goblin world builder

### Social Graph
- **migalkin:** 19 repos — KG researcher; NodePiece (144★), StarE (89★), kgcourse2021 active
- **DJedamski:** 6 repos — Kaggle/data science, mostly archived
- **wasita:** 11 repos — Svelte/neuroscience; wasita.github.io active (2026-07-06)
- **kristinezheng:** 5 repos — MIT/neuroscience; personal site updated 2026-07-01
- **M1shaaa:** 8 repos — Yale/cognitive science
- **AustinCStone:** 40 repos — TextGAN (92★), StereoVisionMRF (11★), bmfork variants (2025)

---

## Hamming Swarm Snapshot — Aptos Mainnet

### Wallet Balances (alice, bob, A–Z)

**Status:** Aptos fullnode coin resource endpoint returned empty responses for all 28 addresses via the environment proxy. The accounts may be zero-balance or the proxy blocked the resource path. Addresses recorded in `aptos_snapshots` table with `balance_apt = NULL`.

| World | Address (truncated) |
|-------|---------------------|
| alice | 0xc793...4cc7b |
| bob   | 0x0a3c...512d5d |
| A–Z   | see DuckDB `aptos_snapshots` |

### Multisig Contract Probes (5/5 HEALTHY ✓)

All five multisig pairs returned `num_signatures_required = 2`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✅ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✅ HEALTHY |

### MNX Testnet (testnet.mnx.fi)

All probed paths (`/api/markets`, `/api/v1/markets`, `/markets`) returned the SPA shell (13,462 bytes HTML). No JSON market data accessible without JavaScript execution. Recorded as `UNAVAILABLE` in `mnx_snapshots`.

---

## Notable Signals

1. **plurigrid/gorj** (this repo) was pushed today (2026-07-14) — sweep is current
2. **TeglonLabs/jank-crane** is new since last sweep — C++ with GF3 convergence maps, active June 2026
3. **bmorphism/anti-bullshit-mcp-server** updated 2026-07-12 — 22 stars, actively maintained
4. **All 5 Hamming multisigs healthy** — 2-of-2 threshold across all pairs
5. **Aptos coin balances unavailable** — proxy blocks fullnode resource path; multisig view endpoint works
6. **bmorphism/Gay.jl** has 187 open issues — may need attention
