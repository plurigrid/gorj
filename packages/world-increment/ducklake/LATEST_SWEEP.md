# World Increment Sweep + Hamming Swarm Snapshot

**Sweep date:** 2026-05-08  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain

| id%3 | trit | color | name |
|------|------|-------|------|
| 0 | 0 | `#d3869b` | ERGODIC |
| 1 | +1 | `#b8bb26` | PLUS |
| 2 | -1 | `#cc241d` | MINUS |

### Sources Swept

| Source | Type | Repos Snapshotted | GF(3) |
|--------|------|-------------------|
-------|
| plurigrid | org | 22 | PLUS `#b8bb26` |
| kubeflow | org | 15 | MINUS `#cc241d` |
| TeglonLabs | org | 4 | ERGODIC `#d3869b` |
| bmorphism | user | 11 | PLUS `#b8bb26` |
| zubyul | user | 10 | MINUS `#cc241d` |
| migalkin | user (social graph) | 6 | ERGODIC `#d3869b` |
| DJedamski | user (social graph) | 6 | PLUS `#b8bb26` |
| wasita | user (social graph) | 1 | MINUS `#cc241d` |
| kristinezheng | user (social graph) | 6 | ERGODIC `#d3869b` |
| M1shaaa | user (social graph) | 8 | PLUS `#b8bb26` |
| AustinCStone | user (social graph) | 7 | MINUS `#cc241d` |

**Total repo snapshots:** 96  
**Total world increments:** 13

### Notable Repos

| Repo | Stars | Language | Description |
|------|-------|----------|
-------------|
| kubeflow/kubeflow | 15,626 | — | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4,136 | Python | Machine Learning Pipelines for Kubeflow |
| kubeflow/spark-operator | 3,124 | Python | Kubernetes Spark operator |
| kubeflow/trainer | 2,096 | Go | Distributed AI Model Training on Kubernetes |
| plurigrid/asi | 21 | HTML | everything is topological chemputer! |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | MCP server for analyzing claims and detecting manipulation |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | OCaml SDK for Model Context Protocol |
| migalkin/NodePiece | 144 | Python | Compositional KG Representations (ICLR'22) |
| migalkin/StarE | 89 | Python | Hyper-Relational KG Message Passing (EMNLP 2020) |
| AustinCStone/TextGAN | 92 | Python | GAN for text generation in TensorFlow |
| plurigrid/gorj | 0 | Clojure | forj + Rama topology nREPL routing + GF(3) gay trit coloring |

### Recently Active (2026-05-08)

- `plurigrid/gorj` — pushed 2026-05-08T18:12:14Z
- `kubeflow/community` — pushed 2026-05-08T18:59:29Z
- `bmorphism/Gay.jl` — pushed 2026-05-08T00:32:04Z
- `M1shaaa/M1shaaa` — pushed 2026-05-08T13:25:36Z

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 wallets queried against `fullnode.mainnet.aptoslabs.com` on 2026-05-08.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | `0xc793ac...` | 0.0 |
| bob | `0x0a3c00...` | 0.0 |
| A | `0x8699ed...` | 0.0 |
| B | `0x3f892e...` | 0.0 |
| C | `0x38b99e...` | 0.0 |
| D | `0xf77656...` | 0.0 |
| E | `0xdc1d9d...` | 0.0 |
| F | `0x18a14b...` | 0.0 |
| G | `0x69a394...` | 0.0 |
| H | `0xce67c3...` | 0.0 |
| I | `0x070fe5...` | 0.0 |
| J | `0x4d964d...` | 0.0 |
| K | `0xa73204...` | 0.0 |
| L | `0x7c2eae...` | 0.0 |
| M | `0x6fed37...` | 0.0 |
| N | `0xe7dde6...` | 0.0 |
| O | `0x73252b...` | 0.0 |
| P | `0x621879...` | 0.0 |
| Q | `0xac40fa...` | 0.0 |
| R | `0x7ce605...` | 0.0 |
| S | `0xb87530...` | 0.0 |
| T | `0x35781d...` | 0.0 |
| U | `0x75860d...` | 0.0 |
| V | `0xb59dd8...` | 0.0 |
| W | `0x5f32ae...` | 0.0 |
| X | `0xa95cbb...` | 0.0 |
| Y | `0xd8e328...` | 0.0 |
| Z | `0x7af0ef...` | 0.0 |

**All 28 wallets: 0.0 APT** — wallets are either unfunded or CoinStore resource not registered.

### Multisig Contract Probes

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | `0x0da4f4...` | 2 | HEALTHY |
| A-G | `0xf56c4a...` | 2 | HEALTHY |
| Y-Z | `0xd3ffe1...` | 2 | HEALTHY |
| S-T | `0x3b1c3a...` | 2 | HEALTHY |
| V-W | `0x40fad7...` | 2 | HEALTHY |

**All 5 multisigs healthy: 2-of-2 threshold confirmed via `0x1::multisig_account::num_signatures_required`**

### MNX Markets

`https://testnet.mnx.fi/api/markets` — **UNAVAILABLE** (SPA returns HTML; no REST market data endpoint exposed).
Root URL `https://testnet.mnx.fi` returns HTTP 200 with CSP headers referencing `https://api.testnet.mnx.fi`. Direct API path probing returned no structured market data. `mnx_snapshots` table is empty.

---

## DuckDB Tables

| Table | Rows |
|-------|------|
| `world_increments` | 13 |
| `repo_snapshots` | 96 |
| `aptos_snapshots` | 28 |
| `multisig_probes` | 5 |
| `mnx_snapshots` | 0 |

```sql
-- Query example: top repos by stars
SELECT org_or_user, repo_name, stars, language
FROM repo_snapshots
ORDER BY stars DESC
LIMIT 10;
```

> Regenerate from `populate.sql`: `duckdb world-increments.duckdb -c "$(cat populate.sql)"`
