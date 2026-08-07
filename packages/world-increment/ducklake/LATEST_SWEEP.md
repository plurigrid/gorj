# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-08-07T15:30:00Z
**GF(3) Color Chain:** PLUS #b8bb26 → MINUS #cc241d → ERGODIC #d3869b

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 15 |
| kubeflow | org | 16 |
| TeglonLabs | org | 4 |
| bmorphism | user | 11 |
| zubyul | user | 8 |
| migalkin | user | 5 |
| wasita | user | 4 |
| AustinCStone | user | 2 |
| kristinezheng | user | 1 |
| M1shaaa | user | 1 |
| **Total** | | **67** |

### GF(3) Distribution (This Sweep)

| Name | Color | Trit | Count |
|------|-------|------|-------|
| PLUS | #b8bb26 | +1 | 23 |
| MINUS | #cc241d | -1 | 22 |
| ERGODIC | #d3869b | 0 | 22 |

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,805 | — |
| kubeflow/pipelines | 4,181 | Python |
| kubeflow/spark-operator | 3,145 | Python |
| kubeflow/trainer | 2,173 | Go |
| kubeflow/katib | 1,694 | Python |
| kubeflow/examples | 1,461 | Jsonnet |
| kubeflow/arena | 816 | Go |
| kubeflow/kale | 699 | Python |
| kubeflow/mpi-operator | 531 | Go |
| kubeflow/mcp-apache-spark-history-server | 188 | Python |
| migalkin/NodePiece | 144 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| plurigrid/asi | 59 | HTML |
| migalkin/StarE | 89 | Python |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |

### Notable Activity

- **plurigrid/gorj** (this repo): 1,699 open issues, pushed 2026-08-07 — most active
- **bmorphism/Gay.jl**: 188 open issues, pushed 2026-08-07 — highly active
- **plurigrid/eirobri**: EiRoBri replay world, 31 open issues
- **kubeflow/sdk**: 232 open issues — new universal Python SDK for AI on Kubernetes
- **wasita/xoxowasita-analysis**: pushed 2026-08-06 — very recent activity
- **TeglonLabs/jank-crane**: crane-jank converged-IR hub with GF3 convergence maps

### Events API
Public events API for bmorphism and zubyul was unavailable through the proxy (HTTP 403). Repo push timestamps used as activity proxy.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

**28 addresses queried** (alice, bob, A–Z)

| Result | Count |
|--------|-------|
| APT balance found | 0 |
| resource_not_found (no coin store) | 28 |

**All 28 addresses** returned `resource_not_found` for the `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource at ledger version 6,656,988,535. This indicates that none of the Hamming swarm addresses have been initialized with an APT coin store on mainnet — they are either unused accounts or hold only non-APT resources.

**Balances summary:** alice=0 APT, bob=0 APT, A=0 APT, B=0 APT, C=0 APT, D=0 APT, E=0 APT, F=0 APT, G=0 APT, H=0 APT, I=0 APT, J=0 APT, K=0 APT, L=0 APT, M=0 APT, N=0 APT, O=0 APT, P=0 APT, Q=0 APT, R=0 APT, S=0 APT, T=0 APT, U=0 APT, V=0 APT, W=0 APT, X=0 APT, Y=0 APT, Z=0 APT

### Multisig Contract Probes

All 5 multisig accounts successfully probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428…987003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c4a1c…0096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ffe181…b883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c3ae9…7883 | 2 | ✅ HEALTHY |
| V-W | 0x40fad7b4…eb6d | 2 | ✅ HEALTHY |

**All 5 multisig contracts healthy — 2-of-N signature threshold confirmed.**

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` returns HTTP 200 but is a Next.js SPA (client-side rendered). No REST API endpoints discovered at `/api/markets`, `/api/v1/markets`, or `/markets`. Market data is rendered client-side via JavaScript and not accessible via server-side endpoints. **Status: UNAVAILABLE** (SPA, no public API).

---

## DuckDB Ducklake State

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 84 |
| repo_snapshots | 1,005 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA unavailable) |

Historical sweeps accumulated in the same DB (incremental ducklake pattern).
