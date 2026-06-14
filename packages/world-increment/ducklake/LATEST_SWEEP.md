# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-14

## Sweep Metadata
- **Date:** 2026-06-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 381 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 2 users + 6 social graph |

---

## GF(3) Color Chain — All 11 Increments

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 1 | TeglonLabs | org | 1 | `#b8bb26` | **PLUS** |
| 2 | plurigrid | org | 2 | `#cc241d` | **MINUS** |
| 3 | kubeflow | org | 0 | `#d3869b` | **ERGODIC** |
| 4 | bmorphism | user | 1 | `#b8bb26` | **PLUS** |
| 5 | zubyul | user | 2 | `#cc241d` | **MINUS** |
| 6 | migalkin | social_graph | 0 | `#d3869b` | **ERGODIC** |
| 7 | DJedamski | social_graph | 1 | `#b8bb26` | **PLUS** |
| 8 | wasita | social_graph | 2 | `#cc241d` | **MINUS** |
| 9 | kristinezheng | social_graph | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | social_graph | 1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | social_graph | 2 | `#cc241d` | **MINUS** |

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 48 |
| AustinCStone | social_graph | 30 |
| migalkin | social_graph | 19 |
| wasita | social_graph | 11 |
| M1shaaa | social_graph | 8 |
| DJedamski | social_graph | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | social_graph | 5 |
| **TOTAL** | | **381** |

---

## Top Repos by Stars

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,720 | — | 2026-06-11 |
| kubeflow/pipelines | 4,153 | Python | 2026-06-13 |
| kubeflow/spark-operator | 3,127 | Python | 2026-06-12 |
| kubeflow/trainer | 2,115 | Go | 2026-06-13 |
| kubeflow/katib | 1,683 | Python | 2026-06-12 |
| kubeflow/examples | 1,461 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1,022 | YAML | 2026-06-12 |
| kubeflow/arena | 812 | Go | 2026-05-07 |
| kubeflow/kale | 694 | Python | 2026-06-12 |
| kubeflow/mpi-operator | 528 | Go | 2026-06-12 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| plurigrid/asi | 26 | HTML | 2026-06-10 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| bmorphism/risc0-cosmwasm-example | 23 | Rust | 2022-10-20 |
| plurigrid/gorj | 0 (569 issues) | Clojure | 2026-06-14 |
| bmorphism/Gay.jl | 1 (189 issues) | Julia | 2026-06-14 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets, mainnet)

**All 28 wallets: 0.00 APT**

The Aptos fullnode returned HTTP 404 (`resource_not_found`) for all 28 addresses — the `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource does not exist at any address (never received APT or fully emptied). API is healthy (ledger ~5.73B at query time).

| World | Address (abbreviated) | APT |
|-------|----------------------|-----|
| alice | 0xc793…cc7b | 0.00 |
| bob | 0x0a3c…512d | 0.00 |
| A–Z | (26 addresses) | 0.00 each |

### Multisig Contract Probes (5 contracts)

**All 5 healthy — all require 2 signatures**

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4…7003 | 2 | ✓ |
| A-G | 0xf56c…0096 | 2 | ✓ |
| Y-Z | 0xd3ff…b883 | 2 | ✓ |
| S-T | 0x3b1c…7883 | 2 | ✓ |
| V-W | 0x40fa…eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Unavailable — HTTP 401 Unauthorized**

Both `/api/markets` and `/api/v1/markets` returned 401. Authentication credentials required.

---

## DuckDB Tables

| Table | Rows |
|-------|------|
| world_increments | 11 |
| repo_snapshots | 381 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (unavailable marker) |

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=2, color=#cc241d, name=MINUS
