# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-11

## Sweep Metadata
- **Date:** 2026-06-11
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 44 |
| Total Repo Snapshots | 44 |
| Sources Covered | 3 orgs + 2 users + 6 social graph |

### Sources

| Source | Type | Repos Snapshotted | Top Repo |
|--------|------|-------------------|----------|
| plurigrid | org | 9 | gorj (507 open issues, pushed 2026-06-11) |
| kubeflow | org | 6 | kubeflow/kubeflow ⭐15714 |
| TeglonLabs | org | 5 | jank-crane (C++, GF3 convergence, pushed 2026-06-08) |
| bmorphism | user | 6 | Gay.jl (Julia, 189 issues, pushed 2026-06-11) |
| zubyul | user | 4 | voice-observatory / nash-tui |
| migalkin | social | 3 | NodePiece ⭐144 (ICLR'22 KG embeddings) |
| DJedamski | social | 2 | kaggle_ncaa18 |
| wasita | social | 3 | wasita.github.io (Svelte, pushed 2026-06-01) |
| kristinezheng | social | 2 | kristinezheng.github.io (pushed 2026-06-07) |
| M1shaaa | social | 2 | M1shaaa profile (pushed 2026-06-11) |
| AustinCStone | social | 2 | TextGAN ⭐92 (TensorFlow GAN) |

### GF(3) Color Chain — Sample (ids 1–12)

| ID | Source | Repo | GF3 Trit | Color | Name |
|----|--------|------|----------|-------|------|
| 1  | plurigrid | asi | +1 | `#b8bb26` | **PLUS** |
| 2  | plurigrid | place | -1 | `#cc241d` | **MINUS** |
| 3  | plurigrid | eirobri | 0 | `#d3869b` | **ERGODIC** |
| 4  | plurigrid | nash-portal | +1 | `#b8bb26` | **PLUS** |
| 5  | plurigrid | gorj | -1 | `#cc241d` | **MINUS** |
| 6  | plurigrid | zig-syrup | 0 | `#d3869b` | **ERGODIC** |
| 7  | plurigrid | asi-skills | +1 | `#b8bb26` | **PLUS** |
| 8  | plurigrid | nanoclj-zig | -1 | `#cc241d` | **MINUS** |
| 9  | plurigrid | ontology | 0 | `#d3869b` | **ERGODIC** |
| 10 | kubeflow | trainer | +1 | `#b8bb26` | **PLUS** |
| 11 | kubeflow | kubeflow | -1 | `#cc241d` | **MINUS** |
| 12 | kubeflow | pipelines | 0 | `#d3869b` | **ERGODIC** |

GF(3) rule: `id%3==1 → PLUS(+1,#b8bb26)` | `id%3==2 → MINUS(-1,#cc241d)` | `id%3==0 → ERGODIC(0,#d3869b)`

### Notable Highlights
- **kubeflow/kubeflow** ⭐15714 — pushed today (2026-06-11)
- **kubeflow/pipelines** ⭐4152 — 493 open issues, active development
- **kubeflow/spark-operator** ⭐3126 — Kubernetes Spark operator
- **bmorphism/Gay.jl** — Wide-gamut GF(3) SPI colors, 189 open issues
- **TeglonLabs/jank-crane** — crane-jank IR hub with GF3 convergence maps
- **migalkin/NodePiece** ⭐144 — compositional KG representations (ICLR'22)
- **AustinCStone/TextGAN** ⭐92 — TensorFlow GAN for text generation
- **plurigrid/gorj** — this repo, ⚠️ 507 open issues, GF(3) nREPL orchestration

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (alice, bob, A–Z) — 28 addresses

All 28 Hamming swarm addresses queried via Aptos fullnode mainnet API. All returned **0 APT** — no registered `CoinStore<AptosCoin>` resource found (accounts uninitialized or assets under different paths on mainnet).

| World | Address (truncated) | APT |
|-------|---------------------|-----|
| alice | 0xc793ac… | 0.0 |
| bob | 0x0a3c00… | 0.0 |
| A | 0x8699ed… | 0.0 |
| B–Z | … | 0.0 each |

### Multisig Contract Probes — 5 pairs

All probed via `0x1::multisig_account::num_signatures_required`. **All 5 contracts healthy.**

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4f4… | 2 | ✅ healthy |
| A-G | 0xf56c4a… | 2 | ✅ healthy |
| Y-Z | 0xd3ffe1… | 2 | ✅ healthy |
| S-T | 0x3b1c3a… | 2 | ✅ healthy |
| V-W | 0x40fad7… | 2 | ✅ healthy |

### MNX Testnet Markets

`https://testnet.mnx.fi` — **Authentication required** (Vercel-gated SPA). No market data accessible from unauthenticated context. `mnx_snapshots` table is empty.

---

## DuckDB Ducklake — Final State

**Path:** `packages/world-increment/ducklake/world-increments.duckdb`

```
world_increments  44 rows  (GF3 trit-colored per-repo increment log)
repo_snapshots    44 rows  (org/user/name/lang/stars/forks/issues/pushed)
aptos_snapshots   28 rows  (alice+bob+A–Z, all 0 APT on mainnet)
multisig_probes    5 rows  (A-B, A-G, Y-Z, S-T, V-W — all 2-of-N healthy)
mnx_snapshots      0 rows  (unavailable: Vercel auth required)
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

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
