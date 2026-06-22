# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-22

## Sweep Metadata
- **Date:** 2026-06-22T05:11 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (2026-06-22)

| Metric | Value |
|--------|-------|
| Total World Increments | 414 |
| Total Repo Snapshots | 1335 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 1 | PLUS | `#b8bb26` | 139 |
| 2 | MINUS | `#cc241d` | 138 |
| 0 | ERGODIC | `#d3869b` | 137 |

Near-perfectly balanced (137/138/139) — ergodic chain at full capacity.

---

## Notable Recent Activity (last 7 days)

- **plurigrid/gorj** (Clojure) — pushed 2026-06-22, 734 open issues — forj + Rama + GF(3) gay trit coloring
- **bmorphism/Gay.jl** (Julia) — pushed 2026-06-22, 187 open issues — Wide-gamut color splittable determinism
- **M1shaaa/M1shaaa** — pushed 2026-06-22 (profile config active)
- **kubeflow/dashboard** (TypeScript) — pushed 2026-06-21
- **kubeflow/katib** (Python) — pushed 2026-06-20, 1684 stars
- **plurigrid/place** (TeX) — pushed 2026-06-20
- **wasita/proj-template** — pushed 2026-06-19
- **TeglonLabs/jank-crane** (C++) — pushed 2026-06-08, GF3 convergence maps

---

## Top Repos by Stars

| Org/User | Repo | Stars | Language |
|----------|------|-------|----------|
| kubeflow | kubeflow | 15,739 | — |
| kubeflow | pipelines | 4,156 | Python |
| kubeflow | spark-operator | 3,127 | Python |
| kubeflow | trainer | 2,118 | Go |
| kubeflow | katib | 1,684 | Python |
| kubeflow | examples | 1,460 | Jsonnet |
| kubeflow | community-distribution | 1,026 | YAML |
| kubeflow | kfp-tekton | 183 | TypeScript |
| migalkin | NodePiece | 144 | Python |
| kubeflow | website | 184 | HTML |
| migalkin | StarE | 89 | Python |
| bmorphism | ocaml-mcp-sdk | 61 | OCaml |
| AustinCStone | TextGAN | 92 | Python |
| plurigrid | asi | 26 | HTML |
| plurigrid | ontology | 8 | JavaScript |

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 48 |
| AustinCStone | user | 40 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| wasita | user (social) | 11 |
| TeglonLabs | org | 5 |
| M1shaaa | user (social) | 8 |
| kristinezheng | user (social) | 5 |
| DJedamski | user (social) | 6 |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances

All 28 wallets (alice, bob, A–Z) queried at `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result: All 28 wallets show 0.0 APT** — wallets exist on mainnet but hold no APT (unfunded swarm, pre-activation state).

| World | Address (prefix) | APT |
|-------|-----------------|-----|
| alice | 0xc793ac… | 0.0 |
| bob | 0x0a3c00… | 0.0 |
| A–Z (26) | various | 0.0 each |

### Multisig Contract Probes

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f4… | 2 | ✓ |
| A-G | 0xf56c4a… | 2 | ✓ |
| Y-Z | 0xd3ffe1… | 2 | ✓ |
| S-T | 0x3b1c3a… | 2 | ✓ |
| V-W | 0x40fad7… | 2 | ✓ |

**All 5 multisig contracts healthy — 2-of-N threshold active.**

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — Vercel deployment protection (HTTP 401). Requires bypass token.

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
- **kubeflow/kubeflow**: 15,739 stars — most active in sweep (pushed 2026-06-18)
- **kubeflow/pipelines**: 4,156 stars — ML pipeline for Kubernetes
- **plurigrid/gorj**: 734 open issues — this repo, Rama + GF(3), most active in plurigrid org
- **bmorphism/Gay.jl**: 187 open issues — wide-gamut color sampling (pushed 2026-06-22 day-of)
- **TeglonLabs/jank-crane**: C++ GF3 convergence maps, pushed 2026-06-08
- **All Hamming wallets**: 0.0 APT — swarm awaiting funding/activation
- **All multisigs**: 2-of-N healthy — Hamming distance pairings (A-B, A-G, Y-Z, S-T, V-W) all live
