# World-Increment + Hamming Swarm Snapshot

**Date:** 2026-07-21  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Total Repos |
|--------|------|-------------|
| plurigrid | org | 103 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 106 |
| zubyul | user | 49 |
| migalkin | user (social) | 19 |
| DJedamski | user (social) | 6 |
| wasita | user (social) | 12 |
| kristinezheng | user (social) | 5 |
| M1shaaa | user (social) | 8 |
| AustinCStone | user (social) | 41 |

### Notable Repos (most recently pushed)

| Repo | Stars | Language | Updated |
|------|-------|----------|---------|
| plurigrid/asi | 31 | HTML | 2026-07-17 |
| plurigrid/gorj | 1 | Clojure | 2026-07-07 (1284 open issues) |
| kubeflow/kubeflow | 15786 | — | 2026-07-20 |
| kubeflow/spark-operator | 3140 | Python | 2026-07-20 |
| kubeflow/trainer | 2152 | Go | 2026-07-20 |
| kubeflow/pipelines | 4169 | Python | 2026-07-20 |
| bmorphism/Gay.jl | 2 | Julia | 2026-07-20 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-05-08 |
| wasita/wasita.github.io | 1 | Svelte | 2026-07-20 |
| AustinCStone/byteruckus | 0 | HTML | 2026-07-15 |
| TeglonLabs/jank-crane | 0 | C++ | 2026-06-08 |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 31 |
| 1 | #b8bb26 | PLUS | 33 |
| -1 | #cc241d | MINUS | 32 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)

All 28 addresses queried against Mainnet. Every address returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — accounts are either empty or have migrated to the fungible asset model.

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793... | 0.0 |
| bob | 0x0a3c... | 0.0 |
| A–Z (26 addrs) | varies | 0.0 each |

**Note:** All 28 addresses show 0 APT (no CoinStore resource found at ledger tip).

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4... | 2 | ✅ |
| A-G | 0xf56c... | 2 | ✅ |
| Y-Z | 0xd3ff... | 2 | ✅ |
| S-T | 0x3b1c... | 2 | ✅ |
| V-W | 0x40fa... | 2 | ✅ |

**All 5 multisig contracts are healthy** — each requiring 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — site is behind Vercel authentication (HTTP 401, visitor password required). No market data could be extracted.

---

## DuckDB Table Summary

| Table | Rows |
|-------|------|
| world_increments | 96 |
| repo_snapshots | 1017 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (auth-gated) |

