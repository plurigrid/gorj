# World-Increment Sweep + Hamming Snapshot — 2026-06-10

## Sweep Metadata
- **Date:** 2026-06-10
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 112 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — 11 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

### Repo Source Coverage

| Source | Type | Total (GitHub) | Captured | Top Starred Repo |
|--------|------|----------------|----------|-----------------|
| plurigrid | org | 101 | 23 | asi (25★) |
| kubeflow | org | 48 | 24 | kubeflow (15,714★) |
| TeglonLabs | org | 5 | 5 | mathpix-gem (2★) |
| bmorphism | user | 103 | 28 | ocaml-mcp-sdk (61★) |
| zubyul | user | 49 | 13 | WGCNA (2★) |
| migalkin | user | 19 | 5 | NodePiece (144★) |
| DJedamski | user | 6 | 2 | School (1★) |
| wasita | user | 11 | 4 | magic-garden (2★) |
| kristinezheng | user | 5 | 2 | — |
| M1shaaa | user | 8 | 2 | — |
| AustinCStone | user | 40 | 3 | TextGAN (92★) |

### Notable Repos (Pushed ≤ 48h from sweep)

- `plurigrid/place` pushed **2026-06-10** — TeX
- `plurigrid/asi` pushed **2026-06-10** — HTML, 25★ — "everything is topological chemputer!"
- `plurigrid/gorj` pushed **2026-06-10** — Clojure, 479 open issues — forj + Rama topology + GF(3)
- `kubeflow/hub` pushed **2026-06-10** — Go, 175★ — Model Registry
- `kubeflow/website` pushed **2026-06-10** — HTML, 184★
- `kubeflow/pipelines` pushed **2026-06-10** — Python, 4,153★
- `kubeflow/dashboard` pushed **2026-06-10** — TypeScript, 16★
- `kubeflow/trainer` pushed **2026-06-10** — Go, 2,112★
- `bmorphism/Gay.jl` pushed **2026-06-10** — Julia, 189 open issues — wide-gamut GF(3) color sampling
- `kristinezheng/kristinezheng.github.io` pushed **2026-06-07**

### Top Repos by Stars (Full Graph)

| Repo | Stars | Lang | Pushed |
|------|-------|------|--------|
| kubeflow/kubeflow | 15,714 | — | 2026-05-24 |
| kubeflow/pipelines | 4,153 | Python | 2026-06-10 |
| kubeflow/spark-operator | 3,126 | Python | 2026-06-09 |
| kubeflow/trainer | 2,112 | Go | 2026-06-10 |
| kubeflow/katib | 1,685 | Python | 2026-06-05 |
| kubeflow/examples | 1,462 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,022 | YAML | 2026-06-09 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| bmorphism/risc0-cosmwasm-example | 23 | Rust | 2022-10-20 |
| plurigrid/asi | 25 | HTML | 2026-06-10 |
| plurigrid/ontology | 8 | JavaScript | 2025-05-27 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses probed)

**Status:** All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version 5,666,083,543. Addresses exist on mainnet but have no initialized CoinStore (never funded with APT).

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793...cc7b | null |
| bob | 0x0a3c...2d5d | null |
| A | 0x8699...9d7a | null |
| B–Z | (25 addresses) | null |

### Multisig Contract Probes — ALL HEALTHY ✓

All 5 probed multisig contracts respond correctly and require 2-of-N signatures.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Vercel deployment protection active, authentication required. `mnx_snapshots` table is empty for this sweep.

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
