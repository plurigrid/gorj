# World-Increment Sweep + Hamming Snapshot

**Timestamp:** 2026-06-09
**Agent:** world-increment-sweep + hamming-swarm-snapshot
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (zubyul graph) | 19 |
| DJedamski | user (zubyul graph) | 6 |
| wasita | user (zubyul graph) | 11 |
| kristinezheng | user (zubyul graph) | 5 |
| M1shaaa | user (zubyul graph) | 8 |
| AustinCStone | user (zubyul graph) | 40 |
| **TOTAL** | | **391** |

### GF(3) Color Chain Distribution

| Trit | Name | Hex | Count |
|------|------|-----|-------|
| 0 | ERGODIC | #d3869b | 131 |
| 1 | PLUS | #b8bb26 | 130 |
| 2 | MINUS | #cc241d | 130 |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,709 | — | 2026-05-24 |
| kubeflow/pipelines | 4,153 | Python | 2026-06-08 |
| kubeflow/spark-operator | 3,126 | Python | 2026-06-08 |
| kubeflow/trainer | 2,112 | Go | 2026-06-08 |
| kubeflow/katib | 1,685 | Python | 2026-06-05 |
| kubeflow/examples | 1,462 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,021 | YAML | 2026-06-05 |
| kubeflow/arena | 812 | Go | 2026-05-07 |
| kubeflow/kale | 692 | Python | 2026-06-05 |
| kubeflow/mpi-operator | 528 | Go | 2026-06-02 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |

### Most Recent Pushes (at sweep time)

| Repo | Last Pushed |
|------|-------------|
| plurigrid/gorj | 2026-06-09T07:21Z |
| M1shaaa/M1shaaa | 2026-06-09T02:48Z |
| kubeflow/dashboard | 2026-06-09T01:51Z |
| bmorphism/Gay.jl | 2026-06-09T00:36Z |
| TeglonLabs/jank-crane | 2026-06-08T19:03Z |
| kristinezheng/kristinezheng.github.io | 2026-06-07T22:52Z |
| wasita/wasita.github.io | 2026-06-01T04:15Z |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (A-Z + alice/bob)

All 28 addresses queried against `fullnode.mainnet.aptoslabs.com`.

**Result:** All 28 returned `resource_not_found` for
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
These accounts have not received APT via legacy CoinStore
(may use FungibleAsset module or are unfunded).

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793acdec12b4a63... | 0.0 (not found) |
| bob | 0x0a3c00c58fdf9020... | 0.0 (not found) |
| A | 0x8699edc0960dd5b9... | 0.0 (not found) |
| B-Z | (24 addrs) | 0.0 each (not found) |

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428a0c007da... | 2 | true |
| A-G | 0xf56c4a1c09062143... | 2 | true |
| Y-Z | 0xd3ffe1812b2df406... | 2 | true |
| S-T | 0x3b1c3ae905d44c3a... | 2 | true |
| V-W | 0x40fad7b423a84365... | 2 | true |

All 5 multisig contracts are healthy and require **2-of-N** signatures.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` requires Vercel authentication.
Neither `/api/markets` nor the root SPA returned public market data.
`mnx_snapshots` table contains 0 rows.

---

## DuckDB Schema

```
world_increments  391 rows  repo push events, GF3 color chain
repo_snapshots    391 rows  org/user, full_name, language, stars, forks, pushed_at
aptos_snapshots    28 rows  world label, address, balance_apt
multisig_probes     5 rows  pair, address, sigs_required, healthy
mnx_snapshots       0 rows  unavailable (Vercel auth required)
```
