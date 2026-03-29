# World Increment Sweep — 2026-03-29

## Sweep Metadata
- **Date:** 2026-03-29
- **Agent:** world-increment-sweep (Claude claude-sonnet-4-6)
- **GitHub Auth:** zubyul (Yuliya Zubak)
- **DuckDB:** v1.5.1+ at `/usr/local/bin/duckdb`
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 365 |
| Total Repo Snapshots | 365 |
| Aptos Addresses Queried | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## GitHub Repos Swept

| Org/User | Type | Repo Count |
|---|---|---|
| bmorphism | user | 97 |
| plurigrid | org | 87 |
| kubeflow | org | 46 |
| zubyul | user | 44 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| wasita | user | 9 |
| M1shaaa | user | 8 |
| kristinezheng | user | 6 |
| DJedamski | user | 6 |
| TeglonLabs | org | 3 |
| **TOTAL** | | **365** |

---

## GF(3) Color Chain Assignments

| id % 3 | Trit | Color | Name | Count |
|---|---|---|---|---|
| 0 | 0 | #d3869b | ERGODIC | 217 |
| 1 | 1 | #b8bb26 | PLUS | 218 |
| 2 | -1 | #cc241d | MINUS | 218 |

**Assignment rule:**
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

GF(3) chain cycles: ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ...

---

## Aptos Wallet Balances

All 28 addresses were queried against Aptos mainnet. All returned `resource_not_found`
for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`, indicating 0 APT balance
(accounts not initialized or no APT held on mainnet at ledger version ~4.7B).

| World | Address (truncated) | Balance (APT) |
|---|---|---|
| alice | 0xc793ac...4cc7b | 0.0 |
| bob | 0x0a3c00...512d5d | 0.0 |
| A | 0x8699ed...ebe9d7a | 0.0 |
| B | 0x3f892e...577cb13 | 0.0 |
| C | 0x38b99e...691535e | 0.0 |
| D | 0xf77656...fcfdd1 | 0.0 |
| E | 0xdc1d9d...958d36 | 0.0 |
| F | 0x18a14b...c3cf71 | 0.0 |
| G | 0x69a394...bcc7f32 | 0.0 |
| H | 0xce67c3...e5300f | 0.0 |
| I | 0x070fe5...c1fc9 | 0.0 |
| J | 0x4d964d...87f54 | 0.0 |
| K | 0xa73204...425dc4 | 0.0 |
| L | 0x7c2eae...37eba9 | 0.0 |
| M | 0x6fed37...b7f2e9 | 0.0 |
| N | 0xe7dde6...551b2c | 0.0 |
| O | 0x73252b...5a89d | 0.0 |
| P | 0x621879...ec948 | 0.0 |
| Q | 0xac40fa...5c89a9 | 0.0 |
| R | 0x7ce605...76e10 | 0.0 |
| S | 0xb87530...d0386 | 0.0 |
| T | 0x35781d...f4588 | 0.0 |
| U | 0x75860d...ef9956 | 0.0 |
| V | 0xb59dd8...9af2c3 | 0.0 |
| W | 0x5f32ae...ccc7b0 | 0.0 |
| X | 0xa95cbb...e33047d | 0.0 |
| Y | 0xd8e328...2444c4 | 0.0 |
| Z | 0x7af0ef...4e197c | 0.0 |

---

## Multisig Contract Probes

All 5 multisig contracts probed via `POST /v1/view` with
`0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4f4...987003 | 2 | true |
| A-G | 0xf56c4a...c0096 | 2 | true |
| Y-Z | 0xd3ffe1...b883 | 2 | true |
| S-T | 0x3b1c3a...7883 | 2 | true |
| V-W | 0x40fad7...eb6d | 2 | true |

All 5 multisig accounts require 2-of-N signatures and are healthy (responding on mainnet).

---

## MNX Market Data

**Status: UNAVAILABLE**

Endpoints tried:
- `https://testnet.mnx.fi/api/markets` — returns HTML (Next.js app, no JSON API exposed)
- `https://mnx.fi/api/markets` — returns HTML
- `https://api.mnx.fi/markets` — Vercel deployment not found

No structured MNX market data could be retrieved at sweep time.

---

## DuckDB Schema & Row Counts

| Table | Rows |
|---|---|
| world_increments | 365 |
| repo_snapshots | 365 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (N/A placeholder) |

**Total world increments:** 365

---

## GF(3) Assignment Rule (Hamming/Coding Theory Basis)

GF(3) = {-1, 0, +1} under addition mod 3. The "trit coloring" assigns each world increment
to a GF(3) element forming a ternary Hamming code-inspired labeling:

- **ERGODIC (#d3869b)**: trit=0, balanced/neutral state
- **PLUS (#b8bb26)**: trit=+1, growth/forward state
- **MINUS (#cc241d)**: trit=-1, contraction/reverse state

The coloring is uniform across all 365 increments (217/218/218 distribution).

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
