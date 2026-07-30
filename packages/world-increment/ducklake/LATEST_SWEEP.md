# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-07-30  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Total | Captured | Top Star |
|--------|------|-------|----------|----------|
| plurigrid | org | 103 | 21 | asi (56⭐) |
| kubeflow | org | 49 | 15 | kubeflow (15798⭐) |
| TeglonLabs | org | 5 | 5 | mathpix-gem (2⭐) |
| bmorphism | user | 106 | 12 | ocaml-mcp-sdk (61⭐) |
| zubyul | user | 49 | 9 | gay-world (1⭐) |
| migalkin | social | 19 | 4 | NodePiece (144⭐) |
| DJedamski | social | 6 | 2 | kaggle_ncaa18 (0⭐) |
| wasita | social | 12 | 3 | magic-garden (2⭐) |
| kristinezheng | social | 5 | 2 | personal site (0⭐) |
| M1shaaa | social | 8 | 2 | M1shaaa (0⭐) |
| AustinCStone | social | 41 | 3 | TextGAN (92⭐) |

### Most Recently Active

- `plurigrid/gorj` — 2026-07-30T22:14 (1521 open issues — active development hub)
- `kubeflow/spark-operator` — 2026-07-30T22:24 (3142⭐, Python)
- `kubeflow/trainer` — 2026-07-30T19:59 (2163⭐, Go)
- `M1shaaa/M1shaaa` — 2026-07-30T13:50
- `bmorphism/Gay.jl` — 2026-07-30T02:12 (188 open issues)

### GF(3) Color Chain Applied (id%3)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 33 |
| 1 | `#b8bb26` | PLUS | 34 |
| -1 | `#cc241d` | MINUS | 34 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 addresses (alice, bob, A–Z) queried against:
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger ~v6536598554

**All 28 balances = 0.0 APT (resource_not_found)**  
Addresses are on-chain but CoinStore not initialized — no APT coin resource registered on any address.

### Multisig Contract Probes (`0x1::multisig_account::num_signatures_required`)

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|--------------|--------|
| A-B | `0x0da4f428…87003` | 2 | ✅ healthy |
| A-G | `0xf56c4a1c…0096` | 2 | ✅ healthy |
| Y-Z | `0xd3ffe181…b883` | 2 | ✅ healthy |
| S-T | `0x3b1c3ae9…7883` | 2 | ✅ healthy |
| V-W | `0x40fad7b4…eb6d` | 2 | ✅ healthy |

**5/5 multisig contracts responding and healthy. All require 2-of-N signatures.**

### MNX Markets (testnet.mnx.fi)

testnet.mnx.fi is a Next.js SPA. No REST endpoints exposed at `/api/markets` or `/api/v1/markets`. Browser JS required for data extraction. **Status: unavailable via curl — no market data captured.**

---

## DuckDB Schema

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

| Table | Rows |
|-------|------|
| world_increments | 101 |
| repo_snapshots | 78 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

---

## Notable Highlights

- **kubeflow/kubeflow**: 15,798⭐ — flagship ML Kubernetes platform
- **kubeflow/pipelines**: 4,171⭐ — pushed today (2026-07-30)
- **kubeflow/spark-operator**: 3,142⭐ — pushed today
- **kubeflow/trainer**: 2,163⭐ — pushed today
- **migalkin/NodePiece**: 144⭐ — compositional KG embeddings (ICLR'22)
- **AustinCStone/TextGAN**: 92⭐ — TensorFlow text GAN
- **bmorphism/ocaml-mcp-sdk**: 61⭐ — OCaml MCP SDK using Jane Street's oxcaml_effect
- **plurigrid/gorj**: This repo — 1521 open issues, pushed today
- **All 5 multisig pairs healthy** — 2-of-N consensus intact
- **All 28 Hamming swarm addresses** — CoinStore unregistered on Aptos mainnet (0 APT each)
