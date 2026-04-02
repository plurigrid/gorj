# World-Increment Sweep + Hamming Snapshot

**Date/Time:** 2026-04-02T02:30:00Z (UTC)
**Sweep ID:** world-increment/sweep-2026-04-02
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## GitHub Social Graph Sweep

### Sources Queried

| Type | Name | Repos Found |
|------|------|-------------|
| org  | plurigrid | 100 |
| org  | kubeflow | 46 |
| org  | TeglonLabs | 53 |
| user | bmorphism | 100 |
| user | zubyul | 23 |
| user | migalkin | 30 |
| user | DJedamski | 11 |
| user | wasita | 29 |
| user | kristinezheng | 18 |
| user | M1shaaa | 0 (rate limited) |
| user | AustinCStone | 43 |
| **TOTAL** | | **453** |

Events captured: bmorphism (30), zubyul (30)

### GF(3) Color Chain for Increment IDs

| id % 3 | Trit | Name | Color |
|--------|------|------|-------|
| 0 | 0 | ERGODIC | #d3869b |
| 1 | +1 | PLUS | #b8bb26 |
| 2 | -1 | MINUS | #cc241d |

### Top 15 Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15549 | — |
| kubeflow/pipelines | 4118 | Python |
| kubeflow/spark-operator | 3110 | Python |
| kubeflow/trainer | 2070 | Go |
| kubeflow/katib | 1674 | Python |
| kubeflow/examples | 1459 | Jsonnet |
| kubeflow/manifests | 1006 | YAML |
| kubeflow/arena | 809 | Go |
| kubeflow/kale | 681 | Python |
| kubeflow/mpi-operator | 519 | Go |
| kubeflow/fairing | 337 | Jsonnet |
| kubeflow/pytorch-operator | 309 | Jsonnet |
| kubeflow/community | 192 | Jsonnet |
| kubeflow/website | 183 | HTML |
| kubeflow/kfctl | 183 | Go |

---

## Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 addresses queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
All returned `resource_not_found` — accounts are unfunded or use a different token interface.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...e9d7a | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...cfdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...3cf71 | 0.0 |
| G | 0x69a3...c7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...25dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...7f2e9 | 0.0 |
| N | 0xe7dd...51b2c | 0.0 |
| O | 0x7325...5a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...9956 | 0.0 |
| V | 0xb59d...af2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...444c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

### Multisig Contract Probes

All 5 probes used `0x1::multisig_account::num_signatures_required`. All healthy.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

### MNX Markets Status

**Status: API Unavailable**

Endpoints attempted:
- `https://testnet.mnx.fi/api/markets` — returns HTML (Next.js SPA)
- `https://testnet.mnx.fi/api/tickers` — returns HTML
- `https://mnx.fi/api/v1/markets` — returns HTML

MNX (The AI Exchange) does not expose a public REST market data API.

---

## DuckDB Schema

Tables created:
- `world_increments` — 11 rows (one per source, GF3 color chain applied)
- `repo_snapshots` — 453 rows
- `aptos_snapshots` — 28 rows
- `multisig_probes` — 5 rows
- `mnx_snapshots` — 1 row (status note)

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
