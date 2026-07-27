# World-Increment Sweep — 2026-07-27

## Sweep Metadata
- **Date:** 2026-07-27
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Ledger version (Aptos):** 6,475,053,288
- **Aptos block height:** 928,898,092

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 15 |
| New Increments This Run | 3 (ids 13–15) |
| GitHub Sources Reached | 1 (plurigrid/gorj — proxy 403 for others) |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | SPA (no data API) |

---

## GF(3) Color Chain — New Increments (13–15)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | plurigrid (github_sweep_partial) | github_sweep_partial | +1 | `#b8bb26` | **PLUS** |
| 14 | aptos_mainnet | hamming_swarm_snapshot | -1 | `#cc241d` | **MINUS** |
| 15 | gorj (system) | sweep_complete | 0 | `#d3869b` | **ERGODIC** |

GF(3) rule: `id mod 3 == 0` → ERGODIC, `id mod 3 == 1` → PLUS, `id mod 3 == 2` → MINUS

Cumulative chain (ids 1–15): `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## JOB 1: GitHub Social Graph Sweep

### Proxy Restriction
Direct GitHub API calls (`api.github.com`) returned **403 Forbidden** via the environment proxy — the session token only authorises the GitHub MCP, which is scoped to `plurigrid/gorj`.

All other targets (orgs: kubeflow, TeglonLabs; users: bmorphism, zubyul, migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone) were unreachable this run.

For comparison, the last successful full sweep (2026-04-12) captured:

| Source | Repos |
|--------|-------|
| plurigrid | 100 |
| bmorphism | 100 |
| TeglonLabs | 53 |
| kubeflow | 47 |
| AustinCStone | 43 |
| migalkin | 30 |
| wasita | 29 |
| zubyul | 24 |
| kristinezheng | 18 |
| M1shaaa | 16 |
| DJedamski | 11 |
| **TOTAL** | **471** |

### plurigrid/gorj (in-scope snapshot)
| Field | Value |
|-------|-------|
| Full name | plurigrid/gorj |
| Language | Clojure |
| Description | MCP server + hooks giving AI coding agents a Clojure REPL |
| Latest commit | 2026-05-08 (chore: ignore duckdb binary in repo root) |
| Commits seen | 10 recent (all from claude bot) |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (2026-07-27 09:15 UTC)
> Queried via `0x1::coin::balance` view function on `fullnode.mainnet.aptoslabs.com`
> Note: CoinStore resource 404 for all addresses — accounts use legacy coin module (not FA)

| World | Balance (APT) | Address |
|-------|--------------|---------|
| bob | **12.65700700** | `0x0a3c00c5...d5d` |
| F | **1.96051600** | `0x18a14b5b...f71` |
| L | **1.92726900** | `0x7c2eaeaf...ba9` |
| J | **1.89509300** | `0x4d964db8...f54` |
| alice | 0.43643352 | `0xc793acde...c7b` |
| O | 0.21013600 | `0x73252b60...89d` |
| K | 0.16196100 | `0xa732040a...dc4` |
| P | 0.14013600 | `0x62187926...948` |
| M | 0.11228500 | `0x6fed37a7...2e9` |
| N | 0.10612100 | `0xe7dde6da...b2c` |
| Q | 0.10324000 | `0xac40fa50...a9` |
| S | 0.09178800 | `0xb8753014...386` |
| R | 0.09021700 | `0x7ce605cc...e10` |
| T | 0.07371300 | `0x35781dc0...588` |
| U | 0.05577300 | `0x75860da4...956` |
| A | 0.05176700 | `0x8699edc0...a7a` |
| Y | 0.04444900 | `0xd8e32848...4c4` |
| V | 0.04883299 | `0xb59dd817...2c3` |
| X | 0.04257700 | `0xa95cbbd1...47d` |
| W | 0.04070500 | `0x5f32aef7...7b0` |
| B | 0.03625600 | `0x3f892ebe...b13` |
| Z | 0.02426800 | `0x7af0ef6e...97c` |
| D | 0.01162900 | `0xf7765624...dd1` |
| C | 0.01018500 | `0x38b99e63...35e` |
| E | 0.00937200 | `0xdc1d9d53...d36` |
| H | 0.00168100 | `0xce67c327...00f` |
| G | 0.00068100 | `0x69a394c0...f32` |
| I | 0.00068100 | `0x070fe5d7...fc9` |
| **TOTAL** | **20.34477251 APT** | |

**Notable:**
- `bob` holds 62.2% of total swarm APT (12.657 APT)
- `F`, `L`, `J` each hold ~1.9 APT — the next tier
- `G`, `H`, `I` are dust (<0.002 APT) — likely gas-only accounts
- `alice` (seq 72) has active custom contracts: `store_v2::ACSetMeta2`, `address_book::Mapping`, `multiverse::MultiverseState`

### Multisig Contracts (5/5 healthy)

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4f428...003` | 2-of-N | ✓ healthy |
| A-G | `0xf56c4a1c...096` | 2-of-N | ✓ healthy |
| Y-Z | `0xd3ffe181...883` | 2-of-N | ✓ healthy |
| S-T | `0x3b1c3ae9...883` | 2-of-N | ✓ healthy |
| V-W | `0x40fad7b4...b6d` | 2-of-N | ✓ healthy |

All 5 multisig contracts responsive and requiring 2 signatures. No anomalies.

---

## MNX Markets

`testnet.mnx.fi` serves a Next.js SPA — no structured data API discovered at common paths
(`/api/markets`, `/api/v1/markets`, `/markets`, `/api/tickers`). All paths return the same HTML shell;
market data renders client-side only. **Status: unavailable for data extraction.**

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

## Notable Highlights (historical)
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — most popular ML pipeline for Kubernetes
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **plurigrid/asi**: 16 stars — topological chemputer
- **Increment 15**: ERGODIC — sweep_complete, closes 5th GF(3) cycle
