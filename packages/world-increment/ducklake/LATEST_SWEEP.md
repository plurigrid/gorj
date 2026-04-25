# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-04-25  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) chain:** ERGODIC=#d3869b (trit=0) · PLUS=#b8bb26 (trit=1) · MINUS=#cc241d (trit=-1)

---

## JOB 1 — GitHub Social Graph Sweep

### Sources Crawled

| Source | Type | Repos | Max Stars | Total Stars |
|--------|------|------:|----------:|------------:|
| kubeflow | org | 47 | 15,600 | 33,940 |
| migalkin | user | 19 | 143 | 278 |
| bmorphism | user | 100 | 60 | 246 |
| AustinCStone | user | 40 | 92 | 108 |
| plurigrid | org | 100 | 17 | 65 |
| zubyul | user | 49 | 2 | 14 |
| wasita | user | 10 | 2 | 4 |
| DJedamski | user | 6 | 1 | 3 |
| TeglonLabs | org | 4 | 2 | 2 |
| M1shaaa | user | 8 | 0 | 0 |
| kristinezheng | user | 6 | 0 | 0 |
| **TOTAL** | | **389** | | **34,660** |

### Top 10 Repos by Stars

| Repo | Stars | Language |
|------|------:|----------|
| kubeflow/kubeflow | 15,600 | — |
| kubeflow/pipelines | 4,125 | Python |
| kubeflow/spark-operator | 3,120 | Python |
| kubeflow/trainer | 2,092 | Go |
| kubeflow/katib | 1,679 | Python |
| kubeflow/examples | 1,460 | Jsonnet |
| kubeflow/manifests | 1,012 | YAML |
| kubeflow/arena | 810 | Go |
| kubeflow/kale | 685 | Python |
| kubeflow/mpi-operator | 524 | Go |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|------:|
| 0 | #d3869b | ERGODIC | 129 |
| +1 | #b8bb26 | PLUS | 130 |
| -1 | #cc241d | MINUS | 130 |

World-increment IDs 1–389 across the full social graph.

### Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)
repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)
```

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried via `0x1::coin::balance` view function at ledger version ~5,000,313,xxx.

| World | APT Balance | Address (truncated) |
|-------|------------:|---------------------|
| bob | 12.657007 | 0x0a3c…512d |
| F | 1.960516 | 0x18a1…cf71 |
| L | 1.927269 | 0x7c2e…eba9 |
| J | 1.895093 | 0x4d96…7f54 |
| alice | 0.436434 | 0xc793…cc7b |
| O | 0.210136 | 0x7325…a89d |
| K | 0.161961 | 0xa732…5dc4 |
| P | 0.140136 | 0x6218…c948 |
| M | 0.112285 | 0x6fed…f2e9 |
| N | 0.106121 | 0xe7dd…1b2c |
| Q | 0.103240 | 0xac40…89a9 |
| S | 0.091788 | 0xb875…0386 |
| R | 0.090217 | 0x7ce6…6e10 |
| T | 0.073713 | 0x3578…4588 |
| U | 0.055773 | 0x7586…9956 |
| A | 0.051767 | 0x8699…cc7b |
| V | 0.048833 | 0xb59d…f2c3 |
| Y | 0.044449 | 0xd8e3…44c4 |
| X | 0.042577 | 0xa95c…047d |
| W | 0.040705 | 0x5f32…c7b0 |
| B | 0.036256 | 0x3f89…cb13 |
| Z | 0.024268 | 0x7af0…197c |
| D | 0.011629 | 0xf776…fdd1 |
| C | 0.010185 | 0x38b9…535e |
| E | 0.009372 | 0xdc1d…8d36 |
| H | 0.001681 | 0xce67…300f |
| I | 0.000681 | 0x070f…1fc9 |
| G | 0.000681 | 0x69a3…7f32 |

**Total swarm APT:** ~20.39 APT across 28 wallets

### Multisig Contract Probes

All 5 pairs probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|:-------------:|:-------:|
| A-B | 0x0da4…7003 | 2 | ✓ |
| A-G | 0xf56c…0096 | 2 | ✓ |
| Y-Z | 0xd3ff…b883 | 2 | ✓ |
| S-T | 0x3b1c…7883 | 2 | ✓ |
| V-W | 0x40fa…eb6d | 2 | ✓ |

All multisig contracts are healthy 2-of-2 configurations.

### MNX Markets (testnet.mnx.fi)

Status: **UNAVAILABLE** — `testnet.mnx.fi` is a Next.js SPA. Both `/api/markets` and `/api/v1/markets` return the SPA HTML shell, not JSON. No REST market data accessible server-side.

---

## DuckDB Summary

```
world-increments.duckdb
├── world_increments    389 rows  (GF3 color chain across all repo events)
├── repo_snapshots      389 rows  (full GitHub repo metadata)
├── aptos_snapshots      28 rows  (Hamming swarm wallet balances)
├── multisig_probes       5 rows  (all healthy, 2-of-2)
└── mnx_snapshots         1 row   (unavailable marker)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
