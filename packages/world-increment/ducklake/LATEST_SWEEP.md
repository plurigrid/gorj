# World-Increment Sweep — 2026-07-27

## Sweep Metadata
- **Date:** 2026-07-27
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 34 (12 prior + 11 this run) |
| Total Repo Snapshots | 1,264 (473 prior + 320 this run) |
| Sources Covered (this run) | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — This Run (Increments 13–23)

| ID | Source | Type | GF3 Trit | Color | Name | Repos |
|----|--------|------|-----------|-------|------|-------|
| 13 | plurigrid | org | +1 | `#b8bb26` | **PLUS** | 100 |
| 14 | kubeflow | org | -1 | `#cc241d` | **MINUS** | 49 |
| 15 | bmorphism | user | 0 | `#d3869b` | **ERGODIC** | 100 |
| 16 | zubyul | user | +1 | `#b8bb26` | **PLUS** | 49 |
| 17 | migalkin (social) | user | -1 | `#cc241d` | **MINUS** | 5 |
| 18 | wasita (social) | user | 0 | `#d3869b` | **ERGODIC** | 3 |
| 19 | AustinCStone (social) | user | +1 | `#b8bb26` | **PLUS** | 3 |
| 20 | DJedamski (social) | user | -1 | `#cc241d` | **MINUS** | 2 |
| 21 | kristinezheng (social) | user | 0 | `#d3869b` | **ERGODIC** | 2 |
| 22 | M1shaaa (social) | user | +1 | `#b8bb26` | **PLUS** | 2 |
| 23 | TeglonLabs | org | -1 | `#cc241d` | **MINUS** | 5 |

GF(3) chain continues: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

### Top Repos by Stars (This Sweep)

| Repo | Language | Stars | Forks | Issues | Last Push |
|------|----------|-------|-------|--------|-----------|
| kubeflow/kubeflow | — | 15,792 | 2,685 | 0 | 2026-07-10 |
| kubeflow/pipelines | Python | 4,170 | 2,067 | 466 | **2026-07-27** |
| kubeflow/spark-operator | Python | 3,142 | 1,506 | 111 | 2026-07-25 |
| kubeflow/trainer | Go | 2,154 | 997 | 112 | **2026-07-27** |
| kubeflow/katib | Python | 1,692 | 532 | 107 | 2026-07-26 |
| migalkin/NodePiece | Python | 144 | 21 | 0 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 30 | 5 | 2025-03-03 |
| migalkin/StarE | Python | 89 | 16 | 1 | 2026-04-16 |
| TeglonLabs/mathpix-gem | Ruby | 2 | 0 | 11 | 2026-01-01 |
| TeglonLabs/jank-crane | C++ | 0 | 0 | 0 | 2026-06-08 |

### Notable Activity (vs April 2026 baseline)
- **kubeflow/kubeflow**: 15,792★ (+227 since Apr) — still the top star in the graph
- **kubeflow/pipelines** and **kubeflow/trainer** both pushed **today** (2026-07-27) — active sprints
- **migalkin/NodePiece**: 144★ (+1) — steady ICLR'22 KG embeddings growth
- **wasita/wasita.github.io** pushed 2026-07-21 — most recently active social graph member (Svelte site)
- **TeglonLabs/jank-crane** (new since Apr): GF3 convergence maps + loopify pass spec in C++
- **TeglonLabs/mathpix-gem**: 11 open issues — needs attention

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)

All 28 addresses queried against Aptos mainnet (`fullnode.mainnet.aptoslabs.com`). All returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — the accounts exist on-chain but have no initialized APT coin store.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793...4cc7b | 0.00000000 |
| bob | 0x0a3c...512d5d | 0.00000000 |
| A | 0x8699...e9d7a | 0.00000000 |
| B–Z | (25 addresses) | 0.00000000 each |

> Status: All 28 wallets show 0 APT — `CoinStore` not initialized on Aptos mainnet.

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4...87003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**All 5 multisig contracts healthy — 2-of-N signatures required on each.**

### MNX Markets

`testnet.mnx.fi` is a Next.js SPA. All probed API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`, `/markets`) returned the SPA HTML shell — no public JSON REST endpoint found. Status: **unavailable (SPA-only)**. Recorded as placeholder row in `mnx_snapshots`.

---

## DuckDB Ducklake Totals

| Table | Rows |
|-------|------|
| world_increments | 34 |
| repo_snapshots | 1,264 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

Database: `packages/world-increment/ducklake/world-increments.duckdb`

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
