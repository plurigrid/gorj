# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-10

## Sweep Metadata
- **Date:** 2026-04-10
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (all-time) | 864 |
| Total Repo Snapshots (all-time) | 940 |
| New Repo Records This Run | 331 |
| New Event Records This Run | 30 |
| Sources Covered | 3 orgs + 6 users (4 rate-limited) |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 (all healthy) |
| MNX Markets | UNAVAILABLE (SPA, no REST API) |

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
- **kubeflow/pipelines**: 4,119 stars — most popular ML pipeline for Kubernetes
- **kubeflow/spark-operator**: 3,111 stars — Kubernetes operator for Apache Spark
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) trit coloring

---

## JOB 2: Hamming Swarm Snapshot (2026-04-10)

### GitHub Social Graph — This Run

| Source | Type | Records | Status |
|--------|------|---------|--------|
| plurigrid | org | 100 repos | ✓ |
| kubeflow | org | 47 repos | ✓ |
| TeglonLabs | org | 53 repos | ✓ |
| zubyul | user | 24 repos | ✓ |
| AustinCStone | user | 43 repos | ✓ |
| M1shaaa | user | 16 repos | ✓ |
| kristinezheng | user | 18 repos | ✓ |
| migalkin | user | 30 repos | ✓ |
| bmorphism events | events | 30 events | ✓ |
| bmorphism repos | user | — | ✗ rate-limited |
| DJedamski | user | — | ✗ rate-limited |
| wasita | user | — | ✗ rate-limited |
| zubyul events | events | — | ✗ rate-limited |

### Aptos Mainnet — Hamming Swarm Balances

Queried `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` for 28 addresses.
All returned `resource_not_found` — accounts not initialized or zero APT balance.

| World | Balance (APT) |
|-------|--------------|
| alice, bob, A–Z (28 total) | 0.0 each |

### Multisig Contract Probes

`0x1::multisig_account::num_signatures_required` — all 5 contracts live and responding.

| Pair | Sigs Required | Healthy |
|------|--------------|---------|
| A-B (0x0da4...7003) | 2 | ✓ |
| A-G (0xf56c...0096) | 2 | ✓ |
| Y-Z (0xd3ff...b883) | 2 | ✓ |
| S-T (0x3b1c...7883) | 2 | ✓ |
| V-W (0x40fa...eb6d) | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `/api/markets` returns HTTP 404. Site is a Next.js SPA with client-side rendering only. No market data extractable via direct HTTP. `mnx_snapshots` table has 0 rows this run.

### DuckDB State After This Run

```
world_increments : 864 rows  (GF3-colored event log, all-time)
repo_snapshots   : 940 rows  (org/user repo metadata, all-time)
aptos_snapshots  :  28 rows  (Hamming swarm A–Z + alice + bob)
multisig_probes  :   5 rows  (all healthy, 2-sig threshold)
mnx_snapshots    :   0 rows  (unavailable)
```

### GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

*Generated by world-increment-sweep + hamming-swarm-snapshot agent — 2026-04-10*
