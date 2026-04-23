# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-23

## Sweep Metadata
- **Date:** 2026-04-23
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Previous sweep:** 2026-04-14

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured | Most Recent Push |
|--------|------|---------------|-----------------|
| plurigrid | org | 16 | 2026-04-23 (gorj) |
| kubeflow | org | 12 | 2026-04-23 (pipelines) |
| TeglonLabs | org | 6 | 2026-01-16 (Stahl) |
| bmorphism | user | 50 | 2026-04-23 (Gay.jl) |
| zubyul | user | 8 | 2026-04-23 (voice-observatory) |
| migalkin | social | 15 | 2025-08-04 (kgcourse2021) |
| DJedamski | social | 11 | (various) |
| wasita | social | 15 | (various) |
| kristinezheng | social | 15 | (various) |
| M1shaaa | social | 15 | (various) |
| AustinCStone | social | 15 | (various) |

**Total repo_snapshots this sweep:** 178 new rows (cumulative DB total: 1,122)  
**Total world_increments:** 33 rows

### GF(3) Color Chain — New Increments (IDs 12–21)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 12 | plurigrid (org) | GithubSweep | 0 | `#d3869b` | **ERGODIC** |
| 13 | kubeflow (org) | GithubSweep | 1 | `#b8bb26` | **PLUS** |
| 14 | TeglonLabs (org) | GithubSweep | -1 | `#cc241d` | **MINUS** |
| 15 | bmorphism (user) | GithubSweep | 0 | `#d3869b` | **ERGODIC** |
| 16 | zubyul (user) | GithubSweep | 1 | `#b8bb26` | **PLUS** |
| 17 | bmorphism (event) | ForkEvent | -1 | `#cc241d` | **MINUS** |
| 18 | zubyul (event) | PullRequestEvent | 0 | `#d3869b` | **ERGODIC** |
| 19 | migalkin (social) | GithubSweep | 1 | `#b8bb26` | **PLUS** |
| 20 | DJedamski (social) | GithubSweep | -1 | `#cc241d` | **MINUS** |
| 21 | hamming-swarm | AptosSnapshot | 0 | `#d3869b` | **ERGODIC** |

### Notable Recent Activity

**bmorphism recent events:**
- `ForkEvent` → xenodium/emacs-skills (2026-04-21)
- `ForkEvent` → chrisreade/PenroseKiteDart (2026-04-19)
- `ReleaseEvent` → bmorphism/tree-sitter-hy (2026-04-19)
- `PushEvent` → plurigrid/nanoclj-zig (2026-04-18)
- `PullRequestReviewEvent` → plurigrid/nash-portal (2026-04-18)

**zubyul recent events:**
- `PullRequestEvent` × 4 → plurigrid/gorj (2026-04-23) — intense PR activity today
- `PushEvent` × 5 → zubyul/voice-observatory (2026-04-23) — active dev

### Top Repos by Stars (this sweep)

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/pipelines | 4,125 | Python |
| kubeflow/spark-operator | 3,118 | Python |
| kubeflow/trainer | 2,090 | Go |
| kubeflow/katib | 1,679 | Python |
| kubeflow/manifests | 1,012 | YAML |
| kubeflow/arena | 810 | Go |
| kubeflow/kale | 685 | Python |
| kubeflow/mpi-operator | 524 | Go |
| plurigrid/asi | 17 | HTML |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (alice, bob, A–Z)

Queried 28 addresses via Aptos fullnode mainnet (ledger ~4,983,709,564).  
**Result:** All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
These are valid addresses that have not been funded / registered a CoinStore.

| World | Address (prefix…suffix) | Balance APT |
|-------|------------------------|-------------|
| alice | 0xc793…c7b | 0 (no resource) |
| bob | 0x0a3c…d5d | 0 (no resource) |
| A | 0x8699…9d7a | 0 (no resource) |
| B | 0x3f89…b13 | 0 (no resource) |
| C | 0x38b9…35e | 0 (no resource) |
| D | 0xf776…dd1 | 0 (no resource) |
| E | 0xdc1d…d36 | 0 (no resource) |
| F | 0x18a1…f71 | 0 (no resource) |
| G | 0x69a3…f32 | 0 (no resource) |
| H | 0xce67…00f | 0 (no resource) |
| I | 0x070f…c9 | 0 (no resource) |
| J | 0x4d96…f54 | 0 (no resource) |
| K | 0xa732…dc4 | 0 (no resource) |
| L | 0x7c2e…ba9 | 0 (no resource) |
| M | 0x6fed…e9 | 0 (no resource) |
| N | 0xe7dd…b2c | 0 (no resource) |
| O | 0x7325…89d | 0 (no resource) |
| P | 0x6218…948 | 0 (no resource) |
| Q | 0xac40…a9 | 0 (no resource) |
| R | 0x7ce6…e10 | 0 (no resource) |
| S | 0xb875…386 | 0 (no resource) |
| T | 0x3578…588 | 0 (no resource) |
| U | 0x7586…956 | 0 (no resource) |
| V | 0xb59d…2c3 | 0 (no resource) |
| W | 0x5f32…7b0 | 0 (no resource) |
| X | 0xa95c…47d | 0 (no resource) |
| Y | 0xd8e3…4c4 | 0 (no resource) |
| Z | 0x7af0…97c | 0 (no resource) |

### Multisig Contract Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|--------------|---------|
| A-B | 0x0da4…003 | 2 | ✓ |
| A-G | 0xf56c…096 | 2 | ✓ |
| Y-Z | 0xd3ff…883 | 2 | ✓ |
| S-T | 0x3b1c…883 | 2 | ✓ |
| V-W | 0x40fa…eb6 | 2 | ✓ |

**All 5 multisig contracts healthy** — 2-of-N threshold confirmed.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` serves a Next.js SPA. Probed `/`, `/api/markets`, `/api/tickers`.  
No machine-readable JSON API endpoints found — data is client-rendered only.  
**Status: SPA_UNAVAILABLE** — recorded in `mnx_snapshots`.

---

## DuckDB Table Summary

| Table | Rows (total) | Notes |
|-------|-------------|-------|
| world_increments | 33 | GF3 color-chained events |
| repo_snapshots | 1,122 | 11 sources, 2 sweep dates |
| aptos_snapshots | 28 | All unfunded (0 APT) |
| multisig_probes | 5 | All healthy, sigs=2 |
| mnx_snapshots | 1 | SPA_UNAVAILABLE |

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
