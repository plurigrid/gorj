# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-21 10:11 UTC

---

## JOB 1 — GitHub Social Graph Sweep

### Sources Covered

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 45 |
| kubeflow | org | 20 |
| TeglonLabs | org | 5 |
| bmorphism | user | 18 |
| zubyul | user | 7 |
| migalkin | social | 6 |
| DJedamski | social | 4 |
| wasita | social | 5 |
| kristinezheng | social | 3 |
| M1shaaa | social | 3 |
| AustinCStone | social | 5 |
| **Total** | | **121** |

### GF(3) Color Chain Distribution

- **ERGODIC** (#d3869b, trit=0): ids where id%3==0 — ~40 repos
- **PLUS** (#b8bb26, trit=1): ids where id%3==1 — ~41 repos
- **MINUS** (#cc241d, trit=-1): ids where id%3==2 — ~40 repos

### Notable Repos by Activity (pushed_at ≤ 24h)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| plurigrid/gorj | 0 | Clojure | 2026-06-21 |
| kubeflow/dashboard | 16 | TypeScript | 2026-06-21 |
| kubeflow/katib | 1683 | Python | 2026-06-20 |
| kubeflow/pipelines | 4155 | Python | 2026-06-20 |
| bmorphism/Gay.jl | 2 | Julia | 2026-06-21 |

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,738 | — |
| kubeflow/pipelines | 4,155 | Python |
| kubeflow/spark-operator | 3,127 | Python |
| kubeflow/trainer | 2,118 | Go |
| kubeflow/katib | 1,683 | Python |
| kubeflow/examples | 1,460 | Jsonnet |
| kubeflow/community-distribution | 1,026 | YAML |
| kubeflow/arena | 813 | Go |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/NodePiece | 144 | Python |

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

| World | Balance (APT) | Address (truncated) |
|-------|--------------|---------------------|
| alice | 0.43643352 | ...alic |
| bob | 12.65700700 | ...bob |
| A | 0.05176700 | ...a |
| B | 0.03625600 | ...b |
| C | 0.01018500 | ...c |
| D | 0.01162900 | ...d |
| E | 0.00937200 | ...e |
| F | 1.96051600 | ...f |
| G | 0.00068100 | ...g |
| H | 0.00168100 | ...h |
| I | 0.00068100 | ...i |
| J | 1.89509300 | ...j |
| K | 0.16196100 | ...k |
| L | 1.92726900 | ...l |
| M | 0.11228500 | ...m |
| N | 0.10612100 | ...n |
| O | 0.21013600 | ...o |
| P | 0.14013600 | ...p |
| Q | 0.10324000 | ...q |
| R | 0.09021700 | ...r |
| S | 0.09178800 | ...s |
| T | 0.07371300 | ...t |
| U | 0.05577300 | ...u |
| V | 0.04883299 | ...v |
| W | 0.04070500 | ...w |
| X | 0.04257700 | ...x |
| Y | 0.04444900 | ...y |
| Z | 0.02426800 | ...z |

**Total APT across all worlds:** 20.34477251 APT

### Multisig Probes (Mainnet)

| Pair | Sigs Required | Healthy |
|------|--------------|---------|
| A-B | 2 | ✅ |
| A-G | 2 | ✅ |
| Y-Z | 2 | ✅ |
| S-T | 2 | ✅ |
| V-W | 2 | ✅ |

All 5/5 multisig contracts healthy — 2-of-2 threshold on each pair.

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — testnet.mnx.fi serves an SPA with no accessible JSON API at standard endpoints (`/api/markets`, `/api/v1/markets`, `/markets`, `/api/tokens`). Recorded as `N/A` in `mnx_snapshots` table.

---

## DuckDB Tables

- `world_increments` — 121 rows (GF3 trit-colored repo push events)
- `repo_snapshots` — 121 rows (full repo metadata)
- `aptos_snapshots` — 28 rows (Hamming swarm balances, coin::balance view fn)
- `multisig_probes` — 5 rows (A-B, A-G, Y-Z, S-T, V-W; all healthy)
- `mnx_snapshots` — 1 row (unavailable marker)

**Database:** `packages/world-increment/ducklake/world-increments.duckdb`
