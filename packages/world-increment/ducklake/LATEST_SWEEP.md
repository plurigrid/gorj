# World-Increment Sweep — 2026-07-28

## Sweep Metadata
- **Date:** 2026-07-28
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 26 (added 3 this run: ids 13–15) |
| Total Repo Snapshots | 945 (added 1 this run: plurigrid/gorj) |
| Aptos Wallets Snapshotted | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| GitHub Scope | plurigrid/gorj only (session-scoped proxy) |
| MNX Markets | SPA — no REST API endpoint found |

---

## GF(3) New Increments — This Run

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | plurigrid (org) | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 14 | aptos-mainnet (blockchain) | hamming_swarm_snapshot | -1 | `#cc241d` | **MINUS** |
| 15 | world-increment-sweep (meta) | sweep_complete | 0 | `#d3869b` | **ERGODIC** |

GF(3) continuation: `… ERGODIC(12) → PLUS(13) → MINUS(14) → ERGODIC(15)`

---

## GitHub Social Graph Sweep

**Note:** This session's GitHub API is scoped to `plurigrid/gorj`. Org-wide and cross-user API calls returned 403 (session-bound endpoint restriction). Only the primary repo was snapshotted.

### plurigrid/gorj (latest snapshot)
| Field | Value |
|-------|-------|
| Language | Clojure |
| Description | MCP server + hooks that give AI coding agents a Clojure REPL |
| Last Commit | `5b28fe0` — chore: ignore duckdb binary in repo root (2026-05-08) |
| Recent Activity | 10 commits from Claude agent across April–May 2026 |

**Previous sweep (2026-04-12)** covered 11 sources / 471 repos:
- plurigrid (100), kubeflow (47), TeglonLabs (53), bmorphism (100),
  zubyul (24), migalkin (30), DJedamski (11), wasita (29),
  kristinezheng (18), M1shaaa (16), AustinCStone (43)

---

## Hamming Swarm Snapshot — Aptos Mainnet

**Ledger version at query time:** ~6,493,475,733 (epoch 16,701)

### Wallet Balances (alice, bob, A–Z)

All 28 accounts confirmed **existing on-chain** (sequence numbers verified).
All 28 accounts show **0.0 APT** native coin balance (CoinStore resource absent — accounts active but holding no native APT).

| World | Address (truncated) | Balance (APT) | Exists |
|-------|---------------------|---------------|--------|
| alice | `0xc793...cc7b` | 0.0 | ✓ |
| bob   | `0x0a3c...2d5d` | 0.0 | ✓ |
| A     | `0x8699...9d7a` | 0.0 | ✓ |
| B     | `0x3f89...b13`  | 0.0 | ✓ |
| C     | `0x38b9...35e`  | 0.0 | ✓ |
| D     | `0xf776...dd1`  | 0.0 | ✓ |
| E     | `0xdc1d...d36`  | 0.0 | ✓ |
| F     | `0x18a1...f71`  | 0.0 | ✓ |
| G     | `0x69a3...f32`  | 0.0 | ✓ |
| H     | `0xce67...00f`  | 0.0 | ✓ |
| I     | `0x070f...c9`   | 0.0 | ✓ |
| J     | `0x4d96...f54`  | 0.0 | ✓ |
| K     | `0xa732...dc4`  | 0.0 | ✓ |
| L     | `0x7c2e...ba9`  | 0.0 | ✓ |
| M     | `0x6fed...2e9`  | 0.0 | ✓ |
| N     | `0xe7dd...b2c`  | 0.0 | ✓ |
| O     | `0x7325...89d`  | 0.0 | ✓ |
| P     | `0x6218...948`  | 0.0 | ✓ |
| Q     | `0xac40...89a9` | 0.0 | ✓ |
| R     | `0x7ce6...e10`  | 0.0 | ✓ |
| S     | `0xb875...386`  | 0.0 | ✓ |
| T     | `0x3578...588`  | 0.0 | ✓ |
| U     | `0x7586...956`  | 0.0 | ✓ |
| V     | `0xb59d...2c3`  | 0.0 | ✓ |
| W     | `0x5f32...b0`   | 0.0 | ✓ |
| X     | `0xa95c...47d`  | 0.0 | ✓ |
| Y     | `0xd8e3...44c4` | 0.0 | ✓ |
| Z     | `0x7af0...97c`  | 0.0 | ✓ |

---

## Multisig Contract Probes

All 5 multisig contracts are **healthy** (2-of-N threshold confirmed).

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B  | `0x0da4...003`  | 2 | ✓ healthy |
| A-G  | `0xf56c...096`  | 2 | ✓ healthy |
| Y-Z  | `0xd3ff...883`  | 2 | ✓ healthy |
| S-T  | `0x3b1c...883`  | 2 | ✓ healthy |
| V-W  | `0x40fa...b6d`  | 2 | ✓ healthy |

---

## MNX Markets

`https://testnet.mnx.fi` — Returns HTTP 200 but is a Next.js SPA.
No REST API endpoints found at `/api/markets`, `/api/v1/markets`, `/api/tickers`, or `/v1/markets`.
`/markets` path returns the SPA HTML shell. No market data extractable without browser JS execution.

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
- **All 28 Hamming swarm addresses exist on Aptos mainnet** — accounts active (sequence numbers >0), no native APT balances (wallets use other tokens or are relay/multisig accounts)
- **All 5 multisig pairs healthy** — unanimous 2-of-N threshold across A-B, A-G, Y-Z, S-T, V-W
- **Aptos mainnet ledger height:** ~931,522,929 blocks, epoch 16,701
- **GitHub scope restriction:** cross-org sweep blocked; previous run (2026-04-12) data remains valid for orgs/users; only gorj snapshotted this run
- **Increment 15:** ERGODIC — completes 5th GF(3) cycle (15 = 5×3)
