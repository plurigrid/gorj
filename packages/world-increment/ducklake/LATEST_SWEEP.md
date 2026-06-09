# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-09T21:10:00Z  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources

| Source | Type | Repos | Stars |
|--------|------|------:|------:|
| plurigrid | org | 100 | 76 |
| kubeflow | org | 48 | 34,192 |
| TeglonLabs | org | 5 | 2 |
| bmorphism | user | 100 | 247 |
| zubyul | user | 49 | 14 |
| migalkin | social graph | 6 | 279 |
| AustinCStone | social graph | 5 | 106 |
| wasita | social graph | 5 | 4 |
| DJedamski | social graph | 4 | 3 |
| kristinezheng | social graph | 4 | 0 |
| M1shaaa | social graph | 3 | 0 |
| **TOTAL** | | **329** | **34,923** |

### Top 10 Repos by Stars

| Repo | Stars | Language |
|------|------:|----------|
| kubeflow/kubeflow | 15,713 | — |
| kubeflow/pipelines | 4,153 | Python |
| kubeflow/spark-operator | 3,126 | Python |
| kubeflow/trainer | 2,112 | Go |
| kubeflow/katib | 1,685 | Python |
| kubeflow/examples | 1,462 | Jsonnet |
| kubeflow/manifests | 1,022 | YAML |
| kubeflow/arena | 812 | Go |
| kubeflow/kale | 692 | Python |
| migalkin/NodePiece | 144 | Python |

### Notable Recently Active (plurigrid orbit)

| Repo | Lang | Pushed | Notes |
|------|------|--------|-------|
| plurigrid/gorj | Clojure | 2026-06-09 | forj + Rama topology + GF(3) trit coloring |
| kubeflow/hub | Go | 2026-06-09 | Model Registry |
| kubeflow/trainer | Go | 2026-06-09 | Distributed AI + LLM fine-tuning on K8s |
| bmorphism/Gay.jl | Julia | 2026-06-09 | Wide-gamut color sampling, SPI pattern |
| TeglonLabs/jank-crane | C++ | 2026-06-08 | crane-jank converged-IR, GF3 convergence maps |
| plurigrid/eirobri | Clojure | 2026-06-03 | EiRoBri replay world |

### GF(3) Color Chain Distribution

| Trit | Hex | Name | Count |
|------|-----|------|------:|
| 0 | `#d3869b` | ERGODIC | 109 |
| +1 | `#b8bb26` | PLUS | 110 |
| -1 | `#cc241d` | MINUS | 110 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, ledger ~5,654,673,078)

All 28 Hamming swarm addresses probed via Aptos fullnode mainnet API.

**Result: All 28 wallets report 0.00000000 APT** — `resource_not_found` for
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. Accounts exist on-chain
but have no APT deposited in the standard coin module.

Total swarm balance: **0.00000000 APT**

| World | Address | APT |
|-------|---------|----:|
| alice | 0xc793...c7b | 0.0 |
| bob | 0x0a3c...55d | 0.0 |
| A–Z (26 addrs) | 0x8699...–0x7af0... | 0.0 each |

### Multisig Contract Probes (0x1::multisig_account::num_signatures_required)

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|:---:|----|
| A-B | 0x0da4...003 | **2** | HEALTHY |
| A-G | 0xf56c...096 | **2** | HEALTHY |
| Y-Z | 0xd3ff...883 | **2** | HEALTHY |
| S-T | 0x3b1c...883 | **2** | HEALTHY |
| V-W | 0x40fa...b6d | **2** | HEALTHY |

**All 5 multisig contracts operational — 2-of-N threshold confirmed.**

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — Protected by Vercel Deployment Protection (HTTP 401).
Both `/api/markets` and `/api/tickers` require visitor password or bypass token.
`mnx_snapshots` table remains empty this sweep.

---

## DuckDB Table Counts

```
world_increments : 329  (GF3-colored push events, IDs 1-329)
repo_snapshots   : 329  (full repo metadata snapshot)
aptos_snapshots  :  28  (Hamming swarm wallet balances)
multisig_probes  :   5  (pair contract sig thresholds)
mnx_snapshots    :   0  (unavailable)
```

## GF(3) Trit Semantics

| id % 3 | Trit | Color | Name | Meaning |
|--------|:----:|-------|------|---------|
| 0 | 0 | `#d3869b` | ERGODIC | equilibrium / steady state |
| 1 | +1 | `#b8bb26` | PLUS | constructive / additive |
| 2 | -1 | `#cc241d` | MINUS | contractive / subtractive |
