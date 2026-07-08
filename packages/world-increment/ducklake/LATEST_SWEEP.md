# World-Increment Sweep + Hamming Snapshot — 2026-07-08

## Sweep Metadata
- **Date:** 2026-07-08
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Increment ID:** 12 (of 24 total in DB)
- **GF(3) color:** PLUS `#b8bb26` (trit=+1)

---

## JOB 1 — GitHub Social Graph Sweep

### Coverage

| Source | Type | Status |
|--------|------|--------|
| `plurigrid` | org | 100 repos snapshotted via MCP |
| `kubeflow`, `TeglonLabs`, `bmorphism`, `zubyul`, social graph | various | Proxy blocks cross-org/user endpoints; data from prior sweeps in DB |

> Session proxy restricts GitHub API to `plurigrid/gorj`-scoped endpoints. Cross-org calls return HTTP 403. Prior sweep increments (IDs 1–11) cover kubeflow, TeglonLabs, bmorphism, zubyul, migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone — 944 snapshots still in DB.

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (DB) | 24 |
| Total Repo Snapshots (DB) | 1044 |
| This sweep (plurigrid) | 100 repos |
| Sources active today | plurigrid org (proxy-limited) |

### Top Plurigrid Repos by Stars

| Repo | Language | ★ | Forks | Open Issues | Last Push |
|------|----------|---|-------|-------------|-----------|
| plurigrid/asi | HTML | 30 | 9 | 4 | 2026-06-29 |
| plurigrid/ontology | JavaScript | 8 | 9 | 16 | 2025-05-27 |
| plurigrid/vcg-auction | Rust | 7 | 3 | 1 | 2023-03-16 |
| plurigrid/agent | Python | 5 | 1 | 6 | 2023-03-31 |
| plurigrid/StochFlow | Python | 4 | 1 | 0 | 2024-03-20 |
| plurigrid/asi-skills | Julia | 3 | 0 | 0 | 2026-04-26 |
| plurigrid/Plurigraph | JavaScript | 3 | 5 | 4 | 2025-01-05 |
| plurigrid/act | Python | 3 | 1 | 4 | 2024-07-26 |
| plurigrid/microworlds | Rust | 3 | 5 | 3 | 2023-05-13 |
| plurigrid/nash-portal | Rust | 2 | 3 | 1 | 2026-05-19 |
| plurigrid/gorj | Clojure | 1 | 0 | 1064 | 2026-07-08 |
| plurigrid/place | TeX | 1 | 1 | 12 | 2026-07-07 |

### Language Breakdown (plurigrid, this sweep)

| Language | Repos | Total Stars |
|----------|-------|-------------|
| HTML | 5 | 31 |
| Rust | 12 | 13 |
| Python | 8 | 12 |
| JavaScript | 3 | 11 |
| Zig | 2 | 3 |
| Julia | 3 | 3 |
| TypeScript | 10 | 3 |
| Clojure | 9 | 2 |

### GF(3) Color Chain State (cumulative, 24 increments)

| Name | Trit | Color | Count |
|------|------|-------|-------|
| ERGODIC | 0 | `#d3869b` | 7 |
| PLUS | +1 | `#b8bb26` | 9 |
| MINUS | -1 | `#cc241d` | 8 |

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-07-08)

Queried 28 addresses (alice, bob, A–Z) with 1s sleep between calls.

| Result | Count |
|--------|-------|
| Wallets with APT balance | 0 |
| resource_not_found | 28 |
| Total probed | 28 |

All 28 hamming-swarm addresses returned `resource_not_found` on `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. Accounts unfunded or CoinStore not initialized on mainnet.

### Multisig Contract Probes (5/5 healthy)

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4f428…4987003` | 2 | ✓ healthy |
| A-G | `0xf56c4a1c…bc0096` | 2 | ✓ healthy |
| Y-Z | `0xd3ffe181…75b883` | 2 | ✓ healthy |
| S-T | `0x3b1c3ae9…d7883` | 2 | ✓ healthy |
| V-W | `0x40fad7b4…80eb6d` | 2 | ✓ healthy |

All 5 multisig contracts active and responding to `0x1::multisig_account::num_signatures_required`. All require 2-of-N.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` returns HTTP 401 — Vercel deployment protection (visitor password required). No market data available this sweep.

---

## DuckDB Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)              -- 24 rows

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)             -- 1044 rows

aptos_snapshots(timestamp, world, address, balance_apt)  -- 28 rows
multisig_probes(timestamp, pair, address, sigs_required, healthy)  -- 5 rows
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)  -- 0 rows
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS

## Notable Highlights
- **plurigrid/asi**: 30 stars (up from 16 in April sweep) — topological chemputer active
- **plurigrid/gorj**: 1064 open issues — most active repo in org, pushed today
- **plurigrid/place**: pushed 2026-07-07 — recent activity
- **All 5 multisigs**: 2-of-N, healthy — Hamming swarm governance intact
- **0/28 wallets funded**: Hamming swarm addresses show no on-chain APT balances on mainnet
