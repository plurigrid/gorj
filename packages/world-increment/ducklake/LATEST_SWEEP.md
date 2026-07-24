# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-24

## Sweep Metadata
- **Date:** 2026-07-24
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 12 |
| Total Repo Snapshots | 1 (GitHub API scoped to plurigrid/gorj) |
| Aptos Wallets Snapshotted | 28 |
| Multisig Probes | 5 (all healthy) |
| MNX Markets | Unavailable (SPA, no API) |

---

## JOB 1: GitHub Social Graph Sweep

**Status: PARTIAL** — GitHub API proxy restricted this session to `plurigrid/gorj` only.  
All `/orgs/{org}/repos` and `/users/{user}/repos` calls were blocked:  
`"sessions are bound to their configured repositories"`

**Action required:** Expand session scope to enable full social graph sweeps.

### GF(3) Color Chain — 12 World Increments

| ID | Source | Type | Event | GF3 Trit | Color | Name |
|----|--------|------|-------|-----------|-------|------|
| 1  | plurigrid | org | social_graph_sweep | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | social_graph_sweep (blocked) | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | org | social_graph_sweep (blocked) | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | user | social_graph_sweep (blocked) | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | user | social_graph_sweep (blocked) | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user | social_graph_sweep (blocked) | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | user | social_graph_sweep (blocked) | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | user | social_graph_sweep (blocked) | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | user | social_graph_sweep (blocked) | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | social_graph_sweep (blocked) | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | social_graph_sweep (blocked) | -1 | `#cc241d` | **MINUS** |
| 12 | aptos_mainnet | blockchain | hamming_swarm (wallets A-Z) | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

### Repo Snapshots (from previous sweep 2026-04-12 for reference)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 47 |
| AustinCStone | user | 43 |
| migalkin | user | 30 |
| wasita | user | 29 |
| zubyul | user | 24 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| **TOTAL (prev)** | | **471** |

Notable repos from prior sweep: kubeflow/kubeflow (15,565★), kubeflow/pipelines (4,119★), bmorphism/ocaml-mcp-sdk (60★), migalkin/NodePiece (143★), plurigrid/asi (16★)

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

**Status: COMPLETE** — 28 wallets queried via `0x1::coin::balance` view function  
Ledger version at query time: ~6,437,068,000

### Wallet Balances

| World | Address | Balance (APT) |
|-------|---------|:-------------:|
| alice | 0xc793...cc7b | 0.43643352 |
| bob   | 0x0a3c...2d5d | **12.657007** |
| A     | 0x8699...e9d7a | 0.051767 |
| B     | 0x3f89...b13 | 0.036256 |
| C     | 0x38b9...535e | 0.010185 |
| D     | 0xf776...fdd1 | 0.011629 |
| E     | 0xdc1d...d36 | 0.009372 |
| F     | 0x18a1...cf71 | **1.960516** |
| G     | 0x69a3...f32 | 0.000681 |
| H     | 0xce67...00f | 0.001681 |
| I     | 0x070f...fc9 | 0.000681 |
| J     | 0x4d96...f54 | **1.895093** |
| K     | 0xa732...dc4 | 0.161961 |
| L     | 0x7c2e...ba9 | **1.927269** |
| M     | 0x6fed...f2e9 | 0.112285 |
| N     | 0xe7dd...b2c | 0.106121 |
| O     | 0x7325...89d | 0.210136 |
| P     | 0x6218...948 | 0.140136 |
| Q     | 0xac40...a9 | 0.10324 |
| R     | 0x7ce6...e10 | 0.090217 |
| S     | 0xb875...386 | 0.091788 |
| T     | 0x3578...588 | 0.073713 |
| U     | 0x7586...956 | 0.055773 |
| V     | 0xb59d...f2c3 | 0.048833 |
| W     | 0x5f32...b0 | 0.040705 |
| X     | 0xa95c...47d | 0.042577 |
| Y     | 0xd8e3...4c4 | 0.044449 |
| Z     | 0x7af0...97c | 0.024268 |

### Swarm Aggregate

| Metric | Value |
|--------|-------|
| **Total APT** | **20.3448** |
| Average APT | 0.7266 |
| Max (bob) | 12.6570 |
| Min (G / I) | 0.000681 |
| Wallets > 1 APT | 4 (bob, F, J, L) |
| Wallets < 0.01 APT | 3 (G, H, I — dust) |

**Note:** None of the wallets hold a legacy `CoinStore<AptosCoin>` resource. All balances retrieved via `0x1::coin::balance` view function. Alice (`0xc793...`) is a deployed smart contract address with custom modules: `store_v2::ACSetMeta2`, `multiverse::MultiverseState`, `address_book::Mapping`.

### Multisig Contract Probes — All Healthy ✓

| Pair | Address | Sigs Required | Healthy |
|------|---------|:-------------:|:-------:|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

All 5 multisig contracts respond with `num_signatures_required = 2`.

### MNX Markets

**Status: UNAVAILABLE** — `testnet.mnx.fi` renders as a minimal SPA. The `/api/markets` path returned HTTP 404. No market data could be extracted.

---

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS
