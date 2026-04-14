# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-14

## Sweep Metadata
- **Date:** 2026-04-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Prior sweep:** 2026-04-12 (471 repo_snapshots, 12 increments)

---

## Summary Counts (Cumulative)

| Metric | Prior (2026-04-12) | This Sweep | Total |
|--------|-------------------|------------|-------|
| World Increments | 12 | 196 | 208 |
| Repo Snapshots | 471 | 196 | 667 |
| Aptos Snapshots | 0 | 28 | 28 |
| Multisig Probes | 0 | 5 | 5 |
| GF(3) PLUS (#b8bb26) | — | — | 70 |
| GF(3) MINUS (#cc241d) | — | — | 69 |
| GF(3) ERGODIC (#d3869b) | — | — | 69 |

---

## JOB 1: GitHub Social Graph Sweep (2026-04-14)

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 99 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 22 (top active) |
| zubyul | user | 10 (top active) |
| migalkin | social-graph | 4 |
| DJedamski | social-graph | 2 |
| wasita | social-graph | 3 |
| kristinezheng | social-graph | 1 |
| M1shaaa | social-graph | 1 |
| AustinCStone | social-graph | 3 |
| **TOTAL (this sweep)** | | **196** |

### Top Repos by Stars (This Sweep)

| Repo | Stars | Language |
|------|-------|----------|
| migalkin/NodePiece | 143 | Python |
| migalkin/StarE | 88 | Python |
| AustinCStone/TextGAN | 92 | Python |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml |
| bmorphism/risc0-cosmwasm-example | 23 | Rust |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |
| bmorphism/say-mcp-server | 20 | JavaScript |
| bmorphism/babashka-mcp-server | 18 | JavaScript |

### Most Recently Pushed (2026-04-13 or later)

| Repo | Pushed | Language |
|------|--------|----------|
| bmorphism/boxxy | 2026-04-13 | Move |
| zubyul/nash-web | 2026-04-13 | Rust |
| zubyul/nash-tui | 2026-04-13 | Rust |
| wasita/wasita.github.io | 2026-04-13 | Svelte |
| bmorphism/penrose-mcp | 2026-04-12 | JavaScript |
| wasita/ch3-lib | 2026-04-12 | Typst |

### GF(3) Color Chain — Increment Sequence (This Sweep, first 12)

| ID | Source | GF3 Trit | Color | Name |
|----|--------|----------|-------|------|
| 1  | plurigrid/gmgm | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow/xgboost-operator | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs/topoi | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism/zeldar | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul/gay-world | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin/NodePiece | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski/Kaggle | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita/wasita.github.io | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng/kristinezheng.github.io | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa/M1shaaa | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone/TextGAN | -1 | `#cc241d` | **MINUS** |
| 12 | bmorphism/signal-mcp | 0 | `#d3869b` | **ERGODIC** |

Chain continues for all 196 repo increments...

---

## JOB 2: Hamming Swarm Snapshot (2026-04-14)

### Aptos Wallet Balances (Mainnet)

All 28 addresses probed via `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. All returned **0 APT** — CoinStore resources not initialized or unfunded.

| World | Address | Balance (APT) |
|-------|---------|:-------------:|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...c9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...e9 | 0.0 |
| N | 0xe7dd...2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...9a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...7b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

**Total APT across swarm: 0.0 APT**  
Swarm is in initialization state — addresses exist on-chain but CoinStore not yet funded.

### Multisig Contract Probes

All 5 probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|:-------------:|:-------:|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**5/5 healthy.** All pairs require 2-of-N signatures — uniform 2-sig governance across the Hamming swarm lattice.

### MNX Markets (`testnet.mnx.fi`)

Probed: `/api/markets`, `/api/v1/markets`, `/api/tickers` — all return HTML SPA shell.  
**Status: UNAVAILABLE** — client-side SPA, no REST API accessible from curl. `mnx_snapshots` table has 0 rows.

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

## Cumulative Highlights
- **kubeflow/kubeflow**: 15,572 stars — flagship ML platform
- **kubeflow/pipelines**: 4,119 stars — ML pipelines for Kubernetes
- **migalkin/NodePiece**: 143 stars — knowledge graph embeddings (ICLR'22)
- **AustinCStone/TextGAN**: 92 stars — text generation GAN
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml MCP SDK with Jane Street oxcaml_effect
- **bmorphism/anti-bullshit-mcp-server**: 23 stars — epistemological claim validator
- **zubyul/nash-tui + nash-web**: pushed 2026-04-13 — NASH token TUI (Rust)
- **bmorphism/boxxy**: pushed 2026-04-13 — Move lang
- **All 5 multisig contracts**: healthy, 2-sig threshold
- **Hamming swarm**: 28 wallets, 0 APT — initialization state
