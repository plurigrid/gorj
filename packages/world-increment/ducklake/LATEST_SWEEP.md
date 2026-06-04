# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep Date:** 2026-05-02  
**Increment ID:** 13  
**GF(3) Trit:** 1 — PLUS — `#b8bb26`  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured | Total Stars | Latest Push |
|--------|------|---------------|-------------|-------------|
| kubeflow | org | 18 | 32,870 | 2026-05-01 |
| migalkin | user | 6 | 277 | 2025-08-04 |
| bmorphism | user | 16 | 209 | 2026-04-08 |
| AustinCStone | user | 6 | 107 | 2025-05-09 |
| plurigrid | org | 18 | 63 | 2026-04-30 |
| zubyul | user | 11 | 12 | 2026-03-26 |
| wasita | user | 6 | 4 | 2026-04-28 |
| DJedamski | user | 4 | 3 | 2018-03-07 |
| TeglonLabs | org | 4 | 2 | 2026-01-01 |
| kristinezheng | user | 3 | 0 | 2026-04-09 |
| M1shaaa | user | 3 | 0 | 2026-05-02 |

**Total repos snapshotted this sweep:** 95  
**Total repo_snapshots in DB:** 1,039  
**Total world_increments in DB:** 24

### Top Repos by Stars (this sweep)
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,615 | — | 2026-04-29 |
| kubeflow/pipelines | 4,130 | Python | 2026-05-01 |
| kubeflow/spark-operator | 3,121 | Python | 2026-04-28 |
| kubeflow/trainer | 2,095 | Go | 2026-05-01 |
| kubeflow/katib | 1,681 | Python | 2026-04-14 |
| migalkin/NodePiece | 143 | Python | 2022-02-02 |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml | 2026-03-16 |
| plurigrid/asi | 17 | HTML | 2026-04-26 |

### Active Frontier (pushed within 30 days of sweep)
- `plurigrid/zig-syrup` — Zig, 2026-04-30
- `plurigrid/asi` — HTML, 2026-04-26
- `plurigrid/nash-portal` — Rust, 2026-04-26
- `plurigrid/asi-skills` — Julia, 2026-04-26
- `plurigrid/nanoclj-zig` — Zig, 2026-04-25
- `kubeflow/hub` — Go, 2026-05-01
- `kubeflow/pipelines` — Python, 2026-05-01
- `kubeflow/manifests` — YAML, 2026-04-30
- `M1shaaa/M1shaaa` — profile, 2026-05-02
- `wasita/wasita.github.io` — Svelte, 2026-04-28
- `kristinezheng/kristinezheng.github.io` — HTML, 2026-04-09
- `zubyul/gay-world` — Python, 2026-03-26

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
Queried 28 wallets (alice, bob, A–Z) via Aptos fullnode mainnet API.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…2d5d | 0.0 |
| A–Z (26) | (see DB) | 0.0 each |

**Status:** All 28 addresses returned 0.0 APT — CoinStore resources not initialized (unfunded accounts on mainnet).

### Multisig Contract Probes (Aptos Mainnet)
All 5 multisig contracts resolved successfully via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4…7003 | 2 | healthy |
| A-G | 0xf56c…0096 | 2 | healthy |
| Y-Z | 0xd3ff…b883 | 2 | healthy |
| S-T | 0x3b1c…7883 | 2 | healthy |
| V-W | 0x40fa…eb6d | 2 | healthy |

All pairs are 2-of-2 multisigs. All on-chain and healthy.

### MNX Markets (testnet.mnx.fi)
**Status:** Unavailable — Next.js SPA with no accessible REST API endpoints. `/api/markets` and `/api/v1/markets` return 404. `__NEXT_DATA__` contains no market data. Recorded as placeholder in `mnx_snapshots`.

---

## GF(3) Color Chain

| Increment ID | Trit | Name | Hex |
|-------------|------|------|-----|
| 10 | +1 | PLUS | #b8bb26 |
| 11 | -1 | MINUS | #cc241d |
| 12 | 0 | ERGODIC | #d3869b |
| **13** | **+1** | **PLUS** | **#b8bb26** ← this sweep |

---

## DB Summary

```
Tables:
  world_increments   24 rows
  repo_snapshots   1039 rows
  aptos_snapshots    28 rows  (this sweep)
  multisig_probes     5 rows  (this sweep)
  mnx_snapshots       1 row   (unavailable placeholder)
```
