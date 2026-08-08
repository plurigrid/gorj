# World Increment Sweep + Hamming Swarm Snapshot
**Generated:** 2026-08-08

---

## JOB 1: GitHub Social Graph Sweep

### Coverage Summary

| Source | Type | Repos Snapshotted | GF(3) Color | GF(3) Name |
|--------|------|-------------------|-------------|------------|
| plurigrid | org | 100 (of 103) | #cc241d | MINUS |
| kubeflow | org | 49 | #d3869b | ERGODIC |
| TeglonLabs | org | 5 | #b8bb26 | PLUS |
| bmorphism | user | 100 (of 106) | #b8bb26 | PLUS |
| zubyul | user | 49 | #cc241d | MINUS |
| AustinCStone | user | 41 | #d3869b | ERGODIC |
| wasita | user | 14 | #b8bb26 | PLUS |
| DJedamski | user | 6 | #cc241d | MINUS |
| kristinezheng | user | 5 | #d3869b | ERGODIC |
| M1shaaa | user | 8 | #b8bb26 | PLUS |
| **TOTAL** | | **377** | | |

### Notable Repos by Stars

**kubeflow (top stars):**
| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| kubeflow/pipelines | Python | 4181 | 2026-08-07 |
| kubeflow/trainer | Go | 2175 | 2026-08-08 |
| kubeflow/kale | Python | 699 | 2026-08-07 |
| kubeflow/sdk | Python | 136 | 2026-08-07 |

**plurigrid (most recently active):**
| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| plurigrid/gorj | Clojure | 1 | 2026-08-08 |
| plurigrid/place | TeX | 3 | 2026-08-02 |
| plurigrid/zig-syrup | Zig | 2 | 2026-07-28 |
| plurigrid/asi | HTML | 59 | 2026-07-10 |

**bmorphism (most recently active):**
| Repo | Language | Last Pushed |
|------|----------|-------------|
| bmorphism/Gay.jl | Julia | 2026-08-07 |
| bmorphism/gay-chat | Scheme | 2026-07-14 |
| bmorphism/world | Python | 2026-06-02 |

**TeglonLabs:**
| Repo | Language | Last Pushed |
|------|----------|-------------|
| TeglonLabs/jank-crane | C++ | 2026-06-08 |
| TeglonLabs/mathpix-gem | Ruby | 2026-01-01 |
| TeglonLabs/coin-flip-mcp | JavaScript | 2025-09-21 |

**wasita (highly active — wm-cv pushed 2026-08-07):**
Last activity: `wasita/wm-cv` (Svelte academic CV) pushed 2026-08-07

**M1shaaa (active today):**
Last activity: `M1shaaa/M1shaaa` (profile config) pushed 2026-08-08 01:17

### DuckDB Schema
- `world_increments`: 10 rows (one per source, GF(3) trit chain applied)
- `repo_snapshots`: 377 rows (full_name, language, stars, forks, open_issues, pushed_at, description)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

**Status: All 28 addresses returned `resource_not_found` on Aptos mainnet (ledger v6666543768).**

The CoinStore resource `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` was not found for any address. This indicates these addresses are either:
1. Not initialized on mainnet (never received APT), or
2. Have migrated to the `fungible_asset` module (Aptos moved APT to FA standard)

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793...c7b | null |
| bob | 0x0a3c...5d | null |
| A-Z | (26 addresses) | null (all) |

### Multisig Contract Probes (5 pairs)

**All 5 multisig contracts healthy — 2-of-N signatures required.**

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: SPA — no REST API endpoint found at `/api/markets` or root.**

The site returns HTTP 200 with a Next.js SPA. No structured market data is accessible without browser JS execution. No data inserted into `mnx_snapshots`.

---

## DuckDB Tables Written

| Table | Rows |
|-------|------|
| world_increments | 10 |
| repo_snapshots | 377 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA, no API) |

**Database:** `packages/world-increment/ducklake/world-increments.duckdb`
