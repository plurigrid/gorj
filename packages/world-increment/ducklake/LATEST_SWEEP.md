# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-22

## Sweep Metadata
- **Date:** 2026-06-22
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Total Repos |
|--------|------|-------------|
| plurigrid | org | 101 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 105 |
| zubyul | user | 49 |
| migalkin | social graph | 19 |
| DJedamski | social graph | 6 |
| wasita | social graph | 11 |
| kristinezheng | social graph | 5 |
| M1shaaa | social graph | 8 |
| AustinCStone | social graph | 40 |
| **TOTAL** | | **397** |

### Notable Activity (pushed ≤ 48h, as of 2026-06-22)
| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/trainer | Go | 2118 | 2026-06-22 |
| kubeflow/sdk | Python | 120 | 2026-06-22 |
| kubeflow/pipelines | Python | 4157 | 2026-06-22 |
| plurigrid/gorj | Clojure | 0 | 2026-06-22 |
| bmorphism/Gay.jl | Julia | 2 | 2026-06-22 |
| plurigrid/place | TeX | 1 | 2026-06-20 |
| bmorphism/satreadout | HTML | 0 | 2026-06-20 |
| kubeflow/katib | Python | 1685 | 2026-06-20 |
| wasita/proj-template | — | 0 | 2026-06-19 |

### Top Stars Observed
| Repo | Stars | Description |
|------|-------|-------------|
| kubeflow/kubeflow | 15740 | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4157 | ML Pipelines for Kubeflow |
| kubeflow/spark-operator | 3128 | Kubernetes operator for Apache Spark |
| kubeflow/trainer | 2118 | Distributed AI Model Training on Kubernetes |
| kubeflow/katib | 1685 | AutoML on Kubernetes |
| migalkin/NodePiece | 144 | Parameter-Efficient KG Representations (ICLR'22) |
| AustinCStone/TextGAN | 92 | GAN for text generation (TensorFlow) |
| migalkin/StarE | 89 | Hyper-Relational Knowledge Graphs (EMNLP 2020) |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml SDK for MCP using Jane Street oxcaml_effect |

### GF(3) Color Chain (per-increment, id mod 3)
- `id%3==0` → trit=0, `#d3869b` **ERGODIC**
- `id%3==1` → trit=1, `#b8bb26` **PLUS**
- `id%3==2` → trit=-1, `#cc241d` **MINUS**

Chain cycles: PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → ...

### DuckDB Tables
```sql
world_increments  — 66 rows (cumulative across sweeps)
repo_snapshots    — 987 rows (cumulative)
aptos_snapshots   — 28 rows (this sweep)
multisig_probes   — 5 rows (this sweep)
mnx_snapshots     — 0 rows (unavailable)
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
Queried 28 wallets via `fullnode.mainnet.aptoslabs.com`.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z (26) | various | 0.0 each |

**Total APT across full swarm (alice + bob + A–Z): 0.0 APT**
All 28 wallets return empty `CoinStore` resources — accounts exist on-chain but hold no APT.

### Multisig Contract Probes (Aptos Mainnet)
5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✓ healthy |
| A-G | 0xf56c...096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...883 | 2 | ✓ healthy |
| S-T | 0x3b1c...883 | 2 | ✓ healthy |
| V-W | 0x40fa...b6d | 2 | ✓ healthy |

**5/5 multisig contracts healthy. All configured as 2-of-N.**

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE**  
`testnet.mnx.fi` is behind Vercel deployment protection (HTTP 401). Both `/api/markets` and `/api/v1/markets` require Vercel visitor password authentication. No market data could be extracted this sweep.

---

## Key Findings

| Domain | Finding |
|--------|---------|
| GitHub repos swept | 397 total across 3 orgs + 8 users |
| kubeflow activity | Hot — `trainer`, `sdk`, `pipelines` all pushed 2026-06-22 |
| plurigrid/gorj | Active — pushed today, 741 open issues |
| bmorphism/Gay.jl | Active — pushed today, 187 open issues |
| Hamming swarm balance | **0 APT total** — all 28 wallets empty |
| Multisig health | **5/5 healthy**, all 2-of-N |
| MNX markets | **Unavailable** (Vercel auth wall) |

---

## Schema Reference
```sql
-- GF(3) increment log
CREATE TABLE world_increments (
  id INTEGER, timestamp TIMESTAMP DEFAULT now(), gf3_trit INTEGER,
  gf3_color VARCHAR, gf3_name VARCHAR, source_type VARCHAR,
  source_name VARCHAR, event_type VARCHAR, repo_name VARCHAR,
  actor VARCHAR, snapshot_hash VARCHAR
);

-- GitHub repo snapshots
CREATE TABLE repo_snapshots (
  id INTEGER, timestamp TIMESTAMP DEFAULT now(), increment_id INTEGER,
  org_or_user VARCHAR, repo_name VARCHAR, full_name VARCHAR,
  language VARCHAR, stars INTEGER, forks INTEGER, open_issues INTEGER,
  pushed_at VARCHAR, description VARCHAR
);

-- Aptos Hamming swarm
CREATE TABLE aptos_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  world VARCHAR, address VARCHAR, balance_apt DOUBLE
);

-- Multisig health
CREATE TABLE multisig_probes (
  timestamp TIMESTAMP DEFAULT now(),
  pair VARCHAR, address VARCHAR, sigs_required INTEGER, healthy BOOLEAN
);

-- MNX markets (empty this sweep)
CREATE TABLE mnx_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  ticker VARCHAR, name VARCHAR, category VARCHAR,
  price DOUBLE, change_pct DOUBLE
);
```
