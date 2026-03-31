# World Increment Sweep + Hamming Swarm Snapshot

**Date/Time:** 2026-03-31T03:23 UTC
**DuckDB:** v1.5.1 (Variegata)
**GF3 Color Chain:** id%3==0 → trit=0 "ERGODIC" #d3869b | id%3==1 → trit=1 "PLUS" #b8bb26 | id%3==2 → trit=-1 "MINUS" #cc241d

---

## GitHub Repos Snapshot

### Summary by Source (306 repos captured, 4 sources rate-limited)

| Source | Type | Repo Count | Status |
|--------|------|-----------|--------|
| plurigrid | org | 100 | OK |
| TeglonLabs | org | 53 | OK |
| kubeflow | org | 46 | OK |
| AustinCStone | user | 43 | OK |
| migalkin | user | 30 | OK |
| kristinezheng | user | 18 | OK |
| M1shaaa | user | 16 | OK |
| bmorphism | user | 0 | RATE_LIMITED |
| zubyul | user | 0 | RATE_LIMITED |
| DJedamski | user | 0 | RATE_LIMITED |
| wasita | user | 0 | RATE_LIMITED |

**Note:** bmorphism, zubyul, DJedamski, wasita hit GitHub unauthenticated API rate limit (60 req/hr). Public events also unavailable due to rate limiting.

### Top 20 Repos by Stars

| Org/User | Repo | Stars | Language |
|----------|------|-------|----------|
| kubeflow | kubeflow | 15547 | — |
| kubeflow | pipelines | 4114 | Python |
| kubeflow | spark-operator | 3110 | Python |
| kubeflow | trainer | 2070 | Go |
| kubeflow | katib | 1673 | Python |
| kubeflow | examples | 1459 | Jsonnet |
| kubeflow | manifests | 1006 | YAML |
| kubeflow | arena | 810 | Go |
| kubeflow | kale | 681 | Python |
| kubeflow | mpi-operator | 519 | Go |
| kubeflow | fairing | 337 | Jsonnet |
| kubeflow | pytorch-operator | 309 | Jsonnet |
| kubeflow | community | 191 | Jsonnet |
| kubeflow | website | 183 | HTML |
| kubeflow | kfctl | 183 | Go |
| kubeflow | kfp-tekton | 182 | TypeScript |
| kubeflow | example-seldon | 172 | Jupyter Notebook |
| kubeflow | model-registry | 170 | Go |
| kubeflow | mcp-apache-spark-history-server | 147 | Python |
| migalkin | NodePiece | 143 | Python |

---

## Aptos Wallet Balances (Mainnet)

Queried via `0x1::coin::balance` view function on `fullnode.mainnet.aptoslabs.com`.

| World | Address (truncated) | Balance (APT) |
|-------|--------------------|--------------:|
| alice | 0xc793...4cc7b | 0.43643352 |
| bob | 0x0a3c...512d5d | 12.657007 |
| A | 0x8699...be9d7a | 0.051767 |
| B | 0x3f89...cb13 | 0.036256 |
| C | 0x38b9...535e | 0.010185 |
| D | 0xf776...cfdd1 | 0.011629 |
| E | 0xdc1d...8d36 | 0.012561 |
| F | 0x18a1...cf71 | 1.960516 |
| G | 0x69a3...7f32 | 0.000681 |
| H | 0xce67...300f | 0.000681 |
| I | 0x070f...1fc9 | 0.000681 |
| J | 0x4d96...7f54 | 1.895093 |
| K | 0xa732...25dc4 | 0.161961 |
| L | 0x7c2e...eba9 | 1.927269 |
| M | 0x6fed...7f2e9 | 0.112285 |
| N | 0xe7dd...51b2c | 0.106121 |
| O | 0x7325...a89d | 0.210136 |
| P | 0x6218...ec948 | 0.140136 |
| Q | 0xac40...c89a9 | 0.10324 |
| R | 0x7ce6...76e10 | 0.090217 |
| S | 0xb875...d0386 | 0.091788 |
| T | 0x3578...f4588 | 0.073713 |
| U | 0x7586...f9956 | 0.055773 |
| V | 0xb59d...af2c3 | 0.04783299 |
| W | 0x5f32...7b0 | 0.040705 |
| X | 0xa95c...3047d | 0.042577 |
| Y | 0xd8e3...444c4 | 0.044449 |
| Z | 0x7af0...197c | 0.023268 |

**Total APT across all wallets:** ~20.38 APT
**Largest holder:** bob (12.657 APT)
**Notable balances:** F (1.96 APT), L (1.93 APT), J (1.90 APT)

---

## Multisig Contract Probes (Aptos Mainnet)

Queried via `0x1::multisig_account::num_signatures_required` view function.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|--------------------|--------------:|---------|
| A-B | 0x0da4...7003 | 2 | YES |
| A-G | 0xf56c...0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

All 5 multisig contracts are healthy with 2-of-N signature requirements.

---

## MNX Markets

**Status: UNAVAILABLE**

Endpoints probed:
- `https://testnet.mnx.fi/api/markets` → 404
- `https://api.testnet.mnx.fi/markets` → Cannot GET
- `https://api.testnet.mnx.fi/v1/markets` → Cannot GET
- `https://api.testnet.mnx.fi/spot/markets` → Cannot GET
- `https://api.testnet.mnx.fi/perp/markets` → Cannot GET
- `https://mnx.fi/api/markets` → 404

MNX testnet API is not publicly accessible at this time.

---

## DuckDB Database

Location: `packages/world-increment/ducklake/world-increments.duckdb`

Tables:
- `world_increments` — GF3 color chain increments (319 rows)
- `repo_snapshots` — GitHub repo snapshots (306 rows)
- `aptos_snapshots` — Aptos wallet balances (28 rows)
- `multisig_probes` — Multisig contract probes (5 rows)
- `mnx_snapshots` — MNX markets (1 row, unavailable marker)
