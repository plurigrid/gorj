# World-Increment Sweep — 2026-07-13

## Sweep Metadata
- **Date:** 2026-07-13 14:12 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Aptos ledger version:** 6258464225 (epoch 16521)

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (all-time) | 35 |
| New Increments This Run | 12 (ids 13–24) |
| Total Repo Snapshots (all-time) | 944 |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (Vercel auth) |

---

## JOB 1: GitHub Social Graph Sweep

> **Note:** GitHub API access in this environment is restricted to repository-scoped endpoints (`plurigrid/gorj`). Org/user repo listing APIs (`/orgs/{org}/repos`, `/users/{user}/repos`) returned 403 — blocked by the session scope. Increments are recorded for all 12 sources; repo_snapshots carry forward the 944 rows from previous sweeps.

### GF(3) Color Chain — This Run (IDs 13–24)

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 13 | plurigrid | org | +1 | `#b8bb26` | **PLUS** |
| 14 | kubeflow | org | -1 | `#cc241d` | **MINUS** |
| 15 | TeglonLabs | org | 0 | `#d3869b` | **ERGODIC** |
| 16 | bmorphism | user | +1 | `#b8bb26` | **PLUS** |
| 17 | zubyul | user | -1 | `#cc241d` | **MINUS** |
| 18 | migalkin | user | 0 | `#d3869b` | **ERGODIC** |
| 19 | DJedamski | user | +1 | `#b8bb26` | **PLUS** |
| 20 | wasita | user | -1 | `#cc241d` | **MINUS** |
| 21 | kristinezheng | user | 0 | `#d3869b` | **ERGODIC** |
| 22 | M1shaaa | user | +1 | `#b8bb26` | **PLUS** |
| 23 | AustinCStone | user | -1 | `#cc241d` | **MINUS** |
| 24 | bmorphism (events) | user | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain continues: `… PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

### gorj Recent Activity (in-scope)
Latest commit: `5b28fe0` — chore: ignore duckdb binary in repo root (2026-05-08)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)

All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger v6258464225. These wallets likely use the Fungible Asset (FA) standard for APT rather than the legacy CoinStore, or have not been initialized on-chain.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793…cc7b | resource_not_found |
| bob | 0x0a3c…512d | resource_not_found |
| A | 0x8699…9d7a | resource_not_found |
| B | 0x3f89…cb13 | resource_not_found |
| C | 0x38b9…535e | resource_not_found |
| D | 0xf776…fdd1 | resource_not_found |
| E | 0xdc1d…8d36 | resource_not_found |
| F | 0x18a1…cf71 | resource_not_found |
| G | 0x69a3…7f32 | resource_not_found |
| H | 0xce67…300f | resource_not_found |
| I | 0x070f…1fc9 | resource_not_found |
| J | 0x4d96…7f54 | resource_not_found |
| K | 0xa732…5dc4 | resource_not_found |
| L | 0x7c2e…eba9 | resource_not_found |
| M | 0x6fed…f2e9 | resource_not_found |
| N | 0xe7dd…51b2c | resource_not_found |
| O | 0x7325…a89d | resource_not_found |
| P | 0x6218…c948 | resource_not_found |
| Q | 0xac40…c89a9 | resource_not_found |
| R | 0x7ce6…6e10 | resource_not_found |
| S | 0xb875…d386 | resource_not_found |
| T | 0x3578…4588 | resource_not_found |
| U | 0x7586…f956 | resource_not_found |
| V | 0xb59d…f2c3 | resource_not_found |
| W | 0x5f32…c7b0 | resource_not_found |
| X | 0xa95c…047d | resource_not_found |
| Y | 0xd8e3…444c4 | resource_not_found |
| Z | 0x7af0…197c | resource_not_found |

### Multisig Contract Probes

All 5 multisig contracts are **healthy** — each requires 2 signatures.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4…7003 | 2 | HEALTHY |
| A-G | 0xf56c…0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff…b883 | 2 | HEALTHY |
| S-T | 0x3b1c…7883 | 2 | HEALTHY |
| V-W | 0x40fa…eb6d | 2 | HEALTHY |

### MNX Markets

`https://testnet.mnx.fi` is deployed behind **Vercel deployment protection** (authentication required). All API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`, `/markets`, `/v1/markets`, `/api/pairs`) returned the Vercel auth page. Market data unavailable without a visitor password or bypass token.

---

## Access Constraints Noted

| System | Status | Reason |
|--------|--------|--------|
| GitHub org/user repos | BLOCKED | Session scoped to `plurigrid/gorj` only |
| Aptos CoinStore balances | NOT FOUND | Wallets may use FA standard; no legacy CoinStore |
| MNX testnet markets | AUTH REQUIRED | Vercel deployment protection active |
| Multisig contracts | OK | All 5 healthy, 2-of-N |
| DuckDB storage | OK | All tables written successfully |
