# World-Increment Sweep — 2026-05-08

## Sweep Metadata
- **Date:** 2026-05-08 ~14:10 UTC
- **Agent:** world-increment-sweep
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 100 |
| Aptos Snapshots | 28 |
| Multisig Probes | 5 |
| MNX Snapshots | 1 |
| Sources Covered | 3 orgs + 8 users |

**Note:** GitHub unauthenticated API hit the 60 req/hr rate limit. Only `plurigrid` (100 repos) was captured via the MCP tool. All other sources (kubeflow, TeglonLabs, 8 users) were rate-limited and recorded with 0 repos.

---

## GF(3) Color Chain — All 11 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## Top Repos by Source (2026-05-08 sweep)

### plurigrid (100 repos — captured)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 21 | captured |
| ontology | JavaScript | 7 | captured |
| asi-skills | Julia | 3 | captured |
| zig-syrup | Zig | 2 | captured |
| nash-portal | Rust | 2 | captured |

### kubeflow, TeglonLabs, 8 users — RATE-LIMITED (0 repos this sweep)

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 0 (rate-limited) |
| TeglonLabs | org | 0 (rate-limited) |
| bmorphism | user | 0 (rate-limited) |
| zubyul | user | 0 (rate-limited) |
| migalkin | user | 0 (rate-limited) |
| DJedamski | user | 0 (rate-limited) |
| wasita | user | 0 (rate-limited) |
| kristinezheng | user | 0 (rate-limited) |
| M1shaaa | user | 0 (rate-limited) |
| AustinCStone | user | 0 (rate-limited) |
| **TOTAL** | | **100** |

---

## Aptos Wallet Balances

All 28 addresses returned HTTP 404 (not found on Aptos mainnet). All balances recorded as -1.

| Label | Balance (APT) | Status |
|-------|---------------|--------|
| alice | -1 | 404 not found |
| bob | -1 | 404 not found |
| A–Z (26 wallets) | -1 each | 404 not found |

---

## Multisig Contract Probes

All 5 contracts healthy. All require 2 signatures.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...87003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

---

## MNX Markets

All three endpoints returned HTML (not JSON API data). Testnet appears unreachable.
One placeholder row inserted: ticker=UNAVAILABLE, price=0, change_pct=0.

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

## Notable Highlights
- **plurigrid/asi**: 21 stars — topological chemputer (captured 2026-05-08)
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) trit coloring
- **Multisig sweep**: All 5 A/B/G/S/T/V/W/Y/Z pairs healthy, sigs_required=2
- **Aptos mainnet**: All 28 wallet addresses returned 404 — accounts not yet funded/created on mainnet
- **GitHub rate limit**: Unauthenticated 60 req/hr exhausted; only plurigrid captured this sweep
- **MNX testnet**: All API endpoints return HTML — service unreachable
