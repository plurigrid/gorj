# World Increment Sweep + Hamming Swarm Snapshot — 2026-06-24

## Sweep Metadata
- **Date:** 2026-06-24
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social) | 19 |
| DJedamski | user (social) | 6 |
| wasita | user (social) | 11 |
| kristinezheng | user (social) | 5 |
| M1shaaa | user (social) | 8 |
| AustinCStone | user (social) | 40 |
| **TOTAL** | | **391** |

**world_increments:** 343 rows (320 distinct GF3-tagged events)  
**repo_snapshots:** 1264 rows (multi-snapshot across sources)

### GF(3) Color Chain Distribution

| GF3 Name | Color | Trit | Count |
|----------|-------|------|-------|
| ERGODIC | #d3869b | 0 | 113 |
| PLUS | #b8bb26 | +1 | 115 |
| MINUS | #cc241d | -1 | 115 |

Assignment rule: `id%3==0 → ERGODIC #d3869b | id%3==1 → PLUS #b8bb26 | id%3==2 → MINUS #cc241d`

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15742 | — |
| kubeflow/pipelines | 4157 | Python |
| kubeflow/spark-operator | 3128 | Python |
| kubeflow/trainer | 2120 | Go |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| migalkin/kgcourse2021 | 25 | HTML |

### Notable Activity (June 2026)

- **TeglonLabs/jank-crane** (C++, pushed 2026-06-08): crane-jank converged-IR hub, loopify pass spec, GF3 convergence maps — freshest repo in sweep
- **wasita/proj-template** (pushed 2026-06-19): project template actively maintained
- **wasita/wasita.github.io** (Svelte, pushed 2026-06-15): personal site active
- **migalkin/RWL** (pushed 2026-05-28): Weisfeiler-Leman relational graph networks
- **AustinCStone/EpsteinSearch** (Python, 2026-02-08): notable new repo from AustinCStone

### TeglonLabs Repos (5 total)

| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-06-24)

All 28 wallets queried via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
**Result: All 28 addresses returned 0.0 APT** — no active coin store resource found. Accounts appear unfunded or not yet initialized on Aptos mainnet.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...12d5 | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D–Z | (23 more addresses) | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...3003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All 5 multisigs operational with 2-of-N threshold. No anomalies detected.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE**  
`testnet.mnx.fi` is a Vercel-deployed SPA behind Vercel Authentication (HTTP 401, visitor password required). No market data accessible without credentials. Recorded as `auth_required` placeholder in `mnx_snapshots`.

---

## DuckDB Table Summary

```
world_increments  — 343 rows  (320 distinct GF3-tagged repo push events)
repo_snapshots    — 1264 rows (repo snapshots across 11 sources)
aptos_snapshots   —  28 rows  (alice, bob, A–Z; all 0.0 APT)
multisig_probes   —   5 rows  (all healthy, 2-of-N = 2)
mnx_snapshots     —   1 row   (auth_required placeholder)
```

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
