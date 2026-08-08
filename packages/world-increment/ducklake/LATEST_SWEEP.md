# World Increment Sweep + Hamming Snapshot

**Sweep date:** 2026-08-08
**Run:** world-increment-sweep + hamming-swarm-snapshot

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Indexed |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social graph) | 19 |

**Total repo snapshots recorded:** 322+ across all runs

### Notable Findings

#### plurigrid (most active)
- `plurigrid/gorj` — pushed **2026-08-08 18:12** — 1725 open issues (active)
- `plurigrid/place` — pushed **2026-08-08 10:48** — 18 open issues
- `plurigrid/eirobri` — pushed 2026-08-04 — 31 open issues
- `plurigrid/asi` — 59 stars (highest in org), HTML, topological chemputer
- `plurigrid/vcg-auction` — 7 stars (Rust VCG auction contract)

#### kubeflow (large, active ML infra)
- `kubeflow/kubeflow` — 15,806 stars — flagship ML toolkit
- `kubeflow/pipelines` — 4,182 stars — 518 open issues, pushed today
- `kubeflow/spark-operator` — 3,145 stars — pushed today
- `kubeflow/trainer` — 2,176 stars — Distributed AI training on K8s

#### bmorphism (MCP ecosystem focus)
- `bmorphism/Gay.jl` — 188 open issues, pushed 2026-08-07 (most active)
- `bmorphism/ocaml-mcp-sdk` — 61 stars (top MCP tool in social graph)
- `bmorphism/anti-bullshit-mcp-server` — 23 stars
- `bmorphism/risc0-cosmwasm-example` — 23 stars

#### TeglonLabs
- `TeglonLabs/jank-crane` — C++, GF3 convergence maps, pushed 2026-06-08
- `TeglonLabs/mathpix-gem` — 2 stars, Ruby, mathematical OCR

#### migalkin (knowledge graph researcher)
- `migalkin/NodePiece` — 144 stars, Knowledge Graph representations (ICLR'22)
- `migalkin/StarE` — 89 stars, Hyper-Relational KG (EMNLP 2020)

### GF(3) Color Chain
| Trit | Color | Name | Meaning |
|------|-------|------|---------|
| 0 | `#d3869b` | ERGODIC | id % 3 == 0 |
| 1 | `#b8bb26` | PLUS | id % 3 == 1 |
| 2 | `#cc241d` | MINUS | id % 3 == 2 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

All 28 wallets queried (alice, bob, A–Z). All returned **0.0 APT** — addresses exist but CoinStore resource is uninitialized or accounts hold zero liquid APT on mainnet. This is expected for swarm/multisig participant addresses that operate through contract accounts.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B–Z | (see DuckDB) | 0.0 each |

### Multisig Contract Probes

All 5 multisig pairs probed successfully. **All healthy** — 2-of-2 threshold confirmed.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable as structured data.** `testnet.mnx.fi` is a Next.js SPA — all market data is loaded client-side via JavaScript bundles. No REST API endpoints (`/api/markets`, `/api/v1/markets`) returned JSON; both redirected to the SPA shell. MNX market data is not extractable without a browser runtime.

---

## DuckDB Ducklake

**Path:** `packages/world-increment/ducklake/world-increments.duckdb`

Tables:
- `world_increments` — GF(3) colored event log
- `repo_snapshots` — full repo metadata per source
- `aptos_snapshots` — Hamming swarm wallet balances
- `multisig_probes` — 2-of-2 threshold confirmations
- `mnx_snapshots` — (empty; SPA unavailable)
