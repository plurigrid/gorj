# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-25T00:00Z  
**Ledger version at query time:** 6446542067 (Aptos mainnet)  
**DuckDB version:** v1.5.5 (Variegata)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Total Repos | Repos Sampled | Top Language |
|--------|------|-------------|---------------|--------------|
| plurigrid | org | 103 | 20 | Clojure/Zig/Rust |
| kubeflow | org | 49 | 12 | Python/Go |
| TeglonLabs | org | 5 | 5 | C++/Ruby/JS |
| bmorphism | user | 106 | 15 | Julia/OCaml/Zig |
| zubyul | user | 49 | 10 | Python/Rust/Julia |
| migalkin | user | 19 | 7 | Python/Rust |
| DJedamski | user | 6 | 6 | Jupyter/R |
| wasita | user | 12 | 8 | Svelte/TypeScript |
| kristinezheng | user | 5 | 5 | HTML/Python |
| M1shaaa | user | 8 | 8 | TypeScript |
| AustinCStone | user | 41 | 8 | Python/Haskell |

**Total repo_snapshots in DB:** 1048 rows (cumulative)  
**New inserts this run:** 104  
**world_increments in DB:** 34 rows (cumulative)

### Notable Recent Activity (by pushed_at)

- **plurigrid/asi** (HTML, ⭐31): "everything is topological chemputer!" — 2026-07-17
- **kubeflow/kubeflow** (⭐15793): Main ML Toolkit for Kubernetes — pushed 2026-07-25
- **kubeflow/sdk** (Python, ⭐127): Universal Python SDK for AI workloads — pushed 2026-07-24
- **kubeflow/pipelines** (Python, ⭐4169): ML Pipelines — pushed 2026-07-24
- **bmorphism/Gay.jl** (Julia, ⭐2): 188 open issues — pushed 2026-07-21
- **wasita/wasita.github.io** (Svelte): personal site — pushed 2026-07-21
- **bmorphism/anti-bullshit-mcp-server** (JS, ⭐22): MCP claims analysis — pushed 2026-07-12
- **migalkin/kgcourse2021** (HTML, ⭐24): Knowledge Graphs course — pushed 2026-07-10
- **plurigrid/gorj** (Clojure, ⭐1): This repo — pushed 2026-07-07; 1388 open issues

### GF(3) Color Chain (this run, increments 24–34)

| id%3 | trit | color | name | sources this run |
|------|------|-------|------|------------------|
| 0 | 0 | #d3869b | ERGODIC | plurigrid, TeglonLabs, wasita, AustinCStone |
| 1 | 1 | #b8bb26 | PLUS | kubeflow, bmorphism, kristinezheng |
| 2 | -1 | #cc241d | MINUS | zubyul, migalkin, DJedamski, M1shaaa |

Chain: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ...`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

**Status:** All 28 addresses (alice, bob, A–Z) returned `resource_not_found` for  
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version 6446542067.

The Hamming swarm addresses have no registered APT CoinStore on mainnet —  
the accounts either do not exist on-chain or have never received APT.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.0 (uninitialized) |
| bob | 0x0a3c...512d | 0.0 (uninitialized) |
| A | 0x8699...e9d7 | 0.0 (uninitialized) |
| B | 0x3f89...cb13 | 0.0 (uninitialized) |
| C | 0x38b9...535e | 0.0 (uninitialized) |
| D | 0xf776...fdd1 | 0.0 (uninitialized) |
| E | 0xdc1d...8d36 | 0.0 (uninitialized) |
| F | 0x18a1...cf71 | 0.0 (uninitialized) |
| G | 0x69a3...7f32 | 0.0 (uninitialized) |
| H | 0xce67...300f | 0.0 (uninitialized) |
| I | 0x070f...1fc9 | 0.0 (uninitialized) |
| J | 0x4d96...7f54 | 0.0 (uninitialized) |
| K | 0xa732...dc4 | 0.0 (uninitialized) |
| L | 0x7c2e...eba9 | 0.0 (uninitialized) |
| M | 0x6fed...f2e9 | 0.0 (uninitialized) |
| N | 0xe7dd...1b2c | 0.0 (uninitialized) |
| O | 0x7325...a89d | 0.0 (uninitialized) |
| P | 0x6218...c948 | 0.0 (uninitialized) |
| Q | 0xac40...89a9 | 0.0 (uninitialized) |
| R | 0x7ce6...6e10 | 0.0 (uninitialized) |
| S | 0xb875...0386 | 0.0 (uninitialized) |
| T | 0x3578...4588 | 0.0 (uninitialized) |
| U | 0x7586...f956 | 0.0 (uninitialized) |
| V | 0xb59d...f2c3 | 0.0 (uninitialized) |
| W | 0x5f32...c7b0 | 0.0 (uninitialized) |
| X | 0xa95c...047d | 0.0 (uninitialized) |
| Y | 0xd8e3...44c4 | 0.0 (uninitialized) |
| Z | 0x7af0...97c | 0.0 (uninitialized) |

### Multisig Contract Probes

All 5 multisig contracts responded successfully — all require 2 signatures (2-of-N).

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**All 5 multisig contracts healthy. All pairs require 2 signatures.**

### MNX Markets (testnet.mnx.fi)

**Status: SPA only** — `https://testnet.mnx.fi/api/markets` returns the Next.js HTML shell  
(client-side rendered via React/Vercel). No REST/JSON market data is available without  
JavaScript execution. `mnx_snapshots` table remains empty this run.

---

## DuckDB Summary

```
DB: packages/world-increment/ducklake/world-increments.duckdb

Tables (cumulative):
  world_increments  : 34 rows
  repo_snapshots    : 1048 rows
  aptos_snapshots   : 28 rows  (all 0.0 APT, uninitialized on mainnet)
  multisig_probes   : 5 rows   (all sigs_required=2, all healthy)
  mnx_snapshots     : 0 rows   (SPA, no JSON API accessible)
```

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

## Top Repos by Stars (this sweep)

| Repo | Stars | Language | Pushed At |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15793 | — | 2026-07-25 |
| kubeflow/pipelines | 4169 | Python | 2026-07-24 |
| kubeflow/spark-operator | 3143 | Python | 2026-07-23 |
| kubeflow/trainer | 2153 | Go | 2026-07-24 |
| kubeflow/katib | 1692 | Python | 2026-07-20 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-05-08 |
| plurigrid/asi | 31 | HTML | 2026-07-17 |
