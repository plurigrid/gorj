# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-30

## Sweep Metadata
- **Date:** 2026-04-30
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source (this sweep: 389 new snapshots)

| Source | Type | Repos | Total Stars | Latest Push |
|--------|------|:-----:|:-----------:|-------------|
| plurigrid | org | 100 | 145 | 2026-04-30 |
| bmorphism | user | 100 | 508 | 2026-04-30 |
| kubeflow | org | 47 | ~101k | 2026-04-30 |
| AustinCStone | user (social) | 40 | 324 | 2026-02-11 |
| zubyul | user | 49 | 40 | 2026-04-24 |
| migalkin | user (social) | 19 | 832 | 2025-08-04 |
| wasita | user (social) | 10 | 10 | 2026-04-28 |
| M1shaaa | user (social) | 8 | 0 | 2026-04-30 |
| kristinezheng | user (social) | 6 | 0 | 2026-04-09 |
| DJedamski | user (social) | 6 | 17 | 2018-03-07 |
| TeglonLabs | org | 4 | 14 | 2026-01-16 |
| **TOTAL** | | **389** | **~103k** | |

### GF(3) Color Chain Distribution (cumulative DB)

| Name | Color | Trit | Count |
|------|-------|:----:|------:|
| ERGODIC | #d3869b | 0 | 136 |
| PLUS | #b8bb26 | +1 | 138 |
| MINUS | #cc241d | -1 | 138 |

GF(3) chain rule: `id%3==0 → ERGODIC #d3869b | id%3==1 → PLUS #b8bb26 | id%3==2 → MINUS #cc241d`

### Notable Repos (this sweep)

| Repo | Stars | Pushed |
|------|------:|--------|
| kubeflow/kubeflow | 15,610 | 2026-04-30 |
| kubeflow/pipelines | 4,130 | 2026-04-30 |
| kubeflow/spark-operator | ~3,100 | 2026-04-30 |
| migalkin/NodePiece | 143 | 2025-08-04 |
| bmorphism/ocaml-mcp-sdk | 60 | 2026-04-30 |
| AustinCStone/TextGAN | 92 | 2026-02-11 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried 28 addresses (alice, bob, A–Z) via `fullnode.mainnet.aptoslabs.com`.

| Metric | Value |
|--------|-------|
| Addresses queried | 28 |
| Addresses with APT balance | 0 |
| Total APT across swarm | 0.0 APT |

All 28 addresses returned 0.0 APT. Accounts exist on-chain but hold no APT CoinStore balance.

### Multisig Contract Probes

| Pair | Address | Sigs Required | Status |
|------|---------|:-------------:|:------:|
| A-B | 0x0da4f428...987003 | 2 | ✅ healthy |
| A-G | 0xf56c4a1c...c0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ffe181...b883 | 2 | ✅ healthy |
| S-T | 0x3b1c3ae9...7883 | 2 | ✅ healthy |
| V-W | 0x40fad7b4...eb6d | 2 | ✅ healthy |

All 5 multisig accounts require **2-of-N signatures** and responded correctly via `0x1::multisig_account::num_signatures_required`.

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — site is a Next.js SPA; no machine-readable API found at `/api/markets`, `/api/v1/markets`, or `/api/tickers`. Noted in `mnx_snapshots` table as unavailable marker.

---

## DuckDB Table Summary (cumulative)

| Table | Rows |
|-------|-----:|
| world_increments | 412 |
| repo_snapshots | 1,333 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

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
