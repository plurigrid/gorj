# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-16  
**Run:** world-increment-sweep + hamming-swarm-snapshot agent

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos Snapshotted | Notable |
|--------|------|-------------------|---------|
| plurigrid | org | 101 total (19 key repos) | `gorj` 618 open issues, pushed today; `asi` 26★ |
| kubeflow | org | 48 total (13 key repos) | `kubeflow` 15,725★; `pipelines` 4,154★; `trainer` 2,115★ |
| TeglonLabs | org | 5 | `jank-crane` pushed 2026-06-08 |
| bmorphism | user | 104 total (20 key repos) | `Gay.jl` 187 open issues; `ocaml-mcp-sdk` 61★ |
| zubyul | user | 49 total (12 key repos) | `plurigrid-site` 11 open issues |
| migalkin | social | 19 | `NodePiece` 144★; `StarE` 89★ (KG ML researcher) |
| DJedamski | social | 6 | kaggle/data science repos |
| wasita | social | 11 | `wasita.github.io` active 2026-06-15 |
| kristinezheng | social | 5 | cognitive science / MIT |
| M1shaaa | social | 8 | lab work repos |
| AustinCStone | social | 40 | `TextGAN` 92★; ML/CV researcher |

### GF(3) Color Chain (first 6 increments this run)

| id | trit | color | name | repo |
|----|------|-------|------|------|
| id%3=1 | +1 | #b8bb26 | PLUS | plurigrid/asi |
| id%3=2 | -1 | #cc241d | MINUS | plurigrid/place |
| id%3=0 | 0 | #d3869b | ERGODIC | plurigrid/eirobri |
| id%3=1 | +1 | #b8bb26 | PLUS | plurigrid/nash-portal |
| id%3=2 | -1 | #cc241d | MINUS | plurigrid/gorj |
| id%3=0 | 0 | #d3869b | ERGODIC | plurigrid/zig-syrup |

### Most Active Repos (recent push)

- `plurigrid/gorj` — pushed 2026-06-16 (today), 618 open issues
- `plurigrid/place` — pushed 2026-06-15
- `kubeflow/trainer` — pushed 2026-06-16, 2115★, 969 forks
- `kubeflow/pipelines` — pushed 2026-06-16, 4154★, 2007 forks
- `bmorphism/Gay.jl` — pushed 2026-06-16, 187 open issues
- `wasita/wasita.github.io` — pushed 2026-06-15
- `kubeflow/kubeflow` — 15725★ (top starred across all sources)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

**Result:** All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

Addresses do not hold a native APT CoinStore resource on Aptos mainnet — accounts may be uninitialized, use non-native token modules, or have no on-chain state. All balances recorded as NULL.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793ac... | NULL |
| bob | 0x0a3c00... | NULL |
| A–Z | (see DB) | NULL (all resource_not_found) |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **HEALTHY** — `0x1::multisig_account::num_signatures_required` returned valid threshold.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f4... | 2 | HEALTHY |
| A-G | 0xf56c4a... | 2 | HEALTHY |
| Y-Z | 0xd3ffe1... | 2 | HEALTHY |
| S-T | 0x3b1c3a... | 2 | HEALTHY |
| V-W | 0x40fad7... | 2 | HEALTHY |

All pairs require exactly **2 signatures** (standard 2-of-N multisig threshold).

### MNX Markets (testnet.mnx.fi)

**Status:** Vercel deployment protection active — authentication gate blocks all API paths. Market data unavailable without bypass token or trusted source OIDC. No data recorded in `mnx_snapshots`.

---

## DuckDB Schema State

| Table | Rows (cumulative) |
|-------|-------------------|
| world_increments | 103+ (80 new this run) |
| repo_snapshots | 1024+ (80 new this run) |
| aptos_snapshots | 28 (this run) |
| multisig_probes | 5 (this run) |
| mnx_snapshots | 0 (unavailable) |

**DB:** `packages/world-increment/ducklake/world-increments.duckdb`
