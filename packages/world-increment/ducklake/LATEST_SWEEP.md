# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-23

## Sweep Metadata
- **Date:** 2026-07-23
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 119 |
| Total Repo Snapshots | 119 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Total Repos | Indexed |
|--------|------|-------------|---------|
| plurigrid | org | 103 | 20 |
| kubeflow | org | 49 | 20 |
| TeglonLabs | org | 5 | 5 |
| bmorphism | user | 106 | 20 |
| zubyul | user | 49 | 12 |
| migalkin | user | 19 | 7 |
| DJedamski | user | 6 | 6 |
| wasita | user | 12 | 8 |
| kristinezheng | user | 5 | 5 |
| M1shaaa | user | 8 | 8 |
| AustinCStone | user | 41 | 8 |

### GF(3) Color Chain (first 12 of 119 increments)

| ID | Source | Repo | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 1  | plurigrid | asi | +1 | `#b8bb26` | **PLUS** |
| 2  | plurigrid | gorj | -1 | `#cc241d` | **MINUS** |
| 3  | plurigrid | shrimp | 0 | `#d3869b` | **ERGODIC** |
| 4  | plurigrid | place | +1 | `#b8bb26` | **PLUS** |
| 5  | plurigrid | eirobri | -1 | `#cc241d` | **MINUS** |
| 6  | plurigrid | nash-portal | 0 | `#d3869b` | **ERGODIC** |
| 7  | plurigrid | zig-syrup | +1 | `#b8bb26` | **PLUS** |
| 8  | plurigrid | asi-skills | -1 | `#cc241d` | **MINUS** |
| 9  | plurigrid | bci-blue-share | 0 | `#d3869b` | **ERGODIC** |
| 10 | plurigrid | nanoclj-zig | +1 | `#b8bb26` | **PLUS** |
| … | … | … | … | … | … |
| 119 | AustinCStone | Z-order-curve | -1 | `#cc241d` | **MINUS** |

GF(3) distribution: ERGODIC=39, PLUS=40, MINUS=40

### Notable Recent Activity

| Repo | Stars | Lang | Last Push |
|------|-------|------|-----------|
| kubeflow/kubeflow | 15,788 | — | 2026-07-22 |
| kubeflow/spark-operator | 3,142 | Python | 2026-07-21 |
| kubeflow/pipelines | 4,169 | Python | 2026-07-23 |
| kubeflow/trainer | 2,153 | Go | 2026-07-23 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-05-08 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| plurigrid/asi | 31 | HTML | 2026-07-17 |
| bmorphism/Gay.jl | 2 | Julia | 2026-07-21 |
| wasita/wasita.github.io | 1 | Svelte | 2026-07-21 |

### New Repos in Social Graph (≤30 days)
- `AustinCStone/byteruckus` — new 2026-07-15
- `wasita/pnas-typst-template` — new 2026-07-16
- `bmorphism/gay-chat` — gay://chat over Spritely Brassica Chat 2026-07-14
- `bmorphism/satreadout` — machine-checked saturating perceptual readout 2026-06-20

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)

**Status:** All 28 addresses returned HTTP 404 from Aptos mainnet fullnode.  
These wallets have no CoinStore resource registered — not yet activated on mainnet.

| World | Address | Balance APT |
|-------|---------|------------|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9… | NULL |
| bob   | 0x0a3c00c58fdf9020b27854a3229042efa70cf782… | NULL |
| A     | 0x8699edc0960dd5b916074f1e9bd25d86fb416a8… | NULL |
| B     | 0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2… | NULL |
| C–Z   | (24 more addresses) | NULL |

### Multisig Contract Probes — ALL HEALTHY ✅

All 5 multisig contracts returned `num_signatures_required = 2`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B  | 0x0da4f428a0c007da0f7629c3ec6a08a661ee208… | 2 | ✅ |
| A-G  | 0xf56c4a1c0906214f3f859ccd8b498ab673979df… | 2 | ✅ |
| Y-Z  | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6… | 2 | ✅ |
| S-T  | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae… | 2 | ✅ |
| V-W  | 0x40fad7b423a843650fddcad36b7de6609eead0c… | 2 | ✅ |

### MNX Markets (testnet.mnx.fi)

**Status:** UNAVAILABLE. `testnet.mnx.fi` is a client-rendered SPA.  
Probed paths: `/api/markets`, `/api/v1/markets`, `/api/tickers` — all HTTP 404.  
`mnx_snapshots` table is empty for this run.

---

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)           -- 119 rows

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)           -- 119 rows

aptos_snapshots(timestamp, world, address, balance_apt)  -- 28 rows, all NULL
multisig_probes(timestamp, pair, address, sigs_required, healthy)  -- 5 rows
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)  -- 0 rows
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
