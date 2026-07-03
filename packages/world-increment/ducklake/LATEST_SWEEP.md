# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-03T21:30Z  
**GF(3) chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social) | 19 |
| AustinCStone | user (social) | 30 |
| wasita | user (social) | 11 |
| DJedamski | user (social) | 6 |
| kristinezheng | user (social) | 5 |
| M1shaaa | user (social) | 8 |
| **Total** | | **381** |

### Notable Repos

- `kubeflow/kubeflow` — 15760 ⭐ ML Toolkit for Kubernetes, pushed 2026-06-18
- `kubeflow/pipelines` — 4169 ⭐ ML Pipelines, active 2026-07-03
- `kubeflow/trainer` — 2129 ⭐ Distributed AI training, active 2026-07-03
- `kubeflow/spark-operator` — 3132 ⭐ Kubernetes Spark operator, active 2026-07-02
- `plurigrid/gorj` — 948 open issues, Clojure+GF(3), pushed 2026-07-03
- `plurigrid/asi` — 28 ⭐ topological chemputer, pushed 2026-06-29
- `bmorphism/Gay.jl` — 187 open issues, Julia wide-gamut color, active 2026-07-03
- `bmorphism/ocaml-mcp-sdk` — 61 ⭐ OCaml MCP SDK
- `TeglonLabs/jank-crane` — C++, crane-jank converged-IR hub, 2026-06-08

### GF(3) Color Chain Distribution

```
ERGODIC #d3869b  trit=0   127 increments
PLUS    #b8bb26  trit=1   127 increments
MINUS   #cc241d  trit=-1  127 increments
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 wallets)

All 28 wallets (alice, bob, A–Z) queried via `fullnode.mainnet.aptoslabs.com`.

All 28 wallets returned **0.0 APT** — unfunded or CoinStore resources not initialized.

### Multisig Contract Probes

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428…987003 | 2 | healthy |
| A-G | 0xf56c4a1c…c0096 | 2 | healthy |
| Y-Z | 0xd3ffe181…75b883 | 2 | healthy |
| S-T | 0x3b1c3ae9…d7883 | 2 | healthy |
| V-W | 0x40fad7b4…0eb6d | 2 | healthy |

All multisig accounts are **2-of-2** and responding normally.

### MNX Markets (testnet.mnx.fi)

Unavailable — Vercel authentication required. No market data extracted.

---

## DuckDB Tables

| Table | Rows |
|-------|------|
| world_increments | 381 |
| repo_snapshots | 381 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |
