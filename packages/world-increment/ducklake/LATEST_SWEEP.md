# World-Increment Sweep + Hamming Snapshot — 2026-08-01

## Sweep Metadata
- **Date:** 2026-08-01
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **World Increment:** id=13, GF(3)=PLUS (#b8bb26, trit=1)

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 24 (max id=13) |
| Total Repo Snapshots | 945 |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain (this run)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | plurigrid (org) | sweep_complete | +1 | `#b8bb26` | **PLUS** |
| 12 | bmorphism (org) | sweep_complete | 0 | `#d3869b` | **ERGODIC** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |

GF(3) rule: `id%3==0 → ERGODIC #d3869b` · `id%3==1 → PLUS #b8bb26` · `id%3==2 → MINUS #cc241d`

---

## JOB 1: GitHub Social Graph Sweep

### Source Coverage

| Source | Type | Status | Note |
|--------|------|--------|------|
| plurigrid/gorj | org/repo | ✓ captured | 20 recent commits; only scoped repo accessible |
| kubeflow | org | ✗ unavailable | API restricted to configured repos |
| TeglonLabs | org | ✗ unavailable | API restricted to configured repos |
| bmorphism | user | ✗ unavailable | API restricted to configured repos |
| zubyul | user | ✗ unavailable | API restricted to configured repos |
| zubyul social graph (6 users) | users | ✗ unavailable | API restricted to configured repos |

> The GitHub API in this environment is restricted to repository-scoped endpoints for `plurigrid/gorj`. Org-listing and user-listing endpoints return 403. Previous sweep data (471 repos from 11 sources) remains in the database from the 2026-04-12 run.

### plurigrid/gorj — Recent Commits (20)

| SHA | Date | Message |
|-----|------|---------|
| 5b28fe0 | 2026-05-08 | chore: ignore duckdb binary in repo root |
| ebf263f | 2026-04-14 | world-increment ducklake: sync world.duckdb sweep state |
| b434a43 | 2026-04-14 | Merge sweep state into master |
| e76792f | 2026-04-14 | world-increments.duckdb: sync latest sweep state |
| 631518b | 2026-04-12 | world-increment sweep 2026-04-12: insert id=12 ERGODIC |
| c4238bc | 2026-04-10 | world-increments.duckdb: sync latest sweep state |
| bbcce38 | 2026-04-08 | Merge sweep state into master |
| a79a81c | 2026-04-08 | world-increments.duckdb: sync sweep state |
| 3e3b89e | 2026-04-07 | world-increments.duckdb: sync final uncommitted sweep state |
| 87ca05e | 2026-04-07 | world-increments.duckdb: sync uncommitted sweep state |
| 0b7e1be | 2026-04-07 | world-increments.duckdb: commit final state post-sweep |
| 95d9888 | 2026-04-06 | world-increments.duckdb: sync final sweep state |
| ab32913 | 2026-04-05 | world-increments.duckdb: commit final sweep state |
| 4809438 | 2026-04-05 | world-increment sweep + hamming snapshot [GF3 color chain] |
| 1b2b0b7 | 2026-04-04 | world-increments.duckdb: update sweep data |
| 91999fc | 2026-04-03 | world-increments.duckdb: commit in-progress sweep state |
| 49404d3 | 2026-04-03 | world-increments.duckdb: update snapshot data |
| 9eb3a9a | 2026-04-02 | world-increments.duckdb: update snapshot data |
| 0649552 | 2026-04-02 | world-increments.duckdb: update snapshot data |
| b00021f | 2026-04-02 | world-increments.duckdb: update snapshot data |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet — 2026-08-01)

All 28 addresses queried via `https://fullnode.mainnet.aptoslabs.com`. All returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — no registered APT coin stores on mainnet for any of these addresses.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.00 |
| bob | 0x0a3c...512d | 0.00 |
| A | 0x8699...d7a | 0.00 |
| B | 0x3f89...b13 | 0.00 |
| C | 0x38b9...35e | 0.00 |
| D | 0xf776...dd1 | 0.00 |
| E | 0xdc1d...d36 | 0.00 |
| F | 0x18a1...f71 | 0.00 |
| G | 0x69a3...f32 | 0.00 |
| H | 0xce67...00f | 0.00 |
| I | 0x070f...fc9 | 0.00 |
| J | 0x4d96...f54 | 0.00 |
| K | 0xa732...dc4 | 0.00 |
| L | 0x7c2e...ba9 | 0.00 |
| M | 0x6fed...2e9 | 0.00 |
| N | 0xe7dd...b2c | 0.00 |
| O | 0x7325...89d | 0.00 |
| P | 0x6218...948 | 0.00 |
| Q | 0xac40...89a9 | 0.00 |
| R | 0x7ce6...e10 | 0.00 |
| S | 0xb875...386 | 0.00 |
| T | 0x3578...588 | 0.00 |
| U | 0x7586...956 | 0.00 |
| V | 0xb59d...2c3 | 0.00 |
| W | 0x5f32...7b0 | 0.00 |
| X | 0xa95c...47d | 0.00 |
| Y | 0xd8e3...4c4 | 0.00 |
| Z | 0x7af0...97c | 0.00 |

**Total APT across swarm:** 0.00 APT

### Multisig Contract Probes (Aptos Mainnet — 2026-08-01)

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`. All healthy.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ healthy |
| A-G | 0xf56c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

**Multisig health: 5/5 contracts operational (all 2-of-N).**

### MNX Markets (testnet.mnx.fi — 2026-08-01)

Status: **Unavailable** — `testnet.mnx.fi` is a Next.js SPA with no accessible REST JSON API.  
Endpoints tried: `/api/markets`, `/api/v1/markets`, `/api/tickers`, `/api/v1/tickers`, `/api/pairs`, `/api/v2/markets`, `/api/stats`, `/markets`.  
All returned HTML (SPA shell). No market data extractable.

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

## Notable from Previous Sweeps (historical, stored in DB)
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars (pushed 2026-04-10)
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for MCP
- **plurigrid/asi**: 16 stars — topological chemputer
- **migalkin/NodePiece**: 143 stars — scalable KG embeddings
- **471 repos** from 11 sources captured on 2026-04-12 remain in repo_snapshots
