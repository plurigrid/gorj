# LATEST_SWEEP.md

**Sweep Date/Time:** 2026-04-04T00:00:00Z (automated sweep)

---

## GitHub Repos Collected

**Total: 205 repos across 11 sources**

| Source | Type | Count |
|--------|------|-------|
| plurigrid | org | 20 |
| kubeflow | org | 20 |
| TeglonLabs | org | 20 |
| bmorphism | user | 20 |
| zubyul | user | 20 |
| migalkin | user | 20 |
| DJedamski | user | 11 |
| wasita | user | 20 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| AustinCStone | user | 20 |

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15551 | - |
| kubeflow/pipelines | 4117 | Python |
| kubeflow/spark-operator | 3109 | Python |
| kubeflow/trainer | 2074 | Go |
| kubeflow/katib | 1674 | Python |
| kubeflow/manifests | 1007 | YAML |
| kubeflow/arena | 809 | Go |
| kubeflow/kale | 682 | Python |
| kubeflow/mpi-operator | 519 | Go |
| migalkin/NodePiece | 143 | Python |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml |

---

## GF(3) Color Chain Summary

IDs are assigned sequentially. The GF(3) trit pattern cycles every 3:

| id % 3 | Trit | Color | Name |
|--------|------|-------|------|
| 0 | 0 | #d3869b | ERGODIC |
| 1 | 1 | #b8bb26 | PLUS |
| 2 | -1 | #cc241d | MINUS |

205 world_increments inserted covering all 11 org/user sources.

---

## Aptos Wallet Balances

All queried against `fullnode.mainnet.aptoslabs.com`. All wallets returned 0 APT (accounts not funded or not initialized on mainnet).

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.00000000 |
| bob | 0x0a3c...2d5d | 0.00000000 |
| A | 0x8699...9d7a | 0.00000000 |
| B | 0x3f89...b13 | 0.00000000 |
| C | 0x38b9...535e | 0.00000000 |
| D | 0xf776...fdd1 | 0.00000000 |
| E | 0xdc1d...8d36 | 0.00000000 |
| F | 0x18a1...cf71 | 0.00000000 |
| G | 0x69a3...7f32 | 0.00000000 |
| H | 0xce67...300f | 0.00000000 |
| I | 0x070f...1fc9 | 0.00000000 |
| J | 0x4d96...7f54 | 0.00000000 |
| K | 0xa732...5dc4 | 0.00000000 |
| L | 0x7c2e...eba9 | 0.00000000 |
| M | 0x6fed...f2e9 | 0.00000000 |
| N | 0xe7dd...1b2c | 0.00000000 |
| O | 0x7325...a89d | 0.00000000 |
| P | 0x6218...c948 | 0.00000000 |
| Q | 0xac40...89a9 | 0.00000000 |
| R | 0x7ce6...6e10 | 0.00000000 |
| S | 0xb875...0386 | 0.00000000 |
| T | 0x3578...4588 | 0.00000000 |
| U | 0x7586...9956 | 0.00000000 |
| V | 0xb59d...f2c3 | 0.00000000 |
| W | 0x5f32...c7b0 | 0.00000000 |
| X | 0xa95c...047d | 0.00000000 |
| Y | 0xd8e3...44c4 | 0.00000000 |
| Z | 0x7af0...197c | 0.00000000 |

**Total APT across all wallets: 0.00000000 APT**

---

## Multisig Probe Results

All probes queried via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

All 5 multisig contracts are healthy, each requiring 2-of-N signatures.

---

## MNX Markets

Status: **unavailable** (API endpoints return HTML frontend, not JSON data)

- `https://testnet.mnx.fi/api/markets` - HTML (Next.js SPA, no JSON API exposed)
- `https://testnet.mnx.fi/api/v1/markets` - HTML

No mnx_snapshots inserted.

---

## DuckDB Database

Location: `/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb`

Tables populated:
- `world_increments`: 205 rows
- `repo_snapshots`: 205 rows
- `aptos_snapshots`: 28 rows
- `multisig_probes`: 5 rows
- `mnx_snapshots`: 0 rows (unavailable)
