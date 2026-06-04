# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-29

## Sweep Metadata
- **Date:** 2026-04-29T03:14:00Z
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.2.1
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos Captured | Total Stars |
|--------|------|---------------|-------------|
| plurigrid | org | 100 | 65 |
| bmorphism | user | 100 | 246 |
| zubyul | user | 49 | 14 |
| kubeflow | org | 47 | 33,958 |
| migalkin | user (social graph) | 7 | 277 |
| wasita | user (social graph) | 6 | 3 |
| DJedamski | user (social graph) | 5 | 3 |
| AustinCStone | user (social graph) | 5 | 107 |
| TeglonLabs | org | 4 | 2 |
| kristinezheng | user (social graph) | 4 | 0 |
| M1shaaa | user (social graph) | 3 | 0 |
| **TOTAL** | | **330** | **34,675** |

### GF(3) Color Chain Distribution

| id % 3 | Trit | Color | Name | Count |
|--------|------|-------|------|-------|
| 0 | 0 | `#d3869b` | ERGODIC | 110 |
| 1 | +1 | `#b8bb26` | PLUS | 110 |
| 2 | -1 | `#cc241d` | MINUS | 110 |

GF(3) chain cycles evenly: 110 × ERGODIC, 110 × PLUS, 110 × MINUS across 330 world increments.

### Notable Repos

| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| kubeflow/pipelines | Python | 4,127 | 2026-04-29 |
| kubeflow/spark-operator | Python | 3,121 | 2026-04-28 |
| kubeflow/trainer | Go | 2,094 | 2026-04-28 |
| kubeflow/katib | Python | 1,681 | 2026-04-14 |
| migalkin/NodePiece | Python | 143 | 2026-03-02 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | OCaml | 60 | 2026-03-16 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| plurigrid/asi | HTML | 17 | 2026-04-26 |
| plurigrid/gorj | Clojure | 0 | 2026-04-29 |
| plurigrid/nanoclj-zig | Zig | 1 | 2026-04-25 |
| zubyul/voice-observatory | Python | 0 | 2026-04-24 |
| TeglonLabs/mathpix-gem | Ruby | 2 | 2026-01-01 |
| bmorphism/Gay.jl | Julia | 1 | 2026-04-29 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, Ledger ~5,043,378,240)

All 28 wallets queried via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Address (truncated) | Balance (APT) | Status |
|-------|-------------------|--------------|--------|
| alice | 0xc793...cc7b | 0.00 | resource_not_found |
| bob | 0x0a3c...512d | 0.00 | resource_not_found |
| A | 0x8699...9d7a | 0.00 | resource_not_found |
| B | 0x3f89...b13 | 0.00 | resource_not_found |
| C | 0x38b9...535e | 0.00 | resource_not_found |
| D | 0xf776...fdd1 | 0.00 | resource_not_found |
| E | 0xdc1d...8d36 | 0.00 | resource_not_found |
| F | 0x18a1...f71 | 0.00 | resource_not_found |
| G | 0x69a3...f32 | 0.00 | resource_not_found |
| H | 0xce67...300f | 0.00 | resource_not_found |
| I | 0x070f...1fc9 | 0.00 | resource_not_found |
| J | 0x4d96...f54 | 0.00 | resource_not_found |
| K | 0xa732...dc4 | 0.00 | resource_not_found |
| L | 0x7c2e...ba9 | 0.00 | resource_not_found |
| M | 0x6fed...f2e9 | 0.00 | resource_not_found |
| N | 0xe7dd...b2c | 0.00 | resource_not_found |
| O | 0x7325...89d | 0.00 | resource_not_found |
| P | 0x6218...948 | 0.00 | resource_not_found |
| Q | 0xac40...89a9 | 0.00 | resource_not_found |
| R | 0x7ce6...e10 | 0.00 | resource_not_found |
| S | 0xb875...386 | 0.00 | resource_not_found |
| T | 0x3578...588 | 0.00 | resource_not_found |
| U | 0x7586...956 | 0.00 | resource_not_found |
| V | 0xb59d...2c3 | 0.00 | resource_not_found |
| W | 0x5f32...b0 | 0.00 | resource_not_found |
| X | 0xa95c...47d | 0.00 | resource_not_found |
| Y | 0xd8e3...44c4 | 0.00 | resource_not_found |
| Z | 0x7af0...97c | 0.00 | resource_not_found |

`resource_not_found` = no native APT coin store registered. Accounts may hold non-APT assets or be funded via alternate token modules.

### Multisig Contract Probes (`0x1::multisig_account::num_signatures_required`)

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|-------------------|--------------|---------|
| A-B | 0x0da4...003 | 2 | ✅ |
| A-G | 0xf56c...096 | 2 | ✅ |
| S-T | 0x3b1c...883 | 2 | ✅ |
| V-W | 0x40fa...b6d | 2 | ✅ |
| Y-Z | 0xd3ff...883 | 2 | ✅ |

All 5/5 multisig contracts healthy — 2-of-N threshold confirmed.

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable via REST** — MNX testnet is a Next.js SPA communicating exclusively via WebSocket (`wss://api.testnet.mnx.fi`). All REST API paths returned HTTP 404. No market data extractable without a WebSocket client. `mnx_snapshots` table is empty for this sweep.

---

## DuckDB Table Counts

| Table | Rows | Description |
|-------|------|-------------|
| world_increments | 330 | GF(3) world increment log (one per repo) |
| repo_snapshots | 330 | Full repo metadata snapshot |
| aptos_snapshots | 28 | Hamming swarm wallet balances (alice, bob, A-Z) |
| multisig_probes | 5 | Multisig threshold probes |
| mnx_snapshots | 0 | MNX market data (unavailable this sweep) |

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
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS
