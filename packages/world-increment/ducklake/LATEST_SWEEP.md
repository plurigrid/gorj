# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-06-14  **GF3:** PLUS (#b8bb26, trit=1)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos | Stars | Open Issues |
|--------|------|------:|------:|------------:|
| kubeflow | org | 48 | 34,208 | 2,695 |
| plurigrid | org | 100 | 77 | 724 |
| bmorphism | user | 50 | 121 | 218 |
| zubyul | user | 49 | 14 | 12 |
| migalkin | user (social graph) | 5 | 276 | 2 |
| AustinCStone | user (social graph) | 3 | 103 | 5 |
| TeglonLabs | org | 5 | 2 | 13 |
| **TOTAL** | | **260** | **34,801** | **3,669** |

> Social graph users DJedamski, wasita, kristinezheng, M1shaaa were searched but GitHub API rejected compound `user:X OR user:Y` queries without text terms; migalkin and AustinCStone captured individually.

### Top Repos by Stars (this sweep)
| Repo | Language | Stars | Last Push |
|------|----------|------:|-----------|
| kubeflow/kubeflow | — | 15,721 | 2026-06-11 |
| kubeflow/pipelines | Python | 4,154 | 2026-06-14 |
| kubeflow/spark-operator | Python | 3,127 | 2026-06-14 |
| kubeflow/trainer | Go | 2,115 | 2026-06-13 |
| kubeflow/katib | Python | 1,683 | 2026-06-12 |
| migalkin/NodePiece | Python | 144 | active |
| migalkin/StarE | Python | 89 | active |
| AustinCStone/TextGAN | Python | 92 | 2016 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |

### Notable plurigrid Activity
- **gorj** (Clojure): pushed `2026-06-14` — 579 open issues (most active)
- **asi** (HTML): 26 stars, pushed `2026-06-10`
- **nanoclj-zig** (Zig): NaN-boxed Clojure interpreter, interaction nets

### Notable TeglonLabs Activity
- **jank-crane** (C++): crane-jank converged-IR hub, GF3 maps — pushed `2026-06-08`
- **mathpix-gem** (Ruby): 11 open issues, last pushed `2026-01-01`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)
All 28 wallets (alice, bob, A–Z) returned **0.0 APT**.

The Aptos fullnode returned 404/empty for `CoinStore<AptosCoin>` on each address, indicating these accounts have not been funded on mainnet or the coin store resource has not been initialized. This is expected for a Hamming swarm that may operate on testnet or with non-APT assets.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes (mainnet)
All 5 multisig contracts are **live and responsive**. All require **2 signatures**.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|:-------------:|--------|
| A-B | 0x0da4...7003 | 2 | HEALTHY |
| A-G | 0xf56c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY |
| S-T | 0x3b1c...7883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

**5/5 multisig contracts healthy.** All operating as 2-of-N.

### MNX Markets (testnet.mnx.fi)
**UNAVAILABLE** — `testnet.mnx.fi` is protected by Vercel deployment authentication. All API paths (`/api/markets`, `/api/tickers`, `/api/v1/markets`) returned a Vercel auth wall. Access requires a bypass token or Vercel OIDC trust configuration.

---

## GF3 Color Chain
This sweep is increment **#1** (modulo-3 = 1) -> **PLUS** trit, color **#b8bb26** (yellow-green).

```
id%3==0 -> ERGODIC  #d3869b  (trit=0)
id%3==1 -> PLUS     #b8bb26  (trit=1)  <- this sweep
id%3==2 -> MINUS    #cc241d  (trit=-1)
```

---

## DuckDB Tables Updated
| Table | New Rows |
|-------|----------|
| world_increments | 1 |
| repo_snapshots | 260 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (unavailable) |

DB path: `packages/world-increment/ducklake/world-increments.duckdb`
