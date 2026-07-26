# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-26

## Sweep Metadata
- **Date:** 2026-07-26
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos (this run) | Top Stars | Latest Push |
|--------|------|:----------------:|:---------:|-------------|
| plurigrid | org | 100 | asi (16★) | 2026-07-26 |
| kubeflow | org | 49 | kubeflow (15792★) | 2026-07-26 |
| TeglonLabs | org | 5 | mathpix-gem (2★) | 2026-06-08 |
| bmorphism | user | 14 | anti-bullshit-mcp (22★) | 2026-07-21 |
| zubyul | user | 10 | gay-world (1★) | 2026-04-24 |
| migalkin | user (social) | 5 | NodePiece (144★) | 2026-07-10 |
| DJedamski | user (social) | 2 | School (1★) | 2018-02-26 |
| wasita | user (social) | 3 | magic-garden (2★) | 2026-07-21 |
| kristinezheng | user (social) | 2 | (0★) | 2026-07-01 |
| M1shaaa | user (social) | 2 | (0★) | 2026-02-04 |
| AustinCStone | user (social) | 3 | TextGAN (92★) | 2026-04-01 |

**Total repos snapshotted this run: 195**
**Total world_increment events this run: 195**

### GF(3) Color Chain Distribution (this run)
- **ERGODIC** (trit=0, #d3869b): 65 events
- **PLUS** (trit=1, #b8bb26): 65 events
- **MINUS** (trit=-1, #cc241d): 65 events

GF(3) rule: `id%3==0 → ERGODIC #d3869b | id%3==1 → PLUS #b8bb26 | id%3==2 → MINUS #cc241d`

### Notable Active Repos (this run)

| Repo | Language | Stars | Last Pushed |
|------|----------|------:|-------------|
| kubeflow/kubeflow | — | 15,792 | 2026-07-10 |
| kubeflow/pipelines | Python | 4,169 | 2026-07-26 |
| kubeflow/spark-operator | Python | 3,142 | 2026-07-25 |
| kubeflow/trainer | Go | 2,154 | 2026-07-26 |
| kubeflow/katib | Python | 1,692 | 2026-07-26 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 22 | 2026-07-12 |
| bmorphism/say-mcp-server | JavaScript | 20 | 2026-03-19 |
| bmorphism/babashka-mcp-server | JavaScript | 19 | 2026-06-05 |
| migalkin/kgcourse2021 | HTML | 24 | 2026-07-10 |
| TeglonLabs/jank-crane | C++ | 0 | 2026-06-08 |

### Social Graph Notes
- **bmorphism**: Most recently active on `Gay.jl` (188 open issues!), `satreadout`, `nanoclj-zig`, `world`. MCP server portfolio: anti-bullshit, say, babashka, manifold, marginalia, penumbra.
- **zubyul**: Heavy GF(3)/Gay.jl ecosystem focus. Move (vibesnipe, GayMove) + EEG (openbci) + Aptos.
- **wasita**: SvelteKit personal site (active 2026-07-21), Discord automation, typst papers.
- **migalkin**: KG ML research — NodePiece (144★), StarE (89★), NBFNet_mlx. Very active.
- **TeglonLabs/jank-crane**: New (2026-06-08), GF3 convergence maps + simonw workflow for jank/crane IR.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 wallets queried via Aptos fullnode REST API with 1s sleep between calls.

| World | Balance (APT) | Notes |
|-------|:-------------:|-------|
| alice (0xc793…cc7b) | 0.0 | No APT balance |
| bob (0x0a3c…2d5d) | 0.0 | No APT balance |
| A–Z (26 Hamming wallets) | 0.0 each | All 26 return 0.0 |

> **All 28 addresses return 0.0 APT.** The Aptos node responds (no 404), meaning accounts are known but hold zero APT or have not initialized a `CoinStore<AptosCoin>` resource. Total Hamming swarm APT: **0.0 APT**.

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|:-------------:|:------:|
| A-B | 0x0da4…7003 | 2 | ✅ healthy |
| A-G | 0xf56c…0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff…b883 | 2 | ✅ healthy |
| S-T | 0x3b1c…7883 | 2 | ✅ healthy |
| V-W | 0x40fa…eb6d | 2 | ✅ healthy |

**All 5 multisig contracts are healthy — each configured as 2-of-2.**

### MNX Markets (testnet.mnx.fi)

- `GET /api/markets` → HTTP 404
- Root page → SPA shell, no market data rendered at crawl time
- **Status: UNAVAILABLE** — no market data accessible via public endpoints

---

## Cumulative DuckDB Ducklake State

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows (cumulative) |
|-------|:-----------------:|
| world_increments | 218+ |
| repo_snapshots | 1,139+ |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

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
