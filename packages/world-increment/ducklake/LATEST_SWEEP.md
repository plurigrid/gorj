# World Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-06-29 04:09 UTC  
**Branch:** `world-increment/sweep-2026-06-29-0409`  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**DuckDB version:** v1.5.4 (Variegata)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured | Notes |
|--------|------|----------------|-------|
| plurigrid | org | 100 | GitHub caps at 100; 102 total |
| kubeflow | org | 48 | |
| TeglonLabs | org | 5 | |
| bmorphism | user | 100 | GitHub caps at 100; 105 total |
| zubyul | user | 49 | |
| migalkin | user | 19 | |
| DJedamski | user | 6 | |
| kristinezheng | user | 5 | |
| M1shaaa | user | 8 | |
| AustinCStone | user | 40 | |
| **TOTAL** | | **380** | |

### GF(3) Color Distribution

| GF(3) State | Trit | Color | Count |
|-------------|------|-------|-------|
| ERGODIC | 0 | #d3869b | 126 |
| PLUS | +1 | #b8bb26 | 127 |
| MINUS | -1 | #cc241d | 127 |

GF(3) assignment: `id%3==0 → ERGODIC, id%3==1 → PLUS, id%3==2 → MINUS`

### Notable Repos This Sweep

- **TeglonLabs/jank-crane** (C++) – crane-jank converged-IR hub, GF3 convergence maps — pushed 2026-06-08
- **M1shaaa/M1shaaa** – profile repo updated 2026-06-29 (today!)
- **kristinezheng/kristinezheng.github.io** (HTML) – personal site pushed 2026-06-07
- **wasita/wasita.github.io** (Svelte) – personal website pushed 2026-06-25
- **plurigrid** org – 100+ repos, active ML/agent/GF3 ecosystem
- **bmorphism** – 100+ repos spanning OCaml, Zig, MCP tooling, and more

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

**Result:** All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

None of the Hamming swarm addresses currently hold APT in the standard coin store. Accounts may exist on-chain but have not initialized an AptosCoin store (or hold zero balance).

| World | Address (prefix) | Balance |
|-------|-----------------|---------|
| alice | 0xc793acde... | N/A (no coin store) |
| bob | 0x0a3c00c5... | N/A (no coin store) |
| A–Z (26 addrs) | various | N/A (no coin store) |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts responded healthy with **2-of-2** signature threshold:

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428... | 2 | healthy |
| A-G | 0xf56c4a1c... | 2 | healthy |
| Y-Z | 0xd3ffe181... | 2 | healthy |
| S-T | 0x3b1c3ae9... | 2 | healthy |
| V-W | 0x40fad7b4... | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable — Vercel deployment protection (authentication required). The site returns an auth-gate page requiring a Vercel OIDC token. No market data could be extracted.

---

## DuckDB Schema Summary

```sql
-- 380 rows: one increment per repo snapshot
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name, actor, snapshot_hash)

-- 380 rows
repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name, full_name,
               language, stars, forks, open_issues, pushed_at, description)

-- 28 rows (all NULL balance_apt — resource_not_found on Aptos mainnet)
aptos_snapshots(timestamp, world, address, balance_apt)

-- 5 rows (all sigs_required=2, healthy=true)
multisig_probes(timestamp, pair, address, sigs_required, healthy)

-- 0 rows (MNX testnet unavailable — Vercel auth required)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```
