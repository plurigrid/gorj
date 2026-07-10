# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-10

## Sweep Metadata
- **Date:** 2026-07-10
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **GF(3) this run:** trit=1 · color=#b8bb26 · name=PLUS

---

## Summary Counts (2026-07-10 run)

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 24 |
| Total Repo Snapshots (cumulative) | 1014 |
| New repos snapshotted this run | ~70 |
| Sources Covered | 3 orgs + 8 users (+ social graph) |
| Aptos addresses probed | 28 |
| Multisig contracts probed | 5 |

---

## JOB 1: GitHub Social Graph (2026-07-10)

### Source Breakdown

| Source | Type | Repos | Top Stars |
|--------|------|-------|-----------|
| plurigrid | org | 103 total | ontology ★8, nanoclj-zig (20 issues), asi-skills ★3 |
| kubeflow | org | 105 total | kubeflow ★15770, pipelines ★4169, spark-operator ★3136 |
| TeglonLabs | org | 5 | mathpix-gem ★2, jank-crane (GF3 loopify) |
| bmorphism | user | 49 | Gay.jl ★2 (187 issues!), anti-bullshit-mcp ★23 |
| zubyul | user | 49 | gay-world, tilelang-kernels, nash-tui |
| migalkin | social | 19 | NodePiece ★144, StarE ★89, NBFNet_mlx ★10 |
| wasita | social | 11 | wasita.github.io (Svelte), magic-garden bot |
| AustinCStone | social | 40 | TextGAN ★92, StereoVisionMRF ★11 |
| DJedamski | social | 6 | School (R), kaggle_ncaa18 |
| kristinezheng | social | 5 | lookit-jenga, Green-Machine (HackMIT 2021) |
| M1shaaa | social | 8 | lab-bookshelf (TypeScript), MNIST-Classifier |

### Notable New Activity (since last sweep ~3 months ago)

- **kubeflow/community-distribution**: Pushed 2026-07-09 (active CNCF distro)
- **kubeflow/pipelines**: Pushed 2026-07-09, 421 open issues
- **kubeflow/trainer**: ★2134 — Distributed AI Training on K8s, pushed 2026-07-09
- **kubeflow/mpi-operator**: Pushed 2026-07-09
- **bmorphism/Gay.jl**: 187 open issues — wide-gamut splittable determinism color system very active
- **bmorphism/satreadout**: Lean 4.28 + mathlib machine-checked readout, pushed 2026-06-20
- **bmorphism/oxgame**: Stellar resolution + open-game OCaml, pushed 2026-05-15
- **TeglonLabs/jank-crane**: crane-jank GF3 convergence maps, pushed 2026-06-08
- **plurigrid/asi-skills**: 69 skills Galois Hole Type (Seven Sketches §1.4.1), pushed 2026-04-26
- **plurigrid/nanoclj-zig**: NaN-boxed Clojure in Zig 0.15 + interaction nets + GF(3), pushed 2026-04-25
- **migalkin/NodePiece**: Knowledge graph embedding ICLR'22, still active 2026

---

## JOB 2: Hamming Swarm Snapshot (2026-07-10)

### Aptos Mainnet Balances — 28 Addresses

All CoinStore resources returned 0 (uninitialized or empty accounts on mainnet).

| World | Address | Balance |
|-------|---------|---------|
| alice | 0xc793...cc7b | 0.00000000 APT |
| bob | 0x0a3c...512d | 0.00000000 APT |
| A–Z (26) | (see DB) | 0.00000000 APT each |

### Multisig Contract Probes — 5 Pairs

All 5 multisig contracts are live and healthy:

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✅ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✅ HEALTHY |

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — requires Vercel authentication. All endpoints (`/api/markets`, `/api/v1/markets`, `/api/tickers`) return auth wall.

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
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS (this sweep)
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
