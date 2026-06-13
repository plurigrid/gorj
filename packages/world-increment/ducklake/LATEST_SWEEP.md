# World Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-06-13  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** v1.5.3 (Variegata)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried (391 repos captured)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 48 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| wasita | user | 11 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user | 5 |
| **TOTAL** | | **391** |

### GF(3) Color Chain (391 increments this sweep)

| GF3 | Trit | Color | Count |
|-----|------|-------|-------|
| PLUS | +1 | `#b8bb26` | 131 |
| ERGODIC | 0 | `#d3869b` | 130 |
| MINUS | -1 | `#cc241d` | 130 |

Rule: `id%3==0 → ERGODIC #d3869b`, `id%3==1 → PLUS #b8bb26`, `id%3==2 → MINUS #cc241d`

### Top Repos by Stars (this sweep)

| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| kubeflow/kubeflow | — | 15565 | 2026-01-05 |
| kubeflow/pipelines | Python | 4119 | 2026-04-10 |
| kubeflow/spark-operator | Python | 3111 | 2026-04-10 |
| kubeflow/trainer | Go | 2080 | 2026-04-10 |
| kubeflow/katib | Python | 1676 | 2026-04-02 |
| migalkin/NodePiece | Python | 143 | — |
| AustinCStone/TextGAN | Python | 92 | — |
| bmorphism/ocaml-mcp-sdk | OCaml | 60 | — |
| migalkin/StarE | Python | 88 | — |
| TeglonLabs/mathpix-gem | Ruby | 2 | 2026-01-01 |

### Recently Pushed (this sweep)

- `TeglonLabs/jank-crane` — crane-jank converged-IR hub, GF3 maps (2026-06-08, C++)
- `kristinezheng/kristinezheng.github.io` — personal site (2026-06-07, HTML)
- `M1shaaa/M1shaaa` — profile config (2026-06-13)
- `wasita/wasita.github.io` — personal website (2026-06-01, Svelte)
- `plurigrid/asi` — topological chemputer (2026-04-10, HTML, 16 stars)

### Language Distribution (this sweep)

| Language | Repos |
|----------|-------|
| Python | 88 |
| Rust | 26 |
| JavaScript | 21 |
| Go | 20 |
| HTML | 18 |
| TypeScript | 16 |
| Jupyter Notebook | 15 |
| Clojure | 12 |

### DuckDB Cumulative State
- `world_increments`: 414 total rows (391 this sweep)
- `repo_snapshots`: 1335 total rows (391 this sweep)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 28 addresses)

All 28 Hamming swarm addresses (alice, bob, A–Z) were probed via  
`GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

| Metric | Value |
|--------|-------|
| Addresses probed | 28 |
| Non-zero APT | 0 |
| Zero / no CoinStore | 28 |

All addresses have 0 APT on mainnet — CoinStore resource absent, wallets not funded.

### Multisig Contract Probes

All 5 pairs probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | `0x0da4f428...87003` | 2 | ✓ HEALTHY |
| A-G | `0xf56c4a1c...0096` | 2 | ✓ HEALTHY |
| Y-Z | `0xd3ffe181...b883` | 2 | ✓ HEALTHY |
| S-T | `0x3b1c3ae9...7883` | 2 | ✓ HEALTHY |
| V-W | `0x40fad7b4...eb6d` | 2 | ✓ HEALTHY |

**All 5 multisig accounts healthy** — all require 2-of-2 threshold.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — protected by Vercel deployment auth on all endpoints  
(`/api/markets`, `/api/v1/markets`, `/markets`, root). `mnx_snapshots` has 0 rows.

---

## Schema Reference

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
