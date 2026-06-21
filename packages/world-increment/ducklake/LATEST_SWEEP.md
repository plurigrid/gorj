# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-21

## Sweep Metadata
- **Date:** 2026-06-21
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.2.1
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Run timestamp:** 2026-06-21T01:08 UTC

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Source | Type | Repos | Total Stars | GF3 Trit | GF3 Color |
|--------|------|:-----:|:-----------:|:--------:|:---------:|
| plurigrid | org | 100 | 157 | +1 PLUS | `#b8bb26` |
| kubeflow | org | 48 | 101,957 | -1 MINUS | `#cc241d` |
| TeglonLabs | org | 5 | 2 | 0 ERGODIC | `#d3869b` |
| bmorphism | user | 100 | 510 | +1 PLUS | `#b8bb26` |
| zubyul | user | 49 | 40 | -1 MINUS | `#cc241d` |
| migalkin | social | 79 | 834 | 0 ERGODIC | `#d3869b` |
| DJedamski | social | 28 | 17 | +1 PLUS | `#b8bb26` |
| wasita | social | 71 | 11 | -1 MINUS | `#cc241d` |
| kristinezheng | social | 41 | 0 | 0 ERGODIC | `#d3869b` |
| M1shaaa | social | 40 | 0 | +1 PLUS | `#b8bb26` |
| AustinCStone | social | 126 | 324 | -1 MINUS | `#cc241d` |
| **TOTAL** | | **687** | **103,852** | | |

**Total repo records in DB (cumulative):** 1,335  
**World increment records (this run):** 36 rows across 13 sources × 3 GF3 slots

### GF(3) Color Chain

```
id%3==0 → trit=0  ERGODIC  #d3869b  (TeglonLabs, migalkin, kristinezheng, hamming_swarm)
id%3==1 → trit=+1 PLUS     #b8bb26  (plurigrid, bmorphism, DJedamski, M1shaaa, multisig_probe)
id%3==2 → trit=-1 MINUS    #cc241d  (kubeflow, zubyul, wasita, AustinCStone)
```

### Notable Repos (Most Recently Pushed)

**plurigrid** — top by recency (June 2026):
- `plurigrid/place` (TeX, 1★) pushed 2026-06-20 — 9 open issues
- `plurigrid/asi` (HTML, 26★) pushed 2026-06-10 — "everything is topological chemputer!"
- `plurigrid/eirobri` (Clojure, 0★) pushed 2026-06-03 — "EiRoBri replay world"

**TeglonLabs** — new repo since last sweep:
- `TeglonLabs/jank-crane` (C++, 0★) pushed 2026-06-08 — "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow"

**kubeflow** — dominant by stars (101,957 total across 48 repos)

**bmorphism** — 100 repos, 510★ total; active across OCaml/Zig/JavaScript/Python

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice–Z, 28 wallets)

All 28 wallets returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
Wallets have not registered a coin store on Aptos mainnet. All balances: **0.0 APT**.

| World | Address | Balance |
|-------|---------|---------|
| alice | 0xc793...cc7b | 0.0 APT |
| bob | 0x0a3c...2d5d | 0.0 APT |
| A–Z | (26 wallets) | 0.0 APT each |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **healthy** — each requires **2-of-2 signatures**.

| Pair | Address | Sigs Required | Status |
|------|---------|:-------------:|:------:|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | ✓ healthy |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | ✓ healthy |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | ✓ healthy |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — site requires Vercel visitor password authentication.
No market data accessible without bypass token. Recorded as unavailable in `mnx_snapshots`.

---

## Database Tables

| Table | Rows (cumulative) |
|-------|:-----------------:|
| world_increments | 36 |
| repo_snapshots | 1,335 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (unavailable marker) |

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Δ vs 2026-04-12 Sweep
- Repos: 471 → 1,335 cumulative (+864 new records)
- plurigrid/asi: 16★ → 26★ (+10)
- plurigrid/place: new, 9 open issues
- TeglonLabs/jank-crane: new (GF3 convergence maps in C++)
- kubeflow stars stable ~101k
- All 5 multisig contracts remain 2-of-2 healthy
- Aptos wallets: unchanged (all unregistered coin stores)
