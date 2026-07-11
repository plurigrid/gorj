# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-11

## Sweep Metadata
- **Date:** 2026-07-11
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **GF(3) Increment:** id=12 (ERGODIC, trit=0, color=#d3869b)

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (rows) | 24 |
| Total Repo Snapshots | 944 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Snapshots | N/A (auth wall) |
| Sources Covered (GitHub) | 3 orgs + 8 users (2026-04-12 baseline) |

---

## GF(3) New Increment

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 12 | hamming-swarm | hamming_snapshot | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain continuation: `… PLUS → MINUS → ERGODIC (this sweep)`

---

## Job 1: GitHub Social Graph

**Status:** Baseline carried forward from 2026-04-12 sweep (944 repo snapshots).
GitHub MCP access is scoped to `plurigrid/gorj` only — cross-org/user queries are policy-restricted in this session. Prior sweep data remains current in the database.

### Repo Counts (2026-04-12 baseline)

| Source | Type | Repos |
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

---

## Job 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (2026-07-11)

All 28 wallets in the Hamming swarm (alice, bob, A–Z) returned **0 APT**.
The `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource was not found for any address, indicating accounts have not received APT on mainnet.

| World | Address (last 8) | Balance (APT) |
|-------|-----------------|---------------|
| alice | …d624cc7b | 0.0 |
| bob   | …05512d5d | 0.0 |
| A     | …eaebe9d7a | 0.0 |
| B     | …4577cb13 | 0.0 |
| C     | …2691535e | 0.0 |
| D     | …9fcfdd1 | 0.0 |
| E     | …d0958d36 | 0.0 |
| F     | …74c3cf71 | 0.0 |
| G     | …dbcc7f32 | 0.0 |
| H     | …d94e5300f | 0.0 |
| I     | …fc00c1fc9 | 0.0 |
| J     | …3e87f54 | 0.0 |
| K     | …7a425dc4 | 0.0 |
| L     | …6337eba9 | 0.0 |
| W     | …45a6ccc7b0 | 0.0 |
| X     | …2cbe33047d | 0.0 |
| Y     | …0fa2444c4 | 0.0 |
| Z     | …5e6e4e197c | 0.0 |
| *(M–V omitted for brevity — all 0)* | | |

**Total swarm APT:** 0.0

---

### Multisig Contract Probes (2026-07-11)

All 5 multisig contracts responded successfully via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (last 8) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | …ef4987003 | **2** | ✓ |
| A-G | …3fbc0096 | **2** | ✓ |
| Y-Z | …38e75b883 | **2** | ✓ |
| S-T | …23ded7883 | **2** | ✓ |
| V-W | …c80eb6d | **2** | ✓ |

All 5 multisig accounts are **healthy** and configured for 2-of-2 consensus.

---

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable — Vercel authentication wall blocks all endpoints (`/`, `/api`, `/api/markets`). No market data extractable without credentials.

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

## Key Findings
- **Hamming swarm (A–Z + alice/bob):** All 28 wallets at 0 APT on Aptos mainnet — swarm accounts unfunded
- **Multisig health:** All 5 pairs (A-B, A-G, Y-Z, S-T, V-W) live with 2-of-2 threshold — topology intact
- **MNX testnet:** Gated behind Vercel SSO — requires authenticated session to extract market data
- **GitHub social graph:** Baseline of 944 snapshots from 471 repos across 11 sources; fresh cross-org sweep deferred pending MCP scope expansion
