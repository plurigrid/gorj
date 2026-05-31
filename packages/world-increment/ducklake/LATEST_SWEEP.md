# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-31

## Sweep Metadata
- **Date:** 2026-05-31
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social (zubyul) | 19 |
| DJedamski | social (zubyul) | 6 |
| wasita | social (zubyul) | 11 |
| kristinezheng | social (zubyul) | 6 |
| M1shaaa | social (zubyul) | 8 |
| AustinCStone | social (zubyul) | 40 |
| **TOTAL** | | **391** |

### GF(3) Trit Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 130 |
| 1 | `#b8bb26` | PLUS | 131 |
| -1 | `#cc241d` | MINUS | 130 |

Assignment rule: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS.

### Notable Repos (top by stars)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,693 | — | 2026-05-24 |
| kubeflow/pipelines | 4,149 | Python | 2026-05-30 |
| kubeflow/spark-operator | 3,124 | Python | 2026-05-29 |
| kubeflow/trainer | 2,107 | Go | 2026-05-30 |
| kubeflow/katib | 1,685 | Python | 2026-05-29 |
| kubeflow/examples | 1,463 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,019 | YAML | 2026-05-29 |
| kubeflow/arena | 811 | Go | 2026-05-07 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/asi | 23 | HTML | 2026-04-26 |

### Most Active (pushed ≤7 days from sweep: 2026-05-24 to 2026-05-31)

- `plurigrid/eirobri` — Clojure, EiRoBri replay world (2026-05-26)
- `plurigrid/gorj` — Clojure, forj + Rama topology + GF(3) coloring (2026-05-31)
- `bmorphism/Gay.jl` — Julia, wide-gamut GF(3) color sampling (2026-05-31)
- `kubeflow/pipelines` — Python, ML Pipelines (2026-05-30)
- `kubeflow/trainer` — Go, Distributed AI training (2026-05-30)
- `kubeflow/katib` — Python, AutoML (2026-05-29)
- `kubeflow/notebooks` — Kubeflow Notebooks (2026-05-29)
- `kubeflow/hub` — Go, Model Registry (2026-05-29)
- `migalkin/RWL` — Python, Weisfeiler-Leman Relational (2026-05-28)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

Queried via `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. 1s sleep between calls.

| World | Balance (APT) |
|-------|--------------|
| alice | 0.0 |
| bob | 0.0 |
| A | 0.0 |
| B | 0.0 |
| C | 0.0 |
| D | 0.0 |
| E | 0.0 |
| F | 0.0 |
| G | 0.0 |
| H | 0.0 |
| I | 0.0 |
| J | 0.0 |
| K | 0.0 |
| L | 0.0 |
| M | 0.0 |
| N | 0.0 |
| O | 0.0 |
| P | 0.0 |
| Q | 0.0 |
| R | 0.0 |
| S | 0.0 |
| T | 0.0 |
| U | 0.0 |
| V | 0.0 |
| W | 0.0 |
| X | 0.0 |
| Y | 0.0 |
| Z | 0.0 |

**Total swarm balance: 0.0 APT** (wallets unfunded or CoinStore not initialized).

### Multisig Contract Probes

Probed via `POST /v1/view` with `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | `0x0da4f428...` | 2 | ✅ |
| A-G | `0xf56c4a1c...` | 2 | ✅ |
| Y-Z | `0xd3ffe181...` | 2 | ✅ |
| S-T | `0x3b1c3ae9...` | 2 | ✅ |
| V-W | `0x40fad7b4...` | 2 | ✅ |

All 5 multisig accounts healthy (2-of-n threshold, live on Aptos mainnet).

### MNX Markets

- **Endpoint:** `https://testnet.mnx.fi/api/markets`
- **Status:** Unavailable — no data returned (SPA or service offline)
- **Recorded as:** `ticker=unavailable` in `mnx_snapshots`

---

## DuckDB Tables

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 391 | GF(3)-colored event log per repo |
| `repo_snapshots` | 391 | Repo metadata snapshot |
| `aptos_snapshots` | 28 | Hamming swarm wallet balances |
| `multisig_probes` | 5 | Multisig account health |
| `mnx_snapshots` | 1 | MNX market data (unavailable) |

### Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```

### Example Queries
```sql
-- Top repos by stars
SELECT full_name, language, stars FROM repo_snapshots
ORDER BY stars DESC LIMIT 10;

-- GF(3) sweep summary
SELECT gf3_name, gf3_color, count(*) as n
FROM world_increments GROUP BY gf3_name, gf3_color;

-- Healthy multisigs
SELECT pair, address, sigs_required
FROM multisig_probes WHERE healthy = true;

-- All Aptos balances
SELECT world, address, balance_apt FROM aptos_snapshots ORDER BY world;
```
