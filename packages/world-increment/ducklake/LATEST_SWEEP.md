# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-26

## Sweep Metadata
- **Date:** 2026-07-26
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep (2026-07-26)

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 34 |
| Total Repo Snapshots (cumulative) | 1338 |
| Sources Covered (this sweep) | 3 orgs + 8 users = 11 |
| New Repos This Sweep | 394 |

### GF(3) Color Chain — This Sweep's Increments

| Source | Type | Repos | GF3 Trit | Color | Name |
|--------|------|-------|-----------|-------|------|
| plurigrid | org | 100 | +1 | `#b8bb26` | **PLUS** |
| bmorphism | user | 100 | -1 | `#cc241d` | **MINUS** |
| zubyul | user | 49 | 0 | `#d3869b` | **ERGODIC** |
| kubeflow | org | 49 | +1 | `#b8bb26` | **PLUS** |
| TeglonLabs | org | 5 | -1 | `#cc241d` | **MINUS** |
| migalkin | user | 19 | 0 | `#d3869b` | **ERGODIC** |
| DJedamski | user | 6 | +1 | `#b8bb26` | **PLUS** |
| wasita | user | 12 | -1 | `#cc241d` | **MINUS** |
| kristinezheng | user | 5 | 0 | `#d3869b` | **ERGODIC** |
| M1shaaa | user | 8 | +1 | `#b8bb26` | **PLUS** |
| AustinCStone | user | 41 | -1 | `#cc241d` | **MINUS** |

### Top Repos by Source (2026-07-26 Snapshot)

#### plurigrid (100 repos, ⭐177 total)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gorj | Clojure | 1 | **2026-07-26** ← today |
| asi | HTML | 45 | 2026-07-10 |
| eirobri | Clojure | 0 | 2026-07-21 |
| place | TeX | 1 | 2026-07-14 |

#### bmorphism (100 repos, ⭐508 total)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| Gay.jl | Julia | 2 | **2026-07-26** ← today |
| gay-chat | Scheme | 0 | 2026-07-14 |
| satreadout | HTML | 0 | 2026-06-20 |

#### kubeflow (49 repos, ⭐102,133 total)
| Repo | Language | Stars |
|------|----------|-------|
| kubeflow | — | 15,792 |
| pipelines | Python | 4,169 |
| trainer | Go | 2,154 |
| kale | Python | 697 |

#### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

#### Social Graph Highlights
- **wasita/wasita.github.io** (Svelte): pushed 2026-07-21
- **kristinezheng/kristinezheng.github.io** (HTML): pushed 2026-07-01
- **M1shaaa/M1shaaa** (profile): pushed **2026-07-26 13:12 UTC** ← today
- **migalkin**: 19 repos, knowledge graph research

---

## JOB 2: Hamming Swarm Snapshot (2026-07-26)

### Aptos Wallet Balances (alice, bob, A–Z — 28 addresses)

**Note:** All 28 accounts verified reachable on Aptos mainnet (e.g. alice: seq=72). CoinStore balances = 0 APT because these accounts use the **new Fungible Asset (FA) standard** — `0x1::coin::CoinStore` resource absent. Balances reside in `0x1::primary_fungible_store`.

| Category | Count | CoinStore APT |
|----------|-------|--------------|
| Named wallets (alice, bob) | 2 | 0.0 (FA migrated) |
| Hamming worlds A–Z | 26 | 0.0 each (FA migrated) |

### Multisig Contract Probes — 5/5 Healthy ✓

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ healthy |
| A-G | 0xf56c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

All 5 multisig contracts respond with 2-of-N signatures required.

### MNX Markets (testnet.mnx.fi)

**Status: SPA-only — no REST API.**  
`https://testnet.mnx.fi` serves a Next.js SPA with no parseable JSON market endpoint at `/api/markets` or `/api/v1/markets`. No data ingested. Table `mnx_snapshots` empty this run.

---

## Schema (unchanged)
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

## Notable Highlights (2026-07-26)
- **plurigrid/gorj + bmorphism/Gay.jl**: both pushed TODAY — active development
- **M1shaaa/M1shaaa**: profile updated today at 13:12 UTC
- **kubeflow/kubeflow**: 15,792 stars — up from 15,565 in April sweep (+227)
- **5/5 multisig contracts**: all healthy, 2-of-N
- **Aptos FA migration**: all 28 Hamming wallets on new standard, CoinStore not applicable
