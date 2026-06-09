# World-Increment Sweep + Hamming Swarm Snapshot
**Generated:** 2026-06-09  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 26 |
| bmorphism | user | 20 |
| kubeflow | org | 20 |
| zubyul | user | 20 |
| TeglonLabs | org | 5 |
| migalkin | social-graph | 8 |
| wasita | social-graph | 8 |
| AustinCStone | social-graph | 7 |
| M1shaaa | social-graph | 7 |
| DJedamski | social-graph | 6 |
| kristinezheng | social-graph | 5 |
| **TOTAL** | | **132** |

### Notable Repos (by stars)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15713 | — | 2026-05-24 |
| kubeflow/pipelines | 4153 | Python | 2026-06-09 |
| kubeflow/spark-operator | 3126 | Python | 2026-06-09 |
| kubeflow/trainer | 2112 | Go | 2026-06-09 |
| kubeflow/katib | 1685 | Python | 2026-06-05 |
| kubeflow/manifests | 1022 | YAML | 2026-06-09 |
| kubeflow/arena | 812 | Go | 2026-05-07 |
| kubeflow/kale | 692 | Python | 2026-06-05 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| plurigrid/ontology | 8 | JavaScript | 2025-05-27 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| bmorphism/say-mcp-server | 20 | JavaScript | 2025-01-07 |
| bmorphism/babashka-mcp-server | 19 | JavaScript | 2025-01-05 |
| bmorphism/Gay.jl | 1 | Julia | 2026-06-09 |

### Hot Repos (pushed 2026-06-09)

- `kubeflow/pipelines` — ML Pipelines (Python, 4153 stars)
- `kubeflow/spark-operator` — Kubernetes Spark Operator (Python, 3126 stars)
- `kubeflow/trainer` — Distributed AI Training (Go, 2112 stars)
- `kubeflow/hub` — Model Registry (Go, 175 stars)
- `bmorphism/Gay.jl` — Wide-gamut color sampling (Julia, 189 open issues)
- `M1shaaa/M1shaaa` — GitHub profile config
- `TeglonLabs/jank-crane` — crane-jank converged-IR hub GF3 (C++, pushed 2026-06-08)

### GF(3) Color Chain Distribution (this sweep, 132 repos)

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 44 |
| 1 | PLUS | `#b8bb26` | 44 |
| -1 | MINUS | `#cc241d` | 44 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 Hamming swarm addresses probed via `fullnode.mainnet.aptoslabs.com`.  
**All addresses returned 0 APT** — CoinStore resource not found (accounts not yet activated / no APT deposited on mainnet).

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793acdec12b... | 0.0 |
| bob | 0x0a3c00c58fdf... | 0.0 |
| A–Z (26) | 0x8699... – 0x7af0... | 0.0 each |

### Multisig Contract Probes

All 5 multisig pairs probed via `0x1::multisig_account::num_signatures_required`.  
**All require 2-of-2 signatures. All healthy.**

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f428a0c0... | 2 | yes |
| A-G | 0xf56c4a1c0906... | 2 | yes |
| Y-Z | 0xd3ffe1812b2d... | 2 | yes |
| S-T | 0x3b1c3ae905d4... | 2 | yes |
| V-W | 0x40fad7b423a8... | 2 | yes |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is protected by Vercel deployment protection. No market data could be extracted. `mnx_snapshots` table is empty for this sweep.

---

## DuckDB Tables

| Table | Rows (this sweep) | Notes |
|-------|-------------------|-------|
| `world_increments` | 132 | GF(3) color chain, one per repo event |
| `repo_snapshots` | 132 | Full repo metadata |
| `aptos_snapshots` | 28 | All balances: 0.0 APT |
| `multisig_probes` | 5 | All 2-of-2, healthy |
| `mnx_snapshots` | 0 | Unavailable (Vercel auth) |

---

*Sweep timestamp: 2026-06-09*
