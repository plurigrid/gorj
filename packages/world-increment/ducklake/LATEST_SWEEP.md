# World-Increment Sweep — 2026-08-02

## Sweep Metadata
- **Date:** 2026-08-02
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Increment ID:** 13 · GF(3) trit=1 · **PLUS** `#b8bb26`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| World Increment ID | 13 (PLUS #b8bb26) |
| Total World Increments (historical) | 24 rows |
| Total Repo Snapshots (historical) | 945 rows |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (SPA) |

---

## JOB 1: GitHub Social Graph Sweep

### Access Status
The proxy environment restricts GitHub API calls to `repos/{owner}/{repo}/...` scoped endpoints only.
Calls to `/orgs/{org}/repos` and `/users/{user}/repos` returned 403 (session bound to configured repository).

| Source | Type | Status |
|--------|------|--------|
| plurigrid/gorj | repo | ✅ accessible via MCP |
| plurigrid (org) | org repos | ⛔ proxy-blocked |
| kubeflow (org) | org repos | ⛔ proxy-blocked |
| TeglonLabs (org) | org repos | ⛔ proxy-blocked |
| bmorphism | user repos | ⛔ proxy-blocked |
| zubyul | user repos | ⛔ proxy-blocked |
| migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone | user repos | ⛔ proxy-blocked |

### plurigrid/gorj — Recent Activity (accessible)
Last 10 commits:

| Date | SHA | Message |
|------|-----|---------|
| 2026-05-08 | 5b28fe0 | chore: ignore duckdb binary in repo root |
| 2026-04-14 | ebf263f | world-increment ducklake: sync world.duckdb sweep state |
| 2026-04-14 | b434a43 | Merge sweep state into master |
| 2026-04-14 | e76792f | world-increments.duckdb: sync latest sweep state |
| 2026-04-12 | 631518b | world-increment sweep 2026-04-12: insert id=12 ERGODIC |
| 2026-04-10 | c4238bc | world-increments.duckdb: sync latest sweep state |
| 2026-04-08 | bbcce38 | Merge sweep state into master |
| 2026-04-08 | a79a81c | world-increments.duckdb: sync sweep state |
| 2026-04-07 | 3e3b89e | world-increments.duckdb: sync final uncommitted sweep state |
| 2026-04-07 | 87ca05e | world-increments.duckdb: sync uncommitted sweep state |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 wallets returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
These addresses have no APT coin store registered — **balance = 0.0 APT** across the entire swarm.

| World | Address (prefix) | Balance (APT) | Status |
|-------|-----------------|---------------|--------|
| alice | 0xc793ac... | 0.0 | no CoinStore |
| bob   | 0x0a3c00... | 0.0 | no CoinStore |
| A     | 0x8699ed... | 0.0 | no CoinStore |
| B     | 0x3f892e... | 0.0 | no CoinStore |
| C     | 0x38b99e... | 0.0 | no CoinStore |
| D     | 0xf77656... | 0.0 | no CoinStore |
| E     | 0xdc1d9d... | 0.0 | no CoinStore |
| F     | 0x18a14b... | 0.0 | no CoinStore |
| G     | 0x69a394... | 0.0 | no CoinStore |
| H     | 0xce67c3... | 0.0 | no CoinStore |
| I     | 0x070fe5... | 0.0 | no CoinStore |
| J     | 0x4d964d... | 0.0 | no CoinStore |
| K     | 0xa73204... | 0.0 | no CoinStore |
| L     | 0x7c2eae... | 0.0 | no CoinStore |
| M     | 0x6fed37... | 0.0 | no CoinStore |
| N     | 0xe7dde6... | 0.0 | no CoinStore |
| O     | 0x73252b... | 0.0 | no CoinStore |
| P     | 0x621879... | 0.0 | no CoinStore |
| Q     | 0xac40fa... | 0.0 | no CoinStore |
| R     | 0x7ce605... | 0.0 | no CoinStore |
| S     | 0xb87530... | 0.0 | no CoinStore |
| T     | 0x357810... | 0.0 | no CoinStore |
| U     | 0x75860d... | 0.0 | no CoinStore |
| V     | 0xb59dd8... | 0.0 | no CoinStore |
| W     | 0x5f32ae... | 0.0 | no CoinStore |
| X     | 0xa95cbb... | 0.0 | no CoinStore |
| Y     | 0xd8e328... | 0.0 | no CoinStore |
| Z     | 0x7af0ef... | 0.0 | no CoinStore |

### Multisig Contract Probes (Mainnet)

All 5 multisig contracts confirmed **healthy** — each requires 2-of-2 signatures.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f4... | 2 | ✅ |
| A-G | 0xf56c4a... | 2 | ✅ |
| Y-Z | 0xd3ffe1... | 2 | ✅ |
| S-T | 0x3b1c3a... | 2 | ✅ |
| V-W | 0x40fad7... | 2 | ✅ |

### MNX Markets (testnet.mnx.fi)

The site returned a Next.js SPA shell on all paths (`/`, `/api/markets`, `/api/v1/markets`).
No REST JSON API endpoint found — market data not extractable without headless browser execution.

**Status: unavailable** (SPA, no public JSON API)

---

## GF(3) Color Chain

| ID | Trit | Name | Color |
|----|------|------|-------|
| 13 | +1 | **PLUS** | `#b8bb26` |
| 12 | 0 | ERGODIC | `#d3869b` |
| 11 | -1 | MINUS | `#cc241d` |
| 10 | +1 | PLUS | `#b8bb26` |
| 9  | 0  | ERGODIC | `#d3869b` |
| 8  | -1 | MINUS | `#cc241d` |
| 7  | +1 | PLUS | `#b8bb26` |
| 6  | 0  | ERGODIC | `#d3869b` |
| 5  | -1 | MINUS | `#cc241d` |
| 4  | +1 | PLUS | `#b8bb26` |
| 3  | 0  | ERGODIC | `#d3869b` |
| 2  | -1 | MINUS | `#cc241d` |
| 1  | +1 | PLUS | `#b8bb26` |

Current position: **cycle 5, position 1/3** — PLUS

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
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS
