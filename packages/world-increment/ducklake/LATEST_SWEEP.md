# World-Increment Sweep + Hamming Snapshot — 2026-08-04

## Sweep Metadata
- **Date:** 2026-08-04
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social) | 19 |
| wasita | user (social) | 13 |
| DJedamski | user (social) | 6 |
| kristinezheng | user (social) | 5 |
| M1shaaa | user (social) | 8 |
| AustinCStone | user (social) | 30 |
| **TOTAL** | | **384** |

### GF(3) Color Chain

128 ERGODIC (#d3869b, trit=0) + 128 PLUS (#b8bb26, trit=+1) + 128 MINUS (#cc241d, trit=-1) across 384 repo events.

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,805 | — | 2026-07-10 |
| kubeflow/pipelines | 4,175 | Python | 2026-08-04 |
| kubeflow/spark-operator | 3,143 | Python | 2026-08-03 |
| kubeflow/trainer | 2,167 | Go | 2026-08-04 |
| kubeflow/katib | 1,694 | Python | 2026-08-04 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| plurigrid/asi | 58 | HTML | 2026-07-10 |

### Notable Recent Activity (2026-08-04)
- **wasita/joint-planning-lit** — created TODAY (joint planning literature)
- **M1shaaa/M1shaaa** — pushed TODAY (profile config)
- **bmorphism/Gay.jl** — pushed TODAY, 188 open issues, Julia wide-gamut GF(3) color sampling
- **kubeflow/mcp-server** — MCP for Kubeflow AI-assisted development, very active
- **plurigrid/gorj** — this repo, 1622 open issues, Clojure/forj

### Language Distribution

| Language | Repos |
|----------|-------|
| Python | 77 |
| Rust | 26 |
| JavaScript | 24 |
| TypeScript | 22 |
| HTML | 18 |
| Go | 15 |
| Clojure | 14 |
| Jupyter Notebook | 14 |
| Julia | 9 |
| Zig | 7 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Alice–Z, 28 addresses)

**Status: NETWORK BLOCKED** — Aptos mainnet API (`fullnode.mainnet.aptoslabs.com`) is not reachable from this execution environment. All 28 addresses recorded with `balance_apt = NULL` in `aptos_snapshots`.

### Multisig Contract Probes (5/5 SUCCESS)

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...7003 | **2** | ✓ |
| A-G | 0xf56c4a1c...0096 | **2** | ✓ |
| Y-Z | 0xd3ffe181...b883 | **2** | ✓ |
| S-T | 0x3b1c3ae9...7883 | **2** | ✓ |
| V-W | 0x40fad7b4...eb6d | **2** | ✓ |

All 5 multisig contracts healthy, all requiring 2-of-N signatures.

### MNX Markets

**Status: UNAVAILABLE** — `https://testnet.mnx.fi/api/markets` returns HTTP 404. Main site renders as SPA with no market data visible. `mnx_snapshots` table is empty.

---

## DuckDB Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)
-- 384 rows

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)
-- 384 rows

aptos_snapshots(timestamp, world, address, balance_apt)
-- 28 rows, balance_apt all NULL (network blocked)

multisig_probes(timestamp, pair, address, sigs_required, healthy)
-- 5 rows, all healthy, all sigs_required=2

mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
-- 0 rows (unavailable)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
