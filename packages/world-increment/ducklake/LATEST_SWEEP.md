# World-Increment Sweep — 2026-08-01

## Sweep Metadata
- **Date:** 2026-08-01
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 26 |
| New Increments This Sweep | 3 (IDs 12–14) |
| Total Repo Snapshots (cumulative) | 945 |
| New Repo Snapshots This Sweep | 1 (plurigrid/gorj) |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Market Snapshots | 0 (SPA — no JSON API) |

---

## GF(3) Color Chain — This Sweep (IDs 12–14)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 12 | plurigrid (org) | repo_sweep | 0 | `#d3869b` | **ERGODIC** |
| 13 | aptos (chain) | hamming_snapshot | +1 | `#b8bb26` | **PLUS** |
| 14 | sweep (meta) | sweep_complete | -1 | `#cc241d` | **MINUS** |

GF(3) rule: `id%3==0` → ERGODIC `#d3869b`, `id%3==1` → PLUS `#b8bb26`, `id%3==2` → MINUS `#cc241d`

---

## Job 1: GitHub Social Graph Sweep

**API scope note:** This session is restricted to repository-scoped endpoints (`plurigrid/gorj` only). Org-level and user-level listing endpoints for kubeflow, TeglonLabs, bmorphism, zubyul, and social graph users are blocked by proxy policy (`sessions are bound to their configured repositories`).

### plurigrid/gorj — Latest Commit (from local + MCP)
| Field | Value |
|-------|-------|
| SHA | `5b28fe016e0e3d0b0f22e35e01f7db0722d988e1` |
| Date | 2026-05-08T14:04:34Z |
| Message | `chore: ignore duckdb binary in repo root` |
| Language | Clojure |
| Description | MCP server + hooks that give AI coding agents a Clojure REPL |

### Other Sources — Restricted
| Source | Type | Status |
|--------|------|--------|
| kubeflow | org | API restricted (proxy policy) |
| TeglonLabs | org | API restricted (proxy policy) |
| bmorphism | user | API restricted (proxy policy) |
| zubyul | user | API restricted (proxy policy) |
| migalkin / DJedamski / wasita / kristinezheng / M1shaaa / AustinCStone | users | API restricted (proxy policy) |

*Last known snapshot for these sources: 471 repos recorded in sweep-2026-04-12.*

---

## Job 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet — 2026-08-01)

All 28 wallets returned 0 APT. The Aptos CoinStore resource was not found for any address, indicating these accounts are either unfunded or not yet registered on mainnet.

| World | Address | APT |
|-------|---------|-----|
| alice | `0xc793...cc7b` | 0.00 |
| bob | `0x0a3c...12d5` | 0.00 |
| A–Z | (26 addresses) | 0.00 each |

Full addresses stored in `aptos_snapshots` table.

### Multisig Contract Probes (mainnet — 2026-08-01)

All 5 multisig contracts are **healthy** — each requires 2 signatures.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4...003` | 2 | healthy |
| A-G | `0xf56c...096` | 2 | healthy |
| Y-Z | `0xd3ff...883` | 2 | healthy |
| S-T | `0x3b1c...883` | 2 | healthy |
| V-W | `0x40fa...b6d` | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — `testnet.mnx.fi` serves a Next.js SPA. All probed paths (`/api/markets`, `/api/v1/markets`, `/api/v2/markets`, `/api/tickers`) return the SPA HTML shell. No JSON market data extracted. Table `mnx_snapshots` remains empty.

---

## Cumulative Database State

| Table | Row Count |
|-------|-----------|
| world_increments | 26 |
| repo_snapshots | 945 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

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

## Notable Highlights
- **Multisig health:** All 5 A-B/A-G/Y-Z/S-T/V-W contracts respond with `sigs_required=2` — no degradation since last probe
- **Hamming swarm:** 28 wallets (alice, bob, A–Z) queried on Aptos mainnet; all show 0 APT (unfunded)
- **Repo count:** 945 cumulative snapshots; +1 this sweep (gorj only, others restricted)
- **GF(3) cycle:** IDs 12–14 complete another partial cycle: ERGODIC → PLUS → MINUS
