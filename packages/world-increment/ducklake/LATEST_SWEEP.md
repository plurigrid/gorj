# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-21

## Sweep Metadata
- **Date:** 2026-06-21
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| New World Increments (this sweep) | 404 |
| Cumulative Repo Snapshots in Ducklake | 1325 |
| Aptos Swarm Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Snapshots | 0 (testnet unavailable) |
| Sources Covered | 3 orgs + 8 users (social graph) |

---

## GF(3) Color Chain — This Sweep (404 increments)

| GF3 Trit | Color | Name | Count |
|-----------|-------|------|-------|
| 0 | `#d3869b` | **ERGODIC** | 134 |
| +1 | `#b8bb26` | **PLUS** | 135 |
| -1 | `#cc241d` | **MINUS** | 135 |

GF(3) chain rule: `id%3==0 → ERGODIC, id%3==1 → PLUS, id%3==2 → MINUS`  
This sweep produced **134 full GF(3) cycles + 2 trailing trits**.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Balances — 28 Addresses

All 28 Hamming swarm addresses (alice, bob, A–Z) returned **0 APT** via `CoinStore<AptosCoin>`. Addresses are on mainnet but hold no APT in the standard coin store (may hold other assets).

### Multisig Contract Probes — All Healthy

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4...003` | 2 | ✓ HEALTHY |
| A-G | `0xf56c...096` | 2 | ✓ HEALTHY |
| Y-Z | `0xd3ff...883` | 2 | ✓ HEALTHY |
| S-T | `0x3b1c...883` | 2 | ✓ HEALTHY |
| V-W | `0x40fa...b6d` | 2 | ✓ HEALTHY |

All 5 multisig accounts require 2-of-N signatures and responded to `0x1::multisig_account::num_signatures_required`.

### MNX Markets
`https://testnet.mnx.fi` — **UNAVAILABLE**. SPA with no accessible API endpoints. `mnx_snapshots` table has 0 rows.

---

---

## Top Repos by Source (2026-06-21 snapshot)

### plurigrid (102 repos this sweep)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 26 | 2026-06-10 |
| ontology | JavaScript | 8 | 2025-05-27 |
| vcg-auction | Rust | 7 | 2023-03-16 |
| agent | Python | 5 | 2023-03-31 |
| zig-syrup | Zig | 2 | 2026-04-30 |
| nash-portal | Rust | 2 | 2026-05-19 |
| gorj | Clojure | 0 | **2026-06-21** |

### kubeflow (50 repos this sweep)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,738 | 2026-06-18 |
| pipelines | Python | 4,155 | 2026-06-20 |
| spark-operator | Python | 3,127 | 2026-06-18 |
| trainer | Go | 2,118 | 2026-06-19 |
| katib | Python | 1,683 | **2026-06-21** |

### TeglonLabs (7 repos this sweep)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

### bmorphism (103 repos this sweep)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| Gay.jl | Julia | 2 | **2026-06-21** |
| shitcoin | Python | 5 | 2026-04-08 |

### migalkin (21 repos this sweep)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 25 |

### AustinCStone (32 repos this sweep)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |

---

## Repo Counts by Source (this sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 102 |
| bmorphism | user | 103 |
| kubeflow | org | 50 |
| zubyul | user | 51 |
| AustinCStone | user | 32 |
| migalkin | user | 21 |
| wasita | user | 13 |
| M1shaaa | user | 10 |
| DJedamski | user | 8 |
| TeglonLabs | org | 7 |
| kristinezheng | user | 7 |
| **TOTAL** | | **404** |

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

## Notable Highlights (2026-06-21)
- **kubeflow/kubeflow**: 15,738 stars (+173 since Apr 12) — flagship ML platform for Kubernetes
- **kubeflow/katib**: pushed **today** (2026-06-21) — AutoML hyperparameter tuning
- **kubeflow/dashboard**: pushed **today** (2026-06-21) — central dashboard
- **bmorphism/Gay.jl**: 187 open issues, pushed **today** — wide-gamut splittable color sampling
- **M1shaaa/M1shaaa**: profile pushed **today** (2026-06-21 03:50 UTC)
- **plurigrid/gorj**: This very repo — pushed today (gorj is the sweep target)
- **plurigrid/place**: pushed 2026-06-20 — bci.place forester preview
- **plurigrid/asi**: 26 stars (+10 since Apr 12) — topological chemputer
- **TeglonLabs/jank-crane**: new repo (created 2026-06-08) — C++ jank/crane GF3 convergence maps
- **Hamming swarm**: All 5 multisig contracts healthy at 2-of-N threshold
- **MNX testnet**: offline/unavailable
