# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-06 UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) color chain:** ERGODIC #d3869b (trit=0) · PLUS #b8bb26 (trit=1) · MINUS #cc241d (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Repo Snapshot Coverage

| Source | Type | Unique Repos | Max Stars |
|--------|------|-------------|-----------|
| plurigrid | org | 168 | 28 |
| bmorphism | user | 165 | 61 |
| zubyul | user | 59 | 2 |
| TeglonLabs | org | 54 | 2 |
| kubeflow | org | 51 | 15,764 |
| AustinCStone | user | 43 | 92 |
| wasita | user | 31 | 2 |
| migalkin | user | 30 | 144 |
| kristinezheng | user | 18 | 0 |
| M1shaaa | user | 16 | 0 |
| DJedamski | user | 11 | 2 |

**Total unique repos indexed:** 646

### Top 15 Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,764 | - |
| kubeflow/kubeflow | 15,572 | - |
| kubeflow/pipelines | 4,169 | Python |
| kubeflow/spark-operator | 3,132 | Python |
| kubeflow/trainer | 2,129 | Go |
| kubeflow/katib | 1,689 | Python |
| kubeflow/examples | 1,460 | Jsonnet |
| kubeflow/community-distribution | 1,027 | YAML |
| kubeflow/manifests | 1,010 | YAML |
| kubeflow/arena | 815 | Go |
| kubeflow/kale | 696 | Python |
| kubeflow/mpi-operator | 529 | Go |
| kubeflow/fairing | 337 | Jsonnet |
| kubeflow/pytorch-operator | 310 | Jsonnet |
| kubeflow/community | 195 | Jsonnet |

### GF(3) Color Distribution

| Color Name | Hex | Trit | Count |
|-----------|-----|------|-------|
| PLUS | #b8bb26 | 1 | 117 |
| MINUS | #cc241d | -1 | 116 |
| ERGODIC | #d3869b | 0 | 115 |

### Sources Queried

**Orgs:** plurigrid, kubeflow, TeglonLabs  
**Users:** bmorphism, zubyul  
**Zubyul social graph:** migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone  

### Notable Findings

- **kubeflow/kubeflow** — 15,764 ★, flagship ML-on-Kubernetes toolkit (most starred in sweep)
- **kubeflow/pipelines** — 4,169 ★, active as of 2026-07-05
- **kubeflow/spark-operator** — 3,132 ★, Kubernetes operator for Spark
- **plurigrid/gorj** — 1,001 open issues, pushed 2026-07-06 (this repo, actively developed)
- **plurigrid/asi** — 28 ★, "everything is topological chemputer!"
- **bmorphism/Gay.jl** — 187 open issues, Julia wide-gamut color sampling (most active bmorphism repo)
- **bmorphism/ocaml-mcp-sdk** — 61 ★, OCaml SDK for MCP using Jane Street's oxcaml_effect
- **migalkin/NodePiece** — 144 ★, large KG representation (ICLR'22)
- **AustinCStone/TextGAN** — 92 ★, TensorFlow GAN for text

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet — Wallet Balances (A–Z + alice/bob)

| World | Address | APT Balance | Status |
|-------|---------|-------------|--------|
| A | `0x8699edc0960dd5b916…` | — | no_coinstore_registered |
| B | `0x3f892ebe6e45164e63…` | — | no_coinstore_registered |
| C | `0x38b99e63ada9b6fef1…` | — | no_coinstore_registered |
| D | `0xf77656248f64d5dd00…` | — | no_coinstore_registered |
| E | `0xdc1d9d533bac3507f9…` | — | no_coinstore_registered |
| F | `0x18a14b5b4bec118c1c…` | — | no_coinstore_registered |
| G | `0x69a394c0b0ac842127…` | — | no_coinstore_registered |
| H | `0xce67c327a7844e5488…` | — | no_coinstore_registered |
| I | `0x070fe5d74e4eda30e2…` | — | no_coinstore_registered |
| J | `0x4d964db8f538374034…` | — | no_coinstore_registered |
| K | `0xa732040a6b0d559041…` | — | no_coinstore_registered |
| L | `0x7c2eaeafad9725492e…` | — | no_coinstore_registered |
| M | `0x6fed37a7553ef16b2a…` | — | no_coinstore_registered |
| N | `0xe7dde6da0a65f51062…` | — | no_coinstore_registered |
| O | `0x73252b6011a75115a2…` | — | no_coinstore_registered |
| P | `0x6218792de4a9bc3891…` | — | no_coinstore_registered |
| Q | `0xac40fa50b81b4ca6b1…` | — | no_coinstore_registered |
| R | `0x7ce605cc8fda4f8e4a…` | — | no_coinstore_registered |
| S | `0xb8753014e4888ea48a…` | — | no_coinstore_registered |
| T | `0x35781dc0e42fef3f25…` | — | no_coinstore_registered |
| U | `0x75860da47565f6509b…` | — | no_coinstore_registered |
| V | `0xb59dd8170321dfab5a…` | — | no_coinstore_registered |
| W | `0x5f32aef70f5ba530d3…` | — | no_coinstore_registered |
| X | `0xa95cbbd116548ac990…` | — | no_coinstore_registered |
| Y | `0xd8e32848f1dffa811b…` | — | no_coinstore_registered |
| Z | `0x7af0ef6e1bd706f4b3…` | — | no_coinstore_registered |
| alice | `0xc793acdec12b4a6371…` | — | no_coinstore_registered |
| bob | `0x0a3c00c58fdf9020b2…` | — | no_coinstore_registered |

**Result:** All 28 addresses returned HTTP 404 — accounts exist on-chain but have no 
`0x1::coin::CoinStore<AptosCoin>` resource registered (never received APT on mainnet).

### Aptos Multisig Contracts

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | `0x0da4f428a0c007da0f…` | 2 | ✅ |
| A-G | `0xf56c4a1c0906214f3f…` | 2 | ✅ |
| S-T | `0x3b1c3ae905d44c3a49…` | 2 | ✅ |
| V-W | `0x40fad7b423a843650f…` | 2 | ✅ |
| Y-Z | `0xd3ffe1812b2df40622…` | 2 | ✅ |

**Result:** All 5 multisig contracts healthy, each requiring 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi/api/markets` — **401 Unauthorized** (authentication required, no public endpoint available)

Market data unavailable; recorded in `mnx_snapshots` table with unavailability note.

---

## DuckDB Schema Summary

```
world_increments  — GF(3)-colored increment log (repo_snapshot events)
repo_snapshots    — full repo metadata per source
aptos_snapshots   — Hamming swarm wallet balances (A-Z + alice, bob)
multisig_probes   — 5 A-Z pair multisig contracts, sigs_required
mnx_snapshots     — MNX market data (unavailable this sweep)
```

**DB path:** `packages/world-increment/ducklake/world-increments.duckdb`
