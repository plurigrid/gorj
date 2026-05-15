# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-15

## Sweep Metadata
- **Date:** 2026-05-15
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 98 |
| Total Repo Snapshots | 98 |
| Sources Covered | 3 orgs + 2 primary users + 6 social graph |

### Sources Swept

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 30 |
| kubeflow | org | 20 |
| TeglonLabs | org | 4 |
| bmorphism | user | 16 |
| zubyul | user | 16 |
| migalkin | social_graph | 5 |
| wasita | social_graph | 2 |
| AustinCStone | social_graph | 2 |
| kristinezheng | social_graph | 1 |
| M1shaaa | social_graph | 1 |
| DJedamski | social_graph | 1 |

### GF(3) Color Chain — All 98 Increments

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 32 |
| +1 | `#b8bb26` | PLUS | 33 |
| -1 | `#cc241d` | MINUS | 33 |

GF(3) assignment rule:
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=**ERGODIC**
- `id mod 3 == 1` → trit=+1, color=`#b8bb26`, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=**MINUS**

### Top Repos by Stars

| Repo | Language | Stars | Forks | Last Pushed |
|------|----------|-------|-------|-------------|
| kubeflow/kubeflow | — | 15,631 | 2,648 | 2026-05-07 |
| kubeflow/pipelines | Python | 4,140 | 1,992 | 2026-05-15 |
| kubeflow/spark-operator | Python | 3,125 | 1,482 | 2026-05-12 |
| kubeflow/trainer | Go | 2,098 | 949 | 2026-05-15 |
| kubeflow/katib | Python | 1,682 | 522 | 2026-05-09 |
| kubeflow/examples | Jsonnet | 1,462 | 757 | 2025-04-14 |
| kubeflow/manifests | YAML | 1,017 | 1,064 | 2026-05-13 |
| kubeflow/arena | Go | 810 | 190 | 2026-05-07 |
| kubeflow/kale | Python | 687 | 156 | 2026-05-13 |
| kubeflow/mpi-operator | Go | 526 | 235 | 2026-05-12 |
| migalkin/NodePiece | Python | 144 | 21 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 30 | 2025-03-03 |
| migalkin/StarE | Python | 89 | 16 | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2 | 2026-03-16 |
| plurigrid/asi | HTML | 22 | 5 | 2026-04-26 |

### Most Recently Active (2026-05-15)

- **plurigrid/gorj** — forj + Rama topology nREPL routing + GF(3) gay trit coloring (200 open issues, active dev)
- **bmorphism/Gay.jl** — Wide-gamut color sampling with splittable determinism (188 open issues)
- **kubeflow/trainer** — Distributed AI Model Training and LLM Fine-Tuning on Kubernetes
- **kubeflow/pipelines** — Machine Learning Pipelines for Kubeflow

### Social Graph Snapshot (zubyul network)

| User | Notable Repos | Top Stars |
|------|--------------|-----------|
| migalkin | NodePiece (KG embeddings), StarE (hyper-relational KG), NBFNet_mlx | 144 |
| wasita | wasita.github.io (Svelte personal site), magic-garden (bot) | 2 |
| AustinCStone | TextGAN (GAN text gen), EpsteinSearch | 92 |
| kristinezheng | kristinezheng.github.io (HTML) | 0 |
| M1shaaa | M1shaaa profile, lab-bookshelf | 0 |
| DJedamski | kaggle_ncaa18, Project_Euler | 0 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses queried via `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result:** All addresses returned `resource_not_found` for the legacy CoinStore module. This indicates the Hamming swarm wallets either:
1. Use the Fungible Asset (FA) standard (post-Aptos upgrade), or
2. Hold zero APT with no initialized CoinStore

| World | Address | APT Balance |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.0 (resource_not_found) |
| bob | 0x0a3c...512d | 0.0 (resource_not_found) |
| A | 0x8699...9d7a | 0.0 (resource_not_found) |
| B | 0x3f89...b13 | 0.0 (resource_not_found) |
| C | 0x38b9...35e | 0.0 (resource_not_found) |
| D | 0xf776...dd1 | 0.0 (resource_not_found) |
| E | 0xdc1d...d36 | 0.0 (resource_not_found) |
| F | 0x18a1...f71 | 0.0 (resource_not_found) |
| G | 0x69a3...f32 | 0.0 (resource_not_found) |
| H | 0xce67...00f | 0.0 (resource_not_found) |
| I | 0x070f...fc9 | 0.0 (resource_not_found) |
| J | 0x4d96...f54 | 0.0 (resource_not_found) |
| K | 0xa732...dc4 | 0.0 (resource_not_found) |
| L | 0x7c2e...ba9 | 0.0 (resource_not_found) |
| M | 0x6fed...2e9 | 0.0 (resource_not_found) |
| N | 0xe7dd...b2c | 0.0 (resource_not_found) |
| O | 0x7325...89d | 0.0 (resource_not_found) |
| P | 0x6218...948 | 0.0 (resource_not_found) |
| Q | 0xac40...a9 | 0.0 (resource_not_found) |
| R | 0x7ce6...e10 | 0.0 (resource_not_found) |
| S | 0xb875...386 | 0.0 (resource_not_found) |
| T | 0x3578...588 | 0.0 (resource_not_found) |
| U | 0x7586...956 | 0.0 (resource_not_found) |
| V | 0xb59d...2c3 | 0.0 (resource_not_found) |
| W | 0x5f32...7b0 | 0.0 (resource_not_found) |
| X | 0xa95c...47d | 0.0 (resource_not_found) |
| Y | 0xd8e3...4c4 | 0.0 (resource_not_found) |
| Z | 0x7af0...97c | 0.0 (resource_not_found) |

**Total APT in CoinStore across swarm:** 0.0 APT

### Multisig Contract Health

Probed via POST `https://fullnode.mainnet.aptoslabs.com/v1/view` with `0x1::multisig_account::num_signatures_required`:

| Pair | Contract Address | Sigs Required | Status |
|------|-----------------|--------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✅ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✅ HEALTHY |

**5/5 multisig contracts healthy. All require 2-of-N signatures.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE — Next.js SPA, no REST API accessible.**

Probed endpoints: `/api/markets`, `/api/tickers`, `/api/v1/markets` — all return SPA HTML (no JSON). Market data cannot be extracted via server-side HTTP probe.

---

## DuckDB Schema

```sql
world_increments(id, ts, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)              -- 98 rows

repo_snapshots(id, ts, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)              -- 98 rows

aptos_snapshots(ts, world, address, balance_apt)   -- 28 rows

multisig_probes(ts, pair, address, sigs_required, healthy)  -- 5 rows

mnx_snapshots(ts, ticker, name, category, price, change_pct) -- 1 row
```

---

*Generated by world-increment-sweep + hamming-swarm-snapshot agent*  
*GF(3) color chain: ERGODIC(#d3869b, trit=0) → PLUS(#b8bb26, trit=+1) → MINUS(#cc241d, trit=-1)*
