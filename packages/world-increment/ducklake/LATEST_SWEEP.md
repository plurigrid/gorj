# World-Increment Sweep + Hamming Snapshot — 2026-07-27

## Sweep Metadata
- **Date:** 2026-07-27
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (2026-07-27 Run)

| Metric | Value |
|--------|-------|
| New Repo Snapshots | 154 |
| Cumulative DB Rows | 1098 |
| Sources Covered | 3 orgs + 7 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts | 5 (all healthy) |
| MNX Markets | SPA-only, no API |

---

## JOB 1: GitHub Social Graph

### Sources & Repo Counts (this run)
| Source | Type | Fetched | Total Available |
|--------|------|---------|----------------|
| plurigrid | org | 50 | 103 |
| kubeflow | org | 30 | 49 |
| TeglonLabs | org | 5 | 5 |
| bmorphism | user | 30 | 106 |
| zubyul | user | 30 | 49 |
| migalkin | social-graph | 3 | 19 |
| wasita | social-graph | 2 | — |
| AustinCStone | social-graph | 2 | — |
| kristinezheng | social-graph | 1 | — |
| M1shaaa | social-graph | 1 | — |
| **TOTAL** | | **154** | |

### Top Repos by Stars (this snapshot)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| kubeflow/pipelines | Python | 4169 | 2026-07-26 |
| kubeflow/spark-operator | Python | 3142 | 2026-07-25 |
| kubeflow/trainer | Go | 2154 | 2026-07-26 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| plurigrid/asi | HTML | 48 | 2026-07-10 |
| migalkin/kgcourse2021 | HTML | 24 | 2026-07-10 |

### Recent Activity Highlights
- **plurigrid/gorj** — pushed **today** (2026-07-27), 1428 open issues
- **plurigrid/eirobri** — pushed 2026-07-21 (EiRoBri replay world, Clojure)
- **bmorphism/Gay.jl** — pushed 2026-07-26 (Julia)
- **wasita/wasita.github.io** — pushed 2026-07-21 (Svelte)
- **zubyul/from-possible-worlds** — pushed 2026-07-18 (TeX)
- **AustinCStone/byteruckus** — pushed 2026-07-15 (HTML, new)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-07-27)
> Method: `0x1::coin::balance<AptosCoin>` view function (FA-compatible, handles both legacy coin and fungible asset accounts)

| World | APT Balance | Notes |
|-------|-------------|-------|
| alice | 0.43643352 | |
| bob | **12.65700700** | top holder |
| A | 0.05176700 | |
| B | 0.03625600 | |
| C | 0.01018500 | |
| D | 0.01162900 | |
| E | 0.00937200 | |
| F | **1.96051600** | |
| G | 0.00068100 | |
| H | 0.00168100 | |
| I | 0.00068100 | |
| J | **1.89509300** | |
| K | 0.16196100 | |
| L | **1.92726900** | |
| M | 0.11228500 | |
| N | 0.10612100 | |
| O | 0.21013600 | |
| P | 0.14013600 | |
| Q | 0.10324000 | |
| R | 0.09021700 | |
| S | 0.09178800 | |
| T | 0.07371300 | |
| U | 0.05577300 | |
| V | 0.04883299 | |
| W | 0.04070500 | |
| X | 0.04257700 | |
| Y | 0.04444900 | |
| Z | 0.02426800 | |

**Total swarm APT:** ~20.71 APT  
**Top holders:** bob (12.66), F (1.96), L (1.93), J (1.90)  
**All 28 accounts:** active on mainnet (seq_num > 0)

### Multisig Contract Probes
All 5 multisig contracts responded with `sigs_required=2` — all healthy.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|--------------|--------|
| A-B | 0x0da4... | 2 | healthy |
| A-G | 0xf56c... | 2 | healthy |
| Y-Z | 0xd3ff... | 2 | healthy |
| S-T | 0x3b1c... | 2 | healthy |
| V-W | 0x40fa... | 2 | healthy |

### MNX Markets (testnet.mnx.fi)
- **Status:** SPA frontend — no REST API endpoints accessible
- `/api/markets` and `/api/v1/markets` both return non-JSON (HTML SPA shell)
- No market data extractable this run; `mnx_snapshots` table is empty

---

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
