# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep date:** 2026-06-04  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 27 (top by activity) |
| kubeflow | org | 20 (top by stars) |
| TeglonLabs | org | 4 |
| bmorphism | user | 26 |
| zubyul | user | 15 |
| migalkin | user (social) | 7 |
| wasita | user (social) | 6 |
| AustinCStone | user (social) | 7 |
| DJedamski | user (social) | 4 |
| kristinezheng | user (social) | 4 |
| M1shaaa | user (social) | 3 |

**Total repo snapshots:** 122  
**Total world_increments:** 122 (GF(3) color-chained)

### GF(3) Color Chain Statistics

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | ~41 |
| 1 | `#b8bb26` | PLUS | ~41 |
| 2 | `#cc241d` | MINUS | ~40 |

### Notable Repos

**plurigrid** (most active, pushed 2026-06-04):
- `gorj` — forj + Rama topology nREPL routing + GF(3) gay trit coloring (354 open issues)
- `eirobri` — EiRoBri replay world (29 open issues)
- `asi` — everything is topological chemputer! ⭐25

**bmorphism** (prolific MCP builder):
- `Gay.jl` — Wide-gamut color sampling with splittable determinism (189 open issues)
- `ocaml-mcp-sdk` — OCaml SDK for MCP using Jane Street's oxcaml_effect ⭐61
- `anti-bullshit-mcp-server` — ⭐23
- `say-mcp-server` — ⭐20

**kubeflow** (largest by stars):
- `kubeflow/kubeflow` — ⭐15,705 ML Toolkit for Kubernetes
- `kubeflow/pipelines` — ⭐4,152 ML Pipelines
- `kubeflow/spark-operator` — ⭐3,124

**migalkin** (KG research):
- `NodePiece` — ⭐144 Compositional KG Representations (ICLR'22)
- `StarE` — ⭐89 Hyper-Relational KGs (EMNLP 2020)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

**Sweep timestamp:** 2026-06-04  
**Network:** Aptos Mainnet (`fullnode.mainnet.aptoslabs.com`)

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

**Note:** All 28 wallets returned 0 APT. Addresses either unfunded or `CoinStore` resource not initialized on mainnet.

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4...003 | 2 | ✅ |
| A-G | 0xf56c...096 | 2 | ✅ |
| Y-Z | 0xd3ff...883 | 2 | ✅ |
| S-T | 0x3b1c...883 | 2 | ✅ |
| V-W | 0x40fa...b6d | 2 | ✅ |

All 5 multisig contracts live and require **2-of-N signatures**. All healthy.

### MNX Markets (`testnet.mnx.fi`)

**Status:** Unavailable — Next.js SPA with no accessible API endpoints. `/api/markets` and `/api/v1/markets` serve the same HTML shell. `mnx_snapshots` table is empty this sweep.

---

## DuckDB Schema Summary

```sql
world_increments  -- 122 rows: GF(3)-colored increment log
repo_snapshots    -- 122 rows: GitHub repo metadata
aptos_snapshots   -- 28 rows: Hamming swarm wallet balances
multisig_probes   -- 5 rows: Aptos multisig contract health
mnx_snapshots     -- 0 rows: MNX market data (SPA unavailable)
```

## Useful Queries

```sql
-- Top stars
SELECT full_name, stars FROM repo_snapshots ORDER BY stars DESC LIMIT 10;

-- GF3 distribution
SELECT gf3_name, gf3_color, COUNT(*) FROM world_increments GROUP BY 1,2;

-- Non-zero Aptos balances
SELECT world, balance_apt FROM aptos_snapshots WHERE balance_apt > 0;

-- Multisig health
SELECT pair, sigs_required, healthy FROM multisig_probes;
```
