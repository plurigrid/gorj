# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-17

## Sweep Metadata
- **Date:** 2026-05-17
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 76 |
| Total Repo Snapshots | 63 |
| Total Aptos Wallets | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 2 orgs + 9 users |

---

## GF(3) Color Distribution (76 increments)

| Name | Color | Count |
|------|-------|-------|
| PLUS | `#b8bb26` | 26 |
| MINUS | `#cc241d` | 25 |
| ERGODIC | `#d3869b` | 25 |

GF(3) chain nearly balanced: PLUS=26, MINUS=25, ERGODIC=25 across 76 increments (63 repos + 13 bmorphism events).

---

## Top Repos by Source

### plurigrid (25 repos, ★47)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 23 | 2026-04-26 |
| ontology | JavaScript | 8 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-26 |
| zig-syrup | Zig | 2 | 2026-04-30 |
| nash-portal | Rust | 2 | 2026-04-26 |
| gorj | Clojure | 0 | 2026-05-17 |

### TeglonLabs (14 repos, ★6)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| vibespace | HTML | 2 |
| acp.el | — | 1 |
| mcp-terminal | — | 1 |

### migalkin (6 repos, ★134) — zubyul social graph
| Repo | Language | Stars |
|------|----------|-------|
| StarE | Python | 89 |
| kgcourse2021 | HTML | 25 |
| NBFNet_mlx | Python | 10 |
| RWL | Python | 7 |
| rambo | Rust | 3 |

### zubyul (11 repos, ★2)
| Repo | Language | Pushed At |
|------|----------|-----------|
| asi | Python | 2026-04-30 |
| voice-observatory | Python | 2026-04-24 |
| Gay.jl | Julia | 2026-03-28 |
| gay-world | Python | 2026-03-26 |

### M1shaaa (5 repos) — zubyul social graph
- M1shaaa/M1shaaa.github.io (TypeScript), portfolio-inner-site, OWLET, WebGazer

---

## Repo Counts by Source

| Source | Type | Repos | ★ Stars |
|--------|------|-------|---------|
| plurigrid | org | 25 | 47 |
| TeglonLabs | org | 14 | 6 |
| zubyul | user | 11 | 2 |
| migalkin | user (zubyul graph) | 6 | 134 |
| M1shaaa | user (zubyul graph) | 5 | 0 |
| DJedamski | user (zubyul graph) | 2 | 4 |
| kubeflow | org | 0 | rate-limited |
| bmorphism | user | 0 | no public repos |
| wasita/kristinezheng/AustinCStone | users | 0 | empty |
| **TOTAL** | | **63** | **193** |

---

## Notable bmorphism Recent Activity (13 events)
- `WatchEvent` astroautomata/SymbolicRegression.jl — 2026-05-17
- `PullRequestEvent` bmorphism/Gay.jl — 2026-05-16
- `CreateEvent` bmorphism/EntropyLoop (fork of QuantumVillage/EntropyLoop) — 2026-05-15
- `PushEvent` bmorphism/nash-portal × 2 — 2026-05-14/15
- `ForkEvent`+`PullRequestEvent` plurigrid/nash-portal — 2026-05-13
- `WatchEvent` AlgebraicJulia/CompTime.jl — 2026-05-16

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances — 28 addresses
All 28 wallets (alice, bob, A–Z) queried via Aptos mainnet fullnode.  
**Result:** All 28 returned 0.00000000 APT — accounts exist on-chain but hold no liquid APT in `0x1::coin::CoinStore<AptosCoin>` at sweep time.

| World | Address prefix | Balance |
|-------|---------------|---------|
| alice | 0xc793...cc7b | 0 APT |
| bob | 0x0a3c...12d5 | 0 APT |
| A–Z (26) | various | 0 APT each |

### Multisig Contract Probes — 5 contracts
All probed via `0x1::multisig_account::num_signatures_required`.  
**All 5 healthy: 2-of-N required.**

| Pair | Address prefix | Sigs Required | Status |
|------|----------------|--------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ healthy |
| A-G | 0xf56c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)
**Status: SPA — no JSON API accessible.**  
`testnet.mnx.fi` serves a Next.js SPA. Paths `/api/markets`, `/api/v1/markets`, `/markets` all return the HTML shell. `mnx_snapshots` table is empty.

---

## DuckDB Tables

```
world_increments  76 rows  (63 repo snapshots + 13 bmorphism events)
repo_snapshots    63 rows  (plurigrid/TeglonLabs/zubyul/migalkin/DJedamski/M1shaaa)
aptos_snapshots   28 rows  (alice, bob, A–Z — all 0 APT)
multisig_probes    5 rows  (A-B, A-G, Y-Z, S-T, V-W — all 2-of-N healthy)
mnx_snapshots      0 rows  (SPA, no JSON API)
```

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
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS

## Notable Highlights
- **migalkin/StarE**: 89 stars — EMNLP 2020 hyper-relational KG message passing (zubyul social graph)
- **plurigrid/asi**: 23 stars — topological chemputer, most starred plurigrid repo
- **bmorphism** active on Gay.jl (multiple PRs/pushes 2026-05-11–16), nash-portal fork, EntropyLoop (QuantumVillage fork)
- **M1shaaa** active today (2026-05-17) — profile repo updated
- **Hamming swarm**: all 28 wallets at 0 APT; 5/5 multisig contracts live with 2-of-N threshold
