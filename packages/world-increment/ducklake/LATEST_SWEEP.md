# World-Increment Sweep — 2026-04-06 (+ Hamming Swarm Snapshot)

## Sweep Metadata
- **Date:** 2026-04-06T16:30:00Z
- **Agent:** claude-code autonomous sweep
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Session:** https://claude.ai/code/session_01MUSuF67mwBBcGYEhxtggM6

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 12 |
| Total Repo Snapshots | 40 |
| Sources Covered | 3 orgs + 5 users |

---

## GF(3) Color Chain — All 12 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | bmorphism | IssuesEvent (gorj) | +1 | `#b8bb26` | **PLUS** |
| 2  | bmorphism | IssuesEvent (asi) | -1 | `#cc241d` | **MINUS** |
| 3  | bmorphism | PushEvent (lolita) | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | PushEvent (asi) | +1 | `#b8bb26` | **PLUS** |
| 5  | bmorphism | PullRequestEvent (asi) | -1 | `#cc241d` | **MINUS** |
| 6  | bmorphism | PushEvent (gorj) | 0 | `#d3869b` | **ERGODIC** |
| 7  | bmorphism | CreateEvent (gorj) | +1 | `#b8bb26` | **PLUS** |
| 8  | bmorphism | WatchEvent (au-ts/sddf) | -1 | `#cc241d` | **MINUS** |
| 9  | bmorphism | PushEvent (asi) | 0 | `#d3869b` | **ERGODIC** |
| 10 | bmorphism | PullRequestEvent (asi) | +1 | `#b8bb26` | **PLUS** |
| 11 | bmorphism | CreateEvent (gtc2026-floxxy) | -1 | `#cc241d` | **MINUS** |
| 12 | bmorphism | PushEvent (zig-syrup) | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## Top Repos by Source

### plurigrid (12 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi-skills | Julia | 1 | 2026-03-28 |
| zig-syrup | Zig | 1 | 2026-03-28 |
| asi | HTML | 13 | 2026-03-28 |
| gorj | Clojure | 0 | 2026-03-28 |
| lolita | Python | 0 | 2026-03-28 |

### kubeflow (9 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| pipelines | Python | 4112 | 2026-03-28 |
| mcp-apache-spark-history-server | Python | 144 | 2026-03-28 |
| spark-operator | Python | 3110 | 2026-03-27 |
| trainer | Go | 2068 | 2026-03-26 |

### TeglonLabs (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| vibespace | HTML | 2 |
| Stahl | Rust | 0 |

### bmorphism (6 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 60 |
| shitcoin | HTML | 5 |
| flox-mcp-bb | Clojure | 0 |

---

## Event Summary (bmorphism — 12 events captured)

| Event Type | Count |
|------------|-------|
| PushEvent | 6 |
| IssuesEvent | 2 |
| PullRequestEvent | 2 |
| CreateEvent | 1 |
| WatchEvent | 1 |

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 12 |
| kubeflow | org | 9 |
| TeglonLabs | org | 5 |
| bmorphism | user | 6 |
| kristinezheng | user | 3 |
| M1shaaa | user | 3 |
| DJedamski | user | 2 |
| **TOTAL** | | **40** |

---

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/pipelines**: 4,112 stars — most popular ML pipeline for Kubernetes (pushed 2026-03-28)
- **kubeflow/spark-operator**: 3,110 stars — Kubernetes operator for Apache Spark
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect
- **plurigrid/asi**: 16 stars — topological chemputer! (pushed 2026-04-06)
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring

---

## 2026-04-06 Sweep Addition: Full Social Graph + Hamming Swarm

### GitHub Social Graph — Repos Captured This Sweep

| Org/User       | Total Repos (API) | Captured |
|----------------|-------------------|---------|
| plurigrid      | 95                | 10      |
| kubeflow       | N/A (auth err)    | —       |
| TeglonLabs     | 3                 | 3       |
| bmorphism      | N/A (auth err)    | —       |
| zubyul         | 44                | 10      |
| migalkin       | 19                | 6       |
| DJedamski      | 6                 | 5       |
| wasita         | 9                 | 4       |
| kristinezheng  | 6                 | 3       |
| M1shaaa        | 8                 | 3       |
| AustinCStone   | 40                | 3       |

### Top New Repos by Stars (2026-04-06 sweep)

| Repo                         | Stars | Language | Description                               |
|------------------------------|-------|----------|-------------------------------------------|
| migalkin/NodePiece            | 143   | Python   | Compositional representations for KGs     |
| AustinCStone/TextGAN          | 92    | Python   | GAN for text generation in TensorFlow     |
| migalkin/StarE                | 88    | Python   | Message Passing for Hyper-Relational KGs  |
| migalkin/kgcourse2021         | 25    | HTML     | Knowledge Graphs course materials         |
| plurigrid/asi                 | 16    | HTML     | everything is topological chemputer!      |
| plurigrid/asi-skills          | 3     | Julia    | 69 skills with Galois Hole Type           |
| plurigrid/zig-syrup           | 2     | Zig      | OCapN Syrup with CapTP optimizations      |
| TeglonLabs/mathpix-gem        | 2     | Ruby     | Mathematical images to LaTeX              |

### Aptos Hamming Swarm — Wallet Balances (2026-04-06)

All 28 addresses returned 0 APT (accounts exist but CoinStore not initialized on mainnet).

| World | Address (truncated)    | APT Balance |
|-------|------------------------|-------------|
| alice | 0xc793...4cc7b         | 0.0         |
| bob   | 0x0a3c...512d5d        | 0.0         |
| A–Z   | (26 addresses)         | 0.0 each    |

### Multisig Contract Probes (2026-04-06)

All 5 multisig contracts are healthy with `sigs_required = 2`.

| Pair  | Contract Address (truncated) | Sigs Required | Healthy |
|-------|------------------------------|---------------|---------|
| A-B   | 0x0da4...7003                | 2             | YES     |
| A-G   | 0xf56c...0096                | 2             | YES     |
| Y-Z   | 0xd3ff...b883                | 2             | YES     |
| S-T   | 0x3b1c...7883                | 2             | YES     |
| V-W   | 0x40fa...eb6d                | 2             | YES     |

### MNX Markets Status (2026-04-06)

`https://testnet.mnx.fi/api/markets` — **UNAVAILABLE as JSON API**

Returns a Next.js SPA (HTML). No REST endpoint accessible. Status: SPA only.

### GF(3) Color Chain Stats (2026-04-06 sweep)

45 new `world_increments` rows added, cycling PLUS → MINUS → ERGODIC:

| GF3 Trit | Color Name | Hex     | Count |
|----------|------------|---------|-------|
| 0        | ERGODIC    | #d3869b | 15    |
| +1       | PLUS       | #b8bb26 | 15    |
| -1       | MINUS      | #cc241d | 15    |
