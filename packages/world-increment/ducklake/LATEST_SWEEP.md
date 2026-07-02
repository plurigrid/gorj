# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-02  
**DB:** `world-increments.duckdb`

---

## JOB 1 — GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| bmorphism | user | 20 (top by push date) |
| zubyul | user | 12 (top public) |
| migalkin | social graph | 5 (top) |
| TeglonLabs | org | 5 |
| wasita | social graph | 5 (top) |
| AustinCStone | social graph | 4 (top) |
| kristinezheng | social graph | 3 (top) |
| DJedamski | social graph | 3 (top) |
| M1shaaa | social graph | 2 (top) |
| **Total** | | **207** |

### GF(3) Color Chain

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 69 |
| +1 | `#b8bb26` | PLUS | 69 |
| -1 | `#cc241d` | MINUS | 69 |

*Perfect tripartite balance: 207 = 3 × 69*

### Notable Repos (most-starred)

| Repo | Stars | Lang | Description |
|------|-------|------|-------------|
| kubeflow/kubeflow | 15757 | — | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4167 | Python | ML Pipelines for Kubeflow |
| kubeflow/spark-operator | 3130 | Python | Kubernetes operator for Apache Spark |
| kubeflow/trainer | 2128 | Go | Distributed AI Model Training on Kubernetes |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | OCaml SDK for MCP (Jane Street oxcaml_effect) |
| migalkin/NodePiece | 144 | Python | Param-efficient KG representations (ICLR'22) |
| AustinCStone/TextGAN | 92 | Python | GAN for text generation (TensorFlow) |
| plurigrid/asi | 28 | HTML | everything is topological chemputer! |

### Recently Active (last 48h as of 2026-07-02)

- `kubeflow/pipelines` — 2026-07-02T19:06:09Z
- `plurigrid/gorj` — 2026-07-02T18:15:47Z (922 open issues)
- `kubeflow/notebooks` — 2026-07-02T17:54:18Z
- `wasita/wasita.github.io` — 2026-07-02T01:40:18Z
- `kristinezheng/kristinezheng.github.io` — 2026-07-01T20:57:48Z

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, mainnet)

All 28 addresses (alice, bob, A–Z) returned **0.0 APT** from the CoinStore resource. Accounts either have zero balance or have not initialized a CoinStore on Aptos mainnet.

### Multisig Probes (5 pairs)

All 5 multisig contracts returned `num_signatures_required = 2`. All healthy.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428… | 2 | healthy |
| A-G | 0xf56c4a1c… | 2 | healthy |
| Y-Z | 0xd3ffe181… | 2 | healthy |
| S-T | 0x3b1c3ae9… | 2 | healthy |
| V-W | 0x40fad7b4… | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

**Unavailable** — protected by Vercel deployment authentication. No market data extracted.

---

## DuckDB Schema Summary

| Table | Rows |
|-------|------|
| world_increments | 207 |
| repo_snapshots | 207 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (auth required) |

```sql
-- Top repos by stars
SELECT full_name, stars, language FROM repo_snapshots ORDER BY stars DESC LIMIT 10;

-- GF(3) distribution
SELECT gf3_name, gf3_color, COUNT(*) FROM world_increments GROUP BY 1,2;

-- Multisig health
SELECT pair, sigs_required, healthy FROM multisig_probes;
```
