# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-24

## Sweep Metadata
- **Date:** 2026-07-24
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (2026-07-24 Run)

| Metric | Value |
|--------|-------|
| Total World Increments (today) | 65 |
| Total Repo Snapshots (today) | 65 |
| Cumulative World Increments | 88 |
| Cumulative Repo Snapshots | 1,009 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain Distribution (Today)

| Color | Name | Trit | Count |
|-------|------|------|-------|
| `#b8bb26` | PLUS | +1 | 22 |
| `#cc241d` | MINUS | -1 | 22 |
| `#d3869b` | ERGODIC | 0 | 21 |

GF(3) assignment: `id mod 3 == 0 → ERGODIC`, `id mod 3 == 1 → PLUS`, `id mod 3 == 2 → MINUS`

---

## Top Repos by Stars (Today's Snapshot)

| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,789 | — | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4,169 | Python | Machine Learning Pipelines for Kubeflow |
| kubeflow/spark-operator | 3,143 | Python | Kubernetes operator for Apache Spark |
| kubeflow/trainer | 2,153 | Go | Distributed AI Model Training on Kubernetes |
| kubeflow/katib | 1,692 | Python | Automated Machine Learning on Kubernetes |
| kubeflow/examples | 1,461 | Jsonnet | Extended examples and tutorials |
| kubeflow/community-distribution | 1,029 | YAML | Kubeflow Community Distribution |
| kubeflow/arena | 815 | Go | A CLI for Kubeflow |
| kubeflow/kale | 695 | Python | Kubeflow superfood for Data Scientists |
| migalkin/NodePiece | 144 | Python | Parameter-Efficient KG Representations (ICLR'22) |

---

## Repo Counts by Source (Today)

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 14 |
| kubeflow | org | 12 |
| bmorphism | user | 10 |
| zubyul | user | 7 |
| TeglonLabs | org | 5 |
| migalkin | social graph | 4 |
| wasita | social graph | 4 |
| AustinCStone | social graph | 3 |
| M1shaaa | social graph | 2 |
| DJedamski | social graph | 2 |
| kristinezheng | social graph | 2 |
| **TOTAL** | | **65** |

---

## Notable Active Repos (Recent Pushes 2026-07)

- **plurigrid/gorj** – pushed 2026-07-24, 1,356 open issues — active Clojure/GF3 REPL orchestration
- **kubeflow/pipelines** – pushed 2026-07-24, 445 open issues — ML pipelines very active
- **kubeflow/trainer** – pushed 2026-07-24 — distributed LLM fine-tuning on K8s
- **bmorphism/Gay.jl** – pushed 2026-07-24, 187 open issues — wide-gamut GF3 color core
- **zubyul/from-possible-worlds** – pushed 2026-07-18 — TeX
- **plurigrid/eirobri** – pushed 2026-07-21, 31 open issues — EiRoBri replay world (Clojure)
- **wasita/wasita.github.io** – pushed 2026-07-21 — Svelte personal site, active
- **TeglonLabs/jank-crane** – pushed 2026-06-08 — C++ GF3 convergence maps / jank IR

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 28 wallets)

All 28 wallets (alice, bob, A–Z) returned **0 APT**. The `CoinStore<AptosCoin>` resource was not found for these addresses on mainnet — wallets are either unfunded or have not been initialized.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z (26) | various | 0.0 each |

### Multisig Contract Probes (Aptos Mainnet)

All 5 multisig contracts are **healthy** and each requires **2 signatures**.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ healthy |
| A-G | 0xf56c...0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✅ healthy |
| S-T | 0x3b1c...7883 | 2 | ✅ healthy |
| V-W | 0x40fa...eb6d | 2 | ✅ healthy |

### MNX Markets (testnet.mnx.fi)

testnet.mnx.fi is a Next.js SPA (62KB HTML loaded). No REST API endpoints returned structured data (`/api/markets`, `/api/v1/markets`, `/api/ticker` all returned the SPA shell). Market data loads client-side via JavaScript bundles. **Status: unavailable via static fetch.**

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
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS

## Previous Sweeps
- **2026-04-10**: 471 repo snapshots
- **2026-04-14**: 473 repo snapshots
- **2026-07-24** (this run): 65 repo snapshots + Aptos hamming snapshot
