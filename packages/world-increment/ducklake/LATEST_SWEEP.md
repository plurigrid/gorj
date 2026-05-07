# World-Increment Sweep + Hamming Snapshot — 2026-05-07

**Timestamp:** 2026-05-07 08:15:26 UTC  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB version:** v1.5.2 (Variegata)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) Color Chain:** ERGODIC #d3869b (trit=0) · PLUS #b8bb26 (trit=+1) · MINUS #cc241d (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| kubeflow | org | 94 | 67,723 |
| migalkin | user (social) | 60 | 554 |
| bmorphism | user | 210 | 352 |
| AustinCStone | user (social) | 86 | 216 |
| plurigrid | org | 229 | 110 |
| zubyul | user | 59 | 27 |
| TeglonLabs | org | 110 | 14 |
| DJedamski | user (social) | 22 | 14 |
| wasita | user (social) | 60 | 6 |
| kristinezheng | user (social) | 36 | 0 |
| M1shaaa | user (social) | 32 | 0 |

**Cumulative total:** 11 sources · 998 repo snapshots in DB

### Selected Recent Repos (pushed ≤ 48h)

| Repo | Lang | Stars | Pushed |
|------|------|-------|--------|
| plurigrid/gorj | Clojure | 0 | 2026-05-07T07:13Z |
| plurigrid/horse | TeX | 1 | 2026-05-07T04:35Z |
| bmorphism/nanoclj-zig | Zig | 0 | 2026-05-07T07:12Z |
| bmorphism/Gay.jl | Julia | 1 | 2026-05-07T00:31Z |
| plurigrid/zig-syrup | Zig | 2 | 2026-04-30T03:52Z |
| bmorphism/boxxy | Move | 0 | 2026-04-30T03:35Z |

### Recent Event Activity

**bmorphism** (top events):
- `CreateEvent` → bmorphism/nanoclj-zig (branch: codex/zig-0.16-final-latest) 2026-05-07
- `WatchEvent` → scicloj/janqua 2026-05-06
- `ForkEvent` → bmorphism/DynamicalSystemsWorlds (from DavidJaz/DynamicalSystemsBook) 2026-05-03
- `PushEvent` → plurigrid/zig-syrup 2026-04-30
- `PushEvent` → bmorphism/boxxy 2026-04-30

**zubyul** (top events):
- `CreateEvent` → plurigrid/gorj (world-increment/sweep-2026-05-07-0713) 2026-05-07
- `PullRequestEvent` → plurigrid/gorj (PR #381) 2026-05-07
- `PullRequestEvent` → plurigrid/horse (PR #27, bcf-0036-jlcpcb-gerber-fix) 2026-05-07
- Continuous sweep branch/PR creation pattern on gorj

### DuckDB Tables

- `world_increments` — 87 rows (GF3 color-chained increment log, cumulative)
- `repo_snapshots` — 998 rows (cumulative org/user repo snapshots)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 Hamming addresses probed via `GET https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` (1s sleep between calls).

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z (26 wallets) | 0x8699...→ 0x7af0... | 0.0 each |

> All CoinStore resources returned empty/404 — addresses hold zero native APT (may hold other tokens or be inactive).

### Multisig Contract Probes

`POST /v1/view` → `0x1::multisig_account::num_signatures_required`

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ healthy |
| A-G | 0xf56c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

All 5 multisig contracts healthy, all requiring 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — site returns Next.js SPA; no public JSON API endpoint exposed.  
Paths probed: `/api/markets`, `/api/v1/markets`, `/api/v2/markets`, `/api/tickers`.  
Market data not capturable without authenticated browser session.

### DuckDB Tables

- `aptos_snapshots` — 28 rows (1 per Hamming world address)
- `multisig_probes` — 5 rows (all healthy, 2-of-N)
- `mnx_snapshots` — 1 row (unavailable marker)

---

## GF(3) Trit Distribution (this sweep, 64 increments)

| GF(3) Name | Trit | Color | Count |
|------------|------|-------|-------|
| ERGODIC | 0 | `#d3869b` | 21 |
| PLUS | +1 | `#b8bb26` | 22 |
| MINUS | -1 | `#cc241d` | 21 |

GF(3) assignment:
- `id mod 3 == 0` → trit=0, ERGODIC `#d3869b`
- `id mod 3 == 1` → trit=+1, PLUS `#b8bb26`
- `id mod 3 == 2` → trit=-1, MINUS `#cc241d`

---

## Notable Highlights

- **plurigrid/gorj** (this repo): 92 open issues, Clojure, active world-increment sweep activity
- **bmorphism/Gay.jl**: 187 open issues, wide-gamut color sampling with splittable determinism
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **plurigrid/asi**: 20 stars — topological chemputer
- **bmorphism/anti-bullshit-mcp-server**: 23 stars — claim validation MCP server
- **kubeflow** org leads with 67,723 total stars across 94 repos
- All 5 Hamming multisig pairs alive and healthy on Aptos mainnet

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
