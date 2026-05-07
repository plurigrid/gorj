# World-Increment Sweep + Hamming Snapshot — 2026-05-07

## Sweep Metadata
- **Date:** 2026-05-07
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 390 |
| Total Repo Snapshots | 390 |
| Sources Covered | 3 orgs + 8 users |
| GF(3) ERGODIC (#d3869b) | 130 |
| GF(3) PLUS (#b8bb26) | 130 |
| GF(3) MINUS (#cc241d) | 130 |

### Repo Counts by Source

| Source | Type | Repos | Stars | Latest Push |
|--------|------|------:|------:|-------------|
| plurigrid | org | 100 | 69 | 2026-05-07 |
| bmorphism | user | 100 | 247 | 2026-05-07 |
| zubyul | user | 49 | 14 | 2026-04-24 |
| kubeflow | org | 47 | 34,011 | 2026-05-07 |
| AustinCStone | user | 40 | 108 | 2026-02-11 |
| migalkin | user (zubyul social) | 19 | 279 | 2025-08-04 |
| wasita | user (zubyul social) | 11 | 4 | 2026-05-06 |
| M1shaaa | user (zubyul social) | 8 | 0 | 2026-05-07 |
| DJedamski | user (zubyul social) | 6 | 3 | 2018-03-07 |
| kristinezheng | user (zubyul social) | 6 | 0 | 2026-04-09 |
| TeglonLabs | org | 4 | 2 | 2026-01-01 |
| **TOTAL** | | **390** | **34,737** | |

### Notable Repos

- **kubeflow org**: 34,011 combined stars — flagship ML on Kubernetes platform
- **migalkin/NodePiece**: 143★ — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: active MCP SDK in OCaml
- **plurigrid/zig-syrup**: High-performance Zig OCapN Syrup with CapTP (pushed 2026-04-30)
- **plurigrid/asi**: "everything is topological chemputer!" 20★ (pushed 2026-04-26)
- **wasita/vocoder**: just pushed 2026-05-06 — newest activity in social graph
- **M1shaaa/M1shaaa**: profile repo pushed 2026-05-07

### Top Repos by Stars

| Repo | Stars | Language | Pushed |
|------|------:|----------|--------|
| kubeflow/* (combined) | 34,011 | multi | 2026-05-07 |
| migalkin/* (combined) | 279 | Python | 2025-08-04 |
| bmorphism/* (combined) | 247 | multi | 2026-05-07 |
| AustinCStone/* (combined) | 108 | Python | 2026-02-11 |
| plurigrid/* (combined) | 69 | multi | 2026-05-07 |

### GF(3) Color Chain — Assignment Rule

```
id mod 3 == 0  →  trit= 0, color=#d3869b, name=ERGODIC
id mod 3 == 1  →  trit=+1, color=#b8bb26, name=PLUS
id mod 3 == 2  →  trit=-1, color=#cc241d, name=MINUS
```

Chain start: `id=1 → PLUS (#b8bb26)`, perfectly balanced at 130 each across 390 increments.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 wallets (alice, bob, A–Z) returned `resource_not_found` from Aptos mainnet fullnode
(`ledger_version=5169006610`), meaning no `0x1::coin::CoinStore<AptosCoin>` exists — **0.0 APT** each.
Accounts are provisioned as address labels but hold no funded coin store.

| World | Address | Balance APT |
|-------|---------|------------:|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...89a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

### Multisig Contract Probes (5 pairs)

All 5 multisig accounts are **healthy** — `num_signatures_required = 2` (2-of-N).

| Pair | Address | Sigs Required | Status |
|------|---------|:-------------:|--------|
| A-B | 0x0da4...003 | 2 | ✓ healthy |
| A-G | 0xf56c...096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...883 | 2 | ✓ healthy |
| S-T | 0x3b1c...883 | 2 | ✓ healthy |
| V-W | 0x40fa...b6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

The site is a **Next.js SPA** ("The AI Exchange") with routes: Home / Create / Trade.
Unauthenticated access renders "Connect Wallet to View Account" — no public REST API for market data.
Paths `/api/markets`, `/api` serve the SPA shell without JSON market data.
**Status: Unavailable — wallet auth required. No data in `mnx_snapshots`.**

---

## Schema Reference

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

---

*Generated by world-increment-sweep + hamming-swarm-snapshot agent · plurigrid/gorj · 2026-05-07*
