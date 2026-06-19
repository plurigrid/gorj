# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-19 10:08 UTC

## Sweep Metadata
- **Date:** 2026-06-19 10:08 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 420 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain — 11 Increments

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 1  | plurigrid | org | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | org | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | user | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | user | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | user | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | user | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | user | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## Repo Snapshot Summary

### By Source (total repos per source)

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 (of 101) |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 (of 104) |
| zubyul | user | 49 |
| migalkin | user | 19 |
| DJedamski | user | 6 |
| wasita | user | 40 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| AustinCStone | user | 40 |

### Notable Recent Activity (most recently pushed)

| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| M1shaaa/M1shaaa | (config) | 0 | 2026-06-19 |
| TeglonLabs/jank-crane | C++ | 0 | 2026-06-08 |
| kristinezheng/kristinezheng.github.io | HTML | 0 | 2026-06-07 |
| wasita/wasita.github.io | Svelte | 1 | 2026-06-15 |

---

## Hamming Swarm — Aptos Wallet Balances

All 28 wallet addresses (alice, bob, A–Z) returned **null** from Aptos mainnet CoinStore resource — accounts either have zero APT balance or have not been initialized on mainnet.

| Label | Address (truncated) |
|-------|---------------------|
| alice | 0xc793...c7b |
| bob | 0x0a3c...12d5d |
| A–Z | (26 addresses probed) |

> All balances: `null` (accounts not found / zero APT on mainnet)

---

## Multisig Contract Probes

All 5 multisig contracts are **healthy** — each requires **2-of-N** signatures.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ healthy |
| A-G | 0xf56c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

---

## MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — `testnet.mnx.fi` requires Vercel authentication (deployment protection active). No market data could be retrieved. The site returns a 401/auth challenge page. No `mnx_snapshots` rows inserted.

---

## DuckDB Table Status

| Table | Rows |
|-------|------|
| world_increments | 11 |
| repo_snapshots | 420 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (auth wall) |
