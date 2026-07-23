# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-23  
**Run type:** Automated scheduled sweep

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| # | Source | Type | Repos | GF3 | Color |
|---|--------|------|-------|-----|-------|
| 1 | plurigrid | org | 100 | trit=1 PLUS | #b8bb26 |
| 2 | kubeflow | org | 49 | trit=-1 MINUS | #cc241d |
| 3 | TeglonLabs | org | 5 | trit=0 ERGODIC | #d3869b |
| 4 | bmorphism | user | 100 | trit=1 PLUS | #b8bb26 |
| 5 | zubyul | user | 49 | trit=-1 MINUS | #cc241d |
| 6 | social_graph | user | 91 | trit=0 ERGODIC | #d3869b |

**Total repos snapshotted: 394**

### Notable Repos (by recent push)

**plurigrid** (top 5 by pushed_at):
- `plurigrid/asi` (HTML, ⭐31) — pushed 2026-07-10
- `plurigrid/gorj` (Clojure, ⭐1) — pushed 2026-07-23
- `plurigrid/place` (TeX, ⭐1) — pushed 2026-07-14
- `plurigrid/eirobri` (Clojure) — pushed 2026-07-21
- `plurigrid/shrimp` — pushed 2026-07-03

**bmorphism** (top 5 by pushed_at):
- `bmorphism/Gay.jl` (Julia, ⭐2) — pushed 2026-07-23
- `bmorphism/gay-chat` (Scheme) — pushed 2026-07-14
- `bmorphism/satreadout` (HTML) — pushed 2026-06-20
- `bmorphism/world` (Python) — pushed 2026-06-02

**TeglonLabs** (5 repos):
- `TeglonLabs/jank-crane` (C++) — crane-jank converged-IR hub, GF3 convergence maps
- `TeglonLabs/mathpix-gem` (Ruby, ⭐2, 11 open issues) — pushed 2026-01-01
- `TeglonLabs/coin-flip-mcp` (JavaScript, 2 forks)

**social graph** (zubyul connections — migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone):
- 91 repos total
- `wasita/wasita.github.io` (Svelte) — pushed 2026-07-21
- `AustinCStone/byteruckus` (HTML) — pushed 2026-07-15

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)

**Total APT held: 20.3448 APT**

| World | Balance (APT) | Address (prefix) |
|-------|--------------|-----------------|
| bob | 12.6570 | 0x0a3c00c58f... |
| F | 1.9605 | 0x18a14b5b4b... |
| L | 1.9273 | 0x7c2eaeafad... |
| J | 1.8951 | 0x4d964db8f5... |
| alice | 0.4364 | 0xc793acdec1... |
| K | 0.1620 | 0xa732040a6b... |
| O | 0.2101 | 0x73252b6011... |
| P | 0.1401 | 0x62187902de... |
| M | 0.1123 | 0x6fed37a755... |
| N | 0.1061 | 0xe7dde6da0a... |
| Q | 0.1032 | 0xac40fa50b8... |
| R | 0.0902 | 0x7ce605cc8f... |
| S | 0.0918 | 0xb8753014e4... |
| T | 0.0737 | 0x35781dc0e4... |
| U | 0.0558 | 0x75860da475... |
| A | 0.0518 | 0x8699edc096... |
| X | 0.0426 | 0xa95cbbd116... |
| Y | 0.0444 | 0xd8e32848f1... |
| V | 0.0488 | 0xb59dd81703... |
| W | 0.0407 | 0x5f32aef70f... |
| B | 0.0363 | 0x3f892ebe6e... |
| Z | 0.0243 | 0x7af0ef6e1b... |
| C | 0.0102 | 0x38b99e63ad... |
| D | 0.0116 | 0xf77656248f... |
| E | 0.0094 | 0xdc1d9d533b... |
| H | 0.0017 | 0xce67c327a7... |
| G | 0.0007 | 0x69a394c0b0... |
| I | 0.0007 | 0x070fe5d74e... |

*Method: `0x1::coin::balance` view function (coin module, not legacy CoinStore)*  
*Note: Alice has an on-chain `ACSetMeta2` resource (877 objects, 148 morphisms) and a `multiverse::MultiverseState` resource — active on-chain computation.*

### Multisig Contract Probes (5 pairs)

All 5 multisig accounts are **HEALTHY** — each requiring **2 signatures**:

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428... | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a1c... | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe181... | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3ae9... | 2 | ✓ HEALTHY |
| V-W | 0x40fad7b4... | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — site returns a Next.js SPA (no REST API exposed). All routes (`/`, `/api/markets`, `/api/v1/markets`) return the same HTML shell. Market data not extractable without browser-side JavaScript execution.

---

## DuckDB Tables Updated

- `world_increments` — 6 rows (one per source sweep)
- `repo_snapshots` — 394 rows
- `aptos_snapshots` — 28 rows (28/28 successful)
- `multisig_probes` — 5 rows (5/5 healthy)
- `mnx_snapshots` — 1 row (unavailable marker)

**DB path:** `packages/world-increment/ducklake/world-increments.duckdb`
