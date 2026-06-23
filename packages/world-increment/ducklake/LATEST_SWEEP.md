# World Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-06-23  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) Chain:** ERGODIC(#d3869b, trit=0) → PLUS(#b8bb26, trit=1) → MINUS(#cc241d, trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Summary
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 48 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| wasita | user | 11 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user | 5 |
| **TOTAL** | | **391** |

### GF(3) Color Distribution (world_increments)
| Color | GF(3) Name | Trit | Count |
|-------|-----------|------|-------|
| #d3869b | ERGODIC | 0 | ~131 |
| #b8bb26 | PLUS | +1 | ~130 |
| #cc241d | MINUS | -1 | ~130 |

GF(3) assignment: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

### Top Repos by Stars
| Repo | Stars | Language |
|------|-------|---------|
| kubeflow/kubeflow | 15,739 | — |
| kubeflow/pipelines | 4,157 | Python |
| kubeflow/spark-operator | 3,128 | Python |
| kubeflow/trainer | 2,119 | Go |
| kubeflow/katib | 1,685 | Python |
| kubeflow/examples | 1,460 | Jsonnet |
| kubeflow/community-distribution | 1,028 | YAML |
| kubeflow/arena | 813 | Go |
| kubeflow/kale | 694 | Python |

### Notable Recent Activity
- **TeglonLabs/jank-crane** (C++, pushed 2026-06-08): "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow"
- **M1shaaa/M1shaaa** (profile, pushed 2026-06-23): active today
- **kristinezheng/kristinezheng.github.io** (HTML, pushed 2026-06-07): recent personal site update
- **wasita/proj-template** (pushed 2026-06-19): most recent wasita activity

---

## JOB 2: Hamming Swarm Snapshot

### Aptos APT Balances (28 addresses, mainnet)
**Total swarm balance: 20.34 APT**  
**Method:** `0x1::coin::balance` view function on mainnet

| World | Balance (APT) | Tier |
|-------|--------------|------|
| bob | 12.6570 | HIGH |
| F | 1.9605 | MED |
| L | 1.9273 | MED |
| J | 1.8951 | MED |
| alice | 0.4364 | LOW |
| O | 0.2101 | LOW |
| K | 0.1620 | LOW |
| P | 0.1401 | LOW |
| M | 0.1123 | LOW |
| N | 0.1061 | LOW |
| Q | 0.1032 | LOW |
| S | 0.0918 | LOW |
| R | 0.0902 | LOW |
| T | 0.0737 | LOW |
| U | 0.0558 | LOW |
| A | 0.0518 | LOW |
| V | 0.0488 | LOW |
| Y | 0.0444 | LOW |
| X | 0.0426 | LOW |
| W | 0.0407 | LOW |
| B | 0.0363 | LOW |
| Z | 0.0243 | DUST |
| D | 0.0116 | DUST |
| C | 0.0102 | DUST |
| E | 0.0094 | DUST |
| H | 0.0017 | DUST |
| I | 0.0007 | DUST |
| G | 0.0007 | DUST |

**Notable:** `bob` holds 62.3% of total swarm APT (12.66/20.34). Tier F/L/J each hold ~1.9 APT. Note: alice's account has sequence_number=72 confirming it is active on-chain.

### Multisig Contract Probes (5 pairs, all 2-of-N)
All 5 multisig accounts **healthy**.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | 0x0da4f428... | 2 | HEALTHY |
| A-G | 0xf56c4a1c... | 2 | HEALTHY |
| Y-Z | 0xd3ffe181... | 2 | HEALTHY |
| S-T | 0x3b1c3ae9... | 2 | HEALTHY |
| V-W | 0x40fad7b4... | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — site requires Vercel authentication for all endpoints. No public market data accessible without credentials.

---

## DuckDB Table Summary
```
world_increments   391 rows — GF(3) tagged increments
repo_snapshots     391 rows — full repo metadata per source
aptos_snapshots     28 rows — APT balances (mainnet)
multisig_probes      5 rows — all healthy (2-of-N=2)
mnx_snapshots        1 row  — UNAVAILABLE marker
```

---

## Schema Reference
```sql
CREATE TABLE world_increments (
  id INTEGER, timestamp TIMESTAMP, gf3_trit INTEGER,
  gf3_color VARCHAR, gf3_name VARCHAR, source_type VARCHAR,
  source_name VARCHAR, event_type VARCHAR, repo_name VARCHAR,
  actor VARCHAR, snapshot_hash VARCHAR
);
CREATE TABLE repo_snapshots (
  id INTEGER, timestamp TIMESTAMP, increment_id INTEGER,
  org_or_user VARCHAR, repo_name VARCHAR, full_name VARCHAR,
  language VARCHAR, stars INTEGER, forks INTEGER, open_issues INTEGER,
  pushed_at VARCHAR, description VARCHAR
);
CREATE TABLE aptos_snapshots (
  timestamp TIMESTAMP, world VARCHAR, address VARCHAR, balance_apt DOUBLE
);
CREATE TABLE multisig_probes (
  timestamp TIMESTAMP, pair VARCHAR, address VARCHAR,
  sigs_required INTEGER, healthy BOOLEAN
);
CREATE TABLE mnx_snapshots (
  timestamp TIMESTAMP, ticker VARCHAR, name VARCHAR,
  category VARCHAR, price DOUBLE, change_pct DOUBLE
);
```

---
*Sweep executed 2026-06-23 by world-increment-sweep + hamming-swarm-snapshot agent*
