# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-11

## Sweep Metadata
- **Date:** 2026-05-11
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 115 |
| Total Repo Snapshots | 115 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 19 |
| kubeflow | org | 19 |
| bmorphism | user | 19 |
| zubyul | user | 15 |
| wasita | social graph | 8 |
| M1shaaa | social graph | 7 |
| AustinCStone | social graph | 7 |
| kristinezheng | social graph | 6 |
| migalkin | social graph | 6 |
| DJedamski | social graph | 5 |
| TeglonLabs | org | 4 |
| **TOTAL** | | **115** |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 38 |
| +1 | `#b8bb26` | PLUS | 39 |
| -1 | `#cc241d` | MINUS | 38 |

GF(3) chain: `ERGODIC(0) → PLUS(+1) → MINUS(-1) → ERGODIC(0) → …` cycling 115 times.

### Top Starred Repos (across all sources)

| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| kubeflow/kubeflow | — | 15,630 | 2026-05-07 |
| kubeflow/pipelines | Python | 4,138 | 2026-05-11 |
| kubeflow/spark-operator | Python | 3,125 | 2026-05-08 |
| kubeflow/trainer | Go | 2,097 | 2026-05-09 |
| kubeflow/katib | Python | 1,683 | 2026-05-09 |
| kubeflow/examples | Jsonnet | 1,462 | 2025-04-14 |
| kubeflow/manifests | YAML | 1,016 | 2026-05-08 |
| kubeflow/arena | Go | 810 | 2026-05-07 |
| kubeflow/kale | Python | 684 | 2026-05-09 |
| kubeflow/mpi-operator | Go | 526 | 2026-05-05 |
| migalkin/NodePiece | Python | 144 | 2022-02-02 |
| AustinCStone/TextGAN | Python | 92 | 2016-10-04 |
| migalkin/StarE | Python | 89 | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| plurigrid/asi | HTML | 21 | 2026-04-26 |

### Most Recently Pushed

| Repo | Pushed At |
|------|-----------|
| plurigrid/gorj | 2026-05-11T15:15:59Z |
| kubeflow/dashboard | 2026-05-11T16:07:41Z |
| bmorphism/Gay.jl | 2026-05-11T07:33:59Z |
| M1shaaa/M1shaaa | 2026-05-11T14:42:08Z |
| kubeflow/blog | 2026-05-11T15:21:33Z |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A–Z) returned `resource_not_found` for `CoinStore<AptosCoin>`.
Coin stores are not initialized on mainnet — **0.00 APT each**.

| World | Address | Balance (APT) |
|-------|---------|--------------|
| alice | 0xc793ac...cc7b | 0.0 |
| bob | 0x0a3c00...2d5d | 0.0 |
| A | 0x8699ed...9d7a | 0.0 |
| B | 0x3f892e...b13 | 0.0 |
| C–Z (24) | … | 0.0 each |

### Multisig Contract Probes

Function: `0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f4...7003 | **2** | ✅ HEALTHY |
| A-G | 0xf56c4a...0096 | **2** | ✅ HEALTHY |
| Y-Z | 0xd3ffe1...b883 | **2** | ✅ HEALTHY |
| S-T | 0x3b1c3a...7883 | **2** | ✅ HEALTHY |
| V-W | 0x40fad7...eb6d | **2** | ✅ HEALTHY |

All 5 multisig accounts active on mainnet, requiring **2-of-N** signatures.

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` → HTTP 200 (SPA). Probed `/api/markets`, `/api/v1/markets`, `/markets`,
`/api/tokens`, `/api/v1/tokens` — no JSON API discovered.  
**Status: unavailable** (frontend SPA only, no REST endpoint).

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

## GF(3) Assignment Rule

- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS

## Notable Highlights

- **kubeflow/kubeflow**: 15,630 stars — flagship ML toolkit for Kubernetes (active 2026-05-11)
- **kubeflow/pipelines**: 4,138 stars — most active ML pipeline on Kubernetes
- **plurigrid/gorj**: This repo — forj + GF(3) trit coloring, 151 open issues, pushed today
- **bmorphism/Gay.jl**: 188 open issues, wide-gamut SPI color sampling, pushed today
- **migalkin/NodePiece**: 144 stars — ICLR'22 compositional KG representations
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml MCP SDK via Jane Street oxcaml_effect
- **All 5 multisig pairs**: healthy on Aptos mainnet, 2-of-N threshold confirmed
