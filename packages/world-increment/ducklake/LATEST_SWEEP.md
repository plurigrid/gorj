# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-06-10  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| DJedamski | user | 6 |
| wasita | user | 11 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| AustinCStone | user | 40 |
| **TOTAL** | | **391** |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 131 |
| 1 | #b8bb26 | PLUS | 130 |
| -1 | #cc241d | MINUS | 130 |

### Top Repos by Stars

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15714 | — | 2026-05-24 |
| kubeflow/pipelines | 4153 | Python | 2026-06-10 |
| kubeflow/spark-operator | 3126 | Python | 2026-06-09 |
| kubeflow/trainer | 2112 | Go | 2026-06-10 |
| kubeflow/katib | 1685 | Python | 2026-06-05 |
| kubeflow/examples | 1462 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1022 | YAML | 2026-06-09 |
| kubeflow/arena | 812 | Go | 2026-05-07 |
| kubeflow/kale | 693 | Python | 2026-06-10 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/asi | 25 | HTML | 2026-06-10 |
| migalkin/kgcourse2021 | 25 | HTML | 2025-08-04 |
| bmorphism/risc0-cosmwasm-example | 23 | Rust | 2022-10-20 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| bmorphism/say-mcp-server | 20 | JavaScript | 2025-01-07 |

### Recently Active Repos (pushed 2026-06)

- **plurigrid/gorj** — 481 open issues, Clojure, forj + Rama + GF(3)
- **bmorphism/Gay.jl** — Julia, wide-gamut color sampling (189 issues)
- **kubeflow/kale** — Python, superfood for Data Scientists
- **M1shaaa/M1shaaa** — pushed 2026-06-10T15:25:37Z
- **plurigrid/place** — TeX, 8 open issues
- **TeglonLabs/jank-crane** — C++, crane-jank converged-IR hub + GF3 maps

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 Hamming-swarm wallets queried against Aptos mainnet
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result: All wallets returned null (no CoinStore resource) → 0.0 APT each.**

Addresses may be fresh/unused or holding non-APT assets only.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes (Aptos Mainnet)

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | YES |
| A-G | 0xf56c...096 | 2 | YES |
| Y-Z | 0xd3ff...883 | 2 | YES |
| S-T | 0x3b1c...883 | 2 | YES |
| V-W | 0x40fa...b6d | 2 | YES |

All 5 multisig contracts healthy — 2-of-N threshold, responding to view calls.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — site requires Vercel deployment authentication (HTTP 401).
No market data ingested; mnx_snapshots table is empty for this sweep.

---

## DuckDB Schema Summary

```
world_increments  : 391 rows  (repo snapshots with GF3 color assignment)
repo_snapshots    : 391 rows  (full metadata for each repo)
aptos_snapshots   :  28 rows  (Hamming swarm wallet balances)
multisig_probes   :   5 rows  (multisig contract health checks)
mnx_snapshots     :   0 rows  (unavailable — Vercel auth required)
```

## GF(3) Color Legend

- ERGODIC  #d3869b  trit=0   ids where id%3==0
- PLUS     #b8bb26  trit=1   ids where id%3==1
- MINUS    #cc241d  trit=-1  ids where id%3==2
