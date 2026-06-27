# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-27  
**GF(3) color chain:** ERGODIC=#d3869b (trit=0) → PLUS=#b8bb26 (trit=1) → MINUS=#cc241d (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos Snapshotted | Max Stars | Total Stars |
|--------|------|------------------:|----------:|------------:|
| plurigrid | org | 100 | 26 | 157 |
| kubeflow | org | 48 | 15,746 | 101,985 |
| TeglonLabs | org | 5 | 2 | 14 |
| bmorphism | user | 100 | 61 | 509 |
| zubyul | user | 49 | 2 | 40 |
| migalkin | user (social) | 19 | 144 | 834 |
| DJedamski | user (social) | 6 | 2 | 17 |
| wasita | user (social) | 11 | 2 | 11 |
| kristinezheng | user (social) | 5 | 0 | 0 |
| M1shaaa | user (social) | 8 | 0 | 0 |
| AustinCStone | user (social) | 30 | 92 | 324 |

**Total repos this sweep:** ~381 new snapshots  
**Total in DB:** 1325 repo_snapshots across all sweeps

### Notable Repos (this sweep)

| Repo | Language | Stars | Forks | Last Push |
|------|----------|------:|------:|-----------|
| kubeflow/kubeflow | — | 15,746 | 2,680 | 2026-06-18 |
| kubeflow/pipelines | Python | 4,156 | 2,012 | 2026-06-26 |
| kubeflow/spark-operator | Python | 3,128 | 1,491 | 2026-06-26 |
| kubeflow/trainer | Go | 2,123 | 972 | 2026-06-26 |
| plurigrid/gorj | Clojure | 0 | 0 | 2026-06-27 ← active now |
| plurigrid/asi | HTML | 26 | 8 | 2026-06-26 |
| bmorphism/Gay.jl | Julia | 2 | 1 | 2026-06-27 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2 | 2026-03-16 |
| TeglonLabs/jank-crane | C++ | 0 | 0 | 2026-06-08 |

### GF(3) Increment Chain

| id | trit | color | name | source |
|----|------|-------|------|--------|
| +n | 0 | #d3869b ERGODIC | sweep | plurigrid |
| +n+1 | 1 | #b8bb26 PLUS | sweep | kubeflow |
| +n+2 | -1 | #cc241d MINUS | sweep | TeglonLabs |
| +n+3 | 0 | #d3869b ERGODIC | sweep | bmorphism |
| +n+4 | 1 | #b8bb26 PLUS | sweep | zubyul |
| +n+5 | -1 | #cc241d MINUS | sweep | migalkin |
| +n+6 | 0 | #d3869b ERGODIC | sweep | DJedamski |
| +n+7 | 1 | #b8bb26 PLUS | sweep | wasita |
| +n+8 | -1 | #cc241d MINUS | sweep | kristinezheng |
| +n+9 | 0 | #d3869b ERGODIC | sweep | M1shaaa |
| +n+10 | 1 | #b8bb26 PLUS | sweep | AustinCStone |
| +n+11 | -1 | #cc241d MINUS | sweep | aptos-mainnet |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 wallets queried on 2026-06-27. All returned **0 APT** (CoinStore resource not found = wallets have 0 on-chain APT or uninitialized coin stores).

| World | Address (truncated) | Balance APT |
|-------|---------------------|------------:|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z (26 wallets) | 0x8699...–0x7af0... | 0.0 each |

**Total APT across swarm:** 0.0 APT

### Multisig Contract Probes (Aptos mainnet)

All 5 contracts successfully probed. All require **2-of-2 signatures** (healthy).

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|:---:|:---:|
| A-B | 0x0da4...7003 | 2 | yes |
| A-G | 0xf56c...0096 | 2 | yes |
| Y-Z | 0xd3ff...b883 | 2 | yes |
| S-T | 0x3b1c...7883 | 2 | yes |
| V-W | 0x40fa...eb6d | 2 | yes |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Vercel deployment protection enabled (HTTP 401). Requires visitor password or Trusted Sources OIDC token. No market data extractable without authentication.

---

## DuckDB Schema (packages/world-increment/ducklake/world-increments.duckdb)

- `world_increments` — 35 rows (GF3-colored event chain, cumulative)
- `repo_snapshots` — 1325 rows (cumulative sweeps)
- `aptos_snapshots` — 28 rows (this sweep)
- `multisig_probes` — 5 rows (this sweep)
- `mnx_snapshots` — 0 rows (unavailable)
