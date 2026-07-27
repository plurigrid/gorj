# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-27

## Sweep Metadata
- **Date:** 2026-07-27
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** latest CLI
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Total Repos | Indexed |
|--------|------|------------|---------|
| plurigrid | org | 50 | 10 |
| kubeflow | org | 49 | 7 |
| bmorphism | user | 106 | 6 |
| TeglonLabs | org | 5 | 3 |
| zubyul | user | 49 | 3 |
| migalkin | user (social) | 19 | 2 |
| wasita | user (social) | 12 | 2 |
| AustinCStone | user (social) | 41 | 1 |
| DJedamski | user (social) | 6 | 0 |
| kristinezheng | user (social) | 5 | 0 |
| M1shaaa | user (social) | 8 | 0 |

### GF(3) Color Chain — World Increments (34 total)
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

Sample chain: `ERGODIC(1) → PLUS(2) → MINUS(3) → ERGODIC(4) → PLUS(5) → ...`

### Top Repositories by Stars (from sweep)
| Repo | Stars | Forks | Language | Last Push |
|------|-------|-------|----------|-----------|
| kubeflow/kubeflow | 15,793 | 2,687 | — | 2026-07-27 |
| kubeflow/pipelines | 4,171 | 2,068 | Python | 2026-07-27 |
| kubeflow/spark-operator | 3,142 | 1,506 | Python | 2026-07-26 |
| kubeflow/trainer | 2,155 | 997 | Go | 2026-07-27 |
| kubeflow/katib | 1,692 | 531 | Python | 2026-07-20 |
| kubeflow/examples | 1,461 | 756 | Jsonnet | 2026-07-22 |
| migalkin/NodePiece | 144 | 21 | Python | 2026-05-07 |
| bmorphism/ocaml-mcp-sdk | 61 | 2 | OCaml | 2026-05-08 |
| plurigrid/asi | 52 | 11 | HTML | 2026-07-10 |
| AustinCStone/TextGAN | 92 | 30 | Python | 2025-03-03 |

### Most Recently Active (plurigrid cluster)
- **plurigrid/gorj** — pushed 2026-07-27, **1446 open issues** — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **plurigrid/eirobri** — pushed 2026-07-21 — EiRoBri replay world (Clojure)
- **plurigrid/place** — pushed 2026-07-14 — bci.place forester preview (TeX)
- **bmorphism/Gay.jl** — pushed 2026-07-21, **188 open issues** — Wide-gamut color sampling SPI (Julia)
- **bmorphism/gay-chat** — pushed 2026-07-14 — gay://chat over Spritely Brassica Chat (Scheme)

### Notable New Repos (2026)
- `kubeflow/mcp-server` (Apr 2026) — MCP Server for Kubeflow Tools; 29★
- `kubeflow/mcp-apache-spark-history-server` (Jun 2025) — 184★, most active kubeflow MCP
- `bmorphism/satreadout` (Jun 2026) — Machine-checked saturating perceptual readout (Lean 4.28 + mathlib)
- `bmorphism/gay-chat` (Jul 2026) — gay://chat operationalization over Spritely Brassica Chat
- `TeglonLabs/jank-crane` (Jun 2026) — crane-jank converged-IR hub, GF3 convergence maps (C++)
- `zubyul/voice-observatory` (Apr 2026) — Passive macOS TUI for voice-download pathways (Python)
- `bmorphism/world` (Jun 2026) — Local worlds launcher for SA3, jank, world proofs

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet — 28 addresses probed)
**API:** `https://fullnode.mainnet.aptoslabs.com/v1`  
**Ledger version probed:** ~6,482,659,490

All 28 Hamming swarm addresses returned `resource_not_found` for  
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

> This means these accounts have not registered an APT CoinStore on mainnet
> (accounts may exist at ledger level but have not received/sent APT, or
> may have migrated to the new FungibleAsset model instead of the legacy Coin module).

| World | Address (truncated) | Balance APT | Status |
|-------|--------------------|-----------:|--------|
| alice | 0xc793...cc7b | 0.0 | resource_not_found |
| bob | 0x0a3c...512d | 0.0 | resource_not_found |
| A | 0x8699...9d7a | 0.0 | resource_not_found |
| B | 0x3f89...b13 | 0.0 | resource_not_found |
| C | 0x38b9...535e | 0.0 | resource_not_found |
| D | 0xf776...fdd1 | 0.0 | resource_not_found |
| E | 0xdc1d...8d36 | 0.0 | resource_not_found |
| F | 0x18a1...3cf71 | 0.0 | resource_not_found |
| G–Z | (20 more addresses) | 0.0 each | resource_not_found |

**Total swarm APT (legacy CoinStore): 0.0 APT**

### Multisig Contract Probes — All 5 Pairs Healthy
**Function:** `0x1::multisig_account::num_signatures_required`

| Pair | Contract Address (truncated) | Sigs Required | Healthy |
|------|--------------------------|:------------:|:-------:|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**5/5 multisig contracts healthy · All require 2-of-N threshold**

### MNX Markets (testnet.mnx.fi)
`testnet.mnx.fi` is a **Next.js SPA** — all probed routes return the HTML shell.  
No REST/JSON market data API is accessible without browser-side JavaScript execution.

Paths probed: `/`, `/api/markets`, `/api/v1/markets`, `/markets`  
**Status: UNAVAILABLE via curl** — recorded in `mnx_snapshots` table as placeholder.

---

## DuckDB Table Summary
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows | Description |
|-------|-----:|-------------|
| world_increments | 34 | GF(3)-colored GitHub push events |
| repo_snapshots | 34 | Full repo metadata (stars, forks, issues, pushed_at) |
| aptos_snapshots | 28 | Hamming swarm APT balances (alice, bob, A–Z) |
| multisig_probes | 5 | Pair multisig health check (all 2-sig, all healthy) |
| mnx_snapshots | 1 | MNX SPA unavailable marker |

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

---

*Generated by world-increment-sweep + hamming-swarm-snapshot agent · 2026-07-27*
