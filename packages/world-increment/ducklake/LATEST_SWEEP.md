# World-Increment Sweep — 2026-07-30

## Sweep Metadata
- **Date:** 2026-07-30
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 13 |
| Total Repo Snapshots | 946 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Market Snapshots | 0 (SPA-only, no API) |

---

## GF(3) Color Chain — Latest Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_sweep | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_sweep | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_sweep | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 12 | bmorphism (org) | sweep_complete | 0 | `#d3869b` | **ERGODIC** |
| **13** | **plurigrid/gorj** | **sweep_complete** | **+1** | **`#b8bb26`** | **PLUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

---

## GitHub Sweep — 2026-07-30

### Access Scope
GitHub API in this session is restricted to `plurigrid/gorj` only (repository-scoped token). Org-level and cross-user queries for kubeflow, TeglonLabs, bmorphism, zubyul, and social graph users were blocked. Historical data from previous sweeps (471 repo snapshots across 11 sources as of 2026-04-12) is preserved in the ducklake.

### plurigrid/gorj — Latest Snapshot
| Field | Value |
|-------|-------|
| Language | Clojure |
| Description | MCP server + hooks that give AI coding agents a Clojure REPL |
| Latest commit | `5b28fe01` — 2026-05-08 |
| Commit author | claude |
| Branches | 30+ active world-increment sweep branches |

### Recent Commits (plurigrid/gorj)
| SHA | Date | Message |
|-----|------|---------|
| `5b28fe01` | 2026-05-08 | chore: ignore duckdb binary in repo root |
| `ebf263f5` | 2026-04-14 | world-increment ducklake: sync world.duckdb sweep state |
| `b434a43c` | 2026-04-14 | Merge sweep state into master |
| `631518bc` | 2026-04-12 | world-increment sweep 2026-04-12: insert id=12 ERGODIC |
| `c4238bcf` | 2026-04-10 | world-increments.duckdb: sync latest sweep state |

---

## Hamming Swarm Snapshot — 2026-07-30

### Aptos Mainnet Wallet Balances

All 28 wallets queried against Aptos mainnet (`fullnode.mainnet.aptoslabs.com`).
API returned `resource_not_found` for all addresses — CoinStore resource absent (unfunded accounts).

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | `0xc793...cc7b` | 0.00000000 |
| bob   | `0x0a3c...2d5d` | 0.00000000 |
| A     | `0x8699...e9d7` | 0.00000000 |
| B     | `0x3f89...b13` | 0.00000000 |
| C     | `0x38b9...535e` | 0.00000000 |
| D     | `0xf776...fdd1` | 0.00000000 |
| E     | `0xdc1d...8d36` | 0.00000000 |
| F     | `0x18a1...cf71` | 0.00000000 |
| G     | `0x69a3...7f32` | 0.00000000 |
| H     | `0xce67...300f` | 0.00000000 |
| I     | `0x070f...1fc9` | 0.00000000 |
| J     | `0x4d96...7f54` | 0.00000000 |
| K     | `0xa732...25dc4` | 0.00000000 |
| L     | `0x7c2e...eba9` | 0.00000000 |
| M     | `0x6fed...7f2e9` | 0.00000000 |
| N     | `0xe7dd...51b2c` | 0.00000000 |
| O     | `0x7325...5a89d` | 0.00000000 |
| P     | `0x6218...c948` | 0.00000000 |
| Q     | `0xac40...c89a9` | 0.00000000 |
| R     | `0x7ce6...6e10` | 0.00000000 |
| S     | `0xb875...d386` | 0.00000000 |
| T     | `0x3578...4588` | 0.00000000 |
| U     | `0x7586...f956` | 0.00000000 |
| V     | `0xb59d...af2c3` | 0.00000000 |
| W     | `0x5f32...c7b0` | 0.00000000 |
| X     | `0xa95c...047d` | 0.00000000 |
| Y     | `0xd8e3...444c4` | 0.00000000 |
| Z     | `0x7af0...197c` | 0.00000000 |

**Total APT across all 28 wallets: 0.00000000**

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B  | `0x0da4...7003` | 2 | ✓ |
| A-G  | `0xf56c...0096` | 2 | ✓ |
| Y-Z  | `0xd3ff...b883` | 2 | ✓ |
| S-T  | `0x3b1c...7883` | 2 | ✓ |
| V-W  | `0x40fa...eb6d` | 2 | ✓ |

**All 5 multisigs healthy. Threshold: 2-of-N signatures required.**

### MNX Markets

`testnet.mnx.fi` returned a Next.js SPA with no accessible JSON API endpoints at standard paths (`/api/markets`, `/api/v1/markets`). No market data extractable. Status: **unavailable via API**.

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

## Notes
- GitHub API restricted to `plurigrid/gorj` scope in this session; broader org/user sweeps blocked by token scope
- Aptos: all 28 hamming-swarm wallets have no CoinStore resource (unfunded on mainnet as of ledger version 6531092860)
- Multisig: all 5 contracts respond correctly with threshold=2
- MNX: SPA-rendered, no REST API surface found
