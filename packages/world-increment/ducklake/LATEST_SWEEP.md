# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-02

## Sweep Metadata
- **Date:** 2026-06-02T22:30:00Z
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 97 |
| Total Repo Snapshots | 97 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Market Rows | 0 (SPA, no API) |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 20 (of 101 total) |
| kubeflow | org | 20 (of 48 total) |
| TeglonLabs | org | 4 |
| bmorphism | user | 20 (of 103 total) |
| zubyul | user | 10 (of 49 total) |
| migalkin | social graph | 6 |
| DJedamski | social graph | 3 |
| wasita | social graph | 4 |
| kristinezheng | social graph | 3 |
| M1shaaa | social graph | 3 |
| AustinCStone | social graph | 4 |
| **TOTAL** | | **97** |

### Top Repositories by Stars

| Repo | Language | ⭐ Stars | 🍴 Forks | 🐛 Issues | Pushed At |
|------|----------|---------|---------|---------|-----------|
| kubeflow/kubeflow | — | 15,704 | 2,668 | 3 | 2026-05-24 |
| kubeflow/pipelines | Python | 4,151 | 2,004 | 487 | 2026-06-02 |
| kubeflow/spark-operator | Python | 3,125 | 1,488 | 103 | 2026-06-01 |
| kubeflow/trainer | Go | 2,110 | 963 | 126 | 2026-06-02 |
| kubeflow/katib | Python | 1,685 | 525 | 122 | 2026-05-29 |
| migalkin/NodePiece | Python | 144 | 21 | 0 | 2022-02-02 |
| AustinCStone/TextGAN | Python | 92 | 30 | 5 | 2016-10-04 |
| migalkin/StarE | Python | 89 | 16 | 1 | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2 | 0 | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 7 | 1 | 2026-01-16 |
| plurigrid/asi | HTML | 24 | 6 | 4 | 2026-04-26 |
| plurigrid/gorj | Clojure | 0 | 0 | 310 | 2026-06-02 |
| bmorphism/Gay.jl | Julia | 1 | 0 | 189 | 2026-06-02 |
| plurigrid/eirobri | Clojure | 0 | 0 | 28 | 2026-05-26 |

### GF(3) Color Chain Distribution (97 world_increments)

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` (rose) | 32 |
| +1 | PLUS | `#b8bb26` (yellow-green) | 33 |
| -1 | MINUS | `#cc241d` (red) | 32 |

GF(3) assignment rule:
- `id mod 3 == 0` → trit=0, ERGODIC `#d3869b`
- `id mod 3 == 1` → trit=+1, PLUS `#b8bb26`
- `id mod 3 == 2` → trit=-1, MINUS `#cc241d`

### Notable Activity

- **plurigrid/gorj** (this repo): 310 open issues, pushed 2026-06-02 — most-discussed plurigrid repo
- **bmorphism/Gay.jl**: 189 open issues — active GF(3) color sampling + splittable determinism library
- **kubeflow/pipelines**: pushed 2026-06-02T19:02:03Z — most active kubeflow project
- **TeglonLabs/mathpix-gem**: 11 open issues — Ruby mathematical OCR gem
- **bmorphism/world**: Python local worlds launcher, pushed 2026-06-02
- **zubyul/wasita.github.io**: personal site, 8 open issues, pushed 2026-06-01

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 Hamming swarm wallets queried via Aptos fullnode mainnet  
(`GET /v1/accounts/{ADDR}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`).

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | `0xc793...4cc7b` | 0.00000000 |
| bob | `0x0a3c...512d5d` | 0.00000000 |
| A | `0x8699...e9d7a` | 0.00000000 |
| B | `0x3f89...cb13` | 0.00000000 |
| C | `0x38b9...535e` | 0.00000000 |
| D | `0xf776...cfdd1` | 0.00000000 |
| E | `0xdc1d...958d36` | 0.00000000 |
| F | `0x18a1...3cf71` | 0.00000000 |
| G | `0x69a3...c7f32` | 0.00000000 |
| H | `0xce67...5300f` | 0.00000000 |
| I | `0x070f...1fc9` | 0.00000000 |
| J | `0x4d96...7f54` | 0.00000000 |
| K | `0xa732...425dc4` | 0.00000000 |
| L | `0x7c2e...7eba9` | 0.00000000 |
| M | `0x6fed...7f2e9` | 0.00000000 |
| N | `0xe7dd...51b2c` | 0.00000000 |
| O | `0x7325...5a89d` | 0.00000000 |
| P | `0x6218...ec948` | 0.00000000 |
| Q | `0xac40...c89a9` | 0.00000000 |
| R | `0x7ce6...76e10` | 0.00000000 |
| S | `0xb875...d0386` | 0.00000000 |
| T | `0x3578...3f4588` | 0.00000000 |
| U | `0x7586...f9956` | 0.00000000 |
| V | `0xb59d...9af2c3` | 0.00000000 |
| W | `0x5f32...c7b0` | 0.00000000 |
| X | `0xa95c...3047d` | 0.00000000 |
| Y | `0xd8e3...444c4` | 0.00000000 |
| Z | `0x7af0...197c` | 0.00000000 |

**Total swarm APT: 0.00000000**

All addresses returned `resource_not_found` for `CoinStore<AptosCoin>`, indicating wallets are uninitialized on Aptos mainnet (no on-chain APT deposits).

### Multisig Contract Probes

Probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`:

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | `0x0da4f4...987003` | **2** | ✅ Healthy |
| A-G | `0xf56c4a...bc0096` | **2** | ✅ Healthy |
| Y-Z | `0xd3ffe1...75b883` | **2** | ✅ Healthy |
| S-T | `0x3b1c3a...ed7883` | **2** | ✅ Healthy |
| V-W | `0x40fad7...80eb6d` | **2** | ✅ Healthy |

All 5 multisig contracts healthy. All require 2-of-N signatures. Network confirmed live contract state for all addresses.

### MNX Markets (testnet.mnx.fi)

**Status: SPA — no public REST API accessible**

`testnet.mnx.fi` is a Next.js single-page application. Paths probed:
- `/api/markets` → returns SPA HTML shell (Next.js SSR scaffold)
- `/api/v1/markets` → returns SPA HTML shell
- `/` → Next.js SPA shell with client-side data loading

No market data extractable without a browser runtime. `mnx_snapshots` table is empty this sweep.

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

---

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent.*
