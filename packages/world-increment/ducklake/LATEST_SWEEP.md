# World-Increment Sweep + Hamming Snapshot

**Date/Time:** 2026-04-02T06:30:00Z

---

## JOB 1: GitHub Social Graph Sweep

### Repos Found (count per org/user)

| Org/User | Repos Fetched | Total Stars |
|---|---|---|
| kubeflow | 46 | 67,603 |
| migalkin | 40 | 385 |
| bmorphism | 97 | 377 |
| zubyul | 19 | 290 |
| AustinCStone | 30 | 216 |
| plurigrid | 93 | 96 |
| TeglonLabs | 3 | 8 |
| DJedamski | 6 | 10 |
| wasita | 9 | 5 |
| kristinezheng | 6 | 0 |
| M1shaaa | 8 | 0 |
| **TOTAL** | **357** | **68,990** |

Total repo_snapshots in DB: 801 (includes paginated results from large orgs)
Total world_increments: 343

### Top Repos by Stars

| Repo | Stars | Language |
|---|---|---|
| kubeflow/kubeflow | 15,548 | - |
| kubeflow/pipelines | 4,118 | Python |
| kubeflow/spark-operator | 3,110 | Python |
| kubeflow/trainer | 2,070 | Go |
| kubeflow/katib | 1,674 | Python |
| kubeflow/examples | 1,459 | Jsonnet |
| kubeflow/manifests | 1,006 | YAML |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 88 | Python |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml |

### Notable Repos

- **bmorphism**: Heavy MCP server builder (babashka-mcp, say-mcp, manifold-mcp, penrose-mcp, nats-mcp). Also ocaml-mcp-sdk (60 stars), anti-bullshit-mcp-server.
- **plurigrid**: Focus on category theory, stochastic flows, OCapN Syrup (zig-syrup), asi-skills.
- **migalkin**: Knowledge graph researcher - NodePiece (143 stars), StarE (88 stars).
- **kubeflow**: ML platform on K8s, flagship repo has 15k+ stars.
- **TeglonLabs**: mathpix-gem (Ruby math OCR), coin-flip-mcp, topoi.

---

## GF(3) Color Chain Summary

The world_increments table encodes each repo snapshot using GF(3) arithmetic:

| GF3 Name | Color | Trit | Count |
|---|---|---|---|
| ERGODIC | #d3869b (rose) | 0 | 114 |
| PLUS | #b8bb26 (yellow-green) | +1 | 115 |
| MINUS | #cc241d (red) | -1 | 114 |

Chain cycles: id%3==0 -> ERGODIC, id%3==1 -> PLUS, id%3==2 -> MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 addresses returned 0.0 APT (accounts not found or zero balance on Aptos mainnet).

| World | Address (truncated) | Balance (APT) |
|---|---|---|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...cfdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...3cf71 | 0.0 |
| G | 0x69a3...c7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...d386 | 0.0 |
| T | 0x3578...f4588 | 0.0 |
| U | 0x7586...f9956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...444c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

### Multisig Contract Probes

All 5 multisig contracts are healthy (require 2 signatures each).

| Pair | Address (truncated) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

### MNX Markets

**Status: UNAVAILABLE** - `https://testnet.mnx.fi/api/markets` returned HTTP 404. Testnet endpoint appears to be down or the API path is not available at time of sweep.

---

## Database Summary

- File: `packages/world-increment/ducklake/world-increments.duckdb`
- Tables: `world_increments`, `repo_snapshots`, `aptos_snapshots`, `multisig_probes`, `mnx_snapshots`
- Total world_increments: 343
- Total repo_snapshots: 801
- Total aptos_snapshots: 28
- Total multisig_probes: 5
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

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
- **plurigrid/asi**: 13 stars — topological chemputer (pushed 2026-03-28)
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
