# World-Increment Sweep — 2026-07-23

**Date:** 2026-07-23  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted | Top Repo (stars) |
|--------|------|-------------------|-----------------|
| plurigrid | org | 100 | plurigrid/asi ⭐31 |
| kubeflow | org | 49 | kubeflow/kubeflow ⭐15789 |
| TeglonLabs | org | 5 | TeglonLabs/mathpix-gem ⭐2 |
| bmorphism | user | 106 | bmorphism/ocaml-mcp-sdk ⭐61 |
| zubyul | user | 49 | zubyul/gay-world ⭐1 |
| migalkin | user | 19 | migalkin/NodePiece ⭐144 |
| wasita | user | 12 | wasita/magic-garden ⭐2 |
| AustinCStone | user | 41 | AustinCStone/TextGAN ⭐92 |
| DJedamski | user | 6 | DJedamski/Kaggle ⭐1 |
| kristinezheng | user | 5 | kristinezheng/kristinezheng.github.io ⭐0 |
| M1shaaa | user | 8 | M1shaaa/lab-bookshelf- ⭐0 |

**Total repos snapshotted this run:** 190 new increments  
**Cumulative world_increments in DB:** 213  
**Cumulative repo_snapshots in DB:** 1134

### Recent Activity Highlights

- **plurigrid/gorj** (this repo): pushed 2026-07-23 — most recently active plurigrid repo
- **kubeflow/trainer** ⭐2153: pushed 2026-07-23 — active kubeflow ML training operator
- **kubeflow/mpi-operator** ⭐530: pushed 2026-07-23
- **kubeflow/pipelines-components**: pushed 2026-07-23
- **bmorphism/Gay.jl** ⭐2: updated 2026-07-21 — wide-gamut color sampling (Pigeons.jl SPI + LispSyntax)
- **bmorphism/anti-bullshit-mcp-server** ⭐22: updated 2026-07-12
- **bmorphism/ocaml-mcp-sdk** ⭐61: most-starred active bmorphism repo
- **wasita/wasita.github.io** ⭐1: updated 2026-07-21 — personal site active
- **migalkin/kgcourse2021** ⭐24: updated 2026-07-10
- **migalkin/NodePiece** ⭐144: top migalkin repo — KG embeddings (ICLR'22)
- **AustinCStone/TextGAN** ⭐92: top AustinCStone repo — text generation GAN
- **TeglonLabs/jank-crane**: pushed 2026-06-08 — crane-jank converged-IR hub, GF3 convergence maps
- **plurigrid/asi** ⭐31: pushed 2026-07-10 — top plurigrid repo

### GF(3) Color Chain Distribution (this run)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 70 |
| 1 | #b8bb26 | PLUS | 72 |
| -1 | #cc241d | MINUS | 71 |

GF(3) assignment: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 Hamming swarm wallets queried via `fullnode.mainnet.aptoslabs.com`.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…12d5 | 0.0 |
| A | 0x8699…9d7a | 0.0 |
| B | 0x3f89…b13 | 0.0 |
| C | 0x38b9…535e | 0.0 |
| D | 0xf776…fdd1 | 0.0 |
| E | 0xdc1d…8d36 | 0.0 |
| F | 0x18a1…cf71 | 0.0 |
| G | 0x69a3…f32 | 0.0 |
| H | 0xce67…300f | 0.0 |
| I | 0x070f…1fc9 | 0.0 |
| J | 0x4d96…7f54 | 0.0 |
| K | 0xa732…5dc4 | 0.0 |
| L | 0x7c2e…eba9 | 0.0 |
| M | 0x6fed…f2e9 | 0.0 |
| N | 0xe7dd…1b2c | 0.0 |
| O | 0x7325…a89d | 0.0 |
| P | 0x6218…c948 | 0.0 |
| Q | 0xac40…89a9 | 0.0 |
| R | 0x7ce6…6e10 | 0.0 |
| S | 0xb875…0386 | 0.0 |
| T | 0x3578…4588 | 0.0 |
| U | 0x7586…9956 | 0.0 |
| V | 0xb59d…af2c3 | 0.0 |
| W | 0x5f32…c7b0 | 0.0 |
| X | 0xa95c…047d | 0.0 |
| Y | 0xd8e3…44c4 | 0.0 |
| Z | 0x7af0…197c | 0.0 |

**All 28 wallets: 0.0 APT.** Wallets are unfunded on Aptos mainnet — likely devnet/testnet addresses or not yet seeded with mainnet APT.

### Multisig Contract Probes

All 5 multisig pairs probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4…7003 | 2 | ✅ |
| A-G | 0xf56c…0096 | 2 | ✅ |
| Y-Z | 0xd3ff…b883 | 2 | ✅ |
| S-T | 0x3b1c…7883 | 2 | ✅ |
| V-W | 0x40fa…eb6d | 2 | ✅ |

**All 5 multisig accounts healthy — 2-of-N threshold confirmed on all pairs.**

### MNX Markets (testnet.mnx.fi)

`/api/markets` and `/api/v1/markets` return Next.js SPA HTML — no REST endpoints exposed. Market data is client-rendered and not extractable via curl. **Status: SPA — no API data available.**

---

## DuckDB Schema Summary

```
world_increments  : 213 rows  (GF3-colored increment chain)
repo_snapshots    : 1134 rows (cumulative repo snapshots)
aptos_snapshots   : 28 rows   (this run — all 0.0 APT)
multisig_probes   : 5 rows    (this run — all healthy, sigs=2)
mnx_snapshots     : 0 rows    (SPA, unavailable)
```

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
