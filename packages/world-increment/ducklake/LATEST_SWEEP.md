# World-Increment Sweep — 2026-07-17

## Sweep Metadata
- **Date:** 2026-07-17
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Python API)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| New World Increments (this run) | 12 |
| Total World Increments (all time) | 35 |
| New Repo Snapshots (this run) | 394 |
| Total Repo Snapshots (all time) | 1338 |
| Sources Covered (this run) | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (Vercel auth) |

---

## GF(3) Color Chain — This Run (Increments 13–24)

| ID | Source | Type | Repos | GF3 Trit | Color | Name |
|----|--------|------|-------|-----------|-------|------|
| 13 | plurigrid | org | 100 | +1 | `#b8bb26` | **PLUS** |
| 14 | kubeflow | org | 49 | -1 | `#cc241d` | **MINUS** |
| 15 | bmorphism | user | 100 | 0 | `#d3869b` | **ERGODIC** |
| 16 | zubyul | user | 49 | +1 | `#b8bb26` | **PLUS** |
| 17 | migalkin | user | 19 | -1 | `#cc241d` | **MINUS** |
| 18 | wasita | user | 12 | 0 | `#d3869b` | **ERGODIC** |
| 19 | AustinCStone | user | 41 | +1 | `#b8bb26` | **PLUS** |
| 20 | TeglonLabs | org | 5 | -1 | `#cc241d` | **MINUS** |
| 21 | kristinezheng | user | 5 | 0 | `#d3869b` | **ERGODIC** |
| 22 | M1shaaa | user | 8 | +1 | `#b8bb26` | **PLUS** |
| 23 | DJedamski | user | 6 | -1 | `#cc241d` | **MINUS** |
| 24 | sweep_agent | system | — | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## Top Repos by Stars (This Sweep)

| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,779 | 2026-07-10 |
| kubeflow/pipelines | Python | 4,167 | 2026-07-16 |
| kubeflow/spark-operator | Python | 3,137 | 2026-07-16 |
| kubeflow/trainer | Go | 2,150 | 2026-07-16 |
| kubeflow/katib | Python | 1,690 | 2026-07-16 |
| kubeflow/examples | Jsonnet | 1,460 | 2025-04-14 |
| kubeflow/community-distribution | YAML | 1,029 | 2026-07-16 |
| kubeflow/arena | Go | 815 | 2026-07-16 |
| kubeflow/kale | Python | 696 | 2026-07-16 |
| migalkin/NodePiece | Python | 144 | 2022-02-02 |
| migalkin/StarE | Python | 89 | 2023-12-01 |
| AustinCStone/TextGAN | Python | 92 | 2016-10-04 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| plurigrid/asi | HTML | 30 | 2026-07-10 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 22 | 2026-01-16 |

---

## Source Breakdown (This Run)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| AustinCStone | user | 41 |
| migalkin | user | 19 |
| wasita | user | 12 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user | 5 |
| **TOTAL** | | **394** |

### Notable New Repos Since Last Sweep

- **plurigrid/gorj** — 1,211 open issues, pushed 2026-07-17 (this repo)
- **plurigrid/nash-portal** — NASH token TUI in browser (ratzilla WASM + GeckoTerminal OHLCV)
- **TeglonLabs/jank-crane** — NEW: crane-jank converged-IR hub, GF3 convergence maps (C++, pushed 2026-06-08)
- **bmorphism/gay-chat** — gay://chat operationalization over Spritely Brassica Chat (pushed 2026-07-14)
- **bmorphism/Gay.jl** — Wide-gamut color sampling, 187 open issues (pushed 2026-07-14)
- **kubeflow/mcp-apache-spark-history-server** — 183 ★ MCP server for Spark debugging (new)
- **wasita/wasita.github.io** — Svelte personal website, pushed 2026-07-16
- **M1shaaa/M1shaaa** — profile repo pushed 2026-07-16

---

## Hamming Swarm Snapshot — Aptos Mainnet

### Wallet Balances (28 addresses probed)

All 28 Hamming swarm wallets (alice, bob, A–Z) returned **0 APT** on Aptos mainnet.
The `CoinStore<AptosCoin>` resource was not funded on any address at sweep time.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...e9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...cdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G–Z | … (20 more) | 0.0 each |

### Multisig Contract Probes (5 contracts)

All 5 multisig contracts probed. **All require 2-of-2 signatures and are healthy.**

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ healthy |
| A-G | 0xf56c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — testnet.mnx.fi requires Vercel deployment authentication (Protection Bypass token needed). No market data could be retrieved.

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,779 stars — flagship ML platform for Kubernetes (pushed 2026-07-10)
- **kubeflow/pipelines**: 4,167 stars — pushed 2026-07-16 (active)
- **kubeflow/mcp-apache-spark-history-server**: 183 ★ — new MCP server for Spark debugging via AI agents
- **TeglonLabs/jank-crane**: NEW repo since last sweep — C++ crane-jank converged-IR hub with GF3 convergence maps
- **bmorphism/Gay.jl**: Wide-gamut deterministic color sampling — 187 open issues, very active (pushed 2026-07-14)
- **plurigrid/gorj**: This repo — 1,211 open issues as of 2026-07-17
- **plurigrid/nash-portal**: NASH token TUI — ratzilla WASM + GeckoTerminal OHLCV candlesticks
- **Hamming swarm**: All 28 wallets show 0 APT; all 5 multisig contracts are 2-of-2 and healthy
- **Increment 24**: ERGODIC — sweep_complete closing the 8th full GF(3) cycle
