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
| Total World Increments | 26 (max id 15) |
| Total Repo Snapshots | 945 |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | Unavailable |

---

## GitHub Social Graph Sweep

**Scope restriction:** GitHub API proxy in this environment restricts API calls to
`repos/plurigrid/gorj/*` only. Cross-org/user queries (plurigrid, kubeflow, TeglonLabs,
bmorphism, zubyul, social graph) were blocked with 403. Prior sweep data (471 repo
snapshots from 2026-04-12) remains intact in the database.

### plurigrid/gorj (in-scope snapshot)
- **Latest commit:** `5b28fe0` — "chore: ignore duckdb binary in repo root" (2026-05-08)
- **Active sweep branches:** 50+ `world-increment/sweep-*` branches, latest 2026-05-02
- **GF(3) increment:** id=13, PLUS (#b8bb26)

---

## GF(3) Color Chain — Increments 13–15 (this sweep)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | plurigrid/gorj | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 14 | aptos_mainnet | hamming_snapshot | -1 | `#cc241d` | **MINUS** |
| 15 | world-increment-sweep | sweep_complete | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain continues: `…ERGODIC (12) → PLUS (13) → MINUS (14) → ERGODIC (15)`

---

## Hamming Swarm Snapshot — Aptos Mainnet

**Probed:** 28 addresses (alice, bob, A–Z) via `fullnode.mainnet.aptoslabs.com`
**Timestamp:** 2026-07-30 UTC

| Address | Label | APT Balance |
|---------|-------|-------------|
| 0xc793...c7b | alice | 0.0 |
| 0x0a3c...d5d | bob | 0.0 |
| 0x8699...9d7a | A | 0.0 |
| 0x3f89...b13 | B | 0.0 |
| 0x38b9...35e | C | 0.0 |
| 0xf776...dd1 | D | 0.0 |
| 0xdc1d...d36 | E | 0.0 |
| 0x18a1...f71 | F | 0.0 |
| 0x69a3...f32 | G | 0.0 |
| 0xce67...00f | H | 0.0 |
| 0x070f...c9 | I | 0.0 |
| 0x4d96...f54 | J | 0.0 |
| 0xa732...dc4 | K | 0.0 |
| 0x7c2e...ba9 | L | 0.0 |
| 0x6fed...2e9 | M | 0.0 |
| 0xe7dd...b2c | N | 0.0 |
| 0x7325...89d | O | 0.0 |
| 0x6218...948 | P | 0.0 |
| 0xac40...9a9 | Q | 0.0 |
| 0x7ce6...e10 | R | 0.0 |
| 0xb875...386 | S | 0.0 |
| 0x3578...588 | T | 0.0 |
| 0x7586...956 | U | 0.0 |
| 0xb59d...2c3 | V | 0.0 |
| 0x5f32...b0 | W | 0.0 |
| 0xa95c...47d | X | 0.0 |
| 0xd8e3...4c4 | Y | 0.0 |
| 0x7af0...97c | Z | 0.0 |

**Note:** All addresses returned `resource_not_found` for CoinStore<AptosCoin> — no APT
balances on mainnet. Addresses may hold other assets or be unfunded.

---

## Multisig Contract Probes

All 5 contracts probed via `POST /v1/view` with `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c...096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ff...883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c...883 | 2 | ✅ HEALTHY |
| V-W | 0x40fa...b6d | 2 | ✅ HEALTHY |

All multisig contracts responding and requiring 2-of-N signatures.

---

## MNX Markets

`https://testnet.mnx.fi/api/markets` → 404 (SPA, no REST endpoint)
`https://api.testnet.mnx.fi/markets` → HTML error (not JSON API)
**Status:** Unavailable — testnet SPA does not expose a public REST market-data endpoint.

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

## Historical Totals (cumulative)
- World increments recorded: 26 rows (ids 1–15, some overlap from prior partial runs)
- Repo snapshots: 945 rows
- Aptos snapshots: 28 rows (first Hamming swarm snapshot)
- Multisig probes: 5 rows (all healthy)
