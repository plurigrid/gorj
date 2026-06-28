# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-06-28  **GF(3) Color Chain Active**

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 9 (recent) |
| kubeflow | org | 7 (recent) |
| TeglonLabs | org | 5 |
| bmorphism | user | 6 (recent) |
| zubyul | user | 4 (recent) |
| migalkin | social | 3 (recent) |
| wasita | social | 3 (recent) |
| DJedamski | social | 2 |
| kristinezheng | social | 2 |
| M1shaaa | social | 2 |
| AustinCStone | social | 2 |

### Notable Activity (pushed ≤ 48h ago)
| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| plurigrid/gorj | 0 | Clojure | forj + Rama topology nREPL + GF(3) trit coloring |
| plurigrid/asi | 26 | HTML | everything is topological chemputer! |
| plurigrid/place | 1 | TeX | pushed 2026-06-27 |
| bmorphism/Gay.jl | 2 | Julia | Wide-gamut color sampling with SPI (187 open issues) |
| kubeflow/pipelines | 4158 | Python | ML Pipelines — active |
| kubeflow/spark-operator | 3129 | Python | Kubernetes Spark operator |
| wasita/wasita.github.io | 1 | Svelte | personal website — pushed 2026-06-25 |
| M1shaaa/M1shaaa | 0 | — | profile pushed 2026-06-28 |

### DuckDB ducklake State
```
world_increments: 68 rows  (GF3: ERGODIC=22, PLUS=23, MINUS=23)
repo_snapshots:   989 rows (cumulative across sweeps)
```

**GF(3) Color Chain Legend:**
- `id%3==0` → trit=0 ERGODIC `#d3869b`
- `id%3==1` → trit=1 PLUS `#b8bb26`
- `id%3==2` → trit=-1 MINUS `#cc241d`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances
All 28 addresses (alice, bob, A–Z) probed via Aptos fullnode mainnet API.

**Result:** All 28 addresses returned **0.0 APT** (CoinStore resource not found or zero balance).

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...9956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

### Multisig Contract Probes
All 5 multisig contracts healthy — all require 2-of-N signatures.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | HEALTHY |
| A-G | 0xf56c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY |
| S-T | 0x3b1c...7883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

### MNX Markets
`https://testnet.mnx.fi` — **UNAVAILABLE** (Vercel deployment protection active; market data inaccessible without bypass token).

---

## DuckDB Schema Summary
```sql
world_increments  -- GF(3)-colored event log (68 rows total)
repo_snapshots    -- GitHub repo metadata (989 rows cumulative)
aptos_snapshots   -- Hamming swarm wallet balances (28 rows this sweep)
multisig_probes   -- Multisig contract health (5 rows this sweep)
mnx_snapshots     -- MNX market data (1 row: unavailable)
```

DB path: `packages/world-increment/ducklake/world-increments.duckdb`
