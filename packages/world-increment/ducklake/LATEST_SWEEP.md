# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-08-08  
**GF(3) Color Chain:** ERGODIC=#d3869b | PLUS=#b8bb26 | MINUS=#cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Fetched |
|--------|------|--------------|
| plurigrid | org | 100 (103 total) |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 80+ |
| zubyul | user | 49 |
| migalkin | social graph | 19 |
| wasita | social graph | 14 |
| AustinCStone | social graph | 31 |
| kristinezheng | social graph | 5 |
| M1shaaa | social graph | 8 |
| DJedamski | social graph | 6 |

### Highlights

**plurigrid** (103 repos, most-pushed 2026-08-08):
- `plurigrid/place` — TeX — pushed today
- `plurigrid/gorj` — Clojure — forj + Rama topology nREPL routing + GF(3) gay trit coloring — pushed today
- `plurigrid/eirobri` — Clojure — EiRoBri replay world — pushed 2026-08-04
- `plurigrid/zig-syrup` — Zig — OCapN Syrup high-performance impl — pushed 2026-07-28
- `plurigrid/asi` — HTML — 59 stars — everything is topological chemputer

**kubeflow** (49 repos, active):
- `kubeflow/spark-operator` — Python — 3,145 stars — pushed today
- `kubeflow/trainer` — Go — 2,176 stars — pushed today
- `kubeflow/pipelines` — Python — 4,182 stars — pushed 2026-08-07
- `kubeflow/mcp-apache-spark-history-server` — Python — 188 stars

**TeglonLabs** (5 repos):
- `TeglonLabs/jank-crane` — C++ — crane-jank converged-IR hub, GF3 convergence maps
- `TeglonLabs/mathpix-gem` — Ruby — 2 stars, 11 open issues

**bmorphism** (106 repos):
- `bmorphism/ocaml-mcp-sdk` — OCaml — 61 stars — Jane Street oxcaml_effect
- `bmorphism/anti-bullshit-mcp-server` — JavaScript — 23 stars
- `bmorphism/Gay.jl` — Julia — 2 stars, 188 open issues — Wide-gamut color sampling

**wasita** — very active: pushed `xoxowasita-analysis` and `wm-cv` this week (2026-08-06/07)

**migalkin** — `NodePiece` 144 stars (ICLR'22 KG representation), `StarE` 89 stars (EMNLP'20)

### DuckDB Stats
- `world_increments`: 199 rows (GF3-colored, incremental IDs)
- `repo_snapshots`: 1,120 rows (multi-run accumulation)
- DB: `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses (alice, bob, A–Z) queried against Aptos mainnet fullnode.

| Result | Count |
|--------|-------|
| Balance = 0 APT | 28 |
| Balance > 0 APT | 0 |

All Hamming swarm wallets currently hold **0 APT**. The accounts exist on mainnet (CoinStore resource confirmed as empty or not initialized).

#### Address Sample

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...12d5 | 0.0 |
| A | 0x8699...b97a | 0.0 |
| Z | 0x7af0...97c | 0.0 |

### Multisig Contract Probes (5/5 healthy)

All 5 multisig contracts respond to `0x1::multisig_account::num_signatures_required`:

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✓ HEALTHY |

All multisigs require **2-of-N** signatures. All contracts reachable and responding.

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi/api/markets` — **unavailable** (pure client-side Next.js SPA; no REST API endpoint accessible server-side). The SPA returns HTML with JS bundles only; no market data extractable without browser execution.

---

## GF(3) Trit Color Chain Summary

| Trit | Color | Name | Meaning |
|------|-------|------|---------|
| 0 | #d3869b | ERGODIC | Neutral/Identity |
| 1 | #b8bb26 | PLUS | Positive increment |
| -1 | #cc241d | MINUS | Negative increment |

World increments are colored by `id % 3` across all repo push events and social graph snapshots.
