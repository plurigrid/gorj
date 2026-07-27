# World-Increment Sweep + Hamming Snapshot

**Date:** 2026-07-27  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| plurigrid | org | 100 | 102 |
| bmorphism | user | 100 | 246 |
| kubeflow | org | 49 | 34,413 |
| zubyul | user | 49 | 14 |
| TeglonLabs | org | 5 | 2 |
| migalkin | user (social graph) | 5 | 275 |
| wasita | user (social graph) | 3 | 4 |
| AustinCStone | user (social graph) | 3 | 103 |
| DJedamski | user (social graph) | 2 | 1 |
| M1shaaa | user (social graph) | 2 | 0 |
| kristinezheng | user (social graph) | 1 | 0 |
| **TOTAL** | | **319** | **35,160** |

### GF(3) Color Chain Distribution

| GF3 Name | Trit | Color | Count |
|----------|------|-------|-------|
| ERGODIC | 0 | #d3869b | 106 |
| PLUS | +1 | #b8bb26 | 107 |
| MINUS | -1 | #cc241d | 106 |

### Notable Active Repos (most recently pushed)

- **plurigrid/gorj** (Clojure) — forj + GF(3) gay trit coloring, pushed 2026-07-27
- **bmorphism/Gay.jl** (Julia) — wide-gamut GF(3) color sampling, pushed 2026-07-27
- **kubeflow/pipelines** (Python) — 4,170★, pushed 2026-07-27
- **kubeflow/trainer** (Go) — 2,154★ distributed AI training, pushed 2026-07-27
- **kubeflow/kubeflow** — 15,793★ ML toolkit flagship
- **wasita/wasita.github.io** (Svelte) — active personal site, pushed 2026-07-21
- **migalkin/NodePiece** (Python) — 144★ ICLR 2022 KG embeddings
- **TeglonLabs/jank-crane** (C++) — crane-jank converged-IR hub with GF3 convergence maps

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (alice, bob, A–Z)

All 28 probed addresses returned `resource_not_found` for
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version 6,473,067,730.
Accounts exist on-chain but have not initialized an APT CoinStore — balance NULL.

### Multisig Contract Probes (5/5 healthy)

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428a0c007da... | 2 | healthy |
| A-G | 0xf56c4a1c0906214f... | 2 | healthy |
| Y-Z | 0xd3ffe1812b2df406... | 2 | healthy |
| S-T | 0x3b1c3ae905d44c3a... | 2 | healthy |
| V-W | 0x40fad7b423a84365... | 2 | healthy |

All 5 multisig contracts on-chain, 2-of-N sigs required, healthy.

### MNX Markets (testnet.mnx.fi)

Returns Next.js SPA — no REST API found at `/api/markets` or `/api/v1/markets`.
`mnx_snapshots` table is empty this sweep.

---

## DuckDB Tables

```
world_increments   319 rows  GF(3) color-chained increment log
repo_snapshots     319 rows  org/user/repo metadata snapshot
aptos_snapshots     28 rows  A-Z + alice/bob (NULL = uninitialized CoinStore)
multisig_probes      5 rows  all healthy, sigs_required=2
mnx_snapshots        0 rows  SPA unavailable
```
