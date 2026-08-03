# World-Increment Sweep + Hamming Swarm Snapshot — 2026-08-03

## Sweep Metadata
- **Date:** 2026-08-03
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried (2026-08-03)

| Source | Type | Repos This Sweep |
|--------|------|-----------------|
| plurigrid | org | 30 |
| kubeflow | org | 16 |
| TeglonLabs | org | 5 |
| bmorphism | user | 10 |
| zubyul | user | 10 |
| migalkin | user (social graph) | 5 |
| AustinCStone | user (social graph) | 4 |
| M1shaaa | user (social graph) | 3 |
| **Total new** | | **83 repo snapshots** |

> DJedamski, wasita, kristinezheng: no public repos found in query window.

### GF(3) Color Chain Distribution (this sweep)

| GF(3) Name | Color | Trit | Count |
|------------|-------|------|-------|
| ERGODIC | #d3869b | 0 | 27 |
| PLUS | #b8bb26 | +1 | 28 |
| MINUS | #cc241d | -1 | 28 |

### Top Repos by Stars (this sweep)

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,804 | 2026-07-10 |
| kubeflow/pipelines | Python | 4,173 | 2026-08-03 |
| kubeflow/spark-operator | Python | 3,142 | 2026-07-31 |
| kubeflow/trainer | Go | 2,165 | 2026-07-31 |
| kubeflow/katib | Python | 1,694 | 2026-08-02 |
| kubeflow/community-distribution | YAML | 1,029 | 2026-07-29 |
| kubeflow/arena | Go | 816 | 2026-07-29 |
| kubeflow/kale | Python | 699 | 2026-08-01 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |

### Notable Active Repos (plurigrid social cluster)

- **plurigrid/gorj** — forj + Rama topology nREPL routing + GF(3) gay trit coloring (pushed **2026-08-03**, 1593 issues)
- **plurigrid/zig-syrup** — High-performance Zig OCapN Syrup + CapTP optimizations (pushed 2026-07-28)
- **plurigrid/place** — bci.place forester (pushed 2026-08-02, 15 open issues)
- **bmorphism/Gay.jl** — Wide-gamut splittable determinism (pushed **2026-08-03**, 188 open issues)
- **TeglonLabs/jank-crane** — crane-jank converged-IR hub with GF3 convergence maps (pushed 2026-06-08)
- **kubeflow/mcp-server** — MCP Server for AI-Assisted Kubeflow Development (31 stars, pushed 2026-07-31)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets: alice, bob, A–Z)

All 28 addresses returned `resource_not_found` on Aptos mainnet — the `CoinStore<AptosCoin>` resource has not been initialized for any of these addresses. Recorded as **0.0 APT** for all worlds.

| Range | Wallets | Balance APT |
|-------|---------|-------------|
| alice | 0xc793... | 0.0 |
| bob | 0x0a3c... | 0.0 |
| A–Z (26) | various | 0.0 each |

### Multisig Contract Probes — ALL HEALTHY ✓

All 5 multisig contracts on Aptos mainnet responded with **2 signatures required**:

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4... | 2 | ✓ healthy |
| A-G | 0xf56c... | 2 | ✓ healthy |
| Y-Z | 0xd3ff... | 2 | ✓ healthy |
| S-T | 0x3b1c... | 2 | ✓ healthy |
| V-W | 0x40fa... | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

Status: **SPA only** — `https://testnet.mnx.fi/api/markets` returns HTML (Next.js SPA). No market data API is publicly exposed. `mnx_snapshots` table remains empty this sweep.

---

## DuckDB Cumulative State

| Table | Total Rows | Added This Sweep |
|-------|-----------|-----------------|
| world_increments | 106 | +83 |
| repo_snapshots | 1,027 | +83 |
| aptos_snapshots | 28 | +28 |
| multisig_probes | 5 | +5 |
| mnx_snapshots | 0 | 0 |

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
