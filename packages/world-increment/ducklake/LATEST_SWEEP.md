# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-24

## Sweep Metadata
- **Date:** 2026-06-24T03:07 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Branch:** `world-increment/sweep-2026-06-24-0307`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Distinct Repos | Total Stars |
|--------|------|---------------|-------------|
| plurigrid | org | 100 | 157 |
| bmorphism | user | 100 | 510 |
| kubeflow | org | 48 | 101,972 |
| AustinCStone | user | 40 | 324 |
| TeglonLabs | org | 5 | 14 |
| zubyul | user | 49 | 40 |
| migalkin | user | 19 | 834 |
| wasita | user | 11 | 11 |
| kristinezheng | user | 5 | 0 |
| M1shaaa | user | 8 | 0 |
| DJedamski | user | 6 | 17 |
| **TOTAL** | | **391** | **103,879** |

### Notable Recent Activity

- **M1shaaa/M1shaaa** — pushed **2026-06-24** (active today, GitHub profile config)
- **TeglonLabs/jank-crane** (C++) — pushed 2026-06-08, "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps"
- **wasita/proj-template** — pushed 2026-06-19
- **kristinezheng/kristinezheng.github.io** (HTML) — pushed 2026-06-07
- **bmorphism** — 510 total stars across 100 repos, led by `ocaml-mcp-sdk` (60★), `anti-bullshit-mcp-server` (23★)
- **migalkin/NodePiece** — 143★ knowledge graph embeddings (top by stars in social graph)
- **kubeflow/kubeflow** — 15,565★, flagship ML platform
- **AustinCStone/TextGAN** — 92★ text generation with GANs

### GF(3) Color Chain — This Sweep (454 increments)

| Trit | Color | Name | Increments |
|------|-------|------|-----------|
| 0 | `#d3869b` | ERGODIC | 150 |
| +1 | `#b8bb26` | PLUS | 152 |
| -1 | `#cc241d` | MINUS | 152 |

GF(3) assignment: `id % 3 == 0 → ERGODIC, id % 3 == 1 → PLUS, id % 3 == 2 → MINUS`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried all 28 addresses (alice, bob, A–Z) via Aptos fullnode:
`https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

**Result:** All 28 accounts return 404 — no `CoinStore<AptosCoin>` resource found.
Accounts are **uninitialized on mainnet** (zero APT balance).

| World | Address | Balance |
|-------|---------|---------|
| alice | 0xc793...4cc7b | 0 APT (uninit) |
| bob | 0x0a3c...512d | 0 APT (uninit) |
| A | 0x8699...9d7a | 0 APT (uninit) |
| B | 0x3f89...cb13 | 0 APT (uninit) |
| C | 0x38b9...535e | 0 APT (uninit) |
| D | 0xf776...fdd1 | 0 APT (uninit) |
| E | 0xdc1d...8d36 | 0 APT (uninit) |
| F | 0x18a1...cf71 | 0 APT (uninit) |
| G | 0x69a3...7f32 | 0 APT (uninit) |
| H | 0xce67...300f | 0 APT (uninit) |
| I | 0x070f...1fc9 | 0 APT (uninit) |
| J | 0x4d96...7f54 | 0 APT (uninit) |
| K | 0xa732...5dc4 | 0 APT (uninit) |
| L | 0x7c2e...eba9 | 0 APT (uninit) |
| M | 0x6fed...7f2e9 | 0 APT (uninit) |
| N | 0xe7dd...51b2c | 0 APT (uninit) |
| O | 0x7325...a89d | 0 APT (uninit) |
| P | 0x6218...c948 | 0 APT (uninit) |
| Q | 0xac40...c89a9 | 0 APT (uninit) |
| R | 0x7ce6...6e10 | 0 APT (uninit) |
| S | 0xb875...0386 | 0 APT (uninit) |
| T | 0x3578...f588 | 0 APT (uninit) |
| U | 0x7586...f9956 | 0 APT (uninit) |
| V | 0xb59d...f2c3 | 0 APT (uninit) |
| W | 0x5f32...c7b0 | 0 APT (uninit) |
| X | 0xa95c...047d | 0 APT (uninit) |
| Y | 0xd8e3...444c4 | 0 APT (uninit) |
| Z | 0x7af0...197c | 0 APT (uninit) |

### Multisig Contract Probes — All 5 Healthy ✓

Probed via `POST /v1/view` with `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✓ HEALTHY |

All multisig contracts operational — 2-of-2 threshold confirmed.

### MNX Testnet Markets

Probed `https://testnet.mnx.fi/api/markets`, `/api/v1/markets`, `/api/tickers`.  
**Result:** HTTP 401 Unauthorized — authentication required, no public market data accessible.

---

## DuckDB Cumulative State (all sweeps)

| Table | Row Count | Notes |
|-------|-----------|-------|
| world_increments | 454 | This sweep's GF3-tagged increment log |
| repo_snapshots | historical | Cumulative across all sweeps |
| aptos_snapshots | 28 | This sweep's wallet probes |
| multisig_probes | 5 | All healthy 2/2 |
| mnx_snapshots | 0 | Unavailable (auth required) |

## GF(3) Assignment Rule
- `id % 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id % 3 == 1` → trit=+1, color=#b8bb26, name=PLUS  
- `id % 3 == 2` → trit=-1, color=#cc241d, name=MINUS
