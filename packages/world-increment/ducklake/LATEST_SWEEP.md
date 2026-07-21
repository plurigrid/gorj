# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-21

## Sweep Metadata
- **Date:** 2026-07-21
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos This Run |
|--------|------|----------------|
| plurigrid | org | 50 |
| kubeflow | org | 30 |
| TeglonLabs | org | 5 |
| bmorphism | user | 50 |
| zubyul | user | 30 |
| migalkin | social-graph | 4 (top) |
| DJedamski | social-graph | 2 (top) |
| wasita | social-graph | 3 (top) |
| kristinezheng | social-graph | 2 (top) |
| M1shaaa | social-graph | 2 (top) |
| AustinCStone | social-graph | 3 (top) |
| **TOTAL this run** | | **181** |

### Notable Activity (most recently pushed 2026-07-21)

- `plurigrid/eirobri` (Clojure) — pushed 2026-07-21
- `plurigrid/gorj` (Clojure) — pushed 2026-07-21 (this repo)
- `bmorphism/Gay.jl` (Julia) — pushed 2026-07-21
- `wasita/wasita.github.io` (Svelte) — pushed 2026-07-21
- `kubeflow/mlflow-integration` (Python) — pushed 2026-07-21
- `kubeflow/pipelines` (Python, ⭐4168) — pushed 2026-07-21

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15789 | — |
| kubeflow/pipelines | 4168 | Python |
| kubeflow/spark-operator | 3142 | Python |
| kubeflow/trainer | 2152 | Go |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| plurigrid/asi | 31 | HTML |

### GF(3) Color Chain Distribution (cumulative in DB)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 67 |
| 1 | #b8bb26 | PLUS | 69 |
| -1 | #cc241d | MINUS | 68 |

**Total world_increments in DB: 204**

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 wallets (alice, bob, A–Z) queried against Aptos mainnet fullnode.

**Result:** All wallets return `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. No initialized APT coin store on mainnet — balance recorded as **0.0 APT** for all 28 addresses.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793acde... | 0.0 |
| bob   | 0x0a3c00c5... | 0.0 |
| A | 0x8699edc0... | 0.0 |
| B | 0x3f892ebe... | 0.0 |
| C | 0x38b99e63... | 0.0 |
| D | 0xf7765624... | 0.0 |
| E | 0xdc1d9d53... | 0.0 |
| F | 0x18a14b5b... | 0.0 |
| G | 0x69a394c0... | 0.0 |
| H | 0xce67c327... | 0.0 |
| I | 0x070fe5d7... | 0.0 |
| J | 0x4d964db8... | 0.0 |
| K | 0xa732040a... | 0.0 |
| L | 0x7c2eaeaf... | 0.0 |
| M | 0x6fed37a7... | 0.0 |
| N | 0xe7dde6da... | 0.0 |
| O | 0x73252b60... | 0.0 |
| P | 0x62187920... | 0.0 |
| Q | 0xac40fa50... | 0.0 |
| R | 0x7ce605cc... | 0.0 |
| S | 0xb8753014... | 0.0 |
| T | 0x35781dc0... | 0.0 |
| U | 0x75860da4... | 0.0 |
| V | 0xb59dd817... | 0.0 |
| W | 0x5f32aef7... | 0.0 |
| X | 0xa95cbbd1... | 0.0 |
| Y | 0xd8e32848... | 0.0 |
| Z | 0x7af0ef6e... | 0.0 |

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required` on mainnet.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f428... | 2 | ✅ |
| A-G | 0xf56c4a1c... | 2 | ✅ |
| Y-Z | 0xd3ffe181... | 2 | ✅ |
| S-T | 0x3b1c3ae9... | 2 | ✅ |
| V-W | 0x40fad7b4... | 2 | ✅ |

**All 5 multisig contracts healthy — 2-of-2 signature requirement confirmed on all pairs.**

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` returns a Next.js SPA (HTML). No public REST API endpoints found at `/api/markets` or `/api/v1/markets`. Market data **unavailable** — SPA requires browser JS execution to hydrate state.

---

## DuckDB State

**Path:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 204 |
| repo_snapshots | 1125 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

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
- **kubeflow/kubeflow**: 15,789 stars (up from 15,565 in Apr run) — growing fast
- **kubeflow/pipelines**: 4,168 stars — pushed 2026-07-21
- **plurigrid/gorj**: This very repo — active today (2026-07-21)
- **bmorphism/Gay.jl**: Julia, pushed 2026-07-21 — latest activity from bmorphism
- **migalkin/NodePiece**: 144 stars — KG embedding research at ICLR22, still gaining traction
- **All 5 Hamming multisigs**: 2-of-2, all healthy
- **Hamming swarm wallets**: All 28 addresses unfunded on mainnet (no CoinStore)
