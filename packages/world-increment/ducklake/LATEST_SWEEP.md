# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-30

## Sweep Metadata
- **Date:** 2026-07-30
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Fetched | Total Available |
|--------|------|--------------|-----------------|
| plurigrid | org | 100 | 103 |
| kubeflow | org | 49 | 49 |
| TeglonLabs | org | 5 | 5 |
| bmorphism | user | 49 | 49 |
| zubyul | user | 19 | 19 |
| migalkin | user (social) | 100 | 106 |
| DJedamski | user (social) | 6 | 6 |
| wasita | user (social) | 12 | 12 |
| kristinezheng | user (social) | 5 | 5 |
| M1shaaa | user (social) | 8 | 8 |
| AustinCStone | user (social) | 41 | 41 |
| **TOTAL** | | **394** | **403** |

### Notable Recent Activity
- **M1shaaa/M1shaaa** — profile config pushed `2026-07-30T13:50:06Z` (today, active)
- **TeglonLabs/jank-crane** — C++ GF3 convergence maps pushed `2026-06-08` (recent)
- **TeglonLabs/mathpix-gem** — Ruby math OCR gem, 2 stars, 11 open issues
- **wasita/wasita.github.io** — Svelte personal site pushed `2026-07-21`
- **kristinezheng/kristinezheng.github.io** — HTML portfolio pushed `2026-07-01`

### GF(3) Color Chain Distribution (cumulative in DB)
| GF3 Name | Trit | Color | Count |
|----------|------|-------|-------|
| ERGODIC | 0 | `#d3869b` | 134 |
| PLUS | +1 | `#b8bb26` | 136 |
| MINUS | -1 | `#cc241d` | 135 |

GF(3) chain balanced: PLUS→MINUS→ERGODIC cycling across 405 increments.

### DuckDB Tables (cumulative)
| Table | Rows |
|-------|------|
| world_increments | 405 |
| repo_snapshots | 1326 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

### Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name, actor, snapshot_hash)
repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues, pushed_at, description)
aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-07-30)
28 addresses (alice, bob, A–Z) queried against `fullnode.mainnet.aptoslabs.com`.

**Result:** All 28 addresses returned no CoinStore resource.
Accounts have no `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` registered —
wallets may be unfunded, on testnet, or using fungible_asset storage.

| World | Address (prefix) | Balance APT | Status |
|-------|-----------------|-------------|--------|
| alice | 0xc793... | 0.0 | not_found |
| bob | 0x0a3c... | 0.0 | not_found |
| A–Z (26) | 0x8699...–0x7af0... | 0.0 each | not_found |

### Multisig Contract Probes (Mainnet)
5 contracts probed for `0x1::multisig_account::num_signatures_required`:

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4... | 2 | ✓ |
| A-G | 0xf56c... | 2 | ✓ |
| Y-Z | 0xd3ff... | 2 | ✓ |
| S-T | 0x3b1c... | 2 | ✓ |
| V-W | 0x40fa... | 2 | ✓ |

**All 5 multisig contracts healthy — each requiring 2-of-N signatures.**

### MNX Markets (testnet.mnx.fi)
`https://testnet.mnx.fi/api/markets` returns HTML (Next.js SPA, no REST API).
Market data requires browser-side JS execution.
**Status: unavailable via HTTP API — SPA only. Stored 0 rows in mnx_snapshots.**

---

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS
