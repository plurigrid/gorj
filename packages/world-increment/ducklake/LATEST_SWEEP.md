# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-06-05
**GF(3) chain:** id%3==0 → trit=0 ERGODIC #d3869b | id%3==1 → trit=1 PLUS #b8bb26 | id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Covered

| # | Source | Type | GF(3) | Repos Snapshotted |
|---|--------|------|-------|-------------------|
| 1 | plurigrid | org | PLUS #b8bb26 | 100 |
| 2 | kubeflow | org | MINUS #cc241d | 48 |
| 3 | TeglonLabs | org | ERGODIC #d3869b | 4 |
| 4 | bmorphism | user | PLUS #b8bb26 | 30 (sample) |
| 5 | zubyul | user | MINUS #cc241d | 20 (sample) |
| 6 | migalkin | user (social) | ERGODIC #d3869b | 19 |
| 7 | DJedamski | user (social) | PLUS #b8bb26 | 6 |
| 8 | wasita | user (social) | MINUS #cc241d | 11 |
| 9 | kristinezheng | user (social) | ERGODIC #d3869b | 5 |
| 10 | M1shaaa | user (social) | PLUS #b8bb26 | 8 |
| 11 | AustinCStone | user (social) | MINUS #cc241d | 20 (sample) |

**Total repo snapshots stored in DuckDB:** 271

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,706 | — | 2026-05-24 |
| kubeflow/pipelines | 4,152 | Python | 2026-06-05 |
| kubeflow/spark-operator | 3,125 | Python | 2026-06-04 |
| kubeflow/trainer | 2,111 | Go | 2026-06-05 |
| kubeflow/katib | 1,684 | Python | 2026-06-04 |
| kubeflow/examples | 1,462 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,020 | YAML | 2026-06-05 |
| kubeflow/arena | 811 | Go | 2026-05-07 |
| kubeflow/kale | 690 | Python | 2026-06-04 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |

### Notable Hot Repos (pushed within 48h of sweep)

- **plurigrid/gorj** — forj + Rama topology nREPL + GF(3) trit coloring (2026-06-05, 370 open issues)
- **plurigrid/eirobri** — EiRoBri replay world (2026-06-03, 29 open issues)
- **bmorphism/Gay.jl** — Wide-gamut color sampling with splittable determinism (2026-06-05, 189 issues)
- **kubeflow/hub** + **kubeflow/pipelines** + **kubeflow/trainer** — active MLOps (2026-06-05)
- **M1shaaa/M1shaaa** — active GitHub profile (2026-06-05)
- **wasita/wasita.github.io** — Svelte personal site (2026-06-01)

### Social Graph Notes

- **migalkin** — Knowledge Graph/GNN researcher (NodePiece 144★, StarE 89★, NBFNet MLX)
- **DJedamski** — Data scientist, mostly 2014-2018 Kaggle/Coursera archive
- **wasita** — Active Svelte dev, personal site + magic-garden Discord bot
- **kristinezheng** — MIT cognitive science researcher, Lookit experiment platform
- **M1shaaa** — Yale/MIT lab, Lookit studies, active (profile pushed 2026-06-05)
- **AustinCStone** — ML/CV, TextGAN 92★, recent Aptos/bmorphism fork work

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried 28 addresses (alice, bob, A-Z) against Aptos mainnet fullnode.
**All 28 addresses returned 0 APT** — CoinStore resource not found (wallets uninitialized or empty on mainnet).

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793...cc7b | 0.00000000 |
| bob | 0x0a3c...2d5d | 0.00000000 |
| A | 0x8699...9d7a | 0.00000000 |
| B | 0x3f89...b13 | 0.00000000 |
| C | 0x38b9...35e | 0.00000000 |
| D | 0xf776...dd1 | 0.00000000 |
| E | 0xdc1d...d36 | 0.00000000 |
| F | 0x18a1...f71 | 0.00000000 |
| G | 0x69a3...f32 | 0.00000000 |
| H | 0xce67...00f | 0.00000000 |
| I | 0x070f...fc9 | 0.00000000 |
| J | 0x4d96...f54 | 0.00000000 |
| K | 0xa732...dc4 | 0.00000000 |
| L | 0x7c2e...ba9 | 0.00000000 |
| M | 0x6fed...2e9 | 0.00000000 |
| N | 0xe7dd...b2c | 0.00000000 |
| O | 0x7325...89d | 0.00000000 |
| P | 0x6218...948 | 0.00000000 |
| Q | 0xac40...9a9 | 0.00000000 |
| R | 0x7ce6...e10 | 0.00000000 |
| S | 0xb875...386 | 0.00000000 |
| T | 0x3578...588 | 0.00000000 |
| U | 0x7586...956 | 0.00000000 |
| V | 0xb59d...2c3 | 0.00000000 |
| W | 0x5f32...7b0 | 0.00000000 |
| X | 0xa95c...47d | 0.00000000 |
| Y | 0xd8e3...44c4 | 0.00000000 |
| Z | 0x7af0...97c | 0.00000000 |

### Multisig Contract Probes

All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`. All return **2 signatures required** and are healthy.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | 2 | true |
| A-G | 0xf56c...096 | 2 | true |
| Y-Z | 0xd3ff...883 | 2 | true |
| S-T | 0x3b1c...883 | 2 | true |
| V-W | 0x40fa...6d | 2 | true |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is protected by Vercel deployment authentication. Neither `/api/markets`, `/api/v1/markets`, nor the root returned market data. `mnx_snapshots` table is empty (0 rows).

---

## DuckDB Table Summary

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 11 | GF(3) trit-colored source events |
| `repo_snapshots` | 271 | GitHub repo metadata (11 sources) |
| `aptos_snapshots` | 28 | Hamming swarm APT balances |
| `multisig_probes` | 5 | Aptos multisig 2-of-2 health checks |
| `mnx_snapshots` | 0 | MNX markets (unavailable) |

---

*Generated by world-increment-sweep + hamming-swarm-snapshot agent · 2026-06-05*
