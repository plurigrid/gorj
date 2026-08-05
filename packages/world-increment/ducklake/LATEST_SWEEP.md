# World-Increment Sweep + Hamming Swarm Snapshot — 2026-08-05

## Sweep Metadata
- **Date:** 2026-08-05
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 58 |
| Total Repo Snapshots | 58 |
| Sources Covered | 3 orgs + 8 users |

### Sources Queried

| Source | Type | Repos Found | Top Star Count |
|--------|------|-------------|----------------|
| plurigrid | Org | 103 (100 returned) | 59 (asi) |
| kubeflow | Org | 49 | 15,805 (kubeflow/kubeflow) |
| TeglonLabs | Org | 5 | 2 (mathpix-gem) |
| bmorphism | User | 106 | 61 (ocaml-mcp-sdk) |
| zubyul | User | 49 | 1 (gay-world) |
| migalkin | Social | 19 | 144 (NodePiece) |
| DJedamski | Social | 6 | 1 |
| wasita | Social | 14 | 2 (magic-garden) |
| kristinezheng | Social | 5 | 0 |
| M1shaaa | Social | 8 | 0 |
| AustinCStone | Social | 41 | 92 (TextGAN) |

### Notable Highlights

- **plurigrid/gorj** (this repo): 1,646 open issues — most of any plurigrid repo; pushed today 2026-08-05
- **plurigrid/asi**: 59 stars, HTML, "everything is topological chemputer!", pushed 2026-07-10
- **kubeflow/kubeflow**: 15,805 stars, 2,692 forks — flagship ML-on-Kubernetes platform
- **kubeflow/pipelines**: active today (2026-08-04), 4,177 stars, 519 open issues
- **kubeflow/spark-operator**: active today (2026-08-05), 3,143 stars
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml MCP SDK using Jane Street oxcaml_effect
- **bmorphism/anti-bullshit-mcp-server**: 23 stars, active 2026-08-02
- **wasita/xoxowasita-analysis**: created yesterday 2026-08-04
- **TeglonLabs/jank-crane**: C++, crane-jank converged-IR hub with GF3 convergence maps

### GF(3) Color Chain — Top Increments

| ID | Trit | Color | Name | Source | Repo |
|---|---|---|---|---|---|
| 1 | 1 | #b8bb26 | PLUS | plurigrid | asi |
| 2 | 2 | #cc241d | MINUS | plurigrid | ontology |
| 3 | 0 | #d3869b | ERGODIC | plurigrid | vcg-auction |
| 4 | 1 | #b8bb26 | PLUS | plurigrid | agent |
| 5 | 2 | #cc241d | MINUS | plurigrid | StochFlow |
| 6 | 0 | #d3869b | ERGODIC | plurigrid | microworlds |
| 7 | 1 | #b8bb26 | PLUS | plurigrid | gorj |
| 8 | 2 | #cc241d | MINUS | plurigrid | place |
| 9 | 0 | #d3869b | ERGODIC | plurigrid | zig-syrup |
| 10 | 1 | #b8bb26 | PLUS | plurigrid | nash-portal |
| ... | | | | | |
| 58 | 1 | #b8bb26 | PLUS | AustinCStone | byteruckus |

GF(3) rule: `id%3==0 → ERGODIC #d3869b`, `id%3==1 → PLUS #b8bb26`, `id%3==2 → MINUS #cc241d`

### Top Repos by Source (Selected)

#### plurigrid (103 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 59 | 2026-07-10 |
| zig-syrup | Zig | 2 | 2026-07-28 |
| gorj | Clojure | 1 | 2026-08-05 |
| place | TeX | 1 | 2026-08-02 |
| nash-portal | Rust | 2 | 2026-05-19 |

#### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,805 | 2026-07-10 |
| pipelines | Python | 4,177 | 2026-08-04 |
| spark-operator | Python | 3,143 | 2026-08-05 |
| trainer | Go | 2,170 | 2026-08-04 |
| katib | Python | 1,694 | 2026-08-05 |

#### bmorphism (106 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-08-02 |
| say-mcp-server | JavaScript | 20 | 2026-03-19 |
| babashka-mcp-server | JavaScript | 19 | 2026-06-05 |
| Gay.jl | Julia | 2 | 2026-07-21 |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances

All 28 wallets probed against `fullnode.mainnet.aptoslabs.com`.

**Total APT across all 28 wallets: 0.0 APT**

All wallets returned zero balance (CoinStore resource present, value=0).

| World | Balance (APT) |
|-------|---------------|
| alice | 0.0 |
| bob | 0.0 |
| A–Z (26 wallets) | 0.0 each |

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4f4...87003 | 2 | ✓ |
| A-G | 0xf56c4a...0096 | 2 | ✓ |
| Y-Z | 0xd3ffe1...b883 | 2 | ✓ |
| S-T | 0x3b1c3a...7883 | 2 | ✓ |
| V-W | 0x40fad7...eb6d | 2 | ✓ |

**All 5 multisig contracts healthy — 2-of-2 threshold confirmed across all pairs.**

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — `testnet.mnx.fi` is a Next.js SPA. Root and `/markets` return HTTP 200 HTML; no JSON API endpoints respond (all return 404). Market data cannot be extracted without JS execution. `mnx_snapshots` table empty for this sweep.

---

## DuckDB Ducklake

**Location:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| `world_increments` | 58 |
| `repo_snapshots` | 58 |
| `aptos_snapshots` | 28 |
| `multisig_probes` | 5 |
| `mnx_snapshots` | 0 (SPA unavailable) |

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
