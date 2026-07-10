# World-Increment Sweep + Hamming Snapshot — 2026-07-10

## Sweep Metadata
- **Date:** 2026-07-10
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (this run) | 392 |
| Total Repo Snapshots (cumulative DB) | 1,336 |
| Sources Covered | 3 orgs + 8 users |
| Aptos wallets probed | 28 |
| Multisig contracts probed | 5 |

---

## GF(3) Color Chain Distribution (this run)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 137 |
| +1 | `#b8bb26` | PLUS | 139 |
| -1 | `#cc241d` | MINUS | 139 |

GF(3) rule: `id mod 3 == 0` → ERGODIC · `id mod 3 == 1` → PLUS · `id mod 3 == 2` → MINUS

---

## Top Repos by Source

### plurigrid (100 repos) — most active: gorj pushed 2026-07-10
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gorj | Clojure | 1 | 2026-07-10 |
| place | TeX | 1 | 2026-07-07 |
| asi | HTML | 30 | 2026-06-29 |
| shrimp | — | 0 | 2026-07-03 |
| eirobri | Clojure | 0 | 2026-06-30 |

### kubeflow (49 repos)
| Repo | Language | Stars |
|------|----------|-------|
| kubeflow | — | 15,771 |
| pipelines | Python | 4,169 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

### bmorphism (100 repos)
Most recently updated; diverse stack (OCaml, Zig, Python, Clojure).

### zubyul social graph: migalkin, wasita, DJedamski, kristinezheng, M1shaaa, AustinCStone
All captured; most recent activity: wasita.github.io pushed 2026-07-06.

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| AustinCStone | user | 40 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| wasita | user | 11 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user | 5 |
| **TOTAL** | | **392** |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances

**Ledger state at query time:** version 6,205,914,685 · epoch 16,479 · block 888,203,517

All 28 addresses (alice, bob, A–Z) returned HTTP 404 `resource_not_found` for `CoinStore<AptosCoin>`.  
No coin store has been initialized on any of these addresses → **balance = 0.0 APT for all**.

### Multisig Contract Probes — ALL HEALTHY ✓

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...987003 | 2 | ✓ |
| A-G | 0xf56c4a1c...c0096 | 2 | ✓ |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ |
| S-T | 0x3b1c3ae9...d7883 | 2 | ✓ |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ |

All multisig accounts require 2-of-N signatures and are responding correctly.

### MNX Markets

`https://testnet.mnx.fi` is protected by Vercel deployment authentication.  
Status: **unavailable** — requires bypass token or Vercel CLI. No market data captured.

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,771 stars — flagship ML platform for Kubernetes (↑ from 15,565 in Apr sweep)
- **kubeflow/pipelines**: 4,169 stars (↑ from 4,119)
- **plurigrid/asi**: 30 stars (↑ from 16 in Apr sweep) — topological chemputer gaining traction
- **plurigrid/gorj**: pushed today 2026-07-10 — active development
- **TeglonLabs/jank-crane**: new C++ repo (GF3+crane converged-IR hub), first appeared since Apr sweep
- **wasita.github.io** (Svelte): pushed 2026-07-06 — social graph still active
- **All 5 multisigs**: healthy at 2-of-N threshold — Hamming swarm structurally sound
- **MNX testnet**: behind Vercel auth wall — needs bypass token for future sweeps
