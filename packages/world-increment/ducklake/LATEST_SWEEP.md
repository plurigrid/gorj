# World-Increment Sweep — 2026-08-08

## Sweep Metadata
- **Date:** 2026-08-08
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.3.0
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 15 (ids 1–15) |
| Total Repo Snapshots | 945 (cumulative) |
| New Increments This Run | 3 (ids 13–15) |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | SPA only — no API data available |

---

## GF(3) Color Chain — This Run's Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | plurigrid/gorj (repo) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 14 | aptos_mainnet (blockchain) | balance_snapshot | -1 | `#cc241d` | **MINUS** |
| 15 | world-increment-sweep | sweep_complete | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain continuing from id=12 (ERGODIC): `PLUS → MINUS → ERGODIC`
Full cycle count: 5 complete GF(3) cycles.

---

## JOB 1: GitHub Social Graph Sweep

### Access Constraints
GitHub org-level API endpoints (`/orgs/{org}/repos`, `/users/{user}/repos`) are blocked in
this remote execution environment — all paths are repository-scoped. Only `plurigrid/gorj`
is accessible via GitHub MCP tools.

### plurigrid/gorj — Latest Commits (top 5)

| SHA (short) | Author | Date | Message |
|-------------|--------|------|---------|
| 5b28fe0 | claude | 2026-05-08 | chore: ignore duckdb binary in repo root |
| ebf263f | claude | 2026-04-14 | world-increment ducklake: sync world.duckdb sweep state |
| b434a43 | claude | 2026-04-14 | Merge sweep state into master |
| e76792f | claude | 2026-04-14 | world-increments.duckdb: sync latest sweep state |
| 631518b | claude | 2026-04-12 | world-increment sweep 2026-04-12: insert id=12 ERGODIC |

### Active Sweep Branches (sample)
28 branches exist under `world-increment/sweep-*` spanning 2026-04-27 through 2026-04-30.
Stale branches not yet merged to master.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 wallets probed via `fullnode.mainnet.aptoslabs.com`. All returned 0 APT — accounts either have zero balance or no CoinStore resource initialized.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793ac… | 0.0 |
| bob   | 0x0a3c00… | 0.0 |
| A     | 0x8699ed… | 0.0 |
| B     | 0x3f892e… | 0.0 |
| C     | 0x38b99e… | 0.0 |
| D     | 0xf77656… | 0.0 |
| E     | 0xdc1d9d… | 0.0 |
| F     | 0x18a14b… | 0.0 |
| G     | 0x69a394… | 0.0 |
| H     | 0xce67c3… | 0.0 |
| I     | 0x070fe5… | 0.0 |
| J     | 0x4d964d… | 0.0 |
| K     | 0xa73204… | 0.0 |
| L     | 0x7c2eae… | 0.0 |
| M     | 0x6fed37… | 0.0 |
| N     | 0xe7dde6… | 0.0 |
| O     | 0x73252b… | 0.0 |
| P     | 0x621879… | 0.0 |
| Q     | 0xac40fa… | 0.0 |
| R     | 0x7ce605… | 0.0 |
| S     | 0xb87530… | 0.0 |
| T     | 0x35781d… | 0.0 |
| U     | 0x75860d… | 0.0 |
| V     | 0xb59dd8… | 0.0 |
| W     | 0x5f32ae… | 0.0 |
| X     | 0xa95cbb… | 0.0 |
| Y     | 0xd8e328… | 0.0 |
| Z     | 0x7af0ef… | 0.0 |

**Total Hamming swarm APT:** 0.0 (no funded wallets detected)

### Multisig Contract Probes

All 5 multisig contracts responded with `sigs_required = 2`. Status: **HEALTHY**.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B  | 0x0da4f4… | 2 | ✓ |
| A-G  | 0xf56c4a… | 2 | ✓ |
| Y-Z  | 0xd3ffe1… | 2 | ✓ |
| S-T  | 0x3b1c3a… | 2 | ✓ |
| V-W  | 0x40fad7… | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA. All REST-style paths (`/api/markets`, `/api/v1/markets`,
`/markets`, `/api/tickers`) return the HTML shell rather than JSON. No structured market
data extractable without executing JavaScript. Status: **UNAVAILABLE via curl**.

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
