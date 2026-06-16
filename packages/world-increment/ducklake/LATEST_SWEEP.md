# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-16  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos Snapped | GF(3) Color | Trit |
|--------|------|--------------|-------------|------|
| plurigrid | org | 100 | #b8bb26 PLUS | +1 |
| kubeflow | org | 27 | #cc241d MINUS | -1 |
| TeglonLabs | org | 5 | #d3869b ERGODIC | 0 |
| bmorphism | user | 34 | #b8bb26 PLUS | +1 |
| zubyul | user | 19 | #cc241d MINUS | -1 |
| migalkin | user | 9 | #d3869b ERGODIC | 0 |
| DJedamski | user | 6 | #b8bb26 PLUS | +1 |
| wasita | user | 6 | #cc241d MINUS | -1 |
| kristinezheng | user | 5 | #d3869b ERGODIC | 0 |
| M1shaaa | user | 5 | #b8bb26 PLUS | +1 |
| AustinCStone | user | 7 | #cc241d MINUS | -1 |

**Total repos snapped this run:** 223  
**Cumulative repo_snapshots:** 1,167  
**Total world_increments:** 34

### Notable Repos (new pushes near sweep date)

- `plurigrid/gorj` — Clojure, pushed 2026-06-16, 616 open issues — forj + Rama topology + GF(3) gay trit coloring
- `plurigrid/place` — TeX, pushed 2026-06-15, 8 open issues
- `plurigrid/eirobri` — Clojure, pushed 2026-06-03, 29 open issues — EiRoBri replay world
- `plurigrid/asi` — HTML, pushed 2026-06-10, 26 stars — "everything is topological chemputer!"
- `kubeflow/community` — pushed 2026-06-16, 194 stars
- `kubeflow/trainer` — Go, pushed 2026-06-16, 2115 stars — Distributed AI Model Training on Kubernetes
- `kubeflow/pipelines` — Python, pushed 2026-06-16, 4154 stars — Machine Learning Pipelines
- `kubeflow/dashboard` — TypeScript, pushed 2026-06-16, 76 open issues
- `bmorphism/Gay.jl` — Julia, pushed 2026-06-16, 187 open issues — Wide-gamut color sampling
- `bmorphism/satreadout` — Lean, pushed 2026-06-15 — Machine-checked saturating perceptual readout
- `wasita/wasita.github.io` — Svelte, pushed 2026-06-15, 8 open issues
- `TeglonLabs/jank-crane` — C++, pushed 2026-06-08 — crane-jank converged-IR hub, GF3 convergence maps
- `kristinezheng/kristinezheng.github.io` — HTML, pushed 2026-06-07

### GF(3) Trit Chain (this run, ids 13–23)

```
id=13 plurigrid    → trit=+1 #b8bb26 PLUS
id=14 kubeflow     → trit=-1 #cc241d MINUS
id=15 TeglonLabs   → trit=0  #d3869b ERGODIC
id=16 bmorphism    → trit=+1 #b8bb26 PLUS
id=17 zubyul       → trit=-1 #cc241d MINUS
id=18 migalkin     → trit=0  #d3869b ERGODIC
id=19 DJedamski    → trit=+1 #b8bb26 PLUS
id=20 wasita       → trit=-1 #cc241d MINUS
id=21 kristinezheng→ trit=0  #d3869b ERGODIC
id=22 M1shaaa      → trit=+1 #b8bb26 PLUS
id=23 AustinCStone → trit=-1 #cc241d MINUS
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Balances (28 addresses)

All 28 Hamming swarm addresses returned `balance_apt = -1.0` — the Aptos mainnet
fullnode returned resource-not-found for each `CoinStore<AptosCoin>` lookup.
These addresses appear to be unregistered or unfunded on mainnet.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | not found |
| bob   | 0x0a3c...12d5 | not found |
| A–Z   | (26 addresses) | not found |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **healthy** with `sigs_required = 2`:

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4...7003 | 2 | yes |
| A-G | 0xf56c...0096 | 2 | yes |
| Y-Z | 0xd3ff...b883 | 2 | yes |
| S-T | 0x3b1c...7883 | 2 | yes |
| V-W | 0x40fa...eb6d | 2 | yes |

All multisigs maintain 2-of-N threshold on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)

Status: **unavailable** — `https://testnet.mnx.fi/api/markets` returned no valid data (SPA or offline). No market snapshots recorded.

---

## DuckDB Tables State

```
world_increments  : 34 rows  (11 new this run)
repo_snapshots    : 1,167 rows (223 new this run)
aptos_snapshots   : 28 rows   (28 new this run, all not found on mainnet)
multisig_probes   : 5 rows    (5 new this run, all healthy sigs=2)
mnx_snapshots     : 0 rows    (testnet.mnx.fi unavailable)
```
