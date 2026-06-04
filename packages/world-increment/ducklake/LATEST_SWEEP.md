# World Increment Sweep + Hamming Swarm Snapshot — 2026-05-08

## Sweep Metadata
- **Date:** 2026-05-08
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Aptos Ledger Version at probe:** 5182851956

---

## Summary Counts

| Metric | Today | Cumulative |
|--------|-------|------------|
| World Increments | 52 | 75 |
| Repo Snapshots | 52 | 996 |
| Aptos Addresses Probed | 28 | 28 |
| Multisig Contracts Probed | 5 | 5 |
| Sources Covered | 11 orgs/users | — |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Discovered |
|--------|------|-----------------|
| plurigrid | org | 100 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social (zubyul graph) | 19 |
| DJedamski | social (zubyul graph) | 6 |
| wasita | social (zubyul graph) | 11 |
| kristinezheng | social (zubyul graph) | 6 |
| M1shaaa | social (zubyul graph) | 8 |
| AustinCStone | social (zubyul graph) | 30 |
| **TOTAL** | | **380+** |

### GF(3) Color Chain (Today — 52 Increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 18 |
| 1 | `#b8bb26` | PLUS | 17 |
| -1 | `#cc241d` | MINUS | 17 |

GF(3) chain rule: `id%3==0 → ERGODIC · id%3==1 → PLUS · id%3==2 → MINUS`

### Top Repos by Stars (Today's Sample)

| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15,625 | — | 2026-05-07 |
| kubeflow/pipelines | 4,136 | Python | 2026-05-08 |
| kubeflow/spark-operator | 3,124 | Python | 2026-05-05 |
| kubeflow/trainer | 2,095 | Go | 2026-05-07 |
| kubeflow/katib | 1,683 | Python | 2026-05-08 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |

### Notable Activity (Since Last Sweep 2026-04-12)

- **plurigrid/gorj** (this repo): 106 open issues, pushed 2026-05-08 — active Clojure REPL orchestration
- **plurigrid/nanoclj-zig**: Zig 0.15, GF(3) trit conservation, 20 open issues (pushed 2026-04-25)
- **plurigrid/zig-syrup**: New — OCapN Syrup in Zig, 2 stars (pushed 2026-04-30)
- **plurigrid/nash-portal**: New — NASH token TUI via ratzilla WASM (pushed 2026-04-26)
- **bmorphism/Gay.jl**: 1 star, **187 open issues** — SPI splittable determinism very active
- **bmorphism/postweb**: New — evolved from prepostweb (pushed 2026-04-09)
- **zubyul/voice-observatory**: New — macOS TUI for voice pathway observation (pushed 2026-04-24)
- **kubeflow/pipelines**: 4,136 stars (+17 since April), pushed today
- **kubeflow/mcp-apache-spark-history-server**: New — MCP server for Spark debug (166 stars)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 Addresses)

All 28 Hamming swarm addresses queried via  
`GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

**Status:** All 28 addresses return 0.0 APT.  
The `CoinStore` resource was not found for any address — accounts either hold no APT  
or use the newer Fungible Asset (FA) standard rather than the legacy coin standard.

| World | Address | Balance (APT) |
|-------|---------|--------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...e9d7 | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...f588 | 0.0 |
| U | 0x7586...f956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

### Multisig Contract Probes (5 Pairs)

All 5 multisig contracts probed via  
`POST /v1/view { function: "0x1::multisig_account::num_signatures_required" }`

**Status: ALL HEALTHY — 2-of-N threshold across all pairs.**

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` is a Next.js SPA (client-side rendered).  
Probed: `/api/markets`, `/api/v1/markets`, root `/`  
**Result: Unavailable via REST API** — all endpoints return HTML shell.  
Market data requires JavaScript execution. Recorded 0 rows in `mnx_snapshots`.

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
