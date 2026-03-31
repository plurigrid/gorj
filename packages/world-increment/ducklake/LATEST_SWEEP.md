# World-Increment Sweep — 2026-03-31 (Full Social Graph + Hamming Swarm)

## Sweep Metadata
- **Date:** 2026-03-31
- **Agent:** world-increment-sweep (full social graph + hamming swarm)
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 841 |
| Total Repo Snapshots | 1096 |
| Sources Covered | 3 orgs + 8 users |
| Events Captured | 60 (bmorphism + zubyul, 30 each) |
| Aptos Wallets Snapshotted | 28 |
| Multisig Contracts Probed | 5 |

---

## GitHub Sources Swept

| Source | Type | Repos |
|--------|------|-------|
| bmorphism | user | 100 |
| plurigrid | org | 100 |
| kubeflow | org | 46 |
| TeglonLabs | org | 53 |
| migalkin | user | 30 |
| AustinCStone | user | 43 |
| wasita | user | 28 |
| zubyul | user | 23 |
| kristinezheng | user | 18 |
| DJedamski | user | 11 |
| M1shaaa | user | 16 |
| **Total** | | **468** |

---

## Aptos Wallet Balances (Mainnet, Hamming Swarm)

Balances fetched via `0x1::coin::balance` view function. Total APT: ~19.84

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| bob | 0x0a3c...2d5d | 12.65700700 |
| F | 0x18a1...f71 | 1.96051600 |
| L | 0x7c2e...ba9 | 1.92726900 |
| J | 0x4d96...f54 | 1.89509300 |
| alice | 0xc793...c7b | 0.43643352 |
| O | 0x7325...89d | 0.21013600 |
| K | 0xa732...dc4 | 0.16196100 |
| P | 0x6218...948 | 0.14013600 |
| M | 0x6fed...e9 | 0.11228500 |
| N | 0xe7dd...b2c | 0.10612100 |
| Q | 0xac40...a9 | 0.10324000 |
| S | 0xb875...386 | 0.09178800 |
| R | 0x7ce6...e10 | 0.09021700 |
| T | 0x3578...588 | 0.07371300 |
| U | 0x7586...956 | 0.05577300 |
| A | 0x8699...d7a | 0.05176700 |
| V | 0xb59d...b3 | 0.04783299 |
| Y | 0xd8e3...c4 | 0.04444900 |
| X | 0xa95c...47d | 0.04257700 |
| W | 0x5f32...b0 | 0.04070500 |
| B | 0x3f89...b13 | 0.03625600 |
| Z | 0x7af0...97c | 0.02326800 |
| E | 0xdc1d...d36 | 0.01256100 |
| D | 0xf776...dd1 | 0.01162900 |
| C | 0x38b9...35e | 0.01018500 |
| G | 0x69a3...f32 | 0.00068100 |
| H | 0xce67...00f | 0.00068100 |
| I | 0x070f...c9 | 0.00068100 |

---

## Multisig Contract Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`. All healthy.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | YES |
| A-G | 0xf56c...096 | 2 | YES |
| Y-Z | 0xd3ff...883 | 2 | YES |
| S-T | 0x3b1c...883 | 2 | YES |
| V-W | 0x40fa...b6d | 2 | YES |

---

## MNX Markets

Status: **UNAVAILABLE** - `https://testnet.mnx.fi/api/markets` and `/api/v1/markets` both return HTML (no JSON API at time of sweep).

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

## Repo Counts by Source (Full Sweep)

| Source | Type | Repos |
|--------|------|-------|
| bmorphism | user | 100 |
| plurigrid | org | 100 |
| kubeflow | org | 46 |
| TeglonLabs | org | 53 |
| migalkin | user | 30 |
| AustinCStone | user | 43 |
| wasita | user | 28 |
| zubyul | user | 23 |
| kristinezheng | user | 18 |
| DJedamski | user | 11 |
| M1shaaa | user | 16 |
| **TOTAL** | | **468** |

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
