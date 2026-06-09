# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-09  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** v1.5.3 (Variegata) — `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| source | type | repos | total ★ | latest push |
|---|---|---|---|---|
| kubeflow | org | 48 | 34,192 | 2026-06-09 |
| migalkin | user | 5 | 276 | 2026-05-28 |
| bmorphism | user | 12 | 191 | 2026-06-05 |
| AustinCStone | user | 6 | 106 | 2026-04-01 |
| plurigrid | org | 100 | 76 | 2026-06-09 |
| zubyul | user | 8 | 7 | 2026-04-13 |
| wasita | user | 5 | 5 | 2026-06-01 |
| DJedamski | user | 4 | 3 | 2023-04-21 |
| TeglonLabs | org | 5 | 2 | 2026-06-08 |
| kristinezheng | user | 3 | 0 | 2026-06-07 |
| M1shaaa | user | 3 | 0 | 2026-02-04 |
| **TOTAL** | | **199** | **34,857** | |

### Top 15 Repos by Stars

| repo | language | ★ | forks |
|---|---|---|---|
| kubeflow/kubeflow | — | 15,713 | 2,672 |
| kubeflow/pipelines | Python | 4,153 | 2,004 |
| kubeflow/spark-operator | Python | 3,126 | 1,488 |
| kubeflow/trainer | Go | 2,112 | 963 |
| kubeflow/katib | Python | 1,685 | 525 |
| kubeflow/examples | Jsonnet | 1,462 | 756 |
| kubeflow/manifests | YAML | 1,022 | 1,065 |
| kubeflow/arena | Go | 812 | 190 |
| kubeflow/kale | Python | 692 | 155 |
| kubeflow/mpi-operator | Go | 528 | 235 |
| kubeflow/fairing | Jsonnet | 337 | 143 |
| kubeflow/pytorch-operator | Jsonnet | 310 | 143 |
| kubeflow/community | Jupyter Notebook | 194 | 258 |
| kubeflow/website | HTML | 184 | 923 |
| kubeflow/kfp-tekton | TypeScript | 182 | 123 |

### GF(3) Color Chain — 13 World Increments

| id | source | trit | color | name |
|---|---|---|---|---|
| 1 | plurigrid (org) | 0 | #d3869b | ERGODIC |
| 2 | kubeflow (org) | 1 | #b8bb26 | PLUS |
| 3 | TeglonLabs (org) | -1 | #cc241d | MINUS |
| 4 | bmorphism (user) | 0 | #d3869b | ERGODIC |
| 5 | zubyul (user) | 1 | #b8bb26 | PLUS |
| 6 | migalkin (user) | -1 | #cc241d | MINUS |
| 7 | DJedamski (user) | 0 | #d3869b | ERGODIC |
| 8 | wasita (user) | 1 | #b8bb26 | PLUS |
| 9 | kristinezheng (user) | -1 | #cc241d | MINUS |
| 10 | M1shaaa (user) | 0 | #d3869b | ERGODIC |
| 11 | AustinCStone (user) | 1 | #b8bb26 | PLUS |
| 12 | bmorphism (user/events) | -1 | #cc241d | MINUS |
| 13 | zubyul (user/events) | 0 | #d3869b | ERGODIC |

GF(3) rule: `id%3==0 → ERGODIC #d3869b` · `id%3==1 → PLUS #b8bb26` · `id%3==2 → MINUS #cc241d`

### Notable Highlights

- **kubeflow/kubeflow**: 15,713 ★ — flagship ML platform for Kubernetes (active 2026-06-09)
- **kubeflow/mcp-apache-spark-history-server**: 174 ★ — new MCP server for Spark debugging
- **migalkin/NodePiece**: 144 ★ — ICLR'22 compositional KG representations
- **bmorphism/ocaml-mcp-sdk**: 61 ★ — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 ★ — text generation GANs (TF)
- **plurigrid/asi**: 25 ★ — "everything is topological chemputer!" (HTML)
- **TeglonLabs/jank-crane**: C++ IR hub pushed 2026-06-08 (most recent TeglonLabs activity)
- **zubyul/tilelang-kernels**: TileLang GPU kernels for SplitMix64 + GF(3) trit classification

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

28 addresses probed on Aptos mainnet (ledger version 5,654,076,996).

All accounts returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — these addresses have not initialized an APT coin store. **Balance: 0.0 APT for all 28 addresses** (alice, bob, A–Z).

| world | address | balance |
|---|---|---|
| alice | 0xc793...cc7b | 0.0 APT |
| bob | 0x0a3c...2d5d | 0.0 APT |
| A–Z (26) | 0x8699...→0x7af0... | 0.0 APT each |

### Multisig Contract Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`. All **healthy** — 2-of-N threshold.

| pair | address | sigs required | status |
|---|---|---|---|
| A-B | 0x0da4f428...7003 | 2 | ✅ healthy |
| A-G | 0xf56c4a1c...0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ffe181...b883 | 2 | ✅ healthy |
| S-T | 0x3b1c3ae9...7883 | 2 | ✅ healthy |
| V-W | 0x40fad7b4...eb6d | 2 | ✅ healthy |

### MNX Markets

`https://testnet.mnx.fi` — **Vercel authentication required**. Market data unavailable without credentials. `mnx_snapshots` table: 0 rows.

---

## DuckDB Schema

```sql
world_increments  -- 13 rows (GF3 color chain sweep events)
repo_snapshots    -- 199 rows (11 orgs/users, 3 orgs + 8 users)
aptos_snapshots   -- 28 rows  (alice, bob, A–Z)
multisig_probes   -- 5 rows   (A-B, A-G, Y-Z, S-T, V-W, all 2-of-N healthy)
mnx_snapshots     -- 0 rows   (Vercel auth gated)
```

GF(3) assignment rule:
- `id mod 3 == 0` → trit=0, color=#d3869b, name=**ERGODIC**
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=**MINUS**
