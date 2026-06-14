# World-Increment Sweep + Hamming Snapshot

**Date:** 2026-06-14  
**GF(3) Color Chain:** id%3==0 → trit=0 ERGODIC #d3869b | id%3==1 → trit=1 PLUS #b8bb26 | id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 37 (of 101 total) |
| kubeflow | org | 30 (of 48 total) |
| TeglonLabs | org | 5 |
| bmorphism | user | 30 (of 104 total) |
| zubyul | user | 30 (of 49 total) |
| migalkin | user (social graph) | 5 |
| DJedamski | user (social graph) | 6 |
| wasita | user (social graph) | 3 |
| kristinezheng | user (social graph) | 5 |
| M1shaaa | user (social graph) | 8 |
| AustinCStone | user (social graph) | 3 |

**Total repo snapshots: 163**

### Notable Repos (by stars/activity)

| Repo | Stars | Forks | Issues | Language | Last Push |
|------|-------|-------|--------|----------|-----------|
| kubeflow/kubeflow | 15720 | 2673 | 3 | — | 2026-06-11 |
| kubeflow/pipelines | 4153 | 2007 | 479 | Python | 2026-06-13 |
| kubeflow/spark-operator | 3127 | 1490 | 102 | Python | 2026-06-12 |
| kubeflow/trainer | 2114 | 969 | 113 | Go | 2026-06-13 |
| kubeflow/katib | 1683 | 527 | 116 | Python | 2026-06-12 |
| plurigrid/gorj | 0 | 0 | **568** | Clojure | 2026-06-14 |
| plurigrid/asi | 26 | 8 | 4 | HTML | 2026-06-10 |
| bmorphism/Gay.jl | 1 | 1 | **189** | Julia | 2026-06-14 |
| bmorphism/ocaml-mcp-sdk | 61 | 2 | 0 | OCaml | 2026-03-16 |
| migalkin/StarE | 89 | 16 | 1 | Python | 2023-12-01 |
| plurigrid/vcg-auction | 7 | 2 | 1 | Rust | 2023-03-16 |

### Hot Activity (pushed today 2026-06-14)

- `plurigrid/gorj` — GF(3) gay trit coloring for compositional open game REPL orchestration (568 open issues!)
- `bmorphism/Gay.jl` — Wide-gamut color sampling with splittable determinism (189 open issues)
- `M1shaaa/M1shaaa` — GitHub profile config (pushed 2026-06-14T03:40)

### DuckDB Tables

```sql
-- world_increments: 163 rows (GF3 trit-colored event stream)
-- repo_snapshots: 163 rows (org_or_user, repo_name, full_name, language, stars, forks, open_issues, pushed_at)
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 addresses (alice, bob, A-Z) returned **0.0 APT** on mainnet. No active coin stores found — addresses may be unused or APT held in non-standard resources.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A-Z | 0x8699...–0x7af0... | 0.0 each |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **healthy** — each requires 2 signatures.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | YES |
| A-G | 0xf56c...096 | 2 | YES |
| Y-Z | 0xd3ff...883 | 2 | YES |
| S-T | 0x3b1c...883 | 2 | YES |
| V-W | 0x40fa...b6d | 2 | YES |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Protected by Vercel Authentication (HTTP 401, visitor password required). No market data extracted.

### DuckDB Tables

```sql
-- aptos_snapshots: 28 rows (all balances 0.0 APT)
-- multisig_probes: 5 rows (all healthy, 2 sigs required)
-- mnx_snapshots: 0 rows (auth-gated, unavailable)
-- sweep_metadata: mnx_status=auth_required_vercel_gated
```

---

## Database Location

```
packages/world-increment/ducklake/world-increments.duckdb
```

Tables: `world_increments`, `repo_snapshots`, `aptos_snapshots`, `multisig_probes`, `mnx_snapshots`, `sweep_metadata`
