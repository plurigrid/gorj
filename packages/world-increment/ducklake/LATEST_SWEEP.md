# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-12  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social (zubyul graph) | 19 |
| DJedamski | social (zubyul graph) | 6 |
| wasita | social (zubyul graph) | 11 |
| kristinezheng | social (zubyul graph) | 5 |
| M1shaaa | social (zubyul graph) | 8 |
| AustinCStone | social (zubyul graph) | 40 |
| **TOTAL** | | **391** |

### GF(3) Color Chain Distribution

| GF3 Name | Trit | Color | Count |
|----------|------|-------|-------|
| ERGODIC | 0 | `#d3869b` | 130 |
| MINUS | -1 | `#cc241d` | 130 |
| PLUS | 1 | `#b8bb26` | 131 |

### Top Repos by Stars

| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| kubeflow/kubeflow | — | 15,714 | 2026-06-11 |
| kubeflow/pipelines | Python | 4,152 | 2026-06-11 |
| kubeflow/spark-operator | Python | 3,127 | 2026-06-09 |
| kubeflow/trainer | Go | 2,111 | 2026-06-12 |
| kubeflow/katib | Python | 1,683 | 2026-06-05 |
| kubeflow/examples | Jsonnet | 1,461 | 2025-04-14 |
| kubeflow/manifests | YAML | 1,022 | 2026-06-09 |
| kubeflow/arena | Go | 812 | 2026-05-07 |
| kubeflow/kale | Python | 692 | 2026-06-10 |
| kubeflow/mpi-operator | Go | 528 | 2026-06-02 |

### Top Languages

| Language | Repos |
|----------|-------|
| Python | 81 |
| Rust | 26 |
| JavaScript | 25 |
| TypeScript | 23 |
| Go | 15 |
| HTML | 15 |
| Clojure | 14 |
| Jupyter Notebook | 14 |
| Julia | 9 |
| Zig | 7 |

### Notable Plurigrid Activity

- `plurigrid/gorj` — 513 open issues (most active); forj + Rama topology nREPL routing
- `plurigrid/eirobri` — 29 open issues; EiRoBri replay world
- `plurigrid/asi` — 25 stars; topological chemputer

### Notable bmorphism Activity

- `bmorphism/Gay.jl` — 189 open issues; wide-gamut color sampling with splittable determinism
- `bmorphism/ocaml-mcp-sdk` — 61 stars; OCaml SDK for Model Context Protocol
- `bmorphism/vibesnipe-market` — 9 open issues (Move)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (coin::balance view — mainnet)

**Total APT across swarm: 20.344773 APT**

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| bob | 0x0a3c...512d | 12.657007 |
| F | 0x18a1...cf71 | 1.960516 |
| L | 0x7c2e...eba9 | 1.927269 |
| J | 0x4d96...7f54 | 1.895093 |
| alice | 0xc793...cc7b | 0.436434 |
| O | 0x7325...89d | 0.210136 |
| K | 0xa732...dc4 | 0.161961 |
| P | 0x6218...948 | 0.140136 |
| M | 0x6fed...f2e9 | 0.112285 |
| N | 0xe7dd...1b2c | 0.106121 |
| Q | 0xac40...89a9 | 0.103240 |
| S | 0xb875...0386 | 0.091788 |
| R | 0x7ce6...6e10 | 0.090217 |
| T | 0x3578...4588 | 0.073713 |
| U | 0x7586...9956 | 0.055773 |
| A | 0x8699...9d7a | 0.051767 |
| V | 0xb59d...f2c3 | 0.048833 |
| Y | 0xd8e3...44c4 | 0.044449 |
| X | 0xa95c...047d | 0.042577 |
| W | 0x5f32...c7b0 | 0.040705 |
| B | 0x3f89...b13 | 0.036256 |
| Z | 0x7af0...197c | 0.024268 |
| D | 0xf776...fdd1 | 0.011629 |
| C | 0x38b9...535e | 0.010185 |
| E | 0xdc1d...8d36 | 0.009372 |
| H | 0xce67...300f | 0.001681 |
| G | 0x69a3...f32 | 0.000681 |
| I | 0x070f...1fc9 | 0.000681 |

### Multisig Contract Probes

All 5 multisig contracts healthy — 2 signatures required each.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` returns HTTP 401 (Vercel password protection). No market data retrievable without credentials.

---

## DuckDB Schema Summary

```sql
world_increments    -- 391 rows (GF3 color-chained repo events)
repo_snapshots      -- 391 rows (full repo metadata)
aptos_snapshots     -- 28 rows (wallet balances, total 20.344773 APT)
multisig_probes     -- 5 rows (2-of-N contracts, all healthy)
mnx_snapshots       -- 0 rows (testnet.mnx.fi unavailable)
```

## Sweep Metadata

- **Timestamp:** 2026-06-12T02:20Z
- **Aptos Ledger:** ~5,691,271,301 (epoch 16142, block 825,365,606)
- **GF3 chain:** id%3==0 → ERGODIC (#d3869b) | id%3==1 → PLUS (#b8bb26) | id%3==2 → MINUS (#cc241d)
