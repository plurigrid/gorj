# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-17

## Sweep Metadata
- **Date:** 2026-05-17
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| bmorphism | user | 102 |
| plurigrid | org | 89 |
| zubyul | user | 50 |
| kubeflow | org | 49 |
| AustinCStone | user (zubyul social) | 41 |
| migalkin | user (zubyul social) | 20 |
| wasita | user (zubyul social) | 12 |
| M1shaaa | user (zubyul social) | 9 |
| kristinezheng | user (zubyul social) | 7 |
| DJedamski | user (zubyul social) | 7 |
| TeglonLabs | org | 5 |
| **TOTAL** | | **391 world-increments** |

### GF(3) Color Chain

Each world increment is colored by `id % 3`:
- `id%3==0` → trit=0 **ERGODIC** `#d3869b`
- `id%3==1` → trit=1 **PLUS** `#b8bb26`
- `id%3==2` → trit=-1 **MINUS** `#cc241d`

### Notable Active Repos (pushed today 2026-05-17)

- `plurigrid/gorj` — forj + Rama topology nREPL routing + GF(3) trit coloring (Clojure)
- `wasita/wasita.github.io` — personal website (Svelte)
- `M1shaaa/M1shaaa` — GitHub profile config

### Top Repos by Stars

- `kubeflow/kubeflow` — 15,565★ flagship ML platform for Kubernetes
- `kubeflow/pipelines` — 4,119★ ML pipeline
- `kubeflow/spark-operator` — 3,111★ Kubernetes/Spark operator
- `migalkin/NodePiece` — 143★ scalable KG embeddings
- `AustinCStone/TextGAN` — 92★ text generation with GANs
- `bmorphism/ocaml-mcp-sdk` — 60★ OCaml MCP SDK
- `TeglonLabs/mathpix-gem` — 2★ math OCR Ruby gem

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (via `0x1::coin::balance` view function)

**Total across 28 wallets: 20.3448 APT**

| World | Balance (APT) | Address |
|-------|---------------|---------|
| bob | 12.6570 | `0x0a3c00c5...e05512d5d` |
| F | 1.9605 | `0x18a14b5b...74c3cf71` |
| L | 1.9273 | `0x7c2eaeaf...6337eba9` |
| J | 1.8951 | `0x4d964db8...3e87f54` |
| alice | 0.4364 | `0xc793acde...d624cc7b` |
| O | 0.2101 | `0x73252b60...25a89d` |
| K | 0.1620 | `0xa732040a...7a425dc4` |
| P | 0.1401 | `0x62187920...1ec948` |
| M | 0.1123 | `0x6fed37a7...49b7f2e9` |
| N | 0.1061 | `0xe7dde6da...1551b2c` |
| Q | 0.1032 | `0xac40fa50...5e5c89a9` |
| S | 0.0918 | `0xb8753014...f99d0386` |
| R | 0.0902 | `0x7ce605cc...36d76e10` |
| T | 0.0737 | `0x35781dc0...d3f4588` |
| U | 0.0558 | `0x75860da4...5ef9956` |
| V | 0.0488 | `0xb59dd817...89af2c3` |
| A | 0.0518 | `0x8699edc0...ebe9d7a` |
| X | 0.0426 | `0xa95cbbd1...be33047d` |
| W | 0.0407 | `0x5f32aef7...a6ccc7b0` |
| Y | 0.0444 | `0xd8e32848...a2444c4` |
| B | 0.0363 | `0x3f892ebe...4577cb13` |
| Z | 0.0243 | `0x7af0ef6e...e4e197c` |
| C | 0.0102 | `0x38b99e63...2691535e` |
| D | 0.0116 | `0xf7765624...d9fcfdd1` |
| E | 0.0094 | `0xdc1d9d53...d0958d36` |
| H | 0.0017 | `0xce67c327...d94e5300f` |
| G | 0.0007 | `0x69a394c0...5dbcc7f32` |
| I | 0.0007 | `0x070fe5d7...fc00c1fc9` |

> **Note:** Initial query used legacy `CoinStore` resource (returned 0 — accounts have migrated to new FA store).
> Re-queried correctly via `0x1::coin::balance` view function on Aptos mainnet.

### Multisig Contract Probes

All 5 multisig contracts are **healthy** — each requires 2 signatures.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4f428...4987003` | 2 | ✓ healthy |
| A-G | `0xf56c4a1c...fbc0096` | 2 | ✓ healthy |
| Y-Z | `0xd3ffe181...e75b883` | 2 | ✓ healthy |
| S-T | `0x3b1c3ae9...3ded7883` | 2 | ✓ healthy |
| V-W | `0x40fad7b4...c80eb6d` | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

**Status: SPA-only — no accessible REST API**

The site serves a Next.js SPA (HTTP 200 confirmed). Routes `/api/markets` and `/api/v1/markets` return the full app HTML shell, not JSON. No market data extractable without browser-side JS execution.

---

## DuckDB Table Summary

| Table | Rows | Notes |
|-------|------|-------|
| `world_increments` | 391 | GitHub repo sweep, GF(3) chain |
| `repo_snapshots` | 473 | Includes 82 additional wasita/kristinezheng repos |
| `aptos_snapshots` | 28 | Hamming swarm A-Z + alice + bob |
| `multisig_probes` | 5 | All healthy, 2-of-N |
| `mnx_snapshots` | 0 | SPA-only, no REST API available |

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
