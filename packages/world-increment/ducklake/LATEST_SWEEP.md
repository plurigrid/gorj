# World-Increment Sweep — 2026-07-29

## Sweep Metadata
- **Date:** 2026-07-29
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Ledger version (Aptos):** 6,502,285,801+

---

## Summary Counts

| Metric | Value |
|--------|-------|
| New World Increments | 3 (IDs 13–15) |
| Cumulative Increments | 15 |
| Aptos Wallets Snapshotted | 28 |
| Total APT Across Swarm | 20.3448 APT |
| Multisig Contracts Probed | 5 |
| Multisigs Healthy | 5 / 5 |
| MNX Markets | Unavailable (SPA only) |
| GitHub Scope | plurigrid/gorj (restricted session) |

---

## GF(3) Color Chain — New Increments (IDs 13–15)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | plurigrid/gorj | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 14 | aptos_mainnet (hamming_swarm) | balance_snapshot | -1 | `#cc241d` | **MINUS** |
| 15 | aptos_mainnet (hamming_swarm) | multisig_probe | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain continuation: `… ERGODIC → PLUS → MINUS → ERGODIC`

---

## JOB 1: GitHub Social Graph Sweep

**Note:** This session's GitHub API scope is restricted to `plurigrid/gorj`. Org-level and cross-user queries (kubeflow, TeglonLabs, bmorphism, zubyul social graph) were blocked. Prior sweep data from 2026-04-12 (IDs 1–12, 944 repo snapshots) remains in the database.

### plurigrid/gorj (scoped access)
- Repository accessible; no new commits in the past 7 days
- Prior sweep captured 944 total repo snapshots across 3 orgs + 8 users

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Balances queried via `0x1::coin::balance` view function (handles both legacy CoinStore and FA standard).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793…cc7b | 0.43643352 |
| bob   | 0x0a3c…512d | **12.65700700** |
| A     | 0x8699…e9d7 | 0.05176700 |
| B     | 0x3f89…b13 | 0.03625600 |
| C     | 0x38b9…535e | 0.01018500 |
| D     | 0xf776…fdd1 | 0.01162900 |
| E     | 0xdc1d…8d36 | 0.00937200 |
| F     | 0x18a1…cf71 | **1.96051600** |
| G     | 0x69a3…7f32 | 0.00068100 |
| H     | 0xce67…300f | 0.00168100 |
| I     | 0x070f…1fc9 | 0.00068100 |
| J     | 0x4d96…7f54 | **1.89509300** |
| K     | 0xa732…5dc4 | 0.16196100 |
| L     | 0x7c2e…eba9 | **1.92726900** |
| M     | 0x6fed…f2e9 | 0.11228500 |
| N     | 0xe7dd…1b2c | 0.10612100 |
| O     | 0x7325…a89d | 0.21013600 |
| P     | 0x6218…c948 | 0.14013600 |
| Q     | 0xac40…89a9 | 0.10324000 |
| R     | 0x7ce6…6e10 | 0.09021700 |
| S     | 0xb875…0386 | 0.09178800 |
| T     | 0x3578…4588 | 0.07371300 |
| U     | 0x7586…9956 | 0.05577300 |
| V     | 0xb59d…af2c3 | 0.04883299 |
| W     | 0x5f32…c7b0 | 0.04070500 |
| X     | 0xa95c…047d | 0.04257700 |
| Y     | 0xd8e3…44c4 | 0.04444900 |
| Z     | 0x7af0…197c | 0.02426800 |

**Total Swarm APT: 20.3448**

Top 5 holders: bob (12.657), F (1.961), L (1.927), J (1.895), alice (0.436)

### Multisig Contract Probes — All Healthy ✓

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4…7003 | 2 | ✓ |
| A-G | 0xf56c…0096 | 2 | ✓ |
| Y-Z | 0xd3ff…b883 | 2 | ✓ |
| S-T | 0x3b1c…7883 | 2 | ✓ |
| V-W | 0x40fa…eb6d | 2 | ✓ |

All 5 multisig contracts require 2-of-2 signatures and are responding normally.

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable — SPA only**. All probed API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`, etc.) return the Next.js SPA shell. No market data accessible without browser-side JS execution. Placeholder row inserted in `mnx_snapshots`.

---

## Database State After Sweep

| Table | Rows |
|-------|------|
| world_increments | 15 |
| repo_snapshots | 944 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (placeholder) |
