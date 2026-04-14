# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-04-14  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB version:** v1.5.2 (Variegata)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept This Run

| Source Type | Name | Repos Indexed |
|-------------|------|--------------|
| org | plurigrid | 99 |
| org | kubeflow | 49 |
| org | TeglonLabs | 4 |
| user | bmorphism | 14 |
| user | zubyul | 7 |
| social | migalkin | 3 |
| social | wasita | 2 |
| social | AustinCStone | 2 |
| social | DJedamski | 1 |
| social | kristinezheng | 1 |
| social | M1shaaa | 2 |

**World_increments added this run:** 182  
**Total world_increments in DB:** 205  
**Total repo_snapshots in DB:** 1,126

### Top Repos by Stars

| Repo | Language | Stars | Forks |
|------|----------|-------|-------|
| kubeflow/kubeflow | — | 15,575 | 2,636 |
| kubeflow/pipelines | Python | 4,119 | 1,985 |
| kubeflow/spark-operator | Python | 3,114 | 1,483 |
| kubeflow/trainer | Go | 2,082 | 946 |
| kubeflow/katib | Python | 1,678 | 521 |
| kubeflow/examples | Jsonnet | 1,459 | 756 |
| kubeflow/arena | Go | 809 | 190 |
| migalkin/NodePiece | Python | 143 | 21 |
| AustinCStone/TextGAN | Python | 92 | 30 |
| migalkin/StarE | Python | 88 | 16 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 7 |
| bmorphism/risc0-cosmwasm-example | Rust | 23 | 2 |
| bmorphism/say-mcp-server | JavaScript | 20 | 8 |
| bmorphism/babashka-mcp-server | JavaScript | 18 | 6 |
| bmorphism/marginalia-mcp-server | JavaScript | 8 | 6 |

### Language Distribution (top 10)

| Language | Count |
|----------|-------|
| Python | 184 |
| Go | 51 |
| Rust | 46 |
| HTML | 43 |
| TypeScript | 40 |
| JavaScript | 39 |
| Jupyter Notebook | 31 |
| Clojure | 24 |
| Jsonnet | 24 |
| R | 16 |

### Notable Recent Activity

**plurigrid** (pushed 2026-04-14):
- `plurigrid/gorj` — Clojure — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- `plurigrid/nash-portal` — Rust — NASH token TUI WASM + GeckoTerminal OHLCV candlesticks (1★)
- `plurigrid/asi` — HTML — topological chemputer (16★, pushed 2026-04-13)
- `plurigrid/nanoclj-zig` — Zig — NaN-boxed Clojure in Zig 0.15, interaction nets
- `plurigrid/zig-syrup` — Zig — OCapN Syrup + CapTP optimizations (2★)

**zubyul** (pushed 2026-04-13):
- `zubyul/nash-web` — Rust — NASH token WASM browser TUI
- `zubyul/nash-tui` — Rust — NASH token terminal TUI, GeckoTerminal OHLCV

**bmorphism** (pushed 2026-04-13):
- `bmorphism/boxxy` — Move — (pushed 2026-04-13)
- `bmorphism/penrose-mcp` — JavaScript — 10★, Penrose diagram MCP server

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 67 |
| +1 | `#b8bb26` | PLUS | 69 |
| -1 | `#cc241d` | MINUS | 69 |

GF(3) rule: `id%3==0` → ERGODIC `#d3869b`, `id%3==1` → PLUS `#b8bb26`, `id%3==2` → MINUS `#cc241d`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` for all 28 addresses. All returned 0 APT — CoinStore resources either absent or unfunded.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z (26 addrs) | 0x8699...→ 0x7af0... | 0.0 each |

### Multisig Contract Probes (`0x1::multisig_account::num_signatures_required`)

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...003 | **2** | ✓ healthy |
| A-G | 0xf56c...096 | **2** | ✓ healthy |
| Y-Z | 0xd3ff...883 | **2** | ✓ healthy |
| S-T | 0x3b1c...883 | **2** | ✓ healthy |
| V-W | 0x40fa...b6d | **2** | ✓ healthy |

All 5 multisig contracts are live and require 2-of-N signatures.

### MNX Markets (`testnet.mnx.fi`)

`testnet.mnx.fi` serves a Next.js SPA. Neither `/api/markets` nor `/api/v1/markets` returned JSON. Market data **unavailable** via server-rendered API at sweep time.

---

## DuckDB Tables

| Table | Rows |
|-------|------|
| world_increments | 205 |
| repo_snapshots | 1,126 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA only) |

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
