# World-Increment Sweep + Hamming Snapshot — 2026-05-10

## Sweep Metadata
- **Date:** 2026-05-10
- **Sweep ID:** 13
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **GF(3):** trit=+1 · color=#b8bb26 · name=PLUS
- **DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Status
GitHub public API rate limit exceeded (unauthenticated IP 34.121.238.53 — 60 req/hr shared pool).  
Live repo data captured via GitHub MCP tools for `plurigrid/gorj`.  
Previous sweep data (id=1–12) covers 471 repos across 3 orgs + 8 users and remains valid.

### plurigrid/gorj (MCP — live 2026-05-10)
- **Language:** Clojure  
- **Description:** MCP server + hooks that give AI coding agents a Clojure REPL  
- **Last master push:** 2026-05-08T14:04:34Z (`chore: ignore duckdb binary`)  
- **Total branches:** 107 (106 world-increment/sweep-* + master)  
- **Latest sweep branch:** `world-increment/sweep-2026-05-07-0816`

### Branch Cadence (plurigrid/gorj since 2026-04-27)
| Date | Sweep Branches |
|---|---|
| 2026-04-27 | 4 |
| 2026-04-28 | 8 |
| 2026-04-29 | 7 |
| 2026-04-30 | 9 |
| 2026-05-01 | 7 |
| 2026-05-02 | 12 |
| 2026-05-03 | 5 |
| 2026-05-04 | 6 |
| 2026-05-05 | 14 |
| 2026-05-06 | 13 |
| 2026-05-07 | 3 (latest) |
| **Total** | **88** sweep branches |

### Rate-limited sources (previous sweep data still valid)
| Source | Type | Repos (last sweep) |
|---|---|---|
| plurigrid | org | 100 |
| kubeflow | org | 47 |
| TeglonLabs | org | 53 |
| bmorphism | user | 100 |
| zubyul | user | 24 |
| migalkin | user | 30 |
| DJedamski | user | 11 |
| wasita | user | 29 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| AustinCStone | user | 43 |
| **TOTAL** | | **471** |

### DuckDB State Post-Sweep
| Table | Rows |
|---|---|
| world_increments | 34 |
| repo_snapshots | 945 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (2026-05-10 08:20 UTC)

Queried via `fullnode.mainnet.aptoslabs.com` with 1s sleep between calls.  
All 28 wallets returned **0 APT** — addresses are unregistered or unfunded on Aptos mainnet.

| World | Address | APT Balance |
|---|---|---|
| alice | 0xc793...cc7b | 0.00000000 |
| bob | 0x0a3c...2d5d | 0.00000000 |
| A | 0x8699...9d7a | 0.00000000 |
| B | 0x3f89...b13 | 0.00000000 |
| C | 0x38b9...535e | 0.00000000 |
| D | 0xf776...fdd1 | 0.00000000 |
| E | 0xdc1d...8d36 | 0.00000000 |
| F | 0x18a1...f71 | 0.00000000 |
| G | 0x69a3...f32 | 0.00000000 |
| H | 0xce67...300f | 0.00000000 |
| I | 0x070f...c9 | 0.00000000 |
| J | 0x4d96...7f54 | 0.00000000 |
| K | 0xa732...dc4 | 0.00000000 |
| L | 0x7c2e...ba9 | 0.00000000 |
| M | 0x6fed...2e9 | 0.00000000 |
| N | 0xe7dd...1b2c | 0.00000000 |
| O | 0x7325...89d | 0.00000000 |
| P | 0x6218...948 | 0.00000000 |
| Q | 0xac40...89a9 | 0.00000000 |
| R | 0x7ce6...6e10 | 0.00000000 |
| S | 0xb875...386 | 0.00000000 |
| T | 0x3578...588 | 0.00000000 |
| U | 0x7586...956 | 0.00000000 |
| V | 0xb59d...2c3 | 0.00000000 |
| W | 0x5f32...b0 | 0.00000000 |
| X | 0xa95c...47d | 0.00000000 |
| Y | 0xd8e3...44c4 | 0.00000000 |
| Z | 0x7af0...97c | 0.00000000 |

**Total APT across full swarm (alice+bob+A–Z):** 0.00000000

### Multisig Contract Probes — 5/5 HEALTHY

All 5 probed multisig accounts report `num_signatures_required = 2` (2-of-N threshold).

| Pair | Address | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4...003 | 2 | YES |
| A-G | 0xf56c...096 | 2 | YES |
| Y-Z | 0xd3ff...883 | 2 | YES |
| S-T | 0x3b1c...883 | 2 | YES |
| V-W | 0x40fa...b6d | 2 | YES |

**Multisig health:** 5/5 (100%) — all require 2-of-N signatures, uniformly configured.

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — `testnet.mnx.fi` is a Next.js SPA (server-side rendered HTML).  
Probed: `/api/markets`, `/api/v1/markets` — both return HTML shell, no JSON.  
Market data requires authenticated WebSocket or browser-side hydration.  
DuckDB row inserted with `category='unavailable'`, `price=NULL`.

---

## GF(3) Color Chain — All Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|---|---|---|---|---|---|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | PLUS |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | MINUS |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | ERGODIC |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | PLUS |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | MINUS |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | ERGODIC |
| 7  | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | PLUS |
| 8  | wasita (user) | repo_snapshot | -1 | `#cc241d` | MINUS |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | ERGODIC |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | PLUS |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | MINUS |
| 12 | bmorphism (org) | sweep_complete | 0 | `#d3869b` | ERGODIC |
| **13** | **plurigrid/gorj** | **sweep_complete** | **+1** | **`#b8bb26`** | **PLUS** ← this run |

Next: id=14 → trit=-1 → MINUS (#cc241d)

---

## Schema Reference
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

## Notable Highlights (from previous sweeps, still valid)
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — most popular Kubernetes ML pipeline
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for MCP using oxcaml_effect
- **migalkin/NodePiece**: 143 stars — scalable KG embeddings
- **plurigrid/asi**: 16 stars — topological chemputer
- **gorj**: 107 branches, 88 sweep branches since 2026-04-27 — continuous world-increment cadence confirmed
