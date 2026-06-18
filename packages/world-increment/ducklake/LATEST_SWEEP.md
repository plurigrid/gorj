# World Increment Sweep + Hamming Snapshot

**Generated:** 2026-06-18T UTC  
**Branch:** world-increment/sweep-$(date +%Y-%m-%d)  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Type | Name | Repos Snapshotted |
|------|------|-------------------|
| org | plurigrid | 15 |
| org | kubeflow | 14 |
| org | TeglonLabs | 5 |
| user | bmorphism | 12 |
| user | zubyul | 7 |
| user | migalkin | 5 |
| user | wasita | 5 |
| user | AustinCStone | 4 |
| user | kristinezheng | 3 |
| user | M1shaaa | 3 |
| user | DJedamski | 4 |
| **Total** | | **77** |

### GF(3) Trit Color Chain
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 25 |
| 1 | #b8bb26 | PLUS | 26 |
| -1 | #cc241d | MINUS | 26 |

### Top Repositories by Stars
| Repo | Language | ★ Stars | Forks |
|------|----------|---------|-------|
| kubeflow/kubeflow | — | 15,734 | 2,677 |
| kubeflow/pipelines | Python | 4,154 | 2,008 |
| kubeflow/spark-operator | Python | 3,127 | 1,490 |
| kubeflow/trainer | Go | 2,116 | 970 |
| kubeflow/katib | Python | 1,683 | 528 |
| migalkin/NodePiece | Python | 144 | 21 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2 |
| AustinCStone/TextGAN | Python | 92 | 30 |
| plurigrid/asi | HTML | 26 | 8 |

### Notable Activity
- **plurigrid/gorj** (this repo): 658 open issues, last pushed 2026-05-08
- **plurigrid/eirobri**: 29 open issues (private), last pushed 2026-05-19
- **kubeflow/docs-agent**: Active AI documentation agent, 152 open issues
- **bmorphism/Gay.jl**: 187 open issues — wide-gamut GF(3) color sampling project
- **TeglonLabs/jank-crane**: C++ crane-jank converged-IR hub with GF3 maps (newest: 2026-06-08)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
All 28 addresses (alice, bob, A–Z) returned **0.0 APT**.

Queried via `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` with 1s inter-call sleep.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z | various | 0.0 each |

> **Note:** Zero balances may indicate accounts not yet funded on mainnet, or the CoinStore resource hasn't been initialized.

### Multisig Contract Probes (5/5 healthy)
All 5 multisig accounts require exactly **2 signatures** and responded successfully.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — `testnet.mnx.fi` requires Vercel authentication (HTTP 401). All API paths (`/api/markets`, `/api/v1/markets`) returned auth-gated responses. No market data could be extracted.

---

## DuckDB Schema Summary
```
world_increments : 77 rows  (GF3-colored repo snapshots)
repo_snapshots   : 77 rows  (full repo metadata)
aptos_snapshots  : 28 rows  (alice, bob, A–Z balances)
multisig_probes  :  5 rows  (all 2-of-N, all healthy)
mnx_snapshots    :  0 rows  (unavailable — Vercel auth)
```
