# World Increment Sweep + Hamming Snapshot

**Timestamp:** 2026-08-09 (automated sweep)
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social graph) | 2 visible |
| DJedamski | user (social graph) | 2 visible |
| wasita | user (social graph) | 2 visible |
| kristinezheng | user (social graph) | 2 visible |
| M1shaaa | user (social graph) | 2 visible |
| AustinCStone | user (social graph) | 2 visible |

**Total repo snapshots inserted this run:** 308
**Total world_increments rows (cumulative):** 326
**Total repo_snapshots rows (cumulative):** 1247

### Notable Repos (Recent Activity)
- `plurigrid/shepherd` (Scheme) — pushed 2026-01-23
- `TeglonLabs/jank-crane` (C++) — crane-jank converged-IR hub — pushed 2026-06-08
- `TeglonLabs/mathpix-gem` (Ruby) — Mathematical OCR gem — pushed 2026-01-01, 2★
- `bmorphism` user — 100 repos across many languages
- `kubeflow` org — 49 repos, ML infra ecosystem

### GF(3) Color Chain Applied
- `id % 3 == 0` → trit=0, ERGODIC `#d3869b`
- `id % 3 == 1` → trit=1, PLUS `#b8bb26`
- `id % 3 == 2` → trit=-1, MINUS `#cc241d`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses in the Hamming swarm (alice, bob, A–Z) probed against Aptos mainnet.

| Address | APT Balance |
|---------|------------|
| alice | 0.00000000 |
| bob | 0.00000000 |
| A–Z (26 addrs) | 0.00000000 each |

**Status:** All wallets report 0 APT on mainnet. Accounts exist on-chain (CoinStore resource found) but hold no balance. This is consistent with prior sweeps.

**Total APT across swarm:** 0.00000000 APT

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | `0x0da4f428...` | 2 | ✓ |
| A-G | `0xf56c4a1c...` | 2 | ✓ |
| Y-Z | `0xd3ffe181...` | 2 | ✓ |
| S-T | `0x3b1c3ae9...` | 2 | ✓ |
| V-W | `0x40fad7b4...` | 2 | ✓ |

**Status:** All 5 multisig accounts healthy, each requiring 2-of-N signatures. No changes from prior sweeps.

### MNX Markets (testnet.mnx.fi)

**Status:** Site is accessible (Next.js SPA, ~58KB HTML). API paths `/api/markets`, `/api/v1/markets`, `/api/tickers` do not return JSON data — market data is loaded client-side. No structured market data extractable via HTTP probe. Logged as unavailable in `mnx_snapshots` table.

---

## DuckDB Table Summary

| Table | Rows (cumulative) |
|-------|------------------|
| world_increments | 326 |
| repo_snapshots | 1247 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

---

## Sweep Health

- GitHub queries: **5/5 orgs/users** successfully queried (social graph limited to public repos)
- Aptos balances: **28/28** addresses probed
- Multisig contracts: **5/5** healthy, 2-of-N each
- MNX Markets: **unavailable** (SPA, no REST API)
