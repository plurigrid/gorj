# World-Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-06-21  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d

---

## JOB 1 — GitHub Social Graph Sweep

### Sources

| Source | Type | Repos | Max ⭐ | Total ⭐ |
|--------|------|------:|------:|--------:|
| bmorphism | user | 96 | 61 | 503 |
| plurigrid | org | 79 | 26 | 157 |
| kubeflow | org | 48 | 15,739 | 101,962 |
| AustinCStone | user | 40 | 92 | 324 |
| migalkin | user | 19 | 144 | 834 |
| zubyul | user | 16 | 2 | 36 |
| wasita | user | 11 | 2 | 11 |
| M1shaaa | user | 8 | 0 | 0 |
| DJedamski | user | 6 | 1 | 17 |
| TeglonLabs | org | 5 | 2 | 14 |
| kristinezheng | user | 5 | 0 | 0 |
| **Total** | | **333** | | **104,858** |

### Top 10 Most Recently Pushed

| Repo | Language | ⭐ | Pushed |
|------|----------|--:|--------|
| plurigrid/gorj | Clojure | 0 | 2026-06-21T19:11Z |
| M1shaaa/M1shaaa | — | 0 | 2026-06-21T14:01Z |
| kubeflow/dashboard | TypeScript | 16 | 2026-06-21T00:56Z |
| bmorphism/Gay.jl | Julia | 2 | 2026-06-21T00:43Z |
| kubeflow/katib | Python | 1,684 | 2026-06-20T23:29Z |
| kubeflow/pipelines | Python | 4,156 | 2026-06-20T19:12Z |
| kubeflow/notebooks | — | 73 | 2026-06-20T17:12Z |
| kubeflow/hub | Go | 173 | 2026-06-20T15:40Z |
| bmorphism/satreadout | HTML | 0 | 2026-06-20T13:05Z |
| kubeflow/kale | Python | 694 | 2026-06-20T11:20Z |

### Top Starred

| Repo | ⭐ |
|------|-:|
| kubeflow/kubeflow | 15,739 |
| kubeflow/pipelines | 4,156 |
| kubeflow/spark-operator | 3,127 |
| kubeflow/trainer | 2,118 |
| kubeflow/katib | 1,684 |
| migalkin/NodePiece | 144 |
| AustinCStone/ml-resources | 92 |
| bmorphism/nix-darwin | 61 |

### GF(3) World-Increment Distribution

| Color | Name | Count |
|-------|------|------:|
| #d3869b | ERGODIC (trit=0) | 118 |
| #b8bb26 | PLUS (trit=1) | 119 |
| #cc241d | MINUS (trit=-1) | 119 |

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A–Z) queried via fullnode.mainnet.aptoslabs.com.

**Result: All balances = 0.0 APT** — accounts unfunded or CoinStore not initialized on mainnet.

### Multisig Probes (Aptos Mainnet)

| Pair | Address | Sigs Required | Healthy |
|------|---------|:-------------:|:-------:|
| A-B | 0x0da4f428...87003 | 2 | YES |
| A-G | 0xf56c4a1c...0096 | 2 | YES |
| Y-Z | 0xd3ffe181...b883 | 2 | YES |
| S-T | 0x3b1c3ae9...7883 | 2 | YES |
| V-W | 0x40fad7b4...eb6d | 2 | YES |

**Status: 5/5 multisigs HEALTHY** — all report 2-of-N signature threshold.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — HTTP 401 on all probed paths. API is auth-gated; no public market data accessible.

---

## DuckDB Tables Summary

| Table | Rows |
|-------|-----:|
| world_increments | 356 |
| repo_snapshots | 1,277 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

_repo_snapshots count reflects search-API pagination overlaps; 333 unique repos ingested._
