# World-Increment Sweep + Hamming Snapshot — 2026-06-07

## Sweep Metadata
- **Date:** 2026-06-07
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried This Sweep

| Source | Type | Repos Captured | Notes |
|--------|------|---------------|-------|
| plurigrid | org | 100 | API cap (101 total); gorj pushed 2026-06-07 |
| kubeflow | org | 48 | Complete set |
| TeglonLabs | org | 4 | mathpix-gem, topoi, monad-mcp-server, coin-flip-mcp |
| bmorphism | user | 100 | API cap (103 total) |
| zubyul | user | 49 | Complete set |
| migalkin | user (social) | 19 | KG researcher; NodePiece ⭐144, StarE ⭐89 |
| wasita | user (social) | 11 | Network scientist; Svelte stack |
| AustinCStone | user (social) | 30 | ML/CV; TextGAN ⭐92 |
| DJedamski | user (social) | 6 | Data science / Kaggle |
| kristinezheng | user (social) | 5 | MIT cognitive science |
| M1shaaa | user (social) | 8 | Yale; TypeScript, Lookit |
| **TOTAL** | | **~380** | |

### Top Repos by Stars (this sweep)

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,706 | — |
| kubeflow/pipelines | 4,153 | Python |
| kubeflow/spark-operator | 3,125 | Python |
| kubeflow/trainer | 2,112 | Go |
| kubeflow/katib | 1,685 | Python |
| kubeflow/examples | 1,462 | Jsonnet |
| kubeflow/manifests | 1,020 | YAML |
| kubeflow/arena | 811 | Go |
| kubeflow/kale | 691 | Python |
| kubeflow/mpi-operator | 528 | Go |
| migalkin/NodePiece | 144 | Python |
| migalkin/StarE | 89 | Python |
| AustinCStone/TextGAN | 92 | Python |
| plurigrid/asi | 25 | HTML |
| migalkin/kgcourse2021 | 25 | HTML |

### Notable plurigrid Activity (2026-06-07)

- **gorj** (`plurigrid/gorj`): pushed **2026-06-07T09:16:28Z** — active today; 415 open issues; Clojure
- **nanoclj-zig**: NaN-boxed Clojure in Zig 0.15 with GF(3) trit conservation; 20 open issues
- **eirobri**: EiRoBri replay world; 29 open issues; pushed 2026-06-03
- **place**: TeX; 8 open issues; pushed 2026-06-04
- **nash-portal**: NASH token TUI — ratzilla WASM + GeckoTerminal OHLCV candlesticks; ⭐2
- **asi**: "everything is topological chemputer!" ⭐25

### GF(3) Increment Color Distribution (this sweep — 362 new increments)

| Name | Color | Trit | Count |
|------|-------|------|-------|
| PLUS | #b8bb26 | +1 | 121 |
| MINUS | #cc241d | -1 | 121 |
| ERGODIC | #d3869b | 0 | 120 |

Balanced near-uniform distribution — GF(3) conservation holding.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances — 28 Addresses

Queried via `fullnode.mainnet.aptoslabs.com` (2026-06-07). Sleep 1s between calls.

| World | Address (truncated) | APT Balance |
|-------|-------------------|-------------|
| alice | 0xc793...4cc7b | 0.0 |
| bob | 0x0a3c...512d5d | 0.0 |
| A–Z (26) | 0x8699… – 0x7af0… | 0.0 each |

**All 28 addresses: 0 APT.** CoinStore resources exist but hold no balance — Hamming swarm addresses are freshly generated and awaiting funding.

### Multisig Contract Probes — 5 Pairs

`0x1::multisig_account::num_signatures_required` via Aptos View API.

| Pair | Contract (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All 5 multisig contracts live on Aptos mainnet — **all require 2-of-N signatures. All healthy.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel deployment protection. All endpoints (`/`, `/api/markets`, `/api/v1/markets`, `/api/tickers`) require authentication. `mnx_snapshots` table: 0 rows.

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
- `id mod 3 == 0` → trit=0, color=#d3869b, **ERGODIC**
- `id mod 3 == 1` → trit=+1, color=#b8bb26, **PLUS**
- `id mod 3 == 2` → trit=-1, color=#cc241d, **MINUS**

*DB accumulates sweeps over time — historical runs from prior sweeps (2026-04-12 etc.) also present in tables.*
