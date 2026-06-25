# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-25

## Sweep Metadata
- **Date:** 2026-06-25
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 34 |
| Total Repo Snapshots (cumulative) | 1,335 |
| New Repos This Sweep | 391 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain — New Increments (This Sweep)

| ID | Source | GF3 Trit | Color | Name |
|----|--------|----------|-------|------|
| 1  | AustinCStone (user) | +1 | `#b8bb26` | **PLUS** |
| 2  | DJedamski (user) | -1 | `#cc241d` | **MINUS** |
| 3  | kubeflow (org) | 0 | `#d3869b` | **ERGODIC** |
| 4  | M1shaaa (user) | +1 | `#b8bb26` | **PLUS** |
| 5  | TeglonLabs (org) | -1 | `#cc241d` | **MINUS** |
| 6  | bmorphism (user) | 0 | `#d3869b` | **ERGODIC** |
| 7  | kristinezheng (user) | +1 | `#b8bb26` | **PLUS** |
| 8  | migalkin (user) | -1 | `#cc241d` | **MINUS** |
| 9  | plurigrid (org) | 0 | `#d3869b` | **ERGODIC** |
| 10 | wasita (user) | +1 | `#b8bb26` | **PLUS** |
| 11 | zubyul (user) | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## Top Repos by Stars (This Sweep)

| Repo | Language | Stars | Forks | Last Pushed |
|------|----------|-------|-------|-------------|
| kubeflow/kubeflow | — | ★15,744 | ⑂2,680 | 2026-06-18 |
| kubeflow/pipelines | Python | ★4,156 | ⑂2,009 | 2026-06-25 |
| kubeflow/spark-operator | Python | ★3,128 | ⑂1,492 | 2026-06-25 |
| kubeflow/trainer | Go | ★2,121 | ⑂972 | 2026-06-25 |
| kubeflow/katib | Python | ★1,685 | ⑂527 | 2026-06-23 |
| kubeflow/examples | Jsonnet | ★1,460 | ⑂756 | 2025-04-14 |
| kubeflow/community-distribution | YAML | ★1,028 | ⑂1,065 | 2026-06-25 |
| kubeflow/manifests | YAML | ★1,010 | ⑂1,069 | 2026-04-09 |
| kubeflow/kfserving | Python | ★959 | ⑂490 | 2025-11-17 |
| kubeflow/mpi-operator | Go | ★780 | ⑂355 | 2026-05-22 |

### Language Distribution
| Language | Repos | Total Stars |
|----------|-------|-------------|
| Python | 199 | 31,295 |
| Go | 45 | 11,963 |
| Jsonnet | 23 | 7,034 |
| TypeScript | 47 | 1,005 |
| Jupyter Notebook | 41 | 992 |
| HTML | 46 | 664 |
| JavaScript | 50 | 196 |
| Rust | 40 | 49 |
| Clojure | 18 | 3 |

### Most Recently Pushed
| Repo | Language | Last Pushed |
|------|----------|-------------|
| kubeflow/pipelines | Python | 2026-06-25T20:51:42 |
| kubeflow/mcp-apache-spark-history-server | Python | 2026-06-25T20:28:43 |
| plurigrid/gorj | Clojure | 2026-06-25T20:11:01 |
| kubeflow/trainer | Go | 2026-06-25T19:47:47 |
| kubeflow/spark-operator | Python | 2026-06-25T19:45:10 |

### TeglonLabs Notable
- **jank-crane** (C++) — crane-jank converged-IR hub: GF3 convergence maps, pushed 2026-06-08
- **mathpix-gem** (Ruby) — Math OCR gem, ★2, pushed 2026-01-01

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses returned **0.0 APT** — wallets are unregistered or unfunded on mainnet (no active `CoinStore<AptosCoin>` resource).

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b | 0.0 |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes — All Healthy

All 5 contracts on Aptos mainnet respond correctly, requiring **2 signatures**.

| Pair | Address | Sigs | Status |
|------|---------|------|--------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | ✅ |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | ✅ |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | ✅ |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | ✅ |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | ✅ |

### MNX Markets (testnet.mnx.fi)
**UNAVAILABLE** — Protected by Vercel deployment protection. Requires OIDC token or bypass. No market data extracted.

---

## Repo Counts by Source (This Sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| AustinCStone | user | 40 |
| kubeflow | org | 48 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| wasita | user | 11 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| TeglonLabs | org | 5 |
| **TOTAL** | | **391** |

---

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,744 stars (+179 since Apr-12 sweep) — ML platform for Kubernetes
- **kubeflow/pipelines**: 4,156 stars (+37) — pushed today 2026-06-25
- **kubeflow/spark-operator**: 3,128 stars (+17) — pushed today 2026-06-25
- **plurigrid/gorj**: Pushed today 2026-06-25T20:11 — this very repo
- **TeglonLabs/jank-crane**: NEW since last sweep — C++ GF3 convergence maps (2026-06-08)
- **Multisig health**: All 5 Hamming-pair contracts at 2-of-N, fully operational
