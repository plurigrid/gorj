# World-Increment Sweep + Hamming Snapshot

**Sweep Date:** 2026-04-05 ~16:18 UTC  
**DB Path:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Job 1: GitHub Social Graph Sweep

### Repos Per Org/User

| Org/User | Repos Sampled | Total Stars |
|---|---|---|
| kubeflow | 16 | 31,787 |
| migalkin | 6 | 276 |
| AustinCStone | 4 | 104 |
| bmorphism | 7 | 66 |
| plurigrid | 15 | 21 |
| TeglonLabs | 8 | 6 |
| DJedamski | 4 | 5 |
| wasita | 5 | 3 |
| zubyul | 5 | 2 |
| kristinezheng | 3 | 0 |
| M1shaaa | 4 | 0 |
| **Total** | **77** | **32,270** |

### Top Repos by Stars

| Repo | Language | Stars | Pushed At |
|---|---|---|---|
| kubeflow/kubeflow | — | 15,553 | 2026-01-05 |
| kubeflow/pipelines | Python | 4,118 | 2026-04-05 |
| kubeflow/spark-operator | Python | 3,110 | 2026-03-31 |
| kubeflow/trainer | Go | 2,074 | 2026-04-03 |
| kubeflow/katib | Python | 1,674 | 2026-04-02 |
| kubeflow/examples | Jsonnet | 1,459 | 2025-04-14 |
| kubeflow/manifests | YAML | 1,008 | 2026-04-05 |
| kubeflow/arena | Go | 808 | 2026-03-19 |
| kubeflow/kale | Python | 682 | 2026-04-02 |
| kubeflow/mpi-operator | Go | 519 | 2026-03-23 |
| migalkin/NodePiece | Python | 143 | 2022-02-02 |
| migalkin/StarE | Python | 88 | 2023-12-01 |
| AustinCStone/TextGAN | Python | 92 | 2016-10-04 |
| bmorphism/ocaml-mcp-sdk | OCaml | 60 | 2026-03-16 |
| plurigrid/asi | HTML | 15 | 2026-04-04 |

### Notable Recent Activity (bmorphism events)
- Heavy push activity on `plurigrid/nanoclj-zig` (Zig NaN-boxed Clojure interpreter) — 10+ pushes on 2026-04-05
- Active development on `plurigrid/horse` and `bmorphism/magic-world-org`

### Notable Recent Activity (zubyul events)
- Multiple PR and branch events on `plurigrid/gorj` on 2026-04-05
- Pushes to `plurigrid/asi-skills`

---

## Job 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 addresses returned 0 APT — no active balances found on mainnet CoinStore.
(Likely accounts exist on-chain but hold no liquid APT in the standard CoinStore resource.)

| World Label | Address (truncated) | APT Balance |
|---|---|---|
| alice | 0xc793...c7b | 0.0 |
| bob | 0x0a3c...d5d | 0.0 |
| A | 0x8699...d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...7b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

### Multisig Contract Probes

All 5 multisig contracts responded successfully with `sigs_required = 2`. All healthy.

| Pair | Address (truncated) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4...003 | 2 | true |
| A-G | 0xf56c...096 | 2 | true |
| Y-Z | 0xd3ff...883 | 2 | true |
| S-T | 0x3b1c...883 | 2 | true |
| V-W | 0x40fa...eb6 | 2 | true |

### MNX Markets

**Status: Unavailable**
`https://testnet.mnx.fi/api/markets` returns HTTP 404. The MNX testnet is a Next.js SPA ("The AI Exchange") where the `/api/markets` REST endpoint does not exist or is not publicly exposed. No market data was collected.

---

## GF(3) Color Chain Summary

Each world-increment row is assigned a GF(3) trit based on `id % 3`:

| Trit | Color | Name | Hex | Count |
|---|---|---|---|---|
| 0 (id%3=0) | Pink | ERGODIC | #d3869b | 4 |
| 1 (id%3=1) | Yellow-Green | PLUS | #b8bb26 | 4 |
| -1 (id%3=2) | Red | MINUS | #cc241d | 3 |

**Total world_increments rows:** 11 (3 orgs + 8 users)
**Total repo_snapshots rows:** 77
**Total aptos_snapshots rows:** 28
**Total multisig_probes rows:** 5
**Total mnx_snapshots rows:** 0 (unavailable)

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

## Notable Highlights
- **kubeflow/pipelines**: 4,118 stars — most popular ML pipeline for Kubernetes (pushed 2026-04-05)
- **kubeflow/spark-operator**: 3,110 stars — Kubernetes operator for Apache Spark
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- All 5 Hamming multisig contracts healthy with 2-of-N threshold signatures required
