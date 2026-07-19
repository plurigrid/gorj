# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-07-19  
**Run type:** world-increment-sweep + hamming-swarm-snapshot  
**GF(3) increments:** 12 (ERGODIC #d3869b), 13 (PLUS #b8bb26), 14 (MINUS #cc241d)

---

## JOB 1: GitHub Social Graph Sweep

**Status:** PARTIAL — GitHub REST API blocked by proxy (proxy-injected token, HTTP 403)

Only `plurigrid/gorj` was accessible via the GitHub MCP (session scope restriction).

### plurigrid/gorj (via MCP)
- Latest commit: `5b28fe0` — 2026-05-08 (`chore: ignore duckdb binary in repo root`)
- Active sweep branches: 50+ `world-increment/sweep-*` branches tracked
- Prior full sweep data (2026-04-14): 944 repo snapshots across 11 orgs/users preserved

### Snapshot stored
| org_or_user | repo_name | pushed_at |
|---|---|---|
| plurigrid | gorj | 2026-05-08T14:04:34Z |

**Cumulative repo_snapshots:** 945 rows (944 prior + 1 new)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
Queried 28 addresses (alice, bob, A–Z) via `fullnode.mainnet.aptoslabs.com`.

**Result: All 28 addresses → 0.0 APT (resource_not_found)**

No `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource found for any address.
Addresses exist on-chain but hold no initialized APT CoinStore at ledger version ~6.35B.

| World | Address (prefix) | Balance APT |
|---|---|---|
| alice | 0xc793ac... | 0.0 |
| bob | 0x0a3c00... | 0.0 |
| A | 0x8699ed... | 0.0 |
| B | 0x3f892e... | 0.0 |
| C | 0x38b99e... | 0.0 |
| D | 0xf77656... | 0.0 |
| E | 0xdc1d9d... | 0.0 |
| F | 0x18a14b... | 0.0 |
| G | 0x69a394... | 0.0 |
| H | 0xce67c3... | 0.0 |
| I | 0x070fe5... | 0.0 |
| J | 0x4d964d... | 0.0 |
| K | 0xa73204... | 0.0 |
| L | 0x7c2eae... | 0.0 |
| M | 0x6fed37... | 0.0 |
| N | 0xe7dde6... | 0.0 |
| O | 0x73252b... | 0.0 |
| P | 0x621879... | 0.0 |
| Q | 0xac40fa... | 0.0 |
| R | 0x7ce605... | 0.0 |
| S | 0xb87530... | 0.0 |
| T | 0x35781d... | 0.0 |
| U | 0x75860d... | 0.0 |
| V | 0xb59dd8... | 0.0 |
| W | 0x5f32ae... | 0.0 |
| X | 0xa95cbb... | 0.0 |
| Y | 0xd8e328... | 0.0 |
| Z | 0x7af0ef... | 0.0 |

### Multisig Contract Probes (Aptos Mainnet)
All 5 probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (prefix) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4f4... | 2 | YES |
| A-G | 0xf56c4a... | 2 | YES |
| Y-Z | 0xd3ffe1... | 2 | YES |
| S-T | 0x3b1c3a... | 2 | YES |
| V-W | 0x40fad7... | 2 | YES |

**All 5 multisigs healthy — 2-of-2 threshold across the board.**

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — Vercel authentication wall on all API paths (`/`, `/api/markets`, `/api/v1/markets`, `/api/tickers`, `/v1/markets`). No market data extractable without credentials.

---

## GF(3) Color Chain — Increments 12–14

| ID | Source | Event Type | GF3 Trit | Color | Name |
|---|---|---|---|---|---|
| 12 | plurigrid (org) | github_sweep | 0 | `#d3869b` | **ERGODIC** |
| 13 | aptos (chain) | hamming_snapshot | +1 | `#b8bb26` | **PLUS** |
| 14 | gorj (system) | sweep_complete | -1 | `#cc241d` | **MINUS** |

GF(3) assignment: `id mod 3 == 0` → ERGODIC · `id mod 3 == 1` → PLUS · `id mod 3 == 2` → MINUS

---

## DuckDB State Summary

| Table | Rows | Notes |
|---|---|---|
| world_increments | 26 | IDs 1–14; 3 new this run |
| repo_snapshots | 945 | 1 new (gorj); 944 from 2026-04-14 |
| aptos_snapshots | 28 | All 0.0 APT / resource_not_found |
| multisig_probes | 5 | All 2-of-2, all healthy |
| mnx_snapshots | 0 | Vercel auth blocked |

**DB:** `packages/world-increment/ducklake/world-increments.duckdb`
