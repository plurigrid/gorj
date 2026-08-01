# World-Increment Sweep + Hamming Swarm Snapshot — 2026-08-01

## Sweep Metadata
- **Date:** 2026-08-01
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| New World Increments (this run) | 34 |
| New Repo Snapshots (this run) | 34 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Worlds Queried | 28 (alice, bob, A–Z) |
| Total APT Balance | 0.0 (all wallets unfunded on mainnet) |
| Multisig Contracts Healthy | 5/5 (all 2-of-N) |
| MNX Market Data | Unavailable (SPA, no REST API) |

---

## Job 1: GitHub Social Graph Sweep

### GF(3) Color Chain — New Increments (IDs 1–34 this run)

GF(3) sequence: `PLUS(#b8bb26) → MINUS(#cc241d) → ERGODIC(#d3869b) → ...` (cycling)

| Source | Type | Repos Snapped | Recent Activity |
|--------|------|--------------|----------------|
| plurigrid | org | 100 | gorj pushed 2026-08-01, asi 57★ |
| kubeflow | org | 49 | kubeflow 15,802★, pipelines 4,172★ |
| TeglonLabs | org | 5 | jank-crane (C++, GF3 maps) |
| bmorphism | user | 106 | Gay.jl 188 issues, ocaml-mcp-sdk 61★ |
| zubyul | user | 49 | voice-observatory, tilelang-kernels |
| migalkin | user | 19 | NodePiece 144★, StarE 89★ |
| wasita | user | 12 | wasita.github.io updated 2026-07-21 |
| AustinCStone | user | 41 | byteruckus new 2026-07-15, TextGAN 92★ |
| DJedamski | user | 6 | kaggle projects |
| kristinezheng | user | 5 | site updated 2026-07-01 |
| M1shaaa | user | 8 | lab-bookshelf TypeScript |

### Top Repos by Stars (2026-08-01 snapshot)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,802 | — | 2026-07-10 |
| kubeflow/pipelines | 4,172 | Python | 2026-07-31 |
| kubeflow/spark-operator | 3,141 | Python | 2026-07-31 |
| kubeflow/trainer | 2,165 | Go | 2026-07-31 |
| kubeflow/katib | 1,695 | Python | 2026-07-26 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-05-08 |
| plurigrid/asi | 57 | HTML | 2026-07-10 |
| bmorphism/anti-bullshit-mcp-server | 22 | JavaScript | 2026-07-12 |
| bmorphism/say-mcp-server | 20 | JavaScript | 2026-03-19 |
| bmorphism/babashka-mcp-server | 19 | JavaScript | 2026-06-05 |

### Notable Activity

- **plurigrid/gorj** (this repo): 1,549 open issues, pushed TODAY 2026-08-01
- **plurigrid/eirobri**: 31 open issues — EiRoBri replay world active
- **TeglonLabs/jank-crane**: C++, GF3 convergence maps — pushed 2026-06-08
- **kubeflow/notebooks**: 167 open issues — most active kubeflow workstream
- **bmorphism/Gay.jl**: 188 open issues (!) — wide-gamut color sampling with splittable determinism
- **bmorphism/gay-chat**: New repo 2026-07-14 — gay://chat over Spritely Brassica Chat (Scheme)

---

## Job 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (2026-08-01)

Queried 28 wallets via `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**All 28 wallets: 0.0 APT** — addresses are unfunded on Aptos mainnet (likely testnet/devnet keys or uninitialized accounts).

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793ac...cc7b | 0.0 |
| bob | 0x0a3c00...512d | 0.0 |
| A–Z (26 wallets) | various | 0.0 each |

**Total swarm APT balance: 0.000000**

### Multisig Contract Probes

All 5 contracts queried via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f4...7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe1...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3a...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fad7...eb6d | 2 | ✓ HEALTHY |

**All 5 multisig accounts are responsive and require 2-of-N signatures.**

### MNX Markets (testnet.mnx.fi)

Probed: `/api/markets`, `/api/v1/markets`, `/api/tickers`.

**Status: UNAVAILABLE** — testnet.mnx.fi is a Next.js SPA; no REST endpoints exposed. No market data returned. No mnx_snapshots inserted.

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
