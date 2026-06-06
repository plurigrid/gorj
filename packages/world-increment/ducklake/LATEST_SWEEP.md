# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-06

## Sweep Metadata
- **Date:** 2026-06-06
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (This Sweep)

| Metric | Value |
|--------|-------|
| New Repo Snapshots | 380 (plurigrid/kubeflow/TeglonLabs/zubyul/bmorphism/migalkin/DJedamski/wasita/kristinezheng/M1shaaa/AustinCStone) |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (Vercel auth) |
| Cumulative World Increments | 381 |
| Cumulative Repo Snapshots | 1302 |

---

## GF(3) Color Chain

GF(3) assignment: `id%3==0` → trit=0 `#d3869b` ERGODIC | `id%3==1` → trit=1 `#b8bb26` PLUS | `id%3==2` → trit=-1 `#cc241d` MINUS

| Color | Name | Count (cumulative) |
|-------|------|-------------------|
| `#d3869b` | ERGODIC | 127 |
| `#b8bb26` | PLUS | 127 |
| `#cc241d` | MINUS | 127 |

---

## JOB 1: GitHub Social Graph Sweep

### Repos This Sweep by Source

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 100 (of 101) |
| kubeflow | org | 48 |
| bmorphism | user | 100 (of 103) |
| zubyul | user | 49 |
| AustinCStone | social | 30 (of 40) |
| migalkin | social | 19 |
| wasita | social | 11 |
| M1shaaa | social | 8 |
| TeglonLabs | org | 4 |
| kristinezheng | social | 5 |
| DJedamski | social | 6 |

### Top Active Repos (open issues)

| Repo | Stars | Open Issues | Language | Pushed |
|------|-------|-------------|----------|--------|
| kubeflow/pipelines | 4152 | 491 | Python | 2026-06-06 |
| plurigrid/gorj | 0 | 395 | Clojure | 2026-06-06 |
| kubeflow/docs-agent | 37 | 151 | Python | 2026-04-14 |
| kubeflow/sdk | 120 | 137 | Python | 2026-06-04 |
| kubeflow/trainer | 2111 | 123 | Go | 2026-06-05 |
| kubeflow/katib | 1685 | 120 | Python | 2026-06-05 |
| bmorphism/Gay.jl | 1 | 189 | Julia | 2026-06-06 |
| kubeflow/fairing | 337 | 134 | Jsonnet | 2022-04-11 |
| kubeflow/examples | 1462 | 111 | Jsonnet | 2025-04-14 |

### Top Starred Repos (new data)

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15706 | — |
| kubeflow/pipelines | 4152 | Python |
| kubeflow/spark-operator | 3125 | Python |
| kubeflow/trainer | 2111 | Go |
| kubeflow/katib | 1685 | Python |
| kubeflow/examples | 1462 | Jsonnet |
| kubeflow/arena | 811 | Go |
| kubeflow/kale | 691 | Python |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| plurigrid/asi | 25 | HTML |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |
| bmorphism/risc0-cosmwasm-example | 23 | Rust |
| bmorphism/say-mcp-server | 20 | JavaScript |
| bmorphism/babashka-mcp-server | 19 | JavaScript |

### Notable Activity

- **plurigrid/gorj** pushed TODAY (2026-06-06) — this repo itself, 395 open issues, Clojure
- **kubeflow/pipelines** pushed TODAY — 4152 stars, 491 open issues
- **bmorphism/Gay.jl** pushed TODAY — wide-gamut color sampling, 189 open issues
- **bmorphism/ocaml-mcp-sdk** (61 stars) — OCaml MCP SDK using Jane Street's oxcaml_effect
- **zubyul/tilelang-kernels** — TileLang GPU kernels for GF(3) trit classification

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 wallets (alice, bob, A–Z) returned **0.0 APT** on mainnet. The `CoinStore<0x1::aptos_coin::AptosCoin>` resource was not found for any address — wallets are either unfunded or use non-native token stores.

### Multisig Contracts — All 5 Healthy ✅

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✅ live |
| A-G | 0xf56c...096 | 2 | ✅ live |
| Y-Z | 0xd3ff...883 | 2 | ✅ live |
| S-T | 0x3b1c...883 | 2 | ✅ live |
| V-W | 0x40fa...b6d | 2 | ✅ live |

All 5 multisig contracts exist on Aptos mainnet and require 2-of-2 signatures. Network is healthy.

### MNX Markets

**Unavailable** — `testnet.mnx.fi` is behind Vercel deployment protection. API paths `/api/markets`, `/api/v1/markets`, `/api/v1/tickers` all return auth-required HTML. No market data extractable without a bypass token.

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
