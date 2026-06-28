# World-Increment Sweep + Hamming Swarm Snapshot
**Run date:** 2026-06-28  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos captured |
|--------|------|----------------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 48 |
| AustinCStone | user (zubyul graph) | 40 |
| migalkin | user (zubyul graph) | 19 |
| wasita | user (zubyul graph) | 11 |
| M1shaaa | user (zubyul graph) | 8 |
| DJedamski | user (zubyul graph) | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user (zubyul graph) | 5 |
| **TOTAL** | | **391** |

### GF(3) Color Chain
| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 131 |
| +1 | PLUS | `#b8bb26` | 130 |
| -1 | MINUS | `#cc241d` | 130 |

### Top Languages Across All Repos
| Language | Repos |
|----------|-------|
| Python | 80 |
| Rust | 26 |
| JavaScript | 25 |
| TypeScript | 23 |
| HTML | 17 |
| Go | 15 |
| Jupyter Notebook | 14 |
| Clojure | 14 |
| Julia | 9 |
| Jsonnet | 7 |

### Most Starred Repos
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15750 | — | 2026-06-18 |
| kubeflow/pipelines | 4158 | Python | 2026-06-27 |
| kubeflow/spark-operator | 3129 | Python | 2026-06-26 |
| kubeflow/trainer | 2125 | Go | 2026-06-26 |
| kubeflow/katib | 1687 | Python | 2026-06-23 |

### Most Recently Pushed
| Repo | Pushed | Language |
|------|--------|----------|
| plurigrid/gorj | 2026-06-28T10:10Z | Clojure |
| M1shaaa/M1shaaa | 2026-06-28T03:29Z | — |
| plurigrid/asi | 2026-06-28T00:42Z | HTML |
| bmorphism/Gay.jl | 2026-06-28T00:39Z | Julia |
| plurigrid/place | 2026-06-27T22:03Z | TeX |
| kubeflow/hub | 2026-06-27T17:16Z | Go |
| kubeflow/pipelines | 2026-06-27T15:18Z | Python |

### TeglonLabs Highlights (GF3-tagged)
- **jank-crane** (C++): crane-jank converged-IR hub, loopify pass spec, GF3 convergence maps — pushed 2026-06-08
- **mathpix-gem** (Ruby): Math/chemistry OCR gem — 2 stars, 11 open issues
- **coin-flip-mcp** (JS): MCP server using random.org — 2 forks

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (alice, bob, A–Z)
All 28 addresses returned **0.0 APT** — no funded `CoinStore<AptosCoin>` resources found on mainnet. Addresses exist in the account namespace but hold no liquid APT (may hold other tokens or have unfunded coin stores).

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…2d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes
All 5 multisig accounts are **healthy** — responding with `num_signatures_required = 2` (2-of-N).

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4…7003 | 2 | healthy |
| A-G | 0xf56c…0096 | 2 | healthy |
| Y-Z | 0xd3ff…b883 | 2 | healthy |
| S-T | 0x3b1c…7883 | 2 | healthy |
| V-W | 0x40fa…eb6d | 2 | healthy |

### MNX Markets (testnet.mnx.fi)
**Unavailable** — site returns Vercel authentication wall. No market data extractable without a bypass token. `mnx_snapshots` table is empty.

---

## DuckDB Schema Summary

| Table | Rows |
|-------|------|
| world_increments | 391 |
| repo_snapshots | 391 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (auth-gated) |
