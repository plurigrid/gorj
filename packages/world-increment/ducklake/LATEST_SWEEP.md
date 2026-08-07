# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-08-07  
**Run:** world-increment-sweep + hamming-swarm-snapshot

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured | Total Stars |
|--------|------|---------------|-------------|
| kubeflow | org | 49 (sampled 10) | 96,958 |
| bmorphism | user | 100 | 509 |
| plurigrid | org | 100 | 193 |
| AustinCStone | user | 20 | 319 |
| zubyul | user | 49 | 40 |
| migalkin | user | 19 | 279 |
| TeglonLabs | org | 5 | 2 |
| wasita | user | 14 | 4 |
| DJedamski | user | 6 | 3 |
| kristinezheng | user | 5 | 0 |
| M1shaaa | user | 8 | 0 |

### Notable Repos (Most Recent Activity)

- **plurigrid/gorj** — Clojure, 1 star — `forj + Rama topology nREPL routing + GF(3) gay trit coloring` — pushed 2026-08-07
- **plurigrid/place** — TeX, 2 stars — pushed 2026-08-02
- **plurigrid/zig-syrup** — Zig, 2 stars — High-performance OCapN Syrup — pushed 2026-07-28
- **plurigrid/asi** — HTML, 59 stars — `everything is topological chemputer!` — pushed 2026-07-10
- **bmorphism/Gay.jl** — Julia, 2 stars — Wide-gamut color sampling with splittable determinism — pushed 2026-08-07
- **bmorphism/ocaml-mcp-sdk** — OCaml, 61 stars — OCaml SDK for Model Context Protocol — pushed 2026-03-16
- **wasita/xoxowasita-analysis** — Python — pushed 2026-08-06 (very recent)
- **kubeflow/kubeflow** — 15,805 stars — Machine Learning Toolkit for Kubernetes — pushed 2026-08-04
- **kubeflow/pipelines** — 4,181 stars — pushed 2026-08-07
- **TeglonLabs/jank-crane** — C++ — crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps — pushed 2026-06-08

### GF(3) Color Chain Applied to Increments

| Increment | Source | GF3 Trit | Color | Name |
|-----------|--------|----------|-------|------|
| 1 | plurigrid (org) | 1 | #b8bb26 | PLUS |
| 2 | kubeflow (org) | -1 | #cc241d | MINUS |
| 3 | TeglonLabs (org) | 0 | #d3869b | ERGODIC |
| 4 | bmorphism (user) | 1 | #b8bb26 | PLUS |
| 5 | zubyul (user) | -1 | #cc241d | MINUS |
| 6 | migalkin (user) | 0 | #d3869b | ERGODIC |
| 7 | DJedamski (user) | 1 | #b8bb26 | PLUS |
| 8 | wasita (user) | -1 | #cc241d | MINUS |
| 9 | kristinezheng (user) | 0 | #d3869b | ERGODIC |
| 10 | M1shaaa (user) | 1 | #b8bb26 | PLUS |
| 11 | AustinCStone (user) | -1 | #cc241d | MINUS |

### DuckDB Schema (ducklake)

- `world_increments`: 34 rows (cumulative across runs)
- `repo_snapshots`: 1,230 rows (cumulative)
- `aptos_snapshots`: 28 rows (this run)
- `multisig_probes`: 5 rows (this run)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 wallets (alice, bob, A–Z) queried via Aptos fullnode mainnet API.

| Status | Count |
|--------|-------|
| 0.0 APT | 28/28 |

All wallets returned 0 APT balance. This may indicate:
- Wallets hold non-APT tokens (FA tokens, other coin types)
- Wallets not yet funded on mainnet
- CoinStore resource not registered (pre-FA migration pattern)

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428...4987003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c4a1c...fbc0096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ffe181...e75b883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c3ae9...3ded7883 | 2 | ✅ HEALTHY |
| V-W | 0x40fad7b4...c80eb6d | 2 | ✅ HEALTHY |

All multisig accounts require 2-of-N signatures and are responding on mainnet.

### MNX Markets (testnet.mnx.fi)

The MNX testnet is a Next.js SPA — no public REST API endpoints found at `/api/markets` or `/api/v1/markets`. The frontend loads dynamically; market data **unavailable via direct API probe**. Marked as SPA-only.

---

## Summary

| Category | Result |
|----------|--------|
| GitHub orgs/users swept | 11 (3 orgs + 8 users) |
| Total repos snapshotted | ~375 unique (1,230 cumulative DB rows) |
| Most active repo | plurigrid/gorj (pushed today 2026-08-07) |
| Aptos wallets checked | 28 (alice, bob, A–Z) |
| Total APT across swarm | 0.0 APT |
| Multisig contracts | 5/5 HEALTHY (2-sig threshold) |
| MNX Markets | SPA — no REST API |
| DuckDB | packages/world-increment/ducklake/world-increments.duckdb |
