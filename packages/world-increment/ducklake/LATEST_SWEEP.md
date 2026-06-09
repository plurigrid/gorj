# World-Increment Sweep + Hamming Snapshot

**Timestamp:** 2026-06-09  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social) | 19 |
| DJedamski | user (social) | 6 |
| wasita | user (social) | 11 |
| kristinezheng | user (social) | 5 |
| M1shaaa | user (social) | 8 |
| AustinCStone | user (social) | 10 |
| **TOTAL** | | **361** |

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,712 | — |
| kubeflow/pipelines | 4,153 | Python |
| kubeflow/spark-operator | 3,126 | Python |
| kubeflow/trainer | 2,112 | Go |
| kubeflow/katib | 1,685 | Python |
| kubeflow/examples | 1,462 | Jsonnet |
| kubeflow/manifests | 1,022 | YAML |
| kubeflow/arena | 812 | Go |
| AustinCStone/TextGAN | 92 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| migalkin/NodePiece | 144 | Python |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |
| bmorphism/risc0-cosmwasm-example | 23 | Rust |
| plurigrid/asi | 25 | HTML |

### Notable Recent Activity

- `plurigrid/gorj` pushed 2026-06-09 (456 open issues) — GF(3)+Rama REPL orchestration
- `bmorphism/Gay.jl` pushed 2026-06-09 (189 open issues) — Wide-gamut SPI coloring
- `kubeflow/pipelines` pushed 2026-06-09 — ML Pipelines for Kubeflow
- `TeglonLabs/jank-crane` pushed 2026-06-08 — C++ GF3 converged-IR hub
- `kubeflow/trainer` pushed 2026-06-08 — Distributed AI training on Kubernetes

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 120 |
| 1 | #b8bb26 | PLUS | 121 |
| 2 | #cc241d | MINUS | 120 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A-Z)

All 28 addresses queried against Aptos mainnet.
Result: All return resource_not_found for CoinStore<AptosCoin> (unfunded).

| World | Address | Balance (APT) |
|-------|---------|--------------|
| alice | 0xc793...c7b | 0.0 |
| bob | 0x0a3c...d5d | 0.0 |
| A-Z | (26 addresses) | 0.0 each |

**Total APT across 28 wallets: 0.0 APT**

### Multisig Contract Probes

All 5 multisig pairs healthy (sigs_required=2).

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4...003 | 2 | true |
| A-G | 0xf56c...096 | 2 | true |
| Y-Z | 0xd3ff...883 | 2 | true |
| S-T | 0x3b1c...883 | 2 | true |
| V-W | 0x40fa...b6d | 2 | true |

### MNX Markets (testnet.mnx.fi)

Status: UNAVAILABLE
All endpoints return HTTP 401 (Vercel Deployment Protection — visitor password required).

---

## DuckDB Tables

```
world_increments   361 rows  (GF3-tagged repo push events)
repo_snapshots     361 rows  (full repo metadata)
aptos_snapshots     28 rows  (Hamming swarm balances)
multisig_probes      5 rows  (multisig health probes)
mnx_snapshots        0 rows  (MNX unavailable)
```
