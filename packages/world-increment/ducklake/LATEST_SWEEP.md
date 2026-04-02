# World-Increment Sweep — 2026-04-02

## Sweep Metadata
- **Date:** 2026-04-02
- **Agent:** world-increment-sweep
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 105 |
| Total Repo Snapshots | 1294 |
| Sources Covered | 3 orgs + 8 users + 2 event batches |

---

## GitHub Sweep

### Orgs queried
| Org | Type | Repos Captured |
|-----|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 46 |
| TeglonLabs | org | 53 |

### Users queried
| User | Type | Repos Captured |
|------|------|---------------|
| bmorphism | user | 100 |
| zubyul | user | 23 |
| migalkin | user | 30 |
| DJedamski | user | 0 (not found) |
| wasita | user | 29 |
| kristinezheng | user | 0 (not found) |
| M1shaaa | user | 16 |
| AustinCStone | user | 43 |

### Events queried
- bmorphism: 30 public events
- zubyul: 30 public events

**Total repo_snapshots rows:** 1294

---

## Aptos Wallet Snapshot

| Label | Address (truncated) | Balance APT |
|-------|---------------------|------------:|
| alice | 0xc793ac...4cc7b | 0.0 |
| bob | 0x0a3c00...512d5d | 0.0 |
| A | 0x8699ed...be9d7a | 0.0 |
| B | 0x3f892e...7cb13 | 0.0 |
| C | 0x38b99e...1535e | 0.0 |
| D | 0xf77656...cfdd1 | 0.0 |
| E | 0xdc1d9d...8d36 | 0.0 |
| F | 0x18a14b...3cf71 | 0.0 |
| G | 0x69a394...c7f32 | 0.0 |
| H | 0xce67c3...5300f | 0.0 |
| I | 0x070fe5...1fc9 | 0.0 |
| J | 0x4d964d...7f54 | 0.0 |
| K | 0xa73204...25dc4 | 0.0 |
| L | 0x7c2eae...7eba9 | 0.0 |
| M | 0x6fed37...7f2e9 | 0.0 |
| N | 0xe7dde6...551b2c | 0.0 |
| O | 0x73252b...5a89d | 0.0 |
| P | 0x621879...ec948 | 0.0 |
| Q | 0xac40fa...c89a9 | 0.0 |
| R | 0x7ce605...76e10 | 0.0 |
| S | 0xb87530...d0386 | 0.0 |
| T | 0x35781d...f4588 | 0.0 |
| U | 0x75860d...f9956 | 0.0 |
| V | 0xb59dd8...af2c3 | 0.0 |
| W | 0x5f32ae...cc7b0 | 0.0 |
| X | 0xa95cbb...3047d | 0.0 |
| Y | 0xd8e328...444c4 | 0.0 |
| Z | 0x7af0ef...e197c | 0.0 |

All 28 addresses returned 0.0 APT (accounts not found on Aptos mainnet or zero balance).

---

## Multisig Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|:-------------:|:-------:|
| A-B | 0x0da4f4...87003 | 2 | true |
| A-G | 0xf56c4a...0096 | 2 | true |
| Y-Z | 0xd3ffe1...b883 | 2 | true |
| S-T | 0x3b1c3a...7883 | 2 | true |
| V-W | 0x40fad7...eb6d | 2 | true |

All 5 multisig accounts healthy with 2-of-N signature threshold.

---

## MNX Markets

`https://testnet.mnx.fi/api/markets` — **UNAVAILABLE**

The endpoint returns a Next.js SPA HTML page (404 from the API route). No rows inserted into `mnx_snapshots`.

---

## GF(3) Color Chain Legend

| id % 3 | Trit | Color | Name |
|--------|------|-------|------|
| 0 | 0 | `#d3869b` | ERGODIC |
| 1 | +1 | `#b8bb26` | PLUS |
| 2 | -1 | `#cc241d` | MINUS |

Chain cycle: ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ...

Each world_increment row is colored by `id % 3`, cycling through ERGODIC (trit=0) → PLUS (trit=+1) → MINUS (trit=-1).

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
