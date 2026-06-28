# World-Increment Sweep — 2026-06-28 (+ Hamming Swarm Snapshot)

## Sweep Metadata
- **Date:** 2026-06-28
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts (this run)

| Metric | Value |
|--------|-------|
| New World Increments | 381 |
| New Repo Snapshots | 381 |
| Sources Covered | 3 orgs + 8 users |

### GF(3) Color Chain — Distribution
- `id % 3 == 0` → trit=0, **ERGODIC** `#d3869b` (~127 repos)
- `id % 3 == 1` → trit=1, **PLUS** `#b8bb26` (~127 repos)
- `id % 3 == 2` → trit=-1, **MINUS** `#cc241d` (~127 repos)

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 48 |
| AustinCStone | user | 40 |
| migalkin | user (social graph) | 19 |
| M1shaaa | user (social graph) | 8 |
| DJedamski | user (social graph) | 6 |
| kristinezheng | user (social graph) | 5 |
| TeglonLabs | org | 5 |
| wasita | user (social graph) | 1 |
| **TOTAL** | | **381** |

### Notable Repos (pushed most recently)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| M1shaaa/M1shaaa | — | 0 | **2026-06-28 TODAY** |
| wasita/wasita.github.io | Svelte | 1 | 2026-06-25 |
| TeglonLabs/jank-crane | C++ | 0 | 2026-06-08 |
| kristinezheng/kristinezheng.github.io | HTML | 0 | 2026-06-07 |
| TeglonLabs/mathpix-gem | Ruby | 2 | 2026-01-01 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All 28 addresses (alice, bob, A–Z) returned `resource_not_found` for
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — **no APT holdings on mainnet**.

| World | Address | APT Balance |
|-------|---------|------------|
| alice | 0xc793...cc7b | NULL (unfunded) |
| bob | 0x0a3c...512d | NULL (unfunded) |
| A | 0x8699...9d7a | NULL (unfunded) |
| B | 0x3f89...b13 | NULL (unfunded) |
| C | 0x38b9...35e | NULL (unfunded) |
| D–Z | … | NULL (unfunded) × 23 |

### Multisig Contract Probes — ALL HEALTHY

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✓ HEALTHY |

All 5 Aptos multisig contracts healthy on mainnet, each requiring 2-of-N signatures.

### MNX Markets

**UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel deployment protection.
No market data extractable without authentication credentials.

---

## DuckDB Table Totals

| Table | Total Rows |
|-------|-----------|
| world_increments | 404+ |
| repo_snapshots | 1325+ |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

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
