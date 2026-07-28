# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-28 UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) chain:** ERGODIC #d3869b (trit=0) → PLUS #b8bb26 (trit=1) → MINUS #cc241d (trit=2)

---

## JOB 1: GitHub Social Graph Sweep

### Orgs Swept

| org/user | repos snapshotted | total stars | latest push |
|---|---|---|---|
| kubeflow | 10 | 26,349 | 2026-07-27T23:37:53Z |
| migalkin | 4 | 267 | 2026-07-10T15:40:00Z |
| AustinCStone | 2 | 103 | 2026-04-01T07:39:41Z |
| bmorphism | 10 | 47 | 2026-07-27T02:46:40Z |
| plurigrid | 14 | 15 | 2026-04-30T03:52:16Z |
| wasita | 2 | 3 | 2026-07-21T15:55:45Z |
| TeglonLabs | 5 | 2 | 2026-06-08T19:03:03Z |
| zubyul | 8 | 1 | 2026-04-24T00:20:56Z |
| DJedamski | 1 | 0 | 2018-02-26 |
| M1shaaa | 1 | 0 | 2024-12-31 |
| kristinezheng | 1 | 0 | 2026-07-01 |

**Total this sweep:** 58 repo snapshots, 58 world-increment records

### Notable Active Repos (pushed this week)
- `kubeflow/trainer` — Distributed AI Model Training on Kubernetes (2155★, pushed 2026-07-27)
- `kubeflow/pipelines` — ML Pipelines for Kubeflow (4171★, pushed 2026-07-27)
- `kubeflow/mpi-operator` — Kubernetes Operator for MPI (530★, pushed 2026-07-27)
- `bmorphism/Gay.jl` — Wide-gamut color sampling, splittable determinism (188 open issues, pushed 2026-07-27)
- `kubeflow/kubeflow` — ML Toolkit for Kubernetes (15793★, pushed 2026-07-10)

### Sources Queried
- **Orgs:** plurigrid (103 repos total), kubeflow (49 repos), TeglonLabs (5 repos)
- **Users:** bmorphism (106 repos total), zubyul (49 repos)
- **Social graph:** migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A–Z) returned HTTP 404 from the Aptos fullnode — no `CoinStore<AptosCoin>` resource exists, indicating wallets have zero APT or were never initialized on mainnet. All balances: **0.0 APT**.

| world | status |
|---|---|
| alice–bob, A–Z (28 total) | 404 Not Found — no APT CoinStore |

### Multisig Contract Probes

All 5 multisig contracts are **healthy** with 2-of-2 signature requirement:

| pair | address | sigs_required | healthy |
|---|---|---|---|
| A-B | 0x0da4f428a0c007da... | 2 | ✓ |
| A-G | 0xf56c4a1c09062... | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df4... | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c... | 2 | ✓ |
| V-W | 0x40fad7b423a843... | 2 | ✓ |

### MNX Testnet Markets

`https://testnet.mnx.fi/api/markets` returns a Next.js SPA (HTML), not JSON. Market data requires client-side rendering and is unavailable via server-side API probe. Status: **unavailable / SPA only**.

---

## DuckDB Schema Summary

```
world_increments  — 81 total rows (58 new this sweep)
repo_snapshots    — 1002 total rows (58 new this sweep)
aptos_snapshots   — 28 rows (this sweep)
multisig_probes   —  5 rows (this sweep)
mnx_snapshots     —  0 rows (SPA, no data)
```

GF(3) color chain this sweep: 20 PLUS (#b8bb26) · 19 ERGODIC (#d3869b) · 19 MINUS (#cc241d)
