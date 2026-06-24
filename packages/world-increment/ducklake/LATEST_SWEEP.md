# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-24  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB version:** v1.5.4 (Variegata)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — 11 World-Increments

| ID | GF3 | Color | Source Type | Source |
|----|-----|-------|-------------|--------|
| 1 | ERGODIC (0) | `#d3869b` | org | plurigrid |
| 2 | PLUS (+1) | `#b8bb26` | org | kubeflow |
| 3 | MINUS (-1) | `#cc241d` | org | TeglonLabs |
| 4 | ERGODIC (0) | `#d3869b` | user | bmorphism |
| 5 | PLUS (+1) | `#b8bb26` | user | zubyul |
| 6 | MINUS (-1) | `#cc241d` | user | migalkin |
| 7 | ERGODIC (0) | `#d3869b` | user | DJedamski |
| 8 | PLUS (+1) | `#b8bb26` | user | wasita |
| 9 | MINUS (-1) | `#cc241d` | user | kristinezheng |
| 10 | ERGODIC (0) | `#d3869b` | user | M1shaaa |
| 11 | PLUS (+1) | `#b8bb26` | user | AustinCStone |

GF(3) chain: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

### Repo Snapshot Summary (108 repos snapshotted)

| Org/User | Repos | Top Repo (by stars) | Stars |
|----------|-------|---------------------|-------|
| kubeflow | 20 | kubeflow/kubeflow | 15742 |
| AustinCStone | 8 | TextGAN | 92 |
| migalkin | 6 | NodePiece | 144 |
| bmorphism | 15 | risc0-cosmwasm-example / anti-bullshit-mcp-server | 23 |
| plurigrid | 20 | vcg-auction | 7 |
| wasita | 8 | magic-garden | 2 |
| TeglonLabs | 5 | mathpix-gem | 2 |
| zubyul | 10 | gay-world | 1 |
| DJedamski | 5 | School / Getting-and-Cleaning-Data | 1 |
| kristinezheng | 5 | (all 0★) | 0 |
| M1shaaa | 5 | (all 0★) | 0 |

### Notable Activity (2026-06-24)

- **plurigrid/gorj** (this repo): 787 open issues, pushed 2026-06-24 — active
- **plurigrid/place**: 9 open issues, pushed 2026-06-24 — active
- **plurigrid/eirobri**: 30 open issues, pushed 2026-06-23 — active
- **kubeflow/mcp-server**: new (17★), MCP tooling for Kubeflow with AI-assisted dev
- **kubeflow/mcp-apache-spark-history-server**: 178★, new Spark history MCP server
- **kubeflow/pipelines**: 4157★, 456 open issues — busiest kubeflow repo
- **bmorphism/Gay.jl**: 187 open issues — very active GF(3) color/SPI work
- **bmorphism/ocaml-mcp-sdk**: 61★ — OCaml MCP SDK using Jane Street oxcaml_effect
- **bmorphism/anti-bullshit-mcp-server**: 23★ — epistemic source validation MCP
- **TeglonLabs/jank-crane**: new (2026-06-08), GF3 convergence maps + loopify pass spec
- **migalkin/NodePiece**: 144★ — top academic KG embedding (ICLR'22)
- **zubyul/nash-tui** + **nash-web**: new Rust NASH TUI / WASM browser apps

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets — alice, bob, A–Z)

All 28 hamming-swarm wallets returned **0.0 APT** on mainnet. The
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource is not initialized
on any of these accounts — they are unfunded.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...e9d7a | 0.0 |
| B–Z | (25 more) | 0.0 each |

### Multisig Contract Probes (5 pairs — all HEALTHY)

All 5 multisig accounts on Aptos mainnet respond to
`0x1::multisig_account::num_signatures_required` with **2 of 2**.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets

`https://testnet.mnx.fi` — **UNAVAILABLE**  
All probed API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`) return a
Vercel authentication gate. No market data extractable without bypass credentials.

---

## DuckDB Table Counts

| Table | Rows |
|-------|------|
| world_increments | 11 |
| repo_snapshots | 108 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

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

- `id % 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id % 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id % 3 == 2` → trit=-1, color=#cc241d, name=MINUS
