# World-Increment Sweep — 2026-05-12

## Sweep Metadata
- **Date:** 2026-05-12
- **Agent:** world-increment-sweep
- **DuckDB version:** v1.5.2
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 891 |
| Total Repo Snapshots (cumulative) | 1812 |
| New Repo Inserts This Sweep | 478 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## Repo Counts by Source (This Sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 48 |
| AustinCStone | user | 43 |
| wasita | user | 32 |
| migalkin | user | 30 |
| zubyul | user | 27 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| **TOTAL** | | **478** |

---

## Aptos Wallet Balances

All 28 addresses returned 0.00000000 APT (accounts exist on-chain, zero balance).

| World Label | Address (truncated) | Balance (APT) |
|-------------|---------------------|---------------|
| alice | 0xc793acdec12b4a63... | 0.00000000 |
| bob | 0x0a3c00c58fdf9020... | 0.00000000 |
| A | 0x8699edc0960dd5b9... | 0.00000000 |
| B | 0x3f892ebe6e45164e... | 0.00000000 |
| C | 0x38b99e63ada9b6fe... | 0.00000000 |
| D | 0xf77656248f64d5dd... | 0.00000000 |
| E | 0xdc1d9d533bac3507... | 0.00000000 |
| F | 0x18a14b5b4bec118c... | 0.00000000 |
| G | 0x69a394c0b0ac8421... | 0.00000000 |
| H | 0xce67c327a7844e54... | 0.00000000 |
| I | 0x070fe5d74e4eda30... | 0.00000000 |
| J | 0x4d964db8f5383740... | 0.00000000 |
| K | 0xa732040a6b0d5590... | 0.00000000 |
| L | 0x7c2eaeafad972549... | 0.00000000 |
| M | 0x6fed37a7553ef16b... | 0.00000000 |
| N | 0xe7dde6da0a65f510... | 0.00000000 |
| O | 0x73252b6011a75115... | 0.00000000 |
| P | 0x6218792de4a9bc38... | 0.00000000 |
| Q | 0xac40fa50b81b4ca6... | 0.00000000 |
| R | 0x7ce605cc8fda4f8e... | 0.00000000 |
| S | 0xb8753014e4888ea4... | 0.00000000 |
| T | 0x35781dc0e42fef3f... | 0.00000000 |
| U | 0x75860da47565f650... | 0.00000000 |
| V | 0xb59dd8170321dfab... | 0.00000000 |
| W | 0x5f32aef70f5ba530... | 0.00000000 |
| X | 0xa95cbbd116548ac9... | 0.00000000 |
| Y | 0xd8e32848f1dffa81... | 0.00000000 |
| Z | 0x7af0ef6e1bd706f4... | 0.00000000 |

---

## Multisig Contract Probes

All 5 multisig contracts are healthy and require 2-of-N signatures.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f428a0c007da... | 2 | true |
| A-G | 0xf56c4a1c0906214f... | 2 | true |
| Y-Z | 0xd3ffe1812b2df406... | 2 | true |
| S-T | 0x3b1c3ae905d44c3a... | 2 | true |
| V-W | 0x40fad7b423a84365... | 2 | true |

---

## MNX Markets Status

**UNAVAILABLE** — `https://testnet.mnx.fi/api/markets`, `/api/tickers`, and `/api/v1/markets` all return HTML (Next.js app shell, no JSON API data accessible). Placeholder row inserted in `mnx_snapshots`.

---

## GF(3) Color Chain Legend

| Trit | Color | Name | Rule |
|------|-------|------|------|
| 0 | `#d3869b` (pink) | ERGODIC | row_num % 3 == 0 |
| +1 | `#b8bb26` (green) | PLUS | row_num % 3 == 1 |
| -1 | `#cc241d` (red) | MINUS | row_num % 3 == 2 |

Cycle: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ...`

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
