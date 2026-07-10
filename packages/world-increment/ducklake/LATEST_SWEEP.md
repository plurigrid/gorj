# World-Increment Sweep — 2026-07-10

## Sweep Metadata
- **Date:** 2026-07-10
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (distinct) | 13 |
| Total Repo Snapshots | 945 |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (Vercel auth required) |

---

## New Increment — id=13 PLUS

| Field | Value |
|-------|-------|
| ID | 13 |
| GF3 trit | +1 |
| GF3 color | `#b8bb26` |
| GF3 name | **PLUS** |
| Source | plurigrid (org) |
| Event | sweep_hamming |
| Repo | gorj |
| Timestamp | 2026-07-10 |

---

## GF(3) Color Chain — All 13 Increments

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
| 12 | bmorphism | sweep_complete | 0 | `#d3869b` | **ERGODIC** |
| 13 | plurigrid | sweep_hamming | +1 | `#b8bb26` | **PLUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

---

## Hamming Swarm Snapshot — Aptos Mainnet

### Wallet Balances (2026-07-10)

All 28 addresses probed. The Aptos fullnode responded to every query; none of the addresses
have an `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource on mainnet (all return
`resource_not_found`). These are pre-provisioned Hamming swarm addresses not yet funded on mainnet.

| World | Address (truncated) | Balance APT | Status |
|-------|---------------------|-------------|--------|
| alice | 0xc793...cc7b | 0.0 | not_found |
| bob   | 0x0a3c...512d | 0.0 | not_found |
| A     | 0x8699...9d7a | 0.0 | not_found |
| B     | 0x3f89...b13 | 0.0 | not_found |
| C     | 0x38b9...35e | 0.0 | not_found |
| D     | 0xf776...dd1 | 0.0 | not_found |
| E     | 0xdc1d...d36 | 0.0 | not_found |
| F     | 0x18a1...f71 | 0.0 | not_found |
| G     | 0x69a3...f32 | 0.0 | not_found |
| H     | 0xce67...00f | 0.0 | not_found |
| I     | 0x070f...fc9 | 0.0 | not_found |
| J     | 0x4d96...f54 | 0.0 | not_found |
| K     | 0xa732...dc4 | 0.0 | not_found |
| L     | 0x7c2e...ba9 | 0.0 | not_found |
| M     | 0x6fed...2e9 | 0.0 | not_found |
| N     | 0xe7dd...b2c | 0.0 | not_found |
| O     | 0x7325...89d | 0.0 | not_found |
| P     | 0x6218...948 | 0.0 | not_found |
| Q     | 0xac40...89a9 | 0.0 | not_found |
| R     | 0x7ce6...e10 | 0.0 | not_found |
| S     | 0xb875...386 | 0.0 | not_found |
| T     | 0x3578...588 | 0.0 | not_found |
| U     | 0x7586...956 | 0.0 | not_found |
| V     | 0xb59d...2c3 | 0.0 | not_found |
| W     | 0x5f32...7b0 | 0.0 | not_found |
| X     | 0xa95c...047d | 0.0 | not_found |
| Y     | 0xd8e3...44c4 | 0.0 | not_found |
| Z     | 0x7af0...97c | 0.0 | not_found |

**Interpretation:** Hamming swarm wallets are pre-allocated but unfunded on mainnet as of 2026-07-10.
Total swarm APT: **0.0 APT**

---

### Multisig Contract Probes

All 5 multisig contracts respond to `0x1::multisig_account::num_signatures_required`.
All require **2 signatures** — consistent 2-of-N configuration across all pairs.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B  | 0x0da4...003 | 2 | ✓ |
| A-G  | 0xf56c...096 | 2 | ✓ |
| Y-Z  | 0xd3ff...883 | 2 | ✓ |
| S-T  | 0x3b1c...883 | 2 | ✓ |
| V-W  | 0x40fa...b6d | 2 | ✓ |

**All multisig pairs healthy.** 5/5 contracts live on mainnet with 2-of-N threshold.

---

### MNX Markets

`https://testnet.mnx.fi` — **Unavailable**. Site requires Vercel visitor authentication
(password-protected deployment). No market data could be extracted.

---

## GitHub Social Graph

GitHub API access for this session is proxy-restricted to repo-scoped endpoints for
`plurigrid/gorj` only. Org-level and cross-user queries (plurigrid org-list,
kubeflow, TeglonLabs, bmorphism, zubyul social graph) are blocked by the session proxy.

The `plurigrid/gorj` repo was captured as the single new repo_snapshot (id=474):
- **Language:** Clojure
- **Last push:** 2026-07-10
- **Description:** MCP server + hooks that give AI coding agents a Clojure REPL
- **Latest commit:** `5b28fe0` — "chore: ignore duckdb binary in repo root" (2026-05-08)

Historical repo data (471 repos from 11 sources) from prior sweeps remains in the database.

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
