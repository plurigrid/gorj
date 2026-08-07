# World-Increment Sweep — 2026-08-07

## Sweep Metadata
- **Date:** 2026-08-07
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 24 |
| Total Repo Snapshots | 945 |
| Aptos Hamming Swarm Wallets | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Market Snapshots | 0 (SPA — no API available) |

---

## GF(3) Color Chain — New Increment (id=13)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | plurigrid/gorj | sweep_complete | +1 | `#b8bb26` | **PLUS** |

GF(3) rule: `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS

Previous chain closed at id=12 (ERGODIC, 2026-04-12). This sweep opens the 5th GF(3) cycle.

---

## Job 1: GitHub Social Graph Sweep

**Status: Partial** — GitHub API via proxy is restricted to repository-scoped endpoints only (`repos/{owner}/{repo}/...`). Cross-org/user sweeps (`/orgs/{org}/repos`, `/users/{user}/repos`) return HTTP 403 from the proxy.

Accessible data (via GitHub MCP):
- **plurigrid/gorj** — the scoped repo, added as repo_snapshot (increment_id=13)
- **Recent commits:** 10 reviewed, latest 2026-05-08 (Claude — chore: ignore duckdb binary)
- **Open branches:** 20+ `world-increment/sweep-*` branches in flight

Sources attempted (all blocked by proxy):
| Source | Type | Result |
|--------|------|--------|
| plurigrid | org | API blocked |
| kubeflow | org | API blocked |
| TeglonLabs | org | API blocked |
| bmorphism | user | API blocked |
| zubyul | user | API blocked |
| migalkin | user | API blocked |
| DJedamski | user | API blocked |
| wasita | user | API blocked |
| kristinezheng | user | API blocked |
| M1shaaa | user | API blocked |
| AustinCStone | user | API blocked |

---

## Job 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 wallets queried against `fullnode.mainnet.aptoslabs.com`. All returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — accounts exist on-chain but hold no APT (unfunded / no native coin store initialized).

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0 |
| bob   | 0x0a3c...512d | 0 |
| A | 0x8699...b9d7a | 0 |
| B | 0x3f89...b13 | 0 |
| C | 0x38b9...535e | 0 |
| D | 0xf776...cfdd1 | 0 |
| E | 0xdc1d...8d36 | 0 |
| F | 0x18a1...cf71 | 0 |
| G | 0x69a3...7f32 | 0 |
| H | 0xce67...300f | 0 |
| I | 0x070f...1fc9 | 0 |
| J | 0x4d96...7f54 | 0 |
| K | 0xa732...25dc4 | 0 |
| L | 0x7c2e...eba9 | 0 |
| M | 0x6fed...7f2e9 | 0 |
| N | 0xe7dd...51b2c | 0 |
| O | 0x7325...a89d | 0 |
| P | 0x6218...ec948 | 0 |
| Q | 0xac40...c89a9 | 0 |
| R | 0x7ce6...6e10 | 0 |
| S | 0xb875...d0386 | 0 |
| T | 0x3578...f4588 | 0 |
| U | 0x7586...f9956 | 0 |
| V | 0xb59d...af2c3 | 0 |
| W | 0x5f32...c7b0 | 0 |
| X | 0xa95c...047d | 0 |
| Y | 0xd8e3...444c4 | 0 |
| Z | 0x7af0...197c | 0 |

### Multisig Contract Probes

All 5 probed via `0x1::multisig_account::num_signatures_required`. **All healthy — 2/2 signatures required.**

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ healthy |
| A-G | 0xf56c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA. All path probes (`/api/markets`, `/api/v1/markets`, `/markets`, `/api/tickers`, etc.) return the SPA HTML shell — no REST API endpoints are exposed. No `__NEXT_DATA__` embedded JSON found with market data. **0 market snapshots captured.**

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
- **Multisig swarm fully healthy** — all 5 contracts (A-B, A-G, Y-Z, S-T, V-W) respond 2-of-2
- **Hamming swarm wallets all unfunded** — 28 addresses probed, all show no APT CoinStore
- **GitHub sweep blocked** — proxy restricts to scoped repo only; plurigrid/gorj metadata captured
- **MNX testnet** — SPA-only, no API surface; 0 market records
- **Increment 13: PLUS** — opens the 5th GF(3) cycle (PLUS → MINUS → ERGODIC → ...)
