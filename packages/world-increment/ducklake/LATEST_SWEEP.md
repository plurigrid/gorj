# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-27

## Sweep Metadata
- **Date:** 2026-07-27
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| New World Increments (this sweep) | 144 |
| Total Repo Snapshots (cumulative) | 1065 |
| Sources Covered | 2 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Pairs Probed | 5 (all healthy) |
| MNX Markets | unavailable (SPA) |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried This Sweep

| Source | Type | Repos Fetched |
|--------|------|---------------|
| plurigrid | org | 50 |
| TeglonLabs | org | 5 |
| bmorphism | user | 21 (of 106 total) |
| zubyul | user | 15 (of 49 total) |
| migalkin | user | 7 (of 19 total) |
| DJedamski | user | 4 (of 6 total) |
| wasita | user | 8 (of 12 total) |
| kristinezheng | user | 4 (of 5 total) |
| M1shaaa | user | 4 (of 8 total) |
| AustinCStone | user | 10 (of 41 total) |

### GF(3) Color Chain — 144 Increments

GF(3) distribution: **ERGODIC×47** (#d3869b) · **PLUS×49** (#b8bb26) · **MINUS×48** (#cc241d)

GF(3) Assignment Rule:
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

### Most Recently Active

| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| plurigrid/gorj | Clojure | 1 | **2026-07-27** |
| wasita/wasita.github.io | Svelte | 1 | 2026-07-21 |
| plurigrid/eirobri | Clojure | 0 | 2026-07-21 |
| bmorphism/Gay.jl | Julia | 2 | 2026-07-21 |
| plurigrid/asi | HTML | 51 | 2026-07-10 |
| migalkin/kgcourse2021 | HTML | 24 | 2026-07-10 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 22 | 2026-07-12 |

### Top Repos by Stars (this sweep)

| Repo | Language | Stars |
|------|----------|-------|
| migalkin/NodePiece | Python | 144 |
| AustinCStone/TextGAN | Python | 92 |
| migalkin/StarE | Python | 89 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 |
| plurigrid/asi | HTML | 51 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 22 |
| migalkin/kgcourse2021 | HTML | 24 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 addresses probed against Aptos mainnet fullnode (`fullnode.mainnet.aptoslabs.com`).

**Result:** All accounts have on-chain activity (sequence numbers 2–49 for L–Z indicate active wallets), but **none hold the APT CoinStore resource** (`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`). These wallets transact via other token types (likely Fungible Asset standard).

| Accounts | Seq# Range | Balance APT |
|----------|------------|-------------|
| alice, bob, A–K | N/A (resource_not_found) | 0.0 |
| L | 49 | 0.0 |
| M | 39 | 0.0 |
| N | 48 | 0.0 |
| O, P | 16 | 0.0 |
| Q | 9 | 0.0 |
| R | 15 | 0.0 |
| S | 11 | 0.0 |
| T, U | 7–9 | 0.0 |
| V | 5 | 0.0 |
| W | 4 | 0.0 |
| X | 3 | 0.0 |
| Y, Z | 2 | 0.0 |

### Multisig Contract Probes

All 5 multisig pairs probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4f428... | 2 | ✅ HEALTHY |
| A-G | 0xf56c4a1c... | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ffe181... | 2 | ✅ HEALTHY |
| S-T | 0x3b1c3ae9... | 2 | ✅ HEALTHY |
| V-W | 0x40fad7b4... | 2 | ✅ HEALTHY |

**All 5/5 multisig pairs respond with 2-of-n threshold. No anomalies detected.**

### MNX Markets (testnet.mnx.fi)

Site is a Next.js SPA — API paths (`/api/markets`, `/api/v1/markets`) return the SPA shell HTML rather than JSON. **No market data accessible without browser execution.** Recorded as unavailable; `mnx_snapshots` table has 0 rows.

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

---

## Previous Sweep Reference

Prior sweep: **2026-04-12** — 12 increments, 471 repo snapshots (3 orgs + 8 users incl. kubeflow).
