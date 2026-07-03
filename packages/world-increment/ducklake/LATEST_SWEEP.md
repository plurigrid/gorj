# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-03

## Sweep Metadata
- **Date:** 2026-07-03
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (via Python duckdb package)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 414 |
| Total Repo Snapshots | 1,335 (646 distinct repos) |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Queried | 28 |
| Multisig Probes | 5 (all healthy) |
| MNX Markets | UNAVAILABLE (Vercel auth) |

---

## GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 137 |
| +1 | PLUS | `#b8bb26` | 139 |
| -1 | MINUS | `#cc241d` | 138 |

**GF(3) Rule:** `id mod 3 == 0` → ERGODIC, `id mod 3 == 1` → PLUS, `id mod 3 == 2` → MINUS

---

## Top Repos by Source

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 28 | 2026-06-29 |
| place | TeX | 1 | 2026-06-29 |
| eirobri | Clojure | 0 | 2026-06-30 |
| gorj | Clojure | 0 | 2026-07-03 |
| shrimp | — | 0 | 2026-07-03 |

### kubeflow (48 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,760 | 2026-06-18 |
| pipelines | Python | 4,168 | 2026-07-03 |
| spark-operator | Python | 3,132 | 2026-07-02 |
| trainer | Go | 2,129 | 2026-07-02 |
| hub | Go | 174 | 2026-07-03 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

### bmorphism (100 repos, up from 100)
Most recently pushed repo: checked 2026-07-03

### Social Graph Highlights
| User | Notable Repos |
|------|--------------|
| migalkin | NodePiece (KG embeddings), StarE |
| AustinCStone | TextGAN, StereoVisionMRF |
| wasita | wasita.github.io (personal site, pushed 2026-07-02) |
| kristinezheng | kristinezheng.github.io (pushed 2026-07-01) |
| M1shaaa | M1shaaa profile repo (pushed 2026-07-03) |

---

## Repo Counts by Source (This Sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 100 |
| kubeflow | org | 48 |
| AustinCStone | user | ~50 |
| migalkin | user | ~30 |
| wasita | user | 11 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| TeglonLabs | org | 5 |
| **DISTINCT TOTAL** | | **646** |

---

## JOB 2: Hamming Swarm — Aptos Snapshot

### Wallet Balances (Mainnet, 2026-07-03)

All 28 wallets (alice, bob, A–Z) returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
These accounts are not initialized with an APT CoinStore on mainnet. **Recorded as 0.0 APT each.**

### Multisig Contract Probes — ALL HEALTHY ✅

| Pair | Address | Sigs Required |
|------|---------|--------------|
| A-B | `0x0da4f428...87003` | 2 |
| A-G | `0xf56c4a1c...0096` | 2 |
| Y-Z | `0xd3ffe181...b883` | 2 |
| S-T | `0x3b1c3ae9...7883` | 2 |
| V-W | `0x40fad7b4...eb6d` | 2 |

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — site is behind Vercel deployment protection. API endpoints (`/api/markets`, `/api/v1/markets`) require authentication. No market data captured.

---

## Most Recently Active (as of sweep)

| Repo | Pushed At |
|------|-----------|
| plurigrid/gorj | 2026-07-03T11:11:23Z |
| kubeflow/hub | 2026-07-03T11:09:45Z |
| kubeflow/pipelines | 2026-07-03T09:34:28Z |
| kubeflow/community-distribution | 2026-07-03T09:20:06Z |
| kubeflow/dashboard | 2026-07-03T08:11:17Z |

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,760 stars — flaghsip ML platform for Kubernetes (up from 15,565 in April sweep)
- **kubeflow/pipelines**: 4,168 stars — ML pipelines (up 49 stars since April)
- **plurigrid/asi**: 28 stars — topological chemputer (up 12 stars since April)
- **plurigrid/gorj**: Pushed today (2026-07-03) — this repo
- **Hamming swarm**: All 5 multisig contracts healthy (2-of-N), all 28 wallets uninitialized on mainnet
- **MNX testnet**: Behind Vercel auth wall — market data not accessible
