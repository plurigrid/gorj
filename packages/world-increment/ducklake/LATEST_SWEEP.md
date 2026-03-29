# World-Increment + Hamming Swarm Snapshot

**Sweep Date/Time:** 2026-03-29 (UTC)
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repos Snapshotted Per Source

| Source | Type | Repos |
|--------|------|-------|
| bmorphism | user | 97 |
| plurigrid | org | 87 |
| kubeflow | org | 46 |
| zubyul | user | 44 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| M1shaaa | user | 8 |
| wasita | user | 9 |
| kristinezheng | user | 6 |
| DJedamski | user | 6 |
| TeglonLabs | org | 3 |
| **TOTAL** | | **365** |

> Note: gh CLI unavailable; mcp__github__ tools used for all queries.
> Social graph users (zubyul's network): migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,538 | — |
| kubeflow/pipelines | 4,113 | Python |
| kubeflow/spark-operator | 3,110 | Python |
| kubeflow/trainer | 2,068 | Go |
| kubeflow/katib | 1,672 | Python |
| kubeflow/examples | 1,459 | Jsonnet |
| kubeflow/manifests | 1,005 | YAML |
| kubeflow/arena | 810 | Go |
| kubeflow/kale | 681 | Python |
| kubeflow/mpi-operator | 519 | Go |

### GF(3) Color Chain Summary

Each repo snapshot assigned a GF(3) trit based on `id % 3`:

| GF3 Name | Color | Trit | Count |
|----------|-------|------|-------|
| ERGODIC | #d3869b | 0 | 121 |
| PLUS | #b8bb26 | 1 | 122 |
| MINUS | #cc241d | -1 | 122 |

- `id%3==0` → trit=0, ERGODIC (#d3869b — rose/pink)
- `id%3==1` → trit=1, PLUS (#b8bb26 — yellow-green)
- `id%3==2` → trit=-1, MINUS (#cc241d — red)

Chain repeats: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ...`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All queried via `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
All 28 addresses returned `resource_not_found` — no APT CoinStore resource initialized.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...9956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

### Multisig Probe Results

All probed via `POST https://fullnode.mainnet.aptoslabs.com/v1/view` with `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

All 5 multisig accounts are healthy with 2-of-N signatures required.

### MNX Markets Status

- `https://testnet.mnx.fi/api/markets` — returned Next.js HTML (no JSON API)
- `https://testnet.mnx.fi/api/v1/markets` — returned Next.js HTML (no JSON API)
- `https://testnet.mnx.fi` — SPA frontend, no parseable market data

**Status: MNX testnet market API unavailable.** The endpoint returns a Next.js frontend application instead of JSON. Zero rows inserted into `mnx_snapshots`.

---

## DuckDB Row Counts (All Tables)

| Table | Rows |
|-------|------|
| world_increments | 377 |
| repo_snapshots | 405 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

> Core sweep stats: 365 world_increment rows (source_type='repo_snapshot'), 365 repo_snapshot rows from this run, 28 aptos balance rows, 5 multisig probe rows.

---

## GF(3) Assignment Rule

| `id % 3` | trit | color | name |
|----------|------|-------|------|
| 0 | 0 | #d3869b | ERGODIC |
| 1 | +1 | #b8bb26 | PLUS |
| 2 | -1 | #cc241d | MINUS |

## Notable Highlights

- **kubeflow/kubeflow**: 15,538 stars — umbrella ML platform for Kubernetes
- **kubeflow/pipelines**: 4,113 stars — ML pipelines with full DAG support
- **plurigrid** org: 87 repos — topological computing, ASI, gorj, lolita and more
- **bmorphism**: 97 repos — most prolific user in the sweep
- **TeglonLabs/mathpix-gem**: mathpix Ruby gem (recently active 2026-01-01)
- **wasita**: cognitive science / Svelte developer (CV updated 2026-03-26)
- **M1shaaa/M1shaaa**: profile repo pushed 2026-03-29 (day of sweep)
- All 5 Aptos multisig pairs confirm 2-of-N threshold — Hamming swarm structurally intact
