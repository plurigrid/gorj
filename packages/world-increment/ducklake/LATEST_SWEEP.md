# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-06  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 47 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social) | 7 |
| DJedamski | user (social) | 5 |
| wasita | user (social) | 7 |
| kristinezheng | user (social) | 4 |
| M1shaaa | user (social) | 6 |
| AustinCStone | user (social) | 8 |
| **Total** | | **285** |

### GF(3) Trit Color Distribution

| GF3 Name | Color | Trit | Count |
|----------|-------|------|-------|
| ERGODIC | `#d3869b` | 0 | 95 |
| PLUS | `#b8bb26` | 1 | 95 |
| MINUS | `#cc241d` | -1 | 95 |

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,706 | — |
| kubeflow/pipelines | 4,153 | Python |
| kubeflow/spark-operator | 3,125 | Python |
| kubeflow/trainer | 2,112 | Go |
| kubeflow/katib | 1,685 | Python |
| AustinCStone/TextGAN | 92 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| migalkin/NodePiece | 144 | Python |
| migalkin/StarE | 89 | Python |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |
| bmorphism/say-mcp-server | 20 | JavaScript |
| plurigrid/asi | 25 | HTML |

### Notable Recent Activity (pushed 2026-06-06)

- **plurigrid/gorj** — forj + Rama topology nREPL routing + GF(3) trit coloring (403 open issues)
- **kubeflow/pipelines** — Machine Learning Pipelines for Kubeflow (4,153 stars)
- **kubeflow/notebooks** — Kubeflow Notebooks on Kubernetes
- **bmorphism/Gay.jl** — Wide-gamut color sampling with splittable determinism (189 open issues)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Balances

All 28 Hamming swarm addresses queried via Aptos fullnode mainnet API.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A-Z (26 addresses) | 0x8699... - 0x7af0... | 0.0 each |

**Total swarm APT:** 0.0  
All addresses returned zero balance. Addresses may be unfunded or hold non-APT assets.

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | HEALTHY |
| A-G | 0xf56c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY |
| S-T | 0x3b1c...7883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

All 5 multisig contracts operational with 2-of-N threshold.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — testnet.mnx.fi is behind Vercel deployment protection. No market data accessible without bypass token. `mnx_snapshots` table is empty.

---

## DuckDB Schema Summary

```
world_increments  — 285 rows  (GF3 trit-colored repo snapshot events)
repo_snapshots    — 285 rows  (full repo metadata: stars, forks, language, pushed_at)
aptos_snapshots   —  28 rows  (Hamming swarm APT balances)
multisig_probes   —   5 rows  (multisig contract health)
mnx_snapshots     —   0 rows  (MNX unavailable)
```

Sweep executed: 2026-06-06 by world-increment-sweep + hamming-swarm-snapshot agent
