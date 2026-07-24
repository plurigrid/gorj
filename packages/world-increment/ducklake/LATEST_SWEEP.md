# World-Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-07-24
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social graph | 5 |
| AustinCStone | social graph | 4 |
| wasita | social graph | 4 |
| DJedamski | social graph | 2 |
| kristinezheng | social graph | 1 |
| M1shaaa | social graph | 2 |

**Total repos snapshotted:** 320
**Total world_increments written:** 320

### Notable repos

- `plurigrid/gorj` — pushed 2026-07-24 (today), 1370 open issues, actively worked
- `plurigrid/asi` — 31 stars, 10 forks, "everything is topological chemputer!"
- `kubeflow/kubeflow` — 14k+ stars, leading MLOps platform
- `migalkin/NodePiece` — 144 stars, ICLR'22 KG representation paper
- `TeglonLabs/jank-crane` — C++, crane-jank converged-IR hub, GF3 convergence maps
- `wasita/wasita.github.io` — pushed 2026-07-21, active Svelte personal site

### GF(3) Color Chain

Increments assigned cyclic GF(3) trit coloring:
- id%3==0: trit=0, ERGODIC (#d3869b)
- id%3==1: trit=1, PLUS (#b8bb26)
- id%3==2: trit=-1, MINUS (#cc241d)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 28 addresses)

All 28 addresses queried (alice, bob, A-Z). All returned **0.0 APT** — CoinStore<AptosCoin> resource not initialized. These are fresh accounts that have not received an on-chain transaction yet.

### Multisig Probes (5 contracts)

All 5 multisig accounts probed via 0x1::multisig_account::num_signatures_required.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B  | 0x0da4... | 2 | healthy |
| A-G  | 0xf56c... | 2 | healthy |
| Y-Z  | 0xd3ff... | 2 | healthy |
| S-T  | 0x3b1c... | 2 | healthy |
| V-W  | 0x40fa... | 2 | healthy |

All 5 multisig contracts require 2-of-N signatures and are active on mainnet.

### MNX Markets (testnet.mnx.fi)

testnet.mnx.fi returns a Next.js SPA. No public REST API endpoint responded with JSON data. Market data marked as unavailable (0 mnx_snapshots rows inserted).

---

## DuckDB Table Summary

| Table | Rows |
|-------|------|
| world_increments | 320 |
| repo_snapshots | 320 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA, no API) |
