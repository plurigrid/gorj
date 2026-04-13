# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-13

## Sweep Metadata
- **Date:** 2026-04-13T05:42Z
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## GF(3) Color Chain

| Trit | Color | Name | Rule |
|------|-------|------|------|
| 0 | `#d3869b` | ERGODIC | id % 3 == 0 |
| +1 | `#b8bb26` | PLUS | id % 3 == 1 |
| -1 | `#cc241d` | MINUS | id % 3 == 2 |

---

## JOB 1: GitHub Social Graph Sweep

### World Increments Added (IDs 13–33)

| ID | Source | Type | Repos | GF(3) | Color |
|----|--------|------|-------|-------|-------|
| 13 | plurigrid | org | 100 | PLUS | `#b8bb26` |
| 14 | kubeflow | org | 47 | MINUS | `#cc241d` |
| 15 | TeglonLabs | org | 53 | ERGODIC | `#d3869b` |
| 16 | bmorphism | user | 100 | PLUS | `#b8bb26` |
| 17 | zubyul | user | 24 | MINUS | `#cc241d` |
| 18 | migalkin | user | 30 | ERGODIC | `#d3869b` |
| 19 | DJedamski | user | 11 | PLUS | `#b8bb26` |
| 20 | wasita | user | 31 | MINUS | `#cc241d` |
| 21 | kristinezheng | user | 18 | ERGODIC | `#d3869b` |
| 22 | M1shaaa | user | 16 | PLUS | `#b8bb26` |
| 23 | AustinCStone | user | 43 | MINUS | `#cc241d` |
| 24–28 | bmorphism events | event | 5 events | ERGODIC/PLUS/MINUS | rolling |
| 29–33 | zubyul events | event | 5 events | PLUS/MINUS/ERGODIC | rolling |

**GF(3) distribution this sweep:** ERGODIC×7, PLUS×7, MINUS×7 — perfectly balanced

### Repo Counts by Source (this sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 47 |
| AustinCStone | user | 43 |
| wasita | user | 31 |
| migalkin | user | 30 |
| zubyul | user | 24 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| **TOTAL NEW** | | **473** |

### Top 10 Stars (this sweep)

| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15,569 | — | 2026-01 |
| kubeflow/pipelines | 4,118 | Python | 2026-04-10 |
| kubeflow/spark-operator | 3,112 | Python | 2026-04-10 |
| kubeflow/trainer | 2,080 | Go | 2026-04-10 |
| kubeflow/katib | 1,677 | Python | 2026-04-02 |
| kubeflow/examples | 1,459 | Jsonnet | — |
| kubeflow/manifests | 1,010 | YAML | — |
| kubeflow/arena | 808 | Go | — |
| kubeflow/kale | 683 | Python | — |
| kubeflow/mpi-operator | 523 | Go | — |

### Language Distribution (this sweep)

| Language | Repos |
|----------|-------|
| Python | 77 |
| HTML | 18 |
| Go | 18 |
| Rust | 15 |
| JavaScript | 14 |
| Jupyter Notebook | 13 |
| TypeScript | 12 |
| Clojure | 8 |
| R | 8 |
| Jsonnet | 8 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

> Method: `0x1::coin::balance` view function — `POST /v1/view`  
> 1s sleep between calls. Total: 28 addresses (alice, bob, A–Z).

| World | Address | Balance (APT) |
|-------|---------|---------------|
| bob | `0x0a3c...512d` | **12.657007** |
| F | `0x18a1...cf71` | 1.960516 |
| L | `0x7c2e...eba9` | 1.927269 |
| J | `0x4d96...7f54` | 1.895093 |
| alice | `0xc793...cc7b` | 0.436434 |
| O | `0x7325...a89d` | 0.210136 |
| K | `0xa732...25dc4` | 0.161961 |
| P | `0x6218...c948` | 0.140136 |
| M | `0x6fed...f2e9` | 0.112285 |
| N | `0xe7dd...1b2c` | 0.106121 |
| Q | `0xac40...c89a9` | 0.103240 |
| S | `0xb875...0386` | 0.091788 |
| R | `0x7ce6...6e10` | 0.090217 |
| T | `0x3578...4588` | 0.073713 |
| U | `0x7586...9956` | 0.055773 |
| A | `0x8699...cc7b` | 0.051767 |
| V | `0xb59d...f2c3` | 0.048833 |
| Y | `0xd8e3...44c4` | 0.044449 |
| X | `0xa95c...047d` | 0.042577 |
| W | `0x5f32...c7b0` | 0.040705 |
| B | `0x3f89...cb13` | 0.036256 |
| Z | `0x7af0...197c` | 0.024268 |
| D | `0xf776...fdd1` | 0.011629 |
| C | `0x38b9...535e` | 0.010185 |
| E | `0xdc1d...8d36` | 0.009372 |
| H | `0xce67...300f` | 0.001681 |
| I | `0x070f...1fc9` | 0.000681 |
| G | `0x69a3...7f32` | 0.000681 |

**Total APT in swarm:** ~20.92 APT  
**Richest:** bob (12.657 APT, 60.5% of total)  
**Note:** `alice` is a deployed contract account (sequence_number=72, holds `MultiverseState`, `address_book`, lending position)

### Multisig Contract Probes

All 5 multisig contracts healthy — threshold: **2-of-N**

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4...7003` | 2 | ✓ healthy |
| A-G | `0xf56c...0096` | 2 | ✓ healthy |
| Y-Z | `0xd3ff...b883` | 2 | ✓ healthy |
| S-T | `0x3b1c...7883` | 2 | ✓ healthy |
| V-W | `0x40fa...eb6d` | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

- Root URL: **200 OK** (Next.js SPA, dark theme)
- `/api/markets`, `/api/tickers`, `/api/v1/*`: **404**
- `/graphql`: returns SPA HTML (not a real GraphQL endpoint)
- **Status:** SPA-only frontend — no machine-readable market data accessible

---

## DuckDB Ducklake State (cumulative)

| Table | Rows | Delta |
|-------|------|-------|
| world_increments | 33 | +21 |
| repo_snapshots | 944 | +473 |
| aptos_snapshots | 28 | +28 (new) |
| multisig_probes | 5 | +5 (new) |
| mnx_snapshots | 1 | +1 (new) |

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

## Notable Highlights

- **kubeflow/kubeflow** 15,569★ — flagship ML platform for Kubernetes
- **kubeflow/pipelines** 4,118★ — most popular Kubernetes ML pipeline (active 2026-04-10)
- **bmorphism/ocaml-mcp-sdk** 60★ — OCaml MCP SDK using Jane Street's oxcaml_effect
- **migalkin/NodePiece** 143★ — scalable knowledge graph embeddings (Python)
- **AustinCStone/TextGAN** 92★ — text generation with GANs
- **plurigrid/asi** — topological chemputer (pushed 2026-04-10)
- **GF(3) balance:** 7 ERGODIC + 7 PLUS + 7 MINUS = perfect trit symmetry
- **All 5 multisigs operational** at 2-of-N threshold
- **bob wallet** holds 60.5% of all tracked APT (12.66 of 20.92 total)
