# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-06

## Sweep Metadata
- **Date:** 2026-05-06
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 200 |
| Total Repo Snapshots | 200 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos Snapshotted | Total Stars |
|--------|------|---|---|
| plurigrid | org | 50 | 47 |
| kubeflow | org | 30 | 32,795 |
| TeglonLabs | org | 4 | 2 |
| bmorphism | user | 40 | 110 |
| zubyul | user | 20 | 10 |
| migalkin | social (zubyul graph) | 10 | 278 |
| wasita | social (zubyul graph) | 10 | 4 |
| DJedamski | social (zubyul graph) | 6 | 3 |
| kristinezheng | social (zubyul graph) | 6 | 0 |
| M1shaaa | social (zubyul graph) | 8 | 0 |
| AustinCStone | social (zubyul graph) | 16 | 108 |
| **TOTAL** | | **200** | **33,357** |

### Top Repos by Stars
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,622 | 2026-04-29 |
| kubeflow/pipelines | Python | 4,133 | 2026-05-05 |
| kubeflow/spark-operator | Python | 3,123 | 2026-05-05 |
| kubeflow/trainer | Go | 2,096 | 2026-05-06 |
| kubeflow/katib | Python | 1,683 | 2026-04-14 |
| kubeflow/examples | Jsonnet | 1,460 | 2025-04-14 |
| kubeflow/manifests | YAML | 1,015 | 2026-04-30 |
| kubeflow/arena | Go | 810 | 2026-04-28 |
| migalkin/NodePiece | Python | 143 | 2026-03-02 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |

### Most Recently Active (plurigrid + bmorphism)
- `plurigrid/gorj` — Clojure — pushed **2026-05-06** (this repo!)
- `bmorphism/Gay.jl` — Julia — pushed **2026-05-06** (187 open issues)
- `plurigrid/zig-syrup` — Zig OCapN Syrup — pushed 2026-04-30
- `plurigrid/horse` — TeX — pushed 2026-04-29
- `bmorphism/boxxy` — Move — pushed 2026-04-30
- `plurigrid/asi` — HTML topological chemputer — pushed 2026-04-26

### GF(3) Color Chain Distribution (200 increments)
| Trit | Name | Color | Count |
|---|---|---|---|
| 0 | ERGODIC | `#d3869b` (pink) | 66 |
| +1 | PLUS | `#b8bb26` (yellow-green) | 67 |
| -1 | MINUS | `#cc241d` (red) | 67 |

GF(3) chain repeats: `PLUS → MINUS → ERGODIC → …` (66⅔ full cycles across 200 increments)

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances — 28 Addresses

All queried via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` on `fullnode.mainnet.aptoslabs.com`.

**Result: All 28 wallets report 0.0 APT** (CoinStore resource value = 0)

| World | Address | APT Balance |
|---|---|---|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...5d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I–Z | 0x070f… → 0x7af0… | 0.0 (all 18) |

### Multisig Contract Probes — 5 Pairs
Probed via `0x1::multisig_account::num_signatures_required` view function.

| Pair | Address | Sigs Required | Status |
|---|---|---|---|
| A-B | 0x0da4...7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✓ HEALTHY |

**All 5 multisig contracts require 2-of-N signatures — all responsive and healthy.**

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — `testnet.mnx.fi` serves a Next.js SPA; no JSON API endpoints
(`/api/markets`, `/api/tickers`) return data. Market data not extractable at time of sweep.

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
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,622 stars — flagship ML platform for Kubernetes (active 2026-04-29)
- **kubeflow/pipelines**: 4,133 stars — pushed 2026-05-05
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) trit coloring
- **bmorphism/Gay.jl**: 187 open issues — wide-gamut SPI color library (pushed 2026-05-06)
- **migalkin/NodePiece**: 143 stars — compositional KG embeddings (ICLR'22)
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml MCP SDK
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs in TensorFlow
- **Hamming swarm**: 28/28 wallets accessible, 0 APT held — swarm dormant on-chain
- **Multisig health**: 5/5 contracts healthy, all threshold=2
