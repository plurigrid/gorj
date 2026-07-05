# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-05

## Sweep Metadata
- **Date:** 2026-07-05
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 404 |
| Total Repo Snapshots (this sweep) | 385 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (Vercel auth) |

---

## GF(3) Color Chain

Chain rule: `id mod 3 == 0` → ERGODIC (#d3869b, trit=0) | `id mod 3 == 1` → PLUS (#b8bb26, trit=1) | `id mod 3 == 2` → MINUS (#cc241d, trit=-1)

**This sweep distribution (balanced):**
- ERGODIC (#d3869b): 134
- PLUS (#b8bb26): 135
- MINUS (#cc241d): 135

---

## Top Repos by Stars (this sweep)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,762 | — | 2026-06-18 |
| kubeflow/pipelines | 4,169 | Python | 2026-07-05 |
| kubeflow/spark-operator | 3,132 | Python | 2026-07-02 |
| kubeflow/trainer | 2,129 | Go | 2026-07-03 |
| kubeflow/katib | 1,689 | Python | 2026-07-01 |
| kubeflow/arena | 815 | Go | 2026-07-03 |
| kubeflow/community-distribution | 1,028 | YAML | 2026-07-05 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| plurigrid/asi | 28 | HTML | 2026-06-29 |
| plurigrid/gorj | 0 | Clojure | 2026-07-05 |

---

## GitHub Social Graph — Source Breakdown

| Source | Type | Repos | Most Recent Push |
|--------|------|-------|-----------------|
| plurigrid | org | 100 | 2026-07-05 (gorj) |
| bmorphism | user | 100 | 2026-07-05 (Gay.jl) |
| kubeflow | org | 48 | 2026-07-05 (community-distribution) |
| zubyul | user | 49 | 2026-04-24 |
| AustinCStone | user | 32 | — |
| migalkin | user | 21 | — |
| wasita | user | 13 | 2026-07-05 (wasita.github.io) |
| M1shaaa | user | 10 | 2026-07-05 (M1shaaa profile) |
| TeglonLabs | org | 5 | 2026-06-08 (jank-crane) |
| DJedamski | user | 6 | 2018-03-07 |
| kristinezheng | user | 7 | 2026-07-01 |

### Notable Recent Activity

**plurigrid:**
- `gorj` — pushed 2026-07-05, 987 open issues, Rama topology nREPL + GF(3) coloring
- `eirobri` — pushed 2026-06-30, EiRoBri replay world (Clojure)
- `place` — pushed 2026-06-29, TeX

**bmorphism:**
- `Gay.jl` — pushed 2026-07-05, wide-gamut color sampling, SPI, 187 open issues
- `satreadout` — pushed 2026-06-20, machine-checked perceptual readout

**kubeflow:**
- `community-distribution` — pushed 2026-07-05 (latest)
- `dashboard` — pushed 2026-07-05, 84 open issues
- `pipelines` — pushed 2026-07-05, 413 open issues

**zubyul social graph:**
- `wasita/wasita.github.io` — pushed 2026-07-05 (Svelte personal site)
- `M1shaaa/M1shaaa` — pushed 2026-07-05 (profile config)
- `kristinezheng/kristinezheng.github.io` — pushed 2026-07-01

**TeglonLabs:**
- `jank-crane` — pushed 2026-06-08, crane-jank converged-IR hub, GF3 convergence maps, C++

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances — 28 Addresses

All 28 Hamming swarm addresses queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. All return **0.0 APT** — CoinStore resources not initialized or zero balance.

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z (26 addrs) | 0x8699...→0x7af0... | 0.0 each |

### Multisig Contract Probes — 5/5 Healthy ✓

All 5 contracts use `0x1::multisig_account::num_signatures_required` and return **2** — all 2-of-2 multisigs are live and responsive.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | healthy |
| A-G | 0xf56c...0096 | 2 | healthy |
| Y-Z | 0xd3ff...b883 | 2 | healthy |
| S-T | 0x3b1c...7883 | 2 | healthy |
| V-W | 0x40fa...eb6d | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Vercel deployment protection blocks unauthenticated access. API paths `/api/markets` and `/api/v1/markets` both return 200 with authentication-required HTML (not JSON). `mnx_snapshots` table is empty this sweep.

---

## DuckDB Schema

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

*Next sweep will diff stars/forks/open_issues deltas against this baseline.*
