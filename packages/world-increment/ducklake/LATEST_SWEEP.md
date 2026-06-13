# World-Increment Sweep + Hamming Snapshot — 2026-06-13

## Sweep Metadata
- **Date:** 2026-06-13T16:14Z
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 61 |
| Total Repo Snapshots | 61 |
| Sources Covered | 3 orgs + 8 users |

### GF(3) Color Chain Distribution (61 increments)
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 20 |
| +1 | `#b8bb26` | PLUS | 21 |
| -1 | `#cc241d` | MINUS | 20 |

GF(3) assignment: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

### Repo Counts and Stars by Source

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| kubeflow | org | 10 | 28,772 |
| migalkin | user (social) | 4 | 268 |
| bmorphism | user | 9 | 91 |
| plurigrid | org | 15 | 36 |
| wasita | user (social) | 3 | 3 |
| TeglonLabs | org | 5 | 2 |
| zubyul | user | 7 | 1 |
| DJedamski | user (social) | 2 | 1 |
| M1shaaa | user (social) | 2 | 0 |
| kristinezheng | user (social) | 2 | 0 |
| AustinCStone | user (social) | 2 | 0 |
| **TOTAL** | | **61** | **29,174** |

### Notable Repos (2026-06-13 snapshot)

| Repo | Stars | Language | Pushed | Description |
|------|-------|----------|--------|-------------|
| kubeflow/kubeflow | 15,720 | — | 2026-06-11 | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4,153 | Python | 2026-06-13 | Machine Learning Pipelines |
| kubeflow/spark-operator | 3,128 | Python | 2026-06-12 | Kubernetes operator for Apache Spark |
| kubeflow/trainer | 2,114 | Go | 2026-06-13 | Distributed AI Model Training |
| kubeflow/katib | 1,683 | Python | 2026-06-12 | Automated ML on Kubernetes |
| kubeflow/community-distribution | 1,023 | YAML | 2026-06-12 | Kubeflow Community Distribution |
| migalkin/NodePiece | 144 | Python | 2022-02-02 | Compositional KG Representations (ICLR'22) |
| migalkin/StarE | 89 | Python | 2023-12-01 | EMNLP 2020: Hyper-Relational KGs |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 | OCaml SDK for Model Context Protocol |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 | MCP server for anti-bullshit |
| migalkin/kgcourse2021 | 25 | HTML | 2025-08-04 | Knowledge Graphs course materials |
| plurigrid/asi | 26 | HTML | 2026-06-10 | everything is topological chemputer! |
| plurigrid/gorj | 0 | Clojure | 2026-06-13 | forj + Rama topology nREPL routing + GF(3) trit coloring |
| TeglonLabs/jank-crane | 0 | C++ | 2026-06-08 | crane-jank converged-IR hub: GF3 convergence maps |
| bmorphism/Gay.jl | 1 | Julia | 2026-06-13 | Wide-gamut color sampling (189 open issues) |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 wallets)
Queried via `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result: All 28 wallets returned 0.0 APT** — CoinStore resource not initialized for these addresses on mainnet.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...12d5 | 0.0 |
| A–Z (26 wallets) | (see DuckDB) | 0.0 each |

### Multisig Contract Probes

Probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |

**All 5 multisig contracts healthy (2-of-N threshold confirmed).**

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — Protected by Vercel authentication. API paths `/api/markets`, `/api/v1/markets`, `/api/tickers` all return 401. No market data extractable without visitor bypass token. `mnx_snapshots` table is empty.

---

## DuckDB Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)   -- 61 rows

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)   -- 61 rows

aptos_snapshots(timestamp, world, address, balance_apt)  -- 28 rows
multisig_probes(timestamp, pair, address, sigs_required, healthy)  -- 5 rows
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)  -- 0 rows (auth wall)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS
