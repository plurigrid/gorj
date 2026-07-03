# World-Increment Sweep + Hamming Snapshot — 2026-07-03

## Sweep Metadata
- **Date:** 2026-07-03
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Python)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts (this sweep)

| Metric | Value |
|--------|-------|
| New World Increments | 391 |
| New Repo Snapshots | 391 |
| Sources Covered | 3 orgs + 8 users |
| Cumulative DB totals | 414 increments / 1335 snapshots |

### Repo Counts by Source

| Source | Type | Repos (this sweep) |
|--------|------|--------------------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 48 |
| zubyul | user | 49 |
| AustinCStone | social graph | 40 |
| migalkin | social graph | 19 |
| wasita | social graph | 11 |
| M1shaaa | social graph | 8 |
| TeglonLabs | org | 5 |
| kristinezheng | social graph | 5 |
| DJedamski | social graph | 6 |
| **TOTAL** | | **391** |

### Notable Repos (most recent pushes)

- `TeglonLabs/jank-crane` — C++ crane-jank converged-IR hub with GF3 convergence maps (pushed 2026-06-08)
- `M1shaaa/M1shaaa` — pushed 2026-07-03 (today)
- `kristinezheng/kristinezheng.github.io` — pushed 2026-07-01
- `wasita/wasita.github.io` — Svelte personal site, pushed 2026-07-02

### GF(3) Color Chain Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

All 28 addresses returned `resource_not_found` for the APT CoinStore resource.
These Hamming-swarm accounts are unfunded on Aptos mainnet (no coin store initialized).

| World | Status |
|-------|--------|
| alice, bob, A–Z (all 28) | 0.0 APT (unfunded) |

### Multisig Contract Probes — All HEALTHY

All 5 probed multisig accounts respond with 2-of-2 signature threshold:

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4f428… | 2 | ✅ HEALTHY |
| A-G | 0xf56c4a1c… | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ffe181… | 2 | ✅ HEALTHY |
| S-T | 0x3b1c3ae9… | 2 | ✅ HEALTHY |
| V-W | 0x40fad7b4… | 2 | ✅ HEALTHY |

### MNX Markets

`https://testnet.mnx.fi` — SPA returning HTML for all probed API paths.
No JSON market data available via public REST API.
Status: **UNAVAILABLE** (SPA-only, no API discovered).

---

## DuckDB Schema

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

## Cumulative Ducklake State

| Table | Total Rows | Notes |
|-------|------------|-------|
| world_increments | 414 | +391 this sweep (prev: 23 from 2026-04-10) |
| repo_snapshots | 1335 | accumulating across sweeps |
| aptos_snapshots | 28 | this sweep only |
| multisig_probes | 5 | this sweep only |
| mnx_snapshots | 1 | unavailable marker |
