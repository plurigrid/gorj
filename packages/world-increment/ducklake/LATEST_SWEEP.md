# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-14

## Sweep Metadata
- **Date:** 2026-04-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources queried

| Source | Type | Repos captured | Notes |
|--------|------|---------------|-------|
| plurigrid | org | 100 | OK |
| DJedamski | user | 11 | OK |
| M1shaaa | user | 16 | OK |
| wasita | user | 31 | OK |
| kubeflow | org | 0 | rate-limited (unauthenticated public API) |
| TeglonLabs | org | 0 | rate-limited |
| bmorphism | user | 0 | rate-limited |
| zubyul | user | 0 | rate-limited |
| migalkin | user | 0 | rate-limited |
| kristinezheng | user | 0 | rate-limited |
| AustinCStone | user | 0 | rate-limited |

**Total this sweep:** 158 repos snapshotted  
**Cumulative in DB:** 1,102 repo_snapshots · 181 world_increments

### GF(3) Color Chain (this sweep — 158 increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 52 |
| 1 | `#b8bb26` | PLUS | 53 |
| −1 | `#cc241d` | MINUS | 53 |

GF(3) assignment rule:
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=−1, color=`#cc241d`, name=MINUS

### Top Repos by Stars (this sweep)

| Org/User | Repo | Language | Stars | Last Pushed |
|----------|------|----------|-------|-------------|
| plurigrid | asi | HTML | 16 | 2026-04-13 |
| plurigrid | ontology | JavaScript | 7 | 2025-05-27 |
| plurigrid | asi-skills | Julia | 3 | 2026-04-09 |
| plurigrid | zig-syrup | Zig | 2 | 2026-04-09 |
| DJedamski | awesome-ruby | — | 2 | 2018-01-02 |
| DJedamski | kaggle-titanic | Python | 2 | 2015-08-11 |
| plurigrid | nash-portal | Rust | 1 | 2026-04-14 |
| plurigrid | horse | TeX | 1 | 2026-04-12 |
| plurigrid | vivarium | Clojure | 1 | 2026-04-08 |

### Public Events
- **bmorphism**: rate-limited / no public events visible
- **zubyul**: rate-limited / no public events visible

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Resource: `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`  
Ledger version at time of query: ~4,875,165,926

| Label | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.00000000 |
| bob | 0x0a3c...2d5d | 0.00000000 |
| A | 0x8699...e9d7a | 0.00000000 |
| B | 0x3f89...cb13 | 0.00000000 |
| C | 0x38b9...535e | 0.00000000 |
| D | 0xf776...cfdd1 | 0.00000000 |
| E | 0xdc1d...8d36 | 0.00000000 |
| F | 0x18a1...cf71 | 0.00000000 |
| G | 0x69a3...c7f32 | 0.00000000 |
| H | 0xce67...300f | 0.00000000 |
| I | 0x070f...1fc9 | 0.00000000 |
| J | 0x4d96...7f54 | 0.00000000 |
| K | 0xa732...25dc4 | 0.00000000 |
| L | 0x7c2e...eba9 | 0.00000000 |
| M | 0x6fed...7f2e9 | 0.00000000 |
| N | 0xe7dd...51b2c | 0.00000000 |
| O | 0x7325...a89d | 0.00000000 |
| P | 0x6218...ec948 | 0.00000000 |
| Q | 0xac40...c89a9 | 0.00000000 |
| R | 0x7ce6...76e10 | 0.00000000 |
| S | 0xb875...0386 | 0.00000000 |
| T | 0x3578...4588 | 0.00000000 |
| U | 0x7586...f9956 | 0.00000000 |
| V | 0xb59d...af2c3 | 0.00000000 |
| W | 0x5f32...c7b0 | 0.00000000 |
| X | 0xa95c...3047d | 0.00000000 |
| Y | 0xd8e3...444c4 | 0.00000000 |
| Z | 0x7af0...197c | 0.00000000 |

> All 28 addresses returned `resource_not_found` — CoinStore not initialized (wallets have not received APT on mainnet).

### Multisig Contract Probes — 5/5 Healthy

Function: `0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ healthy |
| A-G | 0xf56c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

All 5 multisig accounts require **2-of-N signatures**. All probes returned `["2"]`.

### MNX Markets (testnet.mnx.fi)

**Status: SPA — market data unavailable via curl.**  
`testnet.mnx.fi` is a Next.js single-page application. All API paths (`/api/markets`,
`/api/v1/markets`, `/api/v1/tickers`) return the HTML shell. No REST endpoint is
accessible without a browser runtime executing the SPA.

---

## DuckDB Ducklake State

| Table | Total Rows | Latest Timestamp |
|-------|-----------|-----------------|
| world_increments | 181 | 2026-04-14 22:12 UTC |
| repo_snapshots | 1,102 | 2026-04-14 22:12 UTC |
| aptos_snapshots | 28 | 2026-04-14 22:12 UTC |
| multisig_probes | 5 | 2026-04-14 22:12 UTC |
| mnx_snapshots | 1 (placeholder) | 2026-04-14 22:12 UTC |

**DB path:** `packages/world-increment/ducklake/world-increments.duckdb`

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

## Notable Highlights (cumulative)
- **kubeflow/kubeflow**: 15,565 stars (prior sweep) — flagship ML platform for Kubernetes
- **bmorphism/ocaml-mcp-sdk**: 60 stars (prior sweep) — OCaml MCP SDK
- **migalkin/NodePiece**: 143 stars (prior sweep) — scalable KG embeddings
- **plurigrid/asi**: 16 stars — topological chemputer (active, pushed 2026-04-13)
- **plurigrid/nash-portal**: Rust, pushed 2026-04-14 (most recent activity)
- **Multisig swarm**: All 5 pairs (A-B, A-G, Y-Z, S-T, V-W) healthy with 2-of-N threshold
- **Hamming swarm**: All 28 APT wallets show zero balance — uninitialized on mainnet
