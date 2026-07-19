# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-19  
**GF(3) color chain:** id%3==0 → trit=0 ERGODIC #d3869b | id%3==1 → trit=1 PLUS #b8bb26 | id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 16 |
| kubeflow | org | 13 |
| TeglonLabs | org | 5 |
| bmorphism | user | 11 |
| zubyul | user | 8 |
| wasita (social) | user | 6 |
| migalkin (social) | user | 5 |
| kristinezheng (social) | user | 3 |
| M1shaaa (social) | user | 2 |
| AustinCStone (social) | user | 3 |
| DJedamski (social) | user | 1 |

**Total new increments this run:** 73  
**Cumulative DB increments:** 96  
**Cumulative repo snapshots:** 1017

### Most Active Repos (by pushed_at, this sweep)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| plurigrid/gorj | 1 | Clojure | 2026-07-19 |
| kubeflow/pipelines | 4167 | Python | 2026-07-19 |
| kubeflow/mcp-server | 29 | Python | 2026-07-19 |
| kubeflow/sdk | 126 | Python | 2026-07-19 |
| wasita/wasita.github.io | 1 | Svelte | 2026-07-16 |
| zubyul/from-possible-worlds | 0 | TeX | 2026-07-18 |
| bmorphism/gay-chat | 0 | Scheme | 2026-07-14 |
| bmorphism/Gay.jl | 2 | Julia | 2026-07-14 |
| migalkin/kgcourse2021 | 24 | HTML | 2026-07-10 |
| AustinCStone/byteruckus | 0 | HTML | 2026-07-15 |

### Notable Repos by Stars

| Repo | Stars | Description |
|------|-------|-------------|
| kubeflow/kubeflow | 15781 | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4167 | Machine Learning Pipelines for Kubeflow |
| kubeflow/spark-operator | 3139 | Kubernetes operator for Apache Spark |
| kubeflow/trainer | 2151 | Distributed AI Training on Kubernetes |
| kubeflow/katib | 1691 | Automated ML on Kubernetes |
| migalkin/NodePiece | 144 | Parameter-Efficient KG Representations (ICLR 2022) |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml SDK for Model Context Protocol |
| migalkin/StarE | 89 | Message Passing for Hyper-Relational KGs (EMNLP 2020) |
| bmorphism/anti-bullshit-mcp-server | 22 | MCP server for claim validation |
| plurigrid/asi | 31 | everything is topological chemputer! |

### Key Observations

- **plurigrid/gorj** pushed today (2026-07-19) — active development of Rama-based REPL routing
- **kubeflow** dominates by stars (15k+); pipelines, sdk, mcp-server all active today
- **bmorphism/Gay.jl** has 187 open issues — most active issue queue in sweep
- **zubyul/from-possible-worlds** (TeX) pushed 2026-07-18 — new academic work
- **TeglonLabs/jank-crane** (C++) focuses on crane-jank IR convergence with GF3 maps
- **migalkin** social: active KG research — NodePiece (144 stars), StarE (89 stars) recently touched

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 wallets probed via `fullnode.mainnet.aptoslabs.com`.

| World | Address | Balance (APT) | Status |
|-------|---------|---------------|--------|
| alice | 0xc793...cc7b | 0.0 | resource_not_found |
| bob | 0x0a3c...2d5d | 0.0 | resource_not_found |
| A | 0x8699...9d7a | 0.0 | resource_not_found |
| B | 0x3f89...b13 | 0.0 | resource_not_found |
| C | 0x38b9...35e | 0.0 | resource_not_found |
| D | 0xf776...dd1 | 0.0 | resource_not_found |
| E | 0xdc1d...d36 | 0.0 | resource_not_found |
| F | 0x18a1...f71 | 0.0 | resource_not_found |
| G | 0x69a3...f32 | 0.0 | resource_not_found |
| H | 0xce67...00f | 0.0 | resource_not_found |
| I | 0x070f...c9 | 0.0 | resource_not_found |
| J | 0x4d96...f54 | 0.0 | resource_not_found |
| K | 0xa732...dc4 | 0.0 | resource_not_found |
| L–Z (13) | various | 0.0 | 0 (initialized, empty) |

**Summary:** All 28 Hamming swarm wallets hold 0 APT. Addresses alice–K return `resource_not_found` (coin store not initialized); L–Z return 0 (initialized but empty). Total swarm APT: **0.0 APT**.

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | YES |
| A-G | 0xf56c...0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

**All 5 multisig contracts are 2-of-2 and healthy** (sigs_required=2 confirmed via Aptos view function).

### MNX Markets

`https://testnet.mnx.fi` is **Vercel deployment-protected** (visitor password required). No market data could be extracted without credentials.  
**Status: UNAVAILABLE** — authentication required to access SPA or API.

---

## DuckDB Schema Summary

Database: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows (cumulative) |
|-------|-------------------|
| world_increments | 96 |
| repo_snapshots | 1017 |
| aptos_snapshots | 28 (this run) |
| multisig_probes | 5 (this run) |
| mnx_snapshots | 0 (unavailable) |
