# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-21

## Sweep Metadata
- **Date:** 2026-07-21
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Repos Snapshotted (this run) | 394 |
| World Increments (cumulative) | 417 |
| Repo Snapshots (cumulative) | 1338 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain Distribution (this run, 394 new records)

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 138 |
| +1 | PLUS | `#b8bb26` | 140 |
| -1 | MINUS | `#cc241d` | 139 |

GF(3) rule: `id%3==0→ERGODIC, id%3==1→PLUS, id%3==2→MINUS`

---

## Top Repos by Source (2026-07-21 snapshot)

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 31 | 2026-07-10 |
| place | TeX | 1 | 2026-07-14 |
| gorj | Clojure | 1 | 2026-07-21 |
| eirobri | Clojure | 0 | 2026-07-21 |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15786 | 2026-07-10 |
| pipelines | Python | 4169 | 2026-07-21 |
| spark-operator | Python | 3140 | 2026-07-17 |
| trainer | Go | 2152 | 2026-07-20 |
| katib | Python | 1692 | 2026-07-20 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

### bmorphism (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| Gay.jl | Julia | 2 | 2026-07-21 |
| gay-chat | Scheme | 0 | 2026-07-14 |

### migalkin (19 repos)
| Repo | Language | Stars |
|------|----------|-------|
| StarE | Python | 89 |
| kgcourse2021 | HTML | 24 |

### AustinCStone (41 repos)
| Repo | Language | Stars |
|------|----------|-------|
| byteruckus | HTML | 0 |

---

## Repo Counts by Source (this run)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | user | 41 |
| migalkin | user | 19 |
| wasita | user | 12 |
| kristinezheng | user | 5 |
| TeglonLabs | org | 5 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| **TOTAL** | | **394** |

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
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 28 addresses)

All 28 Hamming-swarm addresses (alice, bob, A–Z) queried via Aptos fullnode.

| Wallets | Balance (APT) |
|---------|---------------|
| alice, bob, A–Z (all 28) | 0.0 each |

*Note: Zero balances indicate accounts without initialized CoinStore resources or empty APT balances.*

### Multisig Contract Probes (5 pairs)

All 5 contracts healthy — each requires **2 signatures**.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428... | 2 | ✅ |
| A-G | 0xf56c4a1c... | 2 | ✅ |
| Y-Z | 0xd3ffe181... | 2 | ✅ |
| S-T | 0x3b1c3ae9... | 2 | ✅ |
| V-W | 0x40fad7b4... | 2 | ✅ |

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — Vercel deployment protection active. Requires visitor password or bypass token. No market data extracted.

---

## Notable Highlights (2026-07-21)
- **kubeflow/kubeflow**: 15,786 stars (+221 vs Apr sweep) — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,169 stars — most popular ML pipeline (pushed today)
- **kubeflow/spark-operator**: 3,140 stars — Kubernetes operator for Apache Spark
- **plurigrid/gorj**: pushed today — this very repo (Clojure/forj)
- **plurigrid/eirobri**: pushed today — new active Clojure repo
- **TeglonLabs/jank-crane**: new repo (C++) — GF3 convergence maps + loopify pass spec
- **bmorphism/Gay.jl**: Julia, pushed today — most recently active bmorphism repo
- **All 5 Hamming multisigs**: 2-of-N threshold, all responding on mainnet
- **28 Hamming wallets**: queried, all showing 0 APT (no CoinStore or empty)
