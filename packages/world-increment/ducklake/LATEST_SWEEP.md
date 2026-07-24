# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-24

## Sweep Metadata
- **Date:** 2026-07-24
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| World Increments (this sweep) | 11 |
| Repo Snapshots (this sweep) | 179 |
| Aptos wallets queried | 28 |
| Multisig contracts probed | 5 |
| MNX markets | SPA — no API |
| Total cumulative world_increments | 34 |
| Total cumulative repo_snapshots | 1,123 |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — This Sweep (11 Increments)

| Source | Type | GF3 Trit | Color | Name |
|--------|------|-----------|-------|------|
| AustinCStone | user | 0 | `#d3869b` | **ERGODIC** |
| DJedamski | user | +1 | `#b8bb26` | **PLUS** |
| M1shaaa | user | -1 | `#cc241d` | **MINUS** |
| TeglonLabs | org | 0 | `#d3869b` | **ERGODIC** |
| bmorphism | user | +1 | `#b8bb26` | **PLUS** |
| kubeflow | org | -1 | `#cc241d` | **MINUS** |
| kristinezheng | user | 0 | `#d3869b` | **ERGODIC** |
| migalkin | user | +1 | `#b8bb26` | **PLUS** |
| plurigrid | org | -1 | `#cc241d` | **MINUS** |
| wasita | user | 0 | `#d3869b` | **ERGODIC** |
| zubyul | user | +1 | `#b8bb26` | **PLUS** |

GF(3) assignment: `id%3==0 → trit=0 ERGODIC #d3869b | id%3==1 → trit=1 PLUS #b8bb26 | id%3==2 → trit=-1 MINUS #cc241d`

---

### Top Repos by Stars (this sweep)

| Org/User | Repo | Stars | Language | Last Pushed |
|----------|------|-------|----------|-------------|
| kubeflow | kubeflow | 15,790 | — | 2026-07-10 |
| kubeflow | pipelines | 4,169 | Python | 2026-07-24 |
| kubeflow | spark-operator | 3,143 | Python | 2026-07-17 |
| kubeflow | trainer | 2,153 | Go | 2026-07-24 |
| kubeflow | katib | 1,692 | Python | 2026-07-22 |
| migalkin | NodePiece | 144 | Python | 2026-05-07 |
| migalkin | StarE | 89 | Python | 2026-04-16 |
| bmorphism | ocaml-mcp-sdk | 61 | OCaml | 2026-05-08 |
| migalkin | kgcourse2021 | 24 | HTML | 2026-07-10 |
| plurigrid | asi | 31 | HTML | 2026-07-10 |

### Notable Recent Activity (2026-07-xx)

- **plurigrid/gorj** (Clojure, 1,363 open issues) — pushed TODAY — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **kubeflow/pipelines** (Python, 4,169 stars) — pushed TODAY — ML Pipelines for Kubeflow
- **kubeflow/trainer** (Go, 2,153 stars) — pushed TODAY — Distributed AI Model Training
- **kubeflow/mcp-server** (Python, 29 stars) — pushed TODAY — MCP Server for AI-Assisted Development with Kubeflow
- **bmorphism/Gay.jl** (Julia, 187 open issues) — pushed 2026-07-21 — Wide-gamut color sampling, SPI determinism
- **TeglonLabs/jank-crane** (C++) — pushed 2026-06-08 — crane-jank converged-IR hub, GF3 convergence maps
- **plurigrid/eirobri** (Clojure) — pushed 2026-07-21 — EiRoBri replay world

### Repo Counts by Source

| Source | Type | Repos This Sweep |
|--------|------|-----------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| bmorphism | user | 50 |
| zubyul | user | 49 |
| migalkin | social graph | 8 |
| wasita | social graph | 9 |
| AustinCStone | social graph | 9 |
| kristinezheng | social graph | 4 |
| M1shaaa | social graph | 5 |
| TeglonLabs | org | 5 |
| DJedamski | social graph | 1 |
| **TOTAL** | | **179** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z = 28 addresses)

All 28 hamming swarm wallets queried against Aptos mainnet fullnode.

**Result:** All 28 addresses return 0.0 APT — accounts exist on-chain but have no `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource registered (unfunded or no coin store).

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z (26) | 0x8699...→0x7af0... | 0.0 each |

### Multisig Contract Probes

All 5 contracts probed via `POST /v1/view → 0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | **2** | ✅ |
| A-G | 0xf56c...0096 | **2** | ✅ |
| Y-Z | 0xd3ff...b883 | **2** | ✅ |
| S-T | 0x3b1c...7883 | **2** | ✅ |
| V-W | 0x40fa...eb6d | **2** | ✅ |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed.**

### MNX Markets (testnet.mnx.fi)

Site is live (Next.js SPA deployed on Vercel). No server-rendered JSON at `/api/markets` or `/api/v1/markets`. Market data loads client-side via JavaScript. **Status: SPA only — no structured data extractable without browser execution.**

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
