# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-04

## Sweep Metadata
- **Date:** 2026-06-04
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Table | Rows |
|-------|------|
| world_increments | 11 |
| repo_snapshots | 210 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — All 11 Increments

| ID | Source | Type | Event | GF3 Trit | Color | Name |
|----|--------|------|-------|----------|-------|------|
| 1 | plurigrid | org | repo_sweep | 1 PLUS | `#b8bb26` | **PLUS** |
| 2 | kubeflow | org | repo_sweep | -1 MINUS | `#cc241d` | **MINUS** |
| 3 | TeglonLabs | org | repo_sweep | 0 ERGODIC | `#d3869b` | **ERGODIC** |
| 4 | bmorphism | user | repo_sweep | 1 PLUS | `#b8bb26` | **PLUS** |
| 5 | zubyul | user | repo_sweep | -1 MINUS | `#cc241d` | **MINUS** |
| 6 | migalkin | user | social_graph | 0 ERGODIC | `#d3869b` | **ERGODIC** |
| 7 | DJedamski | user | social_graph | 1 PLUS | `#b8bb26` | **PLUS** |
| 8 | wasita | user | social_graph | -1 MINUS | `#cc241d` | **MINUS** |
| 9 | kristinezheng | user | social_graph | 0 ERGODIC | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | social_graph | 1 PLUS | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | social_graph | -1 MINUS | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

### Top Repos by Stars

| Org/User | Repo | Stars | Language |
|----------|------|-------|----------|
| kubeflow | kubeflow | 15,704 | — |
| kubeflow | pipelines | 4,152 | Python |
| kubeflow | spark-operator | 3,124 | Python |
| kubeflow | trainer | 2,110 | Go |
| kubeflow | katib | 1,685 | Python |
| kubeflow | examples | 1,462 | Jsonnet |
| kubeflow | manifests | 1,020 | YAML |
| kubeflow | arena | 811 | Go |
| kubeflow | kale | 690 | Python |
| kubeflow | mpi-operator | 528 | Go |
| AustinCStone | TextGAN | 92 | Python |
| migalkin | NodePiece | 144 | Python |
| migalkin | StarE | 89 | Python |
| bmorphism | ocaml-mcp-sdk | 61 | OCaml |
| plurigrid | asi | 25 | HTML |
| migalkin | kgcourse2021 | 25 | HTML |
| bmorphism | anti-bullshit-mcp-server | 23 | JavaScript |
| bmorphism | risc0-cosmwasm-example | 23 | Rust |
| bmorphism | say-mcp-server | 20 | JavaScript |
| plurigrid | gorj | 0 | Clojure (345 open issues!) |

### Repo Counts by Source (2026-06-04 snapshot)

| Source | Type | Repos Indexed |
|--------|------|---------------|
| plurigrid | org | 59 |
| kubeflow | org | 25 |
| TeglonLabs | org | 4 |
| bmorphism | user | 30 |
| zubyul | user | 20 |
| migalkin | social_graph | 19 |
| AustinCStone | social_graph | 20 |
| wasita | social_graph | 11 |
| DJedamski | social_graph | 6 |
| kristinezheng | social_graph | 6 |
| M1shaaa | social_graph | 8 |
| **TOTAL** | | **208** |

### Notable Highlights
- **kubeflow/kubeflow**: 15,704★ — flagship ML platform for Kubernetes (pushed 2026-05-24)
- **kubeflow/pipelines**: 4,152★ — ML Pipelines (pushed 2026-06-04)
- **plurigrid/gorj**: 0★ but 345 open issues — this very repo
- **bmorphism/Gay.jl**: 1★, 189 open issues — Wide-gamut GF(3) color sampling
- **bmorphism/ocaml-mcp-sdk**: 61★ — OCaml MCP SDK using Jane Street oxcaml_effect
- **migalkin/NodePiece**: 144★ — Knowledge graph embeddings (ICLR'22)
- **AustinCStone/TextGAN**: 92★ — text generation with GANs (TensorFlow)
- **plurigrid/asi**: 25★ — topological chemputer

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses (alice, bob, A–Z) queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793ac… | 0.0 |
| bob | 0x0a3c00… | 0.0 |
| A–Z (26 wallets) | 0x8699ed…–0x7af0ef… | 0.0 each |

**Total swarm APT:** 0.0 APT across all 28 addresses (CoinStore not registered / empty)

### Multisig Contract Probes

Probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f4… | 2 | ✓ |
| A-G | 0xf56c4a… | 2 | ✓ |
| Y-Z | 0xd3ffe1… | 2 | ✓ |
| S-T | 0x3b1c3a… | 2 | ✓ |
| V-W | 0x40fad7… | 2 | ✓ |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed.**

### MNX Markets

`https://testnet.mnx.fi` — Next.js SPA, all REST paths return HTML. Market data unavailable via direct probing. `mnx_snapshots` table is empty.

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
