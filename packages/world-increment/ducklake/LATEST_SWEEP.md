# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-29

## Sweep Metadata
- **Date:** 2026-05-29
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### New Repos Snapshotted Today (67 fresh snapshots)

| Source | Type | Repos Added | Notable |
|--------|------|-------------|---------|
| plurigrid | org | 20 | gorj (255 open issues), eirobri, nanoclj-zig, zig-syrup |
| kubeflow | org | 13 | pipelines (4150★), kubeflow (15686★), spark-operator (3124★) |
| TeglonLabs | org | 4 | mathpix-gem, coin-flip-mcp, monad-mcp-server, topoi |
| zubyul | user | 8 | nash-tui, tilelang-kernels, gay-world, vibesnipe |
| migalkin | social | 5 | NodePiece (144★), StarE (89★), kgcourse2021 (25★) |
| wasita | social | 5 | wm-cv, vocoder, magic-garden, send2kobo |
| AustinCStone | social | 4 | TextGAN (92★), StereoVisionMRF (11★) |
| DJedamski | social | 2 | kaggle_ncaa18, Kaggle |
| kristinezheng | social | 3 | kristinezheng.github.io, lookit-jenga |
| M1shaaa | social | 3 | lab-bookshelf-, Python-Lookit-Uploads |

**Cumulative DB state: 1,011 repo_snapshots, 90 world_increments** (includes April 2026 prior sweep)

### GF(3) Color Distribution (Today's 67 Increments)
- ERGODIC trit=0 #d3869b: **22 increments**
- PLUS trit=1 #b8bb26: **23 increments**
- MINUS trit=-1 #cc241d: **22 increments**

GF(3) rule: `id%3==0 → ERGODIC #d3869b | id%3==1 → PLUS #b8bb26 | id%3==2 → MINUS #cc241d`

### Notable Repo Highlights

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,686 | — | 2026-05-24 |
| kubeflow/pipelines | 4,150 | Python | 2026-05-29 |
| kubeflow/spark-operator | 3,124 | Python | 2026-05-29 |
| kubeflow/trainer | 2,107 | Go | 2026-05-29 |
| kubeflow/katib | 1,685 | Python | 2026-05-29 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| plurigrid/asi | 23 | HTML | 2026-04-26 |
| plurigrid/gorj | 0 | Clojure | 2026-05-29 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

> Note: Accounts use Fungible Asset standard (not legacy CoinStore v1). Balances retrieved via `0x1::primary_fungible_store::balance`.

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| bob | 0x0a3c... | **12.6570** |
| F | 0x18a1... | **1.9605** |
| L | 0x7c2e... | **1.9273** |
| J | 0x4d96... | **1.8951** |
| alice | 0xc793... | 0.4364 |
| O | 0x7325... | 0.2101 |
| K | 0xa732... | 0.1620 |
| P | 0x6218... | 0.1401 |
| M | 0x6fed... | 0.1123 |
| N | 0xe7dd... | 0.1061 |
| Q | 0xac40... | 0.1032 |
| S | 0xb875... | 0.0918 |
| R | 0x7ce6... | 0.0902 |
| T | 0x3578... | 0.0737 |
| U | 0x7586... | 0.0558 |
| A | 0x8699... | 0.0518 |
| V | 0xb59d... | 0.0488 |
| Y | 0xd8e3... | 0.0444 |
| X | 0xa95c... | 0.0426 |
| W | 0x5f32... | 0.0407 |
| B | 0x3f89... | 0.0363 |
| Z | 0x7af0... | 0.0243 |
| D | 0xf776... | 0.0116 |
| C | 0x38b9... | 0.0102 |
| E | 0xdc1d... | 0.0094 |
| H | 0xce67... | 0.0017 |
| G | 0x69a3... | 0.0007 |
| I | 0x070f... | 0.0007 |

**Total across 28 wallets: 20.3448 APT**

### Multisig Contract Probes (5 contracts)

All 5 multisig contracts respond healthy with **2-of-2 signature threshold**.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4... | 2 | ✅ healthy |
| A-G | 0xf56c... | 2 | ✅ healthy |
| Y-Z | 0xd3ff... | 2 | ✅ healthy |
| S-T | 0x3b1c... | 2 | ✅ healthy |
| V-W | 0x40fa... | 2 | ✅ healthy |

### MNX Markets (testnet.mnx.fi)

**Status: SPA-only, no public JSON API.** Next.js app renders client-side only. `/api/markets` and `/api/v1/markets` return 404. `mnx_snapshots` table: 0 rows.

---

## DuckDB Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)
  -- 90 rows total (67 new today + 23 from April 2026 sweep)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)
  -- 1011 rows total (67 new today + 944 from prior sweeps)

aptos_snapshots(timestamp, world, address, balance_apt)
  -- 28 wallets, 20.3448 APT total

multisig_probes(timestamp, pair, address, sigs_required, healthy)
  -- 5 contracts, all 2-of-2, all healthy

mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
  -- 0 rows (SPA, no public API)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=**ERGODIC**
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=**MINUS**
