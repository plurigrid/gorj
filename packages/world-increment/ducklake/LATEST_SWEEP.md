# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-04-27T00:00:00Z  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Status | Repos |
|--------|------|--------|-------|
| plurigrid | org | ✅ success | 100 |
| zubyul | user | ✅ success | 27 |
| migalkin | user | ✅ success | 30 |
| DJedamski | user | ✅ success | 11 |
| kubeflow | org | ⚠️ rate-limited | — |
| TeglonLabs | org | ⚠️ rate-limited | — |
| bmorphism | user | ⚠️ rate-limited | — |
| wasita | user | ⚠️ rate-limited | — |
| kristinezheng | user | ⚠️ rate-limited | — |
| M1shaaa | user | ⚠️ rate-limited | — |
| AustinCStone | user | ⚠️ rate-limited | — |
| bmorphism events | events | ⚠️ rate-limited | — |
| zubyul events | events | ⚠️ rate-limited | — |

**Total repos ingested:** 168 (across 4 sources)  
Unauthenticated GitHub API (60 req/hr) exhausted mid-sweep; authenticated token needed for full coverage.

### GF(3) Color Chain

| id % 3 | trit | color | name |
|--------|------|-------|------|
| 0 | 0 | `#d3869b` | ERGODIC |
| 1 | 1 | `#b8bb26` | PLUS |
| 2 | -1 | `#cc241d` | MINUS |

### Top Repos by Stars (from ingested data)

| org/user | repo | language | stars |
|----------|------|----------|-------|
| kubeflow | kubeflow | — | 15,572 |
| kubeflow | pipelines | Python | 4,119 |
| kubeflow | spark-operator | Python | 3,114 |
| kubeflow | trainer | Go | 2,082 |
| kubeflow | katib | Python | 1,678 |

### DuckDB Tables

| table | rows |
|-------|------|
| world_increments | 191 |
| repo_snapshots | 1,112 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses (alice, bob, A-Z) queried against Aptos mainnet fullnode.  
All returned **0.00000000 APT** — `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
Wallets exist on-chain but have no APT CoinStore resource (unfunded or non-APT assets only).

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.00000000 |
| bob | 0x0a3c...2d5d | 0.00000000 |
| A | 0x8699...9d7a | 0.00000000 |
| B | 0x3f89...b13 | 0.00000000 |
| C | 0x38b9...35e | 0.00000000 |
| D | 0xf776...dd1 | 0.00000000 |
| E | 0xdc1d...d36 | 0.00000000 |
| F | 0x18a1...f71 | 0.00000000 |
| G | 0x69a3...f32 | 0.00000000 |
| H | 0xce67...00f | 0.00000000 |
| I | 0x070f...fc9 | 0.00000000 |
| J | 0x4d96...f54 | 0.00000000 |
| K | 0xa732...dc4 | 0.00000000 |
| L | 0x7c2e...ba9 | 0.00000000 |
| M | 0x6fed...2e9 | 0.00000000 |
| N | 0xe7dd...1b2c | 0.00000000 |
| O | 0x7325...89d | 0.00000000 |
| P | 0x6218...948 | 0.00000000 |
| Q | 0xac40...89a9 | 0.00000000 |
| R | 0x7ce6...e10 | 0.00000000 |
| S | 0xb875...386 | 0.00000000 |
| T | 0x3578...588 | 0.00000000 |
| U | 0x7586...956 | 0.00000000 |
| V | 0xb59d...2c3 | 0.00000000 |
| W | 0x5f32...7b0 | 0.00000000 |
| X | 0xa95c...47d | 0.00000000 |
| Y | 0xd8e3...44c4 | 0.00000000 |
| Z | 0x7af0...97c | 0.00000000 |

### Multisig Contract Probes (Aptos Mainnet)

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | yes |
| A-G | 0xf56c...096 | 2 | yes |
| Y-Z | 0xd3ff...883 | 2 | yes |
| S-T | 0x3b1c...883 | 2 | yes |
| V-W | 0x40fa...b6d | 2 | yes |

All multisig contracts are **2-of-2** and responding healthy.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a **Next.js SPA** — no public JSON API endpoints found.  
Probed: `/`, `/api/markets`, `/api/v1/markets`, `/api/tickers` — all return HTML.  
`mnx_snapshots` table: 0 rows (data unavailable without browser JS execution).

---

## Summary

| Component | Status |
|-----------|--------|
| GitHub sweep (plurigrid) | 100 repos ingested |
| GitHub sweep (zubyul social graph) | 27+30+11 repos ingested |
| GitHub rate-limited sources | 9 sources skipped (unauthenticated limit) |
| Aptos wallet balances (28 addrs) | all 0 APT (no CoinStore resource) |
| Multisig probes (5 contracts) | all 2-of-2 healthy |
| MNX Markets | unavailable (SPA, no JSON API) |
| DuckDB world-increments.duckdb | created/updated |
