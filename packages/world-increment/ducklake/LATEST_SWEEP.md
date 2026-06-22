# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-22T23:14:27Z  
**Branch:** world-increment/sweep-2026-06-22-2314

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 48 |
| kubeflow | org | 10 |
| TeglonLabs | org | 5 |
| bmorphism | user | 17 |
| zubyul | user | 11 |
| migalkin | social-graph | 4 |
| wasita | social-graph | 3 |
| kristinezheng | social-graph | 3 |
| M1shaaa | social-graph | 3 |
| AustinCStone | social-graph | 2 |
| DJedamski | social-graph | 2 |

**Total repos this sweep:** 108  
**Total cumulative in DB:** 1052+

### Notable Repos (Top Stars This Sweep)

| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15740 | — | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4157 | Python | Machine Learning Pipelines for Kubeflow |
| kubeflow/spark-operator | 3128 | Python | Kubernetes operator for Apache Spark |
| migalkin/NodePiece | 144 | Python | Compositional Representations for Large KGs (ICLR'22) |
| kubeflow/trainer | 2118 | Go | Distributed AI Model Training on Kubernetes |
| plurigrid/gorj | 0 | Clojure | forj + Rama nREPL routing + GF(3) trit coloring (751 open issues — active!) |
| bmorphism/Gay.jl | 2 | Julia | Wide-gamut color sampling with splittable determinism (187 open issues) |
| AustinCStone/TextGAN | 92 | Python | GAN for text generation in TensorFlow |

### GF(3) Color Chain Applied
- `id%3==0` → trit=0, color=#d3869b, name=ERGODIC  
- `id%3==1` → trit=1, color=#b8bb26, name=PLUS  
- `id%3==2` → trit=-1, color=#cc241d, name=MINUS  

Each repo snapshot gets a world-increment entry with GF(3) trit assignment.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)

**All 28 addresses queried at:** 2026-06-22T23:14:27Z

> **Note:** All 28 addresses returned balance=0 APT. The Aptos fullnode responded with no CoinStore resources for these addresses — they either have no APT balance or the CoinStore has not been initialized. The accounts exist on-chain (multisig contracts referencing them are active) but carry no APT coin balance at time of query.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...7b | 0.0 |
| bob | 0x0a3c...5d | 0.0 |
| A | 0x8699...7a | 0.0 |
| B | 0x3f89...13 | 0.0 |
| C | 0x38b9...5e | 0.0 |
| D | 0xf776...d1 | 0.0 |
| E | 0xdc1d...36 | 0.0 |
| F | 0x18a1...71 | 0.0 |
| G | 0x69a3...32 | 0.0 |
| H | 0xce67...0f | 0.0 |
| I | 0x070f...c9 | 0.0 |
| J | 0x4d96...54 | 0.0 |
| K | 0xa732...c4 | 0.0 |
| L | 0x7c2e...a9 | 0.0 |
| M | 0x6fed...e9 | 0.0 |
| N | 0xe7dd...2c | 0.0 |
| O | 0x7325...9d | 0.0 |
| P | 0x6218...48 | 0.0 |
| Q | 0xac40...a9 | 0.0 |
| R | 0x7ce6...10 | 0.0 |
| S | 0xb875...86 | 0.0 |
| T | 0x3578...88 | 0.0 |
| U | 0x7586...56 | 0.0 |
| V | 0xb59d...c3 | 0.0 |
| W | 0x5f32...b0 | 0.0 |
| X | 0xa95c...7d | 0.0 |
| Y | 0xd8e3...c4 | 0.0 |
| Z | 0x7af0...7c | 0.0 |

### Multisig Contract Probes

All 5 multisig contracts are **healthy** — each requires exactly 2 signatures.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✓ healthy |
| A-G | 0xf56c...096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...883 | 2 | ✓ healthy |
| S-T | 0x3b1c...883 | 2 | ✓ healthy |
| V-W | 0x40fa...b6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Vercel deployment protection active. All API paths return HTTP 401 (Authentication Required). No bypass token available. No market data captured this sweep.

---

## DuckDB Schema Summary

```
world_increments   — GF(3)-colored world events
repo_snapshots     — GitHub repo metadata
aptos_snapshots    — Hamming swarm wallet balances  
multisig_probes    — Multisig contract health checks
mnx_snapshots      — MNX market data (empty this run)
```

**DB path:** `packages/world-increment/ducklake/world-increments.duckdb`
