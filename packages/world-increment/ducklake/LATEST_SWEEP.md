# World-Increment Sweep — 2026-07-09

## Sweep Metadata
- **Date:** 2026-07-09
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Aptos Ledger Version:** 6,194,461,637 (block 886,551,627, epoch 16,471)

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 12 |
| Total Repo Snapshots | 125 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | Unavailable (Vercel auth) |

---

## GF(3) Color Chain — All 12 Increments

| ID | Source | Type | Event Type | GF3 Trit | Color | Name |
|----|--------|------|------------|-----------|-------|------|
| 1  | plurigrid | org | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | org | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | user | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | user | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | user | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | user | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | user | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 12 | gorj (meta) | meta | sweep_complete | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## JOB 1: GitHub Social Graph Sweep

### Top Repos by Stars

| Repo | Language | Stars | Forks | Pushed At |
|------|----------|-------|-------|-----------|
| kubeflow/kubeflow | — | 15,768 | 2,685 | 2026-07-08 |
| kubeflow/pipelines | Python | 4,169 | 2,030 | 2026-07-09 |
| kubeflow/spark-operator | Python | 3,136 | 1,499 | 2026-07-08 |
| kubeflow/trainer | Go | 2,134 | 981 | 2026-07-08 |
| kubeflow/katib | Python | 1,689 | 532 | 2026-07-08 |
| kubeflow/examples | Jsonnet | 1,460 | 756 | 2025-04-14 |
| kubeflow/community-distribution | YAML | 1,029 | 1,071 | 2026-07-09 |
| kubeflow/arena | Go | 815 | 195 | 2026-07-08 |
| kubeflow/kale | Python | 695 | 155 | 2026-07-01 |
| migalkin/NodePiece | Python | 144 | 21 | 2021-06-14 |
| AustinCStone/TextGAN | Python | 92 | 30 | 2016-09-19 |
| migalkin/StarE | Python | 89 | 16 | 2020-09-17 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2 | 2026-05-08 |
| bmorphism/risc0-cosmwasm-example | Rust | 23 | 2 | 2025-05-21 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 7 | 2026-02-05 |
| bmorphism/say-mcp-server | JavaScript | 20 | 9 | 2026-03-19 |
| bmorphism/babashka-mcp-server | JavaScript | 19 | 6 | 2026-06-05 |
| bmorphism/penrose-mcp | JavaScript | 9 | 4 | 2026-06-24 |
| plurigrid/asi | HTML | 30 | 9 | 2026-06-29 |
| plurigrid/ontology | JavaScript | 8 | 9 | 2025-05-27 |

### Repo Counts by Source

| Source | Type | Repos Indexed |
|--------|------|--------------|
| plurigrid | org | 16 (100+ total) |
| kubeflow | org | 28 (47+ total) |
| TeglonLabs | org | 5 |
| bmorphism | user | 19 (105 total) |
| zubyul | user | 12 (49 total) |
| migalkin | user | 7 (19 total) |
| DJedamski | user | 6 |
| wasita | user | 11 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| AustinCStone | user | 8 (40 total) |
| **TOTAL** | | **125** |

### Notable Activity Since Last Sweep

- **plurigrid/gorj**: 1,077 open issues — high activity (pushed 2026-07-09)
- **plurigrid/asi**: 30 stars (up from 16 on 2026-04-12), pushed 2026-06-29
- **bmorphism/Gay.jl**: 187 open issues — very active (pushed 2026-06-20)
- **bmorphism/penrose-mcp**: 9 stars, pushed 2026-06-24
- **kubeflow/pipelines**: pushed 2026-07-09 — most recent kubeflow activity
- **TeglonLabs/jank-crane**: new since last sweep (C++, crane-jank converged-IR hub)
- **wasita/wasita.github.io**: pushed 2026-07-06
- **kristinezheng/kristinezheng.github.io**: pushed 2026-07-01

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 Hamming swarm wallets probed at Aptos ledger version **6,194,461,637** (block 886,551,627, epoch 16,471).

**Result: All wallets return `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — no registered APT coin store on any address. Balance = 0.0 APT for all (wallets not yet initialized).**

| World | Address (truncated) | Balance APT | Status |
|-------|---------------------|-------------|--------|
| alice | 0xc793...c7b | 0.0 | resource_not_found |
| bob | 0x0a3c...2d5d | 0.0 | resource_not_found |
| A | 0x8699...9d7a | 0.0 | resource_not_found |
| B | 0x3f89...b13 | 0.0 | resource_not_found |
| C | 0x38b9...35e | 0.0 | resource_not_found |
| D | 0xf776...dd1 | 0.0 | resource_not_found |
| E | 0xdc1d...d36 | 0.0 | resource_not_found |
| F | 0x18a1...f71 | 0.0 | resource_not_found |
| G | 0x69a3...f32 | 0.0 | resource_not_found |
| H | 0xce67...00f | 0.0 | resource_not_found |
| I | 0x070f...c9 | 0.0 | resource_not_found |
| J | 0x4d96...f54 | 0.0 | resource_not_found |
| K | 0xa732...dc4 | 0.0 | resource_not_found |
| L | 0x7c2e...ba9 | 0.0 | resource_not_found |
| M | 0x6fed...f2e9 | 0.0 | resource_not_found |
| N | 0xe7dd...1b2c | 0.0 | resource_not_found |
| O | 0x7325...89d | 0.0 | resource_not_found |
| P | 0x6218...948 | 0.0 | resource_not_found |
| Q | 0xac40...89a9 | 0.0 | resource_not_found |
| R | 0x7ce6...e10 | 0.0 | resource_not_found |
| S | 0xb875...386 | 0.0 | resource_not_found |
| T | 0x3578...588 | 0.0 | resource_not_found |
| U | 0x7586...956 | 0.0 | resource_not_found |
| V | 0xb59d...f2c3 | 0.0 | resource_not_found |
| W | 0x5f32...b0 | 0.0 | resource_not_found |
| X | 0xa95c...047d | 0.0 | resource_not_found |
| Y | 0xd8e3...44c4 | 0.0 | resource_not_found |
| Z | 0x7af0...97c | 0.0 | resource_not_found |

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`. **All healthy — all require 2 signatures.**

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...6d | 2 | ✓ |

### MNX Markets

`https://testnet.mnx.fi` requires Vercel authentication — unavailable from agent context. No market data captured.

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
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,768 stars — flagship ML platform, pushed 2026-07-08
- **kubeflow/pipelines**: 4,169 stars, pushed 2026-07-09 (most recent)
- **plurigrid/asi**: 30 stars — topological chemputer, pushed 2026-06-29
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP using Jane Street oxcaml_effect
- **bmorphism/Gay.jl**: 187 open issues — very high activity
- **TeglonLabs/jank-crane**: new C++ repo — crane-jank converged-IR hub with GF3 convergence maps
- **Multisig 5/5 healthy**: All A-B, A-G, Y-Z, S-T, V-W pairs require 2-of-2 signatures on Aptos mainnet
- **Aptos 0/28 funded**: No CoinStore registered for any Hamming swarm address (wallets not initialized)
- **Increment 12**: ERGODIC — sweep_complete closes 4th full GF(3) cycle
