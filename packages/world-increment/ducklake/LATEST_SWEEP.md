# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-06

## Sweep Metadata
- **Date:** 2026-06-06
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 13 |
| kubeflow | org | 13 |
| TeglonLabs | org | 4 |
| bmorphism | user | 11 |
| zubyul | user | 8 |
| migalkin | user (zubyul social graph) | 6 |
| DJedamski | user (zubyul social graph) | 4 |
| wasita | user (zubyul social graph) | 4 |
| kristinezheng | user (zubyul social graph) | 5 |
| M1shaaa | user (zubyul social graph) | 5 |
| AustinCStone | user (zubyul social graph) | 6 |
| **TOTAL** | | **79** |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | ★15,706 | — | 2026-05-24 |
| kubeflow/pipelines | ★4,152 | Python | 2026-06-05 |
| kubeflow/spark-operator | ★3,125 | Python | 2026-06-04 |
| kubeflow/trainer | ★2,111 | Go | 2026-06-05 |
| kubeflow/katib | ★1,685 | Python | 2026-06-05 |
| migalkin/NodePiece | ★144 | Python | — |
| migalkin/StarE | ★89 | Python | — |
| AustinCStone/TextGAN | ★92 | Python | — |
| plurigrid/asi | ★25 | HTML | 2026-04-26 |
| bmorphism/ocaml-mcp-sdk | ★61 | OCaml | 2026-03-16 |

### Notable Plurigrid Activity (2026-06-06)

- **gorj** (this repo): 385 open issues, forj + Rama topology + GF(3) gay trit coloring
- **eirobri**: EiRoBri replay world — Clojure, 29 open issues
- **nash-portal**: NASH token TUI in WASM browser — Rust
- **nanoclj-zig**: NaN-boxed Clojure interpreter in Zig 0.15 with GF(3) trit conservation

### Notable bmorphism Activity (2026-06-06)

- **Gay.jl**: Wide-gamut color sampling with Pigeons.jl SPI — 189 open issues, pushed today
- **world**: Local worlds launcher for SA3/jank/world proofs — Python
- **ocaml-mcp-sdk**: OCaml SDK for MCP using Jane Street's oxcaml_effect — ★61

### GF(3) Color Chain Distribution (79 increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 26 |
| 1 | #b8bb26 | PLUS | 27 |
| -1 | #cc241d | MINUS | 26 |

Chain rule: `id%3==0 → ERGODIC`, `id%3==1 → PLUS`, `id%3==2 → MINUS`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

**28 worlds queried** (alice, bob, A–Z) via `fullnode.mainnet.aptoslabs.com`.

All wallets returned **0 APT** — the `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource is not initialized on these addresses, indicating they have not received APT on mainnet. This is expected for fresh/specialized Aptos accounts.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b | 0.0 |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d | 0.0 |
| A | 0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a | 0.0 |
| B | 0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13 | 0.0 |
| C | 0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e | 0.0 |
| D–Z | (see DB) | 0.0 each |

### Multisig Contract Probes

All 5 pairs probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | ✓ |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | ✓ |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | ✓ |

**All 5 multisig accounts healthy: 2-of-N threshold, all responsive.**

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — protected by Vercel deployment authentication. No market data accessible without a bypass token. `mnx_snapshots` table empty this sweep.

---

## DuckDB Schema

```sql
world_increments(id, ts, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)           -- 79 rows

repo_snapshots(id, ts, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)           -- 79 rows

aptos_snapshots(ts, world, address, balance_apt) -- 28 rows
multisig_probes(ts, pair, address, sigs_required, healthy) -- 5 rows
mnx_snapshots(ts, ticker, name, category, price, change_pct) -- 0 rows
```

## Query Examples

```sql
-- Top repos by stars
SELECT full_name, stars, language FROM repo_snapshots ORDER BY stars DESC LIMIT 10;

-- GF3 color chain view
SELECT gf3_name, gf3_color, source_name, repo_name FROM world_increments ORDER BY id;

-- All Aptos worlds
SELECT world, address, balance_apt FROM aptos_snapshots;

-- Multisig health
SELECT pair, sigs_required, healthy FROM multisig_probes;
```
