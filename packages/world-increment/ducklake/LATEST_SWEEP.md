# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-21
**Agent:** world-increment-sweep (automated scheduled routine)
**DuckDB version:** v1.5.4
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Orgs & Users Queried

| Entity | Type | Repos This Sweep |
|---|---|---|
| plurigrid | org | 87 |
| kubeflow | org | 29 |
| TeglonLabs | org | 5 |
| zubyul | user | 33 |
| bmorphism | user | 100 |
| migalkin | user | 4 |
| DJedamski | user | 6 |
| wasita | user | 5 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| AustinCStone | user | 8 |
| **Total** | | **278** |

### GF(3) Color Chain Distribution

| Trit | Name | Color | Count (this sweep) |
|---|---|---|---|
| 0 | ERGODIC | `#d3869b` | 99 |
| +1 | PLUS | `#b8bb26` | 101 |
| -1 | MINUS | `#cc241d` | 101 |

Assignment: `id % 3 == 0 → ERGODIC`, `id % 3 == 1 → PLUS`, `id % 3 == 2 → MINUS`

### Top Repos by Stars

| Org/User | Repo | Stars | Language |
|---|---|---|---|
| kubeflow | kubeflow | 15,738 | — |
| kubeflow | pipelines | 4,155 | Python |
| kubeflow | spark-operator | 3,127 | Python |
| kubeflow | trainer | 2,118 | Go |
| kubeflow | katib | 1,683 | Python |
| kubeflow | examples | 1,460 | Jsonnet |
| kubeflow | community-distribution | 1,025 | YAML |
| kubeflow | arena | 813 | Go |
| kubeflow | kale | 694 | Python |
| kubeflow | mpi-operator | 528 | Go |
| migalkin | NodePiece | 144 | Python |
| AustinCStone | TextGAN | 92 | Python |
| migalkin | StarE | 89 | Python |
| bmorphism | ocaml-mcp-sdk | 61 | OCaml |
| plurigrid | asi | 26 | HTML |

### Notable bmorphism Repos

| Repo | Stars | Language | Description |
|---|---|---|---|
| ocaml-mcp-sdk | 61 | OCaml | OCaml MCP SDK |
| anti-bullshit-mcp-server | 23 | JavaScript | Anti-bullshit MCP server |
| risc0-cosmwasm-example | 23 | Rust | CosmWasm + zkVM RISC-V EFI template |
| say-mcp-server | 20 | JavaScript | Say MCP server |
| babashka-mcp-server | 19 | JavaScript | Babashka MCP server |
| manifold-mcp-server | 14 | JavaScript | Manifold MCP server |
| Gay.jl | 2 | Julia | 187 open issues |
| satreadout | — | HTML | Lean 4.28 |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (28 addresses)

| World | Address (truncated) | APT Balance |
|---|---|---|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C–Z | … | 0.0 (all) |

All 28 wallets: **0.0 APT** (no funded CoinStore resources on mainnet).

### Multisig Probes (5 pairs)

| Pair | Address (truncated) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

All 5 multisig contracts: **2-of-N signatures required, all healthy**.  
Probe method: `0x1::multisig_account::num_signatures_required` via POST to `fullnode.mainnet.aptoslabs.com/v1/view`.

### MNX Markets

`testnet.mnx.fi` — Vercel authentication barrier encountered on all paths. No market data extractable.
Status: **UNAVAILABLE**

---

## DuckDB Snapshot Summary

```
world_increments : 301 rows (cumulative across all sweeps)
repo_snapshots   : 1222 rows (cumulative; 278 inserted this sweep)
aptos_snapshots  : 28 rows
multisig_probes  : 5 rows
mnx_snapshots    : 0 rows (MNX unavailable)
```

Path: `packages/world-increment/ducklake/world-increments.duckdb`

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

- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS
