# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-08-09T21:00:00Z  
**GF(3) chain:** ERGODIC(0) #d3869b → PLUS(1) #b8bb26 → MINUS(-1) #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos in DB |
|--------|------|-------------|
| plurigrid | org | 210 |
| bmorphism | user | 205 |
| TeglonLabs | org | 111 |
| kubeflow | org | 99 |
| AustinCStone | social | 88 |
| migalkin | social | 63 |
| wasita | social | 63 |
| zubyul | user | 52 |
| kristinezheng | social | 37 |
| M1shaaa | social | 33 |
| DJedamski | social | 23 |

**Total repo_snapshots:** 984  
**Total world_increments:** 34 (GF3: ERGODIC=10, PLUS=12, MINUS=12)

### Notable Repos (Latest Push)
- `plurigrid/gorj` — forj + Rama topology + GF(3) trit coloring (pushed 2026-08-09)
- `plurigrid/place` — bci.place forester preview (pushed 2026-08-09)
- `kubeflow/spark-operator` — Kubernetes Spark operator, 3146★ (pushed 2026-08-09)
- `kubeflow/pipelines` — ML Pipelines for Kubeflow, 4180★ (pushed 2026-08-09)
- `bmorphism/Gay.jl` — Wide-gamut GF(3) color sampling, 188 issues open (pushed 2026-08-07)
- `wasita/wm-cv` — Academic CV (pushed 2026-08-07)
- `wasita/xoxowasita-analysis` — (pushed 2026-08-06)
- `wasita/joint-planning-lit` — (pushed 2026-08-04)
- `TeglonLabs/jank-crane` — crane-jank converged-IR hub with GF3 maps (pushed 2026-06-08)
- `migalkin/NodePiece` — ICLR'22 KG representation, 144★ (pushed 2026-05-07)

### DuckDB Ducklake
Location: `packages/world-increment/ducklake/world-increments.duckdb`

Tables:
- `world_increments` — GF(3)-colored increment events
- `repo_snapshots` — GitHub repo metadata snapshots
- `aptos_snapshots` — Hamming swarm APT balances
- `multisig_probes` — Multisig contract health checks
- `mnx_snapshots` — MNX market data (SPA, no REST API exposed)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, 2026-08-09)

All 28 addresses (alice, bob, A–Z) returned **0.00000000 APT** via the mainnet CoinStore resource endpoint. This indicates the CoinStore resource has not been initialized for these addresses on Aptos mainnet (accounts exist but hold no APT in this coin store resource).

| World | Address (short) | Balance APT |
|-------|----------------|-------------|
| alice | 0xc793...cc7b | 0.00000000 |
| bob | 0x0a3c...2d5d | 0.00000000 |
| A | 0x8699...9d7a | 0.00000000 |
| B | 0x3f89...b13 | 0.00000000 |
| ... | ... | 0.00000000 |
| Z | 0x7af0...97c | 0.00000000 |

### Multisig Contract Probes (5 pairs)

All 5 multisig pairs are **healthy** and require **2 signatures**:

| Pair | Address (short) | Sigs Required | Healthy |
|------|----------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` returns a Next.js SPA — no public REST API endpoint exposed at `/api/markets` or `/api/v1/markets`. Market data is unavailable without browser JS execution. Recorded as `SPA_unavailable` in `mnx_snapshots`.

---

## GF(3) Color Chain State

| ID mod 3 | Trit | Color | Name | Count |
|-----------|------|-------|------|-------|
| 0 | 0 | #d3869b | ERGODIC | 10 |
| 1 | +1 | #b8bb26 | PLUS | 12 |
| 2 | -1 | #cc241d | MINUS | 12 |
