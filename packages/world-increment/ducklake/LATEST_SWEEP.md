# World Increment Sweep + Hamming Swarm Snapshot — 2026-05-15

## Sweep Metadata
- **Date:** 2026-05-15
- **Increment ID:** 13 (GF3: PLUS · #b8bb26 · trit=+1)
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Coverage
| Source | Type | Status | Repos |
|---|---|---|---|
| plurigrid/gorj | org | ✓ snapshotted (MCP) | 1 |
| kubeflow | org | rate_limited (no auth token) | — |
| TeglonLabs | org | rate_limited | — |
| bmorphism | user | rate_limited | — |
| zubyul | user | rate_limited | — |
| migalkin | user | rate_limited | — |
| DJedamski | user | rate_limited | — |
| wasita | user | rate_limited | — |
| kristinezheng | user | rate_limited | — |
| M1shaaa | user | rate_limited | — |
| AustinCStone | user | rate_limited | — |

Unauthenticated GitHub API hit rate limit. Only `plurigrid/gorj` was accessible via the authenticated MCP scope.

### plurigrid/gorj (snapshotted)
- **Language:** Clojure
- **Latest push:** 2026-05-08T14:04:34Z
- **Latest commit:** `5b28fe0` — chore: ignore duckdb binary in repo root
- **Description:** MCP server + hooks that give AI coding agents a Clojure REPL

### DB State
| Table | Total Rows |
|---|---|
| world_increments | 25 |
| repo_snapshots | 945 |

Cumulative: 945 repo snapshots across all sweeps (471 from 2026-04-12, 473 from 2026-04-14 resync, 1 new).

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

Balances queried via `0x1::coin::balance` view function at ledger ~v5287301004.

### Wallet Balances

| World | Address (short) | Balance (APT) |
|---|---|---|
| bob | 0x0a3c00c5... | **12.657007** |
| F | 0x18a14b5b... | 1.960516 |
| L | 0x7c2eaeaf... | 1.927269 |
| J | 0x4d964db8... | 1.895093 |
| alice | 0xc793acde... | 0.436434 |
| O | 0x73252b60... | 0.210136 |
| K | 0xa732040a... | 0.161961 |
| P | 0x62187920... | 0.140136 |
| M | 0x6fed37a7... | 0.112285 |
| N | 0xe7dde6da... | 0.106121 |
| Q | 0xac40fa50... | 0.103240 |
| S | 0xb8753014... | 0.091788 |
| R | 0x7ce605cc... | 0.090217 |
| T | 0x35781dc0... | 0.073713 |
| U | 0x75860da4... | 0.055773 |
| A | 0x8699edc0... | 0.051767 |
| V | 0xb59dd817... | 0.048833 |
| Y | 0xd8e32848... | 0.044449 |
| X | 0xa95cbbd1... | 0.042577 |
| W | 0x5f32aef7... | 0.040705 |
| B | 0x3f892ebe... | 0.036256 |
| Z | 0x7af0ef6e... | 0.024268 |
| D | 0xf7765624... | 0.011629 |
| C | 0x38b99e63... | 0.010185 |
| E | 0xdc1d9d53... | 0.009372 |
| H | 0xce67c327... | 0.001681 |
| G | 0x69a394c0... | 0.000681 |
| I | 0x070fe5d7... | 0.000681 |

**Total Hamming Swarm: 20.3448 APT**

### Multisig Contract Probes

All 5 probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (short) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

All 5/5 healthy — **2-of-2 multisig**, all operational.

### MNX Markets (testnet.mnx.fi)
**Status:** Unavailable — Next.js SPA, no `/api/markets` endpoint accessible. Data requires browser JS execution.

---

## GF(3) Chain Progress

| id % 3 | trit | name | color |
|---|---|---|---|
| 0 | 0 | ERGODIC | #d3869b |
| 1 | +1 | PLUS | **#b8bb26** ← current |
| 2 | -1 | MINUS | #cc241d |

Sequence so far: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → **PLUS**`

Increment 13 = 5th PLUS (completing the first step of the 5th GF(3) cycle).

---

## Historical Summary

| Sweep | Date | Increments | Repo Snapshots | Sources |
|---|---|---|---|---|
| sweep-1 | 2026-04-10/12 | 1–12 | 471 | 3 orgs + 8 users |
| resync | 2026-04-14 | — | +473 | same |
| sweep-2 | 2026-05-15 | 13 | +1 | plurigrid/gorj (MCP) |

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
