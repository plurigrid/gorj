# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-10  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 36 |
| kubeflow | org | 23 |
| TeglonLabs | org | 5 |
| bmorphism | user | 31 |
| zubyul | user | 15 |
| migalkin | user_social | 5 |
| wasita | user_social | 4 |
| AustinCStone | user_social | 5 |
| kristinezheng | user_social | 2 |
| M1shaaa | user_social | 2 |
| DJedamski | user_social | 2 |
| **TOTAL** | | **130** |

### Notable Repos (by stars)

| repo | stars | pushed_at |
|------|-------|-----------|
| kubeflow/kubeflow | 15715 | 2026-05-24 |
| kubeflow/pipelines | 4153 | 2026-06-10 |
| kubeflow/spark-operator | 3126 | 2026-06-09 |
| kubeflow/trainer | 2112 | 2026-06-10 |
| migalkin/NodePiece | 144 | 2026-05-07 |
| AustinCStone/TextGAN | 92 | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | 61 | 2026-05-08 |
| plurigrid/asi | 25 | 2026-06-10 |
| migalkin/kgcourse2021 | 25 | 2026-02-16 |
| bmorphism/anti-bullshit-mcp-server | 23 | 2026-02-05 |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| +1 | #b8bb26 | PLUS | 44 |
| 0 | #d3869b | ERGODIC | 43 |
| -1 | #cc241d | MINUS | 43 |

### Active Projects (last 48h as of 2026-06-10)

- **plurigrid/gorj** (483 open issues) — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **plurigrid/place** — active TeX work  
- **kubeflow/pipelines** (4153★) — active ML pipeline work
- **kubeflow/mcp-apache-spark-history-server** (174★) — new MCP tooling for Spark
- **bmorphism/Gay.jl** — wide-gamut color sampling (189 open issues)
- **bmorphism/nanoclj-zig** — NaN-boxed Clojure interpreter in Zig

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (alice, bob, A-Z)

All 28 wallets queried via Aptos fullnode mainnet API.  
**Result: All balances returned 0.0 APT** — CoinStore resources return zero balance
(addresses may be unfunded or balances fully staked/delegated).

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A-Z | 0x8699...–0x7af0... | 0.0 each |

### Multisig Contract Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4...3003 | 2 | YES |
| A-G | 0xf56c...0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

**All 5 multisig contracts healthy (2-of-N threshold).**

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — HTTP 401 Vercel Authentication Required.
The SPA is behind Vercel deployment protection (visitor password required).
No market data extractable without credentials.

---

## DuckDB Schema Summary

```
world_increments   130 rows  GF3-colored increment log
repo_snapshots     130 rows  org/user repo metadata snapshots
aptos_snapshots     28 rows  hamming swarm wallet balances
multisig_probes      5 rows  A-B, A-G, Y-Z, S-T, V-W
mnx_snapshots        0 rows  unavailable (auth-gated)
```

*Sweep completed autonomously 2026-06-10 by world-increment-sweep + hamming-swarm-snapshot agent.*
