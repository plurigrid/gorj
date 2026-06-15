# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-15  
**Run type:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured | Total Stars |
|--------|------|---------------|-------------|
| plurigrid | org | 100 | 77 |
| bmorphism | user | 100 | 247 |
| zubyul | user | 49 | 14 |
| kubeflow | org | 48 | 34,214 |
| AustinCStone | user (zubyul graph) | 40 | 108 |
| migalkin | user (zubyul graph) | 19 | 280 |
| wasita | user (zubyul graph) | 11 | 5 |
| M1shaaa | user (zubyul graph) | 8 | 0 |
| DJedamski | user (zubyul graph) | 6 | 3 |
| TeglonLabs | org | 5 | 2 |
| kristinezheng | user (zubyul graph) | 5 | 0 |
| **TOTAL** | | **391** | **34,950** |

### Top Repos by Stars

| Repo | Language | Stars | Forks | Open Issues | Last Push |
|------|----------|-------|-------|-------------|-----------|
| kubeflow/kubeflow | — | 15,726 | 2,673 | 3 | 2026-06-11 |
| kubeflow/pipelines | Python | 4,154 | 2,008 | 475 | 2026-06-15 |
| kubeflow/spark-operator | Python | 3,127 | 1,490 | 101 | 2026-06-15 |
| kubeflow/trainer | Go | 2,115 | 969 | 115 | 2026-06-15 |
| kubeflow/katib | Python | 1,683 | 527 | 117 | 2026-06-15 |
| kubeflow/examples | Jsonnet | 1,461 | 756 | 111 | 2025-04-14 |
| migalkin/NodePiece | Python | 144 | 21 | 0 | 2022-02-02 |
| bmorphism repos | various | 247 total | — | — | — |

### Notable Activity

- **plurigrid/gorj** (this repo): 601 open issues, last push 2026-06-15 — active
- **plurigrid/asi**: 26 stars, HTML — "everything is topological chemputer!"
- **TeglonLabs/jank-crane**: C++, pushed 2026-06-08 — crane-jank GF3 convergence maps
- **TeglonLabs/mathpix-gem**: Ruby, 2 stars, 11 open issues — math OCR gem
- **M1shaaa/M1shaaa**: pushed today (2026-06-15) at 17:09 UTC

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 130 |
| 1 | #b8bb26 | PLUS | 131 |
| -1 | #cc241d | MINUS | 130 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)

All 28 addresses queried against Aptos mainnet `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result: All 28 addresses returned `resource_not_found`.**  
None of the Hamming swarm addresses have an initialized APT CoinStore on mainnet. Accounts are either uncreated or hold no APT.

| Address | Balance |
|---------|---------|
| alice (0xc793...cc7b) | 0 APT (no CoinStore) |
| bob (0x0a3c...2d5d) | 0 APT (no CoinStore) |
| A–Z (26 addrs) | 0 APT each (no CoinStore) |

### Multisig Contract Probes (5/5 HEALTHY)

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...987003 | 2 | HEALTHY |
| A-G | 0xf56c4a1c...c0096 | 2 | HEALTHY |
| Y-Z | 0xd3ffe181...75b883 | 2 | HEALTHY |
| S-T | 0x3b1c3ae9...ed7883 | 2 | HEALTHY |
| V-W | 0x40fad7b4...80eb6d | 2 | HEALTHY |

All 5 multisig accounts require 2-of-N signatures and are structurally healthy.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel deployment protection (authentication required). No market data accessible without a bypass token. `mnx_snapshots` table is empty.

---

## DuckDB Schema Summary

```
world_increments : 391 rows  (one per repo, GF3 color-coded)
repo_snapshots   : 391 rows  (full repo metadata)
aptos_snapshots  : 28 rows   (all 0 APT / no CoinStore)
multisig_probes  : 5 rows    (all HEALTHY, 2 sigs each)
mnx_snapshots    : 0 rows    (Vercel-gated, unavailable)
```

---

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent*
