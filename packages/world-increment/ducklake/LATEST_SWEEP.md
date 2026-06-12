# World Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-06-12  
**GF(3) Color Chain:** ERGODIC #d3869b (45) | PLUS #b8bb26 (46) | MINUS #cc241d (45)

---

## JOB 1: GitHub Social Graph Sweep

### Summary
- **136 repo snapshots** across 11 orgs/users
- **GF(3) trit balance:** ERGODIC=45, PLUS=46, MINUS=45 (near-perfect ternary distribution)

### Sources

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| kubeflow | org | 15 | 32,188 |
| bmorphism | user | 28 | 216 |
| migalkin | user | 7 | 279 |
| AustinCStone | user | 12 | 108 |
| plurigrid | org | 30 | 73 |
| zubyul | user | 15 | 7 |
| wasita | user | 7 | 5 |
| TeglonLabs | org | 5 | 2 |
| DJedamski | user | 5 | 2 |
| M1shaaa | user | 7 | 0 |
| kristinezheng | user | 5 | 0 |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,716 | — | 2026-06-11 |
| kubeflow/pipelines | 4,152 | Python | 2026-06-12 |
| kubeflow/spark-operator | 3,127 | Python | 2026-06-09 |
| kubeflow/trainer | 2,112 | Go | 2026-06-12 |
| kubeflow/katib | 1,683 | Python | 2026-06-05 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/asi | 26 | HTML | 2026-06-10 |

### Most Active by Open Issues

| Repo | Issues | Language |
|------|--------|----------|
| plurigrid/gorj | 524 | Clojure |
| kubeflow/pipelines | 490 | Python |
| bmorphism/Gay.jl | 189 | Julia |
| kubeflow/notebooks | 165 | — |
| kubeflow/fairing | 134 | Jsonnet |
| kubeflow/sdk | 133 | Python |
| plurigrid/eirobri | 29 | Clojure |
| plurigrid/nanoclj-zig | 20 | Zig |

### Notable Findings
- **plurigrid/gorj** (this repo): 524 open issues, most active plurigrid project. GF(3) trit coloring for compositional open game REPL orchestration.
- **bmorphism/Gay.jl**: 189 issues, core GF(3) chromatic identity library referenced across zubyul, plurigrid, TeglonLabs.
- **bmorphism/ocaml-mcp-sdk**: 61 stars — highest bmorphism repo, OCaml SDK for MCP via Jane Street oxcaml_effect.
- **TeglonLabs/jank-crane**: Newest TeglonLabs repo (2026-06-08), C++ converged-IR hub with GF3 convergence maps.
- **migalkin** profile: Knowledge Graph researcher (NodePiece ICLR22, StarE EMNLP20).
- **zubyul** social graph: deep entanglement with Gay.jl/GF(3)/NASH/Plurigrid ecosystem.
- **AustinCStone** has bitmind/bmorphism-fork activity in 2025, connecting to the social graph.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A-Z = 28 addresses)

**All 28 addresses returned 0.0 APT** — CoinStore resources not initialized on Aptos mainnet. Addresses exist in the system but have no APT coin store.

Queried via: `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|:---:|:---:|
| A-B | 0x0da4f428...987003 | 2 | YES |
| A-G | 0xf56c4a1c...c0096 | 2 | YES |
| Y-Z | 0xd3ffe181...b883 | 2 | YES |
| S-T | 0x3b1c3ae9...7883 | 2 | YES |
| V-W | 0x40fad7b4...eb6d | 2 | YES |

**All 5 multisig contracts healthy** — each requires 2 signatures. Probed via `0x1::multisig_account::num_signatures_required`.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — All API paths return HTTP 401 Authentication Required. The SPA serves an auth wall; no public market data accessible without credentials.

---

## DuckDB Schema (`packages/world-increment/ducklake/world-increments.duckdb`)

```
world_increments    136 rows  — GF(3) color chain events (ERGODIC/PLUS/MINUS)
repo_snapshots      136 rows  — GitHub repo metadata by source
aptos_snapshots      28 rows  — Hamming swarm wallet balances (all 0.0 APT)
multisig_probes       5 rows  — Aptos multisig health checks (all 2-sig, healthy)
mnx_snapshots         1 row   — MNX markets status (unavailable-401)
```

## GF(3) Trit Distribution

```
ERGODIC #d3869b  trit= 0   count=45  (33.1%)
PLUS    #b8bb26  trit= 1   count=46  (33.8%)
MINUS   #cc241d  trit=-1   count=45  (33.1%)
Total: 136 world increments
```

Near-perfect ternary balance. The color chain walks GF(3) across all repo events, from plurigrid through the entire social graph.
