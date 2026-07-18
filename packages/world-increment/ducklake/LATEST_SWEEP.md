# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-18

## Sweep Metadata
- **Date:** 2026-07-18
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Python)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 406 |
| Total Repo Snapshots | 1327 (cumulative) |
| This Run Repos | 383 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Market Data | unavailable (auth-gated) |

---

## GF(3) Color Chain Distribution (Cumulative)

| Name | Color | Count |
|------|-------|-------|
| ERGODIC | `#d3869b` | 134 |
| PLUS | `#b8bb26` | 136 |
| MINUS | `#cc241d` | 136 |

GF(3) rule: `id mod 3 == 0` → ERGODIC #d3869b | `id mod 3 == 1` → PLUS #b8bb26 | `id mod 3 == 2` → MINUS #cc241d

---

## GitHub Snapshot — Top Repos by Stars (This Run)

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | - | 15781 | 2026-07-10 |
| kubeflow/pipelines | Python | 4168 | 2026-07-17 |
| kubeflow/spark-operator | Python | 3138 | 2026-07-17 |
| kubeflow/trainer | Go | 2151 | 2026-07-18 |
| kubeflow/hub | Go | 177 | 2026-07-17 |
| kubeflow/sdk | Python | 125 | 2026-07-18 |
| plurigrid/asi | HTML | 31 | 2026-07-10 |
| TeglonLabs/mathpix-gem | Ruby | 2 | 2026-01-01 |

## Most Recently Active (Today 2026-07-18)
- **plurigrid/gorj** (Clojure) — this repo, pushed today
- **kubeflow/trainer** (Go) — pushed today
- **kubeflow/mcp-server** (Python) — new: Kubeflow now has an MCP server
- **kubeflow/sdk** (Python) — pushed today
- **M1shaaa/M1shaaa** — profile config pushed today

## Repo Counts by Source (This Run)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| AustinCStone | user | 30 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| wasita | user | 12 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| TeglonLabs | org | 5 |
| **TOTAL** | | **383** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)

All 28 addresses queried against Aptos mainnet.

**Result:** All addresses returned `Resource not found` — none of the Hamming swarm addresses have initialized APT coin stores on Aptos mainnet. These appear to be uninitialized or testnet-only accounts.

### Multisig Contract Probes — ALL HEALTHY ✅

All 5 multisig pairs probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428a0c007da... | 2 | ✅ healthy |
| A-G | 0xf56c4a1c09062143... | 2 | ✅ healthy |
| Y-Z | 0xd3ffe1812b2df406... | 2 | ✅ healthy |
| S-T | 0x3b1c3ae905d44c3a... | 2 | ✅ healthy |
| V-W | 0x40fad7b423a84365... | 2 | ✅ healthy |

All 5 multisig contracts are live and healthy, each requiring **2-of-N signatures**.

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` is behind Vercel deployment protection — authentication required. No market data accessible without bypass token. Recorded as `UNAVAILABLE`.

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,781 stars (+216 since April sweep) — strong growth
- **kubeflow/mcp-server**: NEW as of this sweep — Kubeflow has shipped an MCP server
- **kubeflow/trainer**: ★2151, pushed today — active ML training infra
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) trit coloring
- **TeglonLabs/jank-crane** (C++): New since April — GF3 convergence maps, loopify pass spec
- **bmorphism/gay-chat** (Scheme): Most recently active bmorphism repo
- **All 5 multisig contracts**: 2-of-N, all healthy on Aptos mainnet
- **Hamming swarm EOAs**: Uninitialized on mainnet (no APT coin stores)
