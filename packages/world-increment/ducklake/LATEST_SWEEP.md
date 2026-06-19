# World Increment Sweep + Hamming Swarm Snapshot
**Generated:** 2026-06-19 UTC  
**Sweep ID range:** 1–381 repo increments  
**GF(3) color chain:** id%3==0 → trit=0 ERGODIC #d3869b · id%3==1 → trit=1 PLUS #b8bb26 · id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social graph) | 19 |
| wasita | user (social graph) | 11 |
| AustinCStone | user (social graph) | 30 |
| DJedamski | user (social graph) | 6 |
| kristinezheng | user (social graph) | 5 |
| M1shaaa | user (social graph) | 8 |
| **TOTAL** | | **381** |

### Notable Repos by Stars
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,736 | — | 2026-06-18 |
| kubeflow/pipelines | 4,154 | Python | 2026-06-19 |
| kubeflow/spark-operator | 3,127 | Python | 2026-06-18 |
| kubeflow/trainer | 2,116 | Go | 2026-06-19 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/asi | 26 | HTML | 2026-06-10 |
| plurigrid/gorj | 0 | Clojure | 2026-06-19 (THIS REPO) |

### Hot Repos (pushed 2026-06-19)
- `plurigrid/gorj` — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- `kubeflow/sdk` — Universal Python SDK for AI workloads on Kubernetes
- `kubeflow/trainer` — Distributed AI Model Training on Kubernetes
- `kubeflow/website` — Kubeflow Website
- `bmorphism/Gay.jl` — Wide-gamut color sampling with splittable determinism (SPI)
- `M1shaaa/M1shaaa` — GitHub profile config (pushed today)

### DuckDB Storage
- Table: `world_increments` — 381 github repo increment rows
- Table: `repo_snapshots` — 381 rows with full metadata

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 wallets)
All Hamming swarm wallets queried via Aptos mainnet fullnode.

**Result: All 28 addresses returned 0 APT** (accounts not initialized or coin stores empty on mainnet).

| World | Address prefix | Balance (APT) |
|-------|---------------|---------------|
| alice | 0xc793acdec12b4a... | 0.0 |
| bob | 0x0a3c00c58fdf90... | 0.0 |
| A–Z (26 wallets) | various | 0.0 each |

### Multisig Contract Probes — 5/5 HEALTHY
| Pair | Address prefix | Sigs Required | Status |
|------|---------------|---------------|--------|
| A-B | 0x0da4f428a0c007... | 2 | healthy |
| A-G | 0xf56c4a1c090621... | 2 | healthy |
| Y-Z | 0xd3ffe1812b2df4... | 2 | healthy |
| S-T | 0x3b1c3ae905d44c... | 2 | healthy |
| V-W | 0x40fad7b423a843... | 2 | healthy |

All 5 multisig contracts live on Aptos mainnet with 2-of-N signature requirements.

### MNX Markets
`testnet.mnx.fi` — UNAVAILABLE: Vercel deployment protection active (visitor password required). No market data extractable.

### DuckDB Storage
- Table: `aptos_snapshots` — 28 rows (all 0.0 APT)
- Table: `multisig_probes` — 5 rows (all healthy, sigs_required=2)
- Table: `mnx_snapshots` — 1 row (unavailability record)

---

## Sweep Summary

| Metric | Value |
|--------|-------|
| GitHub repos snapshotted | 381 |
| Orgs/users swept | 11 |
| Aptos wallets checked | 28 |
| Total APT balance | 0.0 |
| Multisig contracts probed | 5 |
| Multisig contracts healthy | 5/5 |
| MNX markets available | No (Vercel auth-gated) |
| GF(3) color trit-0 (ERGODIC) | 127 repos |
| GF(3) color trit-1 (PLUS) | 127 repos |
| GF(3) color trit-(-1) (MINUS) | 127 repos |

**DB:** `packages/world-increment/ducklake/world-increments.duckdb`
