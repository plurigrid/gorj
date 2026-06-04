# World-Increment Sweep — 2026-05-02

## Sweep Metadata
- **Date:** 2026-05-02
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| New World Increments (this sweep) | 11 |
| Total World Increments (cumulative) | 23 |
| New Repo Snapshots (this sweep) | 343 |
| Total Repo Snapshots (cumulative) | 816 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (auth required) |

---

## GF(3) Color Chain — New Increments (IDs 13–23)

| ID | Source | Type | Event | GF3 Trit | Color | Name |
|----|--------|------|-------|-----------|-------|------|
| 13 | plurigrid | org | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 14 | kubeflow | org | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 15 | TeglonLabs | org | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 16 | bmorphism | user | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 17 | zubyul | user | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 18 | migalkin | user | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 19 | DJedamski | user | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 20 | wasita | user | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 21 | kristinezheng | user | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 22 | M1shaaa | user | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 23 | AustinCStone | user | repo_snapshot | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## GitHub Repo Snapshot

| Source | Type | Repos | Notes |
|--------|------|-------|-------|
| plurigrid | org | 100 | zig-syrup (Zig), nash-portal (Rust), horse (TeX) |
| kubeflow | org | 47 | 33,986 ⭐ total |
| TeglonLabs | org | 4 | mathpix-gem (Ruby, 2⭐), coin-flip-mcp (JS) |
| bmorphism | user | 100 | 247 ⭐ total |
| zubyul | user | 49 | 14 ⭐ total |
| migalkin | user | 5 | NodePiece (143⭐), StarE (89⭐), NBFNet_mlx |
| DJedamski | user | 6 | kaggle_ncaa18, Project_Euler |
| wasita | user | 10 | wasita.github.io (Svelte), magic-garden (Python) |
| kristinezheng | user | 6 | kristinezheng.github.io, lookit-jenga |
| M1shaaa | user | 8 | lab-bookshelf- (TypeScript) |
| AustinCStone | user | 8 | TextGAN (92⭐), StereoVisionMRF (11⭐) |

**Note:** GitHub unauthenticated API was rate-limited (60 req/hr). Data fetched via MCP GitHub search tools.

---

## Hamming Swarm — Aptos Wallet Balances

Queried via `0x1::coin::balance` view function on `fullnode.mainnet.aptoslabs.com`.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793…cc7b | 0.43643352 |
| bob | 0x0a3c…12d5d | **12.65700700** |
| A | 0x8699…9d7a | 0.05176700 |
| B | 0x3f89…b13 | 0.03625600 |
| C | 0x38b9…535e | 0.01018500 |
| D | 0xf776…fdd1 | 0.01162900 |
| E | 0xdc1d…8d36 | 0.00937200 |
| F | 0x18a1…f71 | **1.96051600** |
| G | 0x69a3…7f32 | 0.00068100 |
| H | 0xce67…300f | 0.00168100 |
| I | 0x070f…1fc9 | 0.00068100 |
| J | 0x4d96…7f54 | **1.89509300** |
| K | 0xa732…5dc4 | 0.16196100 |
| L | 0x7c2e…ba9 | **1.92726900** |
| M | 0x6fed…2e9 | 0.11228500 |
| N | 0xe7dd…b2c | 0.10612100 |
| O | 0x7325…89d | 0.21013600 |
| P | 0x6218…948 | 0.14013600 |
| Q | 0xac40…89a9 | 0.10324000 |
| R | 0x7ce6…e10 | 0.09021700 |
| S | 0xb875…386 | 0.09178800 |
| T | 0x3578…588 | 0.07371300 |
| U | 0x7586…956 | 0.05577300 |
| V | 0xb59d…2c3 | 0.04883299 |
| W | 0x5f32…7b0 | 0.04070500 |
| X | 0xa95c…47d | 0.04257700 |
| Y | 0xd8e3…4c4 | 0.04444900 |
| Z | 0x7af0…97c | 0.02426800 |

**Total APT across 28 wallets: 20.345 APT**

Richest: `bob` (12.657 APT), `F` (1.961 APT), `L` (1.927 APT), `J` (1.895 APT)

---

## Multisig Contract Probes

All 5 multisig contracts responded healthy with **2-of-N** signature requirement.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4…003 | 2 | ✓ |
| A-G | 0xf56c…096 | 2 | ✓ |
| Y-Z | 0xd3ff…883 | 2 | ✓ |
| S-T | 0x3b1c…883 | 2 | ✓ |
| V-W | 0x40fa…b6d | 2 | ✓ |

---

## MNX Markets (testnet.mnx.fi)

- Frontend: Next.js SPA, loads correctly at `https://testnet.mnx.fi`
- Backend API: `https://api.testnet.mnx.fi` — responds with Express.js errors for unknown routes
- All probed paths (`/markets`, `/tickers`, `/v1/markets`, etc.) return 404/HTML
- Status: **unavailable for unauthenticated snapshot** (requires authenticated WebSocket/session)

---

## DuckDB Table Stats (cumulative)

| Table | Rows |
|-------|------|
| world_increments | 34 (23 unique increments + 11 duplicate entries from prior sweep) |
| repo_snapshots | 1,287 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |
