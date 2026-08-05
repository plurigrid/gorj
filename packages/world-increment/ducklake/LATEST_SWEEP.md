# World-Increment Sweep — 2026-08-05

## Sweep Metadata
- **Date:** 2026-08-05
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted (2026-08-05)

| Source | Type | Repos Collected |
|--------|------|----------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 50 (top-50 by update) |
| zubyul | user | 49 |
| migalkin | user (social graph) | 19 |
| wasita | user (social graph) | 14 |
| kristinezheng | user (social graph) | 5 |
| AustinCStone | user (social graph) | 41 |
| DJedamski | user (social graph) | 6 |
| M1shaaa | user (social graph) | 8 |
| **TOTAL this sweep** | | **175** |

Cumulative DB total: **1,119 repo_snapshots**, **34 world_increments**

### Top Repos by Stars (this sweep)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,805 | — | 2026-08-04 |
| kubeflow/pipelines | 4,177 | Python | 2026-08-05 |
| kubeflow/spark-operator | 3,143 | Python | 2026-08-05 |
| kubeflow/trainer | 2,170 | Go | 2026-08-05 |
| kubeflow/katib | 1,694 | Python | 2026-08-01 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-05-08 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-08-02 |

### GF(3) Color Chain (world_increments)

34 total world increments accumulated. Assignment: `id mod 3`:
- `0` → trit=0, `#d3869b`, **ERGODIC**
- `1` → trit=1, `#b8bb26`, **PLUS**
- `2` → trit=-1, `#cc241d`, **MINUS**

### Notable Activity

- **plurigrid/gorj** (this repo) pushed **2026-08-05** — active
- **plurigrid/eirobri** pushed **2026-08-04** — Clojure
- **plurigrid/place** pushed **2026-08-02** — TeX
- **plurigrid/asi** stars grew to **58** (up from 16 in April)
- **wasita/xoxowasita-analysis** created **2026-08-04** — very fresh
- **wasita/joint-planning-lit** created **2026-08-04** — very fresh
- **kubeflow/hub**, **kubeflow/sdk**, **kubeflow/pipelines** — all pushed **2026-08-05**
- **bmorphism/Gay.jl** — 188 open issues, active dev
- **TeglonLabs/jank-crane** — new C++ repo, GF3 convergence maps

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-08-05T10:18 UTC)

APT queried via `0x1::coin::balance` view function. All 28 worlds active.

| World | Balance (APT) | GF3 Label |
|-------|--------------|----------|
| alice | 0.43643352 | ERGODIC |
| bob | **12.65700700** | PLUS |
| A | 0.05176700 | MINUS |
| B | 0.03625600 | ERGODIC |
| C | 0.01018500 | PLUS |
| D | 0.01162900 | MINUS |
| E | 0.00937200 | ERGODIC |
| F | **1.96051600** | PLUS |
| G | 0.00068100 | MINUS |
| H | 0.00168100 | ERGODIC |
| I | 0.00068100 | PLUS |
| J | **1.89509300** | MINUS |
| K | 0.16196100 | ERGODIC |
| L | **1.92726900** | PLUS |
| M | 0.11228500 | MINUS |
| N | 0.10612100 | ERGODIC |
| O | 0.21013600 | PLUS |
| P | 0.14013600 | MINUS |
| Q | 0.10324000 | ERGODIC |
| R | 0.09021700 | PLUS |
| S | 0.09178800 | MINUS |
| T | 0.07371300 | ERGODIC |
| U | 0.05577300 | PLUS |
| V | 0.04883299 | MINUS |
| W | 0.04070500 | ERGODIC |
| X | 0.04257700 | PLUS |
| Y | 0.04444900 | MINUS |
| Z | 0.02426800 | ERGODIC |

**Total swarm: 20.3448 APT across 28 worlds.**  
`bob` holds 62% (12.657 APT). Worlds F/J/L each ~1.9 APT.

### Multisig Contract Health

All 5 multisig pairs healthy.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|--------------|--------|
| A-B | 0x0da4f428... | 2 | ✓ healthy |
| A-G | 0xf56c4a1c... | 2 | ✓ healthy |
| Y-Z | 0xd3ffe181... | 2 | ✓ healthy |
| S-T | 0x3b1c3ae9... | 2 | ✓ healthy |
| V-W | 0x40fad7b4... | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi/api/markets` returns 404 (Next.js SPA, no REST API exposed). `mnx_snapshots` table empty this run.

---

## Database Summary

| Table | Rows (cumulative) |
|-------|------------------|
| world_increments | 34 |
| repo_snapshots | 1,119 |
| aptos_snapshots | 28+ (this run) |
| multisig_probes | 5+ (this run) |
| mnx_snapshots | 0 |

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

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
