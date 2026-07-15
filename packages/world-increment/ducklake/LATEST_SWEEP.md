# World-Increment Sweep — 2026-07-15

## Sweep Metadata
- **Date:** 2026-07-15
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Python library)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| New World Increments (this run) | 12 |
| Total World Increments (all time) | 35 |
| Total Repo Snapshots (all time) | 945 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GitHub Sweep — Status

**Result: BLOCKED by environment proxy**

The remote execution environment's network proxy restricts all GitHub API calls to
repository-scoped endpoints for `plurigrid/gorj` only. Org/user listing endpoints
(`/orgs/{org}/repos`, `/users/{user}/repos`) returned 403 for all sources.

**MCP GitHub tools** are additionally scoped to `plurigrid/gorj` only; search outside
this repo is prohibited by session policy.

**What was captured:**
- Latest `plurigrid/gorj` commit: `5b28fe0` — `chore: ignore duckdb binary in repo root` (2026-05-08)
- 20 recent commits logged (all by Claude agent)

**Sources attempted (all blocked externally):**

| # | Source | Type | Status |
|---|--------|------|--------|
| 1 | plurigrid | org | proxy blocked |
| 2 | kubeflow | org | proxy blocked |
| 3 | TeglonLabs | org | proxy blocked |
| 4 | bmorphism | user | proxy blocked |
| 5 | zubyul | user | proxy blocked |
| 6 | migalkin | user | proxy blocked |
| 7 | DJedamski | user | proxy blocked |
| 8 | wasita | user | proxy blocked |
| 9 | kristinezheng | user | proxy blocked |
| 10 | M1shaaa | user | proxy blocked |
| 11 | AustinCStone | user | proxy blocked |

---

## GF(3) Color Chain — This Run (ids 13–24)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|----------|-------|------|
| 13 | plurigrid | repo_sweep_blocked | +1 | `#b8bb26` | **PLUS** |
| 14 | kubeflow | repo_sweep_blocked | -1 | `#cc241d` | **MINUS** |
| 15 | TeglonLabs | repo_sweep_blocked | 0 | `#d3869b` | **ERGODIC** |
| 16 | bmorphism | repo_sweep_blocked | +1 | `#b8bb26` | **PLUS** |
| 17 | zubyul | repo_sweep_blocked | -1 | `#cc241d` | **MINUS** |
| 18 | migalkin | repo_sweep_blocked | 0 | `#d3869b` | **ERGODIC** |
| 19 | DJedamski | repo_sweep_blocked | +1 | `#b8bb26` | **PLUS** |
| 20 | wasita | repo_sweep_blocked | -1 | `#cc241d` | **MINUS** |
| 21 | kristinezheng | repo_sweep_blocked | 0 | `#d3869b` | **ERGODIC** |
| 22 | M1shaaa | repo_sweep_blocked | +1 | `#b8bb26` | **PLUS** |
| 23 | AustinCStone | repo_sweep_blocked | -1 | `#cc241d` | **MINUS** |
| 24 | hamming_sweep | sweep_complete | 0 | `#d3869b` | **ERGODIC** |

---

## Hamming Swarm Snapshot — Aptos Wallets (2026-07-15)

**Status: All 28 addresses probed. All return `resource_not_found` for `CoinStore<AptosCoin>`.**
This means these accounts have never been initialized with APT on mainnet (no on-chain CoinStore resource).

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793...c7b | 0.0 (uninit) |
| bob   | 0x0a3c...5d | 0.0 (uninit) |
| A | 0x8699...7a | 0.0 (uninit) |
| B | 0x3f89...13 | 0.0 (uninit) |
| C | 0x38b9...5e | 0.0 (uninit) |
| D | 0xf776...d1 | 0.0 (uninit) |
| E | 0xdc1d...36 | 0.0 (uninit) |
| F | 0x18a1...71 | 0.0 (uninit) |
| G | 0x69a3...32 | 0.0 (uninit) |
| H | 0xce67...0f | 0.0 (uninit) |
| I | 0x070f...c9 | 0.0 (uninit) |
| J | 0x4d96...54 | 0.0 (uninit) |
| K | 0xa732...c4 | 0.0 (uninit) |
| L | 0x7c2e...a9 | 0.0 (uninit) |
| M | 0x6fed...e9 | 0.0 (uninit) |
| N | 0xe7dd...2c | 0.0 (uninit) |
| O | 0x7325...9d | 0.0 (uninit) |
| P | 0x6218...48 | 0.0 (uninit) |
| Q | 0xac40...a9 | 0.0 (uninit) |
| R | 0x7ce6...10 | 0.0 (uninit) |
| S | 0xb875...86 | 0.0 (uninit) |
| T | 0x3578...88 | 0.0 (uninit) |
| U | 0x7586...56 | 0.0 (uninit) |
| V | 0xb59d...c3 | 0.0 (uninit) |
| W | 0x5f32...b0 | 0.0 (uninit) |
| X | 0xa95c...7d | 0.0 (uninit) |
| Y | 0xd8e3...c4 | 0.0 (uninit) |
| Z | 0x7af0...7c | 0.0 (uninit) |

---

## Multisig Contract Probes

All 5 contracts healthy — all require **2-of-N signatures**.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

---

## MNX Markets

**Status: UNAVAILABLE — `https://testnet.mnx.fi` returns HTTP 401 Unauthorized**

The testnet requires authentication. No market data extracted.

---

## Environment Constraints Observed

| Constraint | Detail |
|-----------|--------|
| GitHub API proxy scope | Restricted to `plurigrid/gorj` repository-scoped endpoints only |
| GitHub MCP session scope | `plurigrid/gorj` only (by policy) |
| Aptos mainnet | All 28 wallet addresses uninitiated (no CoinStore resource) |
| MNX testnet | 401 Unauthorized |
| DuckDB CLI | Not installable (403 from GitHub releases); used Python library instead |
