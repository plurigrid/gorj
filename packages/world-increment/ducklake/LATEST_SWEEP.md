# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-26

## Sweep Metadata
- **Date:** 2026-06-26 14:18 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (today) | 11 |
| Total Repo Snapshots (today) | 265 unique |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Queried | 28 |
| Multisig Contracts Probed | 5/5 healthy |
| MNX Markets | UNAVAILABLE |

---

## GF(3) Color Chain — 2026-06-26 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | AustinCStone | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 2  | DJedamski | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 3  | M1shaaa | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 4  | TeglonLabs | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 5  | bmorphism | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 6  | kristinezheng | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 7  | kubeflow | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 8  | migalkin | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 9  | plurigrid | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 10 | wasita | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 11 | zubyul | repo_snapshot | +1 | `#b8bb26` | **PLUS** |

GF(3) chain: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

---

## Top Repos by Source

### kubeflow (124 repos)
| Repo | Language | Stars |
|------|----------|-------|
| kubeflow/kubeflow | — | 15,744 |
| kubeflow/pipelines | Python | 4,156 |
| kubeflow/spark-operator | Python | 3,128 |
| kubeflow/trainer | Go | 2,122 |
| kubeflow/katib | Python | 1,685 |
| kubeflow/examples | Jsonnet | 1,460 |
| kubeflow/arena | Go | 813 |
| kubeflow/mpi-operator | Go | 528 |

### plurigrid (261 repos)
| Repo | Language | Stars |
|------|----------|-------|
| plurigrid/asi | — | 26 |

### bmorphism (265 repos)
| Repo | Language | Stars |
|------|----------|-------|
| bmorphism/ocaml-mcp-sdk | OCaml | 61 |
| bmorphism/anti-bullshit-mcp-server | — | 23 |
| bmorphism/risc0-cosmwasm-example | — | 23 |
| bmorphism/say-mcp-server | — | 20 |
| bmorphism/babashka-mcp-server | — | 19 |
| bmorphism/manifold-mcp-server | — | 14 |

### migalkin (74 repos)
| Repo | Language | Stars |
|------|----------|-------|
| migalkin/NodePiece | Python | 144 |
| migalkin/StarE | Python | 89 |
| migalkin/kgcourse2021 | HTML | 25 |
| migalkin/NBFNet_mlx | Python | 10 |

### AustinCStone (126 repos)
| Repo | Language | Stars |
|------|----------|-------|
| AustinCStone/TextGAN | Python | 92 |
| AustinCStone/StereoVisionMRF | Python | 11 |

---

## Repo Counts by Source

| Source | Repos |
|--------|-------|
| bmorphism | 265 |
| plurigrid | 261 |
| AustinCStone | 126 |
| kubeflow | 124 |
| TeglonLabs | 111 |
| migalkin | 74 |
| wasita | 71 |
| zubyul | 68 |
| kristinezheng | 41 |
| M1shaaa | 40 |
| DJedamski | 28 |
| **TOTAL** | **1,209** |

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Mainnet Balances

**Network:** `https://fullnode.mainnet.aptoslabs.com/v1/`  
**Addresses queried:** 28 (alice, bob, A–Z)  
**Result:** All 28 addresses at 0.0 APT

> All queried addresses lack `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
> Accounts may use the newer Fungible Asset (FA) standard or have never received APT.

### Multisig Contract Probes

**View function:** `0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4…3003 | 2 | healthy |
| A-G | 0xf56c…0096 | 2 | healthy |
| Y-Z | 0xd3ff…b883 | 2 | healthy |
| S-T | 0x3b1c…7883 | 2 | healthy |
| V-W | 0x40fa…eb6d | 2 | healthy |

**5/5 healthy — all require 2-of-2 signatures.**

### MNX Markets

**Status:** UNAVAILABLE  
`https://testnet.mnx.fi` returns a Vercel authentication page on all endpoints. No `mnx_snapshots` inserted.

---

## DuckDB Table Counts (cumulative)

```
world_increments : 34
repo_snapshots   : 1,209
aptos_snapshots  : 28
multisig_probes  : 5
mnx_snapshots    : 0
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,744 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,156 stars — Kubernetes ML pipelines
- **kubeflow/spark-operator**: 3,128 stars — Kubernetes operator for Apache Spark
- **migalkin/NodePiece**: 144 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for Model Context Protocol (Jane Street oxcaml_effect)
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 26 stars — topological chemputer
- **plurigrid/gorj**: This very repo — forj + GF(3) world-increment sweep
