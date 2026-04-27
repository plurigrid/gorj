# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-04-27T02:15Z  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**DuckDB version:** v1.5.2 (Variegata)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried This Sweep

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 100 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (zubyul graph) | 19 |
| DJedamski | user (zubyul graph) | 6 |
| wasita | user (zubyul graph) | 10 |
| kristinezheng | user (zubyul graph) | 6 |
| M1shaaa | user (zubyul graph) | 8 |
| AustinCStone | user (zubyul graph) | 40 |
| **Total new repos** | | **389** |

### DuckDB State After Sweep

| Table | Total Rows |
|-------|-----------|
| world_increments | 412 |
| repo_snapshots | 1333 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 136 |
| 1 | `#b8bb26` | PLUS | 138 |
| -1 | `#cc241d` | MINUS | 138 |

GF(3) rule: `id%3==0 → ERGODIC #d3869b`, `id%3==1 → PLUS #b8bb26`, `id%3==2 → MINUS #cc241d`

### Top Languages (Cumulative)

| Language | Repos | Stars |
|----------|-------|-------|
| Python | 234 | 31290 |
| Go | 51 | 11930 |
| Jsonnet | 24 | 7229 |
| TypeScript | 47 | 1004 |
| Jupyter Notebook | 40 | 798 |
| Rust | 57 | 52 |
| JavaScript | 52 | 205 |
| HTML | 51 | 687 |
| Clojure | 29 | 6 |
| R | 22 | 15 |

### Most Recently Active Repos

| Repo | Pushed At |
|------|-----------|
| kubeflow/hub | 2026-04-27T00:43:04Z |
| plurigrid/gorj | 2026-04-27T00:31:52Z |
| bmorphism/Gay.jl | 2026-04-27T00:28:09Z |
| kubeflow/pipelines | 2026-04-26T20:55:05Z |
| plurigrid/horse | 2026-04-26T17:05:10Z |

### Notable Repos (by Stars)

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15605 | — |
| kubeflow/pipelines | 4126 | Python |
| kubeflow/spark-operator | 3120 | Python |
| kubeflow/trainer | 2094 | Go |
| migalkin/NodePiece | 143+ | Python |
| AustinCStone/TextGAN | 92+ | Python |
| bmorphism/ocaml-mcp-sdk | 60+ | OCaml |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

28 addresses queried (alice, bob, A–Z). All returned **0.0 APT** — CoinStore resource not found on Aptos mainnet fullnode for any address.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...5d5d | 0.0 |
| A–Z (26) | various | 0.0 each |

### Multisig Contract Probes

5 pair contracts probed via `0x1::multisig_account::num_signatures_required`. None had the multisig module instantiated on mainnet:

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | — | false |
| A-G | 0xf56c...096 | — | false |
| Y-Z | 0xd3ff...883 | — | false |
| S-T | 0x3b1c...883 | — | false |
| V-W | 0x40fa...b6d | — | false |

### MNX Markets

`testnet.mnx.fi` was **unavailable** at sweep time (connection refused on all probed endpoints: `/`, `/api/markets`, `/api/v1/markets`, `/markets`). No `mnx_snapshots` rows inserted.

---

## DuckDB Query Examples

```sql
-- Recent world increments with GF3 color
SELECT id, gf3_name, gf3_color, repo_name, timestamp
FROM world_increments ORDER BY id DESC LIMIT 10;

-- Stars by language
SELECT language, COUNT(*) repos, SUM(stars) stars
FROM repo_snapshots WHERE language != ''
GROUP BY language ORDER BY stars DESC;

-- Aptos snapshot
SELECT world, address, balance_apt FROM aptos_snapshots
ORDER BY world;

-- Multisig health
SELECT pair, address, sigs_required, healthy
FROM multisig_probes ORDER BY pair;
```

## Schema

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
