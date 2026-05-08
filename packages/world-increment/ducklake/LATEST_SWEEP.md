# World Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-05-08  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB version:** v1.5.2 (Variegata)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) color chain:** ERGODIC=#d3869b (trit=0) | PLUS=#b8bb26 (trit=1) | MINUS=#cc241d (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts (Cumulative DB State)
| Metric | Value |
|--------|-------|
| Total World Increments | 112 |
| Total Repo Snapshots | 1033 |
| Sources Covered | 3 orgs + 8 users |
| GF(3) ERGODIC increments | 36 |
| GF(3) PLUS increments | 38 |
| GF(3) MINUS increments | 38 |

### Sources Queried (2026-05-08 sweep)
| Source | Type | Total DB Repos | Top Stars |
|--------|------|----------------|-----------|
| plurigrid | org | 220 | asi (21★), ontology (7★), vcg-auction (7★) |
| kubeflow | org | 109 | kubeflow (15625★), pipelines (4136★), spark-operator (3124★) |
| TeglonLabs | org | 110 | mathpix-gem (2★) |
| bmorphism | user | 213 | ocaml-mcp-sdk (60★), anti-bullshit-mcp-server (23★), risc0-cosmwasm (23★) |
| zubyul | user | 59 | gay-world (1★), cascade-world (1★) |

### Social Graph (zubyul network)
| User | DB Repos | Notable |
|------|----------|---------|
| migalkin | 67 | NodePiece (144★), StarE (89★), kgcourse2021 (25★) — knowledge graphs |
| DJedamski | 26 | kaggle_ncaa18, School, Getting-and-Cleaning-Data |
| wasita | 65 | wasita.github.io (Svelte, active Apr 2026), magic-garden (2★) |
| kristinezheng | 39 | lookit-jenga (MIT cognitive science), portfolio (active Apr 2026) |
| M1shaaa | 35 | profile README (pushed 2026-05-08), lab-bookshelf (TypeScript) |
| AustinCStone | 90 | TextGAN (92★), StereoVisionMRF (11★), bmfork (active May 2025) |

### GF(3) Color Chain — This Sweep (increments 24–112)
```
GF(3) chain pattern: PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → ...
id%3==0 → trit=0  ERGODIC #d3869b
id%3==1 → trit=1  PLUS    #b8bb26
id%3==2 → trit=-1 MINUS   #cc241d
```

### Notable Recent Pushes (≤30 days from 2026-05-08)
| Repo | Pushed | Stars | Notes |
|------|--------|-------|-------|
| plurigrid/gorj | 2026-05-08 | 0 | forj + Rama + GF(3), 105 open issues |
| kubeflow/pipelines | 2026-05-08 | 4136 | ML Pipelines, 490 issues |
| bmorphism/Gay.jl | 2026-05-08 | 1 | GF(3) color sampling, 187 issues |
| M1shaaa/M1shaaa | 2026-05-08 | 0 | profile README |
| kubeflow/katib | 2026-05-08 | 1683 | AutoML on Kubernetes |
| kubeflow/trainer | 2026-05-07 | 2095 | Distributed AI training |
| kubeflow/kubeflow | 2026-05-07 | 15625 | flagship ML platform |
| bmorphism/zig-syrup | 2026-05-07 | 0 | OCapN Syrup in Zig |
| bmorphism/nanoclj-zig | 2026-05-07 | 0 | fork active |
| wasita/vocoder | 2026-05-06 | 0 | JS vocoder |
| plurigrid/horse | 2026-05-07 | 1 | active TeX repo |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses (alice, bob, A–Z) queried via `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result: All 28 addresses uninitialized on Aptos mainnet.**

All returned `{"message":"Resource not found by Address(...)}` — no CoinStore resource exists for any address. These wallets have not been activated on mainnet (no APT deposits received).

| Range | Status | Balance APT |
|-------|--------|-------------|
| alice | uninitialized | — |
| bob | uninitialized | — |
| A through Z (26) | uninitialized | — |

### Multisig Contract Probes

All 5 multisig contracts probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...987003 | **2** | HEALTHY ✓ |
| A-G | 0xf56c4a1c...c0096 | **2** | HEALTHY ✓ |
| Y-Z | 0xd3ffe181...5b883 | **2** | HEALTHY ✓ |
| S-T | 0x3b1c3ae9...d7883 | **2** | HEALTHY ✓ |
| V-W | 0x40fad7b4...0eb6d | **2** | HEALTHY ✓ |

**All 5 multisig contracts respond and require 2-of-N signatures. Hamming swarm topology is intact.**

### MNX Markets (testnet.mnx.fi)

The MNX testnet is a Next.js SPA. The `/api/markets` endpoint returns **HTTP 404** (SPA client-side routing, no REST API exposed server-side). Market data requires JavaScript execution in a browser context.

**Status: UNAVAILABLE** — SPA renders all data client-side; no structured REST API accessible via curl.

---

## DuckDB Schema
```sql
world_increments  -- 112 rows: GF(3)-tagged repo push events
repo_snapshots    -- 1033 rows: cumulative multi-sweep repo metadata  
aptos_snapshots   -- 28 rows: hamming swarm wallet states (all uninitialized)
multisig_probes   -- 5 rows: all healthy, 2-of-N threshold
mnx_snapshots     -- 1 row: SPA_unavailable
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,625★ — flagship ML platform for Kubernetes (all-time high in this sweep)
- **kubeflow/pipelines**: 4,136★ — most popular ML pipeline for Kubernetes
- **kubeflow/spark-operator**: 3,124★ — Kubernetes operator for Apache Spark
- **kubeflow/trainer**: 2,095★ — Distributed AI/LLM training on Kubernetes
- **migalkin/NodePiece**: 144★ — scalable KG representations (ICLR'22)
- **bmorphism/ocaml-mcp-sdk**: 60★ — OCaml SDK for MCP using oxcaml_effect
- **AustinCStone/TextGAN**: 92★ — text generation GANs (TensorFlow, 2016)
- **plurigrid/asi**: 21★ — topological chemputer (active Apr 2026)
- **plurigrid/gorj**: this repo — forj + Rama + GF(3) trit coloring
- **Multisig swarm**: 5/5 contracts healthy, all 2-of-N threshold on Aptos mainnet

*Generated by world-increment-sweep + hamming-swarm-snapshot agent*
