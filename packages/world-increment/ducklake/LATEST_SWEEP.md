# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-20

## Sweep Metadata
- **Date:** 2026-06-20
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 386 |
| Total Repo Snapshots | 386 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts | 5 (all healthy, 2-of-2) |

---

## GF(3) Color Chain Distribution

| Color | Hex | Name | Count |
|-------|-----|------|------:|
| Pink | `#d3869b` | ERGODIC (trit=0) | 129 |
| Yellow-Green | `#b8bb26` | PLUS (trit=1) | 129 |
| Red | `#cc241d` | MINUS (trit=-1) | 128 |

GF(3) rule: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

---

## GitHub Repo Counts by Source

| Source | Type | Repos | Total Stars |
|--------|------|------:|------------:|
| plurigrid | org | 100 | 77 |
| bmorphism | user | 100 | 247 |
| kubeflow | org | 48 | 34,233 |
| zubyul | user | 49 | 14 |
| AustinCStone | user (social) | 40 | 108 |
| migalkin | user (social) | 19 | 280 |
| M1shaaa | user (social) | 8 | 0 |
| DJedamski | user (social) | 6 | 3 |
| wasita | user (social) | 6 | 4 |
| TeglonLabs | org | 5 | 2 |
| kristinezheng | user (social) | 5 | 0 |
| **TOTAL** | | **386** | **34,968** |

---

## Most Recently Pushed Repos (2026-06-20)
- `bmorphism/satreadout` (HTML) — 2026-06-20
- `bmorphism/bci-preview` (HTML) — 2026-06-20
- `bmorphism/Gay.jl` (Julia) — 2026-06-20
- `plurigrid/place` (TeX) — 2026-06-20
- `plurigrid/gorj` (Clojure) — 2026-06-20
- `wasita/proj-template` — 2026-06-19

## Top Star Repos (This Sweep)
| Repo | Language | Stars |
|------|----------|------:|
| kubeflow/pipelines | Python | 4,155 |
| kubeflow/trainer | Go | 2,118 |
| kubeflow/community-distribution | YAML | 1,025 |
| kubeflow/mcp-apache-spark-history-server | Python | 177 |
| migalkin/NodePiece | Python | 144 |
| migalkin/StarE | Python | 89 |
| AustinCStone/TextGAN | Python | 92 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 |
| plurigrid/asi | HTML | 26 |

## Notable New Repos (2026)
- `TeglonLabs/jank-crane` (C++) — crane-jank converged-IR hub with GF3 convergence maps
- `plurigrid/eirobri` (Clojure) — 2026-06-03
- `plurigrid/nash-portal` (Rust) — 2026-05-19
- `bmorphism/oxgame` (OCaml) — 2026-05-15
- `bmorphism/world` (Python) — 2026-06-02
- `wasita/vocoder` (JavaScript) — 2026-05-06

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (alice, bob, A–Z)
All 28 Hamming addresses were probed against `fullnode.mainnet.aptoslabs.com`.

**Result:** All 28 addresses return `resource_not_found` for `CoinStore<AptosCoin>`.  
Accounts have not initialized an APT coin store (wallets exist but hold no APT).

| World | Address | Balance (APT) |
|-------|---------|:-------------:|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Health
Probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|:------------:|:------:|
| A-B | 0x0da4...7003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✅ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✅ HEALTHY |

**All 5 multisig contracts are operational** (2-of-2 required).

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — Vercel deployment protection blocks all paths.  
`mnx_snapshots` table is empty this sweep.

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
