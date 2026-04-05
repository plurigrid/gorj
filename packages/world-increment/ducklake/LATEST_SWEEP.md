# World-Increment Sweep — 2026-04-05

## Sweep Metadata
- **Date:** 2026-04-05
- **Agent:** world-increment-sweep
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 313 |
| Total Repo Snapshots | 253 |
| Sources Covered | 3 orgs + 8 users |
| Event Increments (bmorphism + zubyul) | 60 |

---

## GitHub Repos Collected by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 46 |
| TeglonLabs | org | 53 |
| bmorphism | user | 2 |
| zubyul | user | 2 |
| migalkin | user_social | 2 |
| DJedamski | user_social | 11 |
| wasita | user_social | 2 |
| kristinezheng | user_social | 2 |
| M1shaaa | user_social | 2 |
| AustinCStone | user_social | 43 |
| **TOTAL** | | **265** |

Public events captured: 30 events from bmorphism, 30 from zubyul (60 total event world_increments)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-04-05)

| Label | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793... | 0.43643352 |
| bob | 0x0a3c... | 12.65700700 |
| A | 0x8699... | 0.05176700 |
| B | 0x3f89... | 0.03625600 |
| C | 0x38b9... | 0.01018500 |
| D | 0xf776... | 0.01162900 |
| E | 0xdc1d... | 0.01256100 |
| F | 0x18a1... | 1.96051600 |
| G | 0x69a3... | 0.00068100 |
| H | 0xce67... | 0.00068100 |
| I | 0x070f... | 0.00068100 |
| J | 0x4d96... | 1.89509300 |
| K | 0xa732... | 0.16196100 |
| L | 0x7c2e... | 1.92726900 |
| M | 0x6fed... | 0.11228500 |
| N | 0xe7dd... | 0.10612100 |
| O | 0x7325... | 0.21013600 |
| P | 0x6218... | 0.14013600 |
| Q | 0xac40... | 0.10324000 |
| R | 0x7ce6... | 0.09021700 |
| S | 0xb875... | 0.09178800 |
| T | 0x3578... | 0.07371300 |
| U | 0x7586... | 0.05577300 |
| V | 0xb59d... | 0.04783299 |
| W | 0x5f32... | 0.04070500 |
| X | 0xa95c... | 0.04257700 |
| Y | 0xd8e3... | 0.04444900 |
| Z | 0x7af0... | 0.02326800 |

**Summary:**
- Total wallets probed: 28
- Non-zero wallets: 28 (100%)
- **Total APT across swarm: 20.34496151 APT**
- Method: `0x1::coin::balance` view function (CoinStore resource not present; accounts use FA standard)

### Multisig Contract Probes

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4... | 2 | true |
| A-G | 0xf56c... | 2 | true |
| Y-Z | 0xd3ff... | 2 | true |
| S-T | 0x3b1c... | 2 | true |
| V-W | 0x40fa... | 2 | true |

All 5 multisig contracts healthy — all require 2-of-N signatures.

### MNX Markets

- `https://testnet.mnx.fi/api/markets` — Returns Next.js SPA HTML (not a JSON endpoint)
- `https://testnet.mnx.fi/api/v1/markets` — Returns Next.js SPA HTML (not a JSON endpoint)
- **Status: UNAVAILABLE** — MNX testnet is a client-rendered SPA; no public REST API endpoint detected. `mnx_snapshots` table is empty.

---

## Database Summary

| Table | Rows |
|-------|------|
| world_increments | 313 |
| repo_snapshots | 253 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

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
