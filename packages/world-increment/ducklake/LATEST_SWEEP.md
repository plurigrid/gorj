# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-29  
**Run:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 15 (representative) |
| kubeflow | org | 14 (representative) |
| TeglonLabs | org | 5 |
| bmorphism | user | 12 |
| zubyul | user | 6 |
| migalkin | user (social) | 4 |
| DJedamski | user (social) | 2 |
| wasita | user (social) | 2 |
| kristinezheng | user (social) | 2 |
| M1shaaa | user (social) | 2 |
| AustinCStone | user (social) | 2 |

**Total world_increments inserted this sweep:** 66  
**GF(3) color chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d (cycling)

### Notable Repos (Top Stars)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,794 | — | 2026-07-10 |
| kubeflow/pipelines | 4,171 | Python | 2026-07-29 |
| kubeflow/spark-operator | 3,142 | Python | 2026-07-25 |
| kubeflow/trainer | 2,160 | Go | 2026-07-27 |
| kubeflow/katib | 1,693 | Python | 2026-07-26 |
| plurigrid/asi | 53 | HTML | 2026-07-10 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |

### Most Active (Recent Pushes)

- **plurigrid/gorj** — pushed 2026-07-29 (1,482 open issues — active!)
- **kubeflow/hub** — pushed 2026-07-29 (Model Registry)
- **kubeflow/arena** — pushed 2026-07-29 (CLI for Kubeflow)
- **bmorphism/Gay.jl** — pushed 2026-07-29 (188 open issues)
- **zubyul/from-possible-worlds** — pushed 2026-07-18

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A-Z)

**Result:** All 28 addresses returned `null` balance.  
**Reason:** The `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource was not found for any of the queried addresses. These may be unfunded accounts, accounts using the newer fungible asset store, or accounts without APT transfers.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793ac...cc7b | null |
| bob | 0x0a3c00...512d | null |
| A-Z | (26 addresses) | null |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **HEALTHY** — `num_signatures_required = 2`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f4...7003 | 2 | YES |
| A-G | 0xf56c4a...0096 | 2 | YES |
| Y-Z | 0xd3ffe1...b883 | 2 | YES |
| S-T | 0x3b1c3a...7883 | 2 | YES |
| V-W | 0x40fad7...eb6d | 2 | YES |

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable via REST API. `testnet.mnx.fi` is a Next.js SPA with no public REST endpoint reachable at standard paths (`/api/markets`, `/api/v1/markets`). No market data could be extracted. Recorded as unavailable in `mnx_snapshots`.

---

## DuckDB Schema Summary

| Table | Rows (post-sweep) |
|-------|-------------------|
| world_increments | 89 |
| repo_snapshots | 1010 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

---

## GF(3) Color Chain Legend

| id % 3 | Trit | Color | Hex | Meaning |
|--------|------|-------|-----|---------|
| 0 | 0 | ERGODIC | #d3869b | Neutral / mixing |
| 1 | +1 | PLUS | #b8bb26 | Positive / additive |
| 2 | -1 | MINUS | #cc241d | Negative / subtractive |
