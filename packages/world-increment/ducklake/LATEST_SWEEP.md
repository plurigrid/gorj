# World-Increment Sweep + Hamming Swarm Snapshot
**Timestamp:** 2026-06-16 UTC  
**GF(3) Color Chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured | Total Stars |
|--------|------|---------------|-------------|
| plurigrid | org | 100 | 170 |
| kubeflow | org | 48 | 101,937 |
| TeglonLabs | org | 5 | 14 |
| bmorphism | user | 100 | 514 |
| zubyul | user (zubyul social) | 49 | 41 |
| migalkin | user (zubyul social) | 19 | 834 |
| DJedamski | user (zubyul social) | 6 | 17 |
| wasita | user (zubyul social) | 11 | 11 |
| kristinezheng | user (zubyul social) | 5 | 0 |
| M1shaaa | user (zubyul social) | 8 | 0 |
| AustinCStone | user (zubyul social) | 45 | 324 |

**Total repos snapshotted: 396**

### Notable Repos (by stars)
- `kubeflow/kubeflow` — 15,726 ⭐ (ML Toolkit for Kubernetes)
- `kubeflow/pipelines` — 4,154 ⭐ (ML Pipelines for Kubeflow)
- `kubeflow/spark-operator` — 3,127 ⭐ (K8s Spark operator)
- `migalkin/NodePiece` — 144 ⭐ (Knowledge Graph representations, ICLR'22)
- `AustinCStone/TextGAN` — 92 ⭐ (TensorFlow text GAN)
- `migalkin/StarE` — 89 ⭐ (Hyper-Relational KGs, EMNLP'20)
- `bmorphism/ocaml-mcp-sdk` — 61 ⭐ (OCaml SDK for MCP)
- `plurigrid/asi` — 26 ⭐ (everything is topological chemputer!)
- `plurigrid/gorj` — 0 stars, **605 open issues** (forj + GF(3) trit coloring — this repo!)

### Recently Active (pushed 2026-06-15)
- `plurigrid/gorj` — pushed 2026-06-15T23:13:14Z
- `plurigrid/place` — pushed 2026-06-15T23:04:11Z
- `kubeflow/trainer` — pushed 2026-06-15T23:34:42Z
- `kubeflow/sdk` — pushed 2026-06-15T23:09:50Z
- `bmorphism/Gay.jl` — pushed 2026-06-15T19:35:36Z (187 open issues)
- `bmorphism/satreadout` — pushed 2026-06-15T21:20:06Z (Lean 4 machine-checked math)
- `wasita/wasita.github.io` — pushed 2026-06-15T20:15:02Z

### GF(3) World Increment Chain
Each source assigned a GF(3) trit via `id % 3`:
- id≡0 → trit=0 ERGODIC (#d3869b, pink)
- id≡1 → trit=1 PLUS (#b8bb26, yellow-green)
- id≡2 → trit=-1 MINUS (#cc241d, red)

Mapping: plurigrid→ERGODIC, kubeflow→PLUS, TeglonLabs→MINUS, bmorphism→ERGODIC, zubyul→PLUS, migalkin→MINUS, DJedamski→ERGODIC, wasita→PLUS, kristinezheng→MINUS, M1shaaa→ERGODIC, AustinCStone→PLUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)

All 28 addresses queried against `https://fullnode.mainnet.aptoslabs.com/v1/`.
**Result:** All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

None of the monitored Hamming swarm addresses have initialized an APT CoinStore on mainnet.
Ledger version at time of probe: ~5,756,440,913.

| World | Balance APT |
|-------|-------------|
| alice | uninitialized |
| bob | uninitialized |
| A–Z (26) | all uninitialized |

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | HEALTHY |
| A-G | 0xf56c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY |
| S-T | 0x3b1c...7883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

**All 5 multisig contracts require 2-of-N signatures. All healthy.**

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` returns Vercel authentication required (deployment protection enabled).
Market data **unavailable** without bypass token.

---

## DuckDB Ducklake

Location: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 11 | GF(3)-colored source sweep events |
| `repo_snapshots` | 396 | GitHub repo metadata snapshots |
| `aptos_snapshots` | 28 | Hamming swarm wallet balance probes |
| `multisig_probes` | 5 | Aptos multisig health checks |
| `mnx_snapshots` | 1 | MNX market probe (unavailable) |

---

## Summary

- **396 repos** snapshotted across 11 GitHub orgs/users in the plurigrid social graph
- **Kubeflow** dominates by stars (101,937 total); **plurigrid/gorj** most active locally
- **All 28 Hamming swarm addresses** uninitialized on Aptos mainnet (no APT CoinStore)
- **All 5 multisig contracts** healthy with 2-sig threshold
- **MNX testnet** gated behind Vercel auth — no market data available this run
