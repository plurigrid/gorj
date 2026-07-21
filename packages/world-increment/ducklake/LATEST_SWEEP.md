# World-Increment Sweep + Hamming Snapshot — 2026-07-21

## Sweep Metadata
- **Date:** 2026-07-21
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Python duckdb)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 406 |
| Total Repo Snapshots (cumulative) | 1327 |
| New Repos This Sweep | 383 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (SPA only) |

---

## GF(3) Color Chain (this sweep: increments 24–406)
- `id % 3 == 0` → trit=0, ERGODIC, `#d3869b`
- `id % 3 == 1` → trit=1, PLUS, `#b8bb26`
- `id % 3 == 2` → trit=-1, MINUS, `#cc241d`

---

## Top Activity (repos pushed today, 2026-07-21)

| Repo | Language | Stars | Source |
|------|----------|-------|--------|
| kubeflow/mlflow-integration | Python | 7 | kubeflow |
| kubeflow/pipelines | Python | 4168 | kubeflow |
| kubeflow/hub | Go | 178 | kubeflow |
| bmorphism/Gay.jl | Julia | 2 | bmorphism |
| wasita/wasita.github.io | Svelte | 1 | wasita |
| M1shaaa/M1shaaa | — | 0 | M1shaaa |
| plurigrid/gorj | Clojure | 1 | plurigrid |
| plurigrid/eirobri | Clojure | 0 | plurigrid |

---

## Repo Counts by Source (this sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | user | 30 |
| migalkin | social-graph | 19 |
| wasita | social-graph | 12 |
| M1shaaa | social-graph | 8 |
| DJedamski | social-graph | 6 |
| kristinezheng | social-graph | 5 |
| TeglonLabs | org | 5 |
| **TOTAL** | | **383** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

All 28 addresses returned `resource_not_found` for
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger v6390225056.
Accounts exist but have no native APT coin store registered — consistent with
accounts holding only objects/NFTs or uncreated coin stores.

### Multisig Contract Probes — ALL HEALTHY ✓

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|--------------|--------|
| A-B | 0x0da4f4… | 2 | ✓ healthy |
| A-G | 0xf56c4a… | 2 | ✓ healthy |
| Y-Z | 0xd3ffe1… | 2 | ✓ healthy |
| S-T | 0x3b1c3a… | 2 | ✓ healthy |
| V-W | 0x40fad7… | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

REST endpoints `/api/markets` and `/api/v1/markets` returned the Next.js SPA
shell — no JSON data available without browser-side rendering. Marked unavailable.

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

## Notable Highlights (2026-07-21)
- **kubeflow/pipelines**: 4,168 stars (up from 4,119 in April) — still most active kubeflow repo
- **bmorphism/Gay.jl**: active today (Julia)
- **wasita/wasita.github.io**: pushed today (Svelte personal site)
- **plurigrid/gorj**: this very repo, pushed today — forj + GF(3) sweep loop
- **plurigrid/asi**: 31 stars (up from 16 in April) — topological chemputer growing
- **All 5 multisig contracts**: healthy, 2-of-N, no degradation since last check
- **Aptos swarm**: 28 addresses probed — all lack native APT CoinStore (expected for hamming swarm wallets)
