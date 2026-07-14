# World-Increment Sweep — 2026-07-14

## Sweep Metadata
- **Date:** 2026-07-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (via Python duckdb)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 37 |
| Total Repo Snapshots (cumulative) | 1,197 |
| New Repos This Sweep | 253 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 2 users (+ 6 social graph) |

---

## GF(3) Color Chain — This Sweep

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | social_graph | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | social_graph | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | social_graph | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | social_graph | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | social_graph | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | social_graph | -1 | `#cc241d` | **MINUS** |
| 12 | hamming-swarm (aptos) | balance_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 13 | multisig (aptos) | probe | +1 | `#b8bb26` | **PLUS** |
| 14 | testnet.mnx.fi (mnx) | market_snapshot | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source (This Sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 (103 total) |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 50 (105 total) |
| zubyul | user | 49 |
| **TOTAL NEW** | | **253** |

### Top Repos by Stars (This Sweep)

**kubeflow:**
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,777 | 2026-07-14 |
| kubeflow/pipelines | Python | 4,165 | 2026-07-13 |
| kubeflow/spark-operator | Python | 3,135 | 2026-07-13 |
| kubeflow/trainer | Go | 2,138 | 2026-07-13 |
| kubeflow/katib | Python | 1,690 | 2026-07-11 |
| kubeflow/mcp-apache-spark-history-server | Python | 182 | 2026-07-07 |

**plurigrid:**
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| plurigrid/asi | HTML | 30 | 2026-07-10 |
| plurigrid/ontology | JavaScript | 8 | 2025-05-27 |
| plurigrid/vcg-auction | Rust | 7 | 2023-03-16 |
| plurigrid/gorj | Clojure | 1 | 2026-07-14 (1158 open issues) |

**bmorphism:**
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 22 | 2026-01-16 |
| bmorphism/Gay.jl | Julia | 2 | 2026-07-14 (187 open issues) |
| bmorphism/graphistry-mcp | Python | 2 | 2025-05-06 |

**TeglonLabs:**
| Repo | Language | Stars | Description |
|------|----------|-------|-------------|
| TeglonLabs/mathpix-gem | Ruby | 2 | Mathematical OCR gem |
| TeglonLabs/jank-crane | C++ | 0 | crane-jank converged-IR hub, GF3 maps |

**zubyul (top active):**
- `zubyul/voice-observatory` — Passive macOS TUI (2026-04-24)
- `zubyul/gay-world` — Goblin world builder (1★, 1 fork)
- `zubyul/tilelang-kernels` — GPU kernels for GF(3)/SplitMix64/Sinkhorn OT

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)

All 28 Hamming swarm wallets (alice, bob, A–Z) queried against Aptos mainnet fullnode.
**CoinStore<AptosCoin> resource absent on all addresses → APT balance = 0.0.**
Accounts exist on-chain (sequence_number confirmed for alice: 72).
Wallets may hold other tokens or serve multisig-only roles.

### Multisig Contract Probes — ALL HEALTHY ✅

All 5 multisig contracts respond with `num_signatures_required = 2` (2-of-2):

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428... | 2 | ✅ HEALTHY |
| A-G | 0xf56c4a1c... | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ffe181... | 2 | ✅ HEALTHY |
| S-T | 0x3b1c3ae9... | 2 | ✅ HEALTHY |
| V-W | 0x40fad7b4... | 2 | ✅ HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — SPA frontend with no accessible REST API.
Paths probed: `/api/markets`, `/api/v1/markets`, `/api/tickers` — all returned no data.
Recorded as `N/A` placeholder in `mnx_snapshots`.

---

## DuckDB Ducklake State

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows (cumulative) | Notes |
|-------|------------------|-------|
| world_increments | 37 | Time-series append |
| repo_snapshots | 1,197 | 3 sweeps accumulated |
| aptos_snapshots | 28 | This sweep only |
| multisig_probes | 5 | This sweep only |
| mnx_snapshots | 1 | Unavailable marker |

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

## Notable Highlights This Sweep
- **kubeflow/kubeflow**: 15,777 stars — active as of 2026-07-14
- **kubeflow/mcp-apache-spark-history-server**: 182★ new in 2026 — MCP for Spark History Server
- **bmorphism/ocaml-mcp-sdk**: 61★ — OCaml MCP SDK with Jane Street oxcaml_effect
- **bmorphism/Gay.jl**: 187 open issues — very active color sampling work
- **plurigrid/gorj**: 1,158 open issues — this repo, very active
- **All 5 multisig contracts**: healthy, 2-of-2 on Aptos mainnet
- **Hamming swarm (A-Z)**: all wallets have 0 APT native balance (CoinStore absent)
