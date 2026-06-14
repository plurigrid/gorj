# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-14

## Sweep Metadata
- **Date:** 2026-06-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 2: Hamming Swarm Snapshot (NEW)

### Aptos Mainnet Wallet Balances (28 addresses, ledger ~5,727,025,320)

**Status:** All 28 addresses return `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
CoinStore not initialized on any of these accounts — balance NULL for all wallets (alice, bob, A–Z).

### Multisig Contract Probes — All Healthy ✓

| Pair | Address | Sigs Required |
|------|---------|---------------|
| A-B | 0x0da4f428...987003 | 2 |
| A-G | 0xf56c4a1c...0096 | 2 |
| Y-Z | 0xd3ffe181...b883 | 2 |
| S-T | 0x3b1c3ae9...7883 | 2 |
| V-W | 0x40fad7b4...eb6d | 2 |

All 5 multisig accounts require exactly 2-of-N signatures and are responsive on mainnet.

### MNX Markets (testnet.mnx.fi)

**Status:** Vercel authentication wall — all API paths blocked without bypass token. Data unavailable.

---

## JOB 1: GitHub Social Graph Sweep (2026-06-14)

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 391 |
| Total Repo Snapshots | 391 |
| Sources Covered | 3 orgs + 8 users (11 total) |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 (all healthy, 2-of-N) |
| MNX Markets | unavailable (Vercel auth) |

---

## GF(3) Color Chain — 391 Increments

Increments are assigned cyclically: PLUS (#b8bb26) → MINUS (#cc241d) → ERGODIC (#d3869b).

| GF3 Name | Color | Count |
|----------|-------|-------|
| PLUS | #b8bb26 | 131 |
| MINUS | #cc241d | 130 |
| ERGODIC | #d3869b | 130 |

Full 130 complete GF(3) cycles + 1 partial (final: PLUS).

---

## Top Repos by Source (2026-06-14)

### kubeflow (48 repos, 34,204 ★)
| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow | — | 15,720 | 2026-06-11 |
| pipelines | Python | 4,153 | 2026-06-13 |
| spark-operator | Python | 3,127 | 2026-06-12 |
| trainer | Go | 2,114 | 2026-06-13 |
| katib | Python | 1,683 | 2026-06-12 |

### bmorphism (100 repos, 247 ★)
Active in: Clojure, Rust, OCaml, Haskell, Move, Zig, TypeScript, Julia, Svelte

### plurigrid (100 repos, 77 ★)
Active in: Clojure, Hy, Zig, Rust, Scheme, Racket, Swift, Julia

### zubyul (49 repos, 14 ★)
Active in: Haskell, Zig, Rust, Clojure, Julia, Move, Svelte, Emacs Lisp

### migalkin (19 repos, 280 ★)
Active in: Python (KG embeddings), Rust, Java, R, Web Ontology Language

### AustinCStone (40 repos, 108 ★)
Active in: Python, C++, Haskell, C, MATLAB

### TeglonLabs (5 repos, 2 ★)
- **jank-crane**: C++ — converged-IR hub, GF3 convergence maps (pushed 2026-06-08)
- **mathpix-gem**: Ruby — mathematical OCR gem

### wasita (11 repos, 5 ★)
Active: wasita.github.io (Svelte, pushed 2026-06-01), wm-cv, vocoder

### Social graph (DJedamski, kristinezheng, M1shaaa)
Smaller personal repos; cognitive science / ML / Lookit studies focus.

---

## Repo Counts by Source (2026-06-14)

| Source | Type | Repos | Stars |
|--------|------|-------|-------|
| bmorphism | user | 100 | 247 |
| plurigrid | org | 100 | 77 |
| zubyul | user | 49 | 14 |
| kubeflow | org | 48 | 34,204 |
| AustinCStone | user | 40 | 108 |
| migalkin | user | 19 | 280 |
| wasita | user | 11 | 5 |
| M1shaaa | user | 8 | 0 |
| DJedamski | user | 6 | 3 |
| TeglonLabs | org | 5 | 2 |
| kristinezheng | user | 5 | 0 |
| **TOTAL** | | **391** | **34,940** |

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

## Notable Highlights (2026-06-14 vs 2026-04-12)

- **kubeflow/kubeflow**: 15,720 stars (+155 since April) — still the top repo
- **kubeflow/pipelines**: 4,153 stars (+34) — pushed 2026-06-13
- **kubeflow/spark-operator**: 3,127 stars (+16) — pushed 2026-06-12
- **TeglonLabs/jank-crane** (NEW): C++ — GF3 convergence maps + simonw workflow, created 2026-06-08
- **M1shaaa/M1shaaa**: profile repo pushed 2026-06-14 (today!) — active
- **wasita/wasita.github.io**: Svelte personal site pushed 2026-06-01
- **All 5 multisig contracts**: healthy, 2-of-N threshold, live on Aptos mainnet
- **Hamming swarm wallets**: 28 addresses probed — CoinStore not initialized (expected for fresh accounts)
- **Increment 391**: PLUS — closes this sweep's final GF(3) step
