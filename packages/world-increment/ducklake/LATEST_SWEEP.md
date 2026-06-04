# World Increment Sweep — 2026-06-04

Generated: `2026-06-04T00:00:00Z`
DuckDB: `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 50 |
| kubeflow | org | 28 |
| TeglonLabs | org | 4 |
| bmorphism | user | 40 |
| zubyul | user | 33 |
| migalkin | social-graph | 6 |
| wasita | social-graph | 5 |
| kristinezheng | social-graph | 3 |
| DJedamski | social-graph | 3 |
| M1shaaa | social-graph | 3 |
| AustinCStone | social-graph | 11 |

**Total repos this sweep: 186**

### Top Repos by Stars

| Repo | Stars | Forks | Language | Last Push |
|------|-------|-------|----------|-----------|
| kubeflow/kubeflow | 15,705 | 2,669 | — | 2026-05-24 |
| kubeflow/pipelines | 4,152 | 2,004 | Python | 2026-06-04 |
| kubeflow/spark-operator | 3,124 | 1,488 | Python | 2026-06-03 |
| kubeflow/trainer | 2,111 | 964 | Go | 2026-06-04 |
| kubeflow/katib | 1,685 | 525 | Python | 2026-06-04 |
| kubeflow/examples | 1,462 | 756 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,020 | 1,065 | YAML | 2026-06-04 |
| kubeflow/arena | 811 | 191 | Go | 2026-05-07 |
| kubeflow/kale | 690 | 155 | Python | 2026-06-04 |
| kubeflow/mpi-operator | 528 | 235 | Go | 2026-06-02 |
| migalkin/NodePiece | 144 | 21 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | 30 | Python | 2025-03-03 |
| migalkin/StarE | 89 | 16 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | 2 | OCaml | 2026-03-16 |
| plurigrid/asi | 25 | 6 | HTML | 2026-04-26 |
| bmorphism/anti-bullshit-mcp-server | 23 | 7 | JavaScript | 2026-01-16 |

### Notable Observations

- **plurigrid/gorj** (this repo) has 352 open issues — highest in plurigrid org by far
- **bmorphism/Gay.jl** has 189 open issues; heavy GF(3)/splittable-determinism work
- **kubeflow** remains the dominant star attractor (15k+ on main repo)
- **bmorphism** is active across OCaml, Zig, Move, Clojure, Julia — polyglot MCP/OCapN work
- **zubyul** focused on BCI, Nash TUI, Ghostty, Gay.jl integrations — close orbit of plurigrid
- **AustinCStone** has `bmfork`/`bmforkupdate` repos — explicit bmorphism fork lineage
- **TeglonLabs** active on Ruby/JS with `mathpix-gem` (11 issues, security-first math OCR)

### GF(3) Color Chain Distribution (this run)

| Trit | Name | Hex | Count |
|------|------|-----|-------|
| 0 | ERGODIC | #d3869b | 62 |
| 1 | PLUS | #b8bb26 | 62 |
| -1 | MINUS | #cc241d | 62 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Hamming Swarm A–Z + alice/bob)

**28 addresses probed** via Aptos mainnet `fullnode.mainnet.aptoslabs.com/v1`.

All addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` —
the accounts either have no APT balance or have not initialized a CoinStore resource.
Balances recorded as `NULL` in `aptos_snapshots`.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793...cc7b | NULL |
| bob | 0x0a3c...2d5d | NULL |
| A | 0x8699...9d7a | NULL |
| B | 0x3f89...cb13 | NULL |
| C | 0x38b9...535e | NULL |
| D | 0xf776...fdd1 | NULL |
| E–Z | (22 more) | NULL |

### Multisig Contract Probes

All 5 contracts healthy, all requiring **2-of-N signatures**.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: SPA — API unavailable.** All API paths (`/api/markets`, `/api/tickers`, `/api/v1/markets`)
return the Next.js SPA HTML shell (server-side rendered, no JSON endpoints accessible).
`mnx_snapshots` table is empty this sweep.

---

## DuckDB Schema Summary

| Table | Rows (this sweep) | Description |
|-------|-------------------|-------------|
| `world_increments` | 186 | GF(3)-colored event log |
| `repo_snapshots` | 186 | Repo metadata by org/user |
| `aptos_snapshots` | 28 | Hamming swarm wallet balances |
| `multisig_probes` | 5 | Multisig threshold checks |
| `mnx_snapshots` | 0 | MNX markets (SPA, no API) |

---

## GF(3) Trit Legend

```
id % 3 == 0  →  trit=0,  ERGODIC  #d3869b  (rose/pink)
id % 3 == 1  →  trit=1,  PLUS     #b8bb26  (yellow-green)
id % 3 == 2  →  trit=-1, MINUS    #cc241d  (red)
```
