# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-12

## Sweep Metadata
- **Date:** 2026-07-12
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (via Python `duckdb`)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 26 |
| New Increments This Run | 3 (IDs 13–15) |
| Total Repo Snapshots (cumulative) | 944 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | Unavailable (401) |

---

## JOB 1: GitHub Social Graph Sweep

### Status: Scope-Restricted

GitHub MCP access in this session is scoped to **`plurigrid/gorj`** only.
Queries to external orgs (plurigrid-org, kubeflow, TeglonLabs) and users
(bmorphism, zubyul, migalkin, DJedamski, wasita, kristinezheng, M1shaaa,
AustinCStone) were not executed — the session scope blocks cross-org/user
reads. The previous sweep (2026-04-12) captured 471 repo snapshots across
these sources; those records remain in the DB (now 944 total with earlier
increments).

### Increment 13 — PLUS `#b8bb26`
- **Source:** github_scope / `plurigrid/gorj`
- **Event:** github_sweep_restricted
- **GF3:** trit=+1, color=#b8bb26, name=PLUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 Hamming Swarm addresses (alice, bob, A–Z) returned
`resource_not_found` from Aptos mainnet (ledger version ~6.23B).
None of these addresses have an initialized `0x1::coin::CoinStore<AptosCoin>`
resource — the wallets have not been funded on mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|--------------|
| alice | 0xc793...cc7b | not_found |
| bob   | 0x0a3c...12d5 | not_found |
| A     | 0x8699...9d7a | not_found |
| B     | 0x3f89...b13  | not_found |
| C     | 0x38b9...535e | not_found |
| D     | 0xf776...fdd1 | not_found |
| E     | 0xdc1d...d36  | not_found |
| F     | 0x18a1...cf71 | not_found |
| G     | 0x69a3...7f32 | not_found |
| H     | 0xce67...300f | not_found |
| I     | 0x070f...1fc9 | not_found |
| J     | 0x4d96...7f54 | not_found |
| K     | 0xa732...dc4  | not_found |
| L     | 0x7c2e...ba9  | not_found |
| M     | 0x6fed...f2e9 | not_found |
| N     | 0xe7dd...1b2c | not_found |
| O     | 0x7325...89d  | not_found |
| P     | 0x6218...948  | not_found |
| Q     | 0xac40...89a9 | not_found |
| R     | 0x7ce6...6e10 | not_found |
| S     | 0xb875...386  | not_found |
| T     | 0x3578...4588 | not_found |
| U     | 0x7586...956  | not_found |
| V     | 0xb59d...2c3  | not_found |
| W     | 0x5f32...c7b0 | not_found |
| X     | 0xa95c...047d | not_found |
| Y     | 0xd8e3...44c4 | not_found |
| Z     | 0x7af0...97c  | not_found |

### Increment 14 — MINUS `#cc241d`
- **Source:** blockchain / `aptos-mainnet`
- **Event:** wallet_sweep / hamming-swarm-A-Z
- **GF3:** trit=-1, color=#cc241d, name=MINUS

---

### Multisig Contract Probes

All 5 probed multisig pairs are **healthy**: each requires exactly **2 signatures**.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

### Increment 15 — ERGODIC `#d3869b`
- **Source:** blockchain / `aptos-mainnet`
- **Event:** multisig_probe / hamming-pairs
- **GF3:** trit=0, color=#d3869b, name=ERGODIC

---

### MNX Markets (testnet.mnx.fi)

Both `https://testnet.mnx.fi` and `https://testnet.mnx.fi/api/markets` returned
**HTTP 401 Unauthorized** — the testnet requires authentication and is not
publicly accessible. No market data recorded.

---

## GF(3) Color Chain — New Increments

```
ID 13: PLUS   (#b8bb26)  github_sweep_restricted  [plurigrid/gorj]
ID 14: MINUS  (#cc241d)  wallet_sweep             [aptos-mainnet / hamming-swarm-A-Z]
ID 15: ERGODIC (#d3869b) multisig_probe           [aptos-mainnet / hamming-pairs]
```

Chain so far (last 6): `… PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

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

## Key Findings
- **Hamming Swarm:** All 28 mainnet addresses uninitialized — no APT balances on-chain
- **Multisig health:** All 5 pairs (A-B, A-G, Y-Z, S-T, V-W) healthy at 2-of-N threshold
- **MNX testnet:** Auth-gated, no public market data available
- **GitHub scope:** Session restricted to `plurigrid/gorj`; cross-org sweep deferred
