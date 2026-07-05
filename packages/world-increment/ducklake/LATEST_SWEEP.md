# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-05

## Sweep Metadata
- **Date:** 2026-07-05
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 342 |
| Total Repo Snapshots | 1,263 |
| Sources Covered | 3 orgs + 8 users |
| GF(3) ERGODIC (#d3869b) | 113 |
| GF(3) PLUS (#b8bb26) | 115 |
| GF(3) MINUS (#cc241d) | 114 |

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social (zubyul) | 19 |
| wasita | social (zubyul) | 11 |
| AustinCStone | social (zubyul) | 40 |
| DJedamski | social (zubyul) | 6 |
| kristinezheng | social (zubyul) | 5 |
| M1shaaa | social (zubyul) | 8 |

### Top Repos by Stars

| Repo | Language | ★ Stars | 🍴 Forks | Pushed At |
|------|----------|---------|---------|-----------|
| kubeflow/kubeflow | — | 15,761 | 2,683 | 2026-07-05 |
| kubeflow/pipelines | Python | 4,169 | 2,023 | 2026-07-05 |
| kubeflow/spark-operator | Python | 3,132 | 1,496 | 2026-07-05 |
| kubeflow/trainer | Go | 2,129 | 978 | 2026-07-05 |
| kubeflow/katib | Python | 1,689 | 530 | 2026-07-05 |
| kubeflow/examples | Jsonnet | 1,460 | 756 | 2026-07-05 |
| AustinCStone/TextGAN | Python | 92 | 30 | 2025-03-03 |
| migalkin/NodePiece | Python | 144 | 21 | 2026-05-07 |
| migalkin/StarE | Python | 89 | 16 | 2026-04-16 |
| migalkin/kgcourse2021 | HTML | 25 | 9 | 2026-02-16 |
| TeglonLabs/mathpix-gem | Ruby | 2 | 0 | 2026-01-01 |
| TeglonLabs/jank-crane | C++ | 0 | 0 | 2026-06-08 |

### Notable Activity (2026-07-05 sweep)

- **TeglonLabs/jank-crane** (pushed 2026-06-08): "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow" — C++
- **wasita/wasita.github.io** (pushed 2026-07-02): Svelte personal site, 8 open issues
- **kristinezheng/kristinezheng.github.io** (pushed 2026-07-01): HTML site, recently active
- **migalkin/RWL** (pushed 2026-05-28): Weisfeiler-Leman Go Relational (LOG 2022)
- **kubeflow/kubeflow** ★ grew from 15,565 → 15,761 (+196 since 2026-04-12 sweep)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, alice–Z)

**Result:** All 28 addresses returned `resource_not_found` for  
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger v6106750606.

None of the Hamming-swarm wallets hold an AptosCoin CoinStore on mainnet at this snapshot.  
All 28 balances recorded as `NULL` in `aptos_snapshots`.

### Multisig Contract Probes (5 pairs)

All probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f42... | **2** | ✅ |
| A-G | 0xf56c4a1... | **2** | ✅ |
| Y-Z | 0xd3ffe18... | **2** | ✅ |
| S-T | 0x3b1c3ae... | **2** | ✅ |
| V-W | 0x40fad7b... | **2** | ✅ |

All 5 multisig contracts are live and healthy. 2-of-N threshold across the board.

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — `testnet.mnx.fi` is protected by Vercel deployment authentication.  
API paths `/api/markets` and `/api/v1/markets` both return auth-gate. No market data extractable.  
`mnx_snapshots` table is empty this sweep.

---

## DuckDB Schema Summary

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

## DB Row Counts (2026-07-05)

```
world_increments    342 rows  (GF3 chain: ERGODIC=113, PLUS=115, MINUS=114)
repo_snapshots     1263 rows  (GitHub social graph snapshot)
aptos_snapshots      28 rows  (all NULL balance — resource_not_found)
multisig_probes       5 rows  (all healthy, 2 sigs required)
mnx_snapshots         0 rows  (auth-gated, unavailable)
```
