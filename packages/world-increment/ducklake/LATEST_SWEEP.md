# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-08-07  
**Sweep IDs:** 14–24 (GF3 color chain: MINUS→ERGODIC→PLUS→MINUS→ERGODIC→PLUS→...)  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| ID | GF3 | Color | Type | Source | Repos |
|----|-----|-------|------|--------|-------|
| 14 | MINUS | #cc241d | org | plurigrid | gorj (API scope limited) |
| 15 | ERGODIC | #d3869b | org | kubeflow | N/A (API scope restricted) |
| 16 | PLUS | #b8bb26 | org | TeglonLabs | N/A (API scope restricted) |
| 17 | MINUS | #cc241d | user | bmorphism | N/A (API scope restricted) |
| 18 | ERGODIC | #d3869b | user | zubyul | N/A (API scope restricted) |
| 19 | PLUS | #b8bb26 | user | migalkin | N/A (API scope restricted) |
| 20 | MINUS | #cc241d | user | DJedamski | N/A (API scope restricted) |
| 21 | ERGODIC | #d3869b | user | wasita | N/A (API scope restricted) |
| 22 | PLUS | #b8bb26 | user | kristinezheng | N/A (API scope restricted) |
| 23 | MINUS | #cc241d | user | M1shaaa | N/A (API scope restricted) |
| 24 | ERGODIC | #d3869b | user | AustinCStone | N/A (API scope restricted) |

### Note on API Scope
The GitHub API session is scoped to `plurigrid/gorj` only. Calls to `/orgs/{org}/repos` and `/users/{user}/repos` for external sources returned HTTP 403 (`This GitHub API path is not available: sessions are bound to their configured repositories`). World increments for all 11 sources have been recorded in the GF(3) color chain, with plurigrid/gorj's latest state captured as repo_snapshot #476.

### plurigrid/gorj Latest State
- **Full name:** plurigrid/gorj  
- **Language:** Clojure  
- **Description:** MCP server + hooks that give AI coding agents a Clojure REPL  
- **Last push:** 2026-05-08T14:04:34Z  
- **Recent commit:** `5b28fe0` — chore: ignore duckdb binary in repo root  
- **Active sweep branches:** 100+ world-increment sweep branches visible  

### DuckDB Totals
| Table | Count |
|-------|-------|
| world_increments | 34 (IDs 1–24) |
| repo_snapshots | 945 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (2026-08-07)

All 28 addresses probed against Aptos mainnet (`fullnode.mainnet.aptoslabs.com`).  
All accounts returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — accounts are not initialized on mainnet (no APT deposits).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...d5d | 0.0 |
| A | 0x8699...e9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...f956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

**Total APT across all 28 wallets: 0.0**

---

### Multisig Contract Probes

All 5 pairs probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ healthy |
| A-G | 0xf56c...0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✅ healthy |
| S-T | 0x3b1c...7883 | 2 | ✅ healthy |
| V-W | 0x40fa...b6d | 2 | ✅ healthy |

**All 5/5 multisig contracts healthy — 2-of-N threshold consistently configured.**

---

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — TLS connection established but the site is a SPA with no accessible REST API. Probed paths:
- `https://testnet.mnx.fi/api/markets` → empty response
- `https://testnet.mnx.fi/api/v1/markets` → empty response

No market data could be extracted. Recorded as `N/A` in `mnx_snapshots`.

---

## Summary

| Component | Status | Notes |
|-----------|--------|-------|
| GitHub sweep (plurigrid/gorj) | ✅ | Scoped to single repo; 945 total snapshots |
| GitHub sweep (external) | ⚠️ | API restricted to plurigrid/gorj scope |
| GF(3) chain | ✅ | IDs 14–24, MINUS→ERGODIC→PLUS cycle |
| Aptos balances (28 wallets) | ✅ | All 0 APT (accounts not initialized on mainnet) |
| Multisig probes (5 pairs) | ✅ | All healthy, sigs_required=2 |
| MNX Markets | ⚠️ | SPA, no API accessible |
