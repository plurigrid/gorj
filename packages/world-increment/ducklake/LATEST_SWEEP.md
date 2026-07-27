# World-Increment Sweep — 2026-07-27

## Sweep Metadata
- **Date:** 2026-07-27
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Increment:** id=13, GF(3)=PLUS (#b8bb26), trit=1

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 24 |
| Total Repo Snapshots | 945 |
| Aptos Wallet Snapshots | 28 |
| Multisig Probes | 5 |
| MNX Snapshots | 1 (unavailable — SPA) |

---

## GF(3) Color Chain — Latest Increment

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | world-increment-sweep | sweep_complete | +1 | `#b8bb26` | **PLUS** |

GF(3) assignment: `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS

Prior chain (last 3):
| 11 | AustinCStone | repo_snapshot | -1 | `#cc241d` | MINUS |
| 12 | bmorphism | sweep_complete | 0 | `#d3869b` | ERGODIC |
| 13 | world-increment-sweep | sweep_complete | +1 | `#b8bb26` | **PLUS** |

---

## GitHub Social Graph — Access Notes

GitHub REST API is restricted by proxy to repository-scoped endpoints only.
Org-level (`/orgs/{org}/repos`) and user-level (`/users/{user}/repos`) endpoints
return 403 from the proxy. Data sourced via MCP tools (plurigrid/gorj only).

| Source | Status | Note |
|--------|--------|------|
| plurigrid (org) | blocked | org endpoint inaccessible |
| kubeflow (org) | blocked | org endpoint inaccessible |
| TeglonLabs (org) | blocked | org endpoint inaccessible |
| bmorphism (user) | blocked | user endpoint inaccessible |
| zubyul (user) | blocked | user endpoint inaccessible |
| Social graph users (6) | blocked | user endpoints inaccessible |
| plurigrid/gorj | accessible | via MCP — 20 recent commits fetched |

### plurigrid/gorj Recent Activity (via MCP)
| SHA | Date | Message |
|-----|------|---------|
| 5b28fe0 | 2026-05-08 | chore: ignore duckdb binary in repo root |
| ebf263f | 2026-04-14 | world-increment ducklake: sync world.duckdb sweep state |
| b434a43 | 2026-04-14 | Merge sweep state into master |
| 631518b | 2026-04-12 | world-increment sweep 2026-04-12: insert id=12 ERGODIC |
| c4238bc | 2026-04-10 | world-increments.duckdb: sync latest sweep state |

Last push: 2026-05-08 by Claude agent (world-increment series).

---

## Hamming Swarm Snapshot — Aptos Mainnet

**Timestamp:** 2026-07-27 05:08 UTC  
**Chain:** Aptos Mainnet (ledger v6,472,397,108, epoch 16685)

All 28 Hamming swarm addresses queried. All returned `resource_not_found`
for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — no APT registered.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob   | 0x0a3c...512d | 0.0 |
| A–Z (26) | 0x8699...–0x7af0... | 0.0 each |

**Total Hamming swarm balance:** 0.0 APT across all 28 worlds.

---

## Multisig Probes — Aptos Mainnet

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | healthy |
| A-G | 0xf56c...0096 | 2 | healthy |
| Y-Z | 0xd3ff...b883 | 2 | healthy |
| S-T | 0x3b1c...7883 | 2 | healthy |
| V-W | 0x40fa...eb6d | 2 | healthy |

All 5 multisig contracts are live and require 2-of-N signatures.

---

## MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` returns a Next.js SPA with no public JSON API endpoint.
`/api/markets` returns 404. Market data unavailable for this sweep.

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
- **Increment 13**: PLUS — 5th GF(3) cycle opens with trit=+1
- **Multisig swarm**: All 5 pairs healthy, all require 2-of-N sigs
- **Hamming swarm**: 28 wallets all at 0.0 APT (no CoinStore resources on mainnet)
- **gorj**: 20+ world-increment commits since April; last by Claude 2026-05-08
- **MNX**: Testnet SPA only — no API data extractable this sweep
