# World-Increment Sweep + Hamming Snapshot — 2026-08-05

## Sweep Metadata
- **Date:** 2026-08-05
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos found |
|--------|------|-------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social_graph | 19 |
| DJedamski | social_graph | 6 |
| wasita | social_graph | 14 |
| kristinezheng | social_graph | 5 |
| M1shaaa | social_graph | 8 |
| AustinCStone | social_graph | 20+ |
| **TOTAL this run** | | **~320** |

### Notable Recent Activity (top pushes as of 2026-08-05)

| Repo | Language | Stars | Last pushed |
|------|----------|-------|-------------|
| plurigrid/gorj | Clojure | 1 | 2026-08-05 |
| kubeflow/sdk | Python | 132 | 2026-08-05 |
| bmorphism/Gay.jl | Julia | 2 | 2026-08-05 |
| kubeflow/mcp-apache-spark-history-server | Python | 185 | 2026-08-04 |
| wasita/xoxowasita-analysis | Python | 0 | 2026-08-04 |
| kubeflow/pipelines | Python | 4176 | 2026-08-04 |
| plurigrid/zig-syrup | Zig | 2 | 2026-07-28 |
| TeglonLabs/jank-crane | C++ | 0 | 2026-06-08 |
| migalkin/kgcourse2021 | HTML | 24 | 2026-07-10 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |

### GF(3) Color Chain Distribution (this run)

| GF(3) trit | Color | Name | Count |
|-----------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 113 |
| +1 | #b8bb26 | PLUS | 115 |
| -1 | #cc241d | MINUS | 115 |

GF(3) rule: `id%3==0 → ERGODIC, id%3==1 → PLUS, id%3==2 → MINUS`

### DuckDB Tables (cumulative all-time)

| Table | Total rows |
|-------|-----------|
| world_increments | 343 |
| repo_snapshots | 1264 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice + A–Z, 28 addresses)

All 28 addresses probed at ledger version ~661,915,xxx.  
**Result: APT CoinStore resource not found on any address.**  
Accounts exist on-chain but do not hold the legacy `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource — consistent with accounts that have never received APT or operate exclusively under the Fungible Asset (FA) standard.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793…cc7b | NULL (no CoinStore) |
| bob | 0x0a3c…512d | NULL (no CoinStore) |
| A | 0x8699…9d7a | NULL (no CoinStore) |
| B | 0x3f89…b13 | NULL (no CoinStore) |
| C | 0x38b9…35e | NULL (no CoinStore) |
| D | 0xf776…dd1 | NULL (no CoinStore) |
| E | 0xdc1d…d36 | NULL (no CoinStore) |
| F | 0x18a1…f71 | NULL (no CoinStore) |
| G | 0x69a3…f32 | NULL (no CoinStore) |
| H | 0xce67…00f | NULL (no CoinStore) |
| I | 0x070f…c9 | NULL (no CoinStore) |
| J | 0x4d96…f54 | NULL (no CoinStore) |
| K | 0xa732…dc4 | NULL (no CoinStore) |
| L | 0x7c2e…a9 | NULL (no CoinStore) |
| M | 0x6fed…e9 | NULL (no CoinStore) |
| N | 0xe7dd…b2c | NULL (no CoinStore) |
| O | 0x7325…89d | NULL (no CoinStore) |
| P | 0x6218…948 | NULL (no CoinStore) |
| Q | 0xac40…9a9 | NULL (no CoinStore) |
| R | 0x7ce6…e10 | NULL (no CoinStore) |
| S | 0xb875…386 | NULL (no CoinStore) |
| T | 0x3578…588 | NULL (no CoinStore) |
| U | 0x7586…956 | NULL (no CoinStore) |
| V | 0xb59d…2c3 | NULL (no CoinStore) |
| W | 0x5f32…7b0 | NULL (no CoinStore) |
| X | 0xa95c…47d | NULL (no CoinStore) |
| Y | 0xd8e3…4c4 | NULL (no CoinStore) |
| Z | 0x7af0…97c | NULL (no CoinStore) |

### Multisig Contract Probes (5 pairs)

All 5 pairs healthy — all require exactly 2 signatures (2-of-N).

| Pair | Address | Sigs required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4…003 | 2 | ✓ |
| A-G | 0xf56c…096 | 2 | ✓ |
| Y-Z | 0xd3ff…883 | 2 | ✓ |
| S-T | 0x3b1c…883 | 2 | ✓ |
| V-W | 0x40fa…b6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: SPA only — no REST API accessible.**  
`testnet.mnx.fi` returns a Next.js single-page application (59 KB HTML). Neither `/api/markets` nor `/api/v1/markets` responds with JSON — both paths return the HTML shell. Market data is rendered client-side; no mnx_snapshot rows inserted this run.

---

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

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

## Notable Highlights
- **kubeflow/pipelines**: 4,176 stars, pushed 2026-08-04 — most active kubeflow repo
- **kubeflow/mcp-apache-spark-history-server**: 185 stars — new addition since last sweep
- **migalkin/NodePiece**: 144 stars (+1) — ICLR'22 KG embeddings still gaining
- **bmorphism/Gay.jl**: pushed 2026-08-05 — most recently active bmorphism repo
- **wasita/xoxowasita-analysis**: brand-new repo (created 2026-08-04) — fresh activity
- **Multisig swarm**: all 5 pairs (A-B, A-G, Y-Z, S-T, V-W) healthy at 2-of-N
- **Aptos hamming swarm**: all 28 accounts lack legacy CoinStore; FA migration likely
