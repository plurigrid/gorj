# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-29

**Run date:** 2026-07-29  
**GF(3) increment:** id=13, trit=1, **PLUS #b8bb26**  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Status: RESTRICTED

The environment's proxy restricts the GitHub API to repository-scoped endpoints only (`repos/{owner}/{repo}/...`). Org-listing (`/orgs/{org}/repos`) and user-listing (`/users/{user}/repos`) endpoints return:

```
This GitHub API path is not available: sessions are bound to their configured repositories.
```

**Scope allowed:** `plurigrid/gorj` only (via GitHub MCP server).

### plurigrid/gorj — Latest Commit Snapshot

| Field | Value |
|---|---|
| Full name | plurigrid/gorj |
| Language | Clojure |
| Latest commit | `5b28fe0` — "chore: ignore duckdb binary in repo root" |
| Commit date | 2026-05-08T14:04:34Z |
| Author | Claude |

**Recent gorj commits (from MCP list_commits):**
- `5b28fe0` 2026-05-08 — chore: ignore duckdb binary in repo root
- `ebf263f` 2026-04-14 — world-increment ducklake: sync world.duckdb sweep state
- `b434a43` 2026-04-14 — Merge sweep state into master
- `631518b` 2026-04-12 — world-increment sweep 2026-04-12: insert id=12 ERGODIC + regenerate LATEST_SWEEP.md
- `c4238bc` 2026-04-10 — world-increments.duckdb: sync latest sweep state
- `48094388` 2026-04-05 — world-increment sweep + hamming snapshot [GF3 color chain]

**Prior sweep context (from repo_snapshots, 944 rows pre-existing):**

| Source | Type | Repos (prior) |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 47 |
| AustinCStone | user | 43 |
| migalkin | user | 30 |
| wasita | user | 29 |
| zubyul | user | 24 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| **TOTAL** | | **471** |

*(Data from 2026-04-12 sweep — org/user listing blocked in current session)*

**Cumulative DuckDB state:**
- `world_increments`: 25 rows (IDs 1–14)
- `repo_snapshots`: 945 rows (944 prior + 1 gorj this run)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

**Method:** `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`  
**Result:** All 28 addresses return 0 APT via legacy CoinStore. Accounts may be using the newer Fungible Asset (FA) standard or be unfunded.

| World | Address (truncated) | APT (CoinStore) |
|---|---|---|
| alice | 0xc793...cc7b | 0.0 |
| bob   | 0x0a3c...2d5d | 0.0 |
| A     | 0x8699...9d7a | 0.0 |
| B     | 0x3f89...b13  | 0.0 |
| C     | 0x38b9...35e  | 0.0 |
| D     | 0xf776...dd1  | 0.0 |
| E     | 0xdc1d...d36  | 0.0 |
| F     | 0x18a1...f71  | 0.0 |
| G     | 0x69a3...f32  | 0.0 |
| H     | 0xce67...00f  | 0.0 |
| I     | 0x070f...fc9  | 0.0 |
| J     | 0x4d96...f54  | 0.0 |
| K     | 0xa732...dc4  | 0.0 |
| L     | 0x7c2e...ba9  | 0.0 |
| M     | 0x6fed...e9   | 0.0 |
| N     | 0xe7dd...b2c  | 0.0 |
| O     | 0x7325...89d  | 0.0 |
| P     | 0x6218...948  | 0.0 |
| Q     | 0xac40...a9   | 0.0 |
| R     | 0x7ce6...e10  | 0.0 |
| S     | 0xb875...386  | 0.0 |
| T     | 0x3578...588  | 0.0 |
| U     | 0x7586...956  | 0.0 |
| V     | 0xb59d...c3   | 0.0 |
| W     | 0x5f32...b0   | 0.0 |
| X     | 0xa95c...47d  | 0.0 |
| Y     | 0xd8e3...4c4  | 0.0 |
| Z     | 0x7af0...97c  | 0.0 |

**Total APT across swarm:** 0.0 APT (28/28 queried)

### Multisig Contract Probes

**Method:** `POST /v1/view` → `0x1::multisig_account::num_signatures_required`  
**Result:** All 5 multisig contracts responding and healthy. All require 2-of-N.

| Pair | Address (truncated) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**Multisig health: 5/5** — all contracts live on Aptos mainnet.

### MNX Testnet Markets

**URL:** `https://testnet.mnx.fi`  
**Status:** SPA (Next.js) — serves HTML only. No REST API found at `/api/markets` or `/api/v1/markets`. Market data unavailable without headless browser. Recorded as `unavailable` in `mnx_snapshots`.

---

## GF(3) Color Chain Progress

| ID | Trit | Color | Name | Event |
|---|---|---|---|---|
| 10 | 1 | #b8bb26 | PLUS | M1shaaa repo_snapshot |
| 11 | -1 | #cc241d | MINUS | AustinCStone repo_snapshot |
| 12 | 0 | #d3869b | ERGODIC | sweep_complete (2026-04-12) |
| **13** | **1** | **#b8bb26** | **PLUS** | **sweep_run (2026-07-29)** ← this run |
| 14 | -1 | #cc241d | MINUS | access_restricted (2026-07-29) |

Next expected: ID=15, trit=0, ERGODIC #d3869b

GF(3) cycle: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → ...`

---

## DuckDB Table Summary

| Table | Rows | Notes |
|---|---|---|
| world_increments | 25 | IDs 1–14 (some IDs have multiple rows) |
| repo_snapshots | 945 | 471 repos from prior sweep + 1 gorj this run |
| aptos_snapshots | 28 | All 28 Hamming swarm addresses, 0 APT each |
| multisig_probes | 5 | All healthy, 2-of-N |
| mnx_snapshots | 1 | Unavailable (SPA) |

---

## Schema Reference

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
